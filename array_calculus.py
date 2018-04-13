#!/usr/bin/env python3

###
#Daniel Chang
#2260161
#Chang254@mail.chapman.edu
#Myranda Hoggatt
#2285495
#hogga102@mail.chapman.edu
#Devon Ball
#2313078
#dball@chapman.edu
#PHYS220 Spring 2018
#CW06
###Exercise 1

import numpy as np
import matplotlib.pyplot as plt
    
def derivative(a,b,n):
    """ derivative(a,b,n) 
    generates a matrix of the derivative with the 
    following arguments.

    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain"""
    x = np.linspace(a,b,n)
    dx = (b-a)/(n-1)
    d = (np.eye(n,n,1)-np.eye(n,n,-1))
    print(d)
    d[0][0] = -1
    d[-1][-1] = 1
    d[0:][0] = d[0:][0]/dx
    d[0:][1:n-1] = d[0:][1:n-1]/(2*dx)
    d[0:][n-1] = d[0:][n-1]/dx
    return d


def second_derivative(a, b, n):
    """second_derivative(a,b,n)
    generates a matrix of the second derivative with the
    following arguments

    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain
    """
    x = np.linspace(a,b,n)
    dx = (b-a)/(n-1)
    d = ((np.eye(n,n,2)-np.eye(n,n,-2))-2*np.eye(n))
    d[0][0] = 2
    d[0][1] = -4
    d[0][2] = 2
    d[1][0] = 2
    d[1][1] = -3
    d[-1][-1] = 2
    d[-1][-2] = -4
    d[-1][-3] = 2
    d[-2][-1] = 2
    d[-2][-2] = -3
    d = (d/(4*dx**2))
    d = np.matmul(derivative(a,b,n),derivative(a,b,n))
    return d

def f(a,b,n):
    """f(a,b,n)
    Returns an array of values satisfying the squared
    function.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain
    Returns:
        numpy array of the range values of x**2
     
        """
    x = np.linspace(a,b,n)
    f = np.array(x**2)
    return f

def s(a,b,n):
    """s(a,b,n)
    Returns the range of the sin(x) function
    stored as a numpy array.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain
        
    Return:
        numpy array of the range values for a sin(x) function
        corresponding to the input domain.
    """
    x = np.linspace(a,b,n)

    return np.array(np.sin(x))

def g(a,b,n):
    """g(a,b,n)
    Returns the range of the gaussian function
    stored as a numpy array.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain
        
    Return:
        numpy array of the range values for a gaussian function
        corresponding to the input domain.
        """
    x = np.linspace(a,b,n)

    def gauss(x):
        return (1/np.sqrt(2*np.pi))*np.exp(-x**2/2)

    return np.array(gauss(x))

def make_f_plot(M, M2, x, f, graph title):
    """make_f_plot creates a plot of the x^2 function, the derivative of 
    x^2 and also the second derivative.
    
    Args:
        M :
        M2 : 
        x : 
        f : 
        
    """
    deriv_1 = M @ f
    deriv_2 = M2 @ f
    font = {"size" : 18}
    plt.title("TITLE")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, f, color = "blue", label = "function")
    plt.plot(x, deriv_1, color = "red", label = "first derivative")
    plt.plot(x, deriv_2, color = "green", label = "second derivative")
    plt.legend(loc = "upper left")
plt.show()
