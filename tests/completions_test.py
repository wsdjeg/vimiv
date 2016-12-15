#!/usr/bin/env python
# encoding: utf-8
"""Completion tests for vimiv's test suite."""

from unittest import main
from vimiv_testcase import VimivTestCase


class CompletionsTest(VimivTestCase):
    """Completions Tests."""

    @classmethod
    def setUpClass(cls):
        cls.init_test(cls)
        cls.completions = cls.vimiv["completions"]

    def test_reset(self):
        """Reset the internal completion values."""
        self.completions.tab_presses = 42
        self.completions.tab_position = 42
        self.completions.reset()
        self.assertEqual(self.completions.tab_presses, 0)
        self.assertEqual(self.completions.tab_position, 0)

    def test_internal_completion(self):
        """Completion of internal commands."""
        self.completions.entry.set_text(":a")
        self.completions.complete()
        expected_completions = ["accept_changes", "alias", "autorotate"]
        liststore = self.completions.treeview.get_model()
        for row in liststore:
            self.assertIn(row[0], expected_completions)
        self.assertEqual(len(liststore), len(expected_completions))

    def test_external_completion(self):
        """Completion of external commands. Currently none."""
        self.completions.entry.set_text(":!vimi")
        self.completions.complete()
        liststore = self.completions.treeview.get_model()
        self.assertFalse(len(liststore))

    def test_path_completion(self):
        """Completion of paths."""
        self.completions.entry.set_text(":./vimiv/testimages/ar")
        self.completions.complete()
        expected_completions = ["./vimiv/testimages/arch-logo.png",
                                "./vimiv/testimages/arch_001.jpg"]
        liststore = self.completions.treeview.get_model()
        for row in liststore:
            self.assertIn(row[0], expected_completions)
        self.assertEqual(len(liststore), len(expected_completions))

    def test_tabbing(self):
        """Tabbing through completions."""
        # Complete to last matching character
        self.completions.entry.set_text(":cl")
        self.completions.complete()
        expected_text = ":clear_t"
        received_text = self.completions.entry.get_text()
        self.assertEqual(expected_text, received_text)
        # First result
        liststore = self.completions.treeview.get_model()
        self.vimiv["completions"].complete()
        expected_text = "clear_thumbs"
        selected_path = self.completions.treeview.get_cursor()[0]
        selected_index = selected_path.get_indices()[0]
        selected_text = liststore[selected_index][0]
        self.assertEqual(expected_text, selected_text)
        # Second result
        self.vimiv["completions"].complete()
        expected_text = "clear_trash"
        selected_path = self.completions.treeview.get_cursor()[0]
        selected_index = selected_path.get_indices()[0]
        selected_text = liststore[selected_index][0]
        self.assertEqual(expected_text, selected_text)
        # First again
        self.vimiv["completions"].complete(inverse=True)
        expected_text = "clear_thumbs"
        selected_path = self.completions.treeview.get_cursor()[0]
        selected_index = selected_path.get_indices()[0]
        selected_text = liststore[selected_index][0]
        self.assertEqual(expected_text, selected_text)


if __name__ == '__main__':
    main()
