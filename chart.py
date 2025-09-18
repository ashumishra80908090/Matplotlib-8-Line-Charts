import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(16,8))
plt.suptitle("My 8 Line Chart ",size=20,color="red")
# plot 1
x=np.array([1,2,3,4,5])
y=np.array([2,5,3,6,3])
plt.subplot(2,4,1)
plt.grid(color="green",linestyle="--",linewidth=0.5)
plt.title("Plot 1")
plt.xlabel("x axis",family="monospace")
plt.ylabel("y axis",family="cursive")
plt.plot(x,y,color=("blue"))

# plot 2
x=np.array([1,2,3,4,5])
y=np.array([1,3,2,5,2])
plt.subplot(2,4,2)
plt.grid(color="green",linestyle="--",linewidth=0.5)
plt.title("Plot 2")
plt.xlabel("x axis",family="monospace")
plt.ylabel("y axis",family="cursive")
plt.plot(x,y,color="orange")

# plot 3
x=np.array([1,2,3,4,5])
y=np.array([2,5,3,6,4])
plt.subplot(2,4,3)
plt.grid(color="green",linestyle="--",linewidth=0.5)
plt.title("Plot 3")
plt.xlabel("x axis",family="monospace")
plt.ylabel("y axis",family="cursive")
plt.plot(x,y,color=("violet"))

# plot 4
x=np.array([1,2,3,4,5])
y=np.array([1,3,5,3,2])
plt.subplot(2,4,4)
plt.grid(color="green",linestyle="--",linewidth=0.5)
plt.title("Plot 4")
plt.xlabel("x axis",family="monospace")
plt.ylabel("y axis",family="cursive")
plt.plot(x,y,color="lightgray")

# plot 5
x=np.array([1,2,3,4,5])
y=np.array([2,4,1,3,5])
plt.subplot(2,4,5)
plt.grid(color="green",linestyle="--",linewidth=0.5)
plt.title("Plot 5")
plt.xlabel("x axis",family="monospace")
plt.ylabel("y axis",family="cursive")
plt.plot(x,y,color="mediumseagreen")

#plot 6
x=np.array([1,2,3,4,5])
y=np.array([2,4,3,5,2])
plt.subplot(2,4,6)
plt.grid(color="green",linestyle="--",linewidth=0.5)
plt.title("Plot 6")
plt.xlabel("x axis",family="monospace")
plt.ylabel("y axis",family="cursive")
plt.plot(x,y,color="hotpink")

# plot 7
x=np.array([1,2,3,4,5])
y=np.array([1,3,5,3,6])
plt.subplot(2,4,7)
plt.grid(color="green",linestyle="--",linewidth=0.5)
plt.title("Plot 7")
plt.xlabel("x axis",family="monospace")
plt.ylabel("y axis",family="cursive")
plt.plot(x,y,color="tomato")

# plot 8
x=np.array([1,2,3,4,5])
y=np.array([1,3,2,5,3])
plt.subplot(2,4,8)
plt.grid(color="green",linestyle="--",linewidth=0.5)
plt.title("Plot 5")
plt.xlabel("x axis",family="monospace")
plt.ylabel("y axis",family="cursive")
plt.plot(x,y,color="grey")

plt.tight_layout()
plt.show()



































