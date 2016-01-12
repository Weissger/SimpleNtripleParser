from unittest import TestCase
from src.NtripleLineParser import NtripleParser

__author__ = 'tmy'

lines = ["# This is a comment",
         "<http://www.test.org/subject> <http://www.test.org/predicate> <http://www.test.org/object>."]


class TestNtripleParser(TestCase):
    def setUp(self):
        self.parser = NtripleParser(" ")

    def test_is_comment_line(self):
        self.assertTrue(self.parser.is_comment_line(lines[0]))
        self.assertFalse(self.parser.is_comment_line(lines[1]))

    def test_get_subject_comment(self):
        self.assertEqual(None, self.parser.get_subject(lines[0]))

    def test_get_subject(self):
        self.assertEqual("http://www.test.org/subject", self.parser.get_subject(lines[1]))

    def test_get_predicate_comment(self):
        self.assertEqual(None, self.parser.get_predicate(lines[0]))

    def test_get_predicate(self):
        self.assertEqual("http://www.test.org/predicate", self.parser.get_predicate(lines[1]))

    def test_get_object_comment(self):
        self.assertEqual(None, self.parser.get_object(lines[0]))

    def test_get_object(self):
        self.assertEqual("http://www.test.org/object", self.parser.get_object(lines[1]))

    def test_get_triple(self):
        triple = self.parser.get_triple(lines[1])
        self.assertEqual("http://www.test.org/subject", triple["subject"])
        self.assertEqual("http://www.test.org/predicate", triple["predicate"])
        self.assertEqual("http://www.test.org/object", triple["object"])