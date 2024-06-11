import requests
from bs4 import BeautifulSoup as bs
import pandas as pd;

url = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(url)
soup = bs(response.text,'html')
country_blocks = soup.find_all(class_="col-md-4 country")
# print(country_blocks)

country_data = [[x.find(class_='country-name').text.strip(),
        x.find(class_='country-capital').text.strip(),
        x.find(class_='country-population').text.strip(),
        x.find(class_='country-area').text.strip()] 
        for x in country_blocks]

cols = ['Name','Capital','Population','Area']
df = pd.DataFrame(country_data,columns = cols)

# df.to_excel('Countries.xlsx')


