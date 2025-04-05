# WSAA-Assignments
Project for for the Web services and Applications module, part of the HDip in Data Analytics

Contents


Tasks
assignment 2 Card Draw
The script demonstrates how to make HTTP requests using the requests library in Python and how to handle and interpret the response from the Deck of Cards API, including checking for success or failure using status codes (e.g., 200 for success, 404 for not found).The API response is in JSON format, and I show how to parse this format using response.json and extract meaningful data from the api. I also demonstrate how to dislay images from the api data. The script shows how to interact with an external web service in realtime.

I start by importing the necessary libraries - requests for making HTTP requests and IPython.display for displaying images.  The first step in the process pulls in and shuffles a new deck of cards by sending a GET request to the Deck of Cards API and checks whether it was successful. The response is parsed in JSON format, allowing me to retrieve the deck_id needed for subsequent actions. After successfully obtaining the deck ID, the script makes another request to draw 5 cards from the deck. The script then checks the drawn cards for pairs or triples. It uses a dictionary to count the occurrences of each card value and displays a congratulatory message if a pair or triple is found. If neither is found, it lets the user know that no pair or triple was drawn.

assignment 3 CSO

The script usees the requests library to send an HTTP GET request to a specific URL. When the response from the API is received, the respons.json method is used to parse the JSON data into a Python data structure. Ths script use the status codes to check if the API response was successful. The 200 status code indicates that it was successful, the other status codes generally indicate an error has occured. If the data has been retrieved successfully, the script writes the data to a file using Python's json.dump(method). This stores the data in a local file for future use.
The script opens a file cso.json and writes to is using with open()

I start by importing the libraries needed , requests and json. I define the url, this is the API CSO endpoint from which I want to retrieve the data. I send a GET request to the URL to retrieve the data from the server. Using response.jsp I parse the response content into a Python dictionary. I check if the response code is successful using the response.status code. If this is 200, then I save the data to a JSON file. Using open("cso.json", "w"), it opens a file named cso.json in write mode, if the file does not exist, it will be created. If the status code is not 200 , it will return a message to say it failed to retrieve the data.

assignment 4 github
This script automates the process of fetching a file from a GitHub repository, performisng a text replacement within that file, and then updating the modified file back to the repository. The script uses the PyGithub library to interact with the GitHub API and the requests library to download the file content.

I import the necessary libraries - PyGithub, Requests and a Github API key configured in a file config.py. 
The script fetches the file andrew.txt from the specified GitHub repository. It performs a search-and-replace operation, replacing occurrences of a target word ("Andrew") with a new word ("Grainne"). The modified content is then committed back to the repository with a commit message.



https://www.tutorialspoint.com/How-to-search-and-replace-text-in-a-file-using-Python