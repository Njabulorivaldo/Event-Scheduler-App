import unittest
from unittest.mock import patch
from App import *
from Event import Event

class TestEventApp(unittest.TestCase):

    events = [
            Event("Event 1", "Description 1", "2024-04-01", "08:00"),
            Event("Event 2", "Description 2", "2024-04-01", "09:00"),
            Event("Event 3", "Description 3", "2024-04-02", "10:00")
            ]
    def test_validate_date(self):
        # Test valid date
        self.assertTrue(validate_date("2024-04-01"))
        self.assertTrue(validate_date("2024-04-31"))
        
        # Test invalid date
        self.assertFalse(validate_date("2024/04/01"))
        self.assertFalse(validate_date("04-01-2024"))

    def test_validate_time(self):
        # Test valid time
        self.assertTrue(validate_time("08:00"))
        # Test invalid time
        self.assertFalse(validate_time("25:00"))
        self.assertFalse(validate_time("08-00"))
        self.assertFalse(validate_time("08:60"))

    # def setUp(self):
    #     # Create a list of events for testing
    #     self.events = [
    #         Event("Event 1", "Description 1", "2024-04-01", "08:00"),
    #         Event("Event 2", "Description 2", "2024-04-01", "09:00"),
    #         Event("Event 3", "Description 3", "2024-04-02", "10:00")
    #     ]

    def test_delete_existing_event(self):
        # Test deleting an existing event
        deleteEvent("Event 1")
        self.assertEqual(len(self.events), 2)  # Check if the event is deleted
        self.assertNotIn("Event 1", [event.title for event in self.events])  # Check if the event title is not in the list

    def test_delete_nonexistent_event(self):
        # Test deleting a non-existing event
        deleteEvent("Nonexistent Event")
        self.assertEqual(len(self.events), 3)  # Check if no event is deleted
        # Check if the event list remains unchanged
        self.assertEqual([event.title for event in self.events], ["Event 1", "Event 2", "Event 3"])

#-------------------------------------------------------
    @patch('builtins.print')
    def test_search_with_existing_date(self, mocked_print):
        # Test searching with an existing date
        search_withDate("2024-04-01")
        # Check if the correct events are printed
        mocked_print.assert_called_once_with('\n{:<15} | {:<30} | {:<15} | {:<10}\n' \
        '--------------------------------------------------------------------------------\n' \
        'Event 1        | Description 1                   | 2024-04-01      | 08:00    \n' \
        'Event 2        | Description 2                   | 2024-04-01      | 09:00    \n\n')

    @patch('builtins.print')
    def test_search_with_nonexistent_date(self, mocked_print):
        # Test searching with a non-existing date
        search_withDate(self.events, "2024-04-03")
        # Check if "No events..." is printed
        mocked_print.assert_called_once_with('\nNo events...\n')

if __name__ == '__main__':
    unittest.main()
