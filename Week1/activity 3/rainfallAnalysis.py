import numpy as np

def rainFall():
    rainFall = np.array([0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5])
    rainDays = np.size(rainFall)
    zeroRain=np.count_nonzero(rainFall == 0)
    heavyRain=[]
    avg=np.mean(rainFall)
    totalRain=np.sum(rainFall)
    i=0
    print("list to numpy array:", rainFall)
    print("Total rain fall:", totalRain)
    print("Average rain fall:", avg)
    print("Zero rain fall:", zeroRain, "days")
    # print("Heavy rainfall:", np.size(rainFall))

    for i in range (rainDays):
        # print("ss", rainDays)
        if rainFall[i]>5:
            # heavyRain.append(rainFall[i])
            heavyRain.append(i+1)
            # print("Rain with above 5mm:", rainFall[i], "Day:", i+1)
        i=i+1
    print("Days where rain was above 5mm:", heavyRain)

    percentileData = np.percentile(rainFall, 75)
    print("75th percentile of rainfall:", percentileData)

    above75 = rainFall[rainFall > percentileData]
    print("More than 75th percentile:", above75)
    


if __name__=="__main__":
    rainFall()