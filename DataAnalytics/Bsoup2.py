import requests
from bs4 import BeautifulSoup as bs
import pandas as pd;

url = 'https://www.scrapethissite.com/pages/forms/'
teams_data =[]
for pg_no in range(1,25):
    
    response = requests.get(url,params={'page_num':pg_no})
    soup = bs(response.text,'html')
    team_rows = soup.find_all(class_='team')
    for team in team_rows:
        teams_data.append([cell.text.split()[0] if cell.text.split() != [] else '' for cell in team.find_all('td')])

    print(pg_no)
cols = ['NAME','YEAR','WINS','LOSSES','OT_LOSSES','WIN%','GF','GA','+/-']
df = pd.DataFrame(teams_data,columns=cols)
df.to_excel('Teams.xlsx',index = False)