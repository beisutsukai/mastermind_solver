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


## How it works

The program tries to find the combination that gives the most information. If we start with a 4 boxes game, there are 4096 possible combinations.
The program will evaluate every combination, and calculate : for every patterns of hints possibles, how many possible combinations will remain ? 
What we want is the combination, that, on average, will leave the fewest possibilities.

Let's take a simple example, with two possible patterns : if the combination gets pattern 1, there will be 4 combinations left, and if it gets pattern 2, 6 combinations left. 
So on average there will be : (4 * 4) / (10 * 10) + (6 * 6) / (10 * 10) = 52% of the initial combinations left.

If we evaluate another combination, that gets  5 combinations left with pattern 1, and 5 with pattern 2.
So on average there will be : (5 * 5) / (10 * 10) + (5 * 5) / (10 * 10) = 50% of the total combinations left. This second combination is better, because on average, there will only be 5 combinations left after we try it, instead of 


To represent the information given by a combination, we can compute its expected entropy reduction, as in the scienceetonnante.com example.
For instance, the second combination reduces by half the entropy. So Information = log2(0.5) = 1 bit.

The program will select the combination with the highest expected average information. Then, you can try it, see the results, and start the next step, until you find the solution.