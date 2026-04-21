 Object Localization Project


This project leverages Transfer Learning with the EfficientNetB0 architecture to predict bounding box coordinates in images. By utilizing a pre-trained model as a feature extractor, the system achieves high localization accuracy even with a custom head.



🎯 Supported Task: The model performs Object Localization, outputting four normalized coordinates [xmin, ymin, xmax, ymax] for the target object.


🛠 Tech Stack: Language: Python 3.x Framework: TensorFlow / Keras Environment: Jupyter Notebook Libraries: OpenCV, NumPy, Matplotlib, Re


⚙️ Installation


To set up the environment and install all dependencies, run the following commands:
```bash
 Create virtual environment
   python -m venv venv

 Activate virtual environment
   On Windows:
     venv\Scripts\activate
   On macOS/Linux:
     source venv/bin/activate

 Install dependencies
   pip install -r requirements.txt
```

📊 Results:


<img width="714" height="704" alt="image" src="https://github.com/user-attachments/assets/eb4f93e8-c4b9-49c4-b743-b7090748c9dd" />
