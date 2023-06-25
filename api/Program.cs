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

string? connectionString = config["ROMANIAN_NEWS_AGGREGATOR_CONNECTION_STRING"] ?? 
                           throw new InvalidOperationException("No connection string has been configured");

app.MapGet("/news", async (ArticleQueryParams queryParams) =>
{
    return await Article.GetArticlesAsync(queryParams, connectionString);
});

app.UseCors("AllowAll");

app.Run();