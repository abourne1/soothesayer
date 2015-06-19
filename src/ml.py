from sklearn.ensemble import RandomForestClassifier
import numpy as np

stopwords = [line.strip() for line in open('../data/stopwords.txt')]

def train(model, body, tag):
    labels, texts = unzip(read_texts())
    rf = RandomForestClassifier(n_estimators=80)
    rf.fit(texts, labels)
    return rf

def filter(text):
    words = text.split(' ')
    no_stops = [no_plural(word) for word in words if word not in stopwords]

def read_texts():
    return [(line[0], line[1:].strip()) for line in open('../data/data.txt')]

def unzip(iterable):
    return zip(*iterable)

def no_plural(word):
    if word[-1] == 's':
        return word[:-1]
    else:
        return word

def main():
    #create the training & test sets, skipping the header row with [1:]
    dataset = genfromtxt(open('Data/train.csv','r'), delimiter=',', dtype='f8')[1:]    
    target = [x[0] for x in dataset]
    train = [x[1:] for x in dataset]
    test = genfromtxt(open('Data/test.csv','r'), delimiter=',', dtype='f8')[1:]
    
    #create and train the random forest
    #multi-core CPUs can use: rf = RandomForestClassifier(n_estimators=100, n_jobs=2)
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(train, target)

    savetxt('Data/submission2.csv', rf.predict(test), delimiter=',', fmt='%f')
