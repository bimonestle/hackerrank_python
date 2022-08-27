# A Discrete Mathematics Professor has a class of students.
# Frustrated with their lack of discipline, the professor
# decides to cancel the class if fewer than some number 
# of students who are present when the class starts.

# Arrival times go from on time (arrival_time <= 0)
# to arrived late (arrival_time > 0)

# Given the arrival time of each student and a threshold
# number of attendees, determine if the class is cancelled.

# Example 1
# k = 3
# a = [-2,-1,0,1,2]
# The first 3 stundents arrived on time.
# The last 2 stundents are late.
# The threshold is 3 students, so the class will go on.
# Return 'YES' if cancelled,
# 'NO' otherwise.

# Example 2
# k = 3
# a = [-1,-3,4,2]
# Return 'YES'

# Example 3
# k = 2
# a = [0,-1,2,1]
# Return 'NO'

def angryProfessor(k, a):
    count = 0
    for student in a:
        if student <= 0:
            count += 1
    if count >= k:
        return 'NO'
    else:
        return 'YES'