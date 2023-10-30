#!/usr/bin/python3
"""
backtracking program nqueen
"""


from sys import argv

if __name__ == "__main__":
    avellin = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    num = int(argv[1])
    if num < 4:
        print("N must be at least 4")
        exit(1)

    '''init range'''
    for b in range(num):
        avellin.append([b, None])

    def checker(z):
        """chekcs it doesn't alrady exists"""
        for z in range(num):
            if z == a[y][1]:
                return True
        return False

    def rejector(y, z):
        """evaluate whether rejecting the return or not"""
        if (checker(z)):
            return False
        b = 0
        while(b < y):
            if abs(avellin[b][1] - z) == abs(b - y):
                return False
            b += 1
        return True

    def clear_me(y):
        """clears the answers"""
        for b in range(y, num):
            avellin[b][1] = None

    def nqueens(y):
        """recursive backtracking fx"""
        for z in range(num):
            clear_me(y)
            if reject(y, z):
                a[y][1] = z
                if (y == num - 1):
                    print(avellin)
                else:
                    nqueens(y + 1)

    nqueens(0)
