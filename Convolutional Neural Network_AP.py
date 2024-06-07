# Example: Convolutional Neural Network
#Name: Aayush Prasad @aprasad
import torch
import torch.nn as nn

# Define a simple CNN architecture
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.fc = nn.Linear(32 * 7 * 7, 10)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1, 32 * 7 * 7)
        x = self.fc(x)
        return x

# Initialize the network and input data
net = CNN()
input_data = torch.randn(1, 1, 28, 28)

# Forward pass
output = net(input_data)
print(output)

"""
Sample Output:
tensor([[ 0.0528, -0.0183, -0.0569,  0.0476, -0.0539, -0.0832,  0.0273, -0.0122,
          0.0587,  0.0321]], grad_fn=<AddmmBackward>)
"""