# def function(length):
#     otp=""   
#     for i in range(1,length):
#       otp+=Math.floor(Math.random()*10)
#       print(i)

import random

def generate_otp(length):
    otp = ""   
    for i in range(length):
        otp += str(random.randint(0, 9))
    print(otp)
    
generate_otp(6)  
