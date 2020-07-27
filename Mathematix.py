import math

def add(Set_of_all_Values):
    #this will add all the values
    ans = 0
    for x in Set_of_all_Values :
        ans = ans + x
    return ans

def sub(Set_of_all_Values):
    #this will subtract all of the other values from the first value
    GVal = Set_of_all_Values[0]
    del Set_of_all_Values[0]
    for Sval in Set_of_all_Values :
        GVal = Gval-Sval
    return GVal

def mul(Set_of_all_Values):
    #this will multiply all values
    Answer = 1
    for A in Set_of_all_Values :
        Answer = Answer * A
    return Answer

def div(Dividend,Set_of_all_Divisors):
    #this will divide the dividend with all the divisors provided
    Answer = Dividend
    for D in Set_of_all_Divisors:
        Answer = Answer/D
    return Answer

def Expo(Base, Power):
    #finds the exponent of the given base and power
    Answer = Base**Power
    return Answer

def SqRoot(Value):
    #finds the Square root of the given value
    Answer = Value**0.5
    return Answer

def CubeRoot(Value):
    #finds the Cube root of the given value
    Ans = Value**(1/3)
    return round(Ans)

def Mean(Set_of_all_Values):
    #finds the mean of the given values
    Len = len(Set_of_all_Values)
    Amount = 0
    for x in Set_of_all_Values:
        Amount = Amount + x
    Ans = Amount/Len
    return Ans

def Median(Set_of_all_Values_in_ascending_order):
    #finds the median of the given values
    Vals = Set_of_all_Values_in_ascending_order.copy()
    Len = len(Vals)
    if Len%2 != 0 :
        index = (Len+1)/2-1
        median = Vals[index]
    elif Len%2 == 0 :
        index1 = Len/2-1
        index2 = Len/2
        m1 = Vals[index1]
        m2 = Vals[index2]
        median = (m1+m2)/2
    return median

def CubeVol(Lenght):
    #finds the volume of a cube with the given parameters 
    ans = Lenght**3
    return ans

def CuboidVol(l, b, h):
    #this gives the volume of a cuboid with the given parameters
    ans = l*b*h
    return ans

def CylinderVol(radii, height):
    #finds the volume of a cylinder with the given parameters
    ans = π*(radii**2)*height
    return ans

def ConeVol(radii, height):
    #finds the volume of a cone with the given parameters
    ans = (1/3)*π*(radii**2)*height
    return ans

def SphereVol(radii):
    #finds the volume of a sphere with the given parameters
    ans = (4/3)*π*(radii**3)
    return ans
