using System.Reflection;
using static Api.Query.ArticleQueryParams;

namespace Api.Query;

public class ArticleQueryParams
{
    public ICollection<int> ProviderIds { get; init; }
    public string Keyword { get; init; }
    public string BeforeDate { get; init; }
    public int Count { get; init; } = 50;

    public static async ValueTask<ArticleQueryParams?> BindAsync(HttpContext context, ParameterInfo parameter)
    {
        string keyword = context.Request.Query["Keyword"];
        string datePosted = context.Request.Query["BeforeDate"];
        var providerIdsStringVals = context.Request.Query["providerIds"];

        if (providerIdsStringVals.Count == 0)
        {
            return new ArticleQueryParams
            {
                Keyword = keyword,
                BeforeDate = datePosted,
            };
        }

        var providerIds = providerIdsStringVals.ToString()?
            .Split(',')
            .Select(int.Parse)
            .ToList();

        var result = new ArticleQueryParams
        {
            Keyword = keyword,
            ProviderIds = providerIds,
            BeforeDate = datePosted,
        };

        return await ValueTask.FromResult<ArticleQueryParams?>(result);
    }
}
