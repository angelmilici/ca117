def sumup(n):
    if n == 0:
        return 0
    return n + sumup(n - 1)

def main():
    print(sumup(1))

if __name__ == '__main__':
    main()
