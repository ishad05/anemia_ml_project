# Anemia Subtype Classification Using Machine Learning

This project presents a machine learning system for automated classification of anemia subtypes using routine Complete Blood Count (CBC) parameters. The objective is to support early clinical screening by providing an accurate, data-driven anemia subtype prediction model.

---

## Problem Statement

Anemia is a widespread hematological disorder with multiple subtypes that require different treatment strategies. However, subtype identification is often delayed due to limited access to specialized diagnostic tests.

This project aims to classify patients into the following categories using only CBC data:

- Normal
- Iron Deficiency Anemia
- Thalassemia

By leveraging machine learning, the system provides a low-cost, rapid, and automated decision support tool.

---

## Dataset and Features

The model is trained using standard CBC parameters along with a clinically important derived feature.

### Input Features

- RBC – Red Blood Cell Count  
- PCV – Packed Cell Volume  
- MCV – Mean Corpuscular Volume  
- MCH – Mean Corpuscular Hemoglobin  
- MCHC – Mean Corpuscular Hemoglobin Concentration  
- RDW – Red Cell Distribution Width  
- TLC – Total Leukocyte Count  
- PLT /mm3 – Platelet Count  
- HGB – Hemoglobin  
- Mentzer Index (MCV / RBC)

The Mentzer Index is clinically used to differentiate Iron Deficiency Anemia and Thalassemia.

---

## Methodology

1. Data cleaning and preprocessing  
2. Feature engineering (Mentzer Index)  
3. Handling class imbalance using SMOTE  
4. Model training using Random Forest Classifier  
5. Hyperparameter tuning and validation  
6. Model evaluation using test set and cross-validation  

---

## Model Performance

The trained Random Forest model achieved:

- Test Accuracy: 95%  
- Macro F1-score: 0.95  
- Mean 5-Fold Cross-Validation F1-macro Score: 0.94  

These results indicate strong generalization and class-balanced performance.

---

## Web Application

A Streamlit-based web application is developed to allow real-time prediction. Users can input CBC values and receive:

- Predicted anemia subtype  
- Probability distribution across all classes  

This demonstrates the model’s applicability in real-world clinical screening scenarios.

---

## Project Structure
