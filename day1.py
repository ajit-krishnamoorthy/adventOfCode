class Solution:
    def sumOfCalibration(self, s: str) -> int:
        nums = []
        for x in s:
            if x in '1234567890':
                nums.append(x)
            for d,val in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if s.startswith(val):
                    nums.append(str(d))
        return int(nums[0]+nums[-1])
    finalSum = 0
    with open('/Users/ajit/Desktop/Programming/adventOfCode/day1/calibrationDocument.txt') as file:
        for line in file:
            finalSum += sumOfCalibration("", line)
    print(finalSum)