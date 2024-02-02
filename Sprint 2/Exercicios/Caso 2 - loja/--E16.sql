--E16

select
    vendas.estado,
    MAX(vendas.nmpro) as nmpro,
    ROUND(AVG(vendas.qtd), 4) as quantidade_media
from tbvendas as vendas
where vendas.status = 'Concluído'
group by vendas.estado, vendas.cdpro
order by vendas.estado, nmpro