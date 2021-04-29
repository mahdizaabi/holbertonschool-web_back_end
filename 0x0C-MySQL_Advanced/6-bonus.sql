-- 5. Email validation to sent
-- a trigger to resets the attribute valid_email only when the email has been changed

DELIMITER !!
CREATE PROCEDURE AddBonus
(
    user_id int,
    project_name varchar(255),
    score float
)

BEGIN
    IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0
    THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
     SET project_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_name, score);
END!!
DELIMITER ;