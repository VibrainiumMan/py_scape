import requests
from bs4 import BeautifulSoup

user_input = input("URL: ") #User input for the url

try:
    request = requests.get(user_input) 
    request.raise_for_status() #check for error
    print(f"Response: \n{request}")

    parser = BeautifulSoup(request.content, 'html.parser')
    print(parser.prettify())
except requests.exceptions.RequestException as e:
    print(f"{e}")
    
