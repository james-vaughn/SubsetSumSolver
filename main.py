from multiprocessing import Pool, cpu_count
from argparse import ArgumentParser
from functools import lru_cache


def formatSolver(target, nums):
    solution = solve(target, sorted(nums, reverse=True))
    return f"{target}: {solution}"


# Returns the first solution to the subset sum problem found
# Uses a dynamic programming approach
def solve(target, nums):
    @lru_cache(maxsize=None)
    def subsetSum(idx, num):
        if idx >= len(nums):
            return frozenset()
        if nums[idx] == num:
            return frozenset([idx])
        with_v = subsetSum(idx + 1, num - nums[idx])
        if with_v:
            return with_v | frozenset([idx])
        else:
            return subsetSum(idx + 1, num)
    try:
        solution = list(nums[i] for i in subsetSum(0, target))
        return solution if not solution == [] else None
    except Exception as e:
        print(f"Error solving {target}: {e}")


def logResult(results, outputFilename):
    with open(outputFilename, "w") as file:
        for line in results:
            file.write(line + "\n")


if __name__ == '__main__':
    argParser = ArgumentParser()
    argParser.add_argument("-f", dest="filename", type=str, help="File to process")
    argParser.add_argument("-o", dest="output", default="output.txt", type=str, help="Output file location")
    argParser.add_argument("-p", dest="processes", default=cpu_count(), type=int, help="Size of process pool")
    args = argParser.parse_args()

    problems = []
    results = []

    try:
        with open(args.filename, "r") as file:
            for inputLine in file:
                line = inputLine.strip().replace(" ", "")
                if line:
                    problems.append(list(map(float, line.split(","))))
    except:
        print("""
        Input file not formatted correctly. 
        The file should be in the form 'solution, value1, value2, ...'""")
        quit()

    pool = Pool(processes=args.processes)
    for problem in problems:
        pool.apply_async(formatSolver, args=(problem[0], problem[1:]),
                         callback=results.append)

    pool.close()
    pool.join()

    logResult(results, args.output)
