🚨 Job Fraud Detection using Machine Learning (NLP)

📌 Problem Statement

   Online job portals are increasingly affected by fraudulent job postings that mislead candidates through fake promises, vague descriptions, and scam-driven       language.
   
   The objective of this project is to detect fraudulent job postings using machine learning by analyzing job descriptions and related text data.
   Key challenge: Severe class imbalance and higher cost of missing fraudulent jobs compared to false alarms.

📊 Dataset

Source: Fake Job Postings dataset
Total records: ~18,000+

Target variable:

0 → Genuine job

1 → Fraudulent job

Class distribution:

Genuine: ~95%

Fraudulent: ~5% (highly imbalanced)

Key Features Used

Job title

Location

Company profile

Job description

Requirements

Benefits

All text fields were combined into a single feature for NLP processing.

🛠️ Approach & Methodology

1. Data Preprocessing

Removed non-informative columns (IDs, sparse flags)

Handled missing values by replacing with empty strings

Combined multiple text columns into a single corpus per job posting

2. Feature Engineering

TF-IDF Vectorization

Unigrams + bigrams

Stopword removal

Sublinear term frequency scaling

This helps capture scam-related phrases rather than isolated words.

🤖 Model Selection

Logistic Regression

Chosen for interpretability and robustness

Applied class_weight='balanced' to handle class imbalance

Random Forest was tested but Logistic Regression was preferred due to:

Better control over precision–recall tradeoff

Easier interpretability for fraud detection

⚖️ Handling Class Imbalance

Due to a 95:5 imbalance, accuracy alone was misleading.

The focus was shifted to:

Recall (Fraud class)

F1-score

Precision-Recall tradeoff

🎯 Threshold Tuning

Instead of using the default 0.5 probability threshold, multiple thresholds were evaluated.

Threshold	Fraud Precision	Fraud Recall

0.5	0.92	0.89

0.4	0.78	0.92

0.3 (Selected)	0.62	0.95

✔ Final threshold chosen: 0.3, prioritizing fraud recall while maintaining acceptable precision.

📈 Model Performance (Final)

Fraud Recall: 95%

Fraud Precision: 62%

Fraud F1-Score: 0.75

Missed fraud cases: Very low (8 out of 173)

This aligns with real-world fraud detection systems where false negatives are more costly than false positives.

🔍 Model Interpretability

Logistic Regression coefficients were analyzed to identify keywords strongly associated with fraudulent postings.

Common Fraud Indicators

“work from home”

“no experience required”

“training provided”

“quick income”

“part time job”

These patterns reflect vague promises, urgency, and minimal qualification requirements—common traits of job scams.

A bar-chart visualization of top fraud keywords is included in the notebook.

🧠 Key Learnings

Accuracy is not suitable for imbalanced fraud problems

Class weighting and threshold tuning significantly improve recall

Interpretability is crucial for trust in ML-driven fraud systems

NLP models can effectively capture scam-specific language patterns

🚀 Future Improvements

  Use SMOTE or other resampling techniques
  
  Experiment with Linear SVM or Gradient Boosting
  
  Deploy as an API for real-time job screening
  
  Add explainability using SHAP for deeper insights

📌 Conclusion

This project demonstrates a business-driven ML approach to fraud detection, emphasizing recall, interpretability, and risk-aware decision making.

The final model successfully identifies fraudulent job postings while maintaining practical precision, making it suitable for real-world deployment scenarios.
