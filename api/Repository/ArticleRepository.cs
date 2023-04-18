using Api.Entities;
using Api.Query;
using Npgsql;

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
            using (var command = new NpgsqlCommand())
            {
                command.Connection = connection;
                command.CommandText = "SELECT a.id, a.title, a.date, a.scrape_date, a.article_url, a.picture_url, a.provider_id " +
                                      "FROM articles a ";

                if (queryParams.ProviderIds is not null && queryParams.ProviderIds.Any())
                {
                    var providerIdsParameter = string.Join(",", Enumerable.Range(0, queryParams.ProviderIds.Count).Select(i => "@ProviderId" + i));
                    command.CommandText += "WHERE a.provider_id IN (" + providerIdsParameter + ") ";
                    for (int i = 0; i < queryParams.ProviderIds.Count; i++)
                    {
                        command.Parameters.AddWithValue("ProviderId" + i, queryParams.ProviderIds.ElementAt(i));
                    }
                }

                if (!string.IsNullOrWhiteSpace(queryParams.Keyword))
                {
                    command.CommandText += queryParams.ProviderIds is not null && queryParams.ProviderIds.Any() ? "AND " : "WHERE ";
                    command.CommandText += "a.title LIKE @Keyword ";
                    command.Parameters.AddWithValue("Keyword", "%" + queryParams.Keyword + "%");
                }

                command.CommandText += "ORDER BY a.date DESC";

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
                            ProviderId = reader.GetInt32(6)
                        });
                    }
                }

                return articles;
            }
        }
    }
}
