import knn
import util

test = knn.KNN()

data = util.openFile("iris.csv")

print(test.knnRun(data, 5))