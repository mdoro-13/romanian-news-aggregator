
# Romanian News Aggregator

A small project which consists of a web page displaying news from various Romanian sites. For now, it supports infinite scrolling as well as the possibility to search for articles. 

The articles are stored in a database, so it doesn't only show today's articles.


## How to run
* git clone the repo
* run the serve_locally.sh bash script

## Details
A cron job executes the web scrapers every two minutes and inserts new articles into a Postgres database. The articles are served using an ASP.NET web api. These components have been dockeriezed so that the setup can be run easily. 

For the UI, I used plain HTML, CSS and JS. I tried to minimize the use of libraries and frameworks because the project is quite small. If somehow it grows in complexity, I may switch to Entity Framework and use a frontend framework.

## Further info
I will deploy this in the future to show it as a demo more easily only if I find a way to do so free of charge.

![Alt text](https://i.ibb.co/yhjS8Gg/news-aggregator.png "a title")
