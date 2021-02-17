# About

This is a simple Flask application created during BootCamp course in 2021.

This application uses following libraries:

- SQLAlchemy for SQL stuff
- Flask for web goodness
- Some terminal candies (ex. tqdm)
- Uses pipenv for managing dependencies

Application can be easily deployed to Heroku or DigitalOcean. Have been tested only on Python 3.

# Config file

Make sure to create .env file in your project root (see .env_example) which contains correct DATABASE URI connection string. This will allow you to run application locally and connect to correct database.

# Runnig application

```shell
# optional if you don't have pipenv installed
pip install pipenv
pipenv install
pipenv shell
python app.py
```

# Inserting data from CSV file to database

- Download CSV data here: https://www.avoindata.fi/data/fi/dataset/alkoholielinkeinorekisteri (Alkoholijuomien anniskelupaikat) as CSV file.
- Place CSV file in project root
- Rename CSV file to data.csv
- Run ```python csv2db.py``` within python virtual enviroment

# Deplyment to DigitalOcean app platform

## Setting up App platform in DigitalOcean

![](https://dl.dropboxusercontent.com/s/1bd57jbxb5j29cm/2021-02-17_11-36-05.gif)

# Dcoumentation

Documentation can be found in doc folder.

# Author

Artem Daniliants / www.daniliants.com

# License

Copyright 2021 Artem Daniliants

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.