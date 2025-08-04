import numpy as np
def factorial():
    tempData=np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
    newTempData=np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
    hotDays=[]
    i=0
    arrLength=len(tempData)
    avg=np.mean(tempData)

    print("The average temperature is:", avg)

    highTemp=np.max(tempData)
    print("The highest temperature is:", highTemp)

    lowTemp=np.min(tempData)
    print("The lowest temperature is:", lowTemp)
    # lenTempData=len(tempData)
    # sumTemp=sum(tempData)

    for tempData[i] in range (arrLength):
        tempData[i]=(tempData[i]*9/5) + 32
        # print("The temperature in fahrenheit:", tempData, i)
        if newTempData[i]>20:
            hotDays.append(newTempData[i])
        i+=1
    print("The temperature in fahrenheit:", tempData)
    print("The temperature above 20 are:", hotDays)
    

if __name__ == "__main__":
    factorial()




