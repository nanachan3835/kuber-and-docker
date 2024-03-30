import jwt ,datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL


sever = Flask(__name__)
mysql = MySQL(sever)

sever.config["MYSQL_HOST"]= os.environ.get("MYSQL_HOST")
