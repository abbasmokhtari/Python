data = open('Data.txt', 'r') #external file was opened and read permission given 
items = data.read().split()        #external file was read and turned into array
item = ''

while item.lower() != 'q':
    item = input('Add item to your list')
    items.append(item)
    if item.lower() == 'q':
        items.pop(-1) #-1 is thee last item in our array
        # this is how we open a txt file
        f = open('Data.txt', 'w') # a is command for append

        for i in range(len(items)):
            f.write(str(items[i]) + ' ') # we added space to make sure words won't stick together
    
        f.close()
        print(items)
        break


#remove items in next session with Mahan


