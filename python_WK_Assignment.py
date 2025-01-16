#Code for File Read & Write Challenge

try:
    # Open the input file in read mode
    with open('input.txt', 'r') as file:
        content = file.read()  # Read the entire content of the file

    # Modify the content (e.g., converting to uppercase)
    modified_content = content.upper()

    # Write the modified content into a new file
    with open('output.txt', 'w') as file:
        file.write(modified_content)  # Write the modified content to the new file

    print("File read and write operation was successful!")
    print("Modified content has been written to 'output.txt'.")

except FileNotFoundError:
    print("Error: 'input.txt' does not exist.")
except IOError:
    print("Error: There was an issue reading or writing to the file.")





#Code for Error handling

filename = input("Enter the filename to read (e.g., input.txt): ")

try:
    # Try to open the file for reading
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n", content)  # Display the file content

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: There was an issue reading the file '{filename}'. Please check the file permissions.")


