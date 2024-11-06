class Tuscan:
    @staticmethod
    def generate_tuscan_permutations(arg):
        if arg == 3:
            Tuscan.generate_three()
        elif arg == 5:
            Tuscan.generate_five()
        else:
            Tuscan.generate_tuscan_square(arg)
        return Tuscan.r

    @staticmethod
    def helper(a, i):
        Tuscan.r[i] = a[:]

    @staticmethod
    def generate_tuscan_square(n):
        nn = n
        # Compute base size for Tuscan square
        while (n - 1) % 4 == 0 and n != 1 and n != 9:
            n = (n - 1) // 2 + 1
        
        # Initialize `r` as a matrix of zeroes with size `nn x (nn + 1)`
        Tuscan.r = [[0] * (nn + 1) for _ in range(nn)]

        if n % 2 == 0:
            a = [0] * n
            for i in range(0, n, 2):
                a[i] = i // 2
                a[i + 1] = n - 1 - a[i]
            Tuscan.helper(a, 0)
            for j in range(1, n):
                a = [(x + 1) % n for x in a]
                Tuscan.helper(a, j)
        elif n % 4 == 3:
            k = (n - 3) // 4
            b = [0] * n
            for i in range(n - 1):
                p = (1 if i == 0 else
                     (4 * k + 2 if i == k + 1 else
                      (3 if i == 2 * k + 2 else
                       (4 * k if i == 3 * k + 2 else 2 * k))))
                a = [0] * n
                for j in range(n):
                    index = n + j - p if j < p else j - p
                    a[index] = (n - 1 if j == 0 else (i + (j // 2 if j % 2 == 0 else n - 1 - (j - 1) // 2))) % (n - 1)
                b[a[n - 1]] = a[0]
                Tuscan.helper(a, i)
            t = [0] * n
            t[0] = n - 1
            for i in range(1, n):
                t[i] = b[t[i - 1]]
            Tuscan.helper(t, n - 1)
        elif n == 9:
            t = [
                [0, 1, 7, 2, 6, 3, 5, 4, 8],
                [3, 7, 4, 6, 5, 8, 1, 2, 0],
                [1, 4, 0, 5, 7, 6, 8, 2, 3],
                [6, 0, 7, 8, 3, 4, 2, 5, 1],
                [2, 7, 1, 0, 8, 4, 5, 3, 6],
                [7, 3, 0, 2, 1, 8, 5, 6, 4],
                [5, 0, 4, 1, 3, 2, 8, 6, 7],
                [4, 3, 8, 7, 0, 6, 1, 5, 2],
                [8, 0, 3, 1, 6, 2, 4, 7, 5]
            ]
            for i in range(9):
                Tuscan.helper(t[i], i)
        else:
            assert False

        # Grow the matrix to the final size `nn x (nn + 1)`
        while nn != n:
            n = n * 2 - 1
            h = (n + 1) // 2
            # Expand `r` matrix for larger size requirements
            new_r = [[0] * (n + 1) for _ in range(n)]
            # Copy existing values into new matrix `new_r`
            for i in range(len(Tuscan.r)):
                for j in range(len(Tuscan.r[i])):
                    new_r[i][j] = Tuscan.r[i][j]
            Tuscan.r = new_r
            
            # Fill values in the expanded matrix
            for i in range(h):
                for j in range(h):
                    Tuscan.r[i][n - j] = Tuscan.r[i][j] + h
            for i in range(h, n):
                for j in range(h - 1):
                    Tuscan.r[i][j] = ((0 if j % 2 == 0 else h) + (i - h + (j // 2 if j % 2 == 0 else h - 2 - (j - 1) // 2))) % (h - 1)
                Tuscan.r[i][h - 1] = h - 1
                for j in range(h, n + 1):
                    Tuscan.r[i][j] = ((0 if j % 2 == 0 else h) + Tuscan.r[i][j - h] % h)
            for i in range(n):
                l = 0
                while l < n and Tuscan.r[i][l] != n:
                    l += 1
                t = [0] * n
                t[:n - l] = Tuscan.r[i][l + 1:]
                t[n - l:] = Tuscan.r[i][:l]
                Tuscan.r[i][:] = t



    @staticmethod
    def generate_three():
        Tuscan.r = [
            [0, 1, 2, 0],
            [1, 0, 2, 0],
            [2, 0, 0],
            [2, 1, 0]
        ]

    @staticmethod
    def generate_five():
        Tuscan.r = [
            [0, 1, 2, 3, 4, 0],
            [1, 0, 3, 2, 4, 0],
            [4, 3, 0, 2, 1, 0],
            [1, 4, 2, 0, 0],
            [0, 4, 1, 3, 0],
            [4, 0, 3, 1, 0]
        ]

    @staticmethod
    def print_square(square):
        for row in square:
            print(" ".join(map(str, row)))

if __name__ == "__main__":
    sizes = [
12,
112]
    for size in sizes:
        # print(f"Tuscan Square of size {size}:")
        square = Tuscan.generate_tuscan_permutations(size)
        print(len(square))
        # Tuscan.print_square(square)
        # print()
