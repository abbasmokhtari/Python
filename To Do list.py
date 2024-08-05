data = open('Data.txt', 'r') #external file was opened and read permission given 
items = data.read().split()        #external file was read and turned into array
item = ''


print('This is your To do List ', items)
print('Please type item number to remove or start adding new items')


while item.lower() != 'q':
    item = input('Add or remove item to your list')
    
    try:    
       items.pop(int(item) - 1)     
       print(items) 
    except ValueError:
        items.append(item)
      
        if item.lower() == 'q':

            items.pop(-1) #-1 is the last item in our array we wanted to remove q
            # this is how we open a txt file
            f = open('Data.txt', 'w') # a is command for append

            for i in range(len(items)):
                f.write(str(items[i]) + ' ') # we added space to make sure words won't stick together
            f.close()
            break
    
        print(items)
   
        
           


#remove items in next session with Mahan


