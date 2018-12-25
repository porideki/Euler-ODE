import math

def euler(initial, goal, span):

    n = int(abs(goal - initial[0])/span) + 1
    y = initial[1]

    for i in range(n):
        y += span * df(initial[0] + span * i, y)
        print(i, y)

    return y

def df(x, y):
    #導関数を記述
    return - y * math.tan(x)

if __name__ == "__main__":
    print("result", euler([0, 2], 0.2, 0.1))