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

def run(start_date, number_of_days):
 
    logging.debug("generating events since date {} until {} days later".format(start_date, number_of_days))

    events = ""
    for i in range(0, number_of_days):
        gregorian_date = start_date + datetime.timedelta(days=i)
        persian_month, persian_day = i18n.to_jalali(gregorian_date)[1:3]
        weekday = gregorian_date.weekday()
       
        persian_day_number = i18n.convert_digits_to_persian(persian_day)
        persian_month_name = i18n.PERSIAN_MONTHS[persian_month - 1]
        persian_weekday_name = i18n.PERSIAN_WEEKDAYS[weekday]
                
        title = "{} {} {}".format(persian_weekday_name, persian_day_number, persian_month_name);
        uid = "{}@google.com".format(uuid.uuid4().hex)
        start = gregorian_date.strftime("%Y%m%d")
        end = (gregorian_date + datetime.timedelta(days=1)).strftime("%Y%m%d")
        event = EVENT.format(start=start, end=end, uid=uid, title=title)
        
        events += event
    
    calendar = CALENDAR.format(events=events)
    
    # remove empty lines
    calendar = "".join([s for s in calendar.splitlines(True) if s.strip("\r\n")])
    
    print(calendar)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate daily calendar events with corresponding Persian dates as their titles")
    parser.add_argument('start', type=datetime.date.fromisoformat, help='start date for generating events')
    parser.add_argument('-n', '--number', type=int, default=365, help='number of days following the start date')
    parser.add_argument('-d', '--debug', action='store_true')
    args = parser.parse_args()
    start_date = args.start
    number_of_days = args.number
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)
    run(start_date, number_of_days)
