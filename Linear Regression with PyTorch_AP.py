# Example: Linear Regression with PyTorch
#Name: Aayush Prasad @aprasad
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# Generate some linearly related data
X = torch.randn(100, 1) * 10
y = X + 3 * torch.randn(100, 1)


# Define a simple linear regression model
class LinearRegression(nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


# Instantiate the model, loss function, and optimizer
model = LinearRegression()
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Train the model
for epoch in range(100):
    # Forward pass
    outputs = model(X)
    loss = criterion(outputs, y)

    # Backward and optimize
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Plot the results
plt.scatter(X.numpy(), y.numpy())
plt.plot(X.numpy(), model(X).detach().numpy(), 'r')
plt.show()
