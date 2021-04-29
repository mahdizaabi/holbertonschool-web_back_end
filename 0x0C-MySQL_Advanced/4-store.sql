-- SQL script that creates a table users
-- In and not out


DELIMITER $$

CREATE TRIGGER decrease_after_insert
    AFTER INSERT ON orders 
    FOR EACH ROW 
BEGIN
    UPDATE items 
    SET quantity = quantity - NEW.number 
    WHERE name  = NEW.item_name;
END $$

DELIMITER ;