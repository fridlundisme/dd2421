# Machine learning notes

## Dictionary
Word | Description
------- | -------
Inference | Thing
Quantative variables | Numerical values
Qualitative variables | Classes / categories
## Estimate $f$
### Estimate by Inference
Restrictive models are more interpretable, therefore often better.
Can be easy to understand relationship between $Y$ and $X_1,X_2,X_p$.
### Estimate by Prediction
Flexible approaches can lead to complicated estimates of $f$. Being difficult to understand how an individual predictor is associated with the response.
![Tradeoff between Flexibility and interperability](/tradeoff_flex_interperability.png)

## Supervised Versus Unsupervised Learning
### Supervised Learning

### Unsupervised Learning

## Regression Versus Classification Problems
### Regression Problems
Often having a quantative response

#### Measuring quality of fit
Most commonly-used measure is *mean squared error* (MSE), given by 
$$
MSE = \frac{1}{n} \sum_{i=1}^{n}(y_i - \hat{f}(x_i))^2
$$
$\hat{f}(x_i)$ is prediction that $\hat{f}$ gives for the *i*th observation.
The MSE will be small if the predicted responses are very close to the true responses, and will be large if for some of the observations, the predicted and true responses differ substantially
### Classification Problems
Often having qualitative responses