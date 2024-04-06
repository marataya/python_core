import os

class Cd:
    def __init__(self, new_dir):
        self.new_dir = new_dir
        self.prev_dir = None

        # Check if the new directory is a valid directory
        if not os.path.isdir(new_dir):
            raise ValueError(f"Directory '{new_dir}' does not exist or is not a directory.")

    def __enter__(self):
        self.prev_dir = os.getcwd()  # Save current working directory
        os.chdir(self.new_dir)  # Change directory to the provided path
        return self.new_dir  # Return the new directory path

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.prev_dir:  # Ensure a previous directory was saved
            os.chdir(self.prev_dir)  # Change back to the previous directory
