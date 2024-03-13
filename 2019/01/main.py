import time

def parseLine(line):
    return line


class Solution:
    def __init__(self, test=False):
        self.test = test
        filename = "testinput.txt" if self.test else "input.txt"
        self.data = [int(line) for line in open(filename).read().rstrip().split("\n")]

    def part1(self):
        fuel = 0
        for moudle in self.data:
            fuel += moudle // 3 - 2
        return fuel

    def part2(self):
        fuel = 0
        for moudle in self.data:
            temp =  moudle // 3 - 2
            while temp > 0:
                fuel += temp 
                temp = temp // 3 - 2
        return fuel


def main():
    start = time.perf_counter()

    test = Solution(test=True)
    test1 = test.part1()
    test2 = test.part2()
    print(f"(TEST) Part 1: {test1}, \t{'correct :)' if test1 == 33583 else 'wrong :('}")
    print(f"(TEST) Part 2: {test2}, \t{'correct :)' if test2 == 50346 else 'wrong :('}")

    solution = Solution()
    part1 = solution.part1()
    part2 = solution.part2()
    print(part1_text := f"Part 1: {part1}")
    print(part2_text := f"Part 2: {part2}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")

if __name__ == "__main__":
    main()
