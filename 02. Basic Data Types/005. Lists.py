# Problem: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    n = int(input())
    result = []
    for i in range(n):
        ask_user = input().split()
        command = ask_user[0]
        arguments = ask_user[1:]
        if command == "insert":
            result.insert(int(arguments[0]), int(arguments[1]))
        elif command == "print":
            print (result)
        elif command == "remove":
            result.remove(int(arguments[0]))
        elif command == "append":
            result.append(int(arguments[0]))
        elif command == "sort":
            result.sort()
        elif command == "pop":
            result.pop()
        elif command == "reverse":
            result.reverse()

### Using eval built-in function
            
n = input()
list_ = []
for _ in range(n):
    ask_user = input().split()
    command = ask_user[0]
    args = ask_user[1:]
    if command != "print":
        command += "("+ ",".join(args) +")"
        eval("list_." + command)
    else:
        print (list_)

# command += "("+ ",".join(args) +")" will change the input
# to command(args) by joining them together so it can be interpreted
# then you evaluate that command on your list "list_." + command
# use of '.' is obvious list_.command(args)
