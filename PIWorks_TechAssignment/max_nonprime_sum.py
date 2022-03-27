#return true if number prime False if not a prime number
def isPrime(number):
    flag=1
    if (number==1):
        flag=0
    
    if(number >2):
        for divider in range(2, 1, number//2):
            #if the number can be divided without remainder to any number but 1 and itself it's not a prime return False else True
            if (number%divider ==0):
                flag =0

    if (flag==1):
        return True
    else:
        return False    

#convert a list of strings to list which its elements consist of integer list          
def string_to_int(lines):
    lines_int=list()
    for row in lines:
        elements=list(map(int,row.split(' ')))
        lines_int.append(elements)
    return lines_int    


#read number from text file and find a path with non-prime numbers which has max sum
def triangle_max_sum(inpFilePath):
    inpFile=open(inpFilePath,'r')
    lines=inpFile.readlines()
    lines_list=string_to_int(lines)
    totSum=0
    col=0
    for row in range(len(lines_list)):
        number =int(lines_list[row][col])
        print(isPrime(number),"\n")
        if(isPrime(lines_list[row][col]) == False):
            totSum =totSum+ lines_list[row][col]
            downward=int(lines_list[row+1][col] )#number at the same column index as current number but incremented row index
            diagonal=int(lines_list[row+1][col+1])
            if( isPrime(diagonal) ==False ):
                if(diagonal>=downward ):
                    if(col+1 <= len(lines_list[row])):
                        col=col+1
            
    print(totSum,"\n")            
    inpFile.close()
triangle_max_sum("input.txt")        
