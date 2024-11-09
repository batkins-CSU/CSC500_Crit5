
def main ():
    numOfYears = None

    while (numOfYears is None):
        try:
            numOfYears = int(input("Enter the number of years as an integer: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

    totalRainfall = 0
    numberOfMonthsEvaluated = 0
    for year in range(numOfYears):
        yearRainfall = 0
        for month in range(1, 13):
            monthlyRainfall = None
            while monthlyRainfall is None:
                try:
                    monthlyRainfall = float(input(f"Enter the rainfall for year {year + 1}, month {month}: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
            yearRainfall += monthlyRainfall
            numberOfMonthsEvaluated += 1
        totalRainfall += yearRainfall

        print(f"The total rainfall for year {year + 1} of is {yearRainfall} inches.")
        print(f"The average rainfall for year {year + 1} is {yearRainfall / 12} inches.")
        print(f"Total average rainfall for all years is {totalRainfall / numberOfMonthsEvaluated} inches.")


if __name__ == '__main__':
    main()