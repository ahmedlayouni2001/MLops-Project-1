#  MLOps-Project-1

## Project Objective
Forecast hourly temperature and precipitation using:
- 3 statistical models
- 1 ML model (to analyze its limitations for time series)
- 5 DL models

Using climate data API from 2020 to June 2025 (temperature and precipitation).

## Structure
- `data/`: raw and  processed data
- `notebooks/`: Jupyter notebooks for data collection, EDA, modeling, and evaluation.
- `models/`: saved models (statistical, ML, DL).
- `src/`: reusable scripts for ingestion, preprocessing, and training.
- `reports/`: figures and automated EDA reports.

## Tools
- Python 3.11 (via Anaconda)
- pandas, numpy, matplotlib, seaborn
- scikit-learn, statsmodels
- tensorflow, pytorch
- mlflow for experiment tracking
  
## Summary about All The Models
This project implements an end-to-end MLOps pipeline for hourly temperature forecasting (t2m) over Sfax, using real climate data from 2020 to mid-2025. We structured the workflow to ensure clean versioning, reproducibility, and scalable experimentation.
We evaluated statistical models (ARIMA, ETS, Prophet), machine learning models (XGBoost, Random Forest), and deep learning models (LSTM, GRU, CNN, Transformer) for forecasting performance. Results demonstrate that deep learning models (GRU, CNN) and machine learning models (XGBoost, Random Forest) outperform statistical baselines significantly, achieving lower MAE and RMSE by effectively capturing complex patterns in hourly data. The pipeline is designed to be modular, with environment tracking, systematic model evaluation, and clear progression toward automated, scalable forecasting deployment.
This repository serves as a practical foundation for building scalable weather forecasting pipelines and learning structured MLOps workflows with real data.


