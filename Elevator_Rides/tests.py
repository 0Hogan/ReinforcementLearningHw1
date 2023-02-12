import unittest
from Elevator_Rides.bottom_up import minimum_elevator_rides as SIT
from Elevator_Rides.recursive import minimum_elevator_rides as RECURSIVE_SIT


class TestMinElevatorRides(unittest.TestCase):
    """
    TDD unittest file for CSES Elevator Rides

    Command line:

    ReinforcementLearningHw1# python -m unittest Elevator_Rides.tests
    """

    def test_cses_example(self):
        num_people = 4
        max_weight = 10
        person_weights = [4, 8, 6, 1]

        self.assertEqual(
            SIT(
                num_people, max_weight,
                person_weights
            ),
            2
        )

    def test_recursive_cses_example(self):

        self.assertEqual(
            RECURSIVE_SIT(4),
            2
        )

    def test_all_people_share_one_ride(self):
        num_people = 4
        max_weight = 10
        person_weights = [1, 2, 3, 1]

        self.assertEqual(
            SIT(
                num_people, max_weight,
                person_weights
            ),
            1
        )

    def test_no_people_share_ride(self):
        num_people = 4
        max_weight = 10
        person_weights = [6, 5, 9, 7]

        self.assertEqual(
            SIT(
                num_people, max_weight,
                person_weights
            ),
            4
        )

    def test_children_same_weight(self):
        num_people = 4
        max_weight = 10
        person_weights = [1, 1, 1, 1]

        self.assertEqual(
            SIT(
                num_people, max_weight,
                person_weights
            ),
            1
        )

    def test_adults_same_weight(self):
        num_people = 4
        max_weight = 10
        person_weights = [9, 9, 9, 9]

        self.assertEqual(
            SIT(
                num_people, max_weight,
                person_weights
            ),
            4
        )

    def test_each_person_max_weight(self):
        num_people = 4
        max_weight = 10
        person_weights = [10, 10, 10, 10]

        self.assertEqual(
            SIT(
                num_people, max_weight,
                person_weights
            ),
            4
        )

    def test_another_sequence(self):
        num_people = 3
        max_weight = 10
        person_weights = [9, 2, 1]

        self.assertEqual(
            SIT(
                num_people, max_weight,
                person_weights
            ),
            2
        )


if __name__ == '__main__':
    unittest.main()
