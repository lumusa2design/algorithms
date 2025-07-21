<h1 align="center">📔 Algorithms Project</h1>

<p align="center">A personal journey through computer science – from the most basic to the most advanced algorithms 💻🧠✨</p>
<p align="center">
  <img src="https://img.shields.io/badge/Status-In%20Progress-blueviolet" />
  <img src="https://img.shields.io/badge/Language-Python-yellow" />
  <img src="https://img.shields.io/github/followers/lumusa2design?label=Follow&style=social" />
</p>

---


## 📚 Table of Contents

| 🚀 Categories                 | 🔗 Link                            |
|-------------------------------|------------------------------------|
| 🔃 Sorting Algorithms         | [Go](#-sorting-algorithms)         |
| 🗃️ Data Structures           | [Go](#-data-structures)            |
| 🔍 Search Algorithms          | [Go](#-search-algorithms)          |
| 🌐 Graph Traversal Algorithms | [Go](#-graph-traversal-algorithms) |
| 🔢 Numerical Algorithms       | [Go](#-numerical-algorithms)       |
| 🧬 Genetic Algorithms         | [Go](#-genetic-algorithms)         |
| 📄 Text Algorithms            | [Go](#-text-algorithms)            |
| 👨🏽‍💻 Author                | [Go](#-author)                     |

---
# 💻 Types of Algorithms

---

## [🔃 Sorting Algorithms](./sortings_algorithms/sort_algorithms.md)

> Algorithms that sort unordered data into a specific order.

These are algorithms that take unordered lists and, after a series of steps, return a sorted list.
<div align="center">

![ordered:list.svg](sortings_algorithms/ordered_list.svg)

</div>

### ✅ Implemented

- [`Bogosort`](./sortings_algorithms/bogo_sort.py)  
- [`BogoBogosort`](./sortings_algorithms/bogobogosort.py)  
- [`Bubblesort`](./sortings_algorithms/bubble_sort.py)  
- [`Countingsort`](./sortings_algorithms/counting_sort.py)  
- [`Insertionsort`](./sortings_algorithms/insertion_sort.py)  
- [`Mergesort`](./sortings_algorithms/merge_sort.py)  
- [`Quicksort`](./sortings_algorithms/quick_sort.py)  
- [`Selectionsort`](./sortings_algorithms/selection_sort.py)  
- [`Stalinsort`](./sortings_algorithms/stalin_sort.py)
- [`Radix Sort`](./sortings_algorithms/radix_sort.py)

### 🛠️ To Implement

- [ ] `Heapsort`  
- [ ] `Bucketsort`  
- [ ] `Shellsort`

---


## [🗃️ Data Structures](./data_structures/data_structure.md)

> Fundamental for storing and organizing data efficiently. Essential for traversal and search algorithms.

Different data structures that store large amounts of information in various ways. They are essential for many algorithms, such as DFS and BFS, which rely on queues and stacks.

<p align="center">
  <img src="./data_structures/binary_tree.svg" width="400px" alt="Binary Tree">
</p>

### ✅ Implemented:
- [`Binary Tree`](./data_structures/binary_tree.py)  
- [`Double Linked List`](./data_structures/double_linked_list.py)  
- [`Hash Table`](./data_structures/binary_tree.py)  
- [`Linked List`](./data_structures/linked_list.py)
- [`Matrix `](./data_structures/matrix.py)
- [`Queue`](./data_structures/Queue.py)  
- [`Stack`](./data_structures/stack.py)  
- [`Non Directed Graph`](./data_structures/non_directed_graph.py)  


### 🛠️ To implement:

- [ ] `AVL Tree`
- [ ] `B Tree`
- [ ] `Heap`  


---

## [🔍 Search Algorithms](search_algorithms/search.md)

> Locate specific values or solutions within data sets using various strategies.

Search algorithms are those that, through various strategies, locate a value or solution within a dataset.  
They can search for a specific number in a list, a node in a structure like a tree or a graph, or even a point that meets certain conditions.

<div align="center">

![nqueens.gif](search_algorithms/nqueens.gif)

</div>

### ✅Implemented:

- [`Greedy Search Tree`](./search_algorithms/basic_greedy.py)  
- [`Binary Search`](./search_algorithms/binary_search.py)  
- [`Linear Search`](./search_algorithms/lineal_search.py)  
- [`Missing Number`](./search_algorithms/missing_number.py)  
- [`Backtracking`](./search_algorithms/n_queens_backtracking.py)  
- [`Jump Search`](./search_algorithms/jump_search.py)
- [`Exponential Search`](./search_algorithms/exponential_search.py)
- [`Interpolation Search`](./search_algorithms/interpolation_search.py)
- [`Fibonacci Search`](./search_algorithms/fibonacci_search.py)
### 🛠️ To implement:


---

## [🌐 Graph Traversal Algorithms](graph_traversal_algorithms/) 

> Explore vertices and edges of graphs to find paths, detect cycles, or analyze structure.

Graph traversal algorithms are used to systematically visit or explore the vertices and edges of a graph.  
They help solve problems like pathfinding, cycle detection, connected component analysis, and shortest path computation.

<div align="center">

![dfs.gif](graph_traversal_algorithms/dfs_exploracion.gif)

</div>

### ✅ Implemented:

- [`Breadth-First Search (BFS) `](./graph_traversal_algorithms/BFS.py)  
- [`Depth-First Search (DFS)  `](./graph_traversal_algorithms/DFS.py)  
- [`Dijkstra’s Algorithm`](./graph_traversal_algorithms/dijkstra_algorithm.py)  

### 🛠️ To implement:

- [ ] `A* (A Star)`
- [ ] `Bellman-Ford`  
- [ ] `Floyd-Warshall`  
- [ ] `Johnson's Algorithm`  
- [ ] `Topological Sort`  
- [ ] `Tarjan's Algorithm`  
- [ ] `Kosaraju's Algorithm`  
- [ ] `Prim's Algorithm`  
- [ ] `Kruskal's Algorithm`  
- [ ] `IDA* (Iterative Deepening A*)`

---

## [🔢 Numerical Algorithms](./numerical_algorithms/numerical.md)

>  Algorithms that solve numerical problems like root finding or optimization.

They are algorithms that use mathematical methods to find a result, using different tools such as iteration, interpolation, integration... 
These algorithms are key to various branches of engineering and mathematics and are widely used in various fields.



<div align="center">

![bisection_method.png](numerical_algorithms/bisection_method.svg)

</div>

### ✅ Implemented:

- [`binary conversion`](./numerical_algorithms/binary_conversion.py)
- [`bisection method`](./numerical_algorithms/binary_conversion.py)
- [`count ways`](./numerical_algorithms/count_ways.py)
- [`erastothenes sieve`](./numerical_algorithms/erastothenes_sieve.py)
- [`euclides algorithm`](./numerical_algorithms/euclides_algorithm.py)
- [`factorial of a number`](./numerical_algorithms/factorial.py)
- [`fibonacci`](./numerical_algorithms/fibonacci.py)
- [`friendly numbers`](./numerical_algorithms/friendly_numbers.py)
- [`Lucas number`](./numerical_algorithms/lucas_number.py)
- [`max number of an array`](./numerical_algorithms/max_number.py)
- [`min number of an array`](./numerical_algorithms/min_number.py)
- [`mean of a number`](./numerical_algorithms/mean.py)
- [`modular exponentation`](./numerical_algorithms/modular_exponentation.py)
- [`muller method`](./numerical_algorithms/muller_method.py)
- [`Newton Raphson method`](./numerical_algorithms/newton_raphson_method.py)
- [`Pow method`](./numerical_algorithms/pow_method.py)
- [`Regula Falsi Method`](./numerical_algorithms/regulafalsi.py)
- [`Secant method`](./numerical_algorithms/secant_method.py)
- [`Taylor Polinomial`](./numerical_algorithms/taylor_polynomial.py)
- [`Tribonacci`](./numerical_algorithms/tribonacci.py)

### 🛠️ To implement

- [ ] `Cholesky Descomposition`
- [ ] `Gauss Jordan Elimination`
- [ ] `QR Descomposition`
- [ ] `Brent's Method`
- [ ] `Fixed Point Iteration`
- [ ] `Lagrange Polynomial Interpolation`
- [ ] `Spline Interpolation`
- [ ] `Fourier Series`
- [ ] `Standart Deviation and Variance`
- [ ] `Gradient Descent`
- [ ] `Runge-Kutta Methods`
- [ ] `Nash Balance`
- [ ] `K-Means`
- [ ] `Montecarlo's Algorithm`

---

## [🧬 Genetic Algorithms](./genetic_algorithms/genetic_algorithms.md)

> Heuristic search inspired by natural selection: selection, crossover, mutation.

Algorithms are algorithms that are based on organised steps to arrive at the solution of a specific problem. These algorithms are based on evolving populations of individuals by subjecting them to a series of random actions until a solution is reached. Similar to how evolution works.
<div align="center">

![genetic_algorithm.gif](genetic_algorithms/genetic_algorithm.gif)

</div>

### ✅ Implemented

- [`Mutation`](./genetic_algorithms/mutation.py)
- [`One Point Crossover`](./genetic_algorithms/one_point_crossover.py)
- [`Two Point Crossover`](./genetic_algorithms/two_point_crossover.py)
- [`Uniform Crossover`](./genetic_algorithms/uniform_crossover.py)
- [`Sudoku Example`](./genetic_algorithms/sudoku.py)
- [`Fitness Proportional Selection`](./genetic_algorithms/Roulete_wheel.py)
- [`Tournament Selection`](./genetic_algorithms/tournament_selection.py)
- [`Elitism`](./genetic_algorithms/elitism.py)
- 
### 🛠️ To implement

- [ ] `Multiobjective Optimization (NSGA-II)`
- [ ] `Gene Encoding Techniques`
  - `Binary Genome Representation`
  - `Real Genome Representation`
  - `Permutation Genome Representation`
- [ ] `Dynamic Mutation Rate`
- [ ] `Real Valued Genetic Algorithm`
- [ ] `Tree based Genetic Programming`


---

## [📄 Text Algorithms](./text_algorithms/text.md)

>Algorithms that manipulate, analyze, and transform sequences of characters.

Text algorithms include techniques for searching and matching patterns in text (like KMP or Rabin-Karp), compressing data (such as Huffman or LZ77), and encoding/decoding strings (e.g., Base64 or Unicode). They are essential in applications like text editors, search engines, file compressors, communication protocols, and natural language processing.

![text_algoritms.gif](text_algorithms/kmp_text.gif)

### ✅ Implemented

- [`Caesar Encoding`](./text_algorithms/cesar_codex.py)
-  [`Huffman Algorithm`](./text_algorithms/huffman.py)
- [`vigenere encoding`](./text_algorithms/vigenere_codex.py)
### 🛠️ To implement

- [ ] ` Knuth-Morris-Pratt (KMP)`
- [ ] ` Rabin-Karp`
- [ ] `Boyer-Moore`
- [ ] ` LZ77 / LZ78 Compression`
- [ ] ` Run-Length Encoding (RLE)`
- [ ] ` Base64 Encoding`
- [ ] ` ASCII / Unicode Conversion`
- [ ] ` ROT13`
- [ ] ` Edit Distance (Levenshtein)`
- [ ] ` Anagram Checker`
- [ ] ` Trie Construction`
- [ ] ` Regex-based Pattern Matching`

*(Coming soon)*

---

## 🧑🏽‍💻 Author

- [@lumusa2design](https://github.com/lumusa2design)

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=lumusa2design&style=flat-square&color=lightgrey" alt="Profile views" />
</p>