import requests, os, zipfile, io

if not os.path.exists('downloads'):
    os.mkdir('downloads')

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]

target_path = 'downloads/'

def main():
    for uri in download_uris:
        try:

            response = requests.get(uri, stream=True)
            zip_file = zipfile.ZipFile(io.BytesIO(response.content))
            zip_file.extractall(target_path)
            
        except:
            continue


if __name__ == '__main__':
    main()
