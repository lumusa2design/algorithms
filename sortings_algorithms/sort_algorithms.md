# Short algorithms (English) 

A sort algorithm is a set of instructions that arranges a series of elements in (usually ascending) order.

## 📚 Index

- [🔁 Bubble Sort](#bubble-sort)
- [🔢 Counting Sort](#counting-sort)
- [📌 Insertion Sort](#insertion-sort)
- [🧬 Merge Sort](#merge-sort)
- [⚡ Quick Sort](#quick-sort)
- [✅ Selection Sort](#selection-sort)
- [🎲 Bogo Sort](#bogo-sort)
- [✂️ Stalin Sort](#stalin-sort)


### BUBBLE SORT
It is a sorting algorithm in which each element is checked against the next, exchanging its position if it is not in the correct order. It is necessary to go through the vector several times until it is sorted.

#### Algorithm Performance
To find the performance according to the Big O notation, we can look at the average case, the optimal case and the worst case. First we must to knoe that:

$c(n) =\frac{n^2 - n}{2} $

| Average Case      | Optimal case    | Worst case  |
|-------------------|-----------------| ------------|
| $\Theta(n) = n^2$ | $\Omega(n) = n$ | $O(n) = n^2$|

### COUNTING SORT
Non-comparative sorting algorithm. Works by counting the occurrences of each unique value. Best for integers in a limited range.

#### Algorithm Performance
| Average Case        | Optimal case        | Worst case     |
|---------------------|---------------------|----------------|
| $\Theta(n) = n + k$ | $\Omega(n) = n + k$ | $O(n) = n + k$ |

$n =$ number of elements $k = $ range of input
### INSERTION SORT
Builds the sorted array one item at a time, inserting each element into its correct position.
#### Algorithm Performance
| Average Case      | Optimal case    | Worst case  |
|-------------------|-----------------| ------------|
| $\Theta(n) = n^2$ | $\Omega(n) = n$ | $O(n) = n^2$|

### MERGE SORT
A divide-and-conquer algorithm that splits the array into halves, sorts each half, and merges them.
#### Algorithm Performance
| Average Case           | Optimal case           | Worst case       |
|------------------------|------------------------|------------------|
| $\Theta(n) = n log(n)$ | $\Omega(n) = n log(n)$ | $O(n) = nlog(n)$ |

### QUICK SORT

#### Algorithm Performance
| Average Case          | Optimal case          | Worst case   |
|-----------------------|-----------------------|--------------|
| $\Theta(n) = nlog(n)$ | $\Omega(n) = nlog(n)$ | $O(n) = n^2$ |

### SELECTION SORT
Selects the smallest (or largest) element and places it at the correct position, repeating for all elements.
#### Algorithm Perfrmance
| Average Case      | Optimal case      | Worst case  |
|-------------------|-------------------| ------------|
| $\Theta(n) = n^2$ | $\Omega(n) = n^2$ | $O(n) = n^2$|

### BOGO SORT
Generates random permutations of the array until it is sorted. Highly inefficient and impractical—used for educational or humorous purposes.
#### Algorithm Performance
| Average Case              | Optimal case    | Worst case       |
|---------------------------|-----------------|------------------|
| $\Theta(n) = n \times n!$ | $\Omega(n) = n$ | $O(n) =  \infty$ |

### STALIN SORT 
Traverses the list and removes any element that is out of order—brutal but effective. A joke algorithm.
#### Algorithm  Performance
| Average Case    | Optimal case    | Worst case |
|-----------------|-----------------| ----------|
| $\Theta(n) = n$ | $\Omega(n) = n$ | $O(n) = n$|