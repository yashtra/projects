# black - 3, blonde - 2, red - 1
# brown - 3, blue - 2, green - 1
# O - 3, A - 2, B - 1

import csv

buffer = []
dom = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
file = open("C:/Users/Yash Verma/OneDrive/Desktop/genetics2.csv" , 'r') 
for i in file:
    i = i[:-1:]
    buffer.append(i.split(','))

buffer.pop(0)

for i in range(0, len(buffer)-1, 2):
    print("Couple", int((i+2)/2), " :")
    print("Person 1: ", buffer[i][0], " , Person 2: ", buffer[i+1][0])
    print("Traits (Person 1): Hair color-" +
          buffer[i][1]+", Eye color-"+buffer[i][2]+", Blood group-"+buffer[i][3])
    print("Traits (Person 2): Hair color-"+buffer[i+1]
          [1]+", Eye color-"+buffer[i+1][2]+", Blood group-"+buffer[i+1][3])

    # Hair Color
    if (buffer[i][1] == 'black' and buffer[i+1][1] == 'red'):
        print("Dominant person: "+buffer[i][0] +
              " , Hair Color-Dominant trait: "+buffer[i][1])
        dom[i] = dom[i]+1
    elif (buffer[i][1] == 'black' and buffer[i+1][1] == 'blonde'):
        print("Dominant person: "+buffer[i][0] +
              " , Hair Color-Dominant trait: "+buffer[i][1])
        dom[i] = dom[i]+1
    elif (buffer[i][1] == 'red' and buffer[i+1][1] == 'black'):
        print("Dominant person: "+buffer[i+1][0] +
              " , Hair Color-Dominant trait: "+buffer[i+1][1])
        dom[i+1] = dom[i+1]+1
    elif (buffer[i][1] == 'blonde' and buffer[i+1][1] == 'black'):
        print("Dominant person: "+buffer[i+1][0] +
              " , Hair Color-Dominant trait: "+buffer[i+1][1])
        dom[i+1] = dom[i+1]+1
    elif (buffer[i][1] == 'black' and buffer[i+1][1] == 'black'):
        print("Both Dominant"+" , Hair Color-Dominant trait: "+buffer[i+1][1])
        dom[i] = dom[i]+1
        dom[i+1] = dom[i+1]+1
    elif (buffer[i][1] == 'blonde' and buffer[i+1][1] == 'red'):
        print("Dominant person: "+buffer[i][0] +
              " , Hair Color-Dominant trait: "+buffer[i][1])
        dom[i] = dom[i]+1
    elif (buffer[i][1] == 'red' and buffer[i+1][1] == 'blonde'):
        print("Dominant person: "+buffer[i+1][0] +
              " , Hair Color-Dominant trait: "+buffer[i+1][1])
        dom[i+1] = dom[i+1]+1
    elif (buffer[i][1] == 'blonde' and buffer[i+1][1] == 'blonde'):
        print("Both Dominant"+" , Hair Color-Dominant trait: "+buffer[i+1][1])
        dom[i] = dom[i]+1
        dom[i+1] = dom[i+1]+1
    elif (buffer[i][1] == 'red' and buffer[i+1][1] == 'red'):
        print("Both Dominant"+" , Hair Color-Dominant trait: "+buffer[i+1][1])
        dom[i] = dom[i]+1
        dom[i+1] = dom[i+1]+1

    # Eye Color
    if (buffer[i][2] == 'brown' and buffer[i+1][2] == 'blue'):
        print("Dominant person: "+buffer[i][0] +
              " , Eye Color-Dominant trait: "+buffer[i][2])
        dom[i] = dom[i]+1
    elif (buffer[i][2] == 'brown' and buffer[i+1][2] == 'green'):
        print("Dominant person: "+buffer[i][0] +
              " , Eye Color-Dominant trait: "+buffer[i][2])
        dom[i] = dom[i]+1
    elif (buffer[i][2] == 'blue' and buffer[i+1][2] == 'brown'):
        print("Dominant person: "+buffer[i+1][0] +
              " , Eye Color-Dominant trait: "+buffer[i+1][2])
        dom[i+1] = dom[i+1]+1
    elif (buffer[i][2] == 'green' and buffer[i+1][2] == 'brown'):
        print("Dominant person: "+buffer[i+1][0] +
              " , Eye Color-Dominant trait: "+buffer[i+1][2])
        dom[i+1] = dom[i+1]+1
    elif (buffer[i][2] == 'brown' and buffer[i+1][2] == 'brown'):
        print("Both Dominant"+" , Eye Color-Dominant trait: "+buffer[i+1][2])
        dom[i] = dom[i]+1
        dom[i+1] = dom[i+1]+1
    elif (buffer[i][2] == 'blue' and buffer[i+1][2] == 'green'):
        print("Dominant person: "+buffer[i][0] +
              " , Eye Color-Dominant trait: "+buffer[i][2])
        dom[i] = dom[i]+1
    elif (buffer[i][2] == 'green' and buffer[i+1][2] == 'blue'):
        print("Dominant person: "+buffer[i+1][0] +
              " , Eye Color-Dominant trait: "+buffer[i+1][2])
        dom[i+1] = dom[i+1]+1
    elif (buffer[i][2] == 'green' and buffer[i+1][2] == 'green'):
        print("Both Dominant"+" , Eye Color-Dominant trait: "+buffer[i+1][2])
        dom[i] = dom[i]+1
        dom[i+1] = dom[i+1]+1
    elif (buffer[i][2] == 'blue' and buffer[i+1][2] == 'blue'):
        print("Both Dominant"+" , Eye Color-Dominant trait: "+buffer[i+1][2])
        dom[i] = dom[i]+1
        dom[i+1] = dom[i+1]+1

    # Blood group
    if (buffer[i][3] == 'A' and buffer[i+1][3] == 'B'):
        print("Dominant person: "+buffer[i][0] +
              " , Blood Group-Dominant trait: "+buffer[i][3])
        dom[i] = dom[i]+1
    elif (buffer[i][3] == 'A' and buffer[i+1][3] == 'O'):
        print("Dominant person: "+buffer[i][0] +
              " , Blood Group-Dominant trait: "+buffer[i][3])
        dom[i] = dom[i]+1
    elif (buffer[i][3] == 'B' and buffer[i+1][3] == 'A'):
        print("Dominant person: "+buffer[i+1][0] +
              " , Blood Group-Dominant trait: "+buffer[i+1][3])
        dom[i+1] = dom[i+1]+1
    elif (buffer[i][3] == 'O' and buffer[i+1][3] == 'A'):
        print("Dominant person: "+buffer[i+1][0] +
              " , Blood Group-Dominant trait: "+buffer[i+1][3])
        dom[i+1] = dom[i+1]+1
    elif (buffer[i][3] == 'A' and buffer[i+1][3] == 'A'):
        print("Both Dominant"+" , Blood Group-Dominant trait: "+buffer[i+1][3])
        dom[i] = dom[i]+1
        dom[i+1] = dom[i+1]+1
    elif (buffer[i][3] == 'B' and buffer[i+1][3] == 'O'):
        print("Dominant person: "+buffer[i][0] +
              " , Blood Group-Dominant trait: "+buffer[i][3])
        dom[i] = dom[i]+1
    elif (buffer[i][3] == 'O' and buffer[i+1][3] == 'B'):
        print("Dominant person: "+buffer[i+1][0] +
              " , Blood Group-Dominant trait: "+buffer[i+1][3])
        dom[i+1] = dom[i+1]+1
    elif (buffer[i][3] == 'O' and buffer[i+1][3] == 'O'):
        print("Both Dominant"+" , Blood Group-Dominant trait: "+buffer[i+1][3])
        dom[i] = dom[i]+1
        dom[i+1] = dom[i+1]+1
    elif (buffer[i][3] == 'B' and buffer[i+1][3] == 'B'):
        print("Both Dominant"+" , Blood Group-Dominant trait: "+buffer[i+1][3])
        dom[i] = dom[i]+1
        dom[i+1] = dom[i+1]+1

    print("")

print("Most dominant people in the sample of 10 couples: ")
for i in range(0, 20):
    if dom[i] == 3:
        print(buffer[i][0])