import requests
import urllib
import os
import csv
import scrapy
url="https://www.amazon.in/Adidas-Shoes/b?ie=UTF8&node=4510749031"
data=requests.get(url).content
file=open("/home/rijicp/git/outcsv.csv","wb")
file.write(data)
out=open("/home/rijicp/git/outcsv.csv","rb")
output=csv.writer(out)
for row in out:
	output.writerow(row)

out.close()

