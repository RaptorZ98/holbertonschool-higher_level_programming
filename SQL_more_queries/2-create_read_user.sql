-- create and read user
CREATE DATABASE if NOT EXISTS hbtn_0d_2;
CREATE USER if NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
