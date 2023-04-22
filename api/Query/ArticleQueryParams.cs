using System.Reflection;
using static Api.Query.ArticleQueryParams;

namespace Api.Query;

public class ArticleQueryParams
{
    public ICollection<int> ProviderIds { get; init; }
    public string Keyword { get; init; }
    public bool IsScrollDown { get; init; } = true;
    public string DatePosted { get; init; }
    public int Count { get; init; } = 100;

    public static async ValueTask<ArticleQueryParams?> BindAsync(HttpContext context, ParameterInfo parameter)
    {
        string keyword = context.Request.Query["Keyword"];
        string beforeDate = context.Request.Query["DatePosted"];
        string isScrollDownString = context.Request.Query["IsScrollDown"];
        var providerIdsStringVals = context.Request.Query["providerIds"];

        bool isScrollValid = bool.TryParse(isScrollDownString, out bool parsedIsScrollDown);
        bool isScrollDownResult = isScrollValid ? parsedIsScrollDown : true;

        if (providerIdsStringVals.Count == 0)
        {
            return new ArticleQueryParams
            {
                Keyword = keyword,
                DatePosted = beforeDate,
                IsScrollDown = isScrollDownResult
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
            IsScrollDown = isScrollDownResult
        };

        return await ValueTask.FromResult<ArticleQueryParams?>(result);
    }

    public enum ScrollDirection
    {
        Down = 0,
        Up = 1,
    }
}
