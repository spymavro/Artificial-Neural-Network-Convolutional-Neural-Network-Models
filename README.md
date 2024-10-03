# Artificial-Neural-Network-Convolutional-Neural-Network-Models

## Project Overview
This repository is dedicated to the exploration and implementation of neural network models for the recognition of handwritten digits using the MNIST dataset. It features two primary models: an Artificial Neural Network (ANN) and a Convolutional Neural Network (CNN), both designed to classify digits from 0 to 9 with high accuracy. The project leverages deep learning techniques to address common challenges in image recognition tasks.

## Motivation
The motivation behind this project is to demonstrate the effectiveness of neural networks, particularly CNNs, in image classification tasks. By training models on the MNIST dataset, we aim to showcase the potential of neural networks to learn complex patterns and make accurate predictions, serving as a foundational step for more advanced image recognition applications.

## Dataset
The MNIST dataset, a large database of handwritten digits, is used for training and testing the models. It includes:

- **60,000 training examples** from the [Greek Language Center's website](https://www.greek-language.gr/certification/dbs/teachers/index.html) (CEFR levels A1 to C2). These texts are categorized by proficiency levels and can be accessed publicly.
- **10,000 testing examples**: Each image is size-normalized and centered in a fixed-size (28x28 pixels) frame.

**Note**: More information about the dataset can be found [here](https://www.tensorflow.org/datasets/catalog/mnist).

## Technologies Used
- Python
- TensorFlow/Keras
- NumPy
- Matplotlib

## Features
- Implementation of an ANN with two dense layers.
- Implementation of a CNN with two convolutional layers and max pooling layers.
- Evaluation of models using accuracy metrics and confusion matrices.
- Visualization of training and validation loss and accuracy to analyze model performance.

## Results
The performance of the models is summarized as follows:

1. **ANN Model**:
   - **Test Accuracy**: Approximately 97.84%

2. **CNN Model**:
   - **Test Accuracy**: Approximately 98.86%
   - Enhanced accuracy with the addition of max pooling layers.

3. **CNN with Pooling**:
   - **Test Accuracy**: Approximately 99.14%
  
Discussion on overfitting and underfitting issues, as well as the impact of network architecture modifications, are included in the training logs.

## Installation
To set up this project for use or development, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/spymavro/Artificial-Neural-Network-Convolutional-Neural-Network-Models.git
   cd Artificial-Neural-Network-Convolutional-Neural-Network-Models
2. **Install the required Python packages**:

- Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).
- It's recommended to create a virtual environment to keep dependencies required by different projects separate and to avoid conflicts:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
- Install the required packages:
  ```bash
  pip install tensorflow numpy matplotlib

3. **Proceed with project setup and usage as required**:
### Explanation:
- **Step 1**: Cloning the repository is straightforward; make sure to replace `spymavro` with your actual GitHub username.
- **Step 2**: This step covers:
  - Checking for Python installation.
  - Setting up a virtual environment, which is optional but recommended.
  - Direct installation of each required Python package using `pip`.

## Usage
- Navigate to the cloned directory in your terminal and execute the ANN and CNN models script by running:
  ```bash
  python ann_cnn.py 

## Contact
For any inquiries or collaboration requests, please reach out via GitHub or email at spyros.mauromatis@gmail.com.



