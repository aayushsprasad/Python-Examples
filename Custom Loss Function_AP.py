# Example: Custom Loss Function
#Name: Aayush Prasad @aprasad
import torch
import torch.nn as nn

# Define a custom loss function
class CustomLoss(nn.Module):
    def __init__(self):
        super(CustomLoss, self).__init__()

    def forward(self, output, target):
        loss = torch.mean((output - target) ** 2)
        return loss

# Instantiate the loss function
criterion = CustomLoss()

# Example usage
output = torch.randn(10, 1)
target = torch.randn(10, 1)
loss = criterion(output, target)
print(loss)

"""
Sample Output:
tensor(1.5542)
"""