-- Create the database
CREATE DATABASE newfeed;

-- Use the created database
USE newfeed;

-- Create the user table
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

-- Create the post table
CREATE TABLE post (
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_by INT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES user(id)
);

-- Create the comment table
CREATE TABLE comment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_by INT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    post_id INT NOT NULL,
    FOREIGN KEY (created_by) REFERENCES user(id),
    FOREIGN KEY (post_id) REFERENCES post(id)
);

-- Create the like table
CREATE TABLE `like` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_by INT NOT NULL,
    post_id INT,
    comment_id INT,
    FOREIGN KEY (created_by) REFERENCES user(id),
    FOREIGN KEY (post_id) REFERENCES post(id),
    FOREIGN KEY (comment_id) REFERENCES comment(id),
    CHECK (post_id IS NOT NULL OR comment_id IS NOT NULL)
);

-- Create the follow table
CREATE TABLE follow (
    id INT AUTO_INCREMENT PRIMARY KEY,
    following INT NOT NULL,
    followed INT NOT NULL,
    FOREIGN KEY (following) REFERENCES user(id),
    FOREIGN KEY (followed) REFERENCES user(id)
);

-- Create the share table
CREATE TABLE share (
    id INT AUTO_INCREMENT PRIMARY KEY,
    post_id INT NOT NULL,
    created_by INT NOT NULL,
    FOREIGN KEY (post_id) REFERENCES post(id),
    FOREIGN KEY (created_by) REFERENCES user(id)
);
