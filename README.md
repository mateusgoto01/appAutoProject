# appAutoProject

![alt text]([https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.actu-environnement.com%2Fae%2Fnews%2Fdata-scientist-profils-divers-passion-necessaire-43173.php4&psig=AOvVaw3Jj6CBwqmI2GGnjqQlyxxW&ust=1729887040285000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCODMp8npp4kDFQAAAAAdAAAAABAE](https://www.actu-environnement.com/images/illustrations/news/43173_large.jpg)])

This project performs analysis, preprocessing, and predictive modeling on a weld quality dataset. It walks through steps from exploratory data analysis (EDA) to applying machine learning techniques, including semi-supervised learning, to predict weld quality.

## Table of Contents
- [Project Structure](#project-structure)
  - [1_FirstEDA.ipynb](#1_firstedaipynb)
  - [2_DataPreprocessing.ipynb](#2_datapreprocessingipynb)
  - [3_WeldQualityPrediction.ipynb](#3_weldqualitypredictionipynb)
  - [4_SemiSupervisedLearning.ipynb](#4_semisupervisedlearningipynb)
- [Dataset](#dataset)

## Project Structure

### 1_FirstEDA.ipynb
This notebook performs the initial exploratory data analysis (EDA) on the weld quality dataset. It examines the structure of the data, visualizes distributions, and identifies any patterns or correlations that might be useful for modeling.

### 2_DataPreprocessing.ipynb
In this notebook, data preprocessing steps are performed, including handling missing values, feature scaling, and transformations. The preprocessing ensures that the dataset is ready for machine learning models.

### 3_WeldQualityPrediction.ipynb
This notebook applies various supervised learning models such as Random Forest and SVM to predict weld quality. It includes steps for training, testing, and evaluating the performance of the models.

### 4_SemiSupervisedLearning.ipynb
Here, semi-supervised learning techniques are applied, leveraging both labeled and unlabeled data to improve the predictive performance of the model. This method is useful for cases where labeled data is scarce.

## Dataset

- **welddb.data**: The main dataset used for the analysis and modeling.
- **welddb.info**: Metadata about the dataset.
- **welddb.tex**: Additional references related to the dataset.
