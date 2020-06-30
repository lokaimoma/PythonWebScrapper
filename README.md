# PythonWebScrapper
This is a simple flask web API for scrapping E-commerce sites for the prices of items on the web and alerting them when the price they want to buy it has reached.

The program is not yet yet done, but if you know more about flask and python you can make something about it.

Project is in initial stage not yet done.

Mongodb is used as database.
Gmail api is been used as the email sending service.

 # About the database
 
 You will have to install mongodb to run the database
 Currently when the program starts the database created is called "clarkdb"
 
 You can change it on line 4 in the url provided on that line 
 
 Initially there is no data for stores. Because the database files weren't associated for some reasons. But you can create one by
 
 1. When you initiate your database create a collection called "stores".
 
 2. The structure for how the store data is presented can be found in "store data.txt" file. It contains two sample stores.
 
 3. The store data has to be in json format 
 {"_id": "randomId", "name": "storeName", "url_prefix": "homepage of store", "tag_name": "the html tag that holds the price"}
 For example
 {
    "_id": "123",
    "name": "Jumia",
    "url_prefix": "https://www.jumia.ma/",
    "tag_name": "span",
    "query": {
        "class": "-b -ltr -tal -fs24"
    }
}
************************************************************************************

# About the .env
1. Create a .env file and add the a line in the form
ADMIN=admin@example.com

2. Replace only "admin@example.com" with the email you want to use as admin. Keep the .env in the root folder.
3. The program will automatically add it to environmental variables.
4. With admin access you can add stores at a more easier way than what we did above.
5. After adding it to admi.
6. Create a new user with that email and log in.
7. Then you can access the create stores access point and create the stores from your browser.
