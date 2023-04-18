CREATE TABLE Providers (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);

CREATE TABLE Articles (
    Id UUID PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Date TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    article_url VARCHAR(255) NOT NULL,
    picture_url VARCHAR(255) NOT NULL,
    Provider INT REFERENCES Providers(Id) NOT NULL
);

INSERT INTO Providers (Name) VALUES
    ('profit.ro'),
    ('hotnews'),
    ('g4media'),
    ('digi24'),
    ('mediafax');
