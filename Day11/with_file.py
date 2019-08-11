def main():
    try:
        with open('../regular_express.txt', 'r', encoding='ASCII') as f:
            print(f.read())
    except FileNotFoundError:
        print('can not open this file')
    except LookupError:
        print('not know encoding')

if __name__ == '__main__':
    main()
