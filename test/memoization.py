#############
# Problem 3 #
#############

def count_ways_to_climb(s, remember = None):
    """
        1 step, 1 step, 1 step
        1 step, 2 step
        2 step, 1 step
        3 step

    With just one step to go, the ways to get
    to the top of 's' stairs is to either:

    - take a single step from the second to last step, 
    - take a double step from the third to last step, 
    - take a triple step from the fourth to last step

    We don't need to think about scenarios like taking two 
    single steps from the third to last step because this
    is already part of the first scenario (taking a single
    step from the second to last step).

    These final leaps give us a sum:

    count_ways_to_climb(s) = count_ways_to_climb(s-1) + 
                             count_ways_to_climb(s-2) +
                             count_ways_to_climb(s-3)

    To run this function for larger values of 's', you will need
    to update this function to use memoization.  The parameter
    'remember' has already been added as an input parameter to 
    the function for you to complete this task.

    The last test case is commented out because it will not work
    until the memoization is implemented.
    """
    # Base Cases
    if s == 0:
        return 0
    elif s == 1:
        return 1
    elif s == 2:
        return 2
    elif s == 3:
        return 4

    # Solve using recursion
    else:
        ways = count_ways_to_climb(s-1) + count_ways_to_climb(s-2) + count_ways_to_climb(s-3)
        return ways


print("\n=========== PROBLEM 3 TESTS ===========")
print(count_ways_to_climb(5))   # 13
print(count_ways_to_climb(20))  # 121415
# Uncomment out the test below after implementing memoization.  It won't work without it.
# print(count_ways_to_climb(100))  # 180396380815100901214157639