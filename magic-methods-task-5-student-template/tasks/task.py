import os
import random
import shutil
import string
import tempfile


class TempDir:
    def __enter__(self):
        # Save current working directory
        self.old_cwd = os.getcwd()

        # Generate a random directory name
        chars = string.ascii_lowercase + string.digits
        random_dir_name = ''.join(random.choice(chars) for i in range(10))

        # Combine the random name with a system-specific temporary directory path
        self.temp_dir = os.path.join(tempfile.gettempdir(), random_dir_name)

        # Create the directory using os.mkdir
        try:
            os.mkdir(self.temp_dir)
        except OSError as e:
            # Handle potential naming conflicts or other errors during directory creation
            raise OSError(f"Failed to create temporary directory: {e}") from e

        os.chdir(self.temp_dir)  # Change working directory to temporary directory
        return self.temp_dir  # Return the temporary directory path

    def __exit__(self, exc_type, exc_value, traceback):
        # Change working directory back to the original directory
        os.chdir(self.old_cwd)

        # Remove the temporary directory and its contents
        shutil.rmtree(self.temp_dir)



if __name__ == '__main__':
    with TempDir() as temp_dir:
        # Inside the context manager, temp_dir is the path to the temporary directory
        print("Inside TempDir context manager:")
        print("Current directory:", os.getcwd())  # Should be the temporary directory

        # try:
        #     print('Enter file name:')
        #     filename = input()
        #     with open(os.getcwd()+'/'+filename, 'w') as f:
        #         f.write("This is some content for the file.")
        #     print(f"File '{filename}' created successfully.")
        #     # input()
        # except OSError as e:
        #     print(f"Error creating file or directories: {e}")

    # Outside the context manager, the temporary directory has been removed
    print("\nOutside TempDir context manager:")
    print("Current directory:", os.getcwd())  # Should be back to the original directory
