# Group:IT-2003 Team: Assel Shora, Makhambet Kuatov, Tleuzhanov Syrym
import numpy as np
import random

def create_dataset(num):
    data = []
    for i in range(0, num):  #we filling our dataset with random nums and vals
        row = [i , 2 * i, np.random.normal(0, 0.1),
               4 * i , np.random.random_sample() * 20000 - 10000, 8 * i]
        data.append(row)
    random.shuffle(data)  #after finishing our data creation we shuffle our data that we get
    return data

def save_result(data):
    somestr = ""
    for data1 in data:
        somestr += str(data1) + "\n"

    with open("result.txt", "w+") as file:
        file.write(somestr)


if __name__ == '__main__':
    data = create_dataset(1500)   #calling function to create dataset with 1500 entries
    for data2 in data:
        print(data2)
    save_result(data)   #call save function to write our result to txt file
