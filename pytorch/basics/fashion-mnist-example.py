input('building dataset')
from torchvision import datasets
from torchvision.transforms import ToTensor
training_dataset = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
)
print(len(training_dataset[0]))
print(training_dataset[0][0].shape)
print(type(training_dataset[0][1]), training_dataset[0][1])


input('building dataloader')
from torch.utils.data import DataLoader
train_dataloader = DataLoader(training_dataset, batch_size=4)
for x, y in train_dataloader:
    print(x.shape)
    print(y)
    break


input('building model')
from torch import nn
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.model = nn.Sequential(nn.Flatten(), nn.Linear(28*28, 10))
    
    def forward(self, x):
        return self.model(x)
model = MyModel()
print(model)


input('building loss_fn and optimizer')
from torch.optim import SGD
optimizer = SGD(model.parameters(), lr=1e-2)
loss_fn = nn.CrossEntropyLoss()


input('training')
for epoch in range(10):
    input(f'epoch {epoch}')
    for batch, (x, y) in enumerate(train_dataloader):
        input(f'batch {batch}')
        loss = loss_fn(model(x), y)
        print(loss.item())
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    