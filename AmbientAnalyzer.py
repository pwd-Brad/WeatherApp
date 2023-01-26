

def getListFromFile(inputFile):
    outputList = []
    try:
        source = open(inputFile,"r")
        outputList =  source.readlines()
        source.close()

        del outputList[0]
        
    except FileNotFoundError:
        print("Unable to open input file: " + inputFile)

    return outputList

#######################################

def daysBelow(masterFile):

    days = []

    results = []

    yearQuery = input("\nInput year: ")
    tempQuery = int(input("\nInput temperature: "))

    for data in masterFile:

        split = data.split(",")
        date = split[0]
        dateSplit = date.split("T")
        day = dateSplit[0]
        yearSplit = day.split("-")
        year = yearSplit[0]
        temp = int(float(split[1]))
        if year == yearQuery:
            if temp < tempQuery:
                days.append(day)

    for data in days:
        if data not in results:
            results.append(data)


    numDays = str(len(results))
        

    print("\nNumber of days below " + str(tempQuery)+ " degrees: " + numDays)

    daysQuery = input("\nDisplay list of days? Y/N: ").lower()
    print("\n")
    
    if daysQuery == "y":
        results.sort()
        for data in results:
            dates = data.split(",")
            print(dates[0])

#######################################

def daysAbove(masterFile):

    days = []

    results = []

    yearQuery = input("\nInput year: ")
    tempQuery = int(input("\nInput temperature: "))

    for data in masterFile:

        split = data.split(",")
        date = split[0]
        dateSplit = date.split("T")
        day = dateSplit[0]
        yearSplit = day.split("-")
        year = yearSplit[0]
        temp = int(float(split[1]))
        if year == yearQuery:
            if temp > tempQuery:
                days.append(day)

    for data in days:
        if data not in results:
            results.append(data)


    numDays = str(len(results))
        

    print("\nNumber of days above " + str(tempQuery)+ " degrees: " + numDays)

    daysQuery = input("\nDisplay list of days? Y/N: ").lower()
    print("\n")
    
    if daysQuery == "y":
        results.sort()
        for data in results:
            dates = data.split(",")
            print(dates[0])
            
#######################################

def tempExtreme(masterFile):

    temps = []
    yearData = []

    yearQuery = input("\nInput year: ")

    for data in masterFile:
        split = data.split(",")
        date = split[0]
        dateSplit = date.split("T")
        day = dateSplit[0]
        yearSplit = day.split("-")
        year = yearSplit[0]
        temp = int(float(split[1]))
        if year == yearQuery:
            yearData.append(data)
            temps.append(temp)

    maxResult = max(temps)
    minResult = min(temps)

    maxIndex = temps.index(maxResult)
    minIndex = temps.index(minResult)

    for data in [maxIndex]:
        result = (yearData[data])
        split = result.split(",")
        dateTime = split[0]
        dateTimeSplit = dateTime.split("T")
        date = dateTimeSplit[0]
        temp = split[1]
        print("------------")
        print("MAX TEMPERATURE")
        print("Date: " + date + "\nTemperature: " + temp + " degrees")
        print("------------")
        
    for data in [minIndex]:
        result = (yearData[data])
        split = result.split(",")
        dateTime = split[0]
        dateTimeSplit = dateTime.split("T")
        date = dateTimeSplit[0]
        temp = split[1]
        print("------------")
        print("MIN TEMPERATURE")
        print("Date: " + date + "\nTemperature: " + temp + " degrees")
        print("------------")

#######################################

def menu():
    print("(1) Display Menu")
    print("(2) Maximum and Minimum Temps")
    print("(3) Days Above Temp")
    print("(4) Days Below Temp")
    print("(5) Load New File")
    print("(6) Quit")

#######################################

masterFile = getListFromFile("master.csv")

menu()

run = True

while run == True:

    selection = input("\nInput selection or enter 1 for menu: ").lower()

    if selection == "1":
        menu()

    elif selection == "2":
        print("\nMaximum and Minimum Temperatures selected.")
        tempExtreme(masterFile)

    elif selection == "3":
        print("\nDays above specified temp selected.")
        daysAbove(masterFile)

    elif selection == "4":
        print("\nDays below specified temp selected.")
        daysBelow(masterFile)

    elif selection == "5":
        print("Load new file selected.")
        inputFile = input("\nInput file name: ")
        masterfile = getListFromFile(inputFile)

    elif selection == "6":
        run = False

    else:
        print("\nInvalid selection.")

print("Closing Ambient Analyer. Goodbye.")
        
        
        
        



