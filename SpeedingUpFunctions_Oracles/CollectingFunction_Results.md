
## Motivation
- We often use numerically computed functions
- A common use of such functions is  during model fitting. they get evaluated during fitting models to data. This results in repeated calls of the function in a hard to parallelize way. 
- A possible (and an increasingly popular now) solution is using `Oracles`: Black boxes that quickly return an approximate value of the function. The basic idea is to pre-compute a training set, sometimes evaluated very judiciously, and use some form of interpolation on that training set to compute the function. The pre-computation is parallelizable, and this makes the actual curve fitting rapid even though it could be serial.
- The kind of functions used are diverse; some are slow requiring months to evaluate to some fairly fast that take many minutes/hours or less (but can be a problem when called a large number of times). Obviously, for the slow functions the choice of the training set is more important than it is for fast functions. I want to restrict this discussion to fast functions.
- Fast functions, for the purpose of this discussion, are functions 
    - that people regularly run on their computers, (perhaps not in interactive mode). 
    - Fast enough, that the choice of training set input points is not crucial in the sense that a dumb set of inputs can be made up for by a large training set.

