

from dotenv import load_dotenv
import os
import re
import sys

my_USE_GOOGLE_COLAB = False
my_USE_NVIDIA = False
my_CONTENT_PATH = ""
my_TIF_PATH = ""
my_DROPBOX_URL = ""
my_DROPBOX_TOKEN = ""
my_DROPBOX_KEY = ""
my_DROPBOX_SECRET = ""
my_MODEL_FILENAME = ""

def contains_affirmative(string):
    affirmative_values = ["yes", "1", "true"]
    string_lower = string.lower()

    for value in affirmative_values:
        if value in string_lower:
            return True

    return False

def expand_my_vars(input_string):
    def replace_my_var(match):
        my_var = match.group(1)[1:]  # Remove the leading '$'
        z = os.environ.get(my_var, match.group(0))
        return z

    pattern = r'\{(\$[A-Za-z_][A-Za-z0-9_]*)\}'
    return re.sub(pattern, replace_my_var, input_string)#common logic for the jupyter notebooks to set global variables from local .env file

def load_settings(path="./env"):
    
    # Load environment variables from .env file
    zCwd = os.getcwd()
    zDefPath = zCwd + "/.env"
    print( "Loading settings from " + zDefPath)
    load_dotenv()

    # Access environment variables
    global my_CONTENT_PATH
    z = os.environ.get("CONTENT_PATH","{$HOME}/batguts")
    my_CONTENT_PATH = expand_my_vars(z)
    
    global my_TIF_PATH
    z = os.environ.get("TIF_PATH", my_CONTENT_PATH + "/Bat_guts")
    my_TIF_PATH = expand_my_vars(z)
    
    z = os.environ.get("MODEL_FILENAME", "IVP_MODEL.keras")
    global my_MODEL_FILENAME
    my_MODEL_FILENAME = expand_my_vars(z)
    
    z = os.environ.get("DROPBOX_TOKEN", "unknown")
    global my_DROPBOX_TOKEN
    my_DROPBOX_TOKEN = expand_my_vars(z)
    
    z = os.environ.get("DROPBOX_KEY", "unknown")
    global my_DROPBOX_KEY
    my_DROPBOX_KEY = expand_my_vars(z)
    
    z = os.environ.get("DROPBOX_SECRET", "unknown")
    global my_DROPBOX_SECRET
    my_DROPBOX_SECRET = expand_my_vars(z)
    
    z = os.environ.get("DROPBOX_URL", "https://www.dropbox.com/scl/fo/4fkh1x98c2ah3vyi6r5yq/AGpqhAmPn3u2IsPGxost1rI?rlkey=jfrxfj05m2965f2ws7mmp8mvo&st=cw20pi1v&dl=0")
    global my_DROPBOX_URL
    my_DROPBOX_URL = expand_my_vars(z)
    
    z = os.environ.get("IMAGE_SHAPE_X", "299")
    global my_IMAGE_SHAPE_X
    my_IMAGE_SHAPE_X = int(z)
    
    z = os.environ.get("IMAGE_SHAPE_Y", "299")
    global my_IMAGE_SHAPE_Y
    my_IMAGE_SHAPE_Y = int(z)
    
    
    print("my_CONTENT_PATH="+my_CONTENT_PATH)
    print("my_TIF_PATH="+my_TIF_PATH)
    global my_USE_GOOGLE_COLAB
    my_USE_GOOGLE_COLAB = contains_affirmative(os.environ.get('USE_GOOGLE_COLAB', 'False'))
    global my_USE_NVIDIA
    my_USE_NVIDIA = contains_affirmative(os.environ.get('USE_NVIDIA', 'False'))

    return

from dataclasses import dataclass

@dataclass
class BatGutsSettings:
    zContentPath: str
    zTifPath: str
    zModelFilename: str
    zDropboxUrl: str
    zDropboxToken: str
    zDropboxKey: str
    zDropboxSecret: str
    useGoogleColab: bool
    useNvidia: bool
    imageShapeX: int
    imageShapeY: int

def load_BatGutsSettings(path="./env") -> BatGutsSettings:
    load_settings(path)
    return BatGutsSettings(zContentPath=my_CONTENT_PATH,
                           zTifPath=my_TIF_PATH,
                           zModelFilename=my_MODEL_FILENAME,
                           zDropboxUrl=my_DROPBOX_URL,
                           zDropboxToken=my_DROPBOX_TOKEN,
                           zDropboxKey=my_DROPBOX_KEY,
                           zDropboxSecret=my_DROPBOX_SECRET,
                           useGoogleColab=my_USE_GOOGLE_COLAB,
                           useNvidia=my_USE_NVIDIA,
                           imageShapeX=my_IMAGE_SHAPE_X,
                           imageShapeY=my_IMAGE_SHAPE_Y)
()
def show_python_version():
    # Check major version
    print("Python version: " + str(sys.version_info.major)+"."+str(sys.version_info.minor)+"."+str(sys.version_info.micro))


import numpy as np
import math
def mean2(x):
    y = np.sum(x) / np.size(x);
    return y

def old_corr2(a,b):
    a = a - mean2(a)
    b = b - mean2(b)

    r = (a*b).sum() / math.sqrt((a*a).sum() * (b*b).sum());
    return r

import numpy as np

def corr2(a, b):
    """
    Compute the 2D correlation coefficient between two images.
    
    Parameters:
    a, b : numpy arrays of same shape
        Input arrays or images
    
    Returns:
    r : float
        Correlation coefficient
    """
    a = a.astype(float)
    b = b.astype(float)
    
    a = a - np.mean(a)
    b = b - np.mean(b)
    
    r = np.sum(a * b) / np.sqrt(np.sum(a * a) * np.sum(b * b))
    return r

import os
import glob
import shutil

def remove_matching_files(folder_path, pattern):
    """
    Remove all files matching the given pattern in the specified folder and its subdirectories.
    Also remove subdirectories that match the pattern after their contents have been processed.
    
    :param folder_path: Path to the folder containing the files
    :param pattern: File pattern to match (e.g., '*.txt' for all text files)
    """
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    removed_files_count = 0
    removed_dirs_count = 0

    for root, dirs, files in os.walk(folder_path, topdown=False):
        # Process files
        full_pattern = os.path.join(root, pattern)
        matching_files = glob.glob(full_pattern)

        for file_path in matching_files:
            try:
                os.remove(file_path)
                print(f"Removed file: {file_path}")
                removed_files_count += 1
            except Exception as e:
                print(f"Error removing file {file_path}: {e}")

        # Check if the current directory matches the pattern
        if glob.fnmatch.fnmatch(os.path.basename(root), pattern):
            try:
                shutil.rmtree(root)
                print(f"Removed directory: {root}")
                removed_dirs_count += 1
            except Exception as e:
                print(f"Error removing directory {root}: {e}")

    if removed_files_count == 0 and removed_dirs_count == 0:
        print(f"No files or directories matching the pattern '{pattern}' were found in '{folder_path}' or its subdirectories.")
    else:
        print(f"Removed {removed_files_count} file(s) and {removed_dirs_count} directory(ies) matching the pattern '{pattern}'.")



from datetime import datetime

def get_most_recent_subdirectory(zDir):
    try:
        # Get all subdirectories in the given directory
        subdirectories = [os.path.join(zDir, d) for d in os.listdir(zDir) if os.path.isdir(os.path.join(zDir, d))]
        
        if not subdirectories:
            return None  # No subdirectories found
        
        # Sort subdirectories by creation time (most recent first)
        sorted_subdirectories = sorted(subdirectories, key=lambda x: os.path.getctime(x), reverse=True)
        
        # Return the most recently created subdirectory
        return sorted_subdirectories[0]
    
    except FileNotFoundError:
        print(f"Error: The directory '{zDir}' does not exist.")
        return None
    except PermissionError:
        print(f"Error: Permission denied to access the directory '{zDir}'.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None
    
def get_most_recent_numeric_subdirectory(zDir):
    try:
        # Get all subdirectories in the given directory that start with a number
        subdirectories = [
            os.path.join(zDir, d) for d in os.listdir(zDir)
            if os.path.isdir(os.path.join(zDir, d)) and re.match(r'^\d', d)
        ]
        
        if not subdirectories:
            return None  # No matching subdirectories found
        
        # Sort subdirectories by creation time (most recent first)
        sorted_subdirectories = sorted(subdirectories, key=lambda x: os.path.getctime(x), reverse=True)
        
        # Return the most recently created subdirectory
        return sorted_subdirectories[0]
    
    except FileNotFoundError:
        print(f"Error: The directory '{zDir}' does not exist.")
        return None
    except PermissionError:
        print(f"Error: Permission denied to access the directory '{zDir}'.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None
    
import mlflow
import subprocess
import time
import threading
import os

import subprocess

def run_mlflow(zBackendStoreUri=None):
    # Base command to start MLflow UI
    command = ["mlflow", "ui"]
    
    # Add backend store URI if provided
    if zBackendStoreUri is not None:
        command.extend(["--backend-store-uri", zBackendStoreUri])
    
    # Start MLflow UI in the background
    mlflow_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("MLflow UI started. Access it at http://127.0.0.1:5000")
    print("Enter 'q' up at the top of the screen to terminate")
    
    return mlflow_process

def shutdown_mlflow(mlflow_process):
    # Terminate the MLflow process
    mlflow_process.terminate()
    mlflow_process.wait()
    print("MLflow UI has been shut down.")

def user_input_thread(mlflow_process):
    while True:
        user_input = input("Enter 'q' to quit MLflow: ")
        if user_input.lower() == 'q':
            shutdown_mlflow(mlflow_process)
            break
'''
This function fires up "mlflow ui" as a background process until 'q' is entered from the keyboard 
'''
def run_mlflow_until_q(  zBackendStoreUri=None):     
    # Start MLflow in the background
    mlflow_process = run_mlflow(zBackendStoreUri)

    # Start a thread to handle user input
    input_thread = threading.Thread(target=user_input_thread, args=(mlflow_process,))
    input_thread.start()

    try:
        # Keep the main thread alive
        while input_thread.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Shutting down MLflow...")
        shutdown_mlflow(mlflow_process)

import subprocess
def kill_mlflow_server():
    try:
        subprocess.run("kill -9 $(lsof -ti :5000)", shell=True, check=True)
        print("MLflow server processes on port 5000 have been terminated.")
    except subprocess.CalledProcessError:
        print("No MLflow server processes found on port 5000.")

# This line allows the function to be imported in a Jupyter notebook
__all__ = ['load_BatGutsSettings', 
           'show_python_version', 
           'corr2', 
           'remove_matching_files',
           'run_mlflow_until_q',
           'kill_mlflow_server',
           'get_most_recent_subdirectory',
           'get_most_recent_numeric_subdirectory'
           ]


if __name__ == "__main__":
    # Test the function
    test_strings = [
        "My home directory is {$HOME}",
        "The current user is {$USER} and the home is {$HOME}",
        "Path: {$PATH}",
        "Non-existent var: {$NONEXISTENT}",
        "Mixed content: {$HOME}/documents and {$USER}'s files",
        "No variables here",
        "Partial match: {$HOM",
        "Multiple occurrences: {$HOME} and again {$HOME}"
    ]

    for test_string in test_strings:
        expanded = expand_my_vars(test_string)
        print(f"Original: {test_string}")
        print(f"Expanded: {expanded}")
        print()

    load_settings()
    # Use the environment variables
    print(f"USE_GOOGLE_COLAB: {my_USE_GOOGLE_COLAB}")
    print(f"CONTENT_PATH: {my_CONTENT_PATH}")
    




