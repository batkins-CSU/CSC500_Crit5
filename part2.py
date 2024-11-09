

def main():
    mappingOfScores = {
        0: 0,
        2: 5,
        4: 15,
        6: 30,
        8: 60,
        }
    totalBooksPurchased = None
    while totalBooksPurchased is None:
        try:
            totalBooksPurchased = int(input("Enter the total number of books purchased as an integer: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

    if totalBooksPurchased in mappingOfScores:
        print(f"You have earned {mappingOfScores[totalBooksPurchased]} points.")
    else:
        foundPoints = None
        while foundPoints is None:
            for minBooks in mappingOfScores:
                if totalBooksPurchased >= minBooks:
                    foundPoints = mappingOfScores[minBooks]
                elif totalBooksPurchased < minBooks:
                    break

        print(f"You have earned {foundPoints} points.")

if __name__ == "__main__":
    main()

