#!/usr/bin/env python3
import unittest




def Check(password):
    event = ["qwertyuiop", "azertyuiop", "123456789", "password", "abcdefg"]
    ok = len(password) in range(10, 25)
    number = any(c.isdigit() for c in password)
    lower = bool(set(password) & set(password.lower()))
    upper = bool(set(password) & set(password.upper()))
    special = bool(set(password) & set('\"!@#$%^&*()-+?_=,<>/'))
    evident = not (any(word for word in event if word.lower() in password.lower()))

    return ok and number and lower and upper and special and evident


class ValidateTests(unittest.TestCase):

    def test_empty(self):
        self.assertFalse(Check(''))

    def test_too_short(self):
        self.assertFalse(Check('wej'))

    def test_too_long(self):
        self.assertFalse(Check('foughali' * 5 + 'a'))

    def test_no_number(self):
        self.assertFalse(Check("wejdene"))

    def test_no_upper(self):
        self.assertFalse(Check("taketest"))

    def test_no_lower(self):
        self.assertFalse(Check("%&ONETUE"))

    def test_no_special(self):
        self.assertFalse(Check("IMwejdene"))

    def test_valid(self):
        self.assertTrue(Check("FOUGHALIwejdene7?"))

    def test_evident(self):
        self.assertFalse(Check('qwertyuiop'))

if __name__ == '__main__':
    unittest.main()