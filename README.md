# Flask URL-Shortener

## Features
* Shortens URL to a default 3-digit prefix with random character and letter combination.
* Checks if the shortened URL already exists and attempt to rerun the code-generator until it finds an available combination.
* All data is stored in a single MySQL table.
* Case-sensitive. The database distinguishes between upper and lower characters.
* A Stats-page list all the shortened URLs, and shows how many times target link has been redirected.
* There is a button to automatically copy the shortened URL to clipboard.
* Has an option to use Recapcha to prevent spam.

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

