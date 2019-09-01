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
KNN_NEIGHBOR = 3

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
    a = vec[128:160]
    b = vec[256:288]
    c = vec[384:416]
    d = vec[512:544]
    i = vec[672:704]
    j = vec[800:832]
    k = vec[928:960]
    e = [0]
    f = [0]
    g = [0]
    h = [0]
    l = [0]
    m = [0]
    n = [0]
    for i1 in range(3,996,32):
        e.append(vec[i1])
    for i2 in range(7,1000,32):
        f.append(vec[i2])
    for i3 in range(11,1004,32):
        g.append(vec[i3])
    for i4 in range(15,1008,32):
        h.append(vec[i4])
    for i5 in range(20,1013,32):
        l.append(vec[i5])
    for i6 in range(24,1017,32):
        m.append(vec[i6])
    for i7 in range(28,1021,32):
        n.append(vec[i7])
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_i = 0
    count_j = 0
    count_k = 0
    count_e = 0
    count_f = 0
    count_g = 0
    count_h = 0
    count_l = 0
    count_m = 0
    count_n = 0
    for j1 in range(31):
        if a[j1] == 0 and a[j1+1] == 1:
            count_a += 1
        if b[j1] == 0 and b[j1+1] == 1:
            count_b += 1
        if c[j1] == 0 and c[j1+1] == 1:
            count_c += 1
        if d[j1] == 0 and d[j1+1] == 1:
            count_d += 1
        if i[j1] == 0 and i[j1+1] == 1:
            count_i += 1
        if j[j1] == 0 and j[j1+1] == 1:
            count_j += 1
        if k[j1] == 0 and k[j1+1] == 1:
            count_k += 1
    for j2 in range(32):
        if e[j2] == 0 and e[j2+1] == 1:
            count_e += 1
        if f[j2] == 0 and f[j2+1] == 1:
            count_f += 1
        if g[j2] == 0 and g[j2+1] == 1:
            count_g += 1
        if h[j2] == 0 and h[j2+1] == 1:
            count_h += 1
        if l[j2] == 0 and l[j2+1] == 1:
            count_l += 1
        if m[j2] == 0 and m[j2+1] == 1:
            count_m += 1
        if n[j2] == 0 and n[j2+1] == 1:
            count_n += 1
    new_vec = [count_a,count_b,count_c,count_d,
                count_i,count_j,count_k,
                count_e,count_f,count_g,count_h,
                count_l,count_m,count_n]
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
    dist = 15
    for i in range(14):
        if v[i] == w[i]:
            dist -= 1
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
    for d in range(10):
        good = g_test_good[d]
        bad = g_test_bad[d]
        print(d, '=', good, bad, good/(good+bad))
    print('End of Validation @ ', stop)  

if __name__ == '__main__':
    load_data()
    show_info()
    validate()
    predict()