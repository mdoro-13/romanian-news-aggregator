CREATE TABLE IF NOT EXISTS Providers (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Articles (
    Id UUID PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Date TIMESTAMP WITHOUT TIME ZONE NOT NULL,
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
