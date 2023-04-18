using Api.Entities;
using Api.Query;
using Microsoft.AspNetCore.Mvc;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/news", async (ArticleQueryParams queryParams) =>
{

    //ArticleQueryParams queryParams = new()
    //{
    //    Keyword = keyword,
    //    ProviderIds = providerIDs
    //};

    return await Article.GetArticlesAsync(queryParams);
});

app.Run();
