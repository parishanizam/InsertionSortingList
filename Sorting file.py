#Basic Insertion Sort Program
def insertionSort(list): 
  
    # Loop through the list
    for i in range(1, len(list)): 
  
        position = list[i] 

        j = i-1
        #Program determines which number is larger and switches position
        while j >=0 and position < list[j] : 
                list[j+1] = list[j] 
                j -= 1
        list[j+1] = position 
  
  #Test 
list = [12, 11, 13, 5, 6] 
insertionSort(list) 
print ("Sorted array is:") 
for i in range(len(list)): 
    print ("%d" %list[i])