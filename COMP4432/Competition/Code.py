# %%
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# %%
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

# %%
train = pd.read_csv('/kaggle/input/dont-overfit-i/train.csv')
test = pd.read_csv('/kaggle/input/dont-overfit-i/test.csv')
submission=pd.read_csv('/kaggle/input/dont-overfit-i/sample_submission.csv')

# train.shape, test.shape, submission.shape

y=train['target']
X=train.drop(["id", "target"], axis=1)
test = test.drop(["id"], axis=1)

# %% [markdown]
# # 1. Data Cleaning & Preparation

# %%
train.head()

# %%
test.head()

# %%
train.info()

# %%
train.isnull().any().any()

# %%
train.duplicated().sum()

# %%
train.describe()

# %%
train['target'].value_counts()

# %% [markdown]
# ## 1.1 Statistics Analysis

# %%
p = sns.countplot(data=train, x="target")
plt.show()

# %% [markdown]
# ### Balance the dataset with synthetic samples using SMOTE
# reference: https://www.kaggle.com/code/rafjaa/resampling-strategies-for-imbalanced-datasets

# %%
from imblearn.over_sampling import SMOTE

smote = SMOTE(sampling_strategy='minority', n_jobs=-1)
X_sm, y_sm = smote.fit_resample(X, train['target'])

df = pd.DataFrame(X_sm)
df['target'] = y_sm

df['target'].value_counts().plot(kind='bar', title='Count (target)');

# %%
std_values = train[train.columns[2:]].std()
plt.hist(std_values, bins=20)
plt.title('Distribution of Standard Deviation of Features')
plt.ylabel('Frequency')

# %%
mean_values = train[train.columns[2:]].mean()
plt.hist(mean_values, bins=20)
plt.title('Distribution of Mean of Features')
plt.ylabel('Frequency')

# %%
print('Distributions of random 28 columns')
plt.figure(figsize=(26, 24))

random_col = np.random.choice(list(train.columns), 28)

for i, col in enumerate(random_col):
    plt.subplot(7, 4, i + 1)
    plt.hist(train[col])
    plt.title(col, loc='right', fontsize=12, fontweight='bold')

# %% [markdown]
# ## 1.2 feature Analysis

# %%
train_temp = train.drop(['id'], axis=1)
train_temp.corr()

# %%
fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(train_temp.corr(), ax=ax,  cmap='Blues')
plt.show()

# %%
# extract important feature from correlation
corr_matrix = train_temp.corr()
target_corr = corr_matrix['target'].abs().sort_values(ascending=False)
top_10_features = target_corr.head(11).index
top_corr_matrix = train_temp[top_10_features].corr()
top_corr_matrix

# %%
fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(top_corr_matrix, ax=ax, annot=True, cmap='Blues')
plt.show()

# %%
train_top10 = train_temp[top_10_features]
train_top10.shape

# %% [markdown]
# # 2. Feature Engineering

# %%
from sklearn.model_selection import StratifiedKFold, RepeatedStratifiedKFold
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score

from imblearn.over_sampling import SMOTE

# %% [markdown]
# ### 2.1 Creating statistics features: mean+std

# %%
# create feature: mean + std
train = pd.read_csv('/kaggle/input/dont-overfit-i/train.csv')
test = pd.read_csv('/kaggle/input/dont-overfit-i/test.csv')

y=train['target']
X=train.drop(["id", "target"], axis=1)
test = test.drop(["id"], axis=1)

X_train = X
X_test = test
y_train = y

# %%
X_train.shape, X_test.shape, y_train.shape

# %% [markdown]
# ### 2.2 Feature Transformation: Standard Scalar

# %%
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaler = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X_train_scaled = X_scaler
y_train_scaled = y
X_test_scaled = test

# %%
X_train.shape, X_test.shape, y_train.shape, X_train_scaled.shape, y_train_scaled.shape,X_test_scaled.shape

# %% [markdown]
# ### 2.3 Feature Selection: Random Forest

# %%
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
# feature_selector = SelectFromModel(RandomForestClassifier(n_estimators=100, random_state=42))
# X_train = feature_selector.fit_transform(X_train, y_train)
# X_test = feature_selector.transform(X_test)

# X_train.shape, X_test.shape, y_train.shape

# %% [markdown]
# # 3. Training dataset evaluation with different model - AUCROC performance

# %%
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve

from sklearn.linear_model import LogisticRegression, Lasso, SGDClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier

# %% [markdown]
# ## 3.1 train multiple models and evaluate them

# %%
# Train multiple models and evaluate them
models = {
    'Logistic Regression': LogisticRegression(C=0.1, penalty='l2', class_weight='balanced', random_state=42, max_iter=1000),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': SVC(C=1.0, kernel='rbf', class_weight='balanced', random_state=42, probability=True),
    'KNN': KNeighborsClassifier(n_neighbors=5),
    'Decision Tree': DecisionTreeClassifier(class_weight='balanced', random_state=42),
    'Gaussian NB': GaussianNB(),
    'AdaBoost': AdaBoostClassifier(n_estimators=100, random_state=42),
    'Lasso': Lasso(alpha=0.1, random_state=42),
    'SGDClassifier': SGDClassifier(max_iter=1000, tol=1e-3, class_weight='balanced', random_state=42)
}

kf = KFold(n_splits=20, shuffle=True, random_state=42)

# Store AUC scores for plotting
model_auc_scores = {}
model_roc_curves = {}

for model_name, model in models.items():
    auc_scores = []
    all_fpr = []
    all_tpr = []
    
    for train_index, val_index in kf.split(X_train_scaled):
        # Split the data
        X_kf_train, X_kf_val = X_train_scaled[train_index], X_train_scaled[val_index]
        y_kf_train, y_kf_val = y_train.iloc[train_index], y_train.iloc[val_index]
        
        # Fit the model
        model.fit(X_kf_train, y_kf_train)
        
        # Obtain prediction probabilities
        if hasattr(model, 'predict_proba'):
            y_kf_val_pred_prob = model.predict_proba(X_kf_val)[:, 1]
        elif hasattr(model, 'decision_function'):
            y_kf_val_pred_prob = model.decision_function(X_kf_val)
        else:
            y_kf_val_pred_prob = model.predict(X_kf_val)  # Use predictions directly if no proba or decision function

        # Calculate AUC score
        auc_scores.append(roc_auc_score(y_kf_val, y_kf_val_pred_prob))
        
        # Store FPR and TPR for ROC curve
        fpr, tpr, _ = roc_curve(y_kf_val, y_kf_val_pred_prob)
        all_fpr.append(fpr)
        all_tpr.append(tpr)
    
    # Calculate mean and standard deviation of AUC
    mean_auc = np.mean(auc_scores)
    std_auc = np.std(auc_scores)
    model_auc_scores[model_name] = (mean_auc, std_auc)
    
    # Store average ROC curve data
    model_roc_curves[model_name] = (all_fpr, all_tpr)

    print(f"K-Fold ROC AUC Score ({model_name}): {mean_auc:.4f} (+/- {std_auc:.4f})")

# %%
# Plotting K-Fold ROC AUC Scores as a Bar Chart
plt.figure(figsize=(10, 6))
model_names = list(model_auc_scores.keys())
mean_aucs = [model_auc_scores[name][0] for name in model_names]
std_aucs = [model_auc_scores[name][1] for name in model_names]

plt.barh(model_names, mean_aucs, xerr=std_aucs, color='skyblue', alpha=0.8)
plt.xlabel('Mean ROC AUC Score')
plt.title('K-Fold ROC AUC Score for Different Models')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# %%
# Plotting ROC Curves for each model
plt.figure(figsize=(10, 8))
for model_name, (all_fpr, all_tpr) in model_roc_curves.items():
    mean_fpr = np.linspace(0, 1, 100)
    mean_tpr = np.zeros_like(mean_fpr)

    # Average TPR values for each unique FPR point
    for fpr, tpr in zip(all_fpr, all_tpr):
        mean_tpr += np.interp(mean_fpr, fpr, tpr)
    mean_tpr /= len(all_fpr)

    plt.plot(mean_fpr, mean_tpr, label=f"{model_name} (AUC = {model_auc_scores[model_name][0]:.4f})")

# Adding a diagonal line for reference
plt.plot([0, 1], [0, 1], 'k--', lw=2, label='Random Guess')
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.grid(linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# %% [markdown]
# ## 3.2 Comparasion between different penalty, folds, and parameter

# %%
from sklearn.model_selection import StratifiedKFold

penalties = ['l1', 'l2']
C_values = [0.01, 0.1, 1.0]
n_folds_options = [2, 5, 10, 20]
results = []

for n_folds in n_folds_options:
    folds = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=42)
    
    for penalty in penalties:
        for C in C_values:
            model_params = {'penalty': penalty, 'C': C, 'solver': 'liblinear', 'class_weight': 'balanced', 'max_iter': 10000}
            lr_model = LogisticRegression(**model_params)
            
            auc_scores = []
            for train_index, val_index in folds.split(X_train_scaled, y):
                X_train_fold, X_val_fold = X_train_scaled[train_index], X_train_scaled[val_index]
                y_train_fold, y_val_fold = y.iloc[train_index], y.iloc[val_index]
                lr_model.fit(X_train_fold, y_train_fold)
                y_val_pred_prob = lr_model.predict_proba(X_val_fold)[:, 1]
                auc_scores.append(roc_auc_score(y_val_fold, y_val_pred_prob))
            
            mean_score = np.mean(auc_scores)
            result = {
                'n_folds': n_folds,
                'penalty': penalty,
                'C': C,
                'mean_roc_auc_score': mean_score
            }
            results.append(result)
            
            print(f"Processed: folds={n_folds}, penalty={penalty}, C={C}, Mean ROC AUC: {mean_score:.4f}")
# ***RESULT IN REPORT***

# %% [markdown]
# # 4. Basic Modeling Performance - whole training dataset

# %% [markdown]
# ## 4.1 Basic Modelling

# %%
from mlxtend.classifier import StackingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression, Lasso, SGDClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

# all_classifiers = [
#     LogisticRegression(C=0.1, penalty='l2', random_state=42, max_iter=1000),
#     RandomForestClassifier(n_estimators=100, random_state=42),
#     GradientBoostingClassifier(n_estimators=100, random_state=42),
#     SVC(C=1.0, kernel='rbf', random_state=42, probability=True),
#     KNeighborsClassifier(n_neighbors=5),
#     DecisionTreeClassifier(random_state=42),
#     GaussianNB(),
#     AdaBoostClassifier(n_estimators=100, random_state=42),
#     Lasso(alpha=0.1, random_state=42),
#     SGDClassifier(max_iter=1000, tol=1e-3, random_state=42)
# ]
models = {
    'Logistic Regression': LogisticRegression(C=0.1, penalty='l2', random_state=42, max_iter=1000),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': SVC(C=1.0, kernel='rbf', random_state=42, probability=True),
    'KNN': KNeighborsClassifier(n_neighbors=5),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Gaussian NB': GaussianNB(),
    'AdaBoost': AdaBoostClassifier(n_estimators=100, random_state=42),
    'Lasso': Lasso(alpha=0.1, random_state=42),
    'SGDClassifier': SGDClassifier(max_iter=1000, tol=1e-3, random_state=42)
}

# %%

param_grids = {
    'Logistic Regression': {
        'class_weight': ['balanced'],
        'C': [0.001, 0.01, 0.1, 1, 10, 100],
        'penalty': ['l1','l2'],
        'max_iter': [1000, 2000],
        'solver': ['liblinear']
    },
    'Random Forest': {
        'n_estimators': [100, 1000],
        'max_depth': [None, 3, 5, 15],
    },
    'SVM': {
        'C': [0.001, 0.01, 0.1, 1, 10],
        'kernel': ['rbf', 'linear', 'poly'],
        'gamma': ['scale', 'auto'],
    },
    'KNN': {
        'n_neighbors': [2, 3, 5, 7, 9, 10, 20],
        'weights': ['uniform', 'distance'],
        'leaf_size': [5, 10, 30]
    },
    'Decision Tree': {
        'criterion':['gini', 'entropy', 'log_loss'],
        'class_weight':['balanced'],
        'max_depth': [None, 5, 10, 20, 30, 50, 60, 100],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf':[2,3,5,10],
        'min_impurity_decrease':[0.1,0.2,0.5]
    },
    'Gaussian NB': {},
    'AdaBoost': {
        'n_estimators': [5, 10, 50, 100, 200],
        'learning_rate': [0.001, 0.01, 0.1, 0.5, 1, 1.5, 10],
    },
    'Lasso': {
        'alpha': [0.01, 0.1, 1, 10],
        'tol': [0.00025, 0.0005, 0.001, 0.002]
    },
    'SGDClassifier': {
        'alpha': [0.0001, 0.001, 0.01, 0.1],
        'loss': ['hinge', 'log', 'modified_huber'],
        'penalty': ['l1', 'l2', 'elasticnet'],
        'l1_ratio': [0, 0.15, 0.5, 1.0],
        'learning_rate': ['optimal', 'invscaling', 'adaptive'],
        'max_iter': [1000, 2000]
    }
}

# %%
train = pd.read_csv('/kaggle/input/dont-overfit-i/train.csv')
test = pd.read_csv('/kaggle/input/dont-overfit-i/test.csv')

y=train['target']
X=train.drop(["id", "target"], axis=1)
test = test.drop(["id"], axis=1)

X_train = X
X_test = test
y_train = y

scaler = StandardScaler()
X_train_basic = scaler.fit_transform(X_train)
X_test_basic = scaler.transform(X_test)

X_train_basic.shape, X_test_basic.shape, y_train.shape

# %% [markdown]
# ### GridSearchCV

# %%
import warnings
warnings.filterwarnings('ignore')

# %%
# Store the best models and parameters
best_models = {}
basic_predictions = {}

for model_name, model in models.items():
    print(f"Performing GridSearchCV for {model_name}...")
    
    # Create GridSearchCV only if parameter grid is specified
    if param_grids.get(model_name):
        grid_search = GridSearchCV(estimator=model,
                                   param_grid=param_grids[model_name],
                                   scoring='roc_auc',
                                   cv=20,
                                   n_jobs=-1,
                                   verbose=1)
        grid_search.fit(X_train, y_train)
        best_model = grid_search.best_estimator_
        best_params = grid_search.best_params_
        best_score = grid_search.best_score_
        
        print(f"Best parameters for {model_name}: {best_params} with best score: {best_score}")
    else:
        # No parameter grid specified (e.g., Gaussian NB)
        best_model = model
        best_model.fit(X_train_basic, y_train)
    
    # Store the best model for later predictions
    best_models[model_name] = best_model

    # Make predictions using the best model
    y_test_pred = best_model.predict(X_test_basic)
    basic_predictions[model_name] = y_test_pred

    print(f"Training complete for {model_name}.\n")

# ***RESULT IN FOLLOWING CELL***

# %% [markdown]
# ### Final model after GridSearchCV

# %%
final_models = {
    'Logistic Regression': LogisticRegression(C=0.1, penalty='l1', solver='liblinear', class_weight='balanced', max_iter=1000, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=1000, max_depth=3, random_state=42),
    'SVM': SVC(C=0.1, kernel='linear', gamma='scale', random_state=42, probability=True),
    'KNN': KNeighborsClassifier(n_neighbors=10, weights='distance', leaf_size=5),
    'Decision Tree': DecisionTreeClassifier(criterion='entropy', class_weight='balanced', max_depth=None, min_impurity_decrease=0.1, min_samples_leaf=2, min_samples_split=2, random_state=42),
    'Gaussian NB': GaussianNB(),
    'AdaBoost': AdaBoostClassifier(n_estimators=200, learning_rate=1.5, random_state=42),
    'Lasso': Lasso(alpha=0.1, tol=0.00025, random_state=42),
    'SGDClassifier': SGDClassifier(alpha=0.01, l1_ratio=0.5, learning_rate='optimal', loss='log', max_iter=1000, penalty='elasticnet', random_state=42)
}

# %%
basic_predictions = {}

for model_name, pipeline in final_models.items():
    print(f"Training {model_name} on the entire dataset...")
    pipeline.fit(X_train, y_train)
    y_test_pred = pipeline.predict(X_test)
    if model_name == "Lasso":
        y_test_pred = np.where(y_test_pred >= 0.5, 1, 0)
    basic_predictions[model_name] = y_test_pred
    # Convert predictions to DataFrame
    submission_df = pd.DataFrame({
        'id': submission['id'],
        'target': y_test_pred
    })
    file_name = f"submission_basic_{model_name}.csv"

    # Save DataFrame to CSV
    submission_df.to_csv(file_name, index=False)
    print(f"Saved predictions for {model_name} with basic model to {file_name}")

# %%
basic_pred_df = pd.DataFrame(basic_predictions)
basic_pred_df['id'] = submission['id']
basic_pred_df.head()

# %% [markdown]
# result: LR 0.753
# RF 0.500
# SVM 0.629
# KNN 0.546
# DT 0.619
# GNB 0.591
# AB 0.619
# Lasso 0.528
# SGDC 0.589

# %% [markdown]
# ## 4.2 Improved Models: feature creation, selection

# %%
train = pd.read_csv('/kaggle/input/dont-overfit-i/train.csv')
test = pd.read_csv('/kaggle/input/dont-overfit-i/test.csv')

y=train['target']
X=train.drop(["id", "target"], axis=1)
test = test.drop(["id"], axis=1)

X_train = X
X_test = test
y_train = y

X_train['300'] = X_train.std(1)
X_test['300'] = X_test.std(1)
X_train['301'] = X_train.mean(1)
X_test['301'] = X_test.mean(1)

# %% [markdown]
# ## 4.2.1 balance by SMOTE

# %%
from imblearn.over_sampling import SMOTE

smote = SMOTE(sampling_strategy='minority', n_jobs=-1)
X_sm, y_sm = smote.fit_resample(X_train, y_train)

# %%
scaler = StandardScaler()
X_train_final = scaler.fit_transform(X_train)
X_test_final = scaler.transform(X_test)

X_train_final.shape, X_test_final.shape, y_train.shape

# %% [markdown]
# ## 4.2.2 feature selection by ELI5, SelectKBest, VarianceThreshold, RFE, PCA

# %%
import eli5
from eli5.sklearn import PermutationImportance
from sklearn.feature_selection import VarianceThreshold, RFE, SelectKBest, f_classif

# %%
# Feature selection using SelectKBest
select_kbest = SelectKBest(score_func=f_classif, k=10)  # select the 10 most important features based on ANOVA F-value.
X_train_kbest = select_kbest.fit_transform(X_train_final, y_train)
X_test_kbest = select_kbest.transform(X_test_final)

# Feature selection using Recursive Feature Elimination (RFE)
from sklearn.feature_selection import RFE
rfe_selector = RFE(estimator=LogisticRegression(max_iter=1000, random_state=42), n_features_to_select=10)
X_train_rfe = rfe_selector.fit_transform(X_train_final, y_train)
X_test_rfe = rfe_selector.transform(X_test_final)

# Fit the eli5.PermutationImportance
perm_model = LogisticRegression(max_iter=1000, random_state=42).fit(X_train_final, y_train)
perm_importance = PermutationImportance(perm_model, random_state=42, cv=5).fit(X_train_final, y_train)
importances = perm_importance.feature_importances_
sorted_indices = np.argsort(importances)[::-1]
top_10_indices = sorted_indices[:10]
X_train_eli5 = X_train_final[:, top_10_indices]
X_test_eli5 = X_test_final[:, top_10_indices]

X_train_kbest.shape, X_test_kbest.shape,X_train_rfe.shape, X_test_rfe.shape, X_train_eli5.shape, X_test_eli5.shape

# %%
kf = KFold(n_splits=20, shuffle=True, random_state=42)

# Store AUC scores for plotting
model_auc_scores = {}
feature_selection_methods = {
    'KBEST':(X_train_kbest, X_test_kbest),
    'RFE': (X_train_rfe, X_test_rfe),
    'ELI5':(X_train_eli5, X_test_eli5)
}

# %%
improved_predictions = {}
for feature_name, (X_train, X_test) in feature_selection_methods.items():
    print(f"Evaluating feature selection method: {feature_name}")
    improved_predictions[feature_name] = {}
    for model_name, pipeline in final_models.items():
        print(f"Training {model_name} on the entire dataset...")
        pipeline.fit(X_train, y_train)
        y_test_pred = pipeline.predict(X_test)
        if model_name == "Lasso":
            y_test_pred = np.where(y_test_pred >= 0.5, 1, 0)
        improved_predictions[feature_name][model_name] = y_test_pred
        # Convert predictions to DataFrame
        submission_df = pd.DataFrame({
            'id': submission['id'],
            'target': y_test_pred
        })
        file_name = f"submission_{feature_name}_{model_name}.csv"

        # Save DataFrame to CSV
        submission_df.to_csv(file_name, index=False)
        print(f"Saved predictions for {model_name} with {feature_name} to {file_name}")

# %% [markdown]
# # 5. Submission & Performance Checking

# %% [markdown]
# ## 5.1 submission score with basic modelling

# %%
# leaderboard score with basic modelling
scores_base = {}
scores_base['LR'] = 0.753 # logistic regression
scores_base['RF'] = 0.500 # random forest
scores_base['SVM'] = 0.629 
scores_base['KNN'] = 0.546
scores_base['DT'] = 0.619 # Decision Tree
scores_base['GNB'] = 0.591 # Gaussian NB
scores_base['AB'] = 0.619 #AdaBoost
scores_base['Lasso'] =  0.528
scores_base['SGDC'] = 0.589 # SGDClassifier

# print(scores_base)
plt.figure(figsize=(12, 5))
plt.bar(range(len(scores_base)), list(scores_base.values()), label='Base Modeling', align='center')
plt.title('Scores of Basic Models')
plt.xlabel('Models')
plt.ylabel('Scores')
plt.xticks(range(len(scores_base)), list(scores_base.keys()))
for a, b in zip(range(len(scores_base)), list(scores_base.values())):
    plt.text(a, b, '%.3f' % b, ha='center', va='bottom', fontsize=11)

plt.legend()
plt.show()

# %% [markdown]
# ## 5.2 submission with feature selection

# %%
# leaderboard score with feature engineering
scores_improved = {
    "basic": {'LR': 0.753, 'RF': 0.5, 'SVM': 0.629, 'KNN': 0.546, 'DT': 0.619, 'GNB': 0.591, 'AB': 0.619, 'Lasso': 0.528, 'SGDC': 0.589},
    "KBEST": {'LR': 0.734, 'RF': 0.614, 'SVM': 0.688 , 'KNN': 0.644, 'DT':0.619, 'GNB': 0.670, 'AB': 0.660, 'Lasso': 0.528, 'SGDC': 0.697},
    "RFE": {'LR': 0.545, 'RF': 0.536, 'SVM': 0.515, 'KNN': 0.496, 'DT': 0.502, 'GNB': 0.517, 'AB': 0.524, 'Lasso': 0.533, 'SGDC': 0.521},
    "ELI5": {'LR': 0.717, 'RF': 0.613, 'SVM': 0.665, 'KNN': 0.640, 'DT': 0.619, 'GNB': 0.655, 'AB': 0.632, 'Lasso': 0.528, 'SGDC': 0.682}
}

# Plotting parameters
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.2
index = np.arange(len(scores_improved["basic"]))

# Plotting histograms for each feature engineering method
for i, (feature_name, scores) in enumerate(scores_improved.items()):
    plt.bar(index + i * bar_width, scores.values(), bar_width, label=feature_name)

# Setting labels and title
plt.xlabel('Models', fontsize=14)
plt.ylabel('Leaderboard Score', fontsize=14)
plt.title('Leaderboard Scores with Feature Engineering', fontsize=16)
plt.xticks(index + bar_width, scores_improved["basic"].keys(), fontsize=12, rotation=45)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Display the plot
plt.show()


