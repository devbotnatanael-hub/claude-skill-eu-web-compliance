import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import scan

class Boundaries(unittest.TestCase):
    def test_symlink_file_and_directory_are_not_read(self):
        with tempfile.TemporaryDirectory() as root, tempfile.TemporaryDirectory() as other:
            Path(other, 'secret.html').write_text('<form><input name="secret"></form>')
            Path(root, 'link.html').symlink_to(Path(other, 'secret.html'))
            Path(root, 'linked').symlink_to(other)
            coverage = {}
            self.assertEqual(scan.scan(root, [], coverage=coverage), [])
            self.assertEqual({o['reason'] for o in coverage['omissions']}, {'symlink_file', 'symlink_directory'})
            self.assertFalse(coverage['complete'])

    def test_limits_and_minified_are_reported(self):
        with tempfile.TemporaryDirectory() as root:
            Path(root, 'large.html').write_text('a' * 100)
            Path(root, 'bundle.min.js').write_text('document.cookie="test"')
            coverage = {}
            scan.scan(root, [], coverage=coverage, max_bytes=20)
            self.assertEqual({o['reason'] for o in coverage['omissions']}, {'file_size_limit', 'minified_requires_runtime_review'})

    def test_read_failure_not_silent(self):
        with tempfile.TemporaryDirectory() as root:
            Path(root, 'page.html').write_text('hello')
            coverage = {}
            with patch.object(scan, 'read_text', side_effect=PermissionError('denied')):
                scan.scan(root, [], coverage=coverage)
            self.assertEqual(coverage['omissions'][0]['reason'], 'PermissionError')
            self.assertFalse(coverage['complete'])

    def test_budget_exhaustion_not_clean(self):
        with tempfile.TemporaryDirectory() as root:
            Path(root, 'page.html').write_text('hello')
            coverage = {}
            scan.scan(root, [], coverage=coverage, max_files=0)
            self.assertTrue(coverage['truncated'])
            self.assertFalse(coverage['complete'])

    def test_fifo_does_not_block(self):
        with tempfile.TemporaryDirectory() as root:
            os.mkfifo(Path(root, 'pipe.html'))
            coverage = {}
            scan.scan(root, [], coverage=coverage)
            self.assertEqual(coverage['omissions'][0]['reason'], 'non_regular_file')

    def test_invalid_utf8_is_reported(self):
        with tempfile.TemporaryDirectory() as root:
            Path(root, 'page.html').write_bytes(b'\xff')
            coverage = {}
            scan.scan(root, [], coverage=coverage)
            self.assertEqual(coverage['omissions'][0]['reason'], 'UnicodeDecodeError')
