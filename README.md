# 🐶 Image Classification for a City Dog Show

## 📌 Project Overview

This project is an **image classification application developed in Python** as part of the Udacity **AI Programming with Python / Image Classification for a City Dog Show** project.

The application uses **pre-trained Convolutional Neural Networks (CNNs)** to analyze images of pets and determine:

1. Whether an image contains a **dog or another type of pet**.
2. If the image contains a dog, which **dog breed** it most closely resembles.
3. Which CNN architecture performs best for the required classification tasks.

The project evaluates three different pre-trained CNN architectures:

* **VGG**
* **AlexNet**
* **ResNet**

The application compares the predictions from the CNN models with the actual pet labels obtained from the image filenames and calculates performance statistics.

---

## 🎯 Project Objectives

The main objectives of this project are:

### Objective 1 — Identify Dogs

Correctly determine whether each pet image contains:

* A dog
* A non-dog

The application must correctly identify dogs even when the predicted breed is incorrect.

### Objective 2 — Classify Dog Breeds

For images identified as dogs, determine whether the CNN correctly predicts the dog's breed.

### Objective 3 — Compare CNN Architectures

Compare the performance of:

* VGG
* AlexNet
* ResNet

The models are evaluated based on their ability to:

* Correctly identify dogs
* Correctly identify non-dogs
* Correctly classify dog breeds
* Execute efficiently

### Objective 4 — Analyze Model Performance

Use the calculated statistics to determine which CNN architecture is most suitable for the classification task.

---

# 🧠 How the Project Works

The project follows a multi-step image-classification pipeline.

```text
Pet Images
    │
    ▼
Extract Pet Labels
    │
    ▼
Classify Images Using CNN
    │
    ▼
Compare Predicted Labels
    │
    ▼
Determine Dog / Not-Dog
    │
    ▼
Calculate Statistics
    │
    ▼
Display Results
```

---

# 🔄 Project Pipeline

## Step 1 — Process Command-Line Arguments

The application accepts command-line arguments that specify:

* The directory containing pet images
* The CNN architecture to use
* The file containing valid dog breed names

Example:

```bash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

The available CNN architectures are:

```text
vgg
alexnet
resnet
```

---

## Step 2 — Extract Pet Labels

The `get_pet_labels.py` module examines the filenames of images in the `pet_images/` directory.

The filenames contain the actual pet names.

For example:

```text
Dalmatian_04017.jpg
Great_dane_05320.jpg
```

are converted into labels such as:

```text
dalmatian
great dane
```

The information is stored in a dictionary called `results_dic`.

Example structure:

```python
results_dic = {
    "Dalmatian_04017.jpg": ["dalmatian"],
    "Great_dane_05320.jpg": ["great dane"]
}
```

This dictionary is used throughout the rest of the application.

---

# 🤖 Step 3 — Classify Images

The `classify_images.py` module uses the selected CNN architecture to classify each image.

The project uses the `classifier.py` module to access the pre-trained models.

The available models are:

### VGG

```text
vgg
```

### AlexNet

```text
alexnet
```

### ResNet

```text
resnet
```

The CNN produces a predicted class label for every image.

The predicted label is then stored in `results_dic`.

The dictionary is updated to contain information similar to:

```python
results_dic = {
    "Dalmatian_04017.jpg": [
        "dalmatian",
        "dalmatian",
        1
    ]
}
```

Where:

```text
Index 0 → Actual pet label
Index 1 → CNN predicted label
Index 2 → Whether the labels match
```

---

# 🐕 Step 4 — Determine Dog or Not-Dog

The `adjust_results4_isadog.py` module determines whether:

* The actual image label represents a dog breed.
* The CNN prediction represents a dog breed.

The project uses `dognames.txt`, which contains the list of recognized dog breeds.

The results dictionary is extended with dog/not-dog information.

For example:

```python
results_dic = {
    "Dalmatian_04017.jpg": [
        "dalmatian",
        "dalmatian",
        1,
        1,
        1
    ]
}
```

The values represent:

```text
Actual Label
Predicted Label
Label Match
Actual Is Dog
Predicted Is Dog
```

This allows the project to distinguish between:

* Correct dog identification
* Incorrect dog identification
* Correct non-dog identification
* Incorrect non-dog identification

---

# 📊 Step 5 — Calculate Statistics

The `calculates_results_stats.py` module calculates the performance statistics of the selected CNN model.

The statistics include:

* Total number of images
* Number of correctly classified images
* Percentage of correctly classified images
* Number of dogs correctly identified
* Percentage of dogs correctly identified
* Number of non-dogs correctly identified
* Percentage of non-dogs correctly identified
* Number of correctly classified dog breeds
* Percentage of correctly classified dog breeds

These statistics make it possible to compare the three CNN architectures.

---

# 🖨️ Step 6 — Display Results

The `print_results.py` module displays the final results.

The output includes:

* Number of images processed
* Dog classification accuracy
* Non-dog classification accuracy
* Dog breed classification accuracy
* Runtime information
* Model performance

This provides a clear summary of how well the selected CNN architecture performed.

---

# 🧪 Step 7 — Testing

The project includes:

```text
test_classifier.py
```

This file can be used to test the image classifier and verify that the classifier is working correctly.

The project also contains:

```text
check_images.py
```

which provides the main interface for running the complete image-classification pipeline.

---

# 🏗️ Project Structure

```text
Image-Classification-for-a-City-Dog-Show/
│
├── data/
│   │
│   ├── pet_images/
│   │   └── *.jpg
│   │
│   ├── uploaded_images/
│   │   └── test images
│   │
│   ├── adjust_results4_isadog.py
│   ├── calculates_results_stats.py
│   ├── check_images.py
│   ├── classifier.py
│   ├── classify_images.py
│   ├── dognames.txt
│   ├── get_input_args.py
│   ├── get_pet_labels.py
│   ├── imagenet1000_clsid_to_human.txt
│   ├── print_functions_for_lab_checks.py
│   ├── print_results.py
│   ├── test_classifier.py
│   └── run_models_batch.sh
│
└── README.md
```

---

# 📁 Important Files

| File                          | Purpose                                                       |
| ----------------------------- | ------------------------------------------------------------- |
| `check_images.py`             | Main program that runs the image-classification pipeline      |
| `get_input_args.py`           | Handles command-line arguments                                |
| `get_pet_labels.py`           | Extracts actual pet labels from image filenames               |
| `classifier.py`               | Provides access to the pre-trained CNN models                 |
| `classify_images.py`          | Classifies images using the selected CNN                      |
| `adjust_results4_isadog.py`   | Determines whether actual and predicted labels represent dogs |
| `calculates_results_stats.py` | Calculates classification statistics                          |
| `print_results.py`            | Displays the final results                                    |
| `dognames.txt`                | Contains the list of recognized dog breeds                    |
| `test_classifier.py`          | Tests the image classifier                                    |
| `run_models_batch.sh`         | Runs the project using multiple CNN architectures             |

---

# 💻 Technologies Used

The project was developed using:

* **Python 3**
* **PyTorch**
* **Torchvision**
* **Pre-trained CNN models**
* **VGG**
* **AlexNet**
* **ResNet**
* **Command-line interfaces**
* **Dictionary-based data structures**
* **File and directory processing**

### Python Concepts Used

This project also demonstrates practical Python programming concepts including:

* Functions
* Dictionaries
* Lists
* Loops
* Conditional statements
* File handling
* Exception handling
* Command-line arguments
* Modules
* Import statements
* String manipulation
* Data processing

---

# 🧠 CNN Models

## VGG

VGG is a deep convolutional neural network architecture known for its strong image-recognition performance.

In this project, VGG achieved the **strongest dog-breed classification performance** among the evaluated architectures.

---

## AlexNet

AlexNet is an influential CNN architecture that significantly advanced image classification using deep learning.

It provides relatively fast classification while producing lower breed-classification accuracy compared with VGG.

---

## ResNet

ResNet, or Residual Network, uses residual connections to make it possible to train very deep neural networks effectively.

In this project, ResNet demonstrated very strong dog/not-dog identification performance.

According to the project evaluation, ResNet correctly identified all dog images while making one dog/not-dog error on a non-dog image.

---

# 📈 Model Comparison

The project demonstrates an important trade-off between classification accuracy and execution time.

| Model       | Dog Identification | Breed Classification    | Runtime     |
| ----------- | ------------------ | ----------------------- | ----------- |
| **VGG**     | Strong             | **Best breed accuracy** | Longer      |
| **AlexNet** | Good               | Lower                   | **Shorter** |
| **ResNet**  | **Excellent**      | Strong                  | Moderate    |

### General Interpretation

**VGG**

Best choice when the primary objective is accurate dog-breed classification.

**AlexNet**

Useful when faster execution is more important and slightly lower classification accuracy is acceptable.

**ResNet**

Strong choice when correctly identifying dogs versus non-dogs is the primary requirement.

Therefore, there is no single model that is automatically the best for every application. The best architecture depends on the requirements of the application.

---

# 📊 Results

The project was tested using the standard **40-image pet dataset**.

The submitted implementation successfully passed the required project checks.

The evaluation confirmed that:

* The standard 40-image dataset is processed correctly.
* Command-line argument defaults meet the project requirements.
* Pet labels are generated in the expected format.
* CNN predictions are stored correctly.
* Dog/not-dog status is assigned consistently.
* VGG, AlexNet, and ResNet produce the expected benchmark behavior.
* The overall statistics are calculated correctly.

The evaluation also demonstrated the expected differences between the models:

* **VGG** achieved the strongest breed-classification performance.
* **AlexNet** provided a shorter runtime but lower breed accuracy.
* **ResNet** correctly identified all dog images but made one dog/not-dog error on a non-dog image.

---

# ▶️ How to Run the Project

## 1. Clone the Repository

Clone the project repository to your computer.

```bash
git clone <your-repository-url>
```

Then navigate to the project directory:

```bash
cd <project-directory>
```

---

## 2. Install Dependencies

Make sure Python 3 is installed.

Install the required libraries:

```bash
pip install torch torchvision
```

Depending on your environment, additional dependencies may be required.

---

# 🚀 Running the Program

The main program is:

```text
check_images.py
```

It accepts three main command-line arguments:

```text
--dir
--arch
--dogfile
```

---

## Run with VGG

```bash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

---

## Run with AlexNet

```bash
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt
```

---

## Run with ResNet

```bash
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt
```

---

# ⚙️ Command-Line Arguments

### `--dir`

Specifies the directory containing the pet images.

Example:

```bash
--dir pet_images/
```

The required default value is:

```text
pet_images/
```

---

### `--arch`

Specifies which CNN architecture should be used.

Available options:

```text
vgg
alexnet
resnet
```

Example:

```bash
--arch vgg
```

---

### `--dogfile`

Specifies the file containing the recognized dog breed names.

Example:

```bash
--dogfile dognames.txt
```

---

# 🧪 Running All Three Models

The project includes a batch script that can be used to run the models.

```bash
bash run_models_batch.sh
```

This allows the results of VGG, AlexNet, and ResNet to be compared.

---

# 📷 Input Data

The standard dataset contains **40 pet images**.

The images include:

* Dogs
* Non-dogs
* Different dog breeds

The actual breed or pet label is obtained from each filename.

For example:

```text
Boston_terrier_02259.jpg
```

produces the label:

```text
boston terrier
```

---

# 📝 Example Classification

Suppose an image has the filename:

```text
Dalmatian_04017.jpg
```

The program extracts:

```text
Actual Label: dalmatian
```

The CNN might produce:

```text
Predicted Label: dalmatian
```

The application then determines:

```text
Label Match: True
Actual Is Dog: True
Predicted Is Dog: True
```

This represents a correctly identified dog and correctly classified breed.

---

# ❌ Example of a Classification Error

Suppose the actual image is:

```text
Golden_retriever_001.jpg
```

but the CNN predicts:

```text
Labrador_retriever
```

The program can determine:

```text
Actual Is Dog: True
Predicted Is Dog: True
```

Even though the breed is incorrect, the model correctly identified that the image contains a dog.

This distinction is important because the project has **two separate classification objectives**:

1. Dog vs. non-dog classification
2. Dog-breed classification

---

# 📊 Understanding the Evaluation

The project evaluates the models using several types of accuracy.

### Overall Classification

Measures whether the predicted label matches the actual label.

### Dog Classification

Measures how accurately the model determines whether an image contains a dog.

### Non-Dog Classification

Measures how accurately the model identifies images that do not contain dogs.

### Breed Classification

Measures how accurately the model identifies the correct dog breed.

These measurements provide more useful information than looking at a single overall accuracy value.

---

# 🔍 Key Learning Outcomes

Through this project, I gained practical experience with:

### Python Programming

* Building functions
* Working with dictionaries
* Processing files
* Handling command-line arguments
* Creating reusable modules

### Machine Learning

* Using pre-trained models
* Understanding image classification
* Comparing model architectures
* Evaluating model performance

### Deep Learning

I gained practical exposure to:

* Convolutional Neural Networks
* Image classification
* Transfer learning
* Pre-trained neural networks
* Model prediction

### Software Development

The project also helped strengthen:

* Debugging
* Code organization
* Testing
* Git/GitHub workflow
* Command-line execution
* Documentation

---

# 💡 Key Insights

One of the most important lessons from this project is that **the best model depends on the application's requirements**.

For example:

```text
If breed accuracy is most important
        ↓
      VGG
```

```text
If execution speed is most important
        ↓
    AlexNet
```

```text
If dog/not-dog identification is most important
        ↓
     ResNet
```

Model evaluation should therefore consider different types of errors instead of relying only on one aggregate accuracy score.

---

# 🚧 Possible Future Improvements

The project could be extended in several ways.

### 1. Improve Error Analysis

Separate errors into categories such as:

* Dog incorrectly classified as non-dog
* Non-dog incorrectly classified as dog
* Dog correctly identified but wrong breed
* Correct breed classification

This would provide a deeper understanding of model weaknesses.

### 2. Add a Graphical User Interface

A GUI could allow users to:

1. Upload an image.
2. Select a CNN model.
3. Run classification.
4. Display the predicted breed.
5. Display confidence information.
---

# 🧑‍💻 Author

**Orapeleng Timothy Madibela**

Interests include:

* Software Development
* Data Science
* Artificial Intelligence
* Machine Learning
* Cybersecurity
* Web Development

---

# 📚 Project Context

This project was completed as part of the **Udacity Future AWS AI Programmer**.

The project focuses primarily on applying Python programming skills to an existing image-classification system and evaluating pre-trained CNN architectures.

---

# ⭐ Conclusion

The Image Classification for a City Dog Show project demonstrates how pre-trained deep-learning models can be used to classify pet images and identify dog breeds.

The complete pipeline:

```text
Input Images
     ↓
Extract Labels
     ↓
CNN Classification
     ↓
Dog / Not-Dog Detection
     ↓
Compare Predictions
     ↓
Calculate Statistics
     ↓
Evaluate Models
```

The project successfully demonstrates the use of **VGG, AlexNet, and ResNet** for image classification and highlights the trade-offs between accuracy, breed classification, dog identification, and execution time.

The results show that **VGG is particularly strong for breed classification, AlexNet provides faster execution, and ResNet performs strongly for dog/not-dog identification**.

This project provided practical experience in Python programming, machine learning, deep learning, model evaluation, testing, and software documentation.
