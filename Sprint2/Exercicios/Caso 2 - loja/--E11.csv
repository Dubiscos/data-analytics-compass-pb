--E11

select 
    vendas.cdcli, 
    vendas.nmcli, 
    SUM(vendas.qtd * vendas.vrunt) as gasto
from tbvendas as vendas
where vendas.status = 'Concluído'
group by vendas.cdcli, vendas.nmcli
order by gasto desc
limit 1
