
import requests
from bs4 import BeautifulSoup

def googlefinance(birim):

        url = "https://www.google.com/finance/quote/"+str(birim)+"-TRY?hl=tr"

        try:
              
            page = requests.get(url)
            
            htmlpage = BeautifulSoup(page._content,"html.parser")

            actual_value = htmlpage.find("div", class_="YMlKec fxKbKc").get_text()
        
            x = round(float(actual_value.replace(".", "").replace(",", ".")), 2)
            


        except Exception as e:
              print("an error occurred: ",e)
        return x          
       