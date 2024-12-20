--E10

select
    vendedor.nmvdd as vendedor,
    SUM(vendas.qtd * vendas.vrunt) as valor_total_vendas,
    ROUND(SUM(vendas.qtd * vendas.vrunt) * (vendedor.perccomissao) / 100, 2) as comissao
from tbvendedor as vendedor
left join tbvendas as vendas
    on vendedor.cdvdd = vendas.cdvdd and vendas.status = 'Concluído'
group by vendedor.cdvdd, vendedor.nmvdd
order by comissao desc
