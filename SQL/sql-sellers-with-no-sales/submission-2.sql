-- Write your query below
-- with cte as (select seller.seller_name, seller.seller_id, cast(orders.sale_date as DATE) 
-- from seller
-- left join orders
-- on seller.seller_id = orders.seller_id
-- -- where  sale_date Not (sale_date < '2020-1-1' and sale_date > '2020-12-31')
-- WHERE NOT (
--     sale_date >= '2020-01-01'
--     AND sale_date <= '2020-12-31'
-- )
-- )

-- select seller_name from cte;

SELECT s.seller_name
FROM seller s
LEFT JOIN orders o
  ON s.seller_id = o.seller_id
 AND o.sale_date >= '2020-01-01'
 AND o.sale_date < '2021-01-01'
WHERE o.seller_id IS NULL
ORDER BY s.seller_name ASC;

