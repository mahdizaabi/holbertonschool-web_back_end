-- 5. Email validation to sent
-- a trigger to resets the attribute valid_email only when the email has been changed

DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(
    user_id INT, 
    project_name VARCHAR(255), 
    score FLOAT)
BEGIN
    DECLARE @project_id INT;
    IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0
    THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    SET @project_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
    INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, @project_id, score);
END
$$
DELIMITER ;
DELIMITER ;