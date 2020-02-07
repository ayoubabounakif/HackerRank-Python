# Problem: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    n = int(input())
    marksheet = [[input(), float(input())]
                 for _ in range(int(n))]
    if 2 <= n <= 5:
        # for each nest in marksheet
        # sort via the score in ascending
        # with {} within sorted[] it creates a "set"
        # output is [37.2, 37.21, 39, 41] - sets remove additonal same numbers
        sorted_score = sorted({s[1] for s in marksheet})

        # for each nest in marksheet (s)
        # return a sorted list (sorted by their names (s[0]))
        # of students whos score (s[1]) is equal to s[1] in sorted_score
        # sorted_name = ["Berry", "Harry"]
        sorted_name = sorted(s[0] for s in marksheet if s[1] == sorted_score[1])

        #.join(sorted_name) takes each element in the sorted_name list
        # so ["Berry", "Harry"]
        # "\n" seperates using a newline BETWEEN each element
        # output is "Berry\nHarry"
        print('\n'.join(sorted_name))

def secondLowestGrade(classList):
    secondLowestScore = sorted(set(_[1] for _ in classList))[1]
    result = sorted([_[0] for _ in classList if _[1] == secondLowestScore])
    return result


numberOfStudents = int(input())
classList = []
for i in range(numberOfStudents):
    classList.append([str(input()), float(input())])
# print('\n'.join(secondLowestGrade(classList)))
