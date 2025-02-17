import os
import anonymize_functions  # Import the updated anonymization functions

def anonymize_slide(filepath):
    """ Calls anonymization function directly from `anonymize_functions.py` """
    abs_filepath = os.path.abspath(filepath)

    print(f"Anonymizing file: {abs_filepath}")

    try:
        success = anonymize_functions._main([abs_filepath])  # Now `_main()` accepts arguments
        if success == 0:  # `_main()` returns 0 on success
            print(f"Anonymization completed successfully for {abs_filepath}")
            return True
        else:
            raise Exception("Anonymization failed with non-zero exit code.")
    except Exception as e:
        print(f"Error during anonymization: {str(e)}")
        raise Exception(f"Error during anonymization: {str(e)}")
