-- creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student

DELIMITER %% ;
CREATE PROCEDURE computeAverageScoreForUser(IN user_id int)
BEGIN
	DECLARE avgScore float;
	SET avgScore = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id);
	UPDATE users SET average_score = avgScore WHERE id = user_id;
END;%%
