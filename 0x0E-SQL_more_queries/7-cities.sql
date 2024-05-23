-- Create the database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,
        name VARCHAR(256) NOT NULL,
	    PRIMARY KEY (id)
	    );
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,
        state_id INT NOT NULL,
	    name VARCHAR(256) NOT NULL,
	        PRIMARY KEY (id),
		    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
		    );
		    
