string = str(input()) + ' '
counter = 1
readyStr = ''
for i in range(len(string)):
    if i == 0: continue
    if string[i] == string[i-1]:
        counter += 1
    else:
        if counter < 2:
            readyStr += string[i-1]
        else:
            readyStr += string[i-1] + str(counter)
            counter =1
print(readyStr)
