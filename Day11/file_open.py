def main():
    f = None
    try:
        f = open('honglou.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('can not open file')
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    main()
