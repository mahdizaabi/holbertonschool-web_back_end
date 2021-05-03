-- 12. Average weighted score
-- creates a stored procedure ComputeAverageWeightedScoreForUser to store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    user_id INT
)
BEGIN
    DECLARE WeightAverageScore FLOAT;
    SET WeightAverageScore = (SELECT SUM(score * weight) / SUM(weight) 
    FROM users AS U 
    JOIN corrections as C ON U.id=C.user_id 
    JOIN projects AS P ON C.project_id=P.id 
    WHERE U.id=user_id);
    UPDATE users
    SET average_score = WeightAverageScore WHERE id=user_id;
END
$$
DELIMITER ;