create database ciudades;
create user ciudades@'localhost' identified by 'ciudades';
create user ciudades@'%' identified by 'ciudades';
grant all privileges on ciudades.* to ciudades@'localhost';
grant all privileges on ciudades.* to ciudades@'%';
