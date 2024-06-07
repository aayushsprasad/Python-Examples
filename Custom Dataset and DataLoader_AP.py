# Example: Custom Dataset and DataLoader
#Name: Aayush Prasad @aprasad
import torch
from torch.utils.data import Dataset, DataLoader

# Define a custom dataset
class CustomDataset(Dataset):
    def __init__(self):
        self.data = torch.randn(100, 10)
        self.targets = torch.randint(0, 2, (100,))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index], self.targets[index]

# Create an instance of the custom dataset and a data loader
dataset = CustomDataset()
dataloader = DataLoader(dataset, batch_size=10, shuffle=True)

# Iterate through the data loader
for inputs, targets in dataloader:
    print(inputs.shape, targets.shape)

"""
Sample Output:
torch.Size([10, 10]) torch.Size([10])
torch.Size([10, 10]) torch.Size([10])
torch.Size([10, 10]) torch.Size([10])
torch.Size([10, 10]) torch.Size([10])
torch.Size([10, 10]) torch.Size([10])
torch.Size([10, 10]) torch.Size([10])
torch.Size([10, 10]) torch.Size([10])
torch.Size([10, 10]) torch.Size([10])
torch.Size([10, 10]) torch.Size([10])
torch.Size([10, 10]) torch.Size([10])
"""