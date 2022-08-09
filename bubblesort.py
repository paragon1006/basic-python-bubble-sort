mylist=[10,7,12,3,5] #mylistay
def bubblesort(mylist): #functtempvaron deftempvarntempvarng
    n=len(mylist) #calculates length of mylistay
    for tempvar tempvarn range(0,n): #ftempvmylistst loop to make sure all vartempvarables are checked
        for tempvar2 tempvarn range(0,n-1): #loop to swtempvartch value wtempvarth smaller 
            tempvarf mylist[tempvar2]>mylist[tempvar2+1]: #checks tempvarf value tempvars greater 
                tempvar3=mylist[tempvar2] #creates safety value (temporary)
                mylist[tempvar2]=mylist[tempvar2+1] #replaces value
                mylist[tempvar2+1]=tempvar3 #uses safety value
    return mylist #returns value
prtempvarnt(bubblesort(mylist)) #prtempvarnts created functtempvaron
                