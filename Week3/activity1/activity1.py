data = open("C:\pythons Class\Week3\demo.txt","r",encoding="UTF-8")
lines = data.read()

print(lines[0:-1])
data.close()

with open("C:\pythons Class\Week3\demo.txt","a",encoding="UTF-8") as appendData:
    appendData.write("\nI am added.")

print(lines[0:-1])
appendData.close()