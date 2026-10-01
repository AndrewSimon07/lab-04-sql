CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(20),
    email VARCHAR(50),
    password VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    user_id INT,
    title VARCHAR(50),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


INSERT INTO users (user_id, username, email, password) VALUES
(1, 'alex123', 'alex@email.com', 'alexpass1'),
(2, 'jordan22', 'jordan@email.com', 'jordanpass2'),
(3, 'sammy', 'sammy@email.com', 'sammypass3'),
(4, 'taylor99', 'taylor@email.com', 'taylorpass4'),
(5, 'morgan5', 'morgan@email.com', 'morganpass5'),
(6, 'casey17', 'casey@email.com', 'caseypass6'),
(7, 'riley8', 'riley@email.com', 'rileypass7'),
(8, 'jamie42', 'jamie@email.com', 'jamiepass8'),
(9, 'chris11', 'chris@email.com', 'chrispass9'),
(10, 'drew7', 'drew@email.com', 'drewpass10');

INSERT INTO posts (post_id, user_id, title, content, created_at) VALUES
(1, 1, 'My First Post', 'Hello everyone!'),
(2, 2, 'Weekend Plans', 'Looking forward to the weekend.'),
(3, 3, 'New Project', 'I started a new project today.'),
(4, 4, 'Favorite Food', 'Pizza is one of my favorite foods.'),
(5, 5, 'Study Tips', 'Here are some tips for studying.'),
(6, 6, 'Great Day', 'Today was a really good day.'),
(7, 7, 'New Hobby', 'I recently started learning guitar.'),
(8, 8, 'Travel Plans', 'I am planning a trip this summer.'),
(9, 9, 'Game Night', 'We had a fun game night yesterday.'),
(10, 10, 'Good Morning', 'Hope everyone has a great day!');



