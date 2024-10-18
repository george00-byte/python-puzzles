def getDataFromUser():

    d={}
    while True:
        studentId = input("Enter student ID: ")
        maksList = input("Enter the marks by comma separated values: ")
        moreStudents = input("Enter no to quit insertion")

        if studentId in d:
            print(studentId+" is already inserted")

        else:
            d[studentId] = maksList.split(",")

        if moreStudents.lower() == "no":
            return d

studentData = getDataFromUser()

def getAvgMarks(d):
    avgMarks ={}

    for x in d:
        L = d[x]
        s=0

        for marks in L:
            s+= int(marks)

        avgMarks[x] = s/ len(L)
    return avgMarks

avgM = getAvgMarks(studentData)

for x in avgM:
    print("Student ",x, "got avg Marks of ", avgM[x])

