using Api.Entities;
using Api.Query;
using Npgsql;
using System.Diagnostics;
using static Api.Query.ArticleQueryParams;

namespace Api.Repository;

public class ArticleRepository
{
    private readonly string connectionString;

    public ArticleRepository()
    {
    }

    public ArticleRepository(string connectionString)
    {
        this.connectionString = connectionString;
    }

    public async Task<List<Article>> GetArticlesAsync(ArticleQueryParams queryParams)
    {
        using (var connection = new NpgsqlConnection(connectionString))
        {
            await connection.OpenAsync();

            var command = CreateCommand(connection, queryParams);

            var articles = await ReadArticlesAsync(command);

            return articles;
        }
    }

    private NpgsqlCommand CreateCommand(NpgsqlConnection connection, ArticleQueryParams queryParams)
    {
        var command = new NpgsqlCommand();
        command.Connection = connection;
        command.CommandText = "SELECT a.id, a.title, a.date, a.scrape_date, a.article_url, a.picture_url, p.name as provider_name " +
                              "FROM articles a " +
                              "JOIN providers p ON a.provider_id = p.id ";

        if (queryParams.ProviderIds is not null && queryParams.ProviderIds.Any())
        {
            FilterByProvider(queryParams, command);
        }

        if (!string.IsNullOrWhiteSpace(queryParams.Keyword))
        {
            FilterByKeyword(queryParams, command);
        }

        FilterByLowerThanDate(queryParams, command);
        OrderByDateDescending(command);
        LimitByCount(queryParams, command);

        Console.WriteLine(command.CommandText);
        return command;
    }

    private static void FilterByProvider(ArticleQueryParams queryParams, NpgsqlCommand command)
    {
        var providerIdsParameter = string.Join(",", Enumerable.Range(0, queryParams.ProviderIds.Count).Select(i => "@ProviderId" + i));
        command.CommandText += "WHERE a.provider_id IN (" + providerIdsParameter + ") ";
        for (int i = 0; i < queryParams.ProviderIds.Count; i++)
        {
            command.Parameters.AddWithValue("ProviderId" + i, queryParams.ProviderIds.ElementAt(i));
        }
    }
    private static void FilterByKeyword(ArticleQueryParams queryParams, NpgsqlCommand command)
    {
        command.CommandText += queryParams.ProviderIds is not null && queryParams.ProviderIds.Any() ? "AND " : "WHERE ";
        command.CommandText += "a.title LIKE @Keyword ";
        command.Parameters.AddWithValue("Keyword", "%" + queryParams.Keyword + "%");
    }

    private static void FilterByLowerThanDate(ArticleQueryParams queryParams, NpgsqlCommand command)
    {
        bool validDate = DateTime.TryParse(queryParams.DatePosted, out var date);

        if (validDate)
        {
            string commandText = queryParams.IsScrollDown ? "AND a.date < @DatePosted " : "AND a.date > @DatePosted ";
            command.CommandText += commandText;
            command.Parameters.AddWithValue("DatePosted", date);
        }
    }
    private static void OrderByDateDescending(NpgsqlCommand command)
    {
        command.CommandText += "ORDER BY a.date DESC ";
    }
    private static void LimitByCount(ArticleQueryParams queryParams, NpgsqlCommand command)
    {
        command.CommandText += "LIMIT @Count ";
        command.Parameters.AddWithValue("Count", queryParams.Count);
    }

    private async Task<List<Article>> ReadArticlesAsync(NpgsqlCommand command)
    {
        var articles = new List<Article>();

        using (var reader = await command.ExecuteReaderAsync())
        {
            while (await reader.ReadAsync())
            {
                articles.Add(new Article
                {
                    Id = reader.GetGuid(0),
                    Title = reader.GetString(1),
                    Date = reader.GetDateTime(2),
                    ScrapeDate = reader.GetDateTime(3),
                    ArticleUrl = reader.GetString(4),
                    PictureUrl = reader.GetString(5),
                    Provider = reader.GetString(6)
                });
            }
        }

        return articles;
    }
}
