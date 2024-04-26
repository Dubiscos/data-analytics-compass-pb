--E8

select 
    vendedor.cdvdd, 
    vendedor.nmvdd
from tbvendedor as vendedor
left join tbvendas as vendas
    on vendedor.cdvdd = vendas.cdvdd
where vendas.status = 'Concluído'
group by vendedor.cdvdd, vendedor.nmvdd
order by count(vendas.cdvdd) desc
limit 1
