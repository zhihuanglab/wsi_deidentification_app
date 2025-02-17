import subprocess
import os
import sys

def anonymize_slide(filepath):
    script_path = os.path.join(os.path.dirname(__file__), "anonymize-slide.py")
    abs_filepath = os.path.abspath(filepath)

    if getattr(sys, 'frozen', False):
        python_executable = os.path.join(sys._MEIPASS, "python.exe")
    else:
        python_executable = sys.executable

    try:
        process = subprocess.Popen(
            [python_executable, script_path, abs_filepath],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            raise Exception(f"Anonymization failed: {stderr}")

        return True
    except Exception as e:
        raise Exception(f"Error during anonymization: {str(e)}")
