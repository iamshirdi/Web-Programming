## Mini game backend server application using http.server- Python

Run using python app.py<br>
Hosted on localhost and port 8080<br>
Internal Data Storage in JSON <br>
Requests and Responses are in JSON<br>
Valid request 200 and invalid 404

### login
userid-31bit unsigned integer<br>
sessionkey- alphanumeric and Capitalization<br>
if userid not there generated new session key and time on fly<br>
returns session keys if session=600s didnt expire<br>
if expired removes from database and creates new<br>

### score post_data
levelid- 31bit unsigned int<br>
score-31bit unsigned int <br>
checks if valid sessionkey and updates<br>
database_scores is updated and returned if previous high score  of the user present and less than present<br>
added directly to database if unique user(above condition not executed) and less than top 15 <br>
else more than 15 unique users present check and remove low score from database_scores

### highscorelist
formatted order retrived from top 15 database_scores<br>
score descending<br>
userid ascending <br>
empty list if not found in database_scores
