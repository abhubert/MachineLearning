import knn
import util

test = knn.KNN()

data = util.openFile("data/iris.csv")

print(test.knnRun(data, 5))