#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    answer = 0
    for j in range(len(sys.argv) - 1):
        answer += int(sys.argv[j + 1])
        print(answer)

