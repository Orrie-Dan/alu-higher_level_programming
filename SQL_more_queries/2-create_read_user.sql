-- Check if the database exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Check if the user user_0d_2 exists and create the user with password if necessary
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the hbtn_0d_2 database to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;

