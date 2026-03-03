--!!! DON"T TOUCH UNLESS ABSOLUTELY NECESSARY"""!!!!

CREATE USER bookapp WITH ENCRYPTED PASSWORD 'BookApp';
GRANT USAGE,CREATE ON SCHEMA public TO bookapp; -- This allows USAGE(SELECT INSERT (Table level) and CREATE (Create Table etc))

CREATE DATABASE bookly_db -- Create database for our backend
