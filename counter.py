def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    #file_name = 'mbox-short.txt'
    open_file = open(file_name)
    counter = {}
    # ^ creates an open dictionary that we'll use to count the number if iterations
    for line in open_file:
        if line.startswith("From "):
            # ^ the space after "From" ensure it won't pull lines with ":"
            split_line = line.split()
            # ^ splits the line into individual words in the form of a list
            day = split_line[2]
            # ^ targets the 3rd word in the line (aka 3rd item in list)
            counter[day] = counter.get(day, 0) + 1
            # ^ inputs the day variable as the key in the counter dictionary
                # .get() searches the dictionary for a particuarl key, value pair
                # "+ 1" adds 1 to the value of each key iteration
                    # since there are 6 iterations of 'Thu' the loop runs 6 times
                    # on that pair and adds 1 to the value for each loop
    print(counter)
            
    
            


## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
