# WSAA-Assignments
Project for for the Web services and Applications module, part of the HDip in Data Analytics

Contents


Tasks
assignement 2 Card Draw
The script demonstrates how to make HTTP requests using the requests library in Python and how to handle and interpret the response from the Deck of Cards API, including checking for success or failure using status codes (e.g., 200 for success, 404 for not found).The API response is in JSON format, and I show how to parse this format using response.json and extract meaningful data from the api. Ie also demonstrate how to dislay images from the api data. The script shows how to interact with an external web service in realtime.

I start by importing the necessary libraries - requests for making HTTP requests and IPython.display for displaying images.  The first step in the process pulls in and shuffles a new deck of cards by sending a GET request to the Deck of Cards API and checks whether it was successful. The response is parsed in JSON format, allowing me to retrieve the deck_id needed for subsequent actions. After successfully obtaining the deck ID, the script makes another request to draw 5 cards from the deck. The script then checks the drawn cards for pairs or triples. It uses a dictionary to count the occurrences of each card value and displays a congratulatory message if a pair or triple is found. If neither is found, it lets the user know that no pair or triple was drawn.
