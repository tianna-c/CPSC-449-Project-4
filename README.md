###### Github Link: https://github.com/tianna-c/CPSC-449-Project-4
###### Program: Project 4
###### Authors: Tianna Cano, Patrick Lin, Raymond Magdaleno, Mark Wiedman
###### Date   : 5/6/2022 
 
  # Database and Microservices Initialization
- **You can clone this github repo or download and extract the folder onto your machine.**

- **It is required to run the AnswersDB.py and WordsDB.py files before running the procfile! _This is to create and initialize the databases if they do not already exist._**
<br> `$ python3 AnswersDB.py`
<br> `$ python3 WordsDB.py`

- **Then you run the procfile using foreman**
<br> `$ foreman start`
![VirtualBox_Tuffix 2020 Edition_08_04_2022_19_58_09](https://user-images.githubusercontent.com/39601543/162554364-03d65d09-02ec-4de7-83a5-5adcbb0efc2d.png)

# Game State Microservice
> Commands in File "Track.py"<br>
> Description: 'Track.py' handles tracking the start of a new game to ensure users cannot play a game they have already finished, updating the amount of guesses a user has made, and restoring the state of a game with words the user has guessed & number of remaining guesses. 
              
              /game-start/{userID}/{gameID}  - 
              /game-update/{userID}/{gameID}  - 
              /game-restore/{userID}/{gameID}  - 

1. /game-start/{userID}/{gameID}
      The '/game-start/{userID}/{gameID}' command will XXXXXXXXXXXXXXXXXXXXXXXXX.
   
   ![VirtualBox_Tuffix 2020 Edition_08_04_2022_19_58_09](https://user-images.githubusercontent.com/39601543/162554364-03d65d09-02ec-4de7-83a5-5adcbb0efc2d.png)
###### ^Above image should be replaced 

2. /game-update/{userID}/{gameID}
      The '/game-update/{userID}/{gameID}' command will XXXXXXXXXXXXXXXXXXXXXXXXXXXX.
   
   ![VirtualBox_Tuffix 2020 Edition_08_04_2022_19_58_09](https://user-images.githubusercontent.com/39601543/162554364-03d65d09-02ec-4de7-83a5-5adcbb0efc2d.png)
###### ^Above image should be replaced 

3. /game-restore/{userID}/{gameID}
      The '/game-restore/{userID}/{gameID}' command will XXXXXXXXXXXXXXXXXXXXXXXXXXXX.
   
   ![VirtualBox_Tuffix 2020 Edition_08_04_2022_19_58_09](https://user-images.githubusercontent.com/39601543/162554364-03d65d09-02ec-4de7-83a5-5adcbb0efc2d.png)
###### ^Above image should be replaced 
   
