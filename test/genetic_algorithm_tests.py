import unittest

from genetic_algorithms.one_point_crossover import one_point_crossover
from genetic_algorithms.two_point_crossover import two_point_crossover
from genetic_algorithms.uniform_crossover import uniform_crossover
from genetic_algorithms.mutation import mutation

class TestGeneticAlgorithmsMethods(unittest.TestCase):

    #one point crossover
    def test_standard_case_one_point_crossover(self):
        father = [1, 1, 1, 1, 1]
        mother = [0, 0, 0, 0, 0]
        point = 2
        new_father, new_mother = one_point_crossover(point, father, mother)
        self.assertEqual(new_father, [0, 0, 1, 1, 1])
        self.assertEqual(new_mother, [1, 1, 0, 0, 0])

    def test_point_at_start(self):
        father = [1, 2, 3]
        mother = [4, 5, 6]
        point = 0
        new_father, new_mother = one_point_crossover(point, father, mother)
        self.assertEqual(new_father, [1, 2, 3])
        self.assertEqual(new_mother, [4, 5, 6])


    def test_point_at_end(self):
        father = [1, 2, 3]
        mother = [4, 5, 6]
        point = 3
        new_father, new_mother = one_point_crossover(point, father, mother)
        self.assertEqual(new_father, [4, 5, 6])
        self.assertEqual(new_mother, [1, 2, 3])

    def test_does_not_modify_originals(self):
        father = [9, 9, 9]
        mother = [1, 1, 1]
        point = 0
        original_father = father[:]
        original_mother = mother[:]
        _ = one_point_crossover(point, father, mother)
        self.assertEqual(father, original_father)
        self.assertEqual(mother, original_mother)

# Two point crossover
    def test_standard_case_two_point_crossover(self):
        father = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        mother = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        first_point = 2
        second_point = 5
        new_father, new_mother = two_point_crossover(first_point, second_point, father, mother)
        self.assertEqual(new_father, [1, 1, 0, 0, 0, 1, 1, 1, 1])
        self.assertEqual(new_mother, [0, 0, 1, 1, 1, 0, 0, 0, 0])

    def test_consecutive_points(self):
        father = [1, 2, 3, 4, 5]
        mother = [5, 4, 3, 2, 1]
        first_point = 2
        second_point = 3
        new_father, new_mother = two_point_crossover(first_point, second_point, father, mother)
        self.assertEqual(new_father, [1, 2, 3, 4, 5])
        self.assertEqual(new_mother, [5, 4, 3, 2, 1])

    def test_entire_swap(self):
        father = [9, 9, 9, 9]
        mother = [1, 1, 1, 1]
        first_point = 0
        second_point = 4
        new_father, new_mother = two_point_crossover(first_point, second_point, father, mother)
        self.assertEqual(new_father, [1, 1, 1, 1])
        self.assertEqual(new_mother, [9, 9, 9, 9])

    # uniform crossover
    def test_equal_length_parents(self):
        father = [1, 1, 1, 1]
        mother = [0, 0, 0, 0]
        son = uniform_crossover(father, mother)
        self.assertEqual(len(son), len(father))
        for i in range(len(son)):
            self.assertIn(son[i], [father[i], mother[i]])

    def test_inequal_length_parents(self):
        father = [1, 2, 3]
        mother = [4, 5]
        result = uniform_crossover(father, mother)
        self.assertEqual(result, -1)

    def test_does_not_modify_parents(self):
        father = [7, 8, 9]
        mother = [1, 2, 3]
        original_father = father[:]
        original_mother = mother[:]
        _ = uniform_crossover(father, mother)
        self.assertEqual(father, original_father)
        self.assertEqual(mother, original_mother)

    def test_randomness_consistency(self):
        father = [0, 0, 0, 0, 0]
        mother = [1, 1, 1, 1, 1]
        sons = set()
        for _ in range(20):
            son = tuple(uniform_crossover(father, mother))
            sons.add(son)
        self.assertGreater(len(sons), 1)

    #mutation
    def test_no_mutation_when_probability_zero(self):
        arr = [1, 1, 1, 1]
        space = [0]
        original = arr[:]
        mutated = mutation(arr[:], space, probability=0)
        self.assertEqual(mutated, original)

    def test_all_mutated_when_probability_100(self):
        arr = [1, 1, 1, 1]
        space = [0]
        mutated = mutation(arr[:], space, probability=100)
        self.assertEqual(mutated, [0, 0, 0, 0])

    def test_mutation_length_preserved(self):
        arr = [1, 2, 3, 4, 5]
        space = [9, 8, 7]
        mutated = mutation(arr[:], space, probability=50)
        self.assertEqual(len(mutated), len(arr))

    def test_mutation_uses_only_space_values(self):
        arr = [1, 2, 3, 4, 5]
        space = [9, 8, 7]
        mutated = mutation(arr[:], space, probability=100)
        for gene in mutated:
            self.assertIn(gene, space)

    def test_does_not_modify_input_if_copied(self):
        arr = [1, 2, 3]
        space = [4, 5, 6]
        original = arr[:]
        _ = mutation(arr[:], space, probability=50)
        self.assertEqual(arr, original)


if __name__=='__main__':
    unittest.main()