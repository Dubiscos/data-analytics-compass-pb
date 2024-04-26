CREATE TABLE Cliente (
	idCLiente INT PRIMARY KEY,
	nomeCliente VARCHAR,
	cidadeCliente VARCHAR,
	estadoCliente VARCHAR,
	paisCliente VARCHAR	
);
CREATE TABLE Vendedor (
	idVendedor INT PRIMARY KEY,
	nomeVendedor VARCHAR,
	sexoVendedor SMALLINT,
	estadoVendedor VARCHAR
);
CREATE TABLE Carro (
	idCarro INT PRIMARY KEY,
	kmCarro INT,
	classiCarro VARCHAR,
	marcaCarro VARCHAR,
	modeloCarro VARCHAR,
	anoCarro INT,
	idcombustivel INT,
	FOREIGN KEY (idcombustivel) REFERENCES Combustivel (idcombustivel)
);
CREATE TABLE Combustivel (
	idcombustivel INT PRIMARY KEY,
	tipoCombustivel VARCHAR
);
CREATE TABLE Locacao(
	idLocacao INT PRIMARY KEY,
	idCliente INT,
	idCarro INT,
	dataLocacao DATETIME,
	horaLocacao TIME,
	qtdDiaria INT,
	vlrDiaria DECIMAL,
	dataEntrega DATE,
	horaEntrega TIME,
	idVendedor INT,
	FOREIGN KEY (idCliente) REFERENCES Cliente(idCLiente),
	FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
	FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
);
INSERT INTO Locacao (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor)
SELECT idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor
FROM tb_locacao;
INSERT INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao AS l
WHERE idVendedor NOT IN (SELECT idVendedor FROM Vendedor)
GROUP BY idVendedor;
INSERT INTO Combustivel  (idcombustivel, tipoCombustivel)
SELECT idcombustivel, tipoCombustivel
FROM tb_locacao AS l
WHERE idcombustivel  NOT IN (SELECT idcombustivel FROM Combustivel)
GROUP BY idcombustivel;
INSERT INTO Cliente (idCLiente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT idCLiente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao AS l
WHERE idCLiente  NOT IN (SELECT idCLiente  FROM Cliente)
GROUP BY idCLiente;
INSERT INTO Carro  (idCarro , kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel)
SELECT idCarro , kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel
FROM tb_locacao AS l
WHERE idCarro  NOT IN (SELECT idCarro FROM Carro)
GROUP BY idCarro;