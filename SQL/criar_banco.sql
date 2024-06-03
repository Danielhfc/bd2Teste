--sqlacodegen --outfile mapeamento.py postgresql+psycopg2://postgres:1234@localhost:5432/ticketmaster
-- TABELAS --
CREATE TABLE classifications (
	genreId text PRIMARY KEY NOT NULL,
	genre text NOT NULL,
	segmentId text NOT NULL,
	segmentName text NOT NULL	
)

CREATE TABLE venues (
	id text PRIMARY KEY NOT NULL,
	name text NOT NULL,
	aliases text,
	url text,
	images text,
	postalCode text NOT NULL,
	timezone text NOT NULL,
	city text NOT NULL,
	state text NOT NULL,
	country text NOT NULL,
	address text,
	markets text
)

CREATE TABLE attractions (
	id text PRIMARY KEY NOT NULL,
	name text NOT NULL,
	url text,
	images text NOT NULL,
	classifications_id text,
    CONSTRAINT fk_classifications FOREIGN KEY (classifications_id) REFERENCES classifications(genreId)
)

CREATE TABLE events (
	id text PRIMARY KEY NOT NULL,
	name text NOT NULL,
	url text,
	images text,
	StartDateSale date,
	EndDateSale date,
	StartDateEvent date,
	timezone text,
	priceMin float,
	priceMax float,
	promoter text,
	venue_id text,
    classifications_id text,
	CONSTRAINT fk_venue FOREIGN KEY (venue_id) REFERENCES Venues(id),
    CONSTRAINT fk_classifications FOREIGN KEY (classifications_id) REFERENCES classifications(genreId)
)

SELECT * FROM Venues;
SELECT * FROM Events;
SELECT * FROM Classifications;
