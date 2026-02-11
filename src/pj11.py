import os


def main():
    # Get the current working directory
    current_directory = os.getcwd()

    # Print the current working directory
    print("Current Working Directory:", current_directory)

    # List all files and directories in the current working directory
    items = os.listdir(current_directory)
    print("Files and Directories in Current Working Directory:")


if __name__ == "__main__":
    main()
