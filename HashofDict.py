    #take in names
def namelist(names):
    # intialize count, name_list, last_list, and temp
    
    count = 0
    name_list = []
    last_list = []
    temp = ''
    
    #loop through each dictionary
    for name in names:
    #from each dictionary pull out data and append data to the new_name list
        name_list.append(names[count]['name'])
        #store last item in a temp variable
        # if last item in list, add appersand

        #add one to the counter
        count += 1
        
    # if the length of name_list is 0, return the empty string    
    if len(name_list) == 0:
        return temp
    
    # if the length of name_list is 1, convert name_list to a string and return it
    elif len(name_list) == 1:
        name_string = ' '.join(name_list)
        return name_string
    # otherwise, grab the last element and add it to last_list with a & in front of it
    else:
        temp = name_list.pop()
        last_list.append(' & ' + temp)
        
    #convert both lists' data to a string and set it to variable name_string and last_string
    #add a comma and a space to add to the joined string for name_string
    #only a space needs to be included for last_string
    
    name_string = ', '.join(name_list)
    last_string = ' '.join(last_list)
    
    #return the two strings added together
    
    return name_string + last_string