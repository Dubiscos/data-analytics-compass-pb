--E3

select 
   count(*) as quantidade,
   edi.nome,
   ende.estado,
   ende.cidade
from livro
left join editora as edi
    on livro.editora = edi.codeditora
left join endereco as ende
    on edi.endereco = ende.codendereco
group by edi.nome, ende.estado, ende.cidade
order by quantidade desc
limit 5
