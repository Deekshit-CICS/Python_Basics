# Find duplicates in array list
from collections import Counter
def find_dup_char(input):
    
    arr = [10,999]
    duplicates = []
    
    for arr1 in range(arr[1]-1):
        str1 = str(arr1)
        # print(str1)
        WC = Counter(str1)
        # print(WC)
        # Finding no. of  occurrence of a character
        # and get the index of it.
        for letter, count in WC.items():
            # print(count)
            if (count > 1):
                duplicates.append(str1)
    
    print(duplicates)
                
         
 
# Driver program
if __name__ == "__main__":
    input = 'geeksforgeeks'
    find_dup_char(input)
