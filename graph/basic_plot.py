import matplotlib
import matplotlib.pyplot as plt

# create the figure
fig = plt.figure()

# add a subplot to the figure (the explicit way)
# Passing the numbers is optional and you can pass 111 but I will stick with this way. 
# That's why I call it explicit way.
# 1, 1, 1 means: 1 axes in a 1 row 1 column grid. More on this later.
ax1 = fig.add_subplot(1, 1, 1)

# some data
x = [1, 2, 3, 4, 5]
y = [3, 2, 1, 4, 5]

# plot basic things
ax1.plot(x, y);