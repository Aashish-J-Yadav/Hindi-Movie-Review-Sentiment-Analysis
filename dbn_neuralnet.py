from statistics import mean

import pickle
import numpy as np
from sklearn.metrics import f1_score
from sklearn.metrics.classification import accuracy_score
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from keras.models import model_from_json
from dbn_outside.dbn.tensorflow import SupervisedDBNClassification
from UnigramTfifdFeaturesetGeneration import get_features


def test_with_unigram_tfidf():
    train_x, train_y, test_x, test_y = get_features('dbn')
    train_x = np.array(train_x, dtype=np.float32)
    train_y = np.array(train_y, dtype=np.int32)
    test_x = np.array(test_x, dtype=np.float32)
    test_y = np.array(test_y, dtype=np.int32)
    print(test_x.shape)
    classifier = SupervisedDBNClassification(hidden_layers_structure=[256, 256, 256],learning_rate_rbm=0.05,learning_rate=0.1,n_epochs_rbm=10,n_iter_backprop=100,batch_size=32,activation_function='relu',dropout_p=0.2)
    classifier.fit(train_x, train_y)
    accuracies = []
    f_measures = []
    for i in range(1):
        y_pred = classifier.predict(test_x)
        accuracy = accuracy_score(test_y, y_pred)
        f_measure = f1_score(test_y, y_pred)
        accuracies.append(accuracy)
        f_measures.append(f_measure)
        
    classifier.save('SentimentClassification.pkl')
        
    print(accuracies)
    print('Accuracy ', mean(accuracies))
    print('F-measure', mean(f_measures))
    return

test_with_unigram_tfidf()
    

