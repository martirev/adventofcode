import functools
import itertools
import os
import re
import string
import sys
import time
from collections import defaultdict, deque
from pprint import pprint

sys.path.insert(0, "../../")
from utils import copy_answer, request_submit, write_solution


def parseLine(line):
    return line


class Solution:
    def __init__(self, test=False):
        self.test = test
        filename = "input.txt"
        self.data = [
            parseLine(line) for line in open(filename).read().rstrip().split("\n")
        ]

    def getBagColor(self, bags):
        eachBag = bags.split(",")
        colors = []
        for bag in eachBag:
            temp = re.sub(r"\d", "", bag).lstrip()
            temp = temp.replace(".", "").rstrip()
            if temp[-1] == "s":
                temp = temp[0:-1]
            colors.append(temp)
        return colors

    def part1(self):
        bag = "shiny gold bag"
        d = dict()
        for l in self.data:
            line = l.split("contain")
            contains = self.getBagColor(line[1])
            container = self.getBagColor(line[0])[0]
            if container not in d:
                d[container] = set()
            for x in contains:
                d[container].add(x)
        flag = True
        bagsContaining = set()
        bagsContaining.add(bag)
        while flag:
            newbags = set(bagsContaining)
            for key in d.keys():
                for bag in bagsContaining:
                    if bag in d[key]:
                        newbags.add(key)
            if len(bagsContaining) == len(newbags):
                flag = False
            bagsContaining = newbags
        return len(bagsContaining) - 1

    def getBagColorAndNumber(self, bags):
        eachBag = bags.split(",")
        colors = []
        for bag in eachBag:
            temp = re.sub(r"\d", "", bag).lstrip()
            temp = temp.replace(".", "").rstrip()
            if temp[-1] == "s":
                temp = temp[0:-1]
            number = re.findall(r"\d", bag)
            if not number:
                number = 0
            else:
                number = int(number[0])
            t = number, temp
            colors.append(t)
        return colors

    def getTotal(self, d, key):
        counter = 0
        if key[1] not in d:
            return key[0]
        inSide = d[key[1]]
        for tuple in inSide:
            if tuple[0] == 0:
                return 1
            counter += tuple[0] * self.getTotal(d, tuple) 
        return counter + 1

    def part2(self):
        bag = "shiny gold bag"
        d = dict()
        for l in self.data:
            line = l.split("contain")
            contains = self.getBagColorAndNumber(line[1])
            container = self.getBagColor(line[0])[0]
            if container not in d:
                d[container] = set()
            for x in contains:
                d[container].add(x)
        t = 1, bag
        n = self.getTotal(d, t)
        return n - 1


def main():
    start = time.perf_counter()

    test = Solution(test=True)
    test1 = test.part1()
    test2 = test.part2()
    print(f"(TEST) Part 1: {test1}, \t{'correct :)' if test1 == 4 else 'wrong :('}")
    print(f"(TEST) Part 2: {test2}, \t{'correct :)' if test2 == 32 else 'wrong :('}")

    solution = Solution()
    part1 = solution.part1()
    part2 = solution.part2()
    print(part1_text := f"Part 1: {part1}")
    print(part2_text := f"Part 2: {part2}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")

    copy_answer(part1, part2)
    write_solution(os.path.dirname(os.path.realpath(__file__)), part1_text, part2_text)
    request_submit(2020, 7, part1, part2)


if __name__ == "__main__":
    main()
