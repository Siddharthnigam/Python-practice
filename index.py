
#                              Area and Parameter of Rectangle

# l=10
# b=5
# print("Area of Rectangle",l*b)


# l=int(input("Length"))
# b=int(input("Breadth"))
# print("Area of Rectangle",l*b)


# l=10
# b=5
# print("Parameter of reactanglr", 2*(l+b))


# l=int(input("Enter Length"))
# b=int(input("Enter Breadth"))
# print("Perameter Of Rectangle=",2*(l*b))


#                              Area and Parameter of Cirlcle


# r=5
# print("Parameter of circle" , 2*3.14*r)


# r=int(input("Radius"))
# print("Parameter of circle" , 2*3.14*r)


# r=5
# print("Area of circle" (3.14*r)*(3.14*r))
 

# r=int(input("Radius"))
# print("Area of circle", (3.14*r)*(3.14*r))
                          

#                               Take digit 
# a=1234
# print(((a+8)*3/5)*5)


#                              Condition  If Else

# a=int(input("a"))
# b=int(input("b"))
# print( "true" if a < b and a > 50 else "False" )



#                                Percentage

# a=78
# b=45
# c=62
# print("Percentage =", (a+b+c)/300*100)


# a=int(input("English"))
# b=int(input("Maths"))
# c=int(input("Science"))
# print("Percentage =", (a+b+c)/300*100)


#                               Convert lenght meter feet etc

# Meter To inch
# a=2
# print("Inch =", (a*39.37))    


# a=int(input("Meter="))
# print("Inches =", (a*39.37))


# Meter to Feet
# a=2
# print("Feet =", (a*3.37))


# a=int(input("Meter="))
# print("Feet =", (a*3.37))


#                               Convert Fehrenite and Calcius 

# Ferhrnite into Calcius
# f=50
# print("Calcius =", (f-32)*5/9)


# f=int(input("Fehrnite"))
# print("Calcius =", (f-32)*5/9)






#                                   Condition  If Else


# a=19
# if(a>18):
#     print("He is Above 18")
# else:
#     print("He is Not Above 18")
    

# a=int(input("Age ="))
# if(a>18):
#     print("He is Above 18")
# else:
#     print("He is Not Above 18")


# a=int(input("a"))
# b=int(input("b"))
# if(a<b and a>50):
#     print("True")
# else:
#     print("False")


# l=int(input("Length= "))
# b=int(input("Breadth= "))
# if(l==b):
#     print("It's an Square")
# else:
#     print("It's  a Rectangle")


# a=int(input("Enter a value of a = "))
# b=int(input("Enter a value of b = "))
# if(a>b):
#     print("A is Greater")
# elif(b>a):
#     print("B is Greater ")
# else:
#     print("Both are Equal")    


# q=int(input("Enter Quantity= "))
# p=q*100
# d=p*10/100
# if(p>1000):
#     print("Your Discount is " , p-d)
# else:
#     print("Ypur Price is " , p)    


# salary=int(input("Enter Salary of a year ="))
# year=int(input("Enter Year ="))
# s=salary*year
# bonus=s*5/100
# if(year>5):
#     print("Your Bonus Amount =" , bonus)
# else:
#     print("Bonus Not Allowed")    


# held=int(input("Classes Held ="))
# attend=int(input("Enter Attendance ="))
# p=held*75/100
# if(attend>75):
#     print("Student is Allowed")
# else:
#     print("Student is Not Allowed")    


# m=int(input("Total Percentage"))
# if(m>75):
#     print("A Grade")
# elif(m<75 & m>60):
#     print("B Grade")
# elif(m<60 & m>50):
#     print("c Grade")
# elif(m<50 & m>40):
#     print("d Grade")
# else:
#     print("Fail")        




# held=int(input("Classes Held ="))
# m=str(input("y or n"))
# attend=int(input("Enter Attendance ="))
# p=held*75/100
# if(attend>75 and m=="y"):
#     print("Student is Allowed")
# else:
#     print("Student is Not Allowed")    













# for i in range(1,100,+1):
#     print(i)



# Hello="Hello World"
# print(Hello)


# Hello='Hello World'
# print(Hello)

# Hello=""" Hello Every One"""
# print(Hello)


# bool= True
# # print(bool)
# bool= False
# print(bool)

# x=1
# y=2.8
# z="ij"
# a=None
# print(type(x),type(y),type(z),type(a))
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(a))





# for  i in range(1,100):
#         if( i%2 == 0):
#               print(i)


# for  i in range(1,100):
#         if( i%2 == 1):
#               print(i)

# a = 0
# for i in range(1,10):
#      a=a+i
#      print(a)

# counter = 0
# counter += 10
# counter = 0
# counter = counter +10
# messege ="Port 1"
# messege += "Port 2"

# print(counter)
# print(messege)


# a = int(input("a"))
# match a:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:  
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("error")





# a = int(input("a"))
# match a:
#     case 1:
#         print("one")
#     case 2:
#         print("two")
#     case 3:  
#         print("three")
#     case 4:
#         print("four")
#     case _:
#         print("no number")    


# a = str(input("a"))
# match a:
#     case 'a':
#         print("Vowel")
#     case 'e':
#         print("Vowel")
#     case 'i':  
#         print("Vowel")
#     case 'o':
#         print("Vowel")
#     case 'u':
#         print("Vowel")    
#     case _:
#         print("consonent")    

# a = int(input("a"))
# match a:
#     case 1:
#         print("31 days ")
#     case 2:
#         print("28 or 29 days ")
#     case 3:  
#         print("31 days  ")
#     case 4:
#         print("30 days  ")
#     case 5:
#         print("31 days ")
#     case 6:
#         print("30 days ")
#     case 7:
#         print("31 days  ")
#     case 8:
#         print("31 days")
#     case 9:
#         print("30 days")
#     case 10:
#         print("31 days")
#     case 11:
#         print("30 days")
#     case 12:
#         print("31 days")        
#     case _:
#         print(" No month exist ")


# a = int(input("a"))
# match a:
#     case 1:
#         print("January ")
#     case 2:
#         print("February ")
#     case 3:  
#         print("March  ")
#     case 4:
#         print("April  ")
#     case 5:
#         print("May ")
#     case 6:
#         print("June ")
#     case 7:
#         print("Jule  ")
#     case 8:
#         print("August")
#     case 9:
#         print("September")
#     case 10:
#         print("October")
#     case 11:
#         print("November")
#     case 12:
#         print("December")        
#     case _:
#         print(" No month exist ")

# a = int(input("a"))
# match a%2:
#     case 1:
#         print("Odd")
#     case _:  
#         print("Even")



# a = int(input("a"))
# match a>0:
#     case 1:
#         print("Positive")
#     case _:  
#         print("Negative")




                                 # For Loop and while loop   


# a = 1
# while a <= 10:
#     print(a)
#     a += 1 



# for i in range(1,10):
#     print(i)


# a = 100
# while a >= 1:
#     print(a)
#     a -= 1 
    
# a = 1
# while a >= -10:
#     print(a)
#     a -= 1 



# a = 1
# while a >= -10:
#     print(a)
#     a -= 1 


# for i in range(99, 0, -1):
#     print(i)



# a = 1
# s=0
# while a <= 100:
#     print(s)
#     a += 1 
#     s +=a

# a=1
# while (a <= 10):
#     if(a%2==0):
#         print(a)
#     a += 1

# for a in range(1, 11):
#     if a % 2 == 0:
#         print(a)


# a=1
# while (a <= 10):
#     if(a%2==1):
#         print(a)
#     a += 1

# for a in range(1, 11):
#     if a % 2 == 1:
#         print(a)


# s = 0
# for a in range(1, 11):
#     if a % 2 == 1:
#         s += a
# print("Sum of all odd numbers from 1 to 10:", s)

# s = 0
# for a in range(1, 11):
#     if a % 2 == 0:
#         s += a
# print("Sum of all even numbers from 1 to 10:", s)



# a = 1
# s = 0
# while a <= 10:
#     if a % 2 == 0:
#         s += a
#     a += 1
# print("Sum of all even numbers from 1 to 10:", s)


# a = 1
# s = 0
# while a <= 10:
#     if a % 2 == 1:
#         s += a
#     a += 1
# print("Sum of all odd numbers from 1 to 10:", s)


# num = int(input("Enter a number: "))
# count = 0
# while num > 0:
#     num //= 10
#     count += 1
# print(" digits:", count)




# num = int(input("Enter a number: "))
# count = 0
# for digit in str(num):
#     count += 1
# print("digits:", count)



# num = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(f"{num} x {i} = {num * i}")
#     i += 1


# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")




# msg='Hello world'
# print(msg[2:5])
     

                                       #  Function



# def siddharth():
#     print("Siddharth The Great")

# siddharth()




# def fun():
#     a=int(input("a"))
#     if a%2==0:
#         print("its even")
#     else:
#         print("Its odd")
# fun()            


# def fun():
#     held=int(input("Classes Held ="))
#     attend=int(input("Enter Attendance ="))
#     p=held*75/100
#     if(attend>75):
#        print("Student is Allowed")
#     else:
#        print("Student is Not Allowed")   


# fun()   

# def fun():
#    salary=int(input("Enter Salary of a year ="))
#    year=int(input("Enter Year ="))
#    s=salary*year
#    bonus=s*5/100
#    if(year>5):
#       print("Your Bonus Amount =" , bonus)
#    else:
#       print("Bonus Not Allowed")
      
# fun()      


# def siddharth(a, b):
#     print(a * b)

# a = int(input("Enter value for a: "))
# b = int(input("Enter value for b: "))
# c = 5
# d = 10
# siddharth(a, b)
# siddharth(c, d)


# def add_numbers(a, b):
#     """
#     This function takes two numbers as input and returns their sum.
#     """
#     return a + b

# # Example usage
# num1 = 5
# num2 = 10
# result = add_numbers(num1, num2)
# print("The sum of", num1, "and", num2, "is:", result)




# def fun( a ):
#     while a<=100:
#         print(a)
#         a+=a
# fun(1)


# def fun( a ):
#     while a<=100:
#         if a%2==0:
#             print(a)
#         a+=1
# fun(1)



# def fun( a , s ):
#     while a<=100:
#         if a%2==0:
#             print(s)
#         a+=1
#         s+=a
# fun(1 , 0)


# def fun( a , s):
#     while a<=100:
#         print(s)
#         a+=1
#         s+=a
# fun(1 , 0)


# def fun( a , s ):
#     while a<=100:
#         if a%2==1:
#             print(s)
#         a+=1
#         s+=a
# fun(1 , 0)


# def fun(a):
#     print(a)
# fun("siddharth")






                                    #    Sir ke diye question

# def circle():
#     p=22/7
#     r=int(input("radius"))
#     print("area of circle" , p*r*r)
#     print("peraeter pf circle", 2*p*r)
# circle()    



# def table():
#     for i in range(1, 11):
#         print(f"{num} x {i} = {num * i}")

# num = int(input("Enter a number"))
# table()



# def vote():
#     a=int(input('a'))
#     if(a>18):
#         print("He is Above 18")
#     else:
#         print("He is Not Above 18")

# vote()    


# def siddharth( ):
#     a=int(input("Enter a number"))
#     if a%2==0:
#         print("its an even number")
#     else:
#         print("its an odd number")

# siddharth()




                                #       List(Array)




# list = ["Apple", "Banana" , "Mango"]
# print(list)


# list = [1, 2 , 3]
# print(list)

# list = [ True, False , False]
# print(list)

# list4 = list((1, 2 , 3))
# print(list4)


# list=[9,10,7,6,2,1]
# # list.sort()
# # list.append(8)
# # list.clear()
# print(len(list))

# str= "apple"
# print(str[0:3])


# list = [9, 10, 7, 6, 2, 1]
# print(list.append(1))



# for i in range(len(list)):
#     for s in range(0, len(list) - i - 1):

#         if list[s] > list[s + 1]:
#             list[s], list[s + 1] = list[s + 1], list[s]


# print(list)



                                #    Methods




# list=[9,10,7,6,2,1]
# # list.sort()
# # list.append(8)
# # list.clear()
# print(len(list))

# list =[1,2,3,4,5]
# list1=[6,7,8,9]
# list.extend(list1)
# print(list)

# list=[1,2,3,4,5]
# list.pop(2)
# print(list)


# list=[1,2,3,4,5]
# list.remove(2)
# print(list)

# list=[1,2,3,4,5,6]
# del list[3]
# print(list)


# list=[1,2,3,4,5,6]
# list.clear()
# print(list)

# list=[1,2,3,4,5,6]
# list.copy()
# print(list)


# list=[1,2,3,4,5,6]
# list.reverse()
# print(list)



# str= "apple"
# print(str[0:3])


# list = [9, 10, 7, 6, 2, 1]
# print(list.append(1))




                                #     Tupples



# list=(3,2,3,4,5,6)
# print(list.count(3))



# list=(1,2,3,4,5,6)
# print(list.count)


                            #    Sets


# set = {1,2,3,"Siddharth"}
# print(len(set))

# set = {1,2,3,"Siddharth"}
# set.add("hello")
# print(set)


# set = {1,2,3,"Siddharth"}
# set.clear()
# print(set)

# set = {1,2,3,"Siddharth"}
# set.copy
# print(set)

# set = {1,2,3,"Siddharth"}
# set.discard(3)
# print(set)

# set = {1,2,3,"Siddharth"}
# set.remove(3)
# print(set)

# set = {1,2,3,"Siddharth"}
# set.pop()
# print(set)




#                                   Dictionary

# my_dict = {"Siddharth": 1, "Aman": 2, "Sohel": 3, "Nahru": 4}
# my_dict.clear()
# print(my_dict)  

# my_dict = {"Siddharth": 1, "Aman": 2, "Sohel": 3, "Nahru": 4}
# copied_dict = my_dict.copy()
# print(copied_dict)  

# my_dict = {"Siddharth": 1, "Aman": 2, "Sohel": 3, "Nahru": 4}
# my_dict.pop("Siddharth", None)  
# print(my_dict)  

# my_dict = {"Siddharth": 1, "Aman": 2, "Sohel": 3, "Nahru": 4}
# my_dict.pop("Aman", None)  
# print(my_dict)  

# my_dict = {"Siddharth": 1, "Aman": 2, "Sohel": 3, "Nahru": 4}
# my_dict.popitem()
# print(my_dict) 


# my_dict = {"Aman": 2, "Siddharth": 1, "Nahru": 3, "Niraj": 4}
# x = my_dict.get("Siddharth")
# print(x)  

# my_dict = {"Aman": 2, "Siddharth": 1, "Nahru": 3, "Niraj": 4}
# x = my_dict.items()
# print(x) 

# my_dict = {"Aman": 2, "Siddharth": 1, "Nahru": 3, "Niraj": 4}
# x = my_dict.keys()
# print(x) 


# my_dict = {"Aman": 2, "Siddharth": 1, "Nahru": 3, "Niraj": 4}
# x = my_dict.popitem()
# print(x)  

# my_dict = {"Aman": 2, "Siddharth": 1, "Nahru": 3, "Niraj": 4}
# x = my_dict.update({"Sohel":"2"})
# print(my_dict)  


# my_dict = {"Aman": 2, "Siddharth": 1, "Nahru": 3, "Niraj": 4}
# x = my_dict.values()
# print(x)  



# def table(a):
#      if a<=10:
#         print(a)
#         table(a + 1)

# table(1)


# def table(a):
#      if a<=100:
#          if a % 2 == 0:
#             print(a)
#          table(a + 1)

# table(1)


# def table(a):
#      if a<=100:
#          if a % 2 == 1:
#             print(a)
#          table(a + 1)

# table(1)


# def table(a, sum=0):
#     if a > 100: 
#         print(sum)
#     else:
#         table(a + 1, sum + a)

# table(1)



# def table(a, sum=0):
#     if a > 100:
#            print(sum)
#     else:
#         if a % 2==0:
#            table(a+1 , sum+a)
#         else:   
#          table(a + 1, sum )

# table(1)



# def table(a, sum=0):
#     if a > 100:
#            print(sum)
#     else:
#         if a % 2==1:
#            table(a+1 , sum+a)
#         else:   
#          table(a + 1, sum )

# table(1)



# def table(a, count=0):
#       if a <= 0:
#         print(count)
#       else:
#         table( a -1 , count + 1)

# table(1532)          


# def table():
#     a=1234
#     count=0    
#     if a < 0:
#         print(count)
#     else:
#         a//=10 
#         print(a)
#         count + 1
#         table()
        
# table()


# class my:
#     def __init__( self , name , rollno , course , number ):
#         self.name= name
#         self.rollno= rollno
#         self.course= course
#         self.number= number

# p= my("Siddharth" , 1 , "PGDFE" , 9098613462)
# print(p.name, p.rollno, p.course, p.number)


# p2= my("Nahru" , 2 , "PGDFE" , 9012343462)
# print(p2.name, p2.rollno, p2.course, p2.number)

# p3= my("Siddhi" , 3 , "PGDFE" , 7828144922)
# print(p3.name, p3.rollno, p3.course, p3.number)


# class my:
#     def __init__( self , name , physics , chemistry , maths ):
#         self.name= name
#         self.physics= physics
#         self.chemistry= chemistry
#         self.maths= maths

# p= my("Siddharth" , 98 , 94 , 99)
# print(p.name , (p.chemistry + p.maths + p.physics) / 300 * 100)


# p2= my("Nahru" , 39 , 45 , 56)
# print(p2.name , (p2.chemistry + p2.maths + p2.physics) / 300 * 100)

# p3= my("Siddhi" , 45 , 65 , 45)
# print(p3.name , (p3.chemistry + p3.maths + p3.physics) / 300 * 100)



# class my:
#     def __init__( self , name , rollno , course , number ):
#         self.name= name
#         self.rollno= rollno
#         self.course= course
#         self.number= number

# # p= my("Siddharth" , 1 , "PGDFE" , 9098613462)
# # print(p.name, p.rollno, p.course, p.number)


# p2= my("Nahru" , 2 , "PGDFE" , 9012343462)
# print(p2.name, p2.rollno, p2.course, p2.number)

# # p3= my("Siddhi" , 3 , "PGDFE" , 7828144922)
# # print(p3.name, p3.rollno, p3.course, p3.number)



#                                   Inheritance



# class Person:
#   def __init__(self, fname, lname):

#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)
    

# x = Person("Siddharth", "Nigam")
# x.printname()



# class person:
#     a=""

# class child(person):
#     pass
 
# x = child()
# x.a = 5
# print(x.a)  


# class person():
#     a=12

# class child(person):
#    b=2
#    pass
 
# class child1(child):
#     pass
# x = child1()
# print(x.a*x.b)  

# 



# class siddharth():
    
#     def __init__(self,name):
#         print(name)

# s=siddharth("siddharth");        

class One:
    def __init__(self, name):
        self.name = name
    
    def print_name(self):
        print(self.name)

x = One("Siddharth")
x.print_name()




class Two:
    def __init__(self, name):
        self.name = name
    
    def print_name(self):
        print(self.name)


y = Two("Nahru")
y.print_name()




class Three:
    def __init__(self, name):
        self.name = name
    
    def print_name(self):
        print(self.name)

z = Three("Anshu")
z.print_name()
