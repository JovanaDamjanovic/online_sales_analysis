

\# Online Sales Analysis



This project is a simple online store inventory and shopping cart

system developed in Python.



The project demonstrates object-oriented programming (OOP),

Git version control, Git branches, merging and GitHub.



\## Classes



\### Product



The Product class represents a product in the store.



Attributes:

\- name

\- price

\- quantity



Methods:

\- display\_info(): displays product information.

\- update\_quantity(): updates product quantity.



\### ProductManager



The ProductManager class manages the store inventory.



Attributes:

\- products: a list of available products.



Methods:

\- add\_product(): adds a product.

\- show\_products(): displays available products.

\- total\_value(): calculates total inventory value.

\- remove\_product(): removes a product by name.



\### Cart



The Cart class represents a shopping cart.



Attributes:

\- cart\_items: a list of products in the cart.



Methods:

\- add\_product(): adds a product to the cart.

\- total\_value(): calculates the total cart value.

\- show\_cart(): displays the cart contents.



\## Main Program



The main.py file creates a ProductManager and adds four products.



It also creates a Cart and randomly selects three products

from the available inventory.



The program displays the selected products and calculates

the total shopping cart value.



\## How to Run



1\. Install Python.

2\. Clone this GitHub repository.

3\. Open the project folder.

4\. Run the following command:



python main.py



\## Git and GitHub



This project uses Git and GitHub for version control.



The following branches were created:

\- main

\- add-product-removal

\- add-cart-functionality



The branches were merged into the main branch.



The project also demonstrates resolving a Git merge conflict.



\## Security



The .gitignore file prevents Git from tracking:

\- config.json

\- screenshots/

\- \_\_pycache\_\_/

\- \*.pyc



\## Technologies



\- Python

\- Git

\- GitHub



\## Author



Jovana Damjanovic



