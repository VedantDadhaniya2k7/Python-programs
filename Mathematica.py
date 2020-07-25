class Bsics:
    def add(Set_of_all_Values)
        #this will add all the values
        ans = 0
        for x in Set_of_all_Values :
            ans = ans + x
        return ans

    def subtract(Set_of_all_Values):
        #this will subtract all of the other values from the first value
        GVal = Values[0]
        for Sval in Set_of_all_Values :
            GVal = Gval-Sval
        return GVal

    def multiply(Set_of_all_Values):
        #this will multiply all values
        Answer = 1
        for A in Set_of_all_Values :
            Answer = Answer * A
        return Answer

    def divide(Dividend,Set_of_all_Divisors):
        #this will divide the dividend with all the divisors provided
        Answer = Dividend
        for D in Set_of_all_Divisors:
            Answer = Answer/D
        return Answer

    def Expo(Base, Power):
        Answer = Base**Power
        return Answer

    def SqRoot(Value):
        Answer = Value**0.5
        return Answer

    def CubeRoot(Value):
        Ans = Value**(1/3)
        return round(Ans)

    def Mean(Set_of_all_Values):
        Len = len(Set_of_all_Values)
        Amount = 0
        for x in Set_of_all_Values:
            Amount = Amount + x
        Ans = Amount/Len
        return Ans

    def Median(Set_of_all_Values_in_ascending order):
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

