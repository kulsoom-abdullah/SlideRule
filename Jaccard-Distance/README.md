# Jaccard Distance functions and modifications

This python code has functions needed to calculate the [Jaccard index] (https://en.wikipedia.org/wiki/Jaccard_index) (or similiarity)
which is used as a measure of distance.


Generally, the set functions in Python, such as intersection and union run quickly, but I had very long running times.
Using python profile to find out the bottleneck, I found it was the set intersection operation, specifically for when I had a very large set of items in the 400,000 and above length, being compared.  Using this code with a modified intersection method sped things up considerably.

```python
def intersect(x, y):
```


"modified jaccard"  

```python
def jaccard_mod(x, y):
    itxn = intersect(x, y)
    # sig_val = sig_factor(x,y)
    return 1.0 * (itxn / min(len(x), len(y)))
    # return 1.0*(itxn/min(len(x),len(y)) )*sig_val
```
There are 2 ways to use it:

* Use a sigmoid factor to normalize the jaccard value for when you have a wide variety of set lengths you are calculating distances for. (This is commented out.)  
* The other method I had used for when comparing sets of a small to a comparible large set, for example, 100 elements to 1000, if that 100 was contained in the 1000, then I wanted the distance to be a value of 1.  This is how the factor of dividing by the minimum length of the two sets being compared was decided on.

