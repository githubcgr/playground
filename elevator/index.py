floors = range(6)
peopleInElevator = []
orderedQueue = []
elevatorLevel = 0
person1 = {"at": 1, "to": 2, "name": "Person 1"}
person2 = {"at": 4, "to": 5, "name": "Person 2"}
person3 = {"at": 3, "to": 4, "name": "Person 3"}
person4 = {"at": 2, "to": 3, "name": "Person 4"}

furtherSteps = list([])
peopleQueue = list([person1, person2, person4, person3])


def moveElevator(queue):
    if not queue:
        print("Nobody is waiting")
    else:
        for floor in floors:
            for i, person in enumerate(queue):
                
                #arrive at the desired floor
                if floor == person["at"]:
                    print(f'>> {person["name"]} will join at floor: {floor}')
                elif person["at"] > floor:
                    # print(f'Person {person["name"]} will not join at floor: {floor}')
                    break
                elif person["to"] == floor:
                    print(f'<< {person["name"]} will drop at floor: {floor}')

def ordenateListByAt(enumaratedList):
    for i, person in enumerate(enumaratedList):
        if (i < len(peopleQueue) - 1):
            # print(person["at"])
            # print(peopleQueue[i+1]["at"])
            # print(enumaratedList, "\n")

            if person["at"] <= peopleQueue[i+1]["at"]:
                orderedQueue.append(person)
                if furtherSteps and len(furtherSteps) >= i:
                    furtherSteps.pop(i)
            else:
                furtherSteps.append(person)
        else:
            orderedQueue.append(person)

    # print(furtherSteps)
    while furtherSteps:
        ordenateListByAt(furtherSteps)


# def pickUpPerson(person):
#     print(f'Elevator is moving to floor: { person["at"] }')
#     peopleInElevator.append(person)
#     print(f'Picked up {person["name"]} moving to floor: { person["to"] }')
#     moveElevator()

ordenateListByAt(peopleQueue)
moveElevator(orderedQueue)

# print(orderedQueue)
# print(furtherSteps)
# moveElevator()
# print(peopleInElevator)