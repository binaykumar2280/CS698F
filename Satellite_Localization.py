#Question 3


import numpy as np
from scipy import constants
import random
from statistics import mean
import matplotlib.pyplot as plt
#  (a)
#Fix the user at (100,100,100). Put 5 satellites at any random locations (you can
#manually put their locations), and fix their positions. Now calculate the time it
#takes for a signal to arrive from each one of these satellites to the user.

print("Below is the solution of 3-(a):\n")
object = np.array((100,100,100))

#location of 5 satellites
satellite_1 = np.array((1009,1013,1019))
satellite_2 = np.array((1171,1181,1187))
satellite_3 = np.array((1409,1429,1459))
satellite_4 = np.array((1559,1693,1709))
satellite_5 = np.array((1823,1873,1999))

print(f"Coordinate of 1st satellite : {satellite_1}\n")
print(f"Coordinate of 2nd satellite : {satellite_2}\n")
print(f"Coordinate of 3rd satellite : {satellite_3}\n")
print(f"Coordinate of 4th satellite : {satellite_4}\n")
print(f"Coordinate of 5th satellite : {satellite_5}\n")

#computing the ranges for each satellite
		
range_sat1 = np.linalg.norm(satellite_1 - object)
range_sat2 = np.linalg.norm(satellite_2 - object)
range_sat3 = np.linalg.norm(satellite_3 - object)
range_sat4 = np.linalg.norm(satellite_4 - object)
range_sat5 = np.linalg.norm(satellite_5 - object)

#printing the times it takes to reach the GPS device
time_sat1 = (range_sat1) / (constants.c)
time_sat2 = (range_sat2) / (constants.c)
time_sat3 = (range_sat3) / (constants.c)
time_sat4 = (range_sat4) / (constants.c)
time_sat5 = (range_sat5) / (constants.c)
 
print(f"Time for satellite_1 : {time_sat1}\n") 
print(f"Time for satellite_2 : {time_sat2}\n") 
print(f"Time for satellite_3 : {time_sat3}\n") 
print(f"Time for satellite_4 : {time_sat4}\n") 
print(f"Time for satellite_5 : {time_sat5}\n") 


#  (b)
#Now lets do the opposite operation, i.e. use the satellite locations and the
#times to find out the location of the user. Check whether it is coming exactly
#as (100,100,100).

print("Below is the solution of 3-(b):\n")

#satellite location remains same
#Here we will be using only 4 satellites as we are not considering
#error due to unsyncronized clock, the 5th satellite will just be 
#redundant
#using the equation in slide 8 of GPS Localization error lecture


#setting the matrices

A = np.array([[(2*(satellite_2[0] - satellite_1[0])),
               (2*(satellite_2[1] - satellite_1[1])),
               (2*(satellite_2[2] - satellite_1[2]))],
              [(2*(satellite_3[0] - satellite_1[0])),
               (2*(satellite_3[1] - satellite_1[1])),
               (2*(satellite_3[2] - satellite_1[2]))],
              [(2*(satellite_4[0] - satellite_1[0])),
               (2*(satellite_4[1] - satellite_1[1])),
               (2*(satellite_4[2] - satellite_1[2]))]])
              

# Here we are taking range1(r1) as time*speed_of_light

a = ((pow(time_sat1*(constants.c),2) - pow(time_sat2*(constants.c),2))
               - (pow(satellite_1[0],2) - pow(satellite_2[0],2))
               - (pow(satellite_1[1],2) - pow(satellite_2[1],2))
               - (pow(satellite_1[2],2) - pow(satellite_2[2],2)))
               
b = ((pow(time_sat1*(constants.c),2) - pow(time_sat3*(constants.c),2))
               - (pow(satellite_1[0],2) - pow(satellite_3[0],2))
               - (pow(satellite_1[1],2) - pow(satellite_3[1],2))
               - (pow(satellite_1[2],2) - pow(satellite_3[2],2)))

c = ((pow(time_sat1*(constants.c),2) - pow(time_sat4*(constants.c),2))
               - (pow(satellite_1[0],2) - pow(satellite_4[0],2))
               - (pow(satellite_1[1],2) - pow(satellite_4[1],2))
               - (pow(satellite_1[2],2) - pow(satellite_4[2],2)))
 
B = np.array([a,b,c])

X = np.linalg.solve(A,B)
print(f"After using the time in 3-(a) the GPS coordinate is : {X}\n")

# (c)
#Now add some random errors with the times (you can use function likes
#“rand” in matlab). Check how much location inaccuracy it showing up.


#introducing a very small random error as 1ms time error can lead to
#300 km range error 

print("Below is the solution of 3-(c):\n")

#This function introduces random error of time and solves the problem using
#trilateration equation
def error(range1):

	delta = random.uniform(-range1,range1) / 1000000
	    
	big_delta = delta * (constants.c)
    
	new_rng1 = range_sat1 - (big_delta)
	new_rng2 = range_sat2 - (big_delta)
	new_rng3 = range_sat3 - (big_delta)
	new_rng4 = range_sat4 - (big_delta)
		
	        
	    
	a = ((pow(new_rng1,2) - pow(new_rng2,2))
               - (pow(satellite_1[0],2) - pow(satellite_2[0],2))
               - (pow(satellite_1[1],2) - pow(satellite_2[1],2))
               - (pow(satellite_1[2],2) - pow(satellite_2[2],2)))
               
	b = ((pow(new_rng1,2) - pow(new_rng3,2))
               - (pow(satellite_1[0],2) - pow(satellite_3[0],2))
               - (pow(satellite_1[1],2) - pow(satellite_3[1],2))
               - (pow(satellite_1[2],2) - pow(satellite_3[2],2)))
    
	c = ((pow(new_rng1,2) - pow(new_rng4,2))
               - (pow(satellite_1[0],2) - pow(satellite_4[0],2))
               - (pow(satellite_1[1],2) - pow(satellite_4[1],2))
               - (pow(satellite_1[2],2) - pow(satellite_4[2],2))) 
    
               
	B = np.array([a,b,c])
    
	X = np.linalg.solve(A,B)
    
	return (X)
    

L_err = error(1)
print(f"After introducing a very small error in time between -1microsecond and 1microsecond we get an location error as : {L_err}\n")

print(f"The localization error is taken as the error distance between object and error location after introducing time error whose value is : {np.linalg.norm(L_err)}\n")
 
#This funtion uses optimization equation to find location by minimizing the error

def minerror(range1):

	delta = random.uniform(-range1,range1) / 1000000
	    
	big_delta = delta * (constants.c)
    
	new_rng1 = range_sat1 - (big_delta)
	new_rng2 = range_sat2 - (big_delta)
	new_rng3 = range_sat3 - (big_delta)
	new_rng4 = range_sat4 - (big_delta)
		
	        
	    
	a = ((pow(new_rng1,2) - pow(new_rng2,2))
               - (pow(satellite_1[0],2) - pow(satellite_2[0],2))
               - (pow(satellite_1[1],2) - pow(satellite_2[1],2))
               - (pow(satellite_1[2],2) - pow(satellite_2[2],2)))
               
	b = ((pow(new_rng1,2) - pow(new_rng3,2))
               - (pow(satellite_1[0],2) - pow(satellite_3[0],2))
               - (pow(satellite_1[1],2) - pow(satellite_3[1],2))
               - (pow(satellite_1[2],2) - pow(satellite_3[2],2)))
    
	c = ((pow(new_rng1,2) - pow(new_rng4,2))
               - (pow(satellite_1[0],2) - pow(satellite_4[0],2))
               - (pow(satellite_1[1],2) - pow(satellite_4[1],2))
               - (pow(satellite_1[2],2) - pow(satellite_4[2],2))) 
    
               
	B = np.array([a,b,c])
    
	P = (A.transpose()) @ A
	I = np.linalg.inv(P)
	Z = (A.transpose()) @ B
	X = I @ Z
    
	return (np.linalg.norm(X-object))
	



#   (d)
#Now increase the amount of the random errors with time, and check what is
#the effect of this change on the localization error. You can plot a graph on the
#amount of timing errors vs localization error to see the effect. You need to run
#the program multiple time and then can take the average localization errors).

print("Below is the solution of 3-(d):\n")

error_array = []

for err in range(11):
    list_err = []
    for average in range(50):
        W = np.linalg.norm(error(err) - object)
#       W = minerror(err)
        list_err.append(W)
        
    
    error_array.append(mean(list_err))
	


def graph_err():
    plt.title('Time Error Vs Localization error')
    plt.xlabel('Time Error in microsecond')
    plt.ylabel('Average Localization Error in metre')
    
    x = list(range(11))
    y = error_array

    plt.scatter(x,y)
    plt.show()

graph_err()

















 
















































































