#from asyncore import file_dispatcher
import os
from unittest import result
import numpy as np
from collections import Counter
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.svm import SVC, NuSVC, LinearSVC

#reading dataset and makes a dict
def make_dictionary(train_dir):
    emails = [os.path.join(train_dir,f ) for f in os.listdir(train_dir)]
    all_words = []
    for mail in emails:
        with open(mail) as m:
            #print(m)
            for i, line in enumerate(m):
                if i == 2:
                    words = line.split()
                    all_words += words
                
        
    dictionary = Counter(all_words)
    list_to_remove = dictionary.keys()
    keys_to_remove = []
    for k in list_to_remove:
        if not k.isalpha():
            keys_to_remove.append(k)
        elif len(k) == 1:
            keys_to_remove.append(k)

    for item in keys_to_remove:
        del dictionary[item]
    
    dictionary = dictionary.most_common(3000)
    #dict containing the 3k most common works in dataset

    return dictionary

#make_dictionary("C:/PROJECTS___/python/ml_proj1/train-mail")


#print(make_dictionary("C:/PROJECTS___/python/ml_proj1/train-mail"))

#extracting features of training data
def extract_fearures(mail_dir):
    files = [os.path.join(mail_dir, file_descriptor) for file_descriptor in os.listdir(mail_dir)]
    #create matrix with zeroes
    features_mat = np.zeros((len(files), 3000))
    doc_id = 0
    for file_to_read in files:
        with open(file_to_read) as file_descriptor:
            for i, line in enumerate(file_descriptor):
                if i == 2:
                    words = line.split()
                    for word in words:
                        word_id = 0
                        for i, d in enumerate(dictionary):
                            if d[0] == word:
                                word_id = i
                                features_mat[doc_id, word_id] = words.count(word)
            doc_id = doc_id + 1
    return features_mat



train_dir = "train-mail"

dictionary = make_dictionary(train_dir)
print("extracting features")
train_labels = np.zeros(702)
train_labels[351:701] = 1
train_matrix = extract_fearures(train_dir)


print("train our stsyem with svm and naive bays")

multinomial_model = MultinomialNB()
svc_model = LinearSVC()
multinomial_model.fit(train_matrix, train_labels)
svc_model.fit(train_matrix, train_labels)
#test mails
test_dir = "test-mail"
test_matrix = extract_fearures(test_dir)
test_labels = np.zeros(260)
test_labels[130:259] = 1

result1 = multinomial_model.predict(test_matrix)
result2 = svc_model.predict(test_matrix)


print(result1)
print(result2)



