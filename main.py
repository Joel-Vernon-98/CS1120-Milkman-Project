JAR_SIZES = (70, 50, 20)
from time import perf_counter_ns


def calculate_minimum_required_jars(milk_amount: int):
    def backtrack(volume, solution=0, jars=0):

        if jars < min(solutions, default=-1):
            return

        if volume == 0:
            solutions.add(jars)
            return

        for jar_size in JAR_SIZES:

            next_jar = volume - jar_size
            if next_jar >= 20 or next_jar == 0:
                backtrack(volume - jar_size, solution, jars + 1)
            else:
                continue

    solutions = set()
    if milk_amount % 10 != 0:
        return print("Sorry !!! Cannot measure the required volume")

    backtrack(milk_amount)
    try:
        print(solutions, sep="\n")
        return print(f"Minimum number of jars used: {min(solutions)}")
    except ValueError:
        return print("Sorry !!! Cannot measure the required volume")


def main():
    calculate_minimum_required_jars(65000)


if __name__ == "__main__":
    start = perf_counter_ns()
    main()
    end = perf_counter_ns()
    print(end - start)
