# Routing Program
I created this program for my Data Structures and Algorithms Class. I implemented an algorithm to route delivery trucks that will allow me to meet all delivery deadlines while travelling the least number of miles. I had to route three trucks, two drivers and an average of 40 packages to deliver each day; each package had specific criteria and delivery requirements.

## Summary
The algorithm used for this project was a greedy algorithm.

The algorithm has three main parts:

First the packages are sorted according to priority. The packages with deadlines are appended first into the delivery list, then packages with specific instructions are added, then delayed packages, and then EOD(end of day) delivery packages are added. The packages are loaded into three trucks and the route is established.

The second part finds the fastest route around the city. The algorithm works in this manner:
  * Find the closest location from the hub.
  * Use that location to find the next closest location. 
  * Call the function recursively for each closest location in that route.

The third part delivers the packages. The route is stored in a dictionary with the location and distance in order. The program loops through the route and then for each route loops through the delivery list to find the package for that location and then delivers the package. The mileage and time are updated.


Operation time for sorting the packages is O(n) as it loops through the package list for each condition. The operation time for finding the closest route will also be O(n). The running time for delivering the package will be O(n^2) because the code loops through the route dictionary and then loops through the delivery list to get the packages for that location. The operation time for the program is O(n^2).

## Concepts Learned
  * Creating software applications that incorporate non-linear data structures for efficient and maintainable software.
  * Writing code using hashing techniques within an application to perform searching operations.
  * Incorporating dictionaries and sets in order to organize data into key-value pairs.
  * Evaluating the space and time complexity of self-adjusting data structures using big-O notation to improve the performance of applications.
  * Writing code using self-adjusting heuristics to improve the performance of applications.
  * Evaluating computational complexity theories in order to apply models to specific scenarios.
