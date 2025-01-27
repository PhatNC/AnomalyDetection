# Anomaly Detection Methods

This repository contains implementations of six anomaly detection methods for analyzing and detecting anomalies in various contexts, such as surveillance, transportation, and robotics. Each method is organized in its own folder with related code, models, and documentation.

## Folder Structure

The repository is organized as follows:

- **[ANDT](https://github.com/Jin-Pu/Drone-Anomaly)/**: Vision Transformer-based anomaly detection framework focusing on learning regular patterns in aerial video sequences. 
- **[ASTT](https://github.com/Tungufm/ASTT)/**: Future frame prediction using cross-self-attention mechanism for spatio-temporal representation in aerial traffic videos. 
- **[MNAD](https://github.com/cvlab-yonsei/MNAD)/**: Memorization-based normality and abnormality detection utilizing a memory module for recording prototypical patterns. 
- **[MLEP](https://github.com/svip-lab/MLEP)/**: Margin learning embedded prediction combining ConvLSTM and learning margin modules to differentiate between normal and abnormal events. 
- **[STD](https://github.com/ChangYunPeng/VideoAnomalyDetection)/**: Spatio-temporal dissociation framework separating spatial and temporal features for detecting abnormal events. 
- **[FFP](https://github.com/StevenLiuWen/ano_pred_cvpr2018)/**: Future frame prediction using U-Net for generative video frame prediction with optical flow estimation. 


Each folder contains the source code and necessary files to run the respective anomaly detection method.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or later
- Necessary dependencies (listed in `requirements.txt` if provided in each method folder)

You can install the dependencies for all methods using:
```bash
pip install -r requirements.txt
```

### Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Navigate to the folder of the method you wish to use:
   ```bash
   cd ANDT
   ```

3. Follow the specific instructions provided in the `README.md` or documentation file inside each method's folder.

## Usage

Each method has its own unique workflow. Navigate to the respective folder and follow the provided scripts or notebooks to train, evaluate, or test the model. For example:

- **Training**:
  ```bash
  python train.py
  ```

- **Evaluation**:
  ```bash
  python evaluate.py
  ```

## Methods Overview

1. **Future Frame Prediction (FFP)**:
   - Predicts the next video frame based on previous frames to detect anomalies.
   - Utilizes a modified U-Net for frame generation and optical flow estimation.

2. **Spatio-Temporal Dissociation (STD)**:
   - Separates spatial and temporal information to identify abnormal events.
   - Employs a spatial autoencoder for appearance modeling and a temporal module for motion detection.

3. **Memorization-Based Normality and Abnormality Detection (MNAD)**:
   - Leverages memory modules to store prototypical patterns of normal data.
   - Uses diversity and discrimination losses to enhance memory representation.

4. **Margin Learning Embedded Prediction (MLEP)**:
   - Combines ConvLSTM and a learning margin module to differentiate between normal and abnormal events.
   - Encodes spatio-temporal features for robust anomaly detection.

5. **Anomaly Detection using Transformers (ANDT)**:
   - A Vision Transformer-based framework that predicts anomalies using spatio-temporal representation.
   - Processes video sequences as tubelets and identifies anomalies during the testing phase.

6. **Attention-based Spatio-Temporal Transformer (ASTT)**:
   - Employs cross-self-attention in Vision Transformers to enhance anomaly detection.
   - Predicts future frames by leveraging self-attention mechanisms for improved accuracy.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.
