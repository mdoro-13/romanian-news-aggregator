using System.Reflection;
using static Api.Query.ArticleQueryParams;

namespace Api.Query;

public class ArticleQueryParams
{
    public ICollection<int> ProviderIds { get; init; }
    public string Keyword { get; init; }
    public ScrollDirection Direction { get; init; }
    public string DatePosted { get; init; }
    public int Count { get; init; } = 100;

    public static async ValueTask<ArticleQueryParams?> BindAsync(HttpContext context, ParameterInfo parameter)
    {
        string keyword = context.Request.Query["Keyword"];
        string beforeDate = context.Request.Query["DatePosted"];
        string stringScrollDirection = context.Request.Query["Direction"];
        var providerIdsStringVals = context.Request.Query["providerIds"];

        ScrollDirection scrollDirection = (ScrollDirection)Int32.Parse(stringScrollDirection);

        if (providerIdsStringVals.Count == 0)
        {
            return new ArticleQueryParams
            {
                Keyword = keyword,
                DatePosted = beforeDate,
                Direction = scrollDirection
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
            Direction = scrollDirection
        };

        return await ValueTask.FromResult<ArticleQueryParams?>(result);
    }

    public enum ScrollDirection
    {
        Down = 0,
        Up = 1,
    }
}
