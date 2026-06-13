from tkinter import *

root = Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

password_label = Label(root, text="Enter Password", font=("Arial", 18, "bold") )
password_label.pack(pady=30)

password_entry = Entry(root, show="*", width=30, font=("Arial",16))
password_entry.pack()

length_label = Label(root, text="")
length_label.pack()

upper_label = Label(root, text="")
upper_label.pack()

lower_label = Label(root, text="")
lower_label.pack()

digit_label = Label(root, text="")
digit_label.pack()

special_label = Label(root, text="")
special_label.pack()

result_label = Label(root, text="")
result_label.pack(pady=20)

def check_password():
    password = password_entry.get()

    special_ch ="!@#$%^&*-_.?"

    allowed = special_ch + "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    if not all(ch in allowed for ch in password):
        result_label.config(text="Invalid password: contains unsupported characters", fg="red")
        return
    

    score = 0
    

    if len(password)>=8:
        length_label.config(text="length of password is at least 8 characters", fg="green")
        score += 1
    else: 
        length_label.config(text="Password must contain at least 8 characters", fg="red")
    
    if  any(ch.isupper() for ch in password ): 
        upper_label.config(text="Password contains an uppercase letter", fg="green")
        score += 1
    else:
        upper_label.config(text="Password must contain an uppercase letter", fg="red") 
    
    if any(ch.islower() for ch in password ): 
        lower_label.config(text="Password contains a lowercase letter", fg="green")
        score += 1
    else:
        lower_label.config(text="Password must contain a lowercase letter", fg="red") 
    
    if any(ch in special_ch for ch  in password):
        special_label.config(text="Password contains a special character", fg="green")
        score += 1
    else:
        special_label.config(text="Password must contain a special character", fg="red") 
                   
    if any( ch.isdigit() for ch in password):
        digit_label.config(text="Password contains a digit", fg="green")
        score += 1
    else:
        digit_label.config(text="Password must contain a digit", fg="red") 
    
    if len(password)>=12:
        score += 1
    
    
   
   
    if (score<=2):
        result_label.config(text="Password Strength: Weak", fg="red")
        
    elif(score<=4):
        result_label.config(text="Password Strength: Medium", fg="orange")
        
    elif(score == 5):
        result_label.config(text="Password Strength: Strong", fg="green")
        
    else:
        result_label.config(text="Password Strength: Very Strong", fg="darkgreen")
        
       
 
check_btn = Button(
    root,
    text="Check Strength",
    font=("Arial",12,"bold"),
    command=check_password
)

check_btn.pack(pady=10)

root.mainloop()