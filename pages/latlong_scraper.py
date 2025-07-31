import requests
from bs4 import BeautifulSoup
import pandas as pd

# base url for google search 
BASE_URL = "https://www.google.com/search?q="

# headers to simulate a real browser visit
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# function to scrape latitude and longitude
def get_coordinates(sector):
      search_term = f"sector {sector} gurgaon longitude & latitude"
      response = requests.get(BASE_URL+search_term, headers=HEADERS)

      if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            coordinates_div = soup.find("div", class_="Z0LcW t2b5Cf")
            if coordinates_div:
                  return coordinates_div.text
      return None

# create a dataframe
df = pd.DataFrame(columns=['Sector','Coordinates'])

# iterate over sectors and fetch coordinates.
for sector in range(1,116):
      coordinates = get_coordinates(sector)
      new_row = pd.DataFrame([{"Sector": f"Sector {sector}", "Coordinates": coordinates}])
      df = pd.concat([df, new_row], ignore_index=True)

# save DataFrame
df.to_csv("gurgaon_sectors_coordinates.csv", index=False)