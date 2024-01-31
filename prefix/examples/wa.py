file_path = '/tmp/percona500M.io'

keySize = 8
valueSize = 100
numOfInsertion = 500000000
total_wMB = 0.0

with open(file_path, 'r') as file:
    for line in file:
        # Split the line into columns based on whitespace
        columns = line.split()

        if len(columns) >= 21:
            try:
                # Extract the value under the 'wMB/s' column (assuming it's at index 15)
                wMB_value = float(columns[8])

                total_wMB += wMB_value
            except (ValueError, IndexError):
                pass

dataWrittenDB = (keySize + valueSize) * numOfInsertion / 1000000000
dataWrittenDisk = total_wMB/1000
print(f'The data written to database is: {dataWrittenDB:.3f} GB')
print(f'The data wrriten to the disk is: {dataWrittenDisk:.3f} GB')
print(f'The WA is: {(dataWrittenDisk/dataWrittenDB):.3f}')




# # Specify the path to your file
# file_path = '/tmp/percona500M.io'

# # Initialize the sum variable
# keySize = 8
# valueSize = 100
# numOfInsertion = 500000000
# total_wMB = 0.0

# # Specify the output file path
# output_file_path = 'output_values.txt'

# # Open the output file in write mode
# with open(output_file_path, 'w') as output_file:
#     # Open and read the file
#     with open(file_path, 'r') as file:
#         # Iterate through each line in the file
#         for line in file:
#             # Split the line into columns based on whitespace
#             columns = line.split()

#             # Check if the line contains the expected number of columns
#             if len(columns) >= 21:
#                 try:
#                     # Extract the value under the 'wMB/s' column (assuming it's at index 15)
#                     wMB_value = float(columns[8])

#                     # Print the value before adding to the total sum
#                     print(f'Current value under the column wMB/s: {wMB_value} MB')

#                     # Write the value to the output file
#                     output_file.write(f'{wMB_value}\n')

#                     # Add the value to the total sum
#                     total_wMB += wMB_value
#                 except (ValueError, IndexError):
#                     # Handle the case where conversion to float fails or index is out of range
#                     pass

# # Print the total sum
# dataWrittenDB = (keySize + valueSize) * numOfInsertion / 1000000000
# dataWrittenDisk = total_wMB/1000
# print(f'The data written to database is: {dataWrittenDB} GB')
# print(f'The data wrriten to the disk is: {dataWrittenDisk:.3f} GB')
# print(f'The WA is: {(dataWrittenDisk/dataWrittenDB):.3f}')
# print(f'Values have been saved to: {output_file_path}')
