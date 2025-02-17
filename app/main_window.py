from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                              QPushButton, QFileDialog, QMessageBox,
                              QDialog, QCheckBox, QLabel, QGridLayout,
                              QProgressDialog)
from PySide6.QtCore import Qt, QTimer
from slide_list_widget import SlideListWidget
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WSI De-identification Tool")
        self.setMinimumSize(800, 600)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create buttons with styling
        self.open_folder_btn = QPushButton("📂 Open Folder")
        self.open_folder_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        self.anonymize_all_btn = QPushButton("🔒 Anonymize All Slides")
        self.anonymize_all_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        self.anonymize_all_btn.setEnabled(False)
        
        # Create slide list widget
        self.slide_list = SlideListWidget()
        
        # Add widgets to layout
        layout.addWidget(self.open_folder_btn)
        layout.addWidget(self.slide_list)
        layout.addWidget(self.anonymize_all_btn)
        
        # Connect signals
        self.open_folder_btn.clicked.connect(self.open_folder)
        self.anonymize_all_btn.clicked.connect(self.anonymize_all_slides)
        
    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            try:
                # Store the folder path for later use
                self.current_folder = folder_path
                
                # Create and show progress dialog
                progress = QProgressDialog("Loading slides...", None, 0, 0, self)
                progress.setWindowTitle("Please Wait")
                progress.setWindowModality(Qt.WindowModal)
                progress.setMinimumDuration(0)
                progress.setValue(0)
                progress.setStyleSheet("""
                    QProgressDialog {
                        background-color: white;
                    }
                    QLabel {
                        color: #333333;
                        font-size: 14px;
                    }
                """)
                
                # Use QTimer to allow the progress dialog to show
                QTimer.singleShot(100, lambda: self._load_slides(folder_path, progress))
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error loading slides: {str(e)}")

    def _load_slides(self, folder_path, progress):
        try:
            self.slide_list.load_slides(folder_path)
            self.anonymize_all_btn.setEnabled(True)
            progress.close()
        except Exception as e:
            progress.close()
            QMessageBox.critical(self, "Error", f"Error loading slides: {str(e)}")
    
    def anonymize_all_slides(self):
        # Show configuration dialog
        config_dialog = AnonymizationConfigDialog(self)
        if config_dialog.exec() != QDialog.Accepted:
            return

        try:
            # Get configuration options
            options = config_dialog.get_options()
            
            # Pass the folder path and options to the slide list widget
            self.slide_list.anonymize_all_slides(self.current_folder, options)
            folder_name = os.path.basename(self.current_folder)
            QMessageBox.information(self, "Success", 
                f"All slides in folder '{folder_name}' have been anonymized successfully and saved in a new folder called '{folder_name}_DEID'.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error during anonymization: {str(e)}")

class AnonymizationConfigDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Anonymization Options")
        self.setModal(True)
        
        layout = QGridLayout(self)
        
        # Add disclaimer first
        disclaimer = QLabel(
            "This de-identification process removes slide labels from whole-slide "
            "images in the following formats:"
            "<ul>"
            "<li>Aperio SVS</li>"
            "<li>Hamamatsu NDPI</li>"
            "<li>3DHISTECH MRXS</li>"
            "</ul>"
            "This tool is based on the anonymize-slide project: "
            "<a href='https://github.com/bgilbert/anonymize-slide'>https://github.com/bgilbert/anonymize-slide</a><br>"
        )
        disclaimer.setWordWrap(True)
        disclaimer.setStyleSheet("QLabel { color: #666666; }")
        disclaimer.setTextFormat(Qt.RichText)
        disclaimer.setOpenExternalLinks(True)
        
        # Add description after disclaimer
        description = QLabel("Please select the anonymization options:")
        description.setWordWrap(True)
        
        layout.addWidget(disclaimer, 0, 0, 1, 2)
        layout.addWidget(description, 1, 0, 1, 2)
        
        # Add checkboxes for the options
        self.filename_md5_cb = QCheckBox("Encrypt filename using MD5")
        self.filename_md5_cb.setChecked(True)
        self.honest_broker_cb = QCheckBox("Create secure data mapping file (PHI, Recommended)")
        self.honest_broker_cb.setChecked(True)
        
        # Add checkboxes to layout (moved down to accommodate disclaimer)
        layout.addWidget(self.filename_md5_cb, 2, 0)
        layout.addWidget(self.honest_broker_cb, 3, 0)
        
        # Add buttons
        self.ok_button = QPushButton("Proceed")
        self.ok_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 6px 12px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                padding: 6px 12px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
        """)
        
        layout.addWidget(self.ok_button, 4, 0)
        layout.addWidget(self.cancel_button, 4, 1)
        
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
    
    def get_options(self):
        return {
            'encrypt_filename': self.filename_md5_cb.isChecked(),
            'create_honest_broker': self.honest_broker_cb.isChecked()
        }