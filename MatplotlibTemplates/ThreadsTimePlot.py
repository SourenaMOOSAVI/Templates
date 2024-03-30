import matplotlib.pyplot as plt

# Data
threads = [1, 2, 3, 4, 5, 6, 7, 8]
times09 = [1.396523, 0.784477, 0.51273, 0.456432, 0.489673, 0.458656, 0.445911, 0.412783]
#times12 = [14.021028, 7.569913, 5.413407, 5.158831, 6.558166, 5.619782, 5.547496, 5.442378]
# Plot
plt.bar(threads, times09, color='blue', width=0.3)
#plt.bar(threads, times12, color='blue', width=0.3)

# Add labels and title
plt.xlabel('Number of Threads')
plt.ylabel('Wall Clock Time (seconds)')
plt.title('Wall Clock Time vs Number of Threads')

# Add legend
plt.legend(['Wall Clock Time'])

# Show plot
plt.show()