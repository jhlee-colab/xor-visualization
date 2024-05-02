import torch
from torch import nn
from torch import optim as optim
from torch.nn import init

class XOR(nn.Module):
    def __init__(self,
                 hidden_layers:list,
                 activation_fn='Sigmoid',
                 optimizer_fn='Adam',
                 learning_rate=0.001,
                 loss='MSELoss',
                 epochs=10,
                 device='cpu'
                ):
        super().__init__()
        self.model = nn.Sequential()

        activation_fn = getattr(nn, activation_fn)
        self.optimizer = optimizer_fn
        self.loss = loss
        self.lr = learning_rate
        self.epochs = epochs

        # hidden layers
        for idx in range(len(hidden_layers)):
            if idx == 0:
                layer = nn.Linear(2, hidden_layers[idx])
            else:
                layer = nn.Linear(hidden_layers[idx-1], hidden_layers[idx])
            init.uniform_(layer.weight)
           # init.uniform_(layer.bias)
            self.model.append(layer)
            self.model.append(activation_fn())

        # output layer
        layer = nn.Linear(hidden_layers[-1], 1)
        init.uniform_(layer.weight)
        init.uniform_(layer.bias)
        self.model.append(layer)
        self.model.append(nn.Sigmoid())
        self.model.to(device)

    def forward(self, x):
        return self.model(x)

    def fit(self, X, y, print_every=100):
        loss_fn = getattr(nn, self.loss)()
        optimizer = getattr(optim, self.optimizer)(self.model.parameters(), lr=self.lr)

        for epoch in range(1, self.epochs+1):
            # initiate optimizer
            optimizer.zero_grad()

            # forward
            hypothesis = self.model(X)

            # check loss(or cost)
            cost = loss_fn(hypothesis, y)

            # backward and update
            cost.backward()
            optimizer.step()

            if epoch % print_every == 0:
                print(f'Epoch: {epoch}, cost: {cost.item()}')

    def predict(self, X):
        return torch.where(self.model(X)>0.5, 1, 0)


if __name__ == '__main__':
    xor_model = XOR([2], epochs=15000)
    print(xor_model.model)
    device = "cuda:0" if torch.cuda.is_available() else 'cpu'

    X = torch.tensor([[0,0],[0,1],[1,0],[1,1]], dtype=torch.float).to(device)
    y = torch.tensor([[0],[1],[1],[0]], dtype=torch.float).to(device)

    xor_model.fit(X, y, print_every=1000)
    print(xor_model(X))
    print(torch.where(xor_model(X) > 0.5, 1, 0))
