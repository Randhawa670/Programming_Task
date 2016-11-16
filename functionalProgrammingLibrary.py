
#Functional Programming Library Class
class funcproglib:
    #Map user function to each element in the list
    def Map(function_name,list_):
        try:
            result = [ function_dict[function_name](val) for val in list_ ]
            return result
        except TypeError as error:#to catch exception where argument mismatch occur
            funcproglib.PrintTypeErrorExist(error)
    
    #Filter elements in the list that return true when evaluated by the user function       
    def Filter(function_name,list_):
        try:
            result = [ val for val in list_ if function_dict[function_name](val) ]
            return result
        except TypeError as error:#to catch exception where argument mismatch occur
            funcproglib.PrintTypeErrorExist(error)
    
    #Reduce elements in the list to a single value, accumulated after list is processed by the user function 
    def Reduce(function_name, list_,start=None):
        if start is None: 
            try:
                start = list_[0]
            except StopIteration:
                raise TypeError('reduce() of empty list')
        accumlator = start
        try:
            for val in list_[1:]:
                accumlator = function_dict[function_name](accumlator,val)
            return accumlator
        except TypeError as error:#to catch exception where argument mismatch occur
            funcproglib.PrintTypeErrorExist(error)
    
    #Fold elements in the list to a single value, accumulator started with some intial value and list folding start from the left
    def LeftFold(function_name, list_,start):
        return funcproglib.Reduce(function_name,list_,start)
    
    #Fold elements in the list to a single value, accumulator started with some intial value and list folding start from the right
    def RightFold(function_name, list_,start):
        list_ = list_[::-1]#reverses the given list
        return funcproglib.Reduce(function_name,list_,start)
    
    #Simply call user function for each element in the list
    def ForEach(function_name, list_):
        for val in list_:
            function_dict[function_name](val)
            
    #Zip take any number of lists and merges them together till the length of the shortest list   
    def Zip(*args):
        common_length = range(len(sorted((args), key=len)[0]))#compute common length or the length of the shorter list 
        no_of_lists = range(len(args))
        result = []
        tuple_ = []
        for i in common_length:
            tuple_.clear()
            for j in no_of_lists:
                tuple_.append(args[j][i])
            result.append(tuple(tuple_))
        return result
    
    #print type error and exit    
    def PrintTypeErrorExist(error):
        print("TypeError : " + str(error))
        exit(1)
    

#user defined functions,that when specidied should be called and used by the Functional Programming library Functions

#Take and return square of the given value
def square(val):
    return val*val

#Take and return cube of the given value
def cube(val):
    return val*val*val

#Evaluate if given value is greater than 5 and then returns true or false 
def greater(val):
    return val > 5

#Simple prints the absolute of the given value,doesn't return anything
def PrintAbsolute(val):
    print("Absolute value for " + str(val) + " is : " + str(abs(val)))
    
#Add the two given values and return their sum     
def Sum(prev_val,curr_val):
    return prev_val+curr_val


#Main to test Functional Programming Library with user deined functions
if __name__=="__main__":
    function_dict = {square:square,cube:cube,greater:greater,Sum:Sum,PrintAbsolute:PrintAbsolute}#All user defined function should be include in this dictionary in form key:value pair form, where both key and value are equal to function name
    
    #Use library function in this form funcproglib.library_function_name(user_defined_function_name,list_of_integers) 
    #zip just expects only two integer lists
    #Testing Map 
    input_list = [1,2,3,4]
    print("----------------")
    
    print("\nMap Test\n")
    
    print("input = " + str(input_list))
    output = funcproglib.Map(square,input_list)
    print("output = " + str(output)+"\n")
    
    input_list = [5,3,4]
    print("input = " + str(input_list))
    output = funcproglib.Map(greater,input_list)
    print("output = " + str(output)+"\n")
    
    print("----------------")
    
    #Testing Filter
    print("\nFilter Test\n")
    
    input_list = [12,3,4]
    print("input = " + str(input_list))
    output = funcproglib.Filter(greater,input_list)
    print("output = " + str(output)+"\n")
    
    print("----------------")
    
    #Testing Reduce
    print("\nReduce Test\n")
    
    input_list = [12,12,4]
    print("input = " + str(input_list))
    output = funcproglib.Reduce(Sum,input_list)
    print("output = " + str(output)+"\n")
    
    print("----------------")
    
    #In left Fold and Right fold,there will be additional Third paramter that will be explictly telling the intial value of accumulator
    #Testing Left Fold with start value = 10 
    print("\nLeft Fold Test\n")
    
    input_list = [12,12,4]
    print("input = " + str(input_list))
    output = funcproglib.LeftFold(Sum,input_list,10)
    print("output = " + str(output)+"\n")
    
    print("----------------")
    
    #Testing Right Fold with start value = 25 
    print("\nRight Fold Test\n")
    
    input_list = [12,9,4]
    print("input = " + str(input_list))
    output = funcproglib.RightFold(Sum,input_list,10)
    print("output = " + str(output)+"\n")
    
    print("----------------")
    
    #Testing For Each 
    print("\nForeach  Test\n")
    
    input_list = [12,-5,-4,9,4]
    print("input = " + str(input_list))
    output = funcproglib.ForEach(PrintAbsolute,input_list)
    print("output = " + str(output)+"\n")
    
    print("----------------")
    
    #Testing Zip
    print("\nZip  Test\n")
    
    input_list_1 = [2,'a',3,'b',7]
    input_list_2 = [4,8,6,18,14]
    print("input list 1 = " + str(input_list_1))
    print("input list 2 = " + str(input_list_2))
    output = funcproglib.Zip(input_list_1,input_list_2)
    print("output = " + str(output)+"\n")
    
    print("----------------")
    