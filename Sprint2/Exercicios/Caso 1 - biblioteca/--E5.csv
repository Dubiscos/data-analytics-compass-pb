--E5

select aut.nome
from autor as aut
left join livro as liv
    on aut.codautor = liv.autor
left join editora as edi
    on liv.editora = edi.codeditora
left join endereco as ende
    on edi.endereco = ende.codendereco
where ende.estado not in ('PARANÁ', 'RIO GRANDE DO SUL')
group by aut.nome
order by aut.nome
