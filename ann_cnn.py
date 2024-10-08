# -*- coding: utf-8 -*-
"""ann_cnn.py
"""

# 1 Artificial Neural Networks and Convolutional Neural Networks
# 1.2 Tasks

# 1. Load Dataset

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np

# Set a seed
np.random.seed(0)

# Load the MNIST dataset using Keras
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the dataset values from [0, 255] to [0, 1]
x_train = x_train / 255.0
x_test = x_test / 255.0

# 2. Artificial Neural Network (ANN)

# Flatten the images to shape (-1, 784)
x_train_ann = x_train.reshape((-1, 784))
x_test_ann = x_test.reshape((-1, 784))

# Convert labels to one-hot encoding
y_train_ann = to_categorical(y_train, 10)
y_test_ann = to_categorical(y_test, 10)

# Define the model architecture
model_ann = Sequential([
    Dense(256, activation='relu', input_shape=(784,)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model_ann.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model with validation split
history_ann = model_ann.fit(x_train_ann, y_train_ann, epochs=10, validation_split=0.1, batch_size=32)

# Evaluate the model on the test set
test_loss_ann, test_acc_ann = model_ann.evaluate(x_test_ann, y_test_ann)

# 3. Convolutional Neural Network (CNN)

# Reshape the images to shape (-1, 28, 28, 1) for CNN
x_train_cnn = x_train.reshape((-1, 28, 28, 1))
x_test_cnn = x_test.reshape((-1, 28, 28, 1))

# Convert labels to one-hot encoding
y_train_cnn = to_categorical(y_train, 10)
y_test_cnn = to_categorical(y_test, 10)

# Define the CNN model architecture
model_cnn = Sequential([
    Conv2D(64, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    Conv2D(32, kernel_size=(3, 3), activation='relu'),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model_cnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model with validation split
history_cnn = model_cnn.fit(x_train_cnn, y_train_cnn, epochs=10, validation_split=0.1, batch_size=32)

# Evaluate the model on the test set
test_loss_cnn, test_acc_cnn = model_cnn.evaluate(x_test_cnn, y_test_cnn)

# 4. Loss/Accuracy

# Plotting Accuracy and Loss using the provided function
def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.ylabel(train)
    plt.xlabel('Epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()

# Plot training/validation accuracy and loss for ANN
show_train_history(history_ann, 'accuracy', 'val_accuracy')
show_train_history(history_ann, 'loss', 'val_loss')

# Plot training/validation accuracy and loss for CNN
show_train_history(history_cnn, 'accuracy', 'val_accuracy')
show_train_history(history_cnn, 'loss', 'val_loss')

# 5. Evaluate the results

# Predictions for the test set
y_pred_ann = model_ann.predict(x_test_ann)
y_pred_cnn = model_cnn.predict(x_test_cnn)

# Convert predictions to class labels
y_pred_ann_classes = y_pred_ann.argmax(axis=-1)
y_pred_cnn_classes = y_pred_cnn.argmax(axis=-1)

# Ensure `y_test` is directly used as class labels
y_test_classes = y_test

# Confusion Matrix for ANN
conf_matrix_ann = confusion_matrix(y_test_classes, y_pred_ann_classes)
ConfusionMatrixDisplay(conf_matrix_ann).plot()
plt.title("Confusion Matrix - ANN")
plt.show()

# Confusion Matrix for CNN
conf_matrix_cnn = confusion_matrix(y_test_classes, y_pred_cnn_classes)
ConfusionMatrixDisplay(conf_matrix_cnn).plot()
plt.title("Confusion Matrix - CNN")
plt.show()

# Comparison
print(f"ANN Test Accuracy: {test_acc_ann}")
print(f"CNN Test Accuracy: {test_acc_cnn}")

# Bonus

# New CNN with Max Pooling after each Convolutional Layer
# Define the new CNN model architecture with additional pooling
model_cnn_pool = Sequential([
    Conv2D(64, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(32, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model_cnn_pool.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model with validation split
history_cnn_pool = model_cnn_pool.fit(x_train_cnn, y_train_cnn, epochs=10, validation_split=0.1, batch_size=32)

# Evaluate the model on the test set
test_loss_cnn_pool, test_acc_cnn_pool = model_cnn_pool.evaluate(x_test_cnn, y_test_cnn)

# Loss/Accuracy for the new CNN model

# Plot training/validation accuracy and loss for the new CNN with pooling
show_train_history(history_cnn_pool, 'accuracy', 'val_accuracy')
show_train_history(history_cnn_pool, 'loss', 'val_loss')

# Evaluate the results for the new CNN model

# Predictions for the test set
y_pred_cnn_pool = model_cnn_pool.predict(x_test_cnn)

# Convert predictions to class labels
y_pred_cnn_pool_classes = y_pred_cnn_pool.argmax(axis=-1)

# Confusion Matrix for the new CNN with pooling
conf_matrix_cnn_pool = confusion_matrix(y_test_classes, y_pred_cnn_pool_classes)
ConfusionMatrixDisplay(conf_matrix_cnn_pool).plot()
plt.title("Confusion Matrix - CNN with Pooling")
plt.show()

# Comparison
print(f"CNN with Pooling Test Accuracy: {test_acc_cnn_pool}")
