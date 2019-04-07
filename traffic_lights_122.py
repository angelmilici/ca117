import sys

def main():
    dist = int(sys.stdin.readline())

    time = 0
    dist_2 = 0
    diff = 0
    for line in sys.stdin:
        line = line.strip().split()

        dist_2, red, green = int(line[0]), int(line[1]), int(line[2])
        time = time + (dist_2 - diff)
        stop_time = time - ((red + green) * (time // (red + green)))

        if stop_time < red:
            other = (red - stop_time)
            time = time + other

        diff = dist_2

    time = time + (dist - dist_2)
    print(time)

if __name__ == '__main__':
    main()
