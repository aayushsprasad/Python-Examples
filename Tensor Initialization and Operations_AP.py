# Example: Tensor Initialization and Operations
#Name: Aayush Prasad @aprasad
import torch

# Initialize tensors
x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[5, 6], [7, 8]])

# Perform tensor operations
z = x + y
print(z)

"""
Sample Output
tensor([[ 6,  8],
        [10, 12]])

"""