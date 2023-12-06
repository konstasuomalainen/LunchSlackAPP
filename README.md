# Lunchbot
LounasBotti

This projects goal is to web scrape restaurants menus in the Lappeenranta area.\
After scraping HTML, desired data is searched and parsed.\
Processed data is converted to PDF, which is then send using Slack API to desired Slack channel.\
Recipients can vote interactively which restaurant to go using buttons

## Install
Python Download:\
https://www.python.org/downloads/

Dependencies are installed using requirements.txt:\
pip install -r requirements.txt

## File modifications
Go to https://api.slack.com/apps and create App.\
After you created App, you should be in the App settings, go to OAuth & Permissions using the left menu:

Look for => OAuth Tokens for Your Workspace.\
Copy your => Bot User OAuth Token.

Inside code editor head over .env file\
Paste your OAuth Token\
example. SLACK_TOKEN = xoxb-**********

## Scraping



### Changing the URl
Put websites URL you wanna scrape the information inside the ''\
example. html_text = requests.get('https://www.lounaat.info/lounas/pancho-villa/lappeenranta').text

### Changing the parameters for the searched elements
Websites are constructed different ways, using different class names and elements.\
You can modify searched elements in method find_all()\
example. datas = soup.find_all('div', class_="item")
