floors = range(6)
orderedQueue = list(range(4))
person1 = {"at": 1, "to": 2, "name": "Person 1"}
person2 = {"at": 4, "to": 5, "name": "Person 2"}
person3 = {"at": 3, "to": 4, "name": "Person 3"}
person4 = {"at": 2, "to": 3, "name": "Person 4"}
peopleQueue = list([person1, person2, person3, person4])

def moveElevator(queue):
    if not queue:
        print("Nobody is waiting")
    else:
        for floor in floors:
            for person in queue:
                #arrived at the desired floor
                if floor == person["at"]:
                    print(f'>>>> {person["name"]} at floor: {floor}')
                elif person["at"] > floor:
                    break
                elif person["to"] == floor:
                    print(f'<< {person["name"]} at floor: {floor}')

def ordenateListByAt(enumaratedList):
    for i, person in enumerate(enumaratedList):
        yes = 1
        for restI, restPeople in enumerate(enumaratedList):
            if i != restI:
                if person["at"] <= restPeople["at"]:
                    yes+=1
            
            if restI == len(enumaratedList)-1:
                orderedQueue[len(enumaratedList)-yes] = person

# ------------------------------
ordenateListByAt(peopleQueue)
moveElevator(orderedQueue)