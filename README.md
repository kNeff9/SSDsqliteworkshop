# Welcome to SSD's SQL/Relational Databases Workshop!

## Description

Here you will be writing two queries to insert and fetch items from a database. The database will come preloaded with workout entries, where each entry is structured as:

    [id, workout_type, weight_used, date]

This data will be plotted using matplotlib to show workout progression over time. 


## Setup

First you will clone this repository. Go to a location in your files where you want the directory to go.
For example, if you navigate to SSD/Projects and clone there, you should now have SSD/Projects/SQLiteActivity

Do so with this command in your terminal:

```bash
git clone https://github.com/kNeff9/SSDsqliteworkshop
```

Before the next steps, you need to make sure you have python installed. 

Now, make sure you cd into the repository directory that you should have just created. Here you will create a python virtual environment where you will install dependencies and run your code. 

Do this with this command:

```bash
python -m venv venv
```

Then enter the venv (short for virtual environment) using

Windows:
```bash
.\venv\Scripts\activate
```

Linux:
```bash
source venv/scripts/activate
```

Now, you should see a green (venv) to the left of your terminal line or something similar. 

When you are in your venv, run
```bash
pip install -r requirements.txt
```

to install the necessary dependencies. 


## Running Program

To create the db and initialize the data, here are some files. Run them in this order from your venv. 

```bash
python create_db.py
```

```bash
python load_workout_data.py
```

These two commands create the SQLite database and loads the data from the .txt file. 

## Your Tasks

You need to fill in two SQL queries. One is located in add_entry.py and one is in display_funcs.py

Once you fill these in, you can test if they work by running the two programs. 

To test your fetch query run

```bash
python main.py
```
This will graph each of the four workouts  and show the graphed data. 

To test the insertion query, run 
```bash
python add_entry.py
```

And you will be prompted for intformation in your terminal