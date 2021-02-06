
# https://courses.edx.org/courses/course-v1:HarvardX+CS50AI+1T2020/course/
# https://www.youtube.com/watch?v=D5aJNFWsWew&feature=youtu.be


# Approach
# Start with a frontier that contains the initial state 
# Repeat:
#     if the frontier is empty, then no solution 
#     Remove a node from frontier
#     if node contains goal state, return solution 
#     Expand node, add resulting nodes to the frontier 


# Revised Approach
# Start with a frontier that contains the initial state 
# -> Start with an empty explored set <-
# Repeat:
#     if the frontier is empty, then no solution 
#     Remove a node from frontier
#     if node contains goal state, return solution 
#     -> Add the node to the explored set <-
#     -> Expand node, add resulting nodes to the frontier if they aren't already in the frontier or explored set 


# treat frontier as stack
# Depth-first search
# Stack: last-in first-out


# Breath-first search
# queue: first-in first-out



# uninformed search:
#     search startegy that uses no problem specific knowledge

# informed search:
#     search startegy yhat uses problem-specific knowldge to find solutions more efficiently


# greedy best-first search:
#     search alogrithm thats expands the node that is closest to the goal, as estimated by a heuristic function h(n)

# manhattan distance 


# A * search:
#     search algorithm that expands node with lowest value of g(n) + h(n)
    
# g(n): cost to reach node 
# h(n): estimated cost to goal 


