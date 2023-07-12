using System.Collections.ObjectModel;
using System.Reflection;
using Microsoft.Extensions.Primitives;

namespace Api.Query;

public class ArticleQueryParams
{
    public IEnumerable<int> ProviderIds { get; init; } = Enumerable.Empty<int>();
    public string? Keyword { get; init; }
    public string? BeforeDate { get; init; }
    public int Count { get; init; } = 120;

    public static async ValueTask<ArticleQueryParams?> BindAsync(HttpContext context, ParameterInfo parameter)
    {
        string? keyword = context.Request.Query["Keyword"];
        string? datePosted = context.Request.Query["BeforeDate"];
        StringValues providerIdsStringVals = context.Request.Query["providerIds"];

        if (providerIdsStringVals.Count == 0)
        {
            return new ArticleQueryParams
            {
                Keyword = keyword,
                BeforeDate = datePosted,
            };
        }

        List<int> providerIds = providerIdsStringVals.ToString()?
            .Split(',')
            .Select(int.Parse)
            .ToList()!;

        ArticleQueryParams result = new()
        {
            Keyword = keyword,
            ProviderIds = providerIds,
            BeforeDate = datePosted,
        };

        return await ValueTask.FromResult<ArticleQueryParams?>(result);
    }
}