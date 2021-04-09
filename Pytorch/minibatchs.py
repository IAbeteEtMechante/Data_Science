#see https://stackoverflow.com/questions/45113245/how-to-get-mini-batches-in-pytorch-in-a-clean-and-efficient-way

n_epochs = 100 # or whatever
batch_size = 128 # or whatever

for epoch in range(n_epochs):

    # X is a torch Variable
    permutation = torch.randperm(X.size()[0])

    for i in range(0,X.size()[0], batch_size):
        optimizer.zero_grad()

        indices = permutation[i:i+batch_size]
        batch_x, batch_y = X[indices], Y[indices]

        # in case you wanted a semi-full example
        outputs = model.forward(batch_x)
        loss = lossfunction(outputs,batch_y)

        loss.backward()
        optimizer.step()