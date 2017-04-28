def comma(thing):
    for i in range(0,len(thing)):
        if i == len(thing)-2:
            print(thing[i],end=', and ')
        elif i == len(thing)-1:
            print(thing[i])
        else:
            print(thing[i],end=', ')

spam = ['apples', 'bananas', 'tofu', 'cats', 'balls', 'stuff', 'works']
comma(spam)
        
