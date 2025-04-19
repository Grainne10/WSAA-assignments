## Assignment 4 Github
### Grainne Boyle
### Task - Write a progrma in python that will read a file from a repository. The program should replace all the instances of the text "Andrew" with your name. Then the program should commit those changes and push the file back to the repository.

# I have installed PyGithub and I import Github to allow me to interact with the Github repository. I also import the requests library to enable the program to make requests e.g. to download the file from github.
# I have stored the apikey in a file called config.py. This is needed as Github will provide a key to allow you to interact with it. I import the config file as cfg.
# Note = I added the config file to my git ignore so that it is not uploaded to Github.

from github import Github
import requests
from config import config as cfg

apikey = cfg["mygithubkey"]
 # I authenticate the key with Github
g = Github(apikey)

# I fetch the repository "Grainne10/aprivateone" 

repo = g.get_repo("Grainne10/aprivateone")

# This retrieves the contents of the file""andrew.txt"

fileInfo = repo.get_contents("andrew.txt")
# The download URL of the file is extracted from fileInfo.

# A GET request is sent to this URL using the requests.get() method to fetch the file's contents.

# The content of the file is saved in the contentOfFile variable
urlOfFile = fileInfo.download_url

response = requests.get(urlOfFile)
contentOfFile = response.text

# A function is created to search the file for a word and to replace the word.
def search_and_replace(contentOfFile, search_word, replace_word):
    update_content = contentOfFile.replace(search_word, replace_word)
    return update_content

# function is called and it replaces the word Andrew with Grainne. I have tested this and it works, if you want to test again, you can change the name Grainne to Andrew or whatever you wish it to be.
updated_content = search_and_replace(contentOfFile, "Andrew", "Grainne")
# This shows the updated file, showing that Andrew has been replaced with Grainne
print(updated_content)

# This uploads the modified file back to the GitHub repository and gives a response if uploaded.

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog", updated_content,fileInfo.sha)

print (gitHubResponse)

# Please note:
# You can check the file on the repository, I have added Andrew Beatty as a collaborator on the "Grainne10/aprivateone" so that Andrew can view the file I updated and can test for himself.