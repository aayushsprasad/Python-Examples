# Example: Recurrent Neural Network
#Name: Aayush Prasad @aprasad
import torch
import torch.nn as nn

# Define a simple RNN
class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(input_size + hidden_size, output_size)

    def forward(self, input, hidden):
        combined = torch.cat((input, hidden), 1)
        hidden = torch.tanh(self.i2h(combined))
        output = self.i2o(combined)
        return output, hidden

# Instantiate the RNN and input data
rnn = RNN(10, 20, 1)
input_data = torch.randn(5, 10)
hidden = torch.zeros(5, 20)

# Forward pass
output, next_hidden = rnn(input_data, hidden)
print(output)

"""
Sample Output:
tensor([[ 0.0206],
        [ 0.0343],
        [-0.0672],
        [-0.0234],
        [-0.0456]], grad_fn=<AddmmBackward>)

"""
