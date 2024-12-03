CREATE DATABASE student_network;

USE student_network;

-- Create Users Table
CREATE TABLE 'tsn_data'.'user data' (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Create Requests Table
CREATE TABLE requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    request_message TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
