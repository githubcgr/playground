nums = [3,3]
target = 6
validOutput = list([])

for i, n in enumerate(nums):
    for iRest, nRest in enumerate(nums):
        if i > iRest:
            if (n + nRest) == target:
                validOutput.append(i)
                validOutput.append(iRest)

print(validOutput)