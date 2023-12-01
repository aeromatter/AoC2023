import re

words = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def part1():
	sum_total = 0

	with open("input.txt", "r") as f:
		for line in f:
			digits = re.findall("\d+", line)
			nums = "".join(digits)
			new_num = nums[0] + nums[-1]
			sum_total += int(new_num)
	print(sum_total)

def part2():
	sum_total = 0

	with open("part2.txt", "r") as f:
		for line in f:
			left = re.findall("^.*?(\d|one|two|three|four|five|six|seven|eight|nine).*$", line)
			right = re.findall("^.*(\d|one|two|three|four|five|six|seven|eight|nine).*?$", line)
			if not left[0].isdigit():
				left[0] = "".join([words[word] for word in left])
			if not right[0].isdigit():
				right[0] = "".join([words[word] for word in right])
			new_num = left[0] + right[0]
			sum_total += int(new_num)
	print(sum_total)

part1()
