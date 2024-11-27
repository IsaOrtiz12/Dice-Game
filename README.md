# Dice-Game
This project is a game made for INST126

Dice game
The Tuple Out Dice Game is a fun dice game simulation. Players roll dice, strategize re-rolls, and aim to score the highest points or reach a target score first. The game includes exciting features like ranks, bonus dice, and a "Demon Die" mechanic for extra challenges!

Features
In this game, players roll three dice during their turn. They can re-roll non-fixed dice (dice that don’t share the same value as another) to try for a higher score but must avoid “tuple out,” which happens when all three dice show the same number which results in zero points. Rolling three ones activates a Bonus Die, multiplying the score by the bonus roll number of a fourth die. Rolling three sixes triggers the Demon Die mode, where a fourth roll is subtracted from 18 to determine the player's score. Based on final scores, players receive the following ranks:  Noob, Nonchalant, Expert, or Legend.

How to Play
To play, run the game in Python, set a target score, and specify the number of players. Players take turns rolling dice and can re-roll non-fixed dice until they choose to stop or “tuple out.” The turn score is the sum of all dice unless special conditions like the Bonus Die or Demon Die are triggered. Play continues until a player reaches or exceeds the target score or if they tuple out!

Example Gameplay
A player starts with [1, 2, 2]. The 2's are fixed, and the player re-rolls the 1, getting [4], then stops for a score of 8. Another player rolls [6, 6, 6], activating the Demon Die, rolling [4] to finalize their turn score as 14 (18 - 4). Later, a player rolls [1, 1, 1], activating the Bonus Die, rolling [5], and scoring 15 (3 * 5).

Code Highlights
The program uses Python's random module for dice rolls and modular functions to manage gameplay, such as rolling dice, calculating scores, and assigning ranks based on those scores. The turn-based system ensures fairness and includes clear prompts for user input. Players are ranked based on their total scores at the end, creating an engaging and competitive experience.