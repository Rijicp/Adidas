import requests
import urllib
import os
import csv
url='https://www.amazon.in/Adidas-Shoes/b?ie=UTF8&node=4510749031'
data=requests.get(url).content




file=open(r"/home/rijicp/output.txt","w")
#file.write(datas)
csv_writer=csv.writer(file)
#reads=csv.reader(file)
for i in data:
	csv_writer.writerow(i)
#print reads
file.close()
