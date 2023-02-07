JAR_SIZES = [70, 50, 20]


def calculate_minimum_jars(milk_amount: int):
    def backtrack(milk_amount, jars=0):

        if milk_amount < 0:
            return

        if milk_amount == 0:
            solutions.append(jars)

        for jar_size in JAR_SIZES:
            backtrack(milk_amount - jar_size, jars + 1)

    solutions = []
    backtrack(milk_amount)

    try:
        return f"Minimum number of jars used is {min(solutions)}"
    except ValueError:
        return f"Sorry !!! Cannot measure the required volume"


def main():
    print(calculate_minimum_jars(0))


if __name__ == "__main__":
    main()
