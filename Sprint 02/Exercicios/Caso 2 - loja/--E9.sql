--E9

select cdpro, nmpro
from tbvendas
where dtven between '2014-02-03' and '2018-02-02'
group by cdpro, nmpro
order by status desc
limit 1
