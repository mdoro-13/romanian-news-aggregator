CREATE TABLE IF NOT EXISTS Providers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Articles (
    id UUID PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    date TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    scrape_date TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    article_url VARCHAR(255) NOT NULL,
    picture_url VARCHAR(255) NOT NULL,
    provider_id INT REFERENCES Providers(Id) NOT NULL,
    UNIQUE (Title, article_url)
);

INSERT INTO Providers (Name) VALUES
    ('profit.ro'),
    ('hotnews'),
    ('g4media'),
    ('digi24'),
    ('mediafax')
    ON CONFLICT (Name) DO NOTHING;
