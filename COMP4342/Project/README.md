# COMP4342_MOBILE

## before run the program !!!
make sure node.js has been installed
Install the expo package which contains the Expo CLI used for starting the dev server:
`yarn add expo`

Then you can use Expo CLI to install the web dependencies in your project:
`npx expo install react-dom react-native-web @expo/webpack-config`

Before build the backend image, please make sure docker is also installed
## how to run the program
./run_program.bat

## frontend 
http://localhost:19006/

## backend
http://localhost:8000/

# Before do the pip install in backend
Please add the item into requirement.txt 

## database
1. download database management tools:  DataGrip / phpmyadmin / dbdeaver
2. connect to database under port 3306



## API List
# User
(GET) list all users:
http://43.156.8.249:8000/api/users/

(GET) show specific user:
http://43.156.8.249:8000/api/users/1/

(POST) Create User:
http://43.156.8.249:8000/api/users/
attribute: ["username","password"] is required

(PATCH) Update User data:
http://43.156.8.249:8000/api/users/1/
attribute: any attribute

(DELETE) DO NOT use delete at this moment

# Product
(GET) list all product:
http://43.156.8.249:8000/api/products/

(GET) show specific user:
http://43.156.8.249:8000/api/products/1/

(POST) Create User:
http://43.156.8.249:8000/api/products/
attribute: ["name","price","stock"] is required

(PATCH) Update User data:
http://43.156.8.249:8000/api/products/1/
attribute: any attribute

(DELETE) DO NOT use delete at this moment

# Order
(GET) list all orders with attached products:
http://43.156.8.249:8000/api/orders/

(GET) show specific order:
http://43.156.8.249:8000/api/orders/1/

(POST) Create User:
http://43.156.8.249:8000/api/orders/
example form body:
```
{
    "customer": 1,
    "total_amount": 150,
    "status": "pending",
    "delivery_status": "not_delivered",
    "products": [
        {
            "product_id": 1,
            "quantity": 2
        },
        {
            "product_id": 2,
            "quantity": 3
        }
    ]
}
```
(DELETE) DO NOT use delete at this moment

