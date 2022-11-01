Before starting

Please Enter these commands in MYSQL and also set the "password = ''" to "password = 'Whatever is your MYSQL password'"

1. create database main
2. create database carts
3. create database billing_info
4. create database revenue
5. use main
6. create table profile(Email_Address varchar(255), Password varchar(255));
7. use billing_info
8. create table billing_info(First_Name varchar(255), Last_Name varchar(255), Email_Address varchar(255), Address varchar(255), City varchar(255), Zip_Code int, Name_On_Card varchar(255), Credit_Card_Number bigint, Expire_Date date);
9. create table revenue (`Product Purchased` varchar(255), ` Customer's Email Address` varchar(255), `Product Price` int);

Thank You 
Made By Aadikshar Bhandari (group leader and the one who wrote and published the source code), Ashlesha Shrestha, Aadisha Shrestha
