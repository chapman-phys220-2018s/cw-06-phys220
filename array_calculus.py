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
    x = np.linspace(a,b,n)
    dx = (b-a)/(n-1)
    d = ((np.eye(n,n,2)-np.eye(n,n,-2))-2*np.eye(n))
    print (d)
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
    return (d/(4*dx**2))

def f(a,b,n):
    """f(a,b,n)
    Returns an array of values satisfying the squared 
    function

    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain"""
    x = np.linspace(a,b,n)
    return np.array(x**2)

def s(a,b,n):
    """s(a,b,n)
    Returns the domain and range of the sin(x) function
    stored as a pair of numpy arrays (x,sx)

    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain

    Return:
        (x, sx) : Pair of numpy arrays of float64
            x  : [a, ..., b] Array of n equally spaced float64 between a and b
            sx  : [sx(a), ..., sx(b)] Array of exponential values matched to x
    """
    x = np.linspace(a,b,n)

    def sin(x):
        return np.sin(x)

    sx = np.array(sin(x))
    return (x,sx)

def g(a,b,n):
    """g(a,b,n)
    Returns the domain and range of the gaussian function
    stored as a pair of numpy arrays (x,g)

    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain

    Return:
        (x, g) : Pair of numpy arrays of float64
            x  : [a, ..., b] Array of n equally spaced float64 between a and b
            g  : [g(a), ..., g(b)] Array of exponential values matched to x
        """
    x = np.linspace(a,b,n)

    def gauss(x):
        return (1/np.sqrt(2*np.pi))*np.exp(-x**2/2)

    g = np.array(gauss(x))
    return (x, g)


