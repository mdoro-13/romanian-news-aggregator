import unittest
import calendar
from datetime import datetime, timedelta
from utils import date_handler

import dateparser


class TestGetDate(unittest.TestCase):
    def test_valid_date(self):
        valid_dates = [
            ("2022-04-18", datetime(2022, 4, 18)),
            ("18 aprilie 2022", datetime(2022, 4, 18)),
            ("18 dec 2022", datetime(2022, 12, 18)),
            ("18 decembrie, 2022", datetime(2022, 12, 18)),
            ("18/12/2022", datetime(2022, 12, 18)),
            ("18 dec, 2022", datetime(2022, 12, 18)),
            ("2019-12-31", datetime(2019, 12, 31)),
            ("31 dec 2019", datetime(2019, 12, 31)),
            ("2023-01-01", datetime(2023, 1, 1)),
            ("2021-09-22", datetime(2021, 9, 22)),
            ("2022-05-01", datetime(2022, 5, 1))
        ]
        for raw_date, expected_date in valid_dates:
            with self.subTest(raw_date=raw_date, expected_date=expected_date):
                self.assertEqual(date_handler.get_date(raw_date), expected_date)

    def test_today(self):
        raw_date = "astăzi"
        expected_date = datetime.now().date()
        self.assertEqual(date_handler.get_date(raw_date).date(), expected_date)

    def test_latest_day_of_week(self):

        today = datetime.today()
        for i in range(7):
            days_since_day = today.weekday() - i
            if days_since_day < 0:
                days_since_day += 7
            latest_day = today.date() - timedelta(days=days_since_day)
            raw_date = calendar.day_name[i].lower()
            self.assertEqual(date_handler.get_date(raw_date).date(), latest_day)

    def test_yesterday(self):
        today = datetime.today()
        yesterday = (today - timedelta(days=1)).date()
        raw_date = "ieri, 22:33"
        self.assertEqual(date_handler.get_date(raw_date).date(), yesterday)

    def test_invalid_date(self):
        raw_date = "foobar"
        self.assertIsNone(date_handler.get_date(raw_date))
