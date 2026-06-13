def password():

    password = input("Enter the password : ")
   
    special_ch ="!@#$%^&*-_.?"

    allowed = special_ch + "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    if not all(ch in allowed for ch in password):
         print("Invalid password: contains unsupported characters")
         return
    

    score = 0
    

    if len(password)>=8:
        print("length of password is greater than or equal to 8")
        score += 1
    else: 
        print("Password should contain at least 8 characters")
    
    if  any(ch.isupper() for ch in password ): 
        print("Password contains uppercase")
        score += 1
    else:
        print("Password should have at least one uppercase letter") 
    
    if any(ch.islower() for ch in password ): 
        print("Password contains lowercase")
        score += 1
    else:
        print("Password should have at least one lowercase letter") 
    
    if any(ch in special_ch for ch  in password):
        print("Password contains special character")
        score += 1
    else:
        print("Password should have at least one special character") 
                   
    if any( ch.isdigit() for ch in password):
        print("Password contains digit")
        score += 1
    else:
        print("Password should have at least one digit") 
    
    if len(password)>=12:
        score += 1
    
    
   
   
    if (score<=2):
        print("Password strength : Weak")
    elif(score<=4):
        print("Password strength : Medium")
    elif(score == 5):
        print("Password strength : Strong")
    else:
        print("Password strength : Very Strong")
 


password()
