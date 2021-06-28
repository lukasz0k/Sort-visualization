import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("times.txt", delimiter=" ")
bubble = data[:,0]
insert = data[:,1]
merge = data[:,2]
selection = data[:,3]
quick = data[:,4]
n = data[:,5]

plt.style.use("classic")
plt.figure(figsize=(12,6), facecolor="white")
plt.xlabel("Number of elements", size = "12")
plt.ylabel("Time", size = "12")
plt.plot(n, bubble, 'b^', label = "Bubble sort")
plt.plot(n, insert, 'r^', label = "Insert sort")
plt.plot(n, merge, 'k^', label = "Merge sort")
plt.plot(n, selection, 'g^', label = "Selection sort")
plt.plot(n, quick, 'm^', label = "Quick sort")
plt.legend(["Bubble sort", "Insert sort", "Merge sort", "Selection sort", "Quick sort"],
           loc ='upper left', numpoints = 1, ncol = 2, frameon = "False")
plt.axis([0, 750, 0, 25000])
plt.savefig("Sort_time.png", dpi = 400)
plt.grid(True)
plt.show()

plt.style.use("classic")
plt.figure(figsize=(12,6), facecolor="white")
plt.xlabel("Number of elements", size = "12")
plt.ylabel("Time", size = "12")
plt.plot(n, bubble, 'b-', label = "Bubble sort")
plt.plot(n, insert, 'r-', label = "Insert sort")
plt.plot(n, merge, 'k-', label = "Merge sort")
plt.plot(n, selection, 'g-', label = "Selection sort")
plt.plot(n, quick, 'm-', label = "Quick sort")
plt.legend(["Bubble sort", "Insert sort", "Merge sort", "Selection sort", "Quick sort"],
           loc ='upper left', numpoints = 1, ncol = 2, frameon = "False")
# plt.axis([0, 750, 0, 12500])
plt.savefig("Sort_time_curves.png", dpi = 400)
plt.grid(True)
plt.show()