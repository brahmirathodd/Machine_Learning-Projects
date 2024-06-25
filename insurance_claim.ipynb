    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import MinMaxScaler

Exploratory Data Analysis

    # Step 1: Read the dataset and basic dataframe exploration
    df = pd.read_csv('insurance_data.csv')

    print("Step 1: Basic DataFrame Exploration")

    Step 1: Basic DataFrame Exploration

    df.head()

  
    # observations:
    # there are a mix of numeric and category columns.
    # there are missing values
    # label column is claim

    df.shape



    # ML models require examples i.e. rows. A good thumb rule to use is 100 rows per column. Our dataset fits that.

    df.dtypes


    # some columns require encoding as they are categorical

    print(df.columns)

    Index(['index', 'PatientID', 'age', 'gender', 'bmi', 'bloodpressure',
           'diabetic', 'children', 'smoker', 'region', 'claim'],
          dtype='object')

    # Step 2: Summary statistics of numeric columns

    print("\nStep 2: Summary Statistics of Numeric Columns")
    df.describe()


    Step 2: Summary Statistics of Numeric Columns


    # 1340 rows in the dataset. Age has 5 missing values.
    # claim column has wide range. may have outliers.

    # Step 3: Value counts of category columns

    # include one for each column:
    df.gender.value_counts()

    df.diabetic.value_counts()

    df.smoker.value_counts()


    # Step 4: Data Visualization

    # Univariate Histogram
    plt.figure(figsize=(8, 5))
    sns.histplot(df['age'], bins=20, kde=True)
    plt.title('Histogram of Age')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

[]

    # Univariate Histogram
    plt.figure(figsize=(8, 5))
    sns.histplot(df['claim'], bins=20, kde=True)
    plt.title('Histogram of claim')
    plt.xlabel('claim')
    plt.ylabel('Frequency')
    plt.show()

[]

    # Univariate Pie Chart
    plt.figure(figsize=(8, 5))
    df['region'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('pastel'))
    plt.title('Pie Chart of Regions')
    plt.ylabel('')
    plt.show()

[]

    # Univariate Box Plot
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df['bmi'])
    plt.title('Box Plot of BMI')
    plt.xlabel('BMI')
    plt.show()

[]

    # shows some outliers in BMI column

    # Univariate Box Plot
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df['claim'])
    plt.title('Box Plot of claim')
    plt.xlabel('claim')
    plt.show()

[]

    # Bivariate Line Plot
    sns.lineplot(x='age', y='claim', data=df, errorbar=None)



[]

    sns.scatterplot(x='bmi', y='claim', data=df)



[]

    # Bivariate Scatter Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='bmi', y='claim', hue='smoker', data=df)
    plt.title('Scatter Plot of Claim vs BMI (colored by Smoker)')
    plt.xlabel('BMI')
    plt.ylabel('Claim')
    plt.legend(title='Smoker')
    plt.show()

[]

    # Step 5: Observations from data visualization
    # - There are ID columns which need to be removed
    # - There are missing values that require rows to be dropped
    # - Outliers require rows to be trimmed
    # - Age seems to have a normal distribution with most values clustered around the mean.
    # - Region is categorical with four distinct values, and the proportions are relatively balanced.
    # - BMI shows some outliers towards the higher end of the distribution.
    # - Claim amount is positively correlated with age but seems to have a wider spread for smokers.

Data Preprocessing

    # Step 1: Remove ID columns - index and PatientID
    df = df.drop(columns=['index', 'PatientID'])

    df.shape


    # Step 2: Remove rows with missing values
    df = df.dropna()

    df.shape

    # Step 3: Split numeric columns into X
    X = df.drop('claim', axis=1)
    X_num = X.select_dtypes(include=['int64', 'float64'])

    # outlier filter

    # get thresholds for outlier
    Q1 = X_num.quantile(0.25)
    Q3 = X_num.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Construct the outlier filter for X_num
    outlier_filter = ~((X_num < lower_bound) | (X_num > upper_bound)).any(axis=1)

    # Remove outliers from 'df' using this filter
    df = df[outlier_filter]  # Remove rows with outliers from 'df'

    # From the outlier trimmed df, fetch label, numeric features and category features for further processing
    # notice the order of these lines
    y = df['claim']
    X = df.drop('claim', axis=1)
    X_num = X.select_dtypes(include=['int64', 'float64'])
    X_cat = df.select_dtypes(include=['object'])

    X_num.shape, X_cat.shape


    # Step 4: Rescale numeric columns (optional, based on the algorithm used)
    scaler = MinMaxScaler()
    X_num_scaled = scaler.fit_transform(X_num)
    # Convert the scaled numpy array back to a DataFrame
    X_num_scaled = pd.DataFrame(X_num_scaled, columns=X_num.columns, index=X_num.index)

    # alt way of achieving the same result as the previous cell. here we create a copy of X_num and overwrite it with scaled values
    # what is happening is the index i.e. row IDs are retained implicitly versus in the above cell we are handling that explicitly.

    #X_num_scaled = X_num.copy()
    #scaler = MinMaxScaler()
    #X_num_scaled[X_num.columns] = scaler.fit_transform(X_num)

    # Step 5: One-hot encode category columns
    X_cat_encoded = pd.get_dummies(X_cat, drop_first=False, dtype=int)  # Drop_first to avoid multicollinearity

    # Step 6: Merge df_num and df_cat_encoded into X
    X = pd.concat([X_num_scaled, X_cat_encoded], axis=1)

    X.shape

    # Step 7: Check for NA in X and y; Check for shape compatibility
    print("\nStep 7: Checking for NAs and Shape Compatibility")
    print(X.isnull().sum())
    print(y.isnull().sum())
    print(X.shape)
    print(y.shape)


    Step 7: Checking for NAs and Shape Compatibility
  

    X.describe()


    # Step 8: Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print(X_train.shape)
    print(X_test.shape)
    print(y_train.shape) 
    print(y_test.shape)

    (1010, 10)
    (253, 10)
    (1010,)
    (253,)

    # Step 9: Observations after preprocessing
    # - ID columns have been removed.
    # - Rows with missing values have been removed.
    # - Numeric and categorical features have been separated into X and y, respectively.
    # - Numeric columns have been rescaled (if required, this step is optional based on the algorithm used).
    # - Category columns have been one-hot encoded to be used in the model.
    # - The dataset has been split into train and test sets for model evaluation.

we are ready to fit ML models to train and evaluate using test

    X.to_csv('insurance_claim_features.csv', index=False)
    y.to_csv('insurance_claim_label.csv',index=False)
