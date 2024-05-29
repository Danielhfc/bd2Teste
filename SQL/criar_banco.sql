sqlacodegen --outfile mapeamento.py postgresql+psycopg2://postgres:1234@localhost:5432/ticketmaster
-- TABELAS --
CREATE TABLE classificacao (
	id text PRIMARY KEY NOT NULL,
	nome text NOT NULL,
	genero text NOT NULL,
	generoid text NOT NULL,
	subGenero text,
	subGeneroid text
)

CREATE TABLE locais (
	id text PRIMARY KEY NOT NULL,
	nome text NOT NULL,
	codigoURL text,
	imagens text NOT NULL,
	codigoPostal text NOT NULL,
	timezone text NOT NULL,
	cidade text NOT NULL,
	estado text NOT NULL,
	pais text NOT NULL,
	proximosEventos text NOT NULL
)

CREATE TABLE eventos (
	id text PRIMARY KEY NOT NULL,
	nome text NOT NULL,
	codigoURL text,
	imagens text NOT NULL,
	inicioVenda date NOT NULL,
	fimVenda date NOT NULL,
	inicioEvento date NOT NULL,
	fimEvento date NOT NULL,
	preco float NOT NULL,
	local_id text,
    classificacao_id text,
	CONSTRAINT fk_local FOREIGN KEY (local_id) REFERENCES locais(id),
    CONSTRAINT fk_classificacao FOREIGN KEY (classificacao_id) REFERENCES classificacao(id)
)

CREATE TABLE atracoes (
	id text PRIMARY KEY NOT NULL,
	nome text NOT NULL,
	codigoURL text,
	imagens text NOT NULL,
	proximosEventos text NOT NULL,
	classificacao_id text,
    evento_id text,
    CONSTRAINT fk_classificacao FOREIGN KEY (classificacao_id) REFERENCES classificacao(id),
    CONSTRAINT fk_evento FOREIGN KEY (evento_id) REFERENCES eventos(id)
)