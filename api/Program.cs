using Api.Entities;
using Api.Query;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", builder =>
    {
        builder.AllowAnyOrigin()
               .AllowAnyMethod()
               .AllowAnyHeader();
    });
});

var app = builder.Build();

app.MapGet("/news", async (ArticleQueryParams queryParams) =>
{
    return await Article.GetArticlesAsync(queryParams);
});

app.UseCors("AllowAll");

app.Run();
