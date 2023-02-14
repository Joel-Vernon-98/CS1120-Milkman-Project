from time import perf_counter
import sys

JAR_SIZES = (70, 50, 20)


def calc_minimum_jars():
    milk_amount = 69440
    extended = set()

    def branch_and_bound(volume, min_req_jars=0, solution=sys.maxsize):

        extended.add(volume)

        if volume == 0:
            return min(solution, min_req_jars)

        for jar in JAR_SIZES:

            next_volume = volume - jar
            next_min_req_jars = min_req_jars + 1

            if next_min_req_jars >= solution:
                return solution

            if next_volume in extended:
                return solution

            if next_volume >= 20 or next_volume == 0:
                solution = branch_and_bound(next_volume, next_min_req_jars, solution)

        return solution

    if milk_amount % 10 != 0:
        return "No Results Found"

    results = branch_and_bound(milk_amount)
    return results if results != sys.maxsize else "No Results Found"


def main():
    print(calc_minimum_jars())


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(end-start)