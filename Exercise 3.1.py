#Take inputs for hours worked and rate per hour
sh=input("enter hours:")
sr=input("Enter rate:")

#convert to floating point
fh=float(sh)
fr=float(sr)
#print(fh,fr)

if fh>40:
    print("Overtime")
    rp=fh*fr
    otp= (fh-40.0)*(fr*1.50)
    print(reg,otp)
    xp=reg+otp
    print(xp)
else:
    print("Regular")
    xp=fh*fr
    print(xp)
#calculate pay in floating point
#xp=fh*fr
print("Pay:",round(xp))