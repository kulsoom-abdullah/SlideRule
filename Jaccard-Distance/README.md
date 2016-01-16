This python code has functions needed to calculate the Jaccard index (or similiarity)
which is used as a measure of distance.
https://en.wikipedia.org/wiki/Jaccard_index

Generally, the set functions in Python, such as intersection and union run quickly,
but I had very long running times.
Using python profile to find out the bottleneck, I found it was the set operation,
specifically for when I had a very large set of items in the 400,000 and above
length, being compared.  Using this code below
sped things up considerably.


# this is a "modified jaccard"  One can use a sigmoid factor to normalize the jaccard
# value for when you have a wide variety of set lengths you are calculating distances for.
# This is commented out.  The other method I had used for when comparing sets of
# a small to a comparible large set, for example, 100 elements to 1000, if that 100 was
# contained in the 1000, then I wanted the distance to be a value of 1.  This is how
# the factor of dividing by the minimum length of the two sets being compared was decided on.

# for most purposes, comment out the if cIPflag condition below.  This was
# a boolean I used to decide whether to normalize jaccard or not.
