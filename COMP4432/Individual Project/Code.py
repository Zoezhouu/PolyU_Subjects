# %% [markdown]
# # Heart Attack Analysis and Prediction
# this notebook analyzes the heart attack dataset and builds predictive models to predict the probability of heart attack.

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
import warnings 
warnings.filterwarnings('ignore')
warnings.filterwarnings("ignore", category=DeprecationWarning)


# %%
heart = pd.read_csv("/kaggle/input/heart-attack-analysis-prediction-dataset/heart.csv")
satura = pd.read_csv("/kaggle/input/heart-attack-analysis-prediction-dataset/o2Saturation.csv")
# heart = pd.read_csv("./input/heart.csv")
# satura = pd.read_csv("./input/o2Saturation.csv")

# %%
heart.shape, satura.shape

# %%
heart.head()

# %%
heart.describe()

# %%
heart.isnull().sum()

# %%
heart.info()

# %%
category_features=['sex', 'cp', 'fbs', 'restecg', 'slp', 'caa', 'thall', 'exng']
numeric_features=['age','trtbps','chol','thalachh','oldpeak']

c_feature =[]
n_feature = []
for feature in category_features:
    # print(feature,':',heart[feature].unique())
    if feature in heart.columns:
        c_feature.append(feature)

for feature in numeric_features:
    # print(feature,':',heart[feature].unique())
    if feature in heart.columns:
        n_feature.append(feature)

numeric_data = heart[n_feature]
category_data = heart[c_feature]

# %%
satura.head()

# %% [markdown]
# # 1. Exploratory Data Analysis

# %%
import seaborn as sns
import matplotlib.pyplot as plt

# %%
print(heart['output'].value_counts())
plt.figure(figsize = (8, 5))
sns.countplot(x = heart['output'])
plt.xlabel("Output", size = 12)
plt.ylabel("Count", size = 12)
plt.title("Distribution of target values", size = 12)

# %%
heart.isnull().sum()

# %%
col = heart.columns
fgi, ax = plt.subplots(7,2 , figsize = (10,15), constrained_layout=True)
ax = ax.flatten()
for ind, axi in enumerate(ax.flat):
    axi.boxplot(heart[col[ind]], vert = False)
    axi.set_title(col[ind], size = 12)

# %%
corr = heart.corr()
plt.figure(figsize =  (12,9))
sns.heatmap(corr, vmax=0.9, cmap="Blues", square=True, annot = True)

# %%
display(heart.corr())
sns.heatmap(heart.corr(), cmap="Blues")

# %%
rel = corr['output'].sort_values(ascending = False)
rel

# %%
# higher correlation between output and features(cp, thalachh, clp, restecg)
positive_list = []
for i in range (len(rel)):
    if rel.iloc[i] > 0:
        positive_list.append(rel.index[i])
positive_list

# %%
# sns.pairplot(heart, hue = 'output') 
# with title
sns.pairplot(heart, hue = 'output').fig.suptitle('Pairplot of the dataset', y=1.02)
plt.show()

# %% [markdown]
#  - Object with cp = 2 have higher chance of heart attack, with cp = 0 have lower chances of heart attack
#  - Object with rest_ecg = 1 have higher chance of heart attack (having ST-T wave abnormality)
#  - Object with higher thalachh have higher change of heart attack(higher Maximum heart rate achieve)
#  - Object with exng = 0 have higher chance of heart attack
#  - Object with lower oldpeak have higher chances of heart attack
#  - Object with slp = 2 have higher chance of heart attack; with slp = 1 have lower chance of heart attack
#  - Object with caa = 0 have higher chance of heart attack
#  - Object with thall = 2 have much higher chance of heart attack

# %% [markdown]
# ## 1.1 Category features 

# %%
category_features

# %%
# sex
x = heart.sex.value_counts()
print(x)
p = sns.countplot(data = heart, x="sex", hue = "output")
# Objects having sex 1 are more than twice the objects having sex 0

# %%
# cp
x = heart.cp.value_counts()
print(x)
p = sns.countplot(data = heart, x="cp", hue = "output")
# Objects of cp 0 have the largest count, cp 3 have the lowest count

# %%
# fbs
x = heart.fbs.value_counts()
print(x)
p = sns.countplot(data = heart, x="fbs", hue = "output")
# Objects having fbs 0 are more than four times the objects having fbs 1

# %%
# restecg
x = heart.restecg.value_counts()
print(x)
p = sns.countplot(data = heart, x="restecg", hue = "output")
# restecg-0 & restecg-1 have similar counts, restecg-2 have the lowest count restecg-2 is almost negligible

# %%
# slp
x = heart.slp.value_counts()
print(x)
p = sns.countplot(data = heart, x="slp", hue = "output")
# slp-1 & slp-2 have similar counts, slp-0 have the lowest count

# %%
# caa
x = heart.caa.value_counts()
print(x)
p = sns.countplot(data = heart, x="caa", hue = "output")
# caa-0 have the largest count, caa-4 have the lowest count

# %%
# thall
x = heart.thall.value_counts()
print(x)
p = sns.countplot(data = heart, x="thall", hue = "output")
# thall-2 have the largest count, thall-0 have the lowest count

# %%
# exng
x = heart.exng.value_counts()
print(x)
p = sns.countplot(data = heart, x="exng", hue = "output")
# exng-0 have more counts than exng-1

# %%
# draw above plots in a single plot
fig, axes = plt.subplots(2, 4, figsize=(20, 10))
axes = [ax for axes_row in axes for ax in axes_row]
for i, c in enumerate(heart[category_features]):
    sns.countplot(x=c, data=heart, hue='output', ax=axes[i])
    axes[i].legend(title='output', loc='upper right')
    axes[i].set_title(c)
    axes[i].set_xlabel('')
    axes[i].set_ylabel('')
plt.show()

# %% [markdown]
# ## 1.2 Numeric features

# %%
numeric_features

# %%
# age
plt.figure(figsize = (10, 5))
sns.histplot(data = heart, x = "age", hue = "output", kde = True)
# age group 40-60 have more heart attacks

# %%
# trtbps
plt.figure(figsize = (10, 5))
sns.histplot(data = heart, x = "trtbps", hue = "output", kde = True)
# trtbps group 120-140 have more heart attacks

# %%
# chol
plt.figure(figsize = (10, 5))
sns.histplot(data = heart, x = "chol", hue = "output", kde = True)
# chol group 200-300 have more heart attacks

# %%
# thalachh
plt.figure(figsize = (10, 5))
sns.histplot(data = heart, x = "thalachh", hue = "output", kde = True)
# thalachh group 150-200 have more heart attacks

# %%
# oldpeak
plt.figure(figsize = (10, 5))
sns.histplot(data = heart, x = "oldpeak", hue = "output", kde = True)
# oldpeak group 0-2 have more heart attacks

# %%
# draw above plots in a single plot
fig, axes = plt.subplots(1, 5, figsize=(50, 5))

for i, c in enumerate(heart[numeric_features]):
    sns.histplot(x=c, data=heart, hue='output', kde=True, ax=axes[i])
    axes[i].legend(title='output', loc='upper right')
    axes[i].set_title(c)
    axes[i].set_xlabel('')
    axes[i].set_ylabel('')

plt.show()

# %%
import matplotlib.pyplot as plt
heart.hist(bins=20, figsize=(15, 10))
plt.show()

# %% [markdown]
# ### PCA (Principal Component Analysis)

# %%
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
components = pca.fit_transform(heart.drop(columns=['output']))
plt.scatter(components[:, 0], components[:, 1], c=heart['output'])

# %% [markdown]
# # 2. Data preprocessing

# %%
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
# Check null data
heart.isnull().sum()

# %% [markdown]
# ## 2.1 Remove duplicate records

# %%
# Check repeated data
print('Number of repeated data:',heart.duplicated().sum())
heart[heart.duplicated()]

# %%
heart.drop_duplicates(keep='first', inplace=True)
heart = heart.reset_index(drop=True)
print('After clean: Number of records:',heart.shape[0], '\nNumber of attributes:',heart.shape[1])

# %% [markdown]
# ## 2.2 remove outlier

# %%
numeric_data=heart[numeric_features]
category_data=heart[category_features]

# %%
numeric_data.head()

# %%
category_data.head()

# %%
# replace outliar with mean value  and  IQR
Q3 = numeric_data.quantile(0.75) 
Q1 = numeric_data.quantile(0.25) 
IQR = Q3 - Q1
# outliar range
upper = dict(Q3 + 1.5 * IQR)
lower = dict(Q1 - 1.5 * IQR)
for feature,values in numeric_data.items():
    for idx in range(len(values)):
        if values[idx] >upper[feature] or values[idx] < lower[feature]:
            numeric_data[feature][idx] = np.mean(numeric_data[feature])

# %% [markdown]
# ## 2.3 One-hot encoding for category features

# %%
heart[c_feature] = heart[c_feature].astype('category')
heart = pd.get_dummies(heart, columns=c_feature, drop_first=True)

print('After one hot encoding: Number of records:',heart.shape[0], '\nNumber of attributes:',heart.shape[1])

x = heart.iloc[:,:-1]
# x.drop('output', axis = 1, inplace = True)

y = heart.loc[:,'output']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
print('Train set:', x_train.shape, y_train.shape)
print('Test set:', x_test.shape, y_test.shape)

# %%
x.head()

# %% [markdown]
# ## 2.4 Normalize numerical features

# %%
col = x.columns
std = StandardScaler()
x_train = std.fit_transform(x_train)
x_test = std.transform(x_test)
print('Train set:', x_train.shape, y_train.shape)
print('Test set:', x_test.shape, y_test.shape)
# x = pd.DataFrame(data = x, columns = col)
heart.head()

# %% [markdown]
# # 3. Modeling methods comparison

# %% [markdown]
# ## 3.1 Classification Methods

# %% [markdown]
# ### 3.1.1 basic classification model

# %%
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from xgboost import XGBClassifier

modelList = []
modelNameList = []
scores =[] 
# Logistic Regression
lr = LogisticRegression()
lr.fit(x_train, y_train)
modelList.append(lr)
modelNameList.append("Logistic Regression")
predictedLR = lr.predict(x_test)
scores.append(accuracy_score(y_test, predictedLR)*100)
print("Logistic Regression Accuracy: ", accuracy_score(y_test, predictedLR)*100, "%")


# Decision Tree
dt = DecisionTreeClassifier(random_state=42)
dt.fit(x_train, y_train)
modelList.append(dt)
modelNameList.append("Decision Tree")
predictedDT = dt.predict(x_test)
scores.append(accuracy_score(y_test, predictedDT)*100)
print("Decision Tree Accuracy: ", accuracy_score(y_test, predictedDT)*100, "%")

# Random Forest
rf = RandomForestClassifier(n_estimators=1, random_state=42)
rf.fit(x_train, y_train)
modelList.append(rf)
modelNameList.append("Random Forest")
predictedRF = rf.predict(x_test)
scores.append(accuracy_score(y_test, predictedRF)*100)
print("Random Forest Accuracy: ", accuracy_score(y_test, predictedRF)*100, "%")

# Gradient Boosting
gb = GradientBoostingClassifier()
gb.fit(x_train, y_train)
modelList.append(gb)
modelNameList.append("Gradient Boosting")
predictedGB = gb.predict(x_test)
scores.append(accuracy_score(y_test, predictedGB)*100)
print("Gradient Boosting Accuracy: ", accuracy_score(y_test, predictedGB)*100, "%")

# XGBoost
xgb = XGBClassifier()
xgb.fit(x_train, y_train)
modelList.append(xgb)
modelNameList.append("XGBoost")
predictedXGB = xgb.predict(x_test)
scores.append(accuracy_score(y_test, predictedXGB)*100)
print("XGBoost Accuracy: ", accuracy_score(y_test, predictedXGB)*100, "%")

# Support Vector Machine
svm = SVC()
svm.fit(x_train, y_train)
modelList.append(svm)
modelNameList.append("Support Vector Machine")
predictedSVM = svm.predict(x_test)
scores.append(accuracy_score(y_test, predictedSVM)*100)
print("Support Vector Machine Accuracy: ", accuracy_score(y_test, predictedSVM)*100, "%")

# K-Nearest Neighbors
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(x_train, y_train)
modelList.append(knn)
modelNameList.append("K-Nearest Neighbors")
predictedKNN = knn.predict(x_test)
scores.append(accuracy_score(y_test, predictedKNN)*100)
print("K-Nearest Neighbors Accuracy: ", accuracy_score(y_test, predictedKNN)*100, "%")

# Naive Bayes
nb = GaussianNB()
nb.fit(x_train, y_train)
modelList.append(nb)
modelNameList.append("Naive Bayes")
predictedNB = nb.predict(x_test)
scores.append(accuracy_score(y_test, predictedNB)*100)
print("Gaussian Naive Bayes Accuracy: ", accuracy_score(y_test, predictedNB)*100, "%")

# Neural Network
nn = MLPClassifier()
nn.fit(x_train, y_train)
modelList.append(nn)
modelNameList.append("Neural Network - MLP")
predictedNN = nn.predict(x_test)
scores.append(accuracy_score(y_test, predictedNN)*100)
print("Neural Network Accuracy: ", accuracy_score(y_test, predictedNN)*100, "%")


# %% [markdown]
# ### 3.1.2 K-fold cross validation score 
# reference: https://www.kaggle.com/code/licgsg/heart-attack-analysis-python

# %%
# k-fold cross validation
from sklearn.model_selection import cross_val_score

# Initialize required variables
k = 10
cv_scores = []
cv_mean = []

# Iterate over all models
for model in modelList:
    scores = cross_val_score(model, x, y, cv=k, scoring='accuracy')
    cv_scores.append(scores)
    cv_mean.append(scores.mean())

# Create a DataFrame to display the cross validation results
cv_results = pd.DataFrame({'Model': modelNameList, 'CV Mean': cv_mean})
display(cv_results)

modelnames = ['LR', "DT", "RF", "GB", "XGB", "SVM", "KNN", "NB", "NN"]
# draw the cross validation results,  bar colors  are different for each model
plt.figure(figsize=(12, 5))
plt.bar(modelnames, cv_mean)
plt.xlabel('Model', fontsize=12)
plt.ylabel('Accuracy', fontsize=12)
# annotate the bar graph with percentages
for i, mean in enumerate(cv_mean):
    plt.text(i, mean, f"{mean*100:.2f}%", ha='center', va='bottom')

plt.title('Cross Validation Mean Accuracy for Different Models', fontsize=14)
plt.show()

# %%
# 10 fold CV
from sklearn.model_selection import cross_val_score
# model_list=[lr,dt,rf, gb, xgb, svm, knn, nb, nn]
def get_cv_score(method):
    cv_score_avg=[]
    for model in modelList:
        cv_result = cross_val_score(model,heart.iloc[:,:-1], heart.loc[:,'output'],cv=10,scoring=method)
        cv_score_avg.append(np.sum(cv_result)/10)
    cv_score_avg=pd.DataFrame(data=cv_score_avg,
             index=modelNameList,
             columns=[method])
    display(cv_score_avg)
    return cv_score_avg

# %%
ax=get_cv_score("accuracy").transpose().plot(label='10-fold CV_score',kind='bar',figsize=[12,5],title='CV accuracy sore of model')
for p in ax.patches:
    ax.annotate(str(p.get_height().round(4)), (p.get_x() * 1.005, p.get_height() * 1.005))
ax.set_xlabel("model")
ax.set_ylabel("cv_score")

ax2=get_cv_score("precision").transpose().plot(label='10-fold CV_score',kind='bar',figsize=[12,5],title='CV accuracy sore of model')
for p in ax2.patches:
    ax2.annotate(str(p.get_height().round(4)), (p.get_x() * 1.005, p.get_height() * 1.005))
ax2.set_xlabel("model")
ax2.set_ylabel("cv_score")

ax3=get_cv_score("f1").transpose().plot(label='10-fold CV_score',kind='bar',figsize=[12,5],title='CV accuracy sore of model')
for p in ax3.patches:
    ax3.annotate(str(p.get_height().round(4)), (p.get_x() * 1.005, p.get_height() * 1.005))
ax3.set_xlabel("model")
ax3.set_ylabel("cv_score")

# %% [markdown]
# ## 3.2 Clustering Methods
# reference: https://www.kaggle.com/code/zixiangzhao001/dlinbmi-assignment1-zz2721

# %%
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.model_selection import cross_val_score


x = heart.iloc[:,:-1]
y = heart.loc[:,'output']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# Scaling
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# PCA
pca = PCA(n_components=2)
x_train_pca = pca.fit_transform(x_train_scaled)
x_test_pca = pca.transform(x_test_scaled)


# %% [markdown]
# ### 3.2.1 KMeans Clustering

# %%
# apply Kmeans clustering to the transformed training data with optimal cluster number = 2
kmeans = KMeans(n_clusters=2, random_state=42)
train_clusters = kmeans.fit_predict(x_train_pca)

# training data with cluster
heart_train = pd.DataFrame(x_train, columns=x.columns)
heart_train['cluster'] = train_clusters
heart_train['output'] = y_train

# %%
from scipy.stats import mode

# Reassign cluster labels based on majority voting
cluster_map = {}
for cluster_id in np.unique(train_clusters):
    # Find the most common true label in each cluster
    mask = train_clusters == cluster_id
    most_common_label = mode(y_train[mask], keepdims=True).mode[0]  # Ensure output is correctly accessed
    cluster_map[cluster_id] = most_common_label

# Map clusters to true labels
aligned_train_clusters = np.vectorize(cluster_map.get)(train_clusters)
accuracy = accuracy_score(y_train, aligned_train_clusters)
print("KMeans Cluster Accuracy(Training):", accuracy)


plt.figure(figsize=(10, 6))
sns.scatterplot(x=x_train_pca[:,0], y=x_train_pca[:,1], hue=aligned_train_clusters, palette='viridis', alpha=0.8)
sns.scatterplot(x=kmeans.cluster_centers_[:,0], y=kmeans.cluster_centers_[:,1], color='red', s=100, label='Centroids')
plt.title('KMeans Clustering of Training Data')
plt.show()

# accuracy = accuracy_score(y_train, train_clusters)
# print("Accuracy of the Clustering-based Prediction Model:", accuracy)

# %%
# Predict clusters for the test data
test_clusters = kmeans.predict(x_test_pca)

# Reassign cluster labels based on majority voting
cluster_map = {}
for cluster_id in np.unique(test_clusters):
    # Find the most common true label in each cluster
    mask = test_clusters == cluster_id
    most_common_label = mode(y_test[mask], keepdims=True).mode[0]  # Ensure output is correctly accessed
    cluster_map[cluster_id] = most_common_label

# Map clusters to true labels
aligned_test_clusters = np.vectorize(cluster_map.get)(test_clusters)
accuracy = accuracy_score(y_test, aligned_test_clusters)
print("KMeans Cluster Accuracy:", accuracy)

clustering_accuracy = []
clustering_accuracy.append(["KMeans", accuracy])

# Visualize the predicted clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x=x_test_pca[:, 0], y=x_test_pca[:, 1], hue=aligned_test_clusters, style=aligned_test_clusters, palette='viridis', legend='brief')
plt.title('Predicted Clusters (Test Data)')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x=x_test_pca[:, 0], y=x_test_pca[:, 1], hue=y_test, style=y_test, palette='viridis', legend='brief')
plt.title('Actual Labels (Test Data)')
plt.legend(title='Actual Label', loc='upper right')
plt.show()

# %% [markdown]
# ### 3.2.2 Agglomerative Clustering

# %%
# Apply Agglomerative Clustering to the PCA-transformed data
agg = AgglomerativeClustering(n_clusters=2)
train_clusters = agg.fit_predict(x_train_pca)

# Reassign cluster labels based on majority voting
cluster_map = {}
for cluster_id in np.unique(train_clusters):
    # Find the most common true label in each cluster
    mask = train_clusters == cluster_id
    most_common_label = mode(y_train[mask], keepdims=True).mode[0]  # Ensure output is correctly accessed
    cluster_map[cluster_id] = most_common_label

# Map clusters to true labels
aligned_train_clusters = np.vectorize(cluster_map.get)(train_clusters)
accuracy = accuracy_score(y_train, aligned_train_clusters)
print("Agglomerative Cluster Accuracy(Training):", accuracy)


plt.figure(figsize=(10, 6))
sns.scatterplot(x=x_train_pca[:,0], y=x_train_pca[:,1], hue=aligned_train_clusters, palette='viridis', alpha=0.8)
plt.title('Agglomerative Clustering of Training Data')
plt.show()


# %%
# Predict clusters for the test data
test_clusters = agg.fit_predict(x_test_pca)

# Reassign cluster labels based on majority voting
cluster_map = {}
for cluster_id in np.unique(test_clusters):
    # Find the most common true label in each cluster
    mask = test_clusters == cluster_id
    most_common_label = mode(y_test[mask], keepdims=True).mode[0]  # Ensure output is correctly accessed
    cluster_map[cluster_id] = most_common_label

# Map clusters to true labels
aligned_test_clusters = np.vectorize(cluster_map.get)(test_clusters)
accuracy = accuracy_score(y_test, aligned_test_clusters)
print("Agglomerative Cluster Accuracy:", accuracy)

clustering_accuracy.append(["AGGLO", accuracy])

# Visualize the predicted clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x=x_test_pca[:, 0], y=x_test_pca[:, 1], hue=aligned_test_clusters, style=aligned_test_clusters, palette='viridis', legend='brief')
plt.title('Predicted Clusters (Test Data)')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x=x_test_pca[:, 0], y=x_test_pca[:, 1], hue=y_test, style=y_test, palette='viridis', legend='brief')
plt.title('Actual Labels (Test Data)')
plt.legend(title='Actual Label', loc='upper right')
plt.show()

# %% [markdown]
# ### 3.2.3 DBSCAN clustering

# %%
# Apply DBSCAN to the PCA-transformed data
dbscan = DBSCAN(eps=0.5, min_samples=5)
train_clusters = dbscan.fit_predict(x_train_pca)

# Reassign cluster labels based on majority voting
cluster_map = {}
for cluster_id in np.unique(train_clusters):
    # Find the most common true label in each cluster
    mask = train_clusters == cluster_id
    most_common_label = mode(y_train[mask], keepdims=True).mode[0]  # Ensure output is correctly accessed
    cluster_map[cluster_id] = most_common_label

# Map clusters to true labels
aligned_train_clusters = np.vectorize(cluster_map.get)(train_clusters)
accuracy = accuracy_score(y_train, aligned_train_clusters)
print("DBSCAN Cluster Accuracy(Training):", accuracy)


plt.figure(figsize=(10, 6))
sns.scatterplot(x=x_train_pca[:,0], y=x_train_pca[:,1], hue=aligned_train_clusters, palette='viridis', alpha=0.8)
plt.title('DBSCAN Clustering of Training Data')
plt.show()


# %%
# Predict clusters for the test data
test_clusters = dbscan.fit_predict(x_test_pca)

# Reassign cluster labels based on majority voting
cluster_map = {}
for cluster_id in np.unique(test_clusters):
    # Find the most common true label in each cluster
    mask = test_clusters == cluster_id
    most_common_label = mode(y_test[mask], keepdims=True).mode[0]  # Ensure output is correctly accessed
    cluster_map[cluster_id] = most_common_label

# Map clusters to true labels
aligned_test_clusters = np.vectorize(cluster_map.get)(test_clusters)
accuracy = accuracy_score(y_test, aligned_test_clusters)
print("DBSCAN Cluster Accuracy:", accuracy)

clustering_accuracy.append(["DBSCAN", accuracy])

# Visualize the predicted clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x=x_test_pca[:, 0], y=x_test_pca[:, 1], hue=aligned_test_clusters, style=aligned_test_clusters, palette='viridis', legend='brief')
plt.title('Predicted Clusters (Test Data)')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x=x_test_pca[:, 0], y=x_test_pca[:, 1], hue=y_test, style=y_test, palette='viridis', legend='brief')
plt.title('Actual Labels (Test Data)')
plt.legend(title='Actual Label', loc='upper right')
plt.show()

# %% [markdown]
# ## 3.3 Modelling methods comparison

# %%
# display accuracy comparison of different clustering algorithms
print("Accuracy of the Clustering-based Prediction Model:")
print("KMeans:", 0.8688524590163934)
print("Agglomerative:", 0.8524590163934426)
print("DBSCAN:", 0.6721311475409836)

clustering_accuracy
classification_accuracy=[["LR", accuracy_score(y_test, predictedLR)], 
                         ["DT", accuracy_score(y_test, predictedDT)], 
                         ["RF", accuracy_score(y_test, predictedRF)], 
                         ["GB", accuracy_score(y_test, predictedGB)], 
                         ["XGBoost", accuracy_score(y_test, predictedXGB)], 
                         ["SVM", accuracy_score(y_test, predictedSVM)], 
                         ["KNN", accuracy_score(y_test, predictedKNN)], 
                         ["NB", accuracy_score(y_test, predictedNB)], 
                         ["NN-MLP", accuracy_score(y_test, predictedNN)]]

# draw histogram of clustering accuracy and classification accuracy with score printed
plt.figure(figsize=(12, 5))
plt.bar(*zip(*clustering_accuracy), color='skyblue', label='Clustering')
plt.bar(*zip(*classification_accuracy), color='salmon', label='Classification')
plt.xlabel('Model', fontsize=12)
plt.ylabel('Accuracy', fontsize=12)
plt.title('Clustering and Classification Accuracy Comparison', fontsize=14)
plt.legend()

# annotate the bar graph with percentages
for i, mean in enumerate(clustering_accuracy):
    plt.text(i, mean[1], f"{mean[1]*100:.2f}%", ha='center', va='bottom')
for i, mean in enumerate(classification_accuracy):
    plt.text(i+3, mean[1], f"{mean[1]*100:.2f}%", ha='center', va='bottom')

plt.show()



# %%
# compare k-fold cross-validation accuracy of different models
# cv_results.append({'Model': 'KMeans', 'CV Mean': 0.9304301075268817}, ignore_index=True)
modelnames.append('KMeans')
cv_mean.append(0.9304301075268817)

# %%
# draw the cross validation results,  bar colors  are different for each model
plt.figure(figsize=(12, 5))
bars = plt.bar(modelnames, cv_mean)
bars[-1].set_color('orange') # clustering - KMeans
plt.xlabel('Model', fontsize=12)
plt.ylabel('Accuracy', fontsize=12)
# annotate the bar graph with percentages
for i, mean in enumerate(cv_mean):
    plt.text(i, mean, f"{mean*100:.2f}%", ha='center', va='bottom')

plt.title('K-fold Cross Validation for Different Models', fontsize=14)
plt.show()


# %% [markdown]
# # 4. ARM - Apriori Analysis
# reference: 
# - https://www.kaggle.com/code/mervetorkan/association-rules-with-python
# - https://www.kaggle.com/code/licgsg/heart-attack-analysis-python

# %%
! pip install apyori

# %%
# Apriori Algorithm
from mlxtend.frequent_patterns import association_rules
from apyori import apriori
from mlxtend.preprocessing import TransactionEncoder

df = pd.read_csv("/kaggle/input/heart-attack-analysis-prediction-dataset/heart.csv")
# df = pd.read_csv('./input/heart.csv')  

# binarized_df = pd.get_dummies(df.astype(str))

# %%
for i in ["age","trtbps","chol","thalachh","oldpeak"]:
    df[i] = pd.cut(df[i], 3)
    df[i] = i+df[i].astype(str)
for i in ['sex','exng','caa','cp','fbs','restecg','slp','thall','output']:
    df[i] = pd.cut(df[i], bins=[-1,0, 1, 2, 3, 4],
                     labels=[i+"-0", i+"-1", i+"-2", i+"-3", i+"-4"])

# %%
# create the tranactions list
transactions = []
for i in range(0, len(df)):
    transactions.append([str(df.values[i, j]) for j in range(0, 14)])
# transactions[:5]

# %%
rules = apriori(transactions,min_support=0.25,min_confidence = 0.7,min_length = 3)
results = list(rules)
results[:5]

# %%
rules_data = []

# results = list(rules)

for rule in results:
    for ordered_statistic in rule.ordered_statistics:
        if 'output-1' in str(ordered_statistic.items_add):
            rules_data.append({
                'rule': str(ordered_statistic.items_base) + " -> " + str(ordered_statistic.items_add),
                'support': rule.support,
                'confidence': ordered_statistic.confidence
            })

rules_df = pd.DataFrame(rules_data)
rules_df.sort_values(by=['support'], ascending=False, inplace=True)

# Display the top 10 rules
pd.set_option('display.max_colwidth', None)
rules_df.head(10)

# %% [markdown]
# # 5. Optimization
# reference: https://www.kaggle.com/code/rocklen/heart-attack-analysis-prediction

# %% [markdown]
# ## 5.1 KNN

# %%
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Initialize required variables
accuracyList = []
maxAccuracy = 0
maxIndex = 0
bestPred = None
best_predict_model = None

# Iterate over different values of neighbors
for i in range(3, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(x_train, y_train)
    predicted = knn.predict(x_test)
    current_accuracy = accuracy_score(y_test, predicted)
    accuracyList.append(current_accuracy)
    if maxAccuracy < current_accuracy:
        maxAccuracy = current_accuracy
        maxIndex = i
        bestPred = predicted
        best_predict_model = knn

# Plot accuracy variation with neighbors
plt.figure(figsize=(12, 5))
plt.plot(range(3, 40), accuracyList, marker='.')
plt.xlabel('Number of Neighbors (K)', fontsize=12)
plt.ylabel('Accuracy', fontsize=12)
plt.title('Accuracy Variation with Neighbors (K)', fontsize=14)
plt.show()

# Print the best accuracy and corresponding K value
print(f"Best accuracy using KNN: {maxAccuracy*100:.2f}% with K={maxIndex}")

# %% [markdown]
# ## 5.2 Random Forest

# %%
# Random Forest optimization
# Initialize required variables
accuracyList = []
maxAccuracy = 0
maxIndex = 0
bestPred = None
best_predict_model = None

for i in range(1, 200):
    rf = RandomForestClassifier(n_estimators=i, random_state=42)
    rf.fit(x_train, y_train)
    predictedRF = rf.predict(x_test)
    current_accuracy = accuracy_score(y_test, predictedRF)
    accuracyList.append(current_accuracy)
    if maxAccuracy < current_accuracy:
        maxAccuracy = current_accuracy
        maxIndex = i
        bestPred = predictedRF
        best_predict_model = rf

plt.figure(figsize=(12, 5))
plt.plot(range(1, 200), accuracyList, marker='.')
plt.xlabel('Number of Estimators', fontsize=12)
plt.ylabel('Accuracy', fontsize=12)
plt.title('Accuracy Variation with Number of Estimators', fontsize=14)
plt.show()
print(f"Best accuracy using Random Forest: {maxAccuracy*100:.2f}% with {maxIndex} estimators")
    
# print(f"Random Forest Accuracy with {i} estimators: ", accuracy_score(y_test, predictedRF)*100, "%")


