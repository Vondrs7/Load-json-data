from read_json import ReadData
import pprint

# used other "read_json" file for read the json file
# "read_json" has ReadData class
# data stored in the "data" variable

continuation = True
e = 'Wrong answer! Please choose only "1" or "2". Press enter' # error message
read_data = ReadData()


# wrong input protection
# we can input only integer 1 or 2, otherwise error message
while continuation:
    try: 
        a = int(input('What do you want to "print"?\n\nPress "1" if all json data\nPress "2" if only "BDI" part\n\n'))
        
        if a == 1:
            data = read_data.read_json()           
            continuation = False

        elif a == 2:
            data = read_data.read_BDI()           
            continuation = False

        else:
            input(e)

    except:
        input(e)

# used "pretty print"
pprint.pprint(data)


    

    
     


