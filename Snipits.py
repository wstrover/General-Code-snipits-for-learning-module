#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Get Freqency and Mode
def freqs(numList):
    freqs = [ 0 ]*(max(numList)+1)
    for aNum in numList:
        freqs[aNum]+=1
    return freqs
def Mode(numList):
    length = 0
    index = 0
    for i in range(len(freqs(numList))):
        if (freqs(numList)[i]) > length:
            length = (freqs(numList)[i])
            index = i
        else:
            pass
    return numList[i]
    
        
        
        
aList = [7,2,1,7,7,5,3,7,1,4,1,2,3,4]        
print(Mode(aList)) 

print(freqs(aList))


# In[2]:


# Read and interact with Tiny.txt

#Task 1
def choiceprint():
    def printList(distCost):
        for pair in distCost:
            stringFormatted = str (pair[0])+" Miles, "+"£ "+str (pair [1])
            print(stringFormatted)
    def selectionSortCost ( array ):
        vendor = len( array )
        for position in range(vendor-1):
            minRow = position
            for temp in range( position + 1 , vendor ):
                if array [temp ] [ 1 ] < array [minRow ] [ 1 ] :
                    minRow = temp
            array [ position ] , array [minRow] = array [minRow] , array [ position ]
        return array
    def selectionSortDistance ( array ):
        vendor = len( array )
        for position in range(vendor-1):
            minRow = position
            for temp in range( position + 1 , vendor ):
                if array [temp ] [ 0 ] < array [minRow ] [ 0 ] :
                    minRow = temp
            array [ position ] , array [minRow] = array [minRow] , array [ position ]
        return array
    status = int(input("Enter choice (1): Print / (2): Sort on Distance / (3): Sort on price / (4):Quit : "))
    if status == 4:
        print("Quitting...")
        pass
    else: 
        fileName = input("Enter a file name: ")
        infline = open( fileName )
        table = []
        recNum = 0
        for line in infline :
            table.append(line.split(','))
            table[recNum][0]=int(table[recNum][0])
            table[recNum][1]=float(table[recNum][1])
            recNum+=1
        if status == 1:
            infline.close()
            printList(table) 
        elif status == 2:
            infline.close()
            table=selectionSortDistance(table) 
            printList(table) 
        elif status == 3:
            infline.close()
            table=selectionSortCost(table) 
            printList(table) 

def subsetOf(List,SubsetList): #Task 2
    K=[]
    for x in List:
        if x in SubsetList:
            K.append(1)
        else:
            K.append(0)
    print(K)
    
def duplicate(List1, List2): # Task 3
    K=[]
    for x in List1:
        if x in List2:
            K.append(x)
        else:
            continue
    print(K)

def LargestValueFinder(List): # Task 4
    largestCount = 0
    LL = (len(List)-1)
    for x in range(LL+1):
        y = (LL)-x
        poppedvalue = List.pop(y)
        if poppedvalue > largestCount:
            largestCount = poppedvalue
        else:
            continue
    print("The largest Value in the stack is %d" % largestCount)
    

#choiceprint()


L=[2,17,12,5,66,20,7]
M=[2,12,66]
subsetOf(L,M)
duplicate(L,M)
LargestValueFinder(L)


# In[3]:


def reverse_list(lst):
    return lst[::-1]

def reverse_listStack(lst):
    lst[:] = lst[::-1]
    return lst


def minSort(lst):
    return sorted(lst)

def maxSort(lst):
    return sorted(lst, reverse=True)

def find_half_max(aQueue):
    theMax = 0
    for item in aQueue:
        if item > theMax:
            theMax = item
    return 0.5 * theMax



List = [1, 2, 3, 4, 5]
List2 = [7, 5, 12, 4, 9]


print("Original List:", List)

print("Reversed List using reverse_listStack:", reverse_listStack(List)) # reverse_listStack changes the actual input list
print("Original List after the change:", List) #can be been seen by printing the list

List = [1, 2, 3, 4, 5] # Remake the original list
print("Reversed List using reverse_listStack:", reverse_listStack(List[:]))  # A way to stop that is to use a copy to preserve original List
print("Original List after the change:", List) #can be been seen by printing the list


print("Reversed List using reverse_list:", reverse_list(List)) # reverse the list without changing it
print("Original List:", List)

print("Sorted List (Ascending) using minSort:", minSort(List2))
print("Sorted List (Descending) using maxSort:", maxSort(List2))
print("Find Half Max in List2:", find_half_max(List2))


# In[ ]:





# In[ ]:




