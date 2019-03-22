from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL Database
# REFERENCE (Python/MySQL): https://www.w3schools.com/python/python_mysql_insert.asp
database_connection = mysql.connector.connect(
    host="localhost",
    user="USERNAME_GOES_HERE",
    passwd="PASSWORD_GOES_HERE",
    database="test_db"
)
cursor = database_connection.cursor()

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submission', methods=['GET', 'POST'])
def submission():
    # Get Data from HTTP-POST Request
    id_column = request.form.get("id_column")
    value_column = request.form.get("value_column")

    # Convert id_column From String to Integer
    id_column = int(id_column)
    
    # Insert Data Into MySQL Database
    sql = "INSERT INTO test_table (id_column, value_column) VALUES (%s, %s)"
    values = (id_column, value_column)
    cursor.execute(sql, values)
    database_connection.commit()

    # Render HTML
    return render_template('submission.html', id_column=id_column, value_column=value_column)