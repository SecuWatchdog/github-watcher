from unittest import TestCase

from app.utils.time_diff_calc import calculate_time_difference


class Test(TestCase):
    def test_calculate_time_difference(self):
        time_created = "2023-09-23T09:28:00Z"
        time_deleted = "2023-09-23T09:30:00Z"
        expected_result = 2.0

        time_diff = calculate_time_difference(time_created, time_deleted)

        self.assertEqual(time_diff, expected_result)
