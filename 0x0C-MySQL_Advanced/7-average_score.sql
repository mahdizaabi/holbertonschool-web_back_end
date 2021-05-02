-- 5. Email validation to sent
-- a trigger to resets the attribute valid_email only when the email has been changed

DROP PROCEDURE IF EXISTS computeAverageScoreForUser;
DELIMITER $$


CREATE PROCEDURE computeAverageScoreForUser(user_id INT)

BEGIN
    SET @average = (
    SELECT AVG(score) 
    from corrections c
    where c.user_id = user_id);
    UPDATE users SET average_score = @average WHERE id = user_id;

END $$
DELIMITER ;
