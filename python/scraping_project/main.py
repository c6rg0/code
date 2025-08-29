import requests
from bs4 import BeautifulSoup

print("Enter the link you want to parse: ")
website_link = input()

response = requests.get(website_link)
soup = BeautifulSoup(response.content, 'html.parser')

content_div = soup.find('div', class_='article--viewer_content')
if content_div:
    for para in content_div.find_all('p'):
        print(para.text.strip())
else:
    print("No article content found.")
