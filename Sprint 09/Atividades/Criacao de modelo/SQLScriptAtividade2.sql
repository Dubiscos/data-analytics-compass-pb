SELECT
    cli.nomeCliente,
    car.marcaCarro,
    car.modeloCarro,
    loc.dataLocacao,
    loc.dataEntrega,
    loc.qtdDiaria,
    loc.vlrDiaria
FROM
    fato_locacao loc
JOIN dim_cliente cli ON loc.idCliente = cli.idCliente
JOIN dim_carro car ON loc.idCarro = car.idCarro;
