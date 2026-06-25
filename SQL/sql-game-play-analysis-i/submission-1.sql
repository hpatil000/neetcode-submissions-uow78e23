-- Write your query below
select player_id, min(event_date) as first_login
From activity
group by player_id
order by player_id ASC;
