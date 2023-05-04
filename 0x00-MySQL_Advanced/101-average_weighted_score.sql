-- creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for a student

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER ^^ ;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users as U,
	  (SELECT U.id, SUM(score * weight) / SUM(weight) AS weighted_av
	  FROM users AS U
	  JOIN corrections as C on C.user_id=U.id
	  JOIN projects AS P ON C.project_id=P.id
	  GROUP BY U.id) AS AVS
	SET U.average_score=AVS.weighted_av WHERE U.id = AVS.id;
END;^^
