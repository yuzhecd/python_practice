import re

def main():
    # make a pattern of re
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    asdfnsdf8130123456789dsf,my iphone number is13512346789 this, 
    not 1560099875, or110ori119, wangdachui15600998765
    '''
    #find all in a list
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------------------------------------------------------------')
    # get information from iterator
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------------------------------------------------------------')
    # use search to find
    m = pattern.search(sentence)
    while m:
        print(m.group)
        m = pattern.search(sentence, m.end())

if __name__ == '__main__':
    main()
    
