# KNN (K closest neighbours)
- learn from here https://www.youtube.com/watch?v=zeFt_JCA3b4
- Regression: Instead of a vote, KNN takes an average (or weighted average) of the values from those K closest neighbors. This becomes the predicted value for the new data point. Like taking an average answer from your closest classmates on a test.
- problem here is the deciding the optimum k value 

# SVM (Support Vector Machine)
- learn from here https://youtu.be/_YPScrckx28?feature=shared
- data isn't always perfectly linearly separable. This is where things get a bit more complex, and SVMs utilize advanced techniques to handle non-linear data.
- SVM create robust decision boundaries, which can be highly effective, especially in scenarios where there is limited data or complex data distributions. This distinguishing characteristic sets SVM apart from other machine learning algorithms and contributes to its versatility and applicability across various domains.

# logistic Regression
- learn from here https://youtu.be/EKm0spFxFG4?feature=shared
- This method is particularly useful when the relationship between the variables is not linear, and it allows for the inclusion of multiple predictors to improve the accuracy of predictions.

# DecesionTrees
- learn from here https://youtu.be/_L39rN6gz7Y?feature=shared for classification
- learn form here for regression https://youtu.be/g9c66TUylZ4?feature=shared

there are two methods which are applied too select the best suited question for an internal node using Information Gain and using Gini Index they basically work on principle if there more certainity after the split the better is the split and ceratininty is measured by using a function of  probabilty of a label to appear in resuting split

The leaf nodes stores the predictions rest of the nodes are questions 
we need to find a sweet spot between overfitiing and underfiting a decesion tree

When a predcition is to be made we move down the tree answering tthe questions till we reach the leaf node 


# Random Forests

# LinearRegression
    it is as simple it goes we just find a line or hyperlane which best suits the data by finding the coefficients of Y = c + BX this line now predicts the data we can just input X and we get the predicted Y
learn from here - https://youtu.be/nk2CQITm_eo?feature=shared
# K-means Clustering 

- Clustering : it is a process of grouping (putting a label on a set of data points ) data points with close proximity data points 

- Now, let's delve into one of the most widely used clustering algorithms: K-means clustering. K-Means Clustering is an Unsupervised Learning algorithm, which groups the unlabeled dataset into different clusters by a process known as clustering. Here K defines the number of pre-defined clusters that need to be created in the process, as if K=2, there will be two clusters, and for K=3, there will be three clusters, and so on. It is an iterative algorithm that divides the unlabeled dataset into k different clusters in such a way that each dataset belongs to only one group that has similar properties

- So how does it work? The first step is to decide how many clusters you want. We'll understand how to make this decision in a while, but for now, let's say we decide on two clusters(red and blue ). For each cluster, you need to place a randomly located centroid on the scatter plot wherever you like. It doesn't have to be one of the existing data points.

- Now, what happens next is that K-means will assign each of the data points to the closest centroid 

- Now, the next step is to calculate the center of mass or center of gravity for each of the preliminary clusters that we have identified. The centroid is not included in this calculation. For example, for the blue cluster, we need to take the average of all the x-coordinates and the average of all the y-coordinates of the data points within that cluster. This will give us the position of the new center of mass And then we move the centroid to those positions.

- Once the centroids have moved, we repeat the process: reassign each data point to the closest centroid.After that, we calculate the center of gravity for each cluster again.Move the centroids and do the process again. repeat until we reach a point where further iterations do not change the assignments of the data points.

- We have finally got our clusters now 
