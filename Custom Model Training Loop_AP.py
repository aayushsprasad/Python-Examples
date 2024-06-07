# Example: Custom Model Training Loop
#Name: Aayush Prasad @aprasad
import torch
import torch.nn as nn

# Define a custom model
class CustomModel(nn.Module):
    def __init__(self):
        super(CustomModel, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

# Instantiate the model, loss function, and optimizer
model = CustomModel()
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Sample input data and target
input_data = torch.randn(32, 10)  # Example: 32 samples, each with 10 features
target = torch.randn(32, 1)  # Example: 32 samples, each with a single target value

# Custom training loop
for epoch in range(100):
    optimizer.zero_grad()
    output = model(input_data)
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()

# Example of inference
output = model(input_data)
print(output)


"""
Sample Output:
tensor([[-0.3846],
        [-0.5438],
        [-0.3899],
        [-0.1282],
        [-0.1336],
        [ 0.1963],
        [-0.0402],
        [ 1.4073],
        [ 0.3030],
        [ 0.2243],
        [-0.0687],
        [-0.0162],
        [ 0.6642],
        [ 0.2182],
        [-0.7323],
        [-0.8123],
        [-0.0778],
        [-1.0551],
        [ 0.1957],
        [ 0.3218],
        [ 0.5617],
        [-0.0194],
        [ 0.5399],
        [ 0.3856],
        [ 0.4115],
        [-0.1475],
        [ 0.5619],
        [-0.6259],
        [-0.1277],
        [ 0.3767],
        [ 0.2922],
        [-0.0309]], grad_fn=<AddmmBackward0>)
"""