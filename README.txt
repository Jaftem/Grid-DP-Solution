README for grid.py
-------------------------------------------------------------------------------------------

Script was written in Python 3.6.0.

To run:
  $ python grid.py
Or
  $ python3 grid.py

* Then enter the grid size (rows by columns), enter, the blocked coordinates, enter, the
  jump coordinates.

* Input does not require parenthesis or nested parenthesis, but you can use these if you
  wish (for eg. ((2,1),(0,3)) is the same as 2 1 0 3 is the same as (2 1), (0 3)). Just
  make sure to separate numbers with a space or [(),]. Alternatively press enter if you
  wish to have no blocking coordinates or jumping coordinates.

* Did not create any error checking on inputs. Out of bounds coordinates will crash
  program. Non-numerical inputs will likely crash program.

* Coordinate (i, k) is i-th row and k-th column.


Design Decisions
-------------------------------------------------------------------------------------------

Initially I thought I could solve this problem using backtracking, but before I started co-
ding I wrote out some examples of the problem on paper and realized each node's total path
count is just the sum of the bottom and right nodes' path counts given the constraint that
each unit of work has to be one step closer to the goal state or a jump. This then turned
the problem into a DP problem.

Solving jumps was just a matter of assigning the jumping node's path count to goal state
to the 'landing' node's path count and then recomputing the path counts for all nodes above
and to the left of this jump node.

I was not completely sure if the assignment required implementation of jump chaining. For
eg., if (2,1) jumps to (1,2) and (1,2) jumps to (3,4). As written, the program should
output the correct answer if jump coordinates are given in the input in the following
order:
	(((1,2),(3,3)), ((4,4),(1,2)))

Jump loops are unaccounted for (For eg., (1,2) to (2,1), etc).


Thanks!