def power(m, n):
    if n == 0:
        return 1
    return power(m, n - 1) * m

def main():
    print(power(4, 4))

if __name__ == '__main__':
    main()
