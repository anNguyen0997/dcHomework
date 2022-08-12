# Given the list above, write a function that sorts the students
#  in the class based on their id, and returns that list

student1 = {
    "id": "478923",
    "name": "Wes",
}
student2 = {
    "id": "578490",
    "name": "Jorge",
}
student3 = {
    "id": "453789",
    "name": "Khanh",
}
student4 = {
    "id": "945890",
    "name": "Jonathan",
}
student5 = {
    "id": "578909",
    "name": "Fiona",
}

dcList = [student1, student2, student3, student4, student5]

def listSort(oldList: list) -> list:

    newList = []
    topNumber = 0

    for x in oldList:
        idNum = int(x["id"])
        if topNumber < idNum:
            newList.append(x)
            topNumber = idNum
        

print(listSort(dcList))