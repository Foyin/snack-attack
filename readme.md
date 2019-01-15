The solutions the the challenge is posted here. 

- I wrote a python script and used it to create a simplified version of the products list json file with less properties to make it easier to create the tables. 
- Then I used an online json to SQL tool to make the code to create the tables 
- Manually assigned primary keys
- Then i used a tool called sqlite3 to test the database schema and queries

Find all emails of snackers with a 'fave_snack'of a product we stock not assuming everything in table is in stock:
SELECT email FROM products JOIN snackers ON snackers.fave_snack=products.title AND products.available = 'True';

Find all emails of snackers with a 'fave_snack'of a product we stock assuming everything in table is in stock:
SELECT email FROM products JOIN snackers ON snackers.fave_snack=products.title;

Assuming everything in products table is in stock
1) List the real stocked snacks you found under the snacker's 'fave_snack'?
SELECT fave_snack FROM products JOIN snackers ON snackers.fave_snack=products.title;

2) What're the emails of the snackers who listed those as a 'fave_snack'?
SELECT email FROM products JOIN snackers ON snackers.fave_snack=products.title;

3) If all those snackers we're to pay for their 'fave_snack'what's the total price?
SELECT SUM(price) FROM products JOIN snackers ON snackers.fave_snack=products.title;

Results (assuming everything in products table is in stock):

Find all emails of snackers with a 'fave_snack'of a product we stock:
```
cbuchett29@simplemachines.org
cshearstonedr@shinystat.com
gtanswillg@rambler.ru
rdelagua1s@engadget.com
alenox2c@answers.com
okillend@ucoz.ru
stirte5c@si.edu
ulapish4u@abc.net.au
```

1) List the real stocked snacks you found under the snacker's 'fave_snack'?
```
Clif Crunch Bar
Clif Crunch Bar
Clif Crunch Bar
Clif Crunch Bar
Bobo's Oat Bars
Bobo's Oat Bars
Bobo's Oat Bars
Bobo's Oat Bars
```

2) What're the emails of the snackers who listed those as a 'fave_snack'?
```
cbuchett29@simplemachines.org
cshearstonedr@shinystat.com
gtanswillg@rambler.ru
rdelagua1s@engadget.com
alenox2c@answers.com
okillend@ucoz.ru
stirte5c@si.edu
ulapish4u@abc.net.au
```

3) If all those snackers we're to pay for their 'fave_snack'what's the total price?
```
22.0
```


