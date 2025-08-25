# File: file_tasks.py

# --- File Read & Write Challenge 🖋️ ---
def file_read_write():
    print("\n=== File Read & Write Challenge ===")
    
    # Ask user for input file name
    input_file = input("Enter the input file name: ")

    # Read content from the input file
    with open(input_file, "r") as infile:
        content = infile.read()

    # Modify the content (convert to uppercase as an example)
    modified_content = content.upper()

    # Ask user for output file name
    output_file = input("Enter the output file name: ")

    # Write modified content to the new file
    with open(output_file, "w") as outfile:
        outfile.write(modified_content)

    print(f"✅ Modified content has been written to '{output_file}'")


# --- Error Handling Lab 🧪 ---
def error_handling_lab():
    print("\n=== Error Handling Lab ===")
    try:
        # Ask user for the file name
        filename = input("Enter the file name to read: ")

        # Try opening and reading the file
        with open(filename, "r") as file:
            content = file.read()
            print("\nFile content:\n")
            print(content)

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You do not have permission to access this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# --- Main Menu ---
def main():
    while True:
        print("\nChoose an option:")
        print("1. File Read & Write Challenge 🖋️")
        print("2. Error Handling Lab 🧪")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            file_read_write()
        elif choice == "2":
            error_handling_lab()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
