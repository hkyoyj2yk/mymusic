# Creating a PyTorch class
import torch

class AE2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        # Building an linear encoder with Linear
        # layer followed by Relu activation function
        self.encoder = torch.nn.Sequential(
            torch.nn.Linear(1536, 800),
            torch.nn.ReLU(),
            torch.nn.Linear(800, 400),
            torch.nn.ReLU(),
            torch.nn.Linear(400, 20),
            torch.nn.ReLU()
        )

        # Building an linear decoder with Linear
        # layer followed by Relu activation function
        self.decoder = torch.nn.Sequential(
            torch.nn.Linear(20, 400),
            torch.nn.ReLU(),
            torch.nn.Linear(400, 800),
            torch.nn.ReLU(),
            torch.nn.Linear(800, 1536),
            torch.nn.ReLU()
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

