# Biomedical Malignancy Detection using KNN

An end-to-end machine learning pipeline designed to automate the classification of breast tumors as Malignant (0) or Benign (1) utilizing the K-Nearest Neighbors (KNN) algorithm. This repository demonstrates clean data engineering workflows, feature selection, and model evaluation on clinical diagnostic datasets.

---

### Pipeline Architecture and Workflow

- Data Engineering: Maps raw categorical diagnostics ('M' / 'B') into numerical binary classes (0 and 1) and handles missing data via programmatic zero-filling.
- Feature Selection: Eliminates redundant identifiers like the ID column to reduce dimensionality and isolate the feature matrix from the target vector.
- Predictive Modeling: Implements a Scikit-Learn KNeighborsClassifier validated over an 80/20 train-test distribution.
- Analytical Visualization: Computes model evaluation metrics and programmatically renders diagnostic accuracy plots via Matplotlib.

---

### Tech Stack and Frameworks

- Core Language: Python
- Data Wrangling: Pandas
- Machine Learning: Scikit-Learn
- Data Visualization: Matplotlib

---

### Model Evaluation Summary

- Test Dataset Split: 20% Unseen Testing Data (x_test, y_test)
- Classification Performance: The K-Nearest Neighbors pipeline achieved a validated accuracy score of 95.0%
- Visual Verification: Performance metrics are programmatically exported using a Matplotlib bar chart configuration.

---

### Developer Profile and Contact

Anlin Shaiju
Email: anlinshaiju24@gmail.com
LinkedIn: www.linkedin.com/in/anlin-shaiju-630729390
GitHub: https://github.com/anlinshaiju24-afk

- Academic Background: 
          Second-Year Bachelor of Technology (B.Tech) Student
          Department of Artificial Intelligence and Data Science Engineering
          APJ Abdul Kalam Technological University (KTU)

- Technical Interests: 
            Data science pipelines
            Python automation
            Cybersecurity frameworks

