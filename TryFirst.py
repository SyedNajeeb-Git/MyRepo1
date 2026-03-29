import mysql.connector 
import tkinter

from time import sleep

print('Assalam Alekum')
print('I was able to import sql conenctor')
print('Walekum Salaam')
print('Ramazan Mubarak')

try:

    cn = mysql.connector.connect(auth_plugin='mysql_native_password', host='localhost', user='najeeb', passwd='Njb@Mysql25', database='myfirstschema')
    cursor = cn.cursor()
except Exception as e:
    print('Something is not right : ', e)
    exit()

    
cursor.execute('SELECT * FROM prod_codes')
for (productCode,prodcode_desc, prod_cat,prc) in cursor:
    print("Product Code: {} -- Product Code Desc: {}  ".format( productCode, prodcode_desc))

cursor.close()
cn.close()
