#casting
#to specify datatype of a variable use casting

#x=str(10)#string   single qutes ,double qutes can use both but one at a time
#y=int(10)#integer number
#z=float(10) #decimal number                              #string cannot be added with integer

#print(x+y) shows error
#print(z+y)
#print(type(z+y))


#variables names
#short names(x,y,z)
#descriptive names (name,age,total_price)


#rules for python variables
   # variables name must star with__or letter
 #   cannot star with a number
  #  can only contain alpha numeric chracters and underscores(a-z,0-9,and_)
 #   are case senstive




#acceptable variable names
#myname='john' valid variable name
#my_name='john'
#print(my_name) is also valid
#_my_name='john' is valid
#myName='john' is not equal to myname='john'

#not acceptable
#2myname='john' is not valid     my-name='john' is not valid
#my name='john'
#print(my name) is not valid

#multi words

#camel case
#myFirstName='john'

#pascal case
#MyFirstName='john'

#snake case
#my_first_name='john'


#x, y, z = 10, 20, 38
#print(x)
#print(y)        assign multiple values to multiple variables
#print(z)

#x=y=z=10         assign same values to multiple variables
#print(x,y,z)


#x='my'
#y='name'
#z='is'
#print(x,y,z)     space will come
#print(x+y+z)   no space will come

#x="my"
#y='name'
#z='is ak'                          #difficult syntax
#print(x+' '+y+' '+z+' ')

#global variables
#variables are created outside of a function
#they can be used outside or inside of a function

#x='john'       #created outside                #garden2 or global variable   (assecible by every one)

#def myfunc():                        #campus

 #   print("my name is " + x)                              #is used inside of a function

#myfunc()                         # compulsary to  end with it





#x = 'john'


#def myfunc():
 #   x='peter'       local variable
  #  print("my name is " + x)

#print(x)

#myfunc()


#x = 'john'  # created outside                #garden2 or global variable   (assecible by every one)


#def myfunc():  # campus
  #  y='peter'  #local variabe
 #   print("my name is " + y)  # is used inside of a function
                                                     #when run first executes inside my function

#myfunc()  # compulsary to  end with it
#print("my name is " + x)


#when x interchanged with y there will be error cause the y function is a local function and cannot be accesd as a global function




