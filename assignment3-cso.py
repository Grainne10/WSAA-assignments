# Assignment 3 CSO
# Grainne Boyle
# Task - Retrieve a dataset from the CSO website and store it in a json file.


# The first step is to find the url for dataset on the CSO.ie website. 
# I import json to work with the file and parse the data.
# I request the data using the url and retrieve the data from the server and store the response.
# I check if the file has been retrieved sucessfully and save it to a json file, if the file does not exist it will create it.
# I print the response. If the file has not been retrieved, depending on the status code, it will advise that it has failed to retrieve the data.


import requests
import json

url = "https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%5D,%22dimension%22:%7B%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22JSON-stat%22,%22version%22:%222.0%22%7D,%22matrix%22:%22FIQ02%22%7D,%22version%22:%222.0%22%7D%7D"

response = requests.get(url)

data = response.json()

if response.status_code == 200:
    with open ("cso.json", "w") as fp:
        json.dump(data, fp, indent=4)  
        print("Data saved to cso.json")  
else:
    print(f'Failed to retrieve data. The status code :{response.status_code}')
