import mysql.connector
import config

connection = mysql.connector.connect(
    host=config.HOST,
    user=config.USER,
    password=config.PASSWORD,
    database=config.DATABASE
)

cursor = connection.cursor()
