--E14

select
    vendas.estado,
    ROUND(AVG(vendas.qtd * vendas.vrunt), 2) as gastomedio
from tbvendas as vendas
where vendas.status = 'Concluído'
group by vendas.estado
order by gastomedio desc