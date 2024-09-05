Abstract
The document outlines a strategic game called the Prime Game, played between two players, Maria and Ben, who alternately select prime numbers from a set of consecutive integers. The player unable to make a move loses, and the goal is to determine the winner over multiple rounds based on varying values of n. The function isWinner computes the overall winner based on optimal play, demonstrating that Ben often emerges victorious given the rules of the game.

Key Points
The Prime Game involves players choosing prime numbers from the integers 1 to n and eliminating those numbers and their multiples from the game.
Maria plays first, and both players are assumed to play optimally to maximize their chances of winning.
The main function isWinner takes in the number of rounds x and a list of integers nums representing different values of n for each round.
The function returns the name of the player who wins the most rounds or None if the winner cannot be determined.
An example illustrates the game mechanics with three rounds resulting in Ben winning the majority of the rounds.
The analysis clarifies the outcomes based on the initial set of numbers and the choices made by each player in their turns.
Assumptions include that n and x will not exceed 10,000, and the use of any imports in the solution is prohibited.
