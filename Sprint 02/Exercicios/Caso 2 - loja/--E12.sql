--E12

select 
    depen.cddep, 
    depen.nmdep, 
    depen.dtnasc,
    SUM(vendas.qtd * vendas.vrunt) as valor_total_vendas
from tbdependente as depen
left join tbvendas as vendas
    on depen.cdvdd = vendas.cdvdd and vendas.status = 'Concluído'
group by depen.cdvdd, depen.nmdep
order by valor_total_vendas
limit 1
