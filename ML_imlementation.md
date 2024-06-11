# Data preprocessing

## splitting 
- we divide into two *training set* and *test set*
- use *from sklearn.model_selection import train_test_split* then we can use train_test_split method to  split data 
        *X_train,X_valid,y_train,y_valid = train_test_split(X, y, random_state = 0,train_size = 0.8,test_size = 0.2)* 
        X here is independent features and y is target varaible random state = 69 ensures data is split randomly with code 69 wheneer we use 69 it will give the same division 

## feature scaling
 (Without feature scaling if some features have much larger values than others(they are given more wt by models), they can dominate the training process and lead to a less accurate model.)
 we can solve above issue by transforming all features in similar range

- *Normalizing* : all values are transformed to lie inside 0 and 1 
    Formulae : X = (X - X_min) / (X_max - X_min)
- *Standardization* : all values are centered around 0 with 0 being the mean and standard deviation being 1
    Formulae : X = (X-X_min) / X_std_deviation
    '''
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train[cols_to_transform] = sc.fit_transform(X_train[cols_to_transform])
    X_valid[cols_to_transform] = sc.transform(X_valid[cols_to_transform])
    '''

 The decision between normalization and standardization depends on your specific problem and the machine learning algorithm you're using. There's no strict rule dictating which to choose. The best way to decide is by experimenting with both techniques.Normalisation is a good choice when we don't know the underlying distribution of our data and Standardization is good to use when our data follows a normal distribution

## Avoiding Data Lekage:
    Data leakage occurs when information from the test set unintentionally influences the training process. If we were to apply both normalization and standardization to both the training and testing data, the model might inadvertently learn information about the test set during training. This can lead to overly optimistic performance estimates and a false sense of the model's effectiveness.
    
    To prevent data leakage, it's crucial to fit the scaling technique (normalization or standardization) using only the training data. Then, use the same fitted technique to transform the testing data. This ensures a fair evaluation of the model's performance and prevents any bias introduced by using information from the test set during training.

## Handling Mising Values:
    giving NaN values to a model as input will generate an error therefore we need to do something
-*Handling by dropping columns with NaN values* : (they may not be effective if feature is highly influence target variable)
-*Handling by imputation* : we can use inbuilt imputers from sckitlearn
    -*By replacing mising with mean/median* : 

from sklearn.impute import SimpleImputer

my_imputer = SimpleImputer(strategy = "mean/median") 
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train)) // we used fit and transform to first fit according to X_train dataset and then transform X_train
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))


imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns

### Handling by imputation and extension
we can add on imputation by creating column with bool values which signify if the feature was mising or not (slighlty better than just imputation)

## Handling Categorical Variables
 giving str type values to models results into a error

### drop categorical columns : 
seems logical if it doesnt influence target variable

### Ordinal Encoding 
This approach assumes an ordering of the categories: "Never" (0) < "Rarely" (1) < "Most days" (2) < "Every day" (3) that is replaces Never with 0 Rarely with 1 in object cols

object_cols : col with data type of object

from sklearn.preprocessing import OrdinalEncoder
ordinal_encoder = OrdinalEncoder()
label_X_train[object_cols] = ordinal_encoder.fit_transform(X_train[object_cols])
label_X_valid[object_cols] = ordinal_encoder.transform(X_valid[object_cols])

This is a common approach that is simpler than providing custom labels; however, we can expect an additional boost in performance if we provide better-informed labels for all ordinal variables.

### One Hot Encoding  
typical hot encoding ![alt text](https://storage.googleapis.com/kaggle-media/learn/images/TW5m0aJ.png) 

from sklearn.preprocessing import OneHotEncoder
*Apply one-hot encoder to each column with categorical data*
OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(X_train[object_cols]))
OH_cols_valid = pd.DataFrame(OH_encoder.transform(X_valid[object_cols]))

*One-hot encoding removed index; put it back*
OH_cols_train.index = X_train.index
OH_cols_valid.index = X_valid.index

*Remove categorical columns (will replace with one-hot encoding)*
num_X_train = X_train.drop(object_cols, axis=1)
num_X_valid = X_valid.drop(object_cols, axis=1)

*Add one-hot encoded columns to numerical features*
OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1)

*Ensure all columns have string type*
OH_X_train.columns = OH_X_train.columns.astype(str)
OH_X_valid.columns = OH_X_valid.columns.astype(str)

### custom encoding 
we can use create a dict with custom encoding as do df.column_name.replace(dict , inplace = True)

# Fitting 
we first insantiate a model then 
we usel model.fit(Data) to train the model 
## Supervised Learning Algos

### DecesionTrees
#### Decesion Tree Regressor  
    from sklearn.tree import DecisionTreeRegressor
    model = DecesionTreeRegressor(random_state = 42,max_leaf_nodes = 50)
*max_leaf_nodes* : can be used to control overfitting or underfiiting of the model u need to find the best number of max_leaf_nodes for the model 
#### RandomForstRegressor
    from sklearn.ensemble import RandomForestRegressor
    model = RandomForestRegressor(random_state = 1,n_estimators = 150)
A random forest is a meta estimator that fits a number of decision tree regressors on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting
**n_estimators** : specify the number of decesion trees in your model
#### LinearRegressor
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()

#### UnsupervisedLearning - K-means Clustering 
    from sklearn.cluster import KMeans
    '''how to intialize a model n_clusters determine how many cusotmers you want and k-means++ is used to  speed up the centroid fidning '''
    model = Kmeans(n_clusters=n,init='k-means++',random_state = 69)
    #here are some usefull attributes
    #model.inertia_ returns the WCSS value of model which is used in calculating the optimal cluster number
    model.inertia_
    #model.fit(X) used to fit the model
    '''model.predict(X) will give out the labels accordingly to the cluster it has created how the model has numbered the clusters
    it returns series of labels and ofcourse indexes'''
    model.predict(X)
    '''model.cluster_centers it returns a dataframe consisting of the centroids's features (it will have thoose features which were there in the train_dataset the model was trained on). the centroid are formed during training of the data'''
    model.cluster_centers

The main problem is how to decide howm manyy clusters are optimal now this could be done by experimenting and in experimenting we follow elbow method. the method says the optimal value is the point of kink in the graph of WCSS on y axis and no of clusters on the x-axis..


# Pipeline
We can use pipeline for organizing preproccessing and modeling tasks
it also reduces coding errors and makes working different sets of data easier 
Here how to use it 
## Code
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline
    Preprocessing for numerical data
    numerical_transformer = SimpleImputer(strategy='constant')
    # Preprocessing for categorical data
    categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    # Bundle preprocessing for numerical and categorical data
    preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    my_pipeline = Pipeline(steps=[('preprocessor', preprocessor),('model', model)])
    my_pipeline.fit(X_train, y_train)
    preds = my_pipeline.predict(X_valid)
see how it automtaically taks care of task transforming columns of both train and test data before fitting 

# Validation

## Cross Validation 
- In cross-validation, we run our modeling process on different subsets of the data to get multiple measures of model quality. For example, we could begin by dividing the data into 5 pieces, each 20% of the full dataset. In this case, we say that we have broken the data into 5 "folds". Now we can choose 4 folds for training and 1 fold for testing what cross validation does is it automates the process of choosing these 4 folds for training and 1 fold for testing and then return the resulting mae of all 5 tests it did  in a list
- We do this as the model might be inaccurate for a randomly selected set of rows and be very accurate for a diiferent set of rows So we can eliminate this by testing the model on all of data but one by one test it on different subsets
### Code
    from sklearn.model_selection import cross_val_score
    scores = -1 * cross_val_score(my_pipeline, X, y,cv=5,scoring='neg_mean_absolute_error')

## MeanAbsoluteError
    from sklearn.metrics import mean_absolute_error
    prediction = model.predict(X)
    mean_absolute_error(y, prediction)

