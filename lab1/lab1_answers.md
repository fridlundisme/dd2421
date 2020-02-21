# Lab 1 - Decision Trees

## Assignment 0

### Problem

Each one of the datasets has properties which makes them hard to learn. Motivate which of the three problems is most difficult for a decision tree algorithm to learn.

### Answer

Probably 2?

## Assignment 1

### Problem

The file dtree.py defines a function entropy which calculates the entropy of a dataset. Import this file along with the monks datasets and use it to calculate the entropy of the training datasets.

### Answer

| Dataset | Entropy |
|------ | ------ |
| MONK-1 | 1.0 |
| MONK-2 | 0.957117.. | 
| MONK-3 | 0.9998061.. |


## Assignment 2

### Problem
Explain entropy for a uniform distribution and a non-uniform distribution, present some example distributions with high and low entropy

### Answer
Uniform distribution have *perfect* entropy. i.e. it is the maximum entropy of that particular problem. Easy example is a (normal) deck of cards which have 1/52 to draw each card. The entropy is maxed because is harder to calculate the next card rather than having a deck of cards with only 2s and 3s. It's only a probability of 26/52 to get 2 or three. It's therefore easier to predict the next card.

## Assignment 3

### Problem
Use the function averageGain (defined in dtree.py) to calculate the expected information gain corresponding to each of the six attributes. Note that the attributes are represented as in-stances of the class Attribute (defined in monkdata.py) which you can access via m.attributes[0], ..., m.attributes[5]. Based on the results, which attribute should be used for splitting the examples at the root node?

### Answer

| Dataset | *a1* | *a2* | *a3* | *a4* | *a5* | *a6* |
| ------ | -------- | -------- | -------- | -------- | -------- | -------- |
| MONK-1 | 0.075273 | 0.005838 | 0.004708 | 0.026312 | **0.287031** | 0.000758 |
| MONK-2 | 0.003756 | 0.002458 | 0.001056 | 0.015664 | **0.017277** | 0.006248 |
| MONK-3 | 0.007121 | **0.293736** | 0.000831 | 0.002892 | 0.255912 | 0.007077 |


## Assignment 4

### Problem

For splitting we choose the attribute that maximizes the information gain, Eq.3. Looking at Eq.3 how does the entropy of the subsets, $S_k$ , look like when the information gain is maximized? How can we motivate using the information gain as a heuristic for picking an attribute for splitting? Think about reduction in entropy after the split and what the entropy implies.

### Answer

$Gain(S,A) = Entropy(S) - \sum_{k \in \textrm{values}(A)} \frac{|S_k|}{|S|} \textrm{Entropy}(S_k)$

The equation shows that the gain is maximized when the entropy of the subsets $S_k \to 0$.
This makes sense since, if the entropy of a given $S_k$ is small, the easier it is to calculate the next step to take when classifying a new point.
When we have high information gain the attribute it self, per definition, gives us most information at the beginning of the decision tree. This means we are most likely to find the correct category for the new point faster and can probably reduce the decision tree far more than if we didn't make it heuristic.

## Assignment 5

### Problem

Assignment 5: Build the full decision trees for all three Monk
datasets using buildTree. Then, use the function check to mea-
sure the performance of the decision tree on both the training and
test datasets.
For example to built a tree for monk1 and compute the performance
on the test data you could use
import monkdata as m
import dtree as d
t=d.buildTree(m.monk1, m.attributes);
print(d.check(t, m.monk1test))
Compute the train and test set errors for the three Monk datasets
for the full trees. Were your assumptions about the datasets correct?
Explain the results you get for the training and test datasets.


### Answer
|  | $E_train$ | $E_test$ |
| --------- | --------- | -------- |
| MONK-1 | 1.000000 | 0.828704 |
| MONK-2 | 1.000000 | 0.692130 |
| MONK-3 | 1.000000 | 0.944444 |

## Assignment 6

### Problem

Explain pruning from a bias variance trade-off per-spective.

### Answer

The more pruning, the more bias and less variance the tree will have.
Creates a more effective tree but also not as accurate (always).

## Assignment 7

### Problem

