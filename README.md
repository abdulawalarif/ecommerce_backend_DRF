# API Endpoint for E-commerce product GET,	POST,	PUT,	DELETE API with Django Rest Framework

Base_URL : https://awalarifdr.pythonanywhere.com


* GET

1.  For all products url => Base_URL/api/products

2.  For a single product url => Base_URL/api/product/product_id


* POST

1. url =>Base_URL/api/products

No authentication required for now. You can send data to the server. for posting data, add the data on requests body as form-data
fill the title / description / num_of_prod_on_stock / price / uploaded_images -> ( this is a list field you can upload multiple images / single image And all the fields are required.


For Example:



* UPDATE

1.  url => Base_URL/api/product/id_of_item

For updating any product put changed data on request body as form-data fill the title/description/num_of_prod_on_stock/price/uploaded_images,
 all the fields are optional send request as  PUT. 

Like the Image below:


![alt text](screenshots/put_data.png)




* Delete

1.  url => Base_URL/api/product/delete/id_of_item

For deleting any item give the id of product on url and hit send as a DELETE request. 



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

![alt text](<screenshots/post data.png>)

```bash
URL: http://127.0.0.1:8000//api/products
# Requird field
title
description
num_of_prod_on_stock 
price
uploaded_images #this is a list of images file you can put multiple images 
```
## How to tweak this project for your own uses

It's a good starter boilerplate, An ecommerce app 

## Found a bug?

If you found an issue or would like to submit an improvement to this project,
please submit an issue using the issues tab above. If you would like to submit a PR with a fix, reference the issue you created!


## Known issues (Work in progress)
*   No auth yet



## Author

- [@abdulawalarif](https://github.com/abdulawalarif)
  
## License

[MIT](https://choosealicense.com/licenses/mit/)


