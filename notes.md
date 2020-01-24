# Machine learning notes

## Dictionary

Word | Description
------- | -------
Inference | Thing
Quantative variables | Numerical values
Qualitative variables | Classes / categories

## Estimate $f$

### Why Estimate $f?$

#### Inference

Restrictive models are more interpretable, therefore often better.
Can be easy to understand relationship between $Y$ and $X_1,X_2,X_p$.

#### Prediction

Flexible approaches can lead to complicated estimates of $f$. Being difficult to understand how an individual predictor is associated with the response.
![Tradeoff between Flexibility and interperability](tradeoff_flex_interperability.png)

### How Do We Estimate $f?$

### Parametric Methods

### Non-parametric Methods

#### Supervised Versus Unsupervised Learning

##### Supervised Learning

##### Unsupervised Learning

### Regression Versus Classification Problems

### Regression Problems

Often having a quantative response



#### Measuring quality of fit

##### Training MSE

Most commonly-used measure is *mean squared error* (MSE), given by 
$$
MSE = \frac{1}{n} \sum_{i=1}^{n}(y_i - \hat{f}(x_i))^2
$$
$\hat{f}(x_i)$ is prediction that $\hat{f}$ gives for the *i*th observation.
The MSE will be small if the predicted responses are very close to the true responses, and will be large if for some of the observations, the predicted and true responses differ substantially.

This is also known as *Training MSE* since it used training data to fit te model. In general we don't care how well the method wodks on the training data. Rather:

*"We are interested in the accuracy of hte predictions that we obtain when we apply our method to previously unseen test data."*

##### Test MSE

![Training vs Test MSE](test_vs_training_mse.png)
As model flexibility increases, training MSE will decrease, but the test MSE may not. This example is said to be *overfitting* the data, since its training MSE is decreasing and test MSE aren't.
This happens because our statistical learning procedure is working too hard to find patterns in the training data, and may be picking up some patterns that are just caused by random chance rather than by true properties of the unknown function *f*.

Computing test MSE is conciderably more difficult than training MSE because, usually, there are no test data available.

##### Example from book

*Suppose that we are interested test data in developing an algorithm to predict a stock’s price based on previous stock returns. We can train the method using stock returns from the past 6 months. But we don’t really care how well our method predicts last week’s stock price. We instead care about how well it will predict tomorrow’s price or next month’s price.*

### Classification Problems

Often having qualitative responses.

## The Bias-Variance Trade-Off
