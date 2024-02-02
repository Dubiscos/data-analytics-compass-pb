--10_livros_mais_caros

select
    cod,
    titulo,
    autor,
    editora,
    valor,
    publicacao,
    edicao,
    idioma
from livro
order by valor desc
limit 10