CREATE DATABASE IF NOT EXISTS hue;
grant all on hue.* to 'lmman'@'0.0.0.0' identified by 'man123456@';
grant all on hue.* to 'root'@'0.0.0.0' identified by 'man123456@';
grant all on hue.* to 'lmman'@'172.21.0.1' identified by 'man123456@';
grant all on hue.* to 'lmman'@'172.22.0.5' identified by 'man123456@';
flush privileges; 
use hue;
CREATE TABLE MyGuests (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,firstname VARCHAR(30) NOT NULL,lastname VARCHAR(30) NOT NULL,email VARCHAR(50));