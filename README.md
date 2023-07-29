# GreenKioskDjangoProject


Prerequisites
Git
Python
Pip
PostgreSQL
Setup
Clone the project repository.
Install the dependencies.
pip install -r requirements.txt
Create a .env file in the root directory and add the following environment variables:
DATABASE_URL=postgres://<username>:<password>@localhost:5432/gren_kiosk
Run the development server.
python manage.py runserver
The app will be available at http://localhost:8000.

Usage
The app is divided into the following sections:

Inventory: This app would allow you to track your inventory levels, set reorder points, and manage inventory transfers.
Customer: This app would allow you to track your customer data, such as their contact information, purchase history, and loyalty points.
Authorization: This app would allow you to authorize payments and manage fraud prevention.
Delivery: This app would allow you to track your deliveries, manage your shipping carriers, and provide customer support for delivery issues.
Reviews: This app would allow you to collect and manage customer reviews, which you could then use to improve your products and services.
Payments: This app would allow you to accept payments from customers, either online or in-store.
Cart: This app would allow customers to add products to their cart and checkout.
Offers: This app would allow you to create and manage marketing offers, such as discounts, coupons, and loyalty programs.


To-Do
Add more products.
Allow users to create accounts and track their orders.
Add a shipping calculator.
Credits
This project was created by RUTH AWINO.
