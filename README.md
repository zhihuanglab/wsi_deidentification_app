# wsi_deidentification_app


## Installation

```bash
conda create -n wsi_deid python=3.11 -y
conda activate wsi_deid
pip install -r requirements.txt
```

## Usage

### Running from source
```bash
python main.py
```

### Building for Windows
1. Install required build dependencies:
```bash
pip install pyinstaller
```

2. Create executable:
```bash
pyinstaller --name wsi_deidentifier --windowed --onefile app/main.py
```

The executable will be created in the `dist` folder. You can find it at `dist/wsi_deidentifier.exe`.

## Notes
- The `--windowed` flag prevents the console window from appearing when running the application
- The `--onefile` flag creates a single executable file containing everything needed to run the application
- You can distribute the executable to other Windows computers, and they won't need Python installed to run it
