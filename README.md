# Flask URL-Shortener

![](https://github.com/coralbeef/Flask-URL-Shortener/blob/master/screenshots.gif)

## Setup
* Create a virtualenv
* Install the requirements ```pip install -r requirements.txt```
* Update settings.py with your own MySQL credentials
* Create the database in MySQL ```CREATE DATABASE shortener;```
* Run ```python create_db.py``` to set up the table
* Then alter the database in MySQL to make characters case-sensitive:

```ALTER DATABASE shortener CHARACTER SET utf8 COLLATE utf8_bin;```
```ALTER TABLE url CONVERT TO CHARACTER SET utf8 COLLATE utf8_bin;```

