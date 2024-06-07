# Example: Generative Adversarial Networks
#Name: Aayush Prasad @aprasad
import torch
import torch.nn as nn

# Define a simple generator and discriminator
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.fc = nn.Linear(100, 784)

    def forward(self, x):
        return torch.sigmoid(self.fc(x))

class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.fc = nn.Linear(784, 1)

    def forward(self, x):
        return torch.sigmoid(self.fc(x))

# Instantiate generator, discriminator, and input noise
generator = Generator()
discriminator = Discriminator()
noise = torch.randn(10, 100)

# Generate fake images
fake_images = generator(noise)
print(fake_images)
