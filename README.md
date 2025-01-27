# Anomaly Detection Methods

This repository contains implementations of 6 anomaly detection methods for analyzing and detecting anomalies in various contexts, such as surveillance, transportation, and robotics. Each method is organized in its own folder with related code, models, and documentation.

## Dataset

- DroneAnomaly Foggy: https://doi.org/10.5281/zenodo.14601864
- UIT-ADrone Foggy:
    - Train: https://doi.org/10.5281/zenodo.14602739
    - Test: 
        - https://doi.org/10.5281/zenodo.14602883 (Part 1)
        - https://doi.org/10.5281/zenodo.14605746 (Part 2)
    

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
