# Example: Simple Neural Network
#Name: Aayush Prasad @aprasad
import torch
import torch.nn as nn

# Define a simple neural network
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

# Initialize the network and input data
net = SimpleNet()
input_data = torch.randn(5, 10)

# Forward pass
output = net(input_data)
print(output)

"""
Sample Output:
tensor([[ 0.1234],
        [-0.2345],
        [ 0.6789],
        [ 0.4567],
        [-0.9876]], grad_fn=<AddmmBackward>)

"""