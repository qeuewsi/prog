import unittest

from src.lab2.caesar import decrypt_caesar, encrypt_caesar
from src.lab2.rsa import decrypt, encrypt, gcd, generate_keypair, is_prime, multiplicative_inverse
from src.lab2.vigenre import decrypt_vigenere, encrypt_vigenere


class CaesarTestCase(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt_caesar("PYTHON"), "SBWKRQ")
        self.assertEqual(encrypt_caesar("python"), "sbwkrq")
        self.assertEqual(encrypt_caesar("Python3.6"), "Sbwkrq3.6")
        self.assertEqual(encrypt_caesar("XYZ"), "ABC")
        self.assertEqual(encrypt_caesar(""), "")

    def test_decrypt(self):
        self.assertEqual(decrypt_caesar("SBWKRQ"), "PYTHON")
        self.assertEqual(decrypt_caesar("sbwkrq"), "python")
        self.assertEqual(decrypt_caesar("Sbwkrq3.6"), "Python3.6")
        self.assertEqual(decrypt_caesar(""), "")

    def test_shift(self):
        self.assertEqual(encrypt_caesar("Hello", 0), "Hello")
        self.assertEqual(decrypt_caesar(encrypt_caesar("Hello, World!", 7), 7), "Hello, World!")


class VigenereTestCase(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(encrypt_vigenere("python", "a"), "python")
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")

    def test_decrypt(self):
        self.assertEqual(decrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(decrypt_vigenere("python", "a"), "python")
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")

    def test_key_d_is_caesar(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "D"), encrypt_caesar("PYTHON"))


class RSATestCase(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(91))

    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)
        self.assertEqual(gcd(0, 5), 5)

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)
        self.assertEqual(multiplicative_inverse(3, 11) * 3 % 11, 1)

    def test_generate_keypair(self):
        public, private = generate_keypair(17, 19)
        self.assertEqual(public[1], 17 * 19)
        self.assertEqual(public[0] * private[0] % ((17 - 1) * (19 - 1)), 1)
        with self.assertRaises(ValueError):
            generate_keypair(4, 7)
        with self.assertRaises(ValueError):
            generate_keypair(7, 7)

    def test_roundtrip(self):
        public, private = generate_keypair(61, 53)
        message = "Hello"
        self.assertEqual(decrypt(public, encrypt(private, message)), message)
