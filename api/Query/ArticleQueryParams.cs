using System.Reflection;

namespace Api.Query;

public class ArticleQueryParams
{
    public ICollection<int> ProviderIds { get; set; }
    public string Keyword { get; set; }

    public static async ValueTask<ArticleQueryParams?> BindAsync(HttpContext context, ParameterInfo parameter)
    {
        string keyword = context.Request.Query["Keyword"];
        var providerIdsStringVals = context.Request.Query["providerIds"];

        if (providerIdsStringVals.Count == 0)
        {
            return new ArticleQueryParams
            {
                Keyword = keyword
            };
        }

        var providerIds = providerIdsStringVals.ToString()?.Split(',').Select(int.Parse).ToList();
        var result = new ArticleQueryParams
        {
            Keyword = keyword,
            ProviderIds = providerIds
        };
        return await ValueTask.FromResult<ArticleQueryParams?>(result);
    }
}
