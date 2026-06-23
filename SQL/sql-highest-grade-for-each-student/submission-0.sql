-- Write your query below
-- 

select student_id, exam_id, score
    from (select student_id, exam_id, score,
            Row_number() over(partition by student_id order by score DESC , exam_id ASC) as ranking 
            from exam_results
        ) t
    where ranking = 1;
































-- select distinct on (student_id)
-- --     student_id,
-- --     exam_id, 
-- --     score
-- -- from exam_results
-- -- order by student_id, score DESC, exam_id; 









