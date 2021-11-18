# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S, T):
    # write your code in Python 3.6
    S_time = getsec(S.split(":"))
    T_time = getsec(T.split(":"))

    ans = 0
    for d in range(1, T_time - S_time):
        if isInteresting(S_time + d):
            ans += 1
    return ans


def getsec(time):
    return int(time[2]) + 60 * (int(time[1]) + 60 * int(time[0]))


def isInteresting(time):
    H = str(int(time / 3600))
    if len(H) < 2:
        H = "0" + H
    M = str(int(time / 60) % 60)
    if len(M) < 2:
        M = "0" + M
    S = str(time % 60)
    if len(H) < 2:
        S = "0" + S
    print(H, M, S)
