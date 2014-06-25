from lib.naive_bayes import NaiveBayes
from lib.svm import SVM

word_list = "all" # all, frequency, tfidf or most_informative

classifiers = [
    NaiveBayes(selected = word_list),
    SVM.Proba(selected = word_list),
    SVM.Linear(selected = word_list),
    SVM.Polynomial(selected = word_list),
]

for classifier in classifiers:

    classifier.get_featuresets()
    classifier.train_and_test(5)
    # classifier.show_most_informative_features(10)

    print "%.2f (accuracy)" % (classifier.accuracy)

    document1 = ['a', ',wickedly', 'entertaining', 'sometimes', 'thrilling', 'adventure']
    print "Classification: A wickedly entertaining, sometimes thrilling adventure."
    print classifier.classify(classifier.sentiment_features(document1, classifier.words))

    document2 = ['providing', 'a', 'riot', 'of', 'action', 'big', 'and', 'visually', 'opulent', 'but', 'oddly', 'lumbering', 'and', 'dull']
    print "Classification: Providing a riot of action, big and visually opulent but oddly lumbering and dull."
    print classifier.classify(classifier.sentiment_features(document2, classifier.words))

    print "tp = %d, tn = %d, fp = %d, fn = %d" % classifier.confusion_matrix()