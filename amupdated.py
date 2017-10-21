import requests
import urllib
import re
import csv
import scrapy


#url="https://www.amazon.in/Adidas-Shoes/b?ie=UTF8&node=4510749031"
url="https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Dshoes&field-keywords=adidas+shoes"
data=requests.get(url).content
file=open("/home/rijicp/git/outcsv.csv","wb")
file.write(data)
file=open("/home/rijicp/git/outcsv.csv","rb")
htmlfile=file.read()
#rex1='<span class="a-size-base a-color-price s-price a-text-bold">(.+?)</span>'

rex1='<img src="https://images-eu.ssl-images-amazon.com/images/I/31PQL9nnH6L._AC_UL260_SR200,260_.jpg" srcset="https://images-eu.ssl-images-amazon.com/images/I/31PQL9nnH6L._AC_UL260_SR200,260_.jpg 1x, https://images-eu.ssl-images-amazon.com/images/I/31PQL9nnH6L._AC_UL390_SR300,390_QL65_.jpg 1.5x, https://images-eu.ssl-images-amazon.com/images/I/31PQL9nnH6L._AC_UL520_SR400,520_QL65_.jpg 2x, https://images-eu.ssl-images-amazon.com/images/I/31PQL9nnH6L._AC_UL650_SR500,650_QL65_.jpg 2.5000x" alt="Product Details" class="s-access-image cfMarker" data-search-image-load="" height="260" width="200">'
pattern=re.compile(rex1)
price=re.findall(pattern,htmlfile)
print price

file.close()



