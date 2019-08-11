import time

def main():
    # read file in one time
    with open('../regular_express.txt', 'r') as f:
        print(f.read())

    #read file use 'for-in'
    with open('../regular_express.txt', 'r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.45)
    print()

    #read file in a list
    with open('../regular_express.txt', 'r') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()
