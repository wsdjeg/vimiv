# vim: ft=python fileencoding=utf-8 sw=4 et sts=4
"""Test Search independently of the command line."""

from unittest import TestCase, main

from vimiv.commandline import Search
from vimiv.settings import settings


class SearchTest(TestCase):
    """Search Tests."""

    @classmethod
    def setUpClass(cls):
        settings.override("incsearch", "false")
        settings.override("search_case_sensitive", "true")
        cls.search = Search(None)
        cls.filelist = []

    def setUp(self):
        self.filelist = ["foo_bar", "foo_baz", "zab"]
        self.search.init(self.filelist, "foo_bar", "none")

    def test_search(self):
        """Search for strings in filelist with independent search class."""
        self.search.run("foo")
        self.assertIn("foo_bar", self.search.results)
        self.assertIn("foo_baz", self.search.results)
        self.assertNotIn("zab", self.search.results)
        self.search.run("z")
        self.assertEqual(["foo_baz", "zab"], self.search.results)
        self.search.run("wololo")
        self.assertFalse(self.search.results)


if __name__ == "__main__":
    main()
