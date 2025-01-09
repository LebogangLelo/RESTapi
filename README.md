# RESTapi
# E-Commerce Platform API

## Description

This project is a RESTful API for managing products on an e-commerce platform. It allows users to add, update, delete, and view product details. The API is built with Django and Django REST Framework.

## Features

- User Authentication and Authorization
- CRUD operations for products
- Product tagging and search functionality
- Product listing and filtering with pagination
- Secure API endpoints

## Installation

### Prerequisites

- Python 3.7+
- Django 3.0+
- PostgreSQL

## **Technologies Used**
- **Backend Framework**: Django, Django REST Framework (DRF)
- **Database**: PostgreSQL
- **Authentication**: Token-based authentication 
- **Testing**: Pytest, Django Test Framework


### Setup

1. **Clone the repository:**
bash
   git clone https://github.com/LebogangLelo/RESTapi.git
   cd e_commerce_project
2. **create and activate a virtual environment:**
bash
     python -m venv env
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. **Install the dependencies:**
bash
   pip install -r requirements.txt
   



# Authentication Setup for E-Commerce API

This guide explains how to set up basic authentication for your e-commerce API using Django and Django REST Framework (DRF) with token-based authentication.

## Setup Instructions

### 1. Ensure you have Django REST Framework and the DRF token authentication package installed:

Add rest_framework and rest_framework.authtoken to your INSTALLED_APPS. And Configure the default authentication classes to include TokenAuthentication

## Create Token for Authentication to access Endpoints
URL: http://localhost:8000/api-token-auth/

## How to test the authentication:
    You can use Postman to test your new authentication endpoints.

**ENDPOINTS:**
1. **Product Management**

#Create Product: Add a new product.    (Admin only)
Path: /api/products/
Method: POST

#Get Product: Retrieve product details by ID.
Path: /api/products/{productId}
Method: GET

#Update Product: Update product details by ID.   (Admin only)
Path: /api/products/{productId}
Method: PUT

#Delete Product:  Delete product by ID.    (Admin only)
Path: /api/products/{productId}
Method: DELETE

2. **User Management**

#Create User: Register a new user.
Path: /api/users/
Method: POST

#Get User: Retrieve user details by ID.   (Admin or Self)
Path:/api /users/{userId}
Method: GET 

#Update User: Update user details by ID.     (Admin or Self)
Path: /api/users/{userId}
Method: PUT

#Delete User: Delete user by ID.      (Admin or Self)
Path: /api/users/{userId}
Method: DELETE

3. **Product search and filtering**

#Search for products by name or category.
Path: /api/products/search/
Method: GET 

#Filter products by category, price range or stock availability.
Path: /api/products/filter/
Method: GET

4. **Category Management**

#List Categories: 
Path: /api/categories/
Method: GET

#Create Category:   (Admin only)
Path: /api/categories/
Method: POST

#Retrieve Category:
Path: /api/categories/{id}/
Method: GET 

#Update Category:    (Admin only)
Path: /api/categories/{id}/
Method: PUT 

#Delete Category:    (Admin only)
Path: /api/categories/{id}/
Method: DELETE 

5. **Order Management**

#List Orders:
Path: /api/orders/
Method: GET 

#Create Order:
Path: /api/orders/
Method: POST 

#Retrieve Order:
Path: /api/orders/{id}/
Method: GET 

#Update Order:
Path: /api/orders/{id}/
Method: PUT 

#Delete Order:
Path: /api/orders/{id}/
Method: DELETE 





