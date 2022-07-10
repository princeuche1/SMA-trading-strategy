import pandas as pd
import sys
sys.path.append('../')
data = pd.read_csv('HINDALCO.csv', index_col=False, delimiter = ',')
data.head()

import mysql.connector as msql
from mysql.connector import Error

try:
	conn = msql.connect(host='localhost', database='assignment', user='prince', password='123456789')
	cursor = conn.cursor()
	cursor.execute("select database();")
	record = cursor.fetchone()
	print("You're connected to database: ",record)
	cursor.execute('DROP TABLE IF EXISTS hinda;')
	print('Creating table....')

	cursor.execute("CREATE TABLE hinda(datetime datetime,close decimal, high decimal,low decimal, open decimal,volume int,instrument char(25))")
	print("Table is created....")


	for i,row in data.iterrows():
				sql = "INSERT INTO assignment.hinda VALUES (%s,%s,%s,%s,%s,%s,%s)"
				cursor.execute(sql, tuple(row))
				
				# the connection is not autocommitted by default, so we must commit to save our changes
				conn.commit()
	print("Record inserted")
	
except Error as e:
    print("Error while connecting to MySQL", e)