import os
import random

# def create_files():
#     # Step 1
#     with open('/tmp/file1.txt', 'w') as file1:
#         for i in range(1, 500000000):
#             file1.write(str(i) + '\n')

#     with open('/tmp/file2.txt', 'w') as file2:
#         for i in range(250000001, 500000000):
#             file2.write(str(i) + '\n')

def create_files():
    # Step 1
    with open('/tmp/file1.txt', 'w') as file1:
        ranges_file1 = [(1, 50000000), (250000001, 300000000), (500000001, 550000000), (750000001, 800000000)]
        for start, end in ranges_file1:
            for i in range(start, end + 1):
                file1.write(str(i) + '\n')

    with open('/tmp/file2.txt', 'w') as file2:
        ranges_file2 = [(50000001, 250000000), (300000001, 500000000), (550000001, 750000000), (800000001, 1000000000)]
        for start, end in ranges_file2:
            for i in range(start, end + 1):
                file2.write(str(i) + '\n')


def shuffle_file_blocks(file_path):
    # Read file into blocks of 31000 lines and shuffle each block
    with open(file_path, 'r') as file:
        lines = file.readlines()
        shuffled_blocks = [lines[i:i+37037] for i in range(0, len(lines), 37037)]
        random.shuffle(shuffled_blocks)

    # Write the shuffled blocks back to the file
    with open(file_path, 'w') as file:
        for block in shuffled_blocks:
            file.write(''.join(block))

def shuffle_file_lines(file_path):
    # Read file lines and shuffle them
    with open(file_path, 'r') as file:
        lines = file.readlines()
        random.shuffle(lines)

    # Write the shuffled lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

def merge_and_output():
    # Merge files in the specified pattern to create the target file
    with open('/tmp/fileForInput', 'w') as target_file:
        with open('/tmp/file1.txt', 'r') as file1, open('/tmp/file2.txt', 'r') as file2:
            while True:
                for i in range(37037):
                    line1 = file1.readline()
                    if line1:
                        target_file.write(line1)
                    else:
                        break

                for i in range(148148):
                    line2 = file2.readline()
                    if line2:
                        target_file.write(line2)
                    else:
                        break

                if not line1 or not line2:
                    break

# Step 1
create_files()

# Step 2
shuffle_file_blocks('/tmp/file1.txt')

# Step 3
shuffle_file_lines('/tmp/file2.txt')

# Step 4
merge_and_output()

print("Script 1000M execution completed. Check /tmp/fileForInput file.")
