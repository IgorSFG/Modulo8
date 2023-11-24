#! /bin/env python3
import numpy as np

class Logictron:
    def __init__(self, learning_rate=0.1, n_iterations=100, threshold=0.5):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.threshold = threshold
        self.weights = np.zeros(2)
        self.bias = 0

    def predict(self, inputs):
        # Calcula a soma ponderada das entradas
        linear_output = np.dot(inputs, self.weights) + self.bias
        # Aplica a função degrau para determinar a saída
        y_predicted = 1 if linear_output >= self.threshold else 0
        
        return y_predicted

    def train(self, X, y):
        for _ in range(self.n_iterations):
            for x, y_true in zip(X, y):
                y_pred = self.predict(x)
                error = y_true - y_pred
                self.weights += error * self.learning_rate * x
                self.bias += error * self.learning_rate

def main():
    # Dados para a porta AND
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    yand = np.array([0, 0, 0, 1]) 
    yor = np.array([0, 1, 1, 1])  
    ynand = np.array([1, 1, 1, 0])
    yxor = np.array([0, 1, 1, 0])

    models = {
        "AND": yand,
        "OR": yor,
        "NAND": ynand,
        "XOR": yxor
    }

    for model_name, model in models.items():
        
        print(f"Model: {model_name}")
        
        # Treinando o Perceptron
        logictron = Logictron()
        logictron.train(X, model)

        # Testando o Perceptron
        print(f"in (0, 0), out: {logictron.predict([0, 0])}")
        print(f"in (0, 1), out: {logictron.predict([0, 1])}")
        print(f"in (1, 0), out: {logictron.predict([1, 0])}")
        print(f"in (1, 1), out: {logictron.predict([1, 1])}")
        print()
        
        if model_name == "XOR":
            print("ERROR: O perceptron não consegue aprender a porta XOR, pois ela não é linearmente separável.")
            print("Para resolver esse problema, vamos usar 2 perceptrons.")
            print()
            print("Model: XOR (CORRECTED)")
            
            # Treinando os Perceptrons
            logictron1 = Logictron()
            logictron1.train(X, yand)
            logictron2 = Logictron()
            logictron2.train(X, ynand)

            # Testando os Perceptrons
            print(f"in (0, 0), out: {logictron1.predict([logictron2.predict([0, 0]), 0])}")
            print(f"in (0, 1), out: {logictron1.predict([logictron2.predict([0, 1]), 1])}")
            print(f"in (1, 0), out: {logictron1.predict([logictron2.predict([1, 0]), 1])}")
            print(f"in (1, 1), out: {logictron1.predict([logictron2.predict([1, 1]), 0])}")
            print()

if __name__ == "__main__":
    main()