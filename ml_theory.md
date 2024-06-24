# Machine Learning Algorithms 

## Supervised Machine Learning
*popular algorithms that fall under this are*
- Linear Regression
- Logistic Regression
- Decision Trees
- Random Forests
- Support Vector Machines (SVM)

Supervised machine learning is a type of machine learning where the algorithm is trained on a labeled dataset, meaning that for every input data point, there is an associated correct output. As the name suggests, a supervisor oversees this process, guiding the algorithm through the training phase. The supervisor, in this case, is the labeled data itself, serving as the teacher providing correct answers to the algorithm. The goal of supervised learning is to learn a mapping from inputs to outputs based on this labeled training data so that when presented with new, unseen data, the algorithm can accurately predict the correct output.

To understand supervised learning, let's use an everyday example: teaching a child to recognize fruits. Imagine you have a child who is learning about different types of fruits. You show them various fruits like apples, bananas, and oranges, and you tell them what each fruit is. This process is similar to providing labeled data – the fruit names are the labels associated with each fruit image.

*it is classified into Classified and Regression*
### Classified
In classification tasks, the algorithm learns to classify input data into different categories or classes.It's essential to note that in classification, the dependent variable is discrete, meaning it takes on distinct, separate values rather than a continuous range . For instance, let's consider a classification problem where the goal is to predict whether a student passes or fails an exam based on certain features such as study hours, attendance, and previous grades. In this example, "Pass/Fail" is the dependent variable.

### Regression
In regression tasks, the algorithm learns to predict continuous values based on one or more input features. Unlike classification, where the goal is to classify data into discrete categories, regression deals with estimating a continuous target variable. 

## Unsupervised Machine Learning
*popular algorithms include*
- K-means clustering
- Hierachiral clustering
Unsupervised learning is a type of machine learning algorithm that learns from unlabeled data, meaning there are no predefined labels associated with the input data. The goal is to find hidden patterns or structures in the data.

Imagine you give unsupervised learning algorithm a basket full of fruit. Unlike supervised learning where it's told "this is an apple" and "this is an orange," this algorithm doesn't have any labels or prior knowledge. Its job is to sort the fruit entirely on its own.

Here's how it might work: The algorithm will analyze features of each piece of fruit, like color, size, and texture. By looking for similarities between these features, it will start to group the fruit together. Over time, it might discover two distinct clusters: one containing mostly smooth, reddish fruit (apples) and another with rougher, orange-hued fruit (oranges). All without anyone ever telling it what an apple or orange is!

Unsupervised learning can be further subdivided into two main categories:
### Clustering 
Clustering is a type of unsupervised learning algorithm where the goal is to partition a dataset into groups, or clusters, based on similarities among the data points within each group.

Imagine you have a dataset of customer purchase history from an online store. Using clustering, you can group customers who exhibit similar purchasing behavior into clusters. For instance, customers who frequently buy electronics might form one cluster, while those who often purchase clothing could belong to another cluster. The algorithm doesn't require predefined categories; it autonomously identifies similarities and forms clusters accordingly.
### Association 
Association learning aims to discover relationships or associations between variables in large datasets. Unlike clustering, which focuses on grouping similar data points, association learning identifies patterns in how variables are related or co-occur within the dataset.

Consider a supermarket transaction dataset. Association rule learning can identify patterns like "if a customer buys bread, they are likely to also buy butter." In this example, "bread" and "butter" are items that frequently appear together in transactions, forming an association. This information is valuable for marketing strategies, store layout optimization, and inventory management.

## Reinforced Learning 
Reinforcement learning operates on a different principle compared to supervised and unsupervised learning. Instead of learning from labeled or unlabeled data, it learns from interactions with an environment to achieve a goal. It can be likened to how humans learn through trial and error, receiving feedback from the environment based on their actions.

In reinforcement learning, an agent learns to make decisions by acting in an environment and receiving feedback through rewards or penalties
Reinforcement learning works similarly in more complex situations, like teaching AI systems to play games or control robots. The AI learns by trial and error, figuring out which actions lead to the best outcomes based on the rewards it receives from its environment
