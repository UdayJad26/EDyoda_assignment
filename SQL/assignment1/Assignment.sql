create database assignment;
use assignment;

create table SalesPeople(
Snum int primary key,
Sname varchar(20) unique,
City varchar(30),
Comm int
);

create table Customers(
Cnum int primary key,
Cname varchar(25),
City Varchar(30),
Snum int,
foreign key (Snum) references SalesPeople (Snum)
);

create table Orders(
Onum int primary key,
Amt decimal(10,2),
Odate Date,
Cnum int,
Snum int,
foreign key (Cnum) references Customers (Cnum),
foreign key (Snum) references SalesPeople (Snum)
);


insert into SalesPeople (Snum, Sname, City, Comm)
values (1001,"Peel","London", 12);
insert into SalesPeople (Snum, Sname, City, Comm)
values (1002,"Serres","Sanjose", 13),
(1004,"Motika","London", 11),
(1007,"Rifkin","Barcelona", 15),
(1003,"Axelrod","Newyork", 10);

insert into Customers (Cnum, Cname, City, Snum)
values (2001,"Hoffman","London", 1001),
(2002,"Giovanni","Rome", 1003),
(2003,"Liu","Sanjose", 1002),
(2004,"Grass","Berlin", 1002),
(2006,"Clemens","London", 1001),
(2008,"Cisneros","Sanjose", 1007),
(2007,"Pereira","Rome", 1004);

insert into Orders
values(3001, 18.69, str_to_date("3-10-1990",'%d-%m-%Y'), 2008, 1007);
insert into Orders
Values (3003, 767.19,str_to_date("3-10-1990 ",'%d-%m-%Y'), 2001, 1001),
(3002, 1900.10, str_to_date("3-10-1990",'%d-%m-%Y'),  2007, 1004),
(3005,  5160.45,str_to_date("3-10-1990",'%d-%m-%Y'), 2003, 1002),
(3006, 1098.16, str_to_date("3-10-1990",'%d-%m-%Y'), 2008, 1007),
(3009, 1713.23, str_to_date("4-10-1990",'%d-%m-%Y'), 2002, 1003),
(3007,  75.75, str_to_date("4-10-1990",'%d-%m-%Y'), 2004, 1002),
(3008,  4273.00, str_to_date("5-10-1990",'%d-%m-%Y'), 2006, 1001),
(3010, 1309.95, str_to_date("6-10-1990",'%d-%m-%Y'), 2004, 1002),
(3011, 9891.88, str_to_date("6-10-1990",'%d-%m-%Y'), 2006 ,1001);

select * from SalesPeople;
select * from Customers;
select * from Orders;
describe Orders;

-- 1. Count the number of Salesperson whose name begin with ‘a’/’A’.
select count(s.Sname) as number_of_Salesperson from SalesPeople s 
where s.Sname like "A%"or "a%";

-- 2.  Display all the Salesperson whose all orders worth is more than Rs. 2000.
select s.Sname as Salesperson , sum(o.Amt) as orders_worth from Orders o
join SalesPeople s on s.Snum=o.Snum
group by s.Sname
having  sum(o.Amt)>2000;

-- 3  Count the number of Salesperson belonging to Newyork.
select count(s.Sname) as number_of_Salesperson_from_Newyork from SalesPeople s 
where s.City="Newyork";

-- 4.  Display the number of Salespeople belonging to London and belonging to Paris.
select count(s.Sname) as number_of_Salesperson_from_London_and_Paris from SalesPeople s 
where s.City="London" or s.City="Paris";

-- 5. Display the number of orders taken by each Salesperson and their date of orders
select s.Sname as Salesperson,count(o.Snum) as number_of_orders, o.Odate as Date from Orders o
join SalesPeople s on s.Snum=o.Snum
group by s.Sname
order by o.Odate;
