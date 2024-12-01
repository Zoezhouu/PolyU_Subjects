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

train = pd.read_csv('/kaggle/input/house-prices-advanced-regression-techniques/train.csv')
test = pd.read_csv('/kaggle/input/house-prices-advanced-regression-techniques/test.csv')
submission=pd.read_csv('/kaggle/input/house-prices-advanced-regression-techniques/sample_submission.csv')

# train = pd.read_csv('./input/train.csv')
# test = pd.read_csv('./input/test.csv')
# submission=pd.read_csv('./input/sample_submission.csv')

train.shape, test.shape, submission.shape

# %%
train_ID = train['Id']
test_ID = test ['Id']
train_result=train['SalePrice']
train_data=train.drop(["Id"],axis=1)
test_data=test.drop(["Id"],axis=1)

train_data.shape, train_result.shape, test_data.shape

# %% [markdown]
# # Data Analysis

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

# %% [markdown]
# ## distribution of SalePrice

# %%
sns.set_style("white")
sns.set_color_codes(palette='deep')
f, ax = plt.subplots(figsize=(8, 7))
# Check the new distribution 
sns.distplot(train_data['SalePrice'], color="b", kde=True)
ax.xaxis.grid(False)
ax.set(ylabel="Frequency")
ax.set(xlabel="SalePrice")
ax.set(title="SalePrice distribution")
sns.despine(trim=True, left=True)
plt.show()

# %% [markdown]
# ## log price calculation

# %%
# log(1+x) to all elements of the column SalePrice
logPrice = np.log1p(train_data['SalePrice']) 

train_data_log = train_data.copy()
train_data_log['logPrice'] = logPrice

# %%
from scipy.stats import norm

sns.set_style("white")
sns.set_color_codes(palette='deep')

f, ax = plt.subplots(figsize=(8, 7))

# Check the new distribution
sns.histplot(train_data_log['logPrice'], color="b", kde=True, stat="density", bins=30, label="Actual Distribution")

# Fit a normal distribution
mean = train_data_log['logPrice'].mean()
std = train_data_log['logPrice'].std()
x = np.linspace(train_data_log['logPrice'].min(), train_data_log['logPrice'].max(), 100)
normal_dist = norm.pdf(x, mean, std)

# Add the normal distribution line
ax.plot(x, normal_dist, color="r", label="Normal Distribution")

# Customize plot
ax.xaxis.grid(False)
ax.set(ylabel="Density")
ax.set(xlabel="logPrice")
ax.set(title="logPrice Distribution with Normal Fit")
sns.despine(trim=True, left=True)
plt.legend()
plt.show()

# %% [markdown]
# ## Missing values for train data & test data 

# %%
train_features = train_data.drop(["SalePrice"],axis=1)
combined_data = pd.concat([train_features, test_data], axis=0, ignore_index=True)

missing_values = combined_data.isna().sum()
missing_columns = (missing_values[missing_values > 0] / len(combined_data)) * 100
print(missing_columns.sort_values(ascending=False))

# %%
# only choose features that missing percentage > 0
missing_columns = missing_columns.sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=missing_columns.index, y=missing_columns.values, palette='viridis')
plt.xticks(rotation=90)
plt.xlabel('Features', fontsize=12)
plt.ylabel('Percentage of Missing Values (%)', fontsize=12)
plt.title('Percentage of Missing Values per Feature', fontsize=15)
plt.show()
print('We can remove features with missing values that are more than 10%.')

# %% [markdown]
# seperate numeric columns and categorical columns

# %%
missing_columns_list = ['GarageFinish','GarageQual','GarageCond','GarageYrBlt','GarageType',
                   'BsmtExposure','BsmtCond','BsmtQual','BsmtFinType2','BsmtFinType1',
                   'MasVnrArea','MSZoning','BsmtFullBath','Functional','Utilities','GarageArea',
                   'GarageCars','Electrical','KitchenQual','TotalBsmtSF','BsmtUnfSF','BsmtFinSF2',
                   'BsmtFinSF1','Exterior2nd','Exterior1st','SaleType']

# functional - typical
# features['Exterior1st'] = features['Exterior1st'].fillna(features['Exterior1st'].mode()[0])

numeric_dtypes = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
numeric = [] # numeric features
categoric = [] # category features
for i in train.columns:
    # delete features with higher missing percentage(>10%)
    if i in ['PoolQC', 'MiscFeature','Alley','Fence','MasVnrType','FireplaceQu','LotFrontage']:
        pass
    else:
        # seperate numeric feature & categorical features 
        if train[i].dtype in numeric_dtypes:
            numeric.append(i) 
            
        else:
            categoric.append(i)

# numeric, categoric

# %% [markdown]
# ## detect outlier

# %%
# Calculate number of rows and columns
ncols = 3
nrows = (len(numeric) // ncols) + (1 if len(numeric) % ncols != 0 else 0)

# Create subplots with larger height for each plot
fig, axs = plt.subplots(ncols=ncols, nrows=nrows, figsize=(24, nrows * 5))  # Increased height
axs = axs.flatten()  # Flatten for easy iteration

# Scatterplots for numeric features against SalePrice
for i, feature in enumerate(numeric):
    sns.scatterplot(x=feature, y='SalePrice', color='blue', alpha=0.6, data=train, ax=axs[i])
    axs[i].set_xlabel(feature, fontsize=15, labelpad=10)
    axs[i].set_ylabel('SalePrice', fontsize=15, labelpad=10)
    axs[i].tick_params(axis='x', labelsize=12)
    axs[i].tick_params(axis='y', labelsize=12)

# Remove unused subplots
for j in range(i + 1, len(axs)):
    fig.delaxes(axs[j])

plt.tight_layout()
plt.show()

# %% [markdown]
# ## Heat Map

# %%
train_numeric_data = train[numeric]
train_numeric_data_log = train_numeric_data.copy()
train_numeric_data_log["logPrice"] = train_data_log['logPrice']
corr = train_numeric_data_log.corr()
plt.subplots(figsize=(15,12))
sns.heatmap(corr, vmax=0.9, cmap="Blues", square=True)

# %%
corr_matrix = train_numeric_data_log.corr()

target_corr = corr_matrix['SalePrice'].abs().sort_values(ascending=False)
top_10_features = target_corr.head(12).index
top_corr_matrix = train_numeric_data_log[top_10_features].corr()

fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(top_corr_matrix, ax=ax, annot=True, cmap='Blues')
plt.show()

# %%
sns.scatterplot(x='OverallQual', y='SalePrice', color='blue', data=train)

# %%
sns.scatterplot(x='GrLivArea', y='SalePrice', color='blue', data=train)

# %% [markdown]
# ## Categorical Feature

# %%
# data = pd.concat([train['SalePrice'], train['OverallQual']], axis=1)
# f, ax = plt.subplots(figsize=(8, 6))
# fig = sns.boxplot(x=train['OverallQual'], y="SalePrice", data=data)
# fig.axis(ymin=0, ymax=800000);

# %%
# data = pd.concat([train['SalePrice'], train['YearBuilt']], axis=1)
# f, ax = plt.subplots(figsize=(16, 8))
# fig = sns.boxplot(x=train['YearBuilt'], y="SalePrice", data=data)
# fig.axis(ymin=0, ymax=800000);
# plt.xticks(rotation=45);


for feature in categoric:
    data = pd.concat([train['SalePrice'], train[feature]], axis=1)
    
    # Create the plot
    plt.figure(figsize=(16, 8))  # Define figure size
    sns.boxplot(x=feature, y="SalePrice", data=data)
    plt.ylim(0, 800000)  # Set y-axis limits
    plt.xticks(rotation=45, fontsize=12)  # Rotate x-axis labels for readability
    plt.title(f'Boxplot of SalePrice by {feature}', fontsize=16)  # Add a title
    plt.xlabel(feature, fontsize=14)  # Add x-axis label
    plt.ylabel('SalePrice', fontsize=14)  # Add y-axis label
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines for y-axis
    plt.tight_layout()  # Adjust layout for clarity
    plt.show()

# %% [markdown]
# # Feature Engineering

# %% [markdown]
# ## Remove outliers

# %%
train_data.drop(train_data[(train_data['OverallQual']<5) & (train_data['SalePrice']>200000)].index, inplace=True)
train_data.drop(train_data[(train_data['GrLivArea']>4500) & (train_data['SalePrice']<300000)].index, inplace=True)
train_data.reset_index(drop=True, inplace=True)
train_data.shape

# %% [markdown]
# ## handle missing values

# %%
# def handle_missing(features):    
missing_columns_list = ['GarageFinish','GarageQual','GarageCond','GarageYrBlt','GarageType',  
                        'BsmtExposure','BsmtCond','BsmtQual','BsmtFinType2','BsmtFinType1', 
                        'MasVnrArea','MSZoning',
                        'Functional',
                        'Utilities',
                        'GarageArea', 'GarageCars',
                        'Electrical',
                        'KitchenQual',
                        'TotalBsmtSF','BsmtUnfSF','BsmtFinSF2', 'BsmtFinSF1','BsmtFullBath',
                        'Exterior2nd','Exterior1st',
                        'SaleType']

# Drop features which missing values > 10%
train_result = train_data['SalePrice']
print(train_result.shape)
train_features = train_data.drop(['SalePrice'], axis=1)
test_features = test_data

features = pd.concat([train_features, test_features]).reset_index(drop=True)

# features = train_data.drop(['PoolQC', 'MiscFeature','Alley','Fence','MasVnrType','FireplaceQu','LotFrontage'], axis=1)
    
# Delete false values
s=0
for i in range(len(features)):
    if not all([features['BsmtQual'].isnull()[i], features['BsmtExposure'].isnull()[i], features['BsmtFinType1'].isnull()[i], features['BsmtFinType2'].isnull()[i], features['BsmtCond'].isnull()[i]]) and not all(not v for v in [features['BsmtQual'].isnull()[i], features['BsmtExposure'].isnull()[i], features['BsmtFinType1'].isnull()[i], features['BsmtFinType2'].isnull()[i], features['BsmtCond'].isnull()[i]]):
        s+=1
        print(s,'\t', i,'\t', features['BsmtQual'].isnull()[i],'\t\t',
                features['BsmtExposure'].isnull()[i], '\t\t', features['BsmtFinType1'].isnull()[i],
            '\t\t', features['BsmtFinType2'].isnull()[i],'\t\t', features['BsmtCond'].isnull()[i])

for i in range(len(features)):
    if not all([features['GarageFinish'].isnull()[i], features['GarageQual'].isnull()[i], features['GarageCond'].isnull()[i], features['GarageYrBlt'].isnull()[i], features['GarageType'].isnull()[i]]) and not all(not v for v in [features['GarageFinish'].isnull()[i], features['GarageQual'].isnull()[i], features['GarageCond'].isnull()[i], features['GarageYrBlt'].isnull()[i], features['GarageType'].isnull()[i]]):
        s+=1
        print(s,'\t', i,'\t', features['GarageFinish'].isnull()[i],'\t\t',
                features['GarageQual'].isnull()[i], '\t\t', features['GarageCond'].isnull()[i],
            '\t\t', features['GarageYrBlt'].isnull()[i],'\t\t', features['GarageType'].isnull()[i])
        
    
# Type 1.1: Special case(Functional): Assume typical unless deductions are warranted
features['Functional'] = features['Functional'].fillna('Typ')

# Type 1.2: fill in mode
features['Electrical'] = features['Electrical'].fillna(features['Electrical'].mode()[0])
features['KitchenQual'] = features['KitchenQual'].fillna(features['KitchenQual'].mode()[0])
features['Exterior1st'] = features['Exterior1st'].fillna(features['Exterior1st'].mode()[0])
features['Exterior2nd'] = features['Exterior2nd'].fillna(features['Exterior2nd'].mode()[0])
features['SaleType'] = features['SaleType'].fillna(features['SaleType'].mode()[0])
features['Utilities'] = features['Utilities'].fillna(features['Utilities'].mode()[0])
# features['MasVnrArea'] = features['MasVnrArea'].fillna(features['MasVnrArea'].mode()[0])


#Type 1.3: fill in '0'/'None'
# Garage
for col in ('GarageArea', 'GarageCars'):
    features[col] = features[col].fillna(0)
for col in ['GarageType', 'GarageFinish', 'GarageQual', 'GarageCond','GarageYrBlt']:
    features[col] = features[col].fillna('None')

# Bsmt
for col in ('BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2'):
    features[col] = features[col].fillna('None')
for col in ('TotalBsmtSF','BsmtUnfSF','BsmtFinSF2', 'BsmtFinSF1','BsmtFullBath',):
    features[col] = features[col].fillna(0)

# MasVnrArea
features['MasVnrArea'] = features['MasVnrArea'].fillna(0)

# LotFrontage
features['LotFrontage'] = features['LotFrontage'].fillna(0)

for col in ('PoolQC', 'MiscFeature','Alley','Fence','MasVnrType','FireplaceQu'):
    features[col] = features[col].fillna('None')

### fill in rest
objects = []
for i in features.columns:
    if features[i].dtype == object:
        objects.append(i)
    features.update(features[objects].fillna('None'))
    
# And we do the same thing for numerical features, but this time with 0s
numeric_dtypes = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
numeric = []
for i in features.columns:
    if features[i].dtype in numeric_dtypes:
        numeric.append(i)
    features.update(features[numeric].fillna(0))    
features.shape

# %%
# delete inconsistent values
train_result = train_result.drop([332, 946], axis=0).reset_index(drop=True)
features = features.drop([332, 946], axis = 0).reset_index(drop = True)
features.shape, train_result.shape

# %% [markdown]
# ## Handle skewed features
# Normalize skewed features: https://www.kaggle.com/code/lavanyashukla01/how-i-made-top-0-3-on-a-kaggle-competition#Fix-skewed-features

# %%
#######################################
# Create box plots for all numeric features
sns.set_style("white")
f, ax = plt.subplots(figsize=(8, 7))
ax.set_xscale("log")
ax = sns.boxplot(data=features[numeric] , orient="h", palette="Set1")
ax.xaxis.grid(False)
ax.set(ylabel="Feature names")
ax.set(xlabel="Numeric values")
ax.set(title="Numeric Distribution of Features")
sns.despine(trim=True, left=True)

# %%
from scipy.stats import skew, norm
from scipy.special import boxcox1p
from scipy.stats import boxcox_normmax
# Find skewed numerical features
skew_features = features[numeric].apply(lambda x: skew(x)).sort_values(ascending=False)

high_skew = skew_features[skew_features > 0.5]
skew_index = high_skew.index

print("There are {} numerical features with Skew > 0.5 :".format(high_skew.shape[0]))
skewness = pd.DataFrame({'Skew' :high_skew})
skew_features.head(10)

# %%
# Normalize skewed features
for i in skew_index:
    features[i] = np.log1p(features[i])

# %%
# Let's make sure we handled all the skewed values
sns.set_style("white")
f, ax = plt.subplots(figsize=(8, 7))
ax.set_xscale("log")
ax = sns.boxplot(data=features[skew_index] , orient="h", palette="Set1")
ax.xaxis.grid(False)
ax.set(ylabel="Feature names")
ax.set(xlabel="Numeric values")
ax.set(title="Numeric Distribution of Features")
sns.despine(trim=True, left=True)

# %% [markdown]
# ## create new features

# %%
features['TotalSF']=features['TotalBsmtSF'] + features['1stFlrSF'] + features['2ndFlrSF']
features['TotalSqrFootage'] = (features['BsmtFinSF1'] + features['BsmtFinSF2'] + features['1stFlrSF'] + features['2ndFlrSF'])
features['TotalBathrooms'] = (features['FullBath'] + (0.5 * features['HalfBath']) + features['BsmtFullBath'] + (0.5 * features['BsmtHalfBath']))
# Age of the house when sold
features['HouseAge'] = features['YrSold'] - features['YearBuilt']
# Age since last remodel
features['YearsSinceRemodel'] = features['YrSold'] - features['YearRemodAdd']


# Simplified feature for central air
features['HasCentralAir'] = features['CentralAir'].apply(lambda x: 1 if x == 'Y' else 0)
features['HasPool'] = features['PoolArea'].apply(lambda x: 1 if x > 0 else 0)
features['Has2ndfloor'] = features['2ndFlrSF'].apply(lambda x: 1 if x > 0 else 0)
features['HasGarage'] = features['GarageArea'].apply(lambda x: 1 if x > 0 else 0)
features['HasBsmt'] = features['TotalBsmtSF'].apply(lambda x: 1 if x > 0 else 0)

features.shape

# %% [markdown]
# ### manage categorical features (get_dummies)

# %%
final_features = pd.get_dummies(features).reset_index(drop=True)
final_features.head()

# %%
final_features.shape

# %%
final_train_feature = final_features.iloc[:1455, :]
final_test_feature = final_features.iloc[len(final_train_feature):, :]
final_train_feature.shape, final_test_feature.shape, train_result.shape

# %% [markdown]
# # Model Training

# %%
# final train feature
# final test feature
# train result

# %% [markdown]
# ## cross validation
# https://www.kaggle.com/code/lavanyashukla01/how-i-made-top-0-3-on-a-kaggle-competition#Encode-categorical-features

# %%
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import mean_squared_error

# %%
# Setup cross validation folds
kf = KFold(n_splits=12, random_state=42, shuffle=True)

# %% [markdown]
# ### evaluation metrics

# %%
# Define error metrics
X = np.log1p(final_train_feature)
y = np.log1p(train_result)

# Apply log transformation
X_test = final_test_feature.apply(pd.to_numeric, errors='coerce')
X_test = X_test.fillna(1e-6)
X_test = X_test.clip(lower=1e-6)
X_test = X_test.applymap(lambda x: np.log1p(x) if np.isfinite(x) else 0)


def rmsle(y, y_pred):
    return np.sqrt(mean_squared_error(y, y_pred))

def cv_rmse(model):
    rmse = np.sqrt(-cross_val_score(model, X, y, scoring="neg_mean_squared_error", cv=kf))
    return (rmse)

# %%
X_test.isnull().any().any()

# %% [markdown]
# ## Hyperparameter tuning on different models(GridSearchCV)
# https://www.kaggle.com/code/jesucristo/1-house-prices-solution-top-1#Models

# %%
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import RobustScaler
from mlxtend.regressor import StackingCVRegressor
# from sklearn.ensemble import RandomForestRegressor

from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import ElasticNetCV, LassoCV, RidgeCV

# %%
# Define parameter grids for tuning
param_grids = {
    'lasso': {
        'model__alpha': [0.0001, 0.0005, 0.001, 0.005, 0.01]
    },
    'decision_tree': {
        'model__max_depth': [3, 5, 10, None],
        'model__min_samples_split': [2, 5, 10],
        'model__min_samples_leaf': [1, 2, 5]
    },
    'svr': {
        'model__C': [1, 10, 20],
        'model__epsilon': [0.001, 0.01, 0.1],
        'model__gamma': ['scale', 0.001, 0.0003]
    },
    'knn': {
        'model__n_neighbors': [3, 5, 7, 9, 11],
        'model__weights': ['uniform', 'distance'],
        'model__p': [1, 2]  # 1: Manhattan, 2: Euclidean
    },
}

# %%
# Base models with pipelines
models = {
    'lasso': Pipeline([
        ('scaler', RobustScaler()),
        ('model', Lasso(random_state=42))
    ]),
    'decision_tree': Pipeline([
        ('model', DecisionTreeRegressor(random_state=42))
    ]),
    'svr': Pipeline([
        ('scaler', RobustScaler()),
        ('model', SVR())
    ]),
    'knn': Pipeline([
        ('scaler', RobustScaler()),  # Handle scaling
        ('model', KNeighborsRegressor())
    ])
}

# %%
# Tune each model
tuned_models = {}
for model_name, pipeline in models.items():
    print(f"Tuning {model_name}...")
    grid = GridSearchCV(estimator=pipeline, param_grid=param_grids[model_name], cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
    grid.fit(X, y)
    tuned_models[model_name] = grid.best_estimator_
    print(f"Best parameters for {model_name}: {grid.best_params_}")
    print(f"Best CV score for {model_name}: {grid.best_score_}")
print("Finish tuning.")

# %%
# Tuning lasso...
# Best parameters for lasso: {'model__alpha': 0.0005}
# Best CV score for lasso: -0.013220234926020305
# Tuning decision_tree...
# Best parameters for decision_tree: {'model__max_depth': 10, 'model__min_samples_leaf': 5, 'model__min_samples_split': 2}
# Best CV score for decision_tree: -0.03477321855507474
# Tuning svr...
# Best parameters for svr: {'model__C': 20, 'model__epsilon': 0.01, 'model__gamma': 0.0003}
# Best CV score for svr: -0.01304639760394804
# Tuning knn...
# Best parameters for knn: {'model__n_neighbors': 7, 'model__p': 1, 'model__weights': 'distance'}
# Best CV score for knn: -0.02722346709961266
# Finish tuning.

# %%
## Lasso Regression
lasso_reg = make_pipeline(
    RobustScaler(),
    Lasso(alpha=0.0005, random_state=42)
)

## Decision Tree
decision_tree = make_pipeline(
    RobustScaler(),
    DecisionTreeRegressor(
        max_depth=10,  # Optimal value found
        min_samples_split=2,  # Optimal value found
        min_samples_leaf=5,  # Optimal value found
        random_state=42
    )
)


# Support Vector Regressor
svr = make_pipeline(
    RobustScaler(),
    SVR(
        C=20,  # Optimal value found
        epsilon=0.01,  # Optimal value found
        gamma=0.0003  # Optimal value found
    )
)

# K-Nearest Neighbors Regressor
knn_reg = make_pipeline(
    RobustScaler(),
    KNeighborsRegressor(
        n_neighbors=7,  # Optimal value found
        weights='distance',  # Optimal value found
        metric='minkowski',
        p=1  # Optimal value found (Manhattan distance)
    )
)

## Gradient Boosting Regressor
gbr = make_pipeline(
    RobustScaler(),
    GradientBoostingRegressor(
        n_estimators=3000, learning_rate=0.05,
        max_depth=4, max_features='sqrt',
        min_samples_leaf=15, min_samples_split=10,
        loss='huber', random_state=42
    )
)

# XGBoost Regressor
xgboost = make_pipeline(
    RobustScaler(),
    XGBRegressor(
        learning_rate=0.01, n_estimators=6000,
        max_depth=4, min_child_weight=0,
        gamma=0.6, subsample=0.7,
        colsample_bytree=0.7, objective='reg:linear',
        nthread=-1, scale_pos_weight=1,
        seed=27, reg_alpha=0.00006, random_state=42
    )
)

# Light Gradient Boosting Regressor
lightgbm = make_pipeline(
    RobustScaler(),
    LGBMRegressor(
        objective='regression', num_leaves=6,
        learning_rate=0.01, n_estimators=7000,
        max_bin=200, bagging_fraction=0.8,
        bagging_freq=4, bagging_seed=8,
        feature_fraction=0.2, feature_fraction_seed=8,
        min_sum_hessian_in_leaf=11, verbose=-1,
        random_state=42
    )
)



# Stack up all the models above, optimized using lasso
stack_gen = StackingCVRegressor(
    regressors=(lasso_reg, decision_tree, gbr, xgboost, lightgbm, svr, knn_reg),
    meta_regressor=svr,
    use_features_in_secondary=True,
    random_state=42
)

# %% [markdown]
# ## train models
# Get cross validation scores for each model

# %%
scores = {}
regressors = {"Lasso": lasso_reg, 
              "Decision Tree": decision_tree, 
              "SVR": svr, 
              "KNN Regressor": knn_reg,
              "GB Regressor": gbr,
              "XGB Regressor": xgboost, 
              "LGB Regressor": lightgbm,
             }

for name, regressor in regressors.items():
    score = cv_rmse(regressor)  # Returns an array of cross-validated RMSE scores
    print(f"{name}: {score.mean():.4f} ({score.std():.4f})")
    scores[name] = (score.mean(), score.std())

# %%
# Extract mean and std scores for plotting
model_names = list(scores.keys())
mean_scores = [scores[n][0] for n in model_names]
std_scores = [scores[n][1] for n in model_names]

# Plot the predictions for each model
sns.set_style("white")
fig = plt.figure(figsize=(24, 12))

# Plot the pointplot
ax = sns.pointplot(x=model_names, y=mean_scores, markers='o', linestyles='-')

# Adding annotations
for i, score in enumerate(mean_scores):
    ax.text(i, score + 0.002, '{:.4f}'.format(score), horizontalalignment='left', size='large', color='black', weight='semibold')

plt.ylabel('Score', size=20, labelpad=12.5)
plt.xlabel('Model', size=20, labelpad=12.5)
plt.tick_params(axis='x', labelsize=13.5)
plt.tick_params(axis='y', labelsize=12.5)

plt.title('Scores of Models', size=20)

plt.show()

# %% [markdown]
# ## Fit the model

# %%
print("Processing lasso ...")
lasso_gen_model = lasso_reg.fit(X, y)

print("Processing decision_tree ...")
decision_tree_model = decision_tree.fit(X, y)

print("Processing svr ...")
svr_model = svr.fit(X, y)

print("Processing knn_reg ...")
knn_reg_model = knn_reg.fit(X, y)

print("Processing gbr ...")
gbr_model = gbr.fit(X, y)

print("Processing xgboost ...")
xgboost_model = xgboost.fit(X, y)

print("Processing lightgbm ...")
lightgbm_model = lightgbm.fit(X, y)

print("Processing stack_gen ...")
stack_gen_model = stack_gen.fit(np.array(X), np.array(y))

print("Finish processing.")

# %%
# Blend models in order to make the final predictions more robust to overfitting
# based on cross validation score
def blended_predictions(X):
    return ((0.15 * lasso_gen_model.predict(X)) + \
            (0.15 * svr_model.predict(X)) + \
            (0.15 * gbr_model.predict(X)) + \
            (0.15 * lightgbm_model.predict(X)) + \
            (0.4 * stack_gen_model.predict(np.array(X))))

# RMSLE score on train data:
# 0.06829440894001784

# %%
# Get final precitions from the blended model
blended_score = rmsle(y, blended_predictions(X))
scores['blended'] = (blended_score, 0)
print('RMSLE score on train data:')
print(blended_score)
# RMSLE score on train data:
# 0.06829440894001784

# %%
# Plot the predictions for each model
sns.set_style("white")
fig = plt.figure(figsize=(24, 12))

ax = sns.pointplot(x=list(scores.keys()), y=[score for score, _ in scores.values()], markers='o', linestyles='-')
for i, score in enumerate(scores.values()):
    ax.text(i, score[0] + 0.002, '{:.6f}'.format(score[0]), horizontalalignment='left', size='large', color='black', weight='semibold')

plt.ylabel('Score (RMSE)', size=20, labelpad=12.5)
plt.xlabel('Model', size=20, labelpad=12.5)
plt.tick_params(axis='x', labelsize=13.5)
plt.tick_params(axis='y', labelsize=12.5)

plt.title('Scores of Models', size=20)

plt.show()

# %% [markdown]
# ## change weight

# %% [markdown]
# # Submission & Prediction Result

# %% [markdown]
# ## Submission

# %%
# Prepare the submission DataFrame template
submission_template = pd.read_csv("/kaggle/input/house-prices-advanced-regression-techniques/sample_submission.csv")
# submission_template = pd.read_csv("./input/sample_submission.csv")

# %%
# Define a dictionary to store prediction methods and their models
models = {
    'lasso': lasso_gen_model,
    'DT': decision_tree_model,
    'svr': svr_model,
    'knn': knn_reg_model,
    'gbr': gbr_model,
    'xgboost': xgboost_model,
    'lightgbm': lightgbm_model,  # Corrected LightGBM model
    'stack': stack_gen_model
}


# Loop through each model and create a submission file
for model_name, model in models.items():
    print(f"Generating predictions for {model_name}...")
    
    # Make predictions
    predictions = model.predict(X_test)
    
    # If the target was log-transformed, reverse the transformation
    predictions = np.expm1(predictions)
    
    # Apply floor to ensure integer predictions (if required)
    predictions = np.floor(predictions)
    
    # Prepare the submission DataFrame
    submission = submission_template.copy()
    submission['SalePrice'] = predictions
    
    # Save the submission file
    submission_file_name = f"submission_{model_name}.csv"
    submission.to_csv(submission_file_name, index=False)
    print(f"Saved predictions for {model_name} to {submission_file_name}")

print("Finish prediction")

# %%
blended_preds = blended_predictions(X_test)
blended_preds = np.expm1(blended_preds)  # Reverse log transformation
blended_preds = np.floor(blended_preds)  # Floor predictions

submission = submission_template.copy()
submission['SalePrice'] = blended_preds

submission.to_csv("submission.csv", index=False)
print("Saved blended predictions to submission_blended.csv")


# %% [markdown]
# ## Performance

# %%
# no normalization(RobustScalar() method)

import matplotlib.pyplot as plt

scores_original = {
    "lasso": 0.12290,
    "DT": 0.19358,
    "SVR": 0.12284,
    "KNN": 0.17308,
    "GBR": 0.12625,
    "XGBoost": 0.16126,
    "LightGBM": 0.15654,
    "Stack": 0.12285,
    "Blended": 0.12206
}

scores_final = {
    'lasso': 0.12755,
    'DT': 0.19325,
    'svr': 0.12288,
    'knn': 0.19533,
    'gbr': 0.12577,
    'xgboost': 0.15694,
    'lightgbm': 0.16698,  
    'stack': 0.12226,
    'blended': 0.12142
}

# plotting
models = list(scores_original.keys())
scores_final_values = list(scores_final.values())
scores_original_values = list(scores_original.values())

plt.figure(figsize=(10, 6))
plt.plot(models, scores_final_values, marker='o', label='Feature Engineered Scores')
plt.plot(models, scores_original_values, marker='s', label='Original Scores')

plt.xlabel('Models')
plt.ylabel('Scores')
plt.title('Model Performance with and without Feature Engineering')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



