import unittest
from Projects.bottom_up import weighted_interval_scheduling as SIT
from Projects.recursive import weighted_interval_scheduling as RECURSIVE_SIT


class TestWeightedIntervalScheduling(unittest.TestCase):
    """
    TDD unittest file for Projects/cses.py.py

    Command line:

    ReinforcementLearningHw1# python -m unittest Projects.tests
    """

    def test_cses_example(self):
        projects = [
            (2, 4, 4), (3, 6, 6),
            (6, 8, 2), (5, 7, 3)
        ]

        self.assertEqual(
            SIT(len(projects), projects),
            7
        )

    def test_cses_example_recursive(self):
        projects = [
            (2, 4, 4), (3, 6, 6),
            (6, 8, 2), (5, 7, 3)
        ]

        self.assertEqual(
            RECURSIVE_SIT(projects),
            7
        )

    def test_no_jobs_overlap(self):
        projects = [
            (0, 6, 60), (7, 9, 30),
            (10, 11, 10), (12, 13, 30),
            (14, 15, 50), (16, 17, 10)
        ]

        self.assertEqual(
            SIT(len(projects), projects),
            190
        )

    def test_no_jobs_overlap_recursive(self):
        projects = [
            (0, 6, 60), (7, 9, 30),
            (10, 11, 10), (12, 13, 30),
            (14, 15, 50), (16, 17, 10)
        ]

        self.assertEqual(
            RECURSIVE_SIT(projects),
            190
        )

    def test_all_jobs_overlap(self):
        projects = [
            (6, 6, 60), (6, 6, 30),
            (6, 6, 10), (6, 6, 30),
            (6, 6, 50), (6, 6, 10)
        ]

        self.assertEqual(
            SIT(len(projects), projects),
            60
        )


if __name__ == '__main__':
    unittest.main()
