
import matplotlib.pyplot as plt
import csv
from collections import defaultdict

# Store results for each program: input sizes mapped to execution times
program_data = defaultdict(lambda: defaultdict(list))

# Read the CSV file
with open('benchmark_results.csv', mode='r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        input_size = int(row['Input Size'])
        program = row['Program']
        time = float(row['Execution Time (seconds)'])
        
        # Append the time for this input size and program
        program_data[program][input_size].append(time)

# Plot the data
plt.figure(figsize=(12, 7))

for program, size_time_map in program_data.items():
    # Sort the data by input size
    sorted_sizes = sorted(size_time_map.keys())
    avg_times = [sum(size_time_map[size]) / len(size_time_map[size]) for size in sorted_sizes]

    plt.plot(sorted_sizes, avg_times, marker=None, label=program)

# Customize the plot
plt.title('Benchmark Results for Sorting Algorithms')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
