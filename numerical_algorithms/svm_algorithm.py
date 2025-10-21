import numpy as np

class LinearSVM:
    def __init__(self, learning_rate=0.01, penalty=1.0, epochs=20, random_state=42):
        self.learning_rate = learning_rate
        self.penalty = penalty
        self.epochs = epochs
        self.random_number_gen = np.random.default_rng(random_state)
        self.weight = 0

    def fit(self, X, y):
        X = np.c_[X, np.ones(len(X))]
        samples, feature = X.shape
        self.weight = np.zeros(feature)

        for epoch in range(self.epochs):
            index = self.random_number_gen.permutation(samples)
            for i in index:
                xi, yi = X[i], y[i]
                margin = yi * (self.weight @ xi)
                if margin < 1:
                    self.weight = self.weight - self.learning_rate * (self.weight - self.penalty * yi * xi)
                else:
                    self.weight = self.weight - self.learning_rate * self.weight
        return self

    def decision_function(self, X):
        X = np.c_[X, np.ones(len(X))]
        return X @ self.weight

    def predict(self, X):
        return np.where(self.decision_function(X) >= 0, 1, -1)
