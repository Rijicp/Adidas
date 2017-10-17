import requests
import urllib
import os
import csv
import scrapy


#url="https://www.amazon.in/Adidas-Shoes/b?ie=UTF8&node=4510749031"
url="https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Dshoes&field-keywords=adidas+shoes"
data=requests.get(url).content
file=open("/home/rijicp/git/outcsv.txt","wb")
file.write(data)
file.close()




out=open(r"/home/rijicp/git/outcsv.txt","rb")
output=csv.reader(out)

new=[row for row in out]
print new

out=open("new.csv","wb")
output=csv.writer(out)
for row in new:
	output.writerow(row)
out.close()
