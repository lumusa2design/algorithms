import unittest
from text_algorithms.cesar_codex import cesar_codex
from text_algorithms.vigenere_codex import vigenere_encrypt, vigenere_decrypt

class TestTextAlgorithms(unittest.TestCase):
    def test_cesar_codex(self):
        self.assertEqual(cesar_codex('abc', 1), 'bcd')
        self.assertEqual(cesar_codex('XYZ', 2), 'ZAB')

    def test_vigenere(self):
        message = 'HELLO WORLD'
        key = 'KEY'
        encrypted = vigenere_encrypt(message, key)
        decrypted = vigenere_decrypt(encrypted, key)
        self.assertEqual(decrypted, message)

if __name__ == '__main__':
    unittest.main()
