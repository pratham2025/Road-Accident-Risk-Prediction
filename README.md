## 🚦 Road Accident Risk Prediction — Kaggle Competition (Rank: 642)

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-ETL-150458?logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Kaggle-Participant-20BEFF?logo=kaggle&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

An end‑to‑end machine learning project to predict road accident risk/severity from tabular data. Built for a Kaggle competition — I participated and achieved a leaderboard rank of **642**. This repo is ready for GitHub with a clean structure, quickstart, and reproducible pipeline.

---

### Table of Contents
- [Overview](#overview)
- [Dataset & Competition](#dataset--competition)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Modeling](#modeling)
- [Results](#results)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

### Overview
This repository contains:
- Reproducible environment via `requirements.txt`
- Jupyter notebook for EDA, modeling, and ensembling
- Submission artifact ready to upload to Kaggle

Use the notebook for interactive EDA/experiments and the script for automated runs.

<details>
<summary><b>Why this problem matters</b></summary>

Predicting accident risk informs better infrastructure, enforcement, and triage decisions. Accurate models can guide resource allocation and potentially save lives.

</details>

---

### Dataset & Competition
- Platform: Kaggle (tabular prediction). I participated and secured **rank 642** on the leaderboard.
- Data files expected at project root:
  - `train.csv`
  - `test.csv`
  - `sample_submission.csv`
  - `submission.csv` (generated predictions; present in this repo after a run)

If you want, update this section with the exact competition link.

---

### Project Structure
```text
ROAD SAFETY PROJECT/
├─ venv/                               # local venv (optional)
├─ requirements.txt                    # dependencies
├─ roadacccident_ensemble.ipynb        # EDA, modeling, and ensemble experiments
├─ train.csv                           # Kaggle train (place here)
├─ test.csv                            # Kaggle test (place here)
├─ sample_submission.csv               # Kaggle sample format
└─ submission.csv                      # Generated predictions (ready to submit)
```

---

### Setup

1) Clone the repo
```bash
git clone <your-repo-url>
cd "ROAD SAFETY PROJECT"
```

2) Create and activate a virtual environment
- Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

- macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3) Install dependencies
```bash
pip install -r requirements.txt
```

4) Add data
Place `train.csv`, `test.csv`, and `sample_submission.csv` in the project root.

---

### Usage

Run the notebook:
```bash
jupyter notebook roadacccident_ensemble.ipynb
```

The notebook will guide you through preprocessing, training, validation, and predicting on the test set. Save the final predictions as `submission.csv` in the project root to upload on Kaggle.

<details>
<summary><b>Troubleshooting</b></summary>

- Ensure Python 3.10+ is used
- Verify CSV file names and paths
- Reinstall dependencies: `pip install -r requirements.txt`
- Clear and recreate the virtual environment if environment resolution fails

</details>

---

### Modeling

Core workflow (as reflected in the notebook and dependencies):
- Data cleaning and preprocessing with `pandas`
- Categorical encoding, missing value handling
- Strong tabular learners via `scikit-learn`, `LightGBM`, `XGBoost`, and `CatBoost`
- K‑fold cross‑validation for robust estimates
- Final fit on full train, then predict on test and save submission

Potential improvements (see Roadmap): gradient boosting (XGBoost/LightGBM/CatBoost), hyperparameter tuning, and model stacking/blending.

---

### Results
- Best public leaderboard rank: **642** (Kaggle)
- Submission format mirrors `sample_submission.csv`

To reproduce: follow [Setup](#setup) and [Usage](#usage), then submit the generated CSV on Kaggle.

---

### Roadmap
- Tighten feature engineering (domain-driven and interaction features)
- Hyperparameter tuning (Optuna)
- Feature selection and domain features
- Stacking/blending for leaderboard gains

---

### Contributing
Contributions are welcome! Please:
- Open an issue to discuss major changes
- Use clear commit messages
- Keep code readable and lint‑clean

---

### License
MIT — see the LICENSE file if present. Otherwise, feel free to use with attribution.


