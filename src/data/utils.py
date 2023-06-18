import os


def create_path(folder, name):
    return os.path.join(folder, f"{name}_data.csv")


def create_directory(directory: str) -> None:
    """
    Create a directory if it doesn't exist

    Args:
        directory (str): Str indicating the directory path.
    Returns:
        None
    """
    if not os.path.exists(directory):
        # If it doesn't exist, create it
        print(f"Creating...{directory}")
        os.makedirs(directory)
