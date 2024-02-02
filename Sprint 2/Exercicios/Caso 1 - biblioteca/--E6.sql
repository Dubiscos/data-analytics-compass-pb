--E6

select
    aut.codautor,
    aut.nome,
    COUNT(liv.cod) as quantidade_publicacoes
from autor as aut
left join livro as liv 
    on aut.codautor = liv.autor
group by aut.codautor, aut.nome
order by quantidade_publicacoes desc
limit 1