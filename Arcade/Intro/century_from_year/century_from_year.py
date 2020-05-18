def centuryFromYear(year):
    generatedYears = [number for number in range(1, 2006)] # Generate years
    step = 100 # Initiate step to divide years into centuries
    yearsList = [generatedYears[i:i + step] for i in range(0, len(generatedYears), step)] #Divided list of years
    for century, timeList in enumerate(yearsList):
        if year in timeList:
            return century + 1 # Index starts from 0

# Alternative best solution
# using floor division
def centuryFromYear(year):
    return (year + 99) // 100

