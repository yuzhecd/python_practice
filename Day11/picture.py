def main():
    try:
        with open('../Downloads/th.jpeg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('copy_picture.jpeg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print(e)
    print('Done')

if __name__ == '__main__':
    main()
