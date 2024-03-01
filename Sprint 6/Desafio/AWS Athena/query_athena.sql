with nomes_decada as (
    select
        nome,
        (ano - (ano % 10)) as decada_inicio,
        sum(total) as total_decada
    from nomes
    where ano >= 1950
    group by nome, (ano - (ano % 10))
),
rank_nomes as (
    select
        nome,
        decada_inicio,
        total_decada,
        row_number() over(partition by decada_inicio order by total_decada desc) as rank
    from nomes_decada
)
select
    nome,
    decada_inicio as decada,
    total_decada,
    rank
from rank_nomes
where rank <= 3
order by
    decada_inicio,
    rank;