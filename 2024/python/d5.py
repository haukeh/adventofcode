from collections import defaultdict
from typing import List


def parse_rule(rule: str):
    before, after = rule.strip().split("|")
    return (int(before), int(after))


rules, updates = open("../input/d5.txt").read().split("\n\n")
flat_rules = [parse_rule(rule) for rule in rules.split("\n")]
rule_map = defaultdict(set)
for before, after in flat_rules:
    rule_map[before].add(after)


def sort(nums: List[int]) -> List[int]:
    all = set(nums)
    i = 0
    while i < len(nums):
        after = rule_map.get(nums[i])
        if after:
            inter = after & all
            for e in inter:
                idx = nums.index(e)
                if idx < i:
                    i = idx
                elem = nums.pop(idx)
                nums.append(elem)
        i += 1

    return nums


p1 = 0
incorrect = []

for update in updates.strip().split("\n"):
    nums = list(map(int, update.split(",")))
    seen = set()
    bad = False
    for num in nums:
        after = rule_map.get(num)
        if after:
            i = seen & after
            if len(i) > 0:
                bad = True
                incorrect.append(nums)
                break

        seen.add(num)

    if not bad:
        p1 += nums[len(nums) // 2]

sorted = []
for update in incorrect:
    sorted.append(sort(update))

p2 = sum([nums[len(nums) // 2] for nums in sorted])

print(p1)
print(p2)
