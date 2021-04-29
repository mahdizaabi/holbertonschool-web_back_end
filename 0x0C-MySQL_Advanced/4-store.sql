-- SQL script that creates a table users
-- In and not out


DELIMITER $$

CREATE TRIGGER decrease_after_insert
    AFTER INSERT ON orders 
    FOR EACH ROW 
BEGIN
    UPDATE items 
    SET quantity = quantity - 1
    WHERE item_name = NEW.name 
END $$

DELIMITER;