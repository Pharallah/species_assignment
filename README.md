# Species Assignment For Ama Earth Group

## Assignment Instructions
Directions: Ama Earth Group is excited to see your creativity and technical skills in backend development. For this take-home assignment, your task is to create a simple RESTful API that provides information about native species in Puerto Rico. The API should include one primary endpoint, /species, which returns a JSON list of species with their common names, scientific names, and brief descriptions. The data can be hardcoded, so there’s no need to set up a database. The API should run locally on your computer, and you are free to use any programming language or framework you are comfortable with, such as Python Flask or Node.js Express. Please include clear instructions for running the API and testing the endpoint.

## Instructions: Testing The API

  You will need Postman to test the API.
  If you don't have it downloaded already, you can do so here: https://www.postman.com/downloads/

  1. Fork & clone this repo in your local computer
  2. Open project in a code editor like VSCode
  3. Open terminal within the code editor and change directory into the project's 'server'
  4. Run 'python app.py' to start the server.
  5. Once the server is running, open Postman app.
  6. Copy the URL address where the server is running (this is found in the terminal) & paste into Postman.
  7. Before clicking 'Send', make sure you add the '/species' URL endpoint in Postman.
  8. If done correctly, hitting 'Send' should show the JSON of the species list.