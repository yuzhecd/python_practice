import re

def main():
    poem = 'one, two, three, four.'
    sentence_list = re.split(r'[,,,.]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)

if __name__ == '__main__':
    main()
