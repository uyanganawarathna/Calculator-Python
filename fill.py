#create calculator using python
############################ ###################
######################### ###################
###################  ####################
#################    #################
############         ############
########             #########
###### Done ALL test ######

while True:
       
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    choice = input("Enter choice(+,-,*,/,^,%,#,$):")
    print("",choice)
    def select_op(choice):
        if(choice == '+'):
                x = input("Enter first number:")
                print("",x)    #get first number from user
                if(x == '0$'):
                    return
                y = input("Enter second number:")   #get second number from user
                print("",y)
                if(x == '0$'):
                    return
                summation(x,y)
                
        elif(choice == '-'):
                x = input("Enter first number:")
                print("",x)
                if(x == '#'):
                    print("Done. Terminating")
                    exit()
                y = input("Enter second number:")
                print("",y)
                if(y == '#'):
                    print("Done. Terminating")
                    exit()
                subtraction(x,y)  
            
        elif(choice == '*'):
                x = float(input("Enter first number:"))
                y = float(input("Enter second number:"))
                multiple(x,y)    #call mul function

        elif(choice == '/'):
               try:
                      if(choice == '/'):
                
                        x = input("Enter first number:")
                        print("",x)#get first number from user
                        y = input("Enter second number:")
                        print("",y)#get second number from user
                        deviation(x,y)
            
        # additional cases for subtraction, multiplication, division, etc. here
            
                      elif(choice == '#'):
                                print("Done. Terminating")
                                exit()

                      else:
                                return

               except ValueError:
                        return
        elif(choice == '^'):
                x = float(input("Enter first number:"))
                y = float(input("Enter second number:"))
                power(x,y)    #call mul function

        elif(choice == '%'):
                x = float(input("Enter first number:"))
                y = float(input("Enter second number:"))
                reminder(x,y)    #call mul function

        elif(choice == '#'):
                print("Done. Terminating")
                exit()

        else:
                print("Reset calculator.")
                   
        return
    #create function for calculating summetion
    def summation(x,y):
            z = float(x)
            v = float(y)
            add = z+v
            print(z ,'+', v,'=',add)
            return

    #create subtraction function
    def subtraction(x,y):
            z = float(x)
            v = float(y)
            min = z - v
            print(z ,'-', v,'=',min)
            return
    #create multiplication function
    def multiple(x,y):
            z = float(x)
            v = float(y)
            mu = z * v
            print(z ,'*', v,'=',mu)
            return
    #create devide function
    def deviation(x,y):
            z = float(x)
            v = float(y)
            if(v == 0.0):
                print("float division by zero")
                print(z ,'/', v,'=','None')
            else:
                print(z ,'/', v,'=',(z/v)) 
            return      
    #create a power function
    def power(x,y):
        z = float(x)
        v = float(y)
        pw = z ** v
        print(z ,'^', v,'=',pw)
        return
    #create a reminder function
    def reminder(x,y):
        z = float(x)
        v = float(y)
        rm = z % v
        print(z ,'%', v,'=',rm)
        return

    select_op(choice)


#this is simple calculator and you can use this calculator for your daytoday life
# //////using python programming language/////////
#******functions,conditional operations and variables were used to developed this calculator
############## Fun and Learn #############