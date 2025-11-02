## Introduction
This is a NLP project to analyze the semantic meaning of reviews/feedbacks provided by patients on respective drugs.

## Procedures
1. Import data as dataframe
2. Conduct EDA to understand the data and look for issues through visual charts or tables
   
   Issues discovered:
   1. Data type mismatch for dependent variable `rating`
   2. Class imbalance -> Positive class is overpopulated
4. Data preprocessing
   #### General
   1. Feature selection   
   2. Check for null values
   3. Compute class weight
   #### Dependent variable - 'rating' preprocessing
   1. Data type mismatch handling
   2. Label encoding
   #### Independent variable - 'review' text preprocessing
   1. Decontract
   2. Normalization
         1. Lowercasing
         2. URL removal
         3. Special character removal
   3. Stopwords removal - `NLTK`
   4. Lemmatization - `spaCy`
   5. Tokenization - `spaCy`
   6. Vectorization - `TfidfVectorizer`
5. Save the variables, otherwise every time refreshing the kernel will lose the variables and take time to run through the preprocessing code
6. Modeling
   1. Traditional ML models
      1. LogisticRegression
      2. LinearSVC
      3. RandomForestClassifier
      4. MultinomialNB
      5. XGClassifier
   2. Deep learning model
      
      BiLSTM RNN
