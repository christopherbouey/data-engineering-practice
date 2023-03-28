import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
spec_date = '2022-02-07 14:03'

def get_file_path(url:str, spec_date:str):
    '''
    Get file path for file modified on spec date
    
    If the program successfully gets the html, and finds the spec date,
    it will return a string of the file path.
    If not, it will return none
    '''
    try:
        html = requests.get(url)
        html.raise_for_status()
    except Exception as e:
        print(f'File Path Exception: {e}')
        return None, None
    soupy = BeautifulSoup(html.content)
    rows = soupy.find_all('tr')
    for i in rows:
        if spec_date in str(i):
            file_name = i.find_all('td')[0].a['href']
            break
    if file_name:
        file_url = url + file_name
        return  file_url, file_name
    else:
        print('No file name found for spec date')
        return None, None
            
def download_file(file_url, file_name):
    '''
    Download the file from the filepath. If filepath is None or is invalid,
    will return Null and print error message
    '''
    if file_url:
        try:
            r = requests.get(file_url)
            r.raise_for_status()
            with open(file_name, mode='wb') as file:
                file.write(r.content)
            return True
        except Exception as e:
            print(f'File Download Exception: {e}')
            return False
    else:
        return False

def get_highest_temp_rows(file_name):
    try:
        df = pd.read_csv(file_name)
        print(df[df['HourlyDryBulbTemperature'] == df['HourlyDryBulbTemperature'].max()])
    except Exception as e:
        print(f'Data Set Exception: {e}')
        
def main():
    file_url, file_name = get_file_path(url, spec_date)
    if download_file(file_url, file_name):
        get_highest_temp_rows(file_name)


if __name__ == '__main__':
    main()

