import i18n
import argparse
import sys
import re
import datetime
import uuid
import logging

CALENDAR = '''
BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Holidays
X-WR-TIMEZONE:Asia/Tehran{events}
END:VCALENDAR
'''

EVENT = '''
BEGIN:VEVENT
DTSTART;VALUE=DATE:{start}
DTEND;VALUE=DATE:{end}
DTSTAMP:20171222T225127Z
UID:{uid}
CREATED:20171222T211914Z
DESCRIPTION:
LAST-MODIFIED:20171222T225127Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:{title}
TRANSP:TRANSPARENT
END:VEVENT
'''


def run(input_file):
    persian_days = parse(input_file)
    days = [(convert_persian_date(persian_date), title) for (persian_date, title) in persian_days]
    
    events = ""
    for (date, title) in days:
        logging.debug("creative event {} with title {} ...".format(date, title))
        start = date.strftime("%Y%m%d")
        end = (date + datetime.timedelta(days=1)).strftime("%Y%m%d")
        uid = "{}@google.com".format(uuid.uuid4().hex)
        event = EVENT.format(start=start, end=end, uid=uid, title=title)
        events += event

    calendar = CALENDAR.format(events=events)
    
    # remove empty lines
    calendar = "".join([s for s in calendar.splitlines(True) if s.strip("\r\n")])
    
    print(calendar)


def parse(input_file):
    try:
        file = open(input_file, "r")
        lines = file.read().splitlines()
        days = []
        for line in lines:
            line = line.strip()
            if not ':' in line:
                continue
            if line.strip() == '':
                continue
            date, title = re.split(': ', line)
            days.append([date, title])
        return days
    except IOError:
        return {}

def convert_persian_date(persian_date):
    year, month, day = persian_date.split('/')
    date = i18n.to_gregorian(int(year), int(month), int(day))
    logging.debug("persian date {} converted to gregorian equivalent {}".format(persian_date, date))
    return date


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate google calendar for holidays")
    parser.add_argument('input')
    parser.add_argument('-d', '--debug', required=False, action='store_true')
    args = parser.parse_args()
    input_file = args.input
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)
    run(input_file)
