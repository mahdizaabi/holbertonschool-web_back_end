-- 5. Email validation to sent
-- a trigger to resets the attribute valid_email only when the email has been changed

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$


CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()

BEGIN
    DECLARE n INT DEFAULT 0;
    DECLARE i INT DEFAULT 0;
    SELECT COUNT(*) FROM users INTO n;
    SET i=0;
WHILE i<n DO 
    SET @avgWeighted = (SELECT SUM(score * weight) / SUM(weight) 
    FROM projects 
    LEFT JOIN corrections 
    ON corrections.project_id = projects.id
    WHERE (SELECT id FROM users  LIMIT i,1));
    UPDATE users
    SET average_score = @avgWeighted WHERE id = (SELECT id FROM users  LIMIT i,1); 
    SET i = i + 1;
END WHILE;
END $$
DELIMITER ;
