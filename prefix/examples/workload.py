import random

total_insertions = 1000000000

def generate_keys(total_insertions):
    key_space = 1000000000
    keys_per_stage = 592592
    min_sequential_keys = 37037
    max_sequential_keys = 148148
    

    with open('/tmp/fileForInput', 'w') as output_file:
        remaining_insertions = total_insertions

        while remaining_insertions > 0:
            random_keys_first_part = random.randint(1, keys_per_stage // 2)
            random_keys = random.sample(range(1, key_space + 1), random_keys_first_part)

            start_position = random.choice(random_keys)
            sequential_length = random.randint(min_sequential_keys, max_sequential_keys)
            sequential_chunk = list(range(start_position, start_position + sequential_length))

            remaining_keys = keys_per_stage - len(random_keys) - len(sequential_chunk)
            random_positions = random.sample(range(1, key_space + 1), remaining_keys)

            stage_keys = random_keys + sequential_chunk + random_positions

            output_file.write('\n'.join(map(str, stage_keys)) + '\n')

            remaining_insertions -= keys_per_stage

        # Handle the case where the last stage has fewer than 592,592 keys
        # if remaining_insertions < 0:
        #     output_file.seek(0, 2)  # Move to the end of the file
        #     output_file.truncate(output_file.tell() + remaining_insertions * -1)  # Remove extra keys

    print(f"{total_insertions} Keys generated and written to '/tmp/fileForInput'.")


generate_keys(total_insertions)

# def count_lines(file_path):
#     with open(file_path, 'r') as file:
#         return sum(1 for line in file)

# # Example usage:
# file_path = '/tmp/fileForInput'  # Replace with the actual path to your output file
#   # Replace with the desired total number of insertions

# # Count the number of lines in the output file
# lines_in_file = count_lines(file_path)

# # Check if the number of lines matches the total_insertions
# if lines_in_file == total_insertions:
#     print(f"Number of lines in the file ({lines_in_file}) matches the total_insertions.")
# else:
#     print(f"Number of lines in the file ({lines_in_file}) does not match the total_insertions.")

