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
    public int ProviderId { get; set; }

    public static async Task<ICollection<Article>> GetArticlesAsync(ArticleQueryParams articleQueryParams)
    {
        var repository = new ArticleRepository("Server=localhost;Database=NewsDb;Port=5432;Username=postgres;Password=sqladmin");
        return await repository.GetArticlesAsync(articleQueryParams);
    }
}
