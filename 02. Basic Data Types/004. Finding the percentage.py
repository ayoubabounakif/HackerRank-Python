# Problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_score = student_marks[query_name]
    query_avg_score = float(sum(query_score) / 3)
    print ('{0:.2f}'.format(query_avg_score))
