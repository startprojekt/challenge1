Challenge: Widgets
==================

*Create a basic system description and document a normalized schema from the
attached widgets text file. Include:*

*1) what you think this system would do*

*2) what you feel would be a reasonable database structure for the data
   and a reasonable architecture for the system*

*3) any questions or concerns you have regarding this dataset/system that might
   need to be answered before establishing an ideal database/solution for such a system.*

*It's a very open-ended problem, and that's part of the problem.*

```
widget	packaging	customer	price	supplier	cost	warehouse	qty	min_qty
Ant Trap	bag of 10	Home Place	$9	Little Traps	$0.50	AUS	112	50
Ant Trap	bag of 5	Home Place	$5	Little Traps	$0.50	AUS	112	50
Ant Trap	bag of 10	Bug Store	$10	Little Traps	$0.50	AUS	112	50
Ant Trap	bag of 5	Bug Store	$6	Little Traps	$0.50	AUS	112	50
Mouse Trap	box of 2	Home Place	$5	Little Traps	$1	ATL	200	50
Mouse Trap 	box of 1	Home Place	$3	Little Traps	$1	ATL	200	50
Mouse Trap	bag of 10	Home Place	$20	Little Traps	$1	ATL	200	50
Mouse Trap 	bag of 5	Bug Store	$15	Little Traps	$1	ATL	200	50
Bear Trap	box of 1	Home Place	$50	Big Traps	$40	MSP	10	10
Bear Trap	box of 5	Home Place	$220	Big Traps	$40	MSP	10	10
Bear Trap 	box of 1	No Bears R Us	$60	Big Traps	$40	MSP	10	10
Moose Trap	box of 1	Home Place	$75	Big Traps	$50	MSP	5	5
Moose Trap	box of 1	No Bears R Us	$80	Big Traps	$50	MSP	5	5
Elephant Trap	crate of 1	Home Place	$100	Raytheon	$90	MSP	3	5
Elephant Trap	crate of 1	No Bears R Us	$110	Raytheon	$90	MSP 	3	5
```


Question 1
----------

*What you think this system would do?*

The table in a given example seems to represent a list of ordered products
("animal traps"), possibly in an online shop or some sales software.
The system would gather orders from customers, manage stock prices and costs
(i.e. calculate profit), control supply and shipment from different suppliers
to many of available warehouses.

There are miscellaneous packages available in which particular products
can be ordered.

The last two columns `qty` and `min_qty` could suggest that this table
represents current stock items with a possible "warning" to be triggered
when available quantity of a particular product achieves value below `min_qty`.

In general it seems to be some kind of sales and stock management software.


Question 2
----------

*What you feel would be a reasonable database structure for the data and
a reasonable architecture for the system*

As for database structure we would need following tables:

* CUSTOMERS
* PRODUCTS (catalogue)
* PACKAGES (for products)
* WAREHOUSES
* STOCK (products on stock = product + delivery/supplier + quantity + price)
* SUPPLIERS
* DELIVERIES (products from suppliers)
* ORDERS
* ORDERED PRODUCTS
* SHIPMENTS (products sent to customers)

Some optional tables if further required:

* PAYMENTS
* ADDRESSES (shipment, bills)
* PRODUCT REVIEWS

We would obviously need all necessary CRUD views for tables like customers, suppliers, products, packages, warehouses. There also needs to be a view for placing orders (accessible by a customer?).

Depending on planned size and foreseeable traffic in the service, a reasonable
architecture might be a REST API with a single page application (e.g. Angular)
as frontend. It could also be a website with standard Django class-based views
supported with AJAX requests in order to get data in the online shop.

Instead of reinventing the wheel we could also go for solutions like [Django Oscar](https://github.com/django-oscar/django-oscar)
as an e-commerce framework since it has similar approach in organizing and selling products to the data presented in the table above. This framework
can be highly customizable and thus adjusted to further customer requirements.



Question 3
----------

*Any questions or concerns you have regarding this dataset/system that might
need to be answered before establishing an ideal database/solution for such a system.*

* We would need to establish fields related to customers or suppliers, do we need
  to store any addresses, contact information, additional data, remarks etc.?

* Is there any shipment of widgets involved?

* Can orders be collected/received by personal pickup?

* Are there any other types of packaging than "box", "bag" or "crate"?

* Shall we be concerned about currency or can we assume that only USD will be used?

* Is the system controlling payments?

* Are there any discounts offered to customers?

* Are there any other product types than "traps"?

* What would be the biggest order limit (total price)? Is there any?

* How many customers, suppliers, products, orders are expected? (daily, monthly)

* Should we use FIFO or some other way to organize stock products?

