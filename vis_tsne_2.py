__author__ = 'lizuyao'
# print(__doc__)
import pickle
import sys
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datasets
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
# from unbalanced_dataset import UnderSampler

# import some data to play with
fileName = sys.argv[1]
X, Y = datasets.load_data(fileName)
ini_dim = 25
model = TSNE(n_components=2, random_state=0)
X_reduced = model.fit_transform(PCA(n_components=ini_dim).fit_transform(X))

pickle.dump(X_reduced, open(sys.argv[2], "wb"))
'''
# Generate the new dataset using under-sampling method
verbose = False
# 'Random under-sampling'
# ratio of majority elements to sample with respect to the number of minority cases.
US = UnderSampler(ratio=1.,verbose=verbose)
X_reduced, Y = US.fit_transform(X_reduced, Y)


# To getter a better understanding of interaction of the dimensions
# plot the first two tsne dimensions
x_min, x_max = X_reduced[:, 0].min() - .5, X_reduced[:, 0].max() + .5
y_min, y_max = X_reduced[:, 1].min() - .5, X_reduced[:, 1].max() + .5
plt.figure(2, figsize=(8, 6))
plt.clf()
# Plot the training points
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=Y, cmap=plt.cm.Paired)
plt.xlabel('1st eigenvector')
plt.ylabel('2nd eigenvector')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

outFile=sys.argv[2]#"pic/tsne_2_t"
plt.savefig(outFile)
# plt.show()
'''
