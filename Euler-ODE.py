import math

def euler(initial, target, span):

    n = int(abs(target - initial[0])/span) + 1
    y = initial[1]

    for i in range(n):
        y += span * df(initial[0] + span * i, y)
        #print("y({0}): {1}".format(initial[0] + span * i, y))

    return y

def df(x, y):
    #導関数を記述
    return - y * math.tan(x)

if __name__ == "__main__":
    print("\nresult: {0}".format(euler([0, 2], 0.2, 0.1)))