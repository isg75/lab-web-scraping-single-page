
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def scrape_100():
    
    """
    Scrapes the Billboard Hot 100 chart and returns a DataFrame with song titles and artists.
    
    Returns:
        pandas.DataFrame: DataFrame containing the song titles and artists.
    """
    
    url = "https://www.billboard.com/charts/hot-100/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Scrapping for the titles of the Hot 100
    title = []
    for li in soup.select("li.lrv-u-width-100p li h3"):
        title.append(li.get_text().strip())
        
    # Scrapping for their respective artists    
    artist = []
    for i in soup.select("li.lrv-u-width-100p li span"):
        text = i.get_text().strip()
        match = re.match(r'^[A-Za-z\s]+(?:[A-Za-z0-9\s\W]*[A-Za-z0-9])?$', text)
        if match:
            artist.append(text)
    
    # Saving the data into a DataFrame
    hot_100_songs = pd.DataFrame({"Title": title, "Artist": artist})

    return hot_100_songs
