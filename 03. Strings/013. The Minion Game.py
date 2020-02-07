# Problem: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = "AEIOU"
    kevin, stuart = 0, 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += (len(string) - i)
        else:
            stuart += (len(string) - i)
    if kevin > stuart:
        print ("Kevin", kevin)
    elif kevin < stuart:
        print ("Stuart", stuart)
    else:
        print ("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
