
import subprocess
import time
import csv
import os

# List of executables to benchmark
programs = ["./bin/bubble-sort", "./bin/optimized-bubble-sort", "./bin/insertion-sort", "./bin/selection-sort"]

# Read inputs from the file
with open("inputs.txt", "r") as f:
    inputs = [line.strip() for line in f]

# Open CSV file for writing results
with open("benchmark_results.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Input Size", "Input", "Program", "Execution Time (seconds)"])

    # Benchmark each input for all programs
    for input_value in inputs:
        print(f"Running benchmarks for input: {input_value}")

        for program in programs:
            if not os.path.exists(program):
                print(f"Executable not found: {program}")
                continue
            try:
                # Measure execution time
                start_time = time.perf_counter()

                # Run the program with input
                process = subprocess.run(
                    [program],
                    input=input_value,
                    text=True,
                    capture_output=True
                )
                end_time = time.perf_counter()
                elapsed_time = end_time - start_time

                # print(f"{os.path.basename(program)} Output: {process.stdout.strip()}")

                # Log result
                writer.writerow([len(input_value.split(" ")), input_value, os.path.basename(program), elapsed_time])

            except Exception as e:
                print(f"Error benchmarking {program} with input {input_value}: {e}")

print("Benchmarking complete. Results saved in benchmark_results.csv.")
