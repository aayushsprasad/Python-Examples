# Example: Transfer Learning with Pretrained Model
#Name: Aayush Prasad @aprasad
import torch
import torchvision.models as models

# Load a pretrained ResNet18 model
resnet = models.resnet18(pretrained=True)

# Freeze all the parameters in the network
for param in resnet.parameters():
    param.requires_grad = False

# Replace the final fully connected layer with a new one (unfrozen by default)
resnet.fc = torch.nn.Linear(resnet.fc.in_features, 100)

# Example of inference
input_data = torch.randn(1, 3, 224, 224)
output = resnet(input_data)
print(output)

"""
Sample Output:
tensor([[ 0.3708, -0.2665, -0.0428,  0.5725, -0.1019, -0.1342, -0.4416, -0.6839,
          0.0150,  0.7170, -0.5022,  0.3325,  0.1649, -0.3190, -0.0150,  0.3078,
          0.5499, -0.4813, -0.0886, -0.3618, -0.6229,  0.6182,  0.3701, -0.7105,
         -0.4854, -0.2495, -0.5060, -0.7618,  0.4791, -0.8382, -0.1356, -0.6293,
         -0.4111,  0.0769,  0.5898, -0.1703, -0.8343, -1.0126,  0.1383,  0.3969,
          0.6150,  0.1087, -0.1352, -0.0269,  0.1646, -0.2985,  0.4232,  0.5594,
          0.3427,  0.2326,  0.2516, -0.0999,  0.3170,  0.6195,  0.3291,  0.5483,
         -0.4133, -0.4814,  0.8713, -0.4933,  0.1974, -0.4852,  1.0118,  0.2551,
          0.0442, -0.0964, -0.3949,  0.9645, -0.5567, -0.3698,  0.5576,  0.1768,
          0.7480,  0.1771,  0.0128, -0.8777,  0.3870,  0.9168, -0.2860,  0.6023,
         -0.3770,  0.3647,  0.6455, -0.4205, -0.0421, -0.1087, -0.0591,  0.0100,
          0.6839, -0.3528,  0.4678, -0.8669, -0.3921, -0.7830,  0.1640, -0.6142,
          0.7802,  0.2669, -0.1434,  0.9240]], grad_fn=<AddmmBackward0>)

"""
