-- -- Write your query below
-- with abc as (
--                 select name as company_name, sales_id
--                 from company 
--                 left join orders 
--                 on company.com_id = orders.com_id
--                 order by orders.sales_id asc
-- )
-- select name from
-- sales_person 
-- left join abc
-- on sales_person.sales_id = abc.sales_id
-- where abc.company_name NOT LIKE '%CRIMSON%'
-- order by sales_person.name ASC;


select sp.name
from sales_person sp
where sp.sales_id NOT IN (
    select o.sales_id
    from orders o 
    left join company c
    on o.com_id = c.com_id
    where c.name = 'CRIMSON'

);

