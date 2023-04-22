using System.Reflection;
using static Api.Query.ArticleQueryParams;

namespace Api.Query;

public class ArticleQueryParams
{
    public ICollection<int> ProviderIds { get; init; }
    public string Keyword { get; init; }
    public bool IsScrollDown { get; init; }
    public string DatePosted { get; init; }
    public int Count { get; init; } = 100;

    public static async ValueTask<ArticleQueryParams?> BindAsync(HttpContext context, ParameterInfo parameter)
    {
        string keyword = context.Request.Query["Keyword"];
        string beforeDate = context.Request.Query["DatePosted"];
        string stringScrollCheck = context.Request.Query["IsScrollDown"];
        var providerIdsStringVals = context.Request.Query["providerIds"];

        bool isScrollDown = bool.Parse(stringScrollCheck);

        if (providerIdsStringVals.Count == 0)
        {
            return new ArticleQueryParams
            {
                Keyword = keyword,
                DatePosted = beforeDate,
                IsScrollDown = isScrollDown
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
            DatePosted = beforeDate,
            IsScrollDown = isScrollDown
        };

        return await ValueTask.FromResult<ArticleQueryParams?>(result);
    }

    public enum ScrollDirection
    {
        Down = 0,
        Up = 1,
    }
}
