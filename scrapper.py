import requests
from bs4 import BeautifulSoup
import textwrap
url = 'https://google.com'  
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    clean_text = soup.get_text()
    words_per_line = 70
    lines = textwrap.wrap(clean_text, width=words_per_line)
  
    for line in lines:
        print(line)
    
    # User 2 added feature
    
    with open('output.txt','w',encoding='utf-8') as file:
    	file.write(clean_text)

    

else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
