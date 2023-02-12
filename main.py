JAR_SIZES = [70, 50, 20]
from time import perf_counter_ns


def calculate_minimum_required_jars(milk_amount: int):
    def backtrack(volume, jars=0):
        if volume in seen:
            return
        if volume < 0:
            seen.add(volume)
            return
        if jars < min(solutions, default=0):
            return
        if volume == 0:
            solutions.add(jars)
            return
        for jar_size in JAR_SIZES:
            seen.add(volume)
            backtrack(volume - jar_size, jars + 1)

    seen = set()
    solutions = set()
    backtrack(milk_amount)

    return min(solutions, default="None")

def main():
    print(calculate_minimum_required_jars(600))


if __name__ == "__main__":
    start = perf_counter_ns()
    main()
    end = perf_counter_ns()
    print(end - start)
