import sys, json, yaml, xmltodict, threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel

def parse():

    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    return sys.argv[1], sys.argv[2]

def load_json(input):
    try:
        with open(input, 'r') as f:
            data = json.load(f)
        print("JSON data loaded successfully")
        return data
    
    except Exception as e:
        print(f"Failed to load JSON file: {e}")
        sys.exit(1)

def save_json(data, output):
    try:
        with open(output, 'w') as f:
            json.dump(data, f, indent=4)
        print("JSON data saved successfully")

    except Exception as e:
        print(f"Failed to save JSON file: {e}")
        sys.exit(1)

def load_yaml(input):
    try:
        with open(input, 'r') as f:
            data = yaml.safe_load(f)
        print("YAML data loaded successfully")
        return data
    
    except Exception as e:
        print(f"Failed to load YAML file: {e}")
        sys.exit(1)

def save_yaml(data, output):
    try:
        with open(output, 'w') as f:
            yaml.safe_dump(data, f)
        print("YAML data saved successfully")

    except Exception as e:
        print(f"Failed to save YAML file: {e}")
        sys.exit(1)

def load_xml(input):
    try:
        with open(input, 'r') as f:
            data = xmltodict.parse(f.read())
        print("XML data loaded successfully")
        return data
    
    except Exception as e:
        print(f"Failed to load XML file: {e}")
        sys.exit(1)

def save_xml(data, output):
    try:
        with open(output, 'w') as f:
            xmltodict.unparse(data, output=f, pretty=True)
        print("XML data saved successfully")

    except Exception as e:
        print(f"Failed to save XML file: {e}")
        sys.exit(1)

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.input_label = QLabel("Input File: None")
        self.output_label = QLabel("Output File: None")
        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.output_label)

        self.input_button = QPushButton('Select Input File')
        self.output_button = QPushButton('Select Output File')
        self.convert_button = QPushButton('Convert')

        self.input_button.clicked.connect(self.select_input)
        self.output_button.clicked.connect(self.select_output)
        self.convert_button.clicked.connect(self.convert_files)

        self.layout.addWidget(self.input_button)
        self.layout.addWidget(self.output_button)
        self.layout.addWidget(self.convert_button)

        self.setLayout(self.layout)
        self.setWindowTitle('Data Converter')
        self.show()

    def select_input(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Select Input File", "", "All Files (*);;JSON Files (*.json);;YAML Files (*.yml *.yaml);;XML Files (*.xml)", options=options)
        if file:
            self.input_label.setText(f"Input File: {file}")
            self.input = file

    def select_output(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getSaveFileName(self, "Select Output File", "", "All Files (*);;JSON Files (*.json);;YAML Files (*.yml *.yaml);;XML Files (*.xml)", options=options)
        if file:
            self.output_label.setText(f"Output File: {file}")
            self.output = file

    def convert_files(self):
        self.thread = threading.Thread(target=self._convert_files)
        self.thread.start()

    def _convert_files(self):
        try:
            if self.input.endswith('.json'):
                data = load_json(self.input)
            elif self.input.endswith('.yml') or self.input.endswith('.yaml'):
                data = load_yaml(self.input)
            elif self.input.endswith('.xml'):
                data = load_xml(self.input)

            if self.output.endswith('.json'):
                save_json(data, self.output)
            elif self.output.endswith('.yml') or self.output.endswith('.yaml'):
                save_yaml(data, self.output)
            elif self.output.endswith('.xml'):
                save_xml(data, self.output)
            self.output_label.setText("Conversion Successful!")
        except Exception as e:
            self.output_label.setText(f"Conversion Failed: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ConverterApp()
    sys.exit(app.exec_())