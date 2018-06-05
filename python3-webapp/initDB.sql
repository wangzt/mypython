create database py_test;
use py_test;

create table users (
	id varchar(50) primary key not null,
    email varchar(50),
    passwd varchar(50),
    admin bool,
    name varchar(50),
    image varchar(500),
    create_at float
    );

create table blogs (
	id varchar(50) primary key not null,
    user_id varchar(50),
    user_name varchar(50),
    name varchar(50),
    summary varchar(200),
    content text,
    create_at float);
    
create table comments (
	id varchar(50) primary key not null,
    blog_id varchar(50),
    user_id varchar(50),
    user_name varchar(50),
    user_image varchar(500),
    content text,
    create_at float
	);