import subprocess
import os
import sys

def anonymize_slide(filepath):
    """
    Wrapper function to call the anonymize-slide script
    """
    script_path = os.path.join(os.path.dirname(__file__), "anonymize-slide.py")
    # Convert filepath to absolute path to ensure correct file location
    abs_filepath = os.path.abspath(filepath)
    
    try:
        result = subprocess.run(
            [sys.executable, script_path, abs_filepath],
            capture_output=True,
            text=True,
            check=True
        )
        return True
    except subprocess.CalledProcessError as e:
        raise Exception(f"Anonymization failed: {e.stderr}") 