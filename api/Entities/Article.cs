using Api.Query;
using Api.Repository;

namespace Api.Entities;

public class Article
{
    public Guid Id { get; set; }
    public string Title { get; set; }
    public DateTime Date { get; set; }
    public DateTime ScrapeDate { get; set; }
    public string ArticleUrl { get; set; }
    public string PictureUrl { get; set; }
    public string Provider { get; set; }

    public static async Task<ICollection<Article>> GetArticlesAsync(ArticleQueryParams articleQueryParams, string connectionString)
    {
        var repository = new ArticleRepository(connectionString);
        return await repository.GetArticlesAsync(articleQueryParams);
    }
}