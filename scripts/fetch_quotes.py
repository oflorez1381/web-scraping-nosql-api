from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests,csv,time
from random import randint
import requests

output_file_path = 'data/output_quotes.csv'
website = "http://www.values.com/inspirational-quotes"
csv_header = [
    "theme",
    "url",
    "img",
    "lines",
    "author"
]

def write_csv_header(file_path,csv_header):
    with open(file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(csv_header)

def write_to_csv(file_path,*args):
    with open(file_path, mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(args)


response = requests.get(website)
soup_data = BeautifulSoup(response.text, 'html.parser')
quotes=[]  # a list to store quotes 
table = soup_data.find('div', attrs = {'id':'all_quotes'})  
   
for row in table.findAll('div', 
                         attrs = {'class':'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'}): 
    quote = {} 
    quote['theme'] = row.h5.text 
    quote['url'] = row.a['href'] 
    quote['img'] = row.img['src'] 
    quote['lines'] = row.img['alt'].split(" #")[0] 
    quote['author'] = row.img['alt'].split(" #")[1] 
    quotes.append(quote)

write_csv_header(output_file_path, csv_header)

for quote in quotes:        
    write_to_csv(output_file_path, quote['theme'], quote['url'], quote['img'],quote['lines'], quote['author'])
    

