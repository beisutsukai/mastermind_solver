# Mastermind game solver
# ----------------------

This program can be used to solve Mastermind using information theory to find the optimal solution (find the coimbination with a minimum number of guesses).

To use it, load all the functions in main.py. Then, you can solve your first game by replicating the steps in example_game.py 
You can configure the size of the combination (usually, a mastermind game involves four or five boxes). But the solver will be very slow for six boxes and over.

This program was inspired by this video, where an equivalent for the Wordle game is shown : https://scienceetonnante.com/2022/02/13/comment-craquer-le-jeu-wordle-sutom/

As you can see in the example, the first guess does not matter too much : any first guess will on average, give more or less the same amount of information. 
This is a major difference with Wordle, where some letters are more commons than others, 
the other difference being that the hints only tells how many colors are in the combination (white hints) and in the right position (red hints). But you don't know which ones are correct.

The first calculation being the longest, it is recommended to hardcode it, rather than redoing it every game.

