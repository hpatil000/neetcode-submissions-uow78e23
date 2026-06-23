-- Write your query below

-- select name  
-- from customers
-- right join orders
-- on customers.id = orders.customer_id;

select name 
from customers
where id not In (select customer_id from orders);