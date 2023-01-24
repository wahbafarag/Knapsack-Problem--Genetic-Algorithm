# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:59:06 2022

@author: S.A
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 20:25:16 2022

@author: Farag
"""


import numpy as np 
import random as rand
class Ga : 
    
    def __init__(self ,noItems ,popSize ,values , weights, totalWeight):
        self.popSize = popSize 
        self.noItems= noItems 
        self.values = values 
        self.weights = weights 
        self.totalWeight = totalWeight
        self.mainGa = []
        self.flag=0
        self.parentIndecies= [] # put here index of parent that will be replaced
    
    #------------------------------------------------
    
    def initial(self) : 
        for i in range(self.popSize):
            smallGaList = []
            for j in range(self.noItems):
                genRandInt = rand.randint(0, 1)
                smallGaList.append(genRandInt)
            self.mainGa.append(smallGaList)
        return  0
      
    #-------------------------------------------------
    
    def calcFt(self):
        values = np.array(self.values)       # turn values into numpy array
        weights = np.array(self.weights)     # turn weights numpy array
        self.mainGa =np.array(self.mainGa)   # turn mainGa into numpy array
        fitArr =[]
        for i in range(self.popSize):
            totVal = values *self.mainGa[i]
            totWei = weights *self.mainGa[i]
            if sum(totWei) <= self.totalWeight:
               fitArr.append(sum(totVal))
            else :
               fitArr.append(0)
               
        comVal =0
        comArr =[]
        for j in range(len(fitArr)):
            comVal=comVal+fitArr[j]
            comArr.append(comVal)
        
        return comArr 
    
    #-------------------------------------------------
    
    def selection(self ,comArr) :
        if sum(comArr) != 0 :
            ftRand = rand.uniform(0, 1)
            secRand = rand.uniform(0, 1)
            selctdPop = []
            for i in range(len(comArr)) :
                if ftRand <= comArr[i] :
                    ftSelected = self.mainGa[i]
                else :
                    continue
            if len(comArr) == 1 and ftRand > comArr[0] :
                self.flag = 0
                return 0
            if (ftRand > comArr[-1]) :
                self.flag = 0
                return 0 
            for j in range(len(comArr)) :
                if secRand  < comArr[j] :
                    secSelected = self.mainGa[j]
                    break 
                else :
                    continue
            if len(comArr) == 1 and secRand > comArr[0] :
                self.flag = 0
                return 0 
            if (secRand > comArr[-1]) :
                self.flag = 0
                return 0 
            ftSelected = ftSelected.tolist()
            secSelected = secSelected.tolist()
            selctdPop.append(ftSelected)
            selctdPop.append(secSelected)
            self.parentIndecies = [i ,j]
            print(self.mainGa )
            self.flag = 1
            return selctdPop
        print("Array is empty")
            
    #-------------------------------------------------
    
    def crossover(self,selctdPop):
        if self.flag == 1 and selctdPop and len(selctdPop):
            pc =0.6         # compare with rc to check possibility of cross over 
            crossPoint =rand.randint(1,self.noItems-1)  # swap after this point
            rc =rand.uniform(0,1)
            
            if rc <= pc :
               print("Crossover point is : " ,crossPoint)
               print("Befor Cross Over  " ,selctdPop[0],selctdPop[1])
               tmp1 = selctdPop[0][crossPoint:]
               tmp2 = selctdPop[1][crossPoint:]
               selctdPop[0] =selctdPop[0][:crossPoint]
               selctdPop[1] =selctdPop[1][:crossPoint]
               selctdPop[0].extend(tmp2)
               selctdPop[1].extend(tmp1)
               print("After Cross Over ",selctdPop[0],selctdPop[1])
               afterCrossOver = [selctdPop[0],selctdPop[1]]
               self.flag=1
               return afterCrossOver
            else :
               self.flag = 0
               print("Pc is greater than Rc : No crossover Occured. ")
               print("Selected Pop still unchanged : " , selctdPop[0],selctdPop[1])
               self.calcFt()
    
    #-------------------------------------------------
    
    def mutation(self,afterCrossOver):
          if self.flag ==1:
             for i in range(2):
                 for j in range(self.noItems):
                     mutationRate =rand.uniform(0,1)
                     if 0.6< mutationRate < 0.9:
                          if afterCrossOver[i][j] == 1 :
                              afterCrossOver[i][j] += -1
                          else : 
                              afterCrossOver[i][j] += 1
             print("After mutation : ",afterCrossOver[0],afterCrossOver[1])
             return afterCrossOver
          else:
              print("No Mutation Occured")
              return 0
    
    #-------------------------------------------------
    
    def replacment(self ,afterCrossOver) :
        
        if self.flag == 1 :
            
            np.array(afterCrossOver[0])
            np.array(afterCrossOver[1])
            
            print("Before Replacment : \n" ,self.mainGa)
            self.mainGa[self.parentIndecies[0]] = afterCrossOver[0]
            self.mainGa[self.parentIndecies[1]] = afterCrossOver[1]
            print("After Replacment : \n" ,self.mainGa)
            print( "indcies of replacment : " ,self.parentIndecies[0] , self.parentIndecies[1])
            print("##############################")
        else :
            print("No replacment occured")
            print("##############################")
     
    #-------------------------------------------------
    
    def output (self) :
        
        if self.flag == 1 :
            outputList = []
            for i in range(len(self.mainGa)) :
                totVal = self.values * self.mainGa[i]
                outputList.append(sum(totVal))
                
            maxVal = max(outputList)
            optSolution = outputList.index(maxVal)
            print("Optimal Solution is : " , self.mainGa[optSolution])
            print("##############################")
        else :
            return 0
        
     #-------------------------------------------------
        
        
if __name__ == '__main__' :
    
    it = 5
    myObj = Ga(3,3,[1,8,2],[4,4,6],15)
    myObj.initial()
    for i in range(it) :  
        ft = myObj.calcFt()
        selected =myObj.selection(ft)
        crossOv =myObj.crossover(selected)
        mutated = myObj.mutation(crossOv)
        myObj.replacment(mutated)
        myObj.output()
    print("Number of Iterations is :" , it)
        
    
    
   