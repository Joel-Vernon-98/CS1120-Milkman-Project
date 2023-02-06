class MinimumJarCalculator:
    def __init__(self, milk_amount):
        self.milk_amount = milk_amount
        self.solutions = []
        self.JAR_SIZES = [70, 50, 20]

    def backtrack(self, milk_amount, jars=0):
        if milk_amount < 0:
            return

        if milk_amount == 0:
            self.solutions.append(jars)
            return

        for jar_size in self.JAR_SIZES:
            self.backtrack(milk_amount - jar_size, jars + 1)

    def find_minimum_jar_count(self):
        self.backtrack(self.milk_amount)
        try:
            return print(f"Minimum number of jars used is: {min(self.solutions)}")
        except ValueError:
            return print("Sorry !!! Cannot measure required volume")


def main():
    minimum_jar_calculator = MinimumJarCalculator(140)
    minimum_jar_calculator.find_minimum_jar_count()


if __name__ == "__main__":
    main()
