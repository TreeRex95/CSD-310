/*
    Title: whatabook.init.sql
    Author: Tristan Boetcher
    Date: 4/30/22
    Description: WhatABook database initialization script.
*/

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('123 1st St. NE Luverne, MN 56156');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('FullMetal Alchemist', 'Hiromu Arakawa', 'Two brothers search for a stone');

INSERT INTO book(book_name, author, details)
  VALUES('My Hero Academia', 'Kohei Horikoshi', 'Boy gains super powers');

INSERT INTO book(book_name, author, details)
  VALUES ('Attack on Titan', 'Hajime Isayama', 'Post apocalyptic vision of a faltering human race besieged by man eating giants');

INSERT INTO book(book_name, author, details)
  VALUES('Vagabond', 'Takehito Inoue', 'Fictional account of Miyamoto Musashis life');

INSERT INTO book(book_name, author, details)
  VALUES ('Tokyo Ghoul', 'Sui Ishida', 'College student Ken, goes on a date and turns into a monster');

INSERT INTO book(book_name, author, details)
  VALUES ('Black Butler', 'Yana Toboso', 'Ciel, guard dog to the royal family and the last surviving member of the Phantomhive family');

INSERT INTO book(book_name, author)
  VALUES ('Blue Exorcist', 'Kazue Kato');

INSERT INTO book(book_name, author)
  VALUES ('Vampire Knight', 'Matsuri Hino');

INSERT INTO book(book_name, author)
  VALUES('A Silent Voice', 'Yoshitoki Oima');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Thorin', 'Oakenshield');

INSERT INTO user(first_name, last_name)
    VALUES('Bilbo', 'Baggins');

INSERT INTO user(first_name, last_name)
    VALUES('Frodo', 'Baggins');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (1,3);

INSERT INTO wishlist(user_id, book_id)
    VALUES (2,6);

INSERT INTO wishlist(user_id, book_id)
    VALUES (3,8);
