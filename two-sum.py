''''''''''''''''''
''''THE PROBLEM'''
''''''''''''''''''
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

''''''''''''''''''''''''''''''''''''
'''My problem solving strategy:'''
''''''''''''''''''''''''''''''''''''

''' Step 1 -> Restate the problem in your own words:'''
# Given an array of integers, find and return the indices of two numbers that add up to a target number 

''' Step 2 -> Ask clarifying questions:'''
# What if there are no numbers that add to the target, what do I return?

''' Step 3 -> State your assumptions:'''
# I assume that each input has exactly one solution
# I assume i cannot use the same element twice 
# I assume each number appears only once 
# I assume there ARE two numbers that add up to a target and I don't have to return none or null

''' Step 4 -> Brainstorm solutions: '''
def two_sum(self, nums, target)
    answer = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                answer.extend(nums[i], nums[j])
    return answer

''' Step 5 -> Explain your rationale: '''
# This method goes through each number once and adds it to each other number in the list to see if they add up to the target
# If they do it returns the indices of the numbers 

''' Step 6 -> Discuss tradeoffs: '''
# Since this uses a double for loop, it is a slow solution, o(n^2)

''' Step 7 -> Suggest improvements: '''
# Maybe try to solve it faster using a hash table or a dictionary 
