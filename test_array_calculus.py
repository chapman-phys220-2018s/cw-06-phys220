#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
import nose
import array_calculus as ac

def test_derivative():
    """Test_derivative() tests the derivative matrix for the chosen values of
    x= -1, 0, and 1."""
    desired = np.array([(np.sin(0)-np.sin(-1)),(np.sin(1)-np.sin(-1)/2),(np.sin(1)-np.sin(0))])
    def sin():
        x = np.linspace(-1,1,3)
        sin = np.sin(x)
        return sin
    obtained = np.array(ac.derivative(-1,1,3), sin())
    print("Desired: ",desired)
    print("Obtained: ",obtained)
    np.testing.assert_almost_equal(obtained, desired)
    
    


