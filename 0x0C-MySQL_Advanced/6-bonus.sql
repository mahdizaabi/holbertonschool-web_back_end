-- 5. Email validation to sent
-- a trigger to resets the attribute valid_email only when the email has been changed

DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$


CREATE PROCEDURE Addbonus(user_id INT, project_name VARCHAR(255), score INT)

BEGIN
    IF EXISTS(SELECT * from projects WHERE name =project_name) = 0 THEN
        INSERT into projects (name) values(project_name);
        SET @NewInsertedProject = LAST_INSERT_ID();
    ELSE
        set @NewInsertedProject = SELECT * from projects where (name = project_name);
    END IF;

    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, @NewInsertedProject, score);
END $$
DELIMITER ;
