# Gophers and Holes

### Description
There are **g** gophers and **h** holes, each at distinct **(x, y)** coordinates in meters.  
A hawk arrives and gophers have **s** seconds to reach a hole, otherwise they might get eaten.  
Every gopher runs at the same speed of **v** meters per seconds.  
Each hole can save only one gopher.  
How many gophers can we save from hawk with optimal strategy?

### Solution
Ford-Fulkerson algorithm computes maximal bipartite matching.  
OOP is used for visualising the results and recontstructing one of the optimal solutions.

### Source 
Exercise description : Waterloo Programming Contest 2001-01-27  
Ford-Fulkerson : https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
