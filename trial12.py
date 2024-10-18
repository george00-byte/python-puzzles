def findInString(x):
    x="""There was once a man named Galileo
    He wa a realy goood man"""
    x=x.lower()
    x=x.replace(" ","")
    print(x)
    x = x.find("galileo")
    if x == -1:
        print("Not Found")
    else:
        print("Found")


findInString("There was")