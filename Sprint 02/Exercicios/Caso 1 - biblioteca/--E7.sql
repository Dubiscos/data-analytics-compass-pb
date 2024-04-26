--E7

select aut.nome
from autor as  aut
left join livro as liv
    on aut.codautor = liv.autor
where liv.cod is NULL
order by aut.nome
