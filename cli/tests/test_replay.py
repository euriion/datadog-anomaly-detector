from unittest import TestCase

import os
import sys
from click.testing import CliRunner

try:
    import replay
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
    import replay


class ReplayCliTestCase(TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_run_successfully(self):
        res = self.runner.invoke(replay.replay, ['--start=2016-08-10 12:00',
                                                 '--end=2016-08-10 12:10'])
        self.assertEqual(res.exit_code, 0)

    def test_invalid_interval(self):
        res = self.runner.invoke(replay.replay, ['--start=2016-08-10 12:00',
                                                 '--end=2016-08-12 12:00'])
        self.assertIsInstance(res.exception, AssertionError)
