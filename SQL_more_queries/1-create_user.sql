-- Check if user user_0d_1 exists
SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost') INTO @user_exists;

-- If the user does not exist, create the user
IF @user_exists = 0 THEN
    -- Output that user doesn't exist
    SELECT 'user_0d_1 doesn''t exist';

    -- Create the user
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
    
    -- Grant all privileges to user_0d_1 on all databases
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
    
    -- Apply the changes
    FLUSH PRIVILEGES;
ELSE
    -- Output that user exists
    SELECT 'user_0d_1 exists';
    
    -- Grant all privileges to the existing user
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
    
    -- Apply the changes
    FLUSH PRIVILEGES;
END IF;

