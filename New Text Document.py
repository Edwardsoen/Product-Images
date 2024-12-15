import os

def add_prefix_to_filenames():
    # Get the current working directory
    current_folder = os.getcwd()

    # Output file to save the results
    output_file = "file_names_with_prefix.txt"

    # Open the output file for writing
    with open(output_file, "w") as f:
        # Loop through all files in the folder
        for filename in os.listdir(current_folder):
            # Skip directories
            if os.path.isdir(filename):
                continue

            # Add the prefix to the file name
            prefixed_name = f"https://edwardsoen.github.io/Product-Images/{filename}"

            # Write the prefixed name to the file
            f.write(prefixed_name + "\n")

    print(f"File names with prefix have been saved to {output_file}")

if __name__ == "__main__":
    add_prefix_to_filenames()
