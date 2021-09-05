import time
import math 
import csv
import tempfile

def FizzBuzz():
    start_time = time.time()
    for i in range(1, 101):
        if i % 3 == 0 and  i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    end_time = time.time()
    print("Execution time of FizzBuzz:", (end_time - start_time),"seconds" )

def SphereVolume(rad):
    vol = (4/3)*math.pi*rad*rad*rad
    return vol

def DictToCSV(data):
    rows = zip(*data.values())
    filename = 'books.csv'
    with open(filename, 'w',newline='') as f:  # You will need 'wb' mode in Python 2.x
        writer = csv.writer(f, delimiter=',')
        writer.writerow(data.keys())
        writer.writerows(rows)
    print("Successfully Updated the File.")
    return filename

def CSVToDict(filename):
    dictionary = {}
    with open(filename, 'r', newline='') as f:
        col_list = f.readline().strip().split(",")
        for col in col_list:
            dictionary[col] = []
        f.seek(0)
        for line in csv.DictReader(f):
            for col in col_list:
                dictionary[col].append(line[col])
    print("Successfully Loaded the File.")
    
    return dictionary


def DictCSVDict(data):
    filename = tempfile.NamedTemporaryFile(delete=False)
    rows = zip(*data.values())
    dictionary = {}
    with open(filename.name, 'w', newline='') as fake:
        fake_writer = csv.writer(fake, delimiter=',')
        fake_writer.writerow(data.keys())
        fake_writer.writerows(rows)
    print("Successfully Updated the Temporary File.")
    with open(filename.name, 'r', newline='') as f:
        col_list = f.readline().strip().split(",")
        for col in col_list:
            dictionary[col] = []
        f.seek(0)
        for line in csv.DictReader(f):
            for col in col_list:
                dictionary[col].append(line[col])

    print("Successfully Loaded the Temporary File.")
    filename.close()
    print("Successfully Deleted the Temporary File.")
    return dictionary
        



# CALLING METHOD FOR QUESTION 1, IT RETURNS THE NUMBERS (1-100) AND EXECUTION TIME AS PER LOGIC
FizzBuzz()

# CALLING METHOD FOR QUESTION 2, IT RETURNS THE VOLUME OF SPHERE WITH PASSED RADIUS
print(SphereVolume(20))

# DATA DICTIONARY AS DEFINED IN QUESTION 3
DATA_DICT = {"Title" : ["1984", "Animal Farm", "Brave New World", "Fahrenheit 451", "Jane Eyre", "Wuthering Heights", "Agnes Grey", "Walden", "Walden Two" ,"``Eats, Shoots & Leaves"],
            "Author" : ["George Orwell", "George Orwell", "Aldous Huxley", "Ray Bradbury", "Charlotte Bronte", "Emily Bronte", "Anne Bronte", "Henry David Thoreau", "B. F. Skinner", "Lynne Truss"], 
            "ISBN13" : ["978-0451524935", "978-0451526342", "978-0060929879", "978-0345342966", "978-0142437209", "978-0141439556", "978-1593083236", "978-1420922615", "978-0872207783", "978-1592400874"], 
            "Pages" : [268, 144, 288, 208, 532, 416, 256, 156, 301, 209]
            }

# CALLING METHOD FOR QUESTION 3, IT RETURNS THE NAME OF CSV FILE IN WHICH DICTIONARY DATA IS WRITTEN 
fName = DictToCSV(DATA_DICT)

# CALLING METHOD FOR QUESTION 4, IT RETURNS THE DICTIONARY DATA WHICH IS READ FROM FILE WE GOT IN Q3 
dictNew = CSVToDict(fName)
print("Dictionary After Reading Csv File\n",dictNew)

# CALLING METHOD FOR QUESTION 5, IT COMBINES 3 AND 4 AND RETURNS THE DICTIONARY DATA WHICH IS STORED AND READ IN TEMPORRAY FILE 
dictNew = DictCSVDict(DATA_DICT)
print("Dictionary After Reading And Writing Temporary Csv File\n",dictNew)
