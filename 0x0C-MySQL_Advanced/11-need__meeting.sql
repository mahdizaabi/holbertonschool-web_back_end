-- 11. No table for a meeting
-- creates a view need_meeting
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS 
SELECT name FROM students 
WHERE 
    score < 80 AND 
    (last_meeting IS NULL 
        OR 
    last_meeting < ADDDATE(CURDATE(), interval -1 MONTH));