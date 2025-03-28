import mysql.connector 

from time import sleep

print('Assalam Alekum')

print('I was able to import sql conenctor')
print('Walekum Salaam')
print('Ramazan Mubarak')


cn = mysql.connector.connect(auth_plugin='mysql_native_password', host='localhost', user='najeeb', passwd='Njb@Mysql25', database='myfirstschema')

cursor = cn.cursor()


cursor.execute('SELECT * FROM prod_codes')
for (productCode,prodcode_desc, prod_cat,prc) in cursor:
    print("Product Code: {} -- Product Code Desc: {}  ".format( productCode, prodcode_desc))

cursor.close()
cn.close()
