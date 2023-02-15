import sys
JAR_SIZES = (70, 50, 20)


def calc_minimum_jars():

    def dfs(volume, min_req_jars=0, solution=sys.maxsize):
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
                solution = dfs(next_volume, next_min_req_jars, solution)
        return solution

    valid_input = False
    while not valid_input:
        try:
            milk_amount = int(input("Enter milk amount: "))
            if milk_amount > 69440:
                raise RecursionError
            valid_input = True
        except ValueError:
            print("Invalid Input: Please Enter an integer.")

        except RecursionError:
            print("Volumes larger than 69440ml are too large to calculate, please enter a smaller number.")

    extended = set()

    if milk_amount % 10 != 0:
        return "Sorry !!! Cannot measure the required volume"
    results = dfs(milk_amount)
    return f"Minimum number of jars required is: {results}" if results != sys.maxsize \
        else "Sorry !!! Cannot measure the required volume"


def main():
    print(calc_minimum_jars())


if __name__ == "__main__":
    main()

