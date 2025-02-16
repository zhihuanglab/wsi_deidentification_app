from PySide6.QtWidgets import (QDialog, QVBoxLayout, QTextEdit, 
                              QPushButton, QLabel)

class SlideMetadataDialog(QDialog):
    def __init__(self, slide, parent=None):
        super().__init__(parent)
        self.slide = slide
        self.setup_ui()
        
    def setup_ui(self):
        self.setWindowTitle("Slide Metadata")
        self.setMinimumSize(400, 300)
        
        layout = QVBoxLayout(self)
        
        # Add metadata text
        metadata_text = QTextEdit()
        metadata_text.setReadOnly(True)
        
        # Format metadata
        metadata = self.slide.properties
        formatted_text = "\n".join([f"{k}: {v}" for k, v in metadata.items()])
        metadata_text.setText(formatted_text)
        
        # Add close button
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        
        layout.addWidget(metadata_text)
        layout.addWidget(close_btn) 