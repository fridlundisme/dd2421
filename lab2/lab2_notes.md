### Problem 1
#### Move the clusters around and change their sizes to make it easier or harder for the classifier to find a decent boundary. Pay attention to when the optimizer (minimize function) is not able to find a solution at all.

### Answer

![Original dataset](plots/basic_data/C:%2010,%20kernel:%20lin_kernel.png)

*linear_data* makes it impossible to classify. It thinks all of the points belong to the same class
![Linear data impossible to calculate](plots/linear_data/C:%2010.00,%20kernel:%20poly_kernel.png)

However, when using other clusters - such as the same only scaled a bit we get this.

![Spread data with linear kernel](plots/spread_data/C:%2010.00,%20kernel:%20lin_kernel.png)


### Problem 2 
#### Implement the two non-linear kernels. You should be able to clas-sify very hard data sets with these.

### Answer

![Spread data with polynomial kernel](plots/spread_data/C:%2010.00,%20kernel:%20poly_kernel.png)


![Spread data with radial kernel](plots/spread_data/C:%2010.00,%20kernel:%20radi_kernel.png)


### Problem 3
#### The non-linear kernels have parameters; explore how they influence the decision boundary. Reason about this in terms of the bias-variance trade-off.

### Answer
When decreasing the *sigma* in the radial kernel, the variance increased because it classified the existing points correctly but it will have a hard time classify new ones since the decision boundry is strictly around the points.

![Polynomial kernel with *high* polynomial value](plots/parameters_change/C10%20poly%20kernel%20high%20p.png)

![Polynomial kernel with *low* polynomial value](plots/parameters_change/C10%20poly%20kernel%20low%20p.png)

### Problem 4
#### Explore the role of the slack parameter C. What happens for very large/small values?

### Answer
When C is large, the margin is decreasing, which means we have a better classification for the existing points but will have a harder time classifying new ones (high variance). At a certain point the bigger value of C is not relevant for our data since no points can be that far a way (less spread) but in bigger samples it will be a difference.
Small values creates lower variance in contrast.

### Problem 5 
#### Imagine that you are given data that is not easily separable. When should you opt for more slack rather than going for a more complex model (kernel) and vice versa?

### Answer
It depends. If the model needs to be better at interpreting new points we would like to have a smaller slack value since the classification for new points are more important than having the exact classification for the existing points.
The same goes for a more complex model.
If we for example have alot of datapoints and all of the **classA** points are above the X-axis and all of the **classB** points are below, we would get a worse model in predicting new values with the radial since it will (eventuatlly) close its boundry (and margins) into a circle and therefore provide a higher variance and not being able to predict new points even for perfectly uniformly distributed points.