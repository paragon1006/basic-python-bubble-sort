mylist=[10,7,12,3,5] #mylistay
def bubblesort(mylist): #function defining
    n=len(mylist) #calculates length of mylistay
    for x in range(0,n): #first loop to make sure all variables are checked
        for tempvar2 in range(0,n-1): #loop to switch value with smaller 
            if mylist[tempvar2]>mylist[tempvar2+1]: #checks if value is greater 
                tempvar=mylist[tempvar2] #creates safety value (temporary)
                mylist[tempvar2]=mylist[tempvar2+1] #replaces value
                mylist[tempvar2+1]=tempvar #uses safety value
    return mylist #returns value
print(bubblesort(mylist)) #prints created function
                