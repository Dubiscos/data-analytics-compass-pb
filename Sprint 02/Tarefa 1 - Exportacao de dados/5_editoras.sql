--5 editoras

select
    edi.codeditora as CodEditora,
    edi.nome as NomeEditora,
    COUNT(liv.cod) as QuantidadeLivros
from editora as edi
left join livro as liv
    ON edi.codeditora = liv.editora
group by edi.codeditora, edi.nome
order by QuantidadeLivros desc
limit 5