#Take inputs for hours worked and rate per hour
sh=input("enter hours:")
sr=input("Enter rate:")

#convert to floating point
try:
        fh=float(sh)
        fr=float(sr)
except:
        print("Please enter a numeric value")
        quit()

#If statement for overtime pay calculation
if fh>40:
    print("Pay Type: Overtime")
    reg=fh*fr
    otp= (fh-40.0)*(fr*0.50)
    print("regular",reg)
    print("overtime",otp)
    xp=reg+otp
    print("pay:",xp)
#Else statement for regular pay
else:
    print("Pay Type: Regular")
    xp=fh*fr
    print(xp)

#print final output
print("Pay:",xp)