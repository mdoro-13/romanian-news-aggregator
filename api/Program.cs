using Api.Entities;
using Api.Query;

WebApplicationBuilder builder = WebApplication.CreateBuilder(args);
ConfigurationManager config = builder.Configuration;

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

string connectionString = config.GetConnectionString("RomanianNewsAggregatorDb");

app.MapGet("/news", async (ArticleQueryParams queryParams) =>
{
    return await Article.GetArticlesAsync(queryParams, connectionString);
});

app.UseCors("AllowAll");

app.Run();
