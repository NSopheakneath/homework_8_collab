def chunking_by(numbers, chunck):
    result = []
    for x in range(0,len(numbers),chunck):
        chunk = numbers[x:x+chunck] # create a list with starting index till numberss of chunks
        result.append(chunk)
    return result
while(True):
    try:
        # this line split the user input and loop through each string to convert it into interger
        user_input = input("Enter a list of numbers seperated by spaces: ")
        seperate_number = [int(x) for x in user_input.split()]
        break
    except ValueError:
        print("Enter numbers only.")

try: 
    chunk_size = int(input("Enter your desired chunk size: "))
    result = chunking_by(seperate_number,chunk_size)
    print(result)
except ValueError:
    print("Enter a valid chunk size.")
