def print_formatted(N):
    # your code goes here


        width = len('{:b}'.format(N))

        for i in range(1, N+1):
                print(str.rjust(str(i), width),\
                str.rjust('{:o}'.format(i), width),\
                str.rjust('{:X}'.format(i), width),\
                str.rjust('{:b}'.format(i), width))

if __name__ == '__main__':
    N = int(input())
    print_formatted(N)
