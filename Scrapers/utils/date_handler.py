import dateparser, datetime, re

from dateparser import date
from datetime import date
from dateutil.relativedelta import relativedelta, MO, TU, WE, TH, FR, SA, SU


weekdays = {'Luni': MO(-1), 'Marți': TU(-1), 'Miercuri': WE(-1), 'Joi': TH(-1), 'Vineri': FR(-1), 'Sâmbătă': SA(-1),
            'Duminică': SU(-1)}


def get_date(raw_date):
    ro_today = 'astăzi'
    if ro_today in raw_date:
        raw_date = raw_date.replace(ro_today, 'azi')
    date_added = dateparser.parse(raw_date)
    if date_added is None:
        raw_date_lower = re.sub(r'[^\w\s]', '', raw_date.lower())
        for weekday in weekdays:
            if re.sub(r'[^\w\s]', '', weekday.lower()) in raw_date_lower:
                last_weekday = date.today() + relativedelta(weekday=weekdays[weekday])
                last_weekday_datetime = datetime.datetime.combine(last_weekday, datetime.time())
                microseconds = len(str(last_weekday_datetime.microsecond))
                unique_microseconds = int(str(last_weekday_datetime.microsecond) + '0' * (6 - microseconds))
                unique_datetime = last_weekday_datetime.replace(microsecond=unique_microseconds)
                return unique_datetime

    timestamp = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    unique_date_added_with_timestamp = date_added.strftime('%Y-%m-%d %H:%M:%S.') + timestamp
    return unique_date_added_with_timestamp

