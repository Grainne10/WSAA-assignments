# WSAA-Assignments

**by Grainne Boyle**

**Contents:** 

1. [Overview](#Overview)
2. [Tasks](#Tasks)
3. [Requirements](#Requirements)
4. [References](#References)

## Overview  

I work at [TE Connectivity] (https://www.te.com/usa-en/home.html)  

I am a student at the [Atlantic Technological University] (https://www.atu.ie/), Galway, studying the Higher Diploma in Science in Data Analytics on a part-time basis over 2 years.    

This repository contains a collection of weekly assignments completed for the Web Services and Applications module. Each notebook or script demonstrates the use of Python for interacting  with web API's, handling data in real time and automation of web-based tasks. The files demonstrate programming techniques such as HTTP requests, JSON parsing, file handling and working with libraries like requests and PyGithub. In this read me, I document the weekly assignments with an explanation of the task, the approach I took to solve it and relevant research. 
Additionally, I completed two online assessments, which test what I have learned during the course. These assessments provide insight into my understanding of web services , API intergration and Python development. 


## Tasks   

### Task 1: Card Draw  

#### Task Description:  
Write a program that uses the Deck of Cards API to shuffle a deck, draw 5 cards, and print their values and suits. Then check the hand for pairs and triples and congratulate the user accordingly.  

#### Task Solution:  
The script demonstrates how to make HTTP requests using the requests library in Python and how to handle and interpret the response from the Deck of Cards API, including checking for success or failure using status codes (e.g., 200 for success, 404 for not found).The API response is in JSON format, and I show how to parse this format using response.json and extract meaningful data from the api. I also demonstrate how to dislay images from the api data. The script shows how to interact with an external web service in realtime.  

I start by importing the necessary libraries - requests for making HTTP requests and IPython.display for displaying images.  The first step in the process pulls in and shuffles a new deck of cards by sending a GET request to the Deck of Cards API and checks whether it was successful. The response is parsed in JSON format, allowing me to retrieve the deck_id needed for subsequent actions. After successfully obtaining the deck ID, the script makes another request to draw 5 cards from the deck. The script then checks the drawn cards for pairs or triples. It uses a dictionary to count the occurrences of each card value and displays a congratulatory message if a pair or triple is found. If neither is found, it lets the user know that no pair or triple was drawn.  

### Task 2: CSO  

#### Task Description:  
Write a short Python program to download the "Exchequer Account(Historical Series)" dataset from CSO.ie and save it as CSO.json.  

#### Task Solution:  
The script usees the requests library to send an HTTP GET request to a specific URL. When the response from the API is received, the response.json method is used to parse the JSON data into a Python data structure. The script use the status codes to check if the API response was successful. The 200 status code indicates that it was successful, the other status codes generally indicate an error has occured. If the data has been retrieved successfully, the script writes the data to a file using Python's json.dump(method). This stores the data in a local file for future use. The script opens a file cso.json and writes to it using with open().  

I start by importing the libraries needed , requests and json. I define the url, this is the API CSO endpoint from which I want to retrieve the data. I send a GET request to the URL to retrieve the data from the server. Using response.json I parse the response content into a Python dictionary. I check if the response code is successful using the response.status code. If this is 200, then I save the data to a JSON file. Using open("cso.json", "w"), it opens a file named cso.json in write mode, if the file does not exist, it will be created. If the status code is not 200, it will return a message to say it failed to retrieve the data.  

### Task 3: Github   

#### Task Description:
Write a Python program that reads a file from a repository, replaces all instances of "Andrew" with your name then commits and pushes the changes back.  

#### Task Solution:  
This script automates the process of fetching a file from a GitHub repository, performing a text replacement within that file, and then updating the modified file back to the repository. The script uses the PyGithub library to interact with the GitHub API and the requests library to download the file content.  

I import the necessary libraries - PyGithub, Requests and a Github API key configured in a file config.py. I saved the github key in the file config.py and I entered the name of the config.py file in my .gitignore file so that it would not upload the file with the private key to Github. The script fetches the file andrew.txt from the specified GitHub repository Grainne10/aprivate one. It performs a search-and-replace operation, replacing occurrences of a target word ("Andrew") with a new word ("Grainne"). The modified content is then committed back to the repository with a commit message. I have added Andrew Beatty as a collaborator on the private file so that he can test that it is working.    

## Requirements  
To review the dependencies please review the requirements.txt file.  


## References  
* [Import Requests](https://realpython.com/python-requests/) - This explains how to to import and get requests.  
* [Display Picture](https://www.reddit.com/r/learnpython/comments/coho06/displaying_picture_from_api_in_jupyter_notebook) - This shows you how to import an image from an api.  
* [Response Statements](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) - Understanding what the response statements mean.  
* [JSON](https://www.w3schools.com/js/js_json_intro.asp) - Tutorials on json.  
* [API's](https://www.geeksforgeeks.org/a-comprehensive-guide-to-api-development/) - Explaining and Learning API's.   
* [Postman](https://www.youtube.com/watch?v=wEOLZq-7DYs) - Learn how to use Postman.   
* [Curl](https://www.roborabbit.com/blog/how-to-use-curl-in-python-with-examples/) - Using Curl in Python to send http requests.  
* [CSO](https://www.cso.ie/en/index.html) - Resources including json files , api's, databases.  
* [Github](https://docs.github.com/en/rest?apiVersion=2022-11-28) - Restful API documentation on Github docuements.  
* [Security](https://blog.gitguardian.com/secrets-api-management/) - Managing security for API keys.  
* [Replacing Text](https://www.tutorialspoint.com/How-to-search-and-replace-text-in-a-file-using-Python) how to find and replace.  