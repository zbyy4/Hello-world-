import random
from collections import defaultdict, Counter
from datetime import datetime
from functools import reduce

g_dataset = {}
g_test_good = {}
g_test_bad = {}
NUM_ROWS = 32
NUM_COLS = 32
DATA_TRAINING = 'digit-training.txt'
DATA_TESTING = 'digit-testing.txt'
DATA_PREDICT = 'digit-predict.txt'

# kNN parameter
KNN_NEIGHBOR = 7

##########################
##### Load Data  #########
##########################

# Convert next digit from input file as a vector 
# Return (digit, vector) or (-1, '') on end of file
def read_digit(p_fp):
    # read entire digit (inlude linefeeds)
    bits = p_fp.read(NUM_ROWS * (NUM_COLS + 1))
    if bits == '':
        return -1,bits
    # convert bit string as digit vector
    vec = [int(b) for b in bits if b != '\n']
    val = int(p_fp.readline())
    new_vec = []
    for i in range(0,993,128):
        a = vec[i:i+32]
        count = 0
        count_one = 0
        for j in range(31):
            if a[j] == 1:
                count_one += 1
            elif a[j+1] == 1:
                count += 3
        new_vec.append(count)
        new_vec.append(count_one)
    
    for i in range(0,32,4):
        a = [0]
        count = 0
        count_one = 0
        for j in range(i,i+993,32):
            a.append(vec[j])
        for k in range(32):
            if a[k] == 1:
                count_one += 1
            elif a[k+1] == 1:
                count += 3
        new_vec.append(count)
        new_vec.append(count_one)

    return val,new_vec

# Parse all digits from training file
# and store all digits (as vectors) 
# in dictionary g_dataset
def load_data(p_filename=DATA_TRAINING):
    global g_dataset
    # Initial each key as empty list 
    g_dataset = defaultdict(list)
    with open(p_filename) as f:
        while True:
            val,vec = read_digit(f)
            if val == -1:
                break
            g_dataset[val].append(vec)

##########################
##### kNN Models #########
##########################

# Given a digit vector, returns
# the k nearest neighbor by vector distance
def knn(p_v, size=KNN_NEIGHBOR):
    nn = []
    for d,vectors in g_dataset.items():
        for v in vectors:
            dist = distance(p_v,v)
            nn.append((dist,d))
    nn.sort()
    # TODO: find the nearest neigbhors
    return nn[:size]

# Based on the knn Model (nearest neighhor),
# return the target value
def knn_by_most_common(p_v):
    nn = knn(p_v)
    temp = []
    for i in nn:
        temp.append(i[1])
    cou_dict = Counter(temp)
    # TODO: target value
    return cou_dict.most_common(1)[0][0]

##########################
##### Prediction  ########
##########################

# Make prediction based on kNN model
# Parse each digit from the predict file
# and print the predicted value
def predict(p_filename=DATA_PREDICT):
    with open(p_filename) as f:
        while True:
            val,vec = read_digit(f)
            if val == -1:
                break
            if knn_by_most_common(vec) == val:
                g_test_good[val] += 1
            else:
                g_test_bad[val] += 1

    # TODO
    print('TO DO: show results of prediction')

##########################
##### Accuracy   #########
##########################

# Compile an accuracy report by
# comparing the data set with every
# digit from the testing file 
def validate(p_filename=DATA_TESTING):
    global g_test_bad, g_test_good
    g_test_bad = defaultdict(int)
    g_test_good = defaultdict(int)
        
    start=datetime.now()
    
    predict(DATA_TESTING)
    # TODO: Validate your kNN model with 
    # digits from test file.
    
    stop=datetime.now()
    show_test(start, stop)

##########################
##### Data Models ########
##########################

# Randomly select X samples for each digit
def data_by_random(size=25):
    for digit in g_dataset.keys():
        g_dataset[digit] = random.sample(g_dataset[digit],size)

##########################
##### Vector     #########
##########################

# Return distance between vectors v & w
def distance(v, w):
    dist = 0
    for i in range(32):
        if v[i] != w[i]:
            dist += abs(v[i]-w[i])
    return dist 

##########################
##### Report     #########
##########################

# Show info for training data set
def show_info():
    print('TODO: Training Info')
    for d in range(10):
        print(d, '=', len(g_dataset[d]))

# Show test results
def show_test(start="????", stop="????"):
    print('Beginning of Validation @ ', start)    
    print('TODO: Testing Info')
    add = 0
    for d in range(10):
        good = g_test_good[d]
        bad = g_test_bad[d]
        add += good/(good+bad)
        print(d, '=', good, bad, good/(good+bad))
    print(add)
    print('End of Validation @ ', stop)  

if __name__ == '__main__':
    load_data()
    show_info()
    validate()
    predict()