f = open('regex_examples.txt','r')
for line in f.readlines():
    enter = input('')
    if enter == '':
        print(line)