-- 5. Email validation to sent
-- a trigger to resets the attribute valid_email only when the email has been changed

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$


CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)

BEGIN
    SET @avgWeighted = (SELECT SUM(score * weight) / SUM(weight) 
    FROM projects 
    LEFT JOIN corrections 
    ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id);
    UPDATE users
    SET average_score = @avgWeighted WHERE id=user_id;
END $$
DELIMITER ;
