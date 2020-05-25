# snakes_and_ladders

A simple python code for snake and ladder game

Source Code:
------------

`<https://github.com/BHushanRathod/snakes_and_ladders.git>`_


Installation and Usage
======================

Download the souce code::
       
    $ git clone https://github.com/BHushanRathod/snakes_and_ladders.git
   
Activate the Virtual Environment::

    No venev requreied

Install the Dependencies::

    pip install -r requirements.txt (No additional packages required.)

Run/Start::
    
    python3 snakeladder.py
    
* Steps to follow:
    * open terminal, run above code
    * Enter Player_1 and Player_2 names        
    * Press Enter to roll a dice, Q/q to Quit.
    
* Algorithm Working:
    * Game board is of size 1 to 100.
    * Game starts at position 1 for both the players.
    * Game consists of snakes and ladder at particular cells. 
    * If player hits the cell with snake head, he'll get down to the cell having tail of snake.
    * If player hits the cell with base of the ladder, he'll get Up in the cell having top end of ladder.
    * First player to enter 100th cell, wins the game.
    * Player can quit the game anytime before rolling the dice by pressing 'Q' or 'q'.
