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
###

import numpy as np
import matplotlib.pyplot as plt


def f(a,b,n):
    """Function will return an array of values satisfying the squared 
    function"""
    x = np.linspace(a,b,n)
    return x**2

def s(a,b,n):
    """Function will return an array of values that satisfy the sine 
    function"""
    x= np.linspace(a,b,n)

    def sin(x):
        return np.sin(x)

    sx= np.array(sin(x))
    return (x,sx)

def g(a,b,n)
    """Function will return an array of values satisfying the gaussian 
    function"""
    x = np.linspace(a,b,n)

    def gauss(x):
        return (1/np.sqrt(2*np.pi))*np.exp(-x**2/2)

    g = np.array(gauss(x))
    return (x, g)
