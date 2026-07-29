# 🌱 Plant Disease Detection using CNN

An end-to-end deep learning project that uses a Convolutional Neural Network (CNN) to identify plant leaf conditions from images.

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone (https://github.com/FireStormy1/Plant-Disease-Detection-)
```

Navigate into the project folder:

```bash
cd Plant-Disease-Detection
```

### 2. Open the Jupyter Notebook

Open the `.ipynb` file using:

- VS Code with the Jupyter extension
- Jupyter Notebook
- JupyterLab
- Google Colab

For local execution, **VS Code is recommended**.

### 3. Install the Required Libraries

Make sure Python is installed on your system.

Install the required dependencies:

```bash
pip install tensorflow numpy matplotlib pillow streamlit
```

You can also install the dependencies using:

```bash
pip install -r requirements.txt
```

### 4. Run the Jupyter Notebook

Open the following file in VS Code:

```text
Plant_Disease_Detection.ipynb
```

Run the notebook cells in order.

The notebook will automatically download the required plant leaf images from the external PlantVillage GitHub repository.

The dataset will then be prepared locally on your computer for training and testing.

> ⚠️ You need an active internet connection during the initial dataset download.

### 5. Train the CNN Model

After the dataset has been downloaded and prepared, the notebook will:

- Load the images
- Explore the dataset
- Create training and testing sets
- Build the CNN
- Train the model
- Evaluate the model
- Generate predictions

The trained model is saved as:

```text
plant_cnn.keras
```

## 🌐 Run the Plant Disease Detector

After training the model, the project can be launched as a local Streamlit application.

Run:

```bash
streamlit run plant_app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

You can then:

1. Upload a plant leaf image.
2. The application processes the image.
3. The trained CNN model analyses the image.
4. The predicted plant condition is displayed along with confidence information.

## 🧠 Model Architecture

The project uses a CNN built from scratch.

The model demonstrates fundamental deep learning concepts including:

- Convolutional layers
- Pooling
- ReLU activation
- Dense layers
- Softmax classification

The model is trained to classify images into 5 plant leaf conditions.

## 🌿 Supported Classes

| Class | Description |
|---|---|
| Apple Black Rot | Apple leaf affected by Black Rot |
| Apple Cedar Rust | Apple leaf affected by Cedar Rust |
| Apple Healthy | Healthy Apple leaf |
| Apple Scab | Apple leaf affected by Scab |
| Corn Common Rust | Corn leaf affected by Common Rust |

## 📊 Dataset

This project uses a selected subset of the PlantVillage dataset.

The required images are downloaded automatically from the original public GitHub repository during notebook execution.

The project prepares a balanced dataset containing 5 selected classes for the CNN training process.

The dataset is not stored directly in this repository to keep the repository lightweight.

## 🔄 Project Workflow

```text
External PlantVillage GitHub Repository
                │
                ▼
       Download Dataset
                │
                ▼
      Prepare & Balance Data
                │
                ▼
       Explore Leaf Images
                │
                ▼
       Train CNN Model
                │
                ▼
       Evaluate the Model
                │
                ▼
      Save Trained Model
                │
                ▼
      Streamlit Web Application
                │
                ▼
       Upload Leaf Image
                │
                ▼
      Predict Plant Condition
```

## 💻 Local Development

This project is designed to run locally on your computer.

The general workflow is:

```text
Open Jupyter Notebook in VS Code
          ↓
Run the notebook
          ↓
Dataset downloads automatically
          ↓
Dataset is prepared locally
          ↓
CNN model is trained
          ↓
Model is saved locally
          ↓
Run Streamlit application
          ↓
Open localhost:8501
```

## ⚠️ Important Notes

- An internet connection is required when running the notebook for the first time because the dataset is downloaded from an external GitHub repository.
- The dataset itself is not included in this repository.
- The notebook should be executed from the beginning to ensure that the dataset and required files are correctly prepared.
- Training performance may vary depending on your hardware.
- A GPU is recommended for faster model training but is not strictly required.

## 🎯 Future Improvements

Possible improvements include:

- Adding more plant and disease classes
- Using data augmentation
- Increasing the training dataset
- Applying transfer learning with pretrained models
- Improving model accuracy
- Deploying the Streamlit application online
- Adding support for more crops
- Developing a mobile-friendly plant disease diagnosis system

## 👨‍💻 Author

**Saswat Dixit**

B.Tech Computer Science and Engineering Student

Interested in:

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Software Development
- Web Development

GitHub: https://github.com/FireStormy1

LinkedIn: https://www.linkedin.com/in/saswatdixit/

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

> **Note:** The required dataset is downloaded automatically from the original public PlantVillage GitHub repository during notebook execution.

> **Attribution:** The source project/file credits Vijay Kishor Singh (Trainer). Please keep appropriate source attribution and check the original dataset/source licensing and usage terms before publishing or redistributing the notebook or any dataset-derived content.
