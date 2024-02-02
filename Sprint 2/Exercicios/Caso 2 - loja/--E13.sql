--E13

select
    vendas.cdpro,
    vendas.nmcanalvendas,
    MAX(vendas.nmpro) as nmpro,
    SUM(vendas.qtd) as quantidade_vendas
from tbvendas as vendas
where vendas.status = 'Concluído' and (vendas.nmcanalvendas = 'Ecommerce' or vendas.nmcanalvendas = 'Matriz')
group by vendas.cdpro, vendas.nmcanalvendas
order by quantidade_vendas
limit 10