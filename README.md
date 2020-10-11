These Python scripts can be used to debug and learn about making API requests with Python and or any other tools.
Primary use case I had in mind is for extract/transform steps of data pipelines.

You can inspect response history, set timeouts, handle authentication and do all manner of things.

This is just a basic script I used to verify a Power BI [bug](https://www.leehbi.com/blog/2020-07-04-Python-Script-Source-Power-BI)

The scrict is minimal at the moment. I'll keep it updated with new routes on the server to pose challenging json/xml/binary data sources. Anyone is welcome to contribute with routes, either remote or local.

To use follow steps below :

1. Run the server.py in /Server - this is a just minimal flask server to provide us with an end point we can use in PowerBI/Javascript/Python/etc. Asssuming you already have Python installed you just just need to pip or conda install flask.   CD into Server and run flask run to launch the server.

2. You can use the client.py in /Client if you would like to experiment with making programatic web requests. If using this with the server.py on your machine you can run both scripts in seperate terminals. Pip or conda install requests.

Python really does come in handy :-)
