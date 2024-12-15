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
- **Authentication**: Token-based authentication (JWT or OAuth2)
- **Testing**: Pytest, Django Test Framework
- **Documentation**: Swagger/OpenAPI (via drf-yasg)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/LebogangLelo/RESTapi.git
   cd e_commerce_project

# Authentication Setup for E-Commerce API

This guide explains how to set up basic authentication for your e-commerce API using Django and Django REST Framework (DRF) with token-based authentication.

## Setup Instructions

### 1. Install Required Packages

Ensure you have Django REST Framework and the DRF token authentication package installed:

```bash
 pip install djangorestframework
 pip install djangorestframework-simplejwt

Add rest_framework and rest_framework.authtoken to your INSTALLED_APPS. And Configure the default authentication classes to include TokenAuthentication

## Create Token Authentication Endpoints with their serializers and views

## How to test the authentication:
You can use Postman to test your new authentication endpoints.

#Register User
URL: http://localhost:8000/auth/register/

Method: POST

Body: JSON data with username, email, and password

#Login User
URL: http://localhost:8000/api/auth/login/

Method: POST

Body: JSON data with username and password

