# 4 Player Chess AI
## How does 4 Player Chess work
Team-based 2v2 Chess Variant on a 14x14 board
Teams: Red, Yellow | Blue, Green
Once any player is checkmated, game over, other team wins! 
Move order: red, blue, yellow, green

Board:
<img width="512" alt="Screenshot 2024-11-05 at 2 56 20 PM" src="https://github.com/user-attachments/assets/6428186d-6681-465d-9b97-29189d24f0b9">

## Why devlop a 4 Player Chess AI
We all have a strong interest in Chess, but the normal 2 player version of Chess has had extensive AI 
research done already. So we decided we wanted to challenge ourselves and come up with something new 
while still in the field of Chess so we settled on making our AI for 4-Player/Team Chess

## Key differences from Normal Chess AI
Many more pieces and more squares so the state space is significantly larger in 4 player chess than in 
2 player chess. This makes predictions much more computationally expensive. 
We also had to consider teamplay in our AI as how well you work with your teammate has a major affect
in this version of Chess

## Methodology
Implemented move ordering, Pre-ordering the move list so that the best moves get searched first, 
this combined with alpha beta pruning helped mitigate the large state space.
Implemented global search classes to avoid re-searching between rational moves. (This greatly improved
speed allowing for better play testing against the AI)
The algorithm we used is a modified minimax function, that lets the search agent find teammate interaction 
by setting teammates to both be maximizing (or minimizing) agents. We combined this with a custom evaluation 
function that evaluates a board based on the value of the pieces left on the board as well as the safety of 
the King (susceptibility to checkmate)

## Results
Was able to beat a randomly moving AI 100% of the time.
Was able to beat real human playes aboput 50% of the time. Our AI was really good at utilizing teammoves to 
make checkmates, but in more nuanced situations where there is no obvious piece to take or checkmate or no 
obvious set up to get you there it had trouble coming up with good moves.

## Demo
https://github.com/user-attachments/assets/0cb1c07b-7be9-4332-b59a-481c700dba3c 

## Potential Improvements
Using a reinforcement learning algorithm like Q learning to learn the expected value of different board 
states could result in a strong performing AI.
Adding things like pawn structure to the evaluation function could help the AI choose moves when there is
no obvious optimal move.


## Other notes
GUI and Initial Code Modified from:
https://github.com/GammaDeltaII/4PlayerChess

We modified code to allow for play using artificial actors. This includes adding legal moves incorrectly
handled by the original codebase. However, some of the functionality from original codebase is not fully
supported with our changes.


