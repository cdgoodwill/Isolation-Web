--create database isolation_web;

drop table if exists users;

CREATE TABLE IF NOT EXISTS users(
id VARCHAR(255) PRIMARY KEY,
house_name VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL,
zip INT NOT NULL
);

drop table if exists connections;

CREATE TABLE IF NOT EXISTS connections(
auto_id SERIAL NOT NULL PRIMARY KEY,
id VARCHAR(255) NOT NULL,
conn_id VARCHAR(255) NOT NULL
);

INSERT INTO users (id, house_name, email, zip)
VALUES
('f531b79b-02aa-48a6-8b08-e8b4fb8ee24d','Bohemia','hans.sprecher+parkslope@gmail.com',11215),
('501edbf4-0a10-4ea3-b7dc-4006d1d07c81','The Park','park.slope@gmail.com',11215),
('60e5be64-021b-4197-b35d-9e555bfa02c5','Bunker','hans.sprecher+les@gmail.com',10002),
('7c599157-bc92-49ac-93e1-5a0ab8620f80','Princess Castle','hans.sprecher+uws@gmail.com',10025);

select * from users;

INSERT INTO connections (id, conn_id)
VALUES
('f531b79b-02aa-48a6-8b08-e8b4fb8ee24d','60e5be64-021b-4197-b35d-9e555bfa02c5'),
('f531b79b-02aa-48a6-8b08-e8b4fb8ee24d','7c599157-bc92-49ac-93e1-5a0ab8620f80'),
('f531b79b-02aa-48a6-8b08-e8b4fb8ee24d','501edbf4-0a10-4ea3-b7dc-4006d1d07c81');

select * from connections;
