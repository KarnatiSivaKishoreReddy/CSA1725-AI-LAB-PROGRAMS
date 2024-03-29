import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights and biases
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.bias_input_hidden = np.random.randn(1, self.hidden_size)
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)
        self.bias_hidden_output = np.random.randn(1, self.output_size)
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward(self, inputs):
        # Forward pass through the network
        self.hidden_output = self.sigmoid(np.dot(inputs, self.weights_input_hidden) + self.bias_input_hidden)
        self.final_output = self.sigmoid(np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_hidden_output)
        return self.final_output
    
    def backward(self, inputs, target, learning_rate):
        # Backward pass through the network
        error = target - self.final_output
        d_output = error * self.sigmoid_derivative(self.final_output)
        
        error_hidden = d_output.dot(self.weights_hidden_output.T)
        d_hidden = error_hidden * self.sigmoid_derivative(self.hidden_output)
        
        # Update weights and biases
        self.weights_hidden_output += self.hidden_output.T.dot(d_output) * learning_rate
        self.bias_hidden_output += np.sum(d_output, axis=0, keepdims=True) * learning_rate
        self.weights_input_hidden += inputs.T.dot(d_hidden) * learning_rate
        self.bias_input_hidden += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate
        
    def train(self, inputs, targets, epochs, learning_rate):
        for i in range(epochs):
            for j in range(len(inputs)):
                self.forward(inputs[j])
                self.backward(inputs[j], targets[j], learning_rate)
            if i % 100 == 0:
                print("Epoch", i, "Loss:", np.mean(np.square(targets - nn.forward(inputs))))
                
# Example usage:
input_size = 2
hidden_size = 3
output_size = 1

# Define training data
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets = np.array([[0], [1], [1], [0]])

# Initialize neural network
nn = NeuralNetwork(input_size, hidden_size, output_size)

# Train the neural network
nn.train(inputs, targets, epochs=1000, learning_rate=0.1)

# Test the trained neural network
print("Predictions after training:")
for i in range(len(inputs)):
    print("Input:", inputs[i], "Target:", targets[i], "Prediction:", nn.forward(inputs[i]))
