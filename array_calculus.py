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

def derivative(a, b, n):
    """ derivative(a, b, n) generates a matrix of the derivative with the 
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
    """second_derivative(a, b, n) generates a matrix of the second 
    derivative with the following arguments

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


def f(a, b, n):
    """f(a, b, n) returns an array of values satisfying the $x^2$
    function.

    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain
    Returns:
        numpy array of the range values of $x^2$

    """
    x = np.linspace(a, b, n)
    fx = np.array(x)
    func = x**2
    return fx, func


def make_f_plot(F, F2, x, f):
    """make_f_plot creates a plot of the x^2 function, the derivative of
    x^2 and also the second derivative.

    Args:
        F : matrix created by the 1st derivative of $x^s$
        F2 : matrix created by the 2nd derivative of $x^s$ 
        x : values of x from $x^2$
        f : values of y from $x^2$

    """
    deriv_1 = F @ f
    deriv_2 = F2 @ f
    font = {"size" : 18}
    plt.title("Plot of $x^2$, 1st Derivative of $x^2$ and 2nd Derivative of $x^2$")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, f, color = "blue", label = "$x^2$")
    plt.plot(x, deriv_1, color = "red", label = "first derivative")
    plt.plot(x, deriv_2, color = "green", label = "second derivative")
    plt.legend(loc = "upper left")
plt.show()


def s(a, b, n):
    """s(a, b, n) returns the range of the sin(x) function
    stored as a numpy array.

    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain

    Returns:
        numpy array of the range values for a sin(x) function
        corresponding to the input domain.

    """
    x = np.linspace(a,b,n)
    sx = np.array(x)
    func = np.sin(x)
    return sx, func


def make_sin_plot(S, S2, x, s):
    """make_sin_plot creates a plot of the sin(x) function, the derivative of 
    sin(x) and also the second derivative.

    Args:
        S : matrix created by the 1st derivative of sin(x)
        S2 : matrix created by the 2nd derivative of sin(x)
        x : x values from sin(x)
        s : y values from sin(x)

    """
    deriv_1 = S @ s
    deriv_2 = S2 @ s
    font = {"size" : 18}
    plt.title("Plot of sin(x), 1st Derivative of sin(x) and 2nd Derivative of sin(x)")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, s, color = "blue", label = "sin(x)")
    plt.plot(x, deriv_1, color = "red", label = "first derivative")
    plt.plot(x, deriv_2, color = "green", label = "second derivative")
    plt.legend(loc = "upper left")
plt.show()


def g(a, b, n):
    """g(a, b, n) returns the range of the gaussian function
    stored as a numpy array.

    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain

    Returns:
        numpy array of the range values for a gaussian function
        corresponding to the input domain.

    """
    x = np.linspace(a,b,n)
    gx = (np.array(x))
    func = (1/np.sqrt(2*np.pi))*np.exp(-x**2/2)
    return gx, func


def make_gauss_plot(G, G2, x, g):
    """make_gauss_plot creates a plot of the gaussian function, the derivative of 
    gaussian and also the second derivative.

    Args:
        G : matrix created by 1st derivative of gaussian
        G2 : matrix created by 2nd derivative of gaussian
        x : x values from gaussian
        g : y values of gaussian

    """
    deriv_1 = G @ g
    deriv_2 = G2 @ g
    font = {"size" : 18}
    plt.title("Plot of gaussian, 1st Derivative of gaussian and 2nd Derivative of gaussian")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, g, color = "blue", label = "gaussian")
    plt.plot(x, deriv_1, color = "red", label = "first derivative")
    plt.plot(x, deriv_2, color = "green", label = "second derivative")
    plt.legend(loc = "upper left")
plt.show()


