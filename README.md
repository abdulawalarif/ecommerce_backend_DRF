# Django REST Framework E-commerce API with Authentication (GET, POST, PUT, DELETE)


## This project provides a Django REST API for an e-commerce platform, supporting CRUD operations (Create, Read, Update, Delete) for products. It includes user authentication for secure access to product data manipulation only (update, delete and create). But user can read for data without auth token.

## Features
* Secure authentication using Django Rest Framework Authentication (JWT Toke)
* Full CRUD support for managing products
* Supports multiple images uploads for products
* API endpoints GET, POST, PUT, and DELETE
* Lightweight and fast, perfect for small to medium-scale e-commerce platforms




## Authentication

Use the provided authentication mechanism to obtain tokens.



* Register User:
* Fill these 3 fields



```bash
  URL: POST to Base_URL/api/auth/register
  username #PK
  email
  password
```

* Login User:



```bash
  POST to Base_URL/api/auth/login
  username 
  password
```


![Login and Registration visualized ](<screenshots/auth.jpg>)

 

On successful login, you will receive an authentication token to be used in the header for subsequent write requests.



# API Endpoints
## Product Endpoints

* Get All Products:


```bash
GET request to Base_URL/api/products
```

* Get a Single Product:


```bash
GET request to Base_URL/api/product/product_id
```


![Fetching products from Database ](<screenshots/fetchProduct.jpg>)

 
* Create Product (Authenticated):

```bash
POST request to Base_URL/api/product/products
# with title, description, num_of_prod_on_stock, price, uploaded_images
# With Auth token
```

![Creating products](<screenshots/createProduct.jpg>)

* Update Product (Authenticated):


```bash
PUT request to Base_URL/api/product/id_of_item
# with title, description, num_of_prod_on_stock, price, uploaded_images
# With Auth token
```
 

![Update products](<screenshots/updateProd.jpg>)

* Delete Product (Authenticated):

```bash
DELETE request to Base_URL/api/product/delete/id_of_item
# With Auth token
```
 

 
 

## Run Locally

1. Clone the project

```bash
  git clone https://github.com/abdulawalarif/ecommerce_backend_DRF.git
```

2. Go to the project directory

```bash
  cd ecommerce_backend_DRF && cd ecommerce_backend
```

3. Create a virtual environment

```bash
  python3 -m venv .ecom_env
```

4. Activate the virtual environment

```bash
  source .ecom_env/bin/activate
```


5. Install all the packages

```bash
  pip install -r requirements.txt
```

6. go to the ecommerce_backend/settings.py and change the databse to Sqlite


```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Or you can crate a SQL if you want to.

7.  Now create migration for your database 

```bash
python manage.py makemigrations
```
8. Now Create Tables and Fields for the database

```bash
 python manage.py migrate
```
9. Run the project

```bash
python manage.py runserver
```

 Now fill some data first with this URL POST request 




## How to tweak this project for your own uses

It's a good starter boilerplate, for an ecommerce app, Create models for categories and user's follow a good design architecture and make sure to Normalize the datababse for preventing overload or duplication of same data in multiple places.

## Found a bug?

If you found an issue or would like to submit an improvement to this project,
please submit an issue using the issues tab above. If you would like to submit a PR with a fix, reference the issue you created!


## Known issues (Work in progress)
*  Update method do no delete images it just add new images with existing image list. 


## Author

- [@abdulawalarif](https://github.com/abdulawalarif)
  
## License

[MIT](https://choosealicense.com/licenses/mit/)


