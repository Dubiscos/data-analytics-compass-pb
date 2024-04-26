--E4

select 
    aut.nome,
    aut.codautor,
    aut.nascimento, 
    count(liv.cod) as quantidade
from autor as aut
left join livro as liv
    on aut.codautor = liv.autor
group by aut.nome, aut.codautor, aut.nascimento
order by aut.nome
