# Car Parking Lot Problem v2
 
<p> The goal of this problem is to demonstrate some of the algorithms we studied in course CS340 (Artificial Intelligence). The notebook will cover the car parking lot problem in detail, explaining how the algorithms work and how well they perform, as well as comparing their performance relative to each other by highlighting visible differences and the time it takes them to solve the problem, and finally concluding with which algorithm provided the most optimal solution. </p>

# Contents
 
1. [What is Car Parking Lot Problem](#what-is-car-parking-lot-problem)
2. [CSP Model Of The Car Parking Lot Problem](#csp-model-of-the-car-parking-lot-problem)
3. [Problem Formulation](#problem-formulation)
4. [Explanation of The Algorithms](#explanation-of-the-algorithms)
5. [Performance Comparison of The Algorithms](#performance-comparison-of-the-algorithms)



## What is Car Parking Lot Problem

It is a Constraints Satisfaction Problem (CSP), where you have a parking lot with a number of separate parking zones, each zone has the same number of parking spots. Each parking spot must be assigned a car without violating any constraints. The domain of all parking spots is a random combination from a number of colored cars, the solution is reached only when the parking lot has no other available parking spot.

## CSP Model Of The Car Parking Lot Problem

In any CSP there are 3 components and the Car Parking Lot Problem is no different:
<ol>
 <li> Variables </li>
 <li> Domains </li>
 <li> Constraints </li>
</ol>

So, **what does Variables represent in the Car Parking Lot Problem?** Each parking spot is considered as a variable.

**What are the domains of the Car Parking Lot Problem?** It is actually a single finite domain for all variables in the problem. Noted that with each variable assignment the domain is reduced for the next variables.

**What are the constraints in the Car Parking Lot Problem?** Each adjacent variable must have a different value.
 
 <br />
 
<p> Consider the constraints graph below to see what the structure of relations or constraints are. The graph is based on a simple two-zone parking lot with 20 parking spots. </p>

 <br />
 
![Two zone parking lot.png](https://github.com/mohammadbinzouman/Car-Parking-Lot-Problem-v2/blob/main/Google%20Colaboratory%20Images/Two%20zone%20parking%20lot.png)

<br />
 
![Two zone parking lot.png](https://github.com/mohammadbinzouman/Car-Parking-Lot-Problem-v2/blob/main/Google%20Colaboratory%20Images/Constraint_Graphs.png)
 
<p> The constraints graph represents two independent graphs, one for each zone, which when joined create the parking lot. </p>

<br />

<p> And for what a solution should look like in the Car Parking Lot Problem, a solution is reached if and only if the given parking lot has all its parking spots assigned appropriately, in respect to the constraints on each parking spot, some may have no solution and some have many solutions but, when there’s a solution there’s always an optimal solution. Consider the two figures example below of a 3 zones parking lot with 30 random color cars, where figure 1 with a solution and figure 2 without a solution. </p>

![Sorted Car Parking Lot.png](https://github.com/mohammadbinzouman/Car-Parking-Lot-Problem-v2/blob/main/Google%20Colaboratory%20Images/Sorted%20Car%20Parking%20Lot.png)
Figure 1: all parking spots assigned, without violating any constraints.

<br />

![Unsorted Car Parking Lot.png](https://github.com/mohammadbinzouman/Car-Parking-Lot-Problem-v2/blob/main/Google%20Colaboratory%20Images/Unsorted%20Car%20Parking%20Lot.png)
Figure 2: all parking spots assigned **BUT**, the constraints were violated therefore it's not a solution.

<br />

<p> Here is an example shown in the GIF presenting a solution, for a 6 zones parking lot with the domain having 60 cars which was produced randomly from a 4 possible car colors combination. </p>

![SortingGif.gif]()

## Problem Formulation

<p> The initial state of the Car Parking Lot Problem is an empty parking lot. As shown in the figure below. </p>

![parking_lot_layout.PNG]()

<br />

<p> The actions in the Car Parking Lot Problem are to assign each adjacent parking spot from first parking spot to the last parking spot. see figure below. </p>

![Intial State.png](https://github.com/mohammadbinzouman/Car-Parking-Lot-Problem-v2/blob/main/Google%20Colaboratory%20Images/Intial%20State.png)

<br />

<p> A state space graph showing the initial state, actions and goal state. </p>

![Space State.png](https://github.com/mohammadbinzouman/Car-Parking-Lot-Problem-v2/blob/main/Google%20Colaboratory%20Images/Space%20State.png)

<br />

<p> The heuristic used for the Car Parking Lot Problem implementation is to start from the first parking spot to the last parking spot, taking in mind the preferred value for each variable and is as follows: red->blue->green->yellow->indigo->orange->violet of the order from best to worst, obviously it depends on the random generated domain. Observe the GIF below. </p>

![OneZoneSortingGif.gif]()
*Parking lot with 1 zone solved from a random generated domain using 7 possible colors.

## Explanation of The Algorithms

### Backtracking

<p> Backtracking algorithm has the simplest straightforward approach, it assigns each variable(parking spot) based on the preferred values if available from the domain and only backtrack when a parking spot has no valid value to be assigned with, so the algorithm backtracks to the previous parking spot trying next preferable value until no value can satisfy parking spot, so it backtrack to more previous parking spots, until a solution is found or no solution is found. see GIF below (same problem on all three algorithms). </p>

### Forward Checking

<p> ForwardChecking algorithm works as follows when a variable (Parking spot) gets assigned, adjacent parking spots remove values that might violate a constraint when chosen, thus filtring bad values, this process continues to the end unless one of the parking spots ends's up filtering all of its values, then it will backtrack to the previous parking spot and try assigning another value until a solution is reached or otherwise no solution found and the result is a failure. see GIF below (same problem on all three algorithms). </p>

### Arc Consistency

<p> Arc Consistency was implemented in the Car Parking Lot Problem as a preprocessor, reducing the parking spot domain of values starting from the first spot to the last spot respecting the constraints, the algorithm assigns each parking spot with preferable values if available from best to worst, and that’s called ascending order, if there are no solutions then the algorithm tries the descending order from worst to best, if no solutions then the algorithm stops and the result is a failure or can’t be solved using Arc Consistency algorithm. see GIF below (same problem on all three algorithms). </p>

## Performance Comparison of The Algorithms

we will consider three performance factors:

1. Time taken for a result.
2. Success ratio.
3. Most optimal solutions.
The test on the algorithms is using the following characteristics, a parking lot with 3 zones and 4 color combinations, that is 30 parking spots and 30 random colored cars.

Note that the domain for each test run is random, therefore not every domain generated has a solution.

The test has ran 50 times, and the results for each algorithm is shown below:
