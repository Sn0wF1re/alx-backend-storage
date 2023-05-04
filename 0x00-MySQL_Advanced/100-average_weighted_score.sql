-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER ^^ ;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id int)
BEGIN
	DECLARE weighted_av FLOAT;
	SET weighted_av = (SELECT SUM(score * weight) / SUM(weight)
			   FROM users AS U
			   JOIN corrections as C on C.user_id=U.id
			   JOIN projects AS P ON C.project_id=P.id
			   WHERE U.id=user_id);
	UPDATE users SET average_score=weighted_av WHERE id=user_id;
END;^^
