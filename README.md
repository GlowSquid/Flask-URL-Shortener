# Flask URL-Shortener

## Features
* Shortens URLs to a default 3-digit prefix using random character and letter combination.
* Checks if the shortened URL already exists and attempt to re-run the code-generator until it finds an available combination.
* All data is stored in a single MySQL table.
* Case-sensitive. The database distinguishes between upper and lower characters.
* A Stats page lists all the shortened URLs, and shows how many times a target link has been redirected.
* There is a button to automatically copy the shortened URL to clipboard.
* Has an option to use Recaptcha to prevent spambots.

![](https://github.com/coralbeef/Flask-URL-Shortener/blob/master/screenshot.gif)

## Setup
* Create a virtualenv
* Install the requirements ```pip install -r requirements.txt```
* Update settings.py with your own MySQL credentials
* Create the database in MySQL ```CREATE DATABASE shortener;```
* Run ```python create_db.py``` to setup the table
* Lastly, alter the database in MySQL to make characters case-sensitive:

```ALTER DATABASE shortener CHARACTER SET utf8 COLLATE utf8_bin;```
```ALTER TABLE url CONVERT TO CHARACTER SET utf8 COLLATE utf8_bin;```
