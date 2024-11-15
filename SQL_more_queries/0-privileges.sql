-- List specific privileges for user_0d_1 on user_2_db
SHOW GRANTS FOR 'user_0d_1'@'localhost' 
  LIKE '%user_2_db%';

-- List specific privileges for user_0d_2 on user_2_db
SHOW GRANTS FOR 'user_0d_2'@'localhost' 
  LIKE '%user_2_db%';

