# Short algorithms (English) 

A sort algorithm is a set of instructions that arranges a series of elements in (usually ascending) order.


### BUBBLE SORT
It is a sorting algorithm in which each element is checked against the next, exchanging its position if it is not in the correct order. It is necessary to go through the vector several times until it is sorted.

#### Algorithm Performance
To find the performance according to the Big O notation, we can look at the average case, the optimal case and the worst case. First we must to knoe that:

$c(n) =\frac{n^2 - n}{2} $

| Average Case      | Optimal case    | Worst case  |
|-------------------|-----------------| ------------|
| $\Theta(n) = n^2$ | $\Omega(n) = n$ | $O(n) = n^2$

