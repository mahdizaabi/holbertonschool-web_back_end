-- SQL script that creates a table users
-- In and not out


DELIMITER $$

CREATE TRIGGER decrease_after_insert
    AFTER UPDATE ON users 
    FOR EACH ROW 
BEGIN
    UPDATE users 
    SET valid_email  = 
    CASE WHEN valid_email = 0 THEN 1
    ELSE 0
END
    WHERE id  = NEW.id;
END $$

DELIMITER ;