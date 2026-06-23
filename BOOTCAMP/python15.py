age=int(input("enter your age:"))
degree= input("enter your degree:")
cgpa=float(input("enter your cgpa:"))
if 21<=age<=40:
    if degree=="b.tech" or degree=="mca":
        if cgpa>=7.0:
            print("interview shortlisted")
        else:
            print("rejected: cgpa below 7.0")
    else:
        print("rejected: degree not eligible")