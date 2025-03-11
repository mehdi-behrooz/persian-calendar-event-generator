### Daily Event Generator Module:
This module creates daily all-day events for each day of the year, with their titles reflecting the corresponding Persian (Jalali) date. This ensures that the Persian equivalent of each calendar day is displayed at the top of Calendar applications, like Google Calendar.  

Generating the persian-titled day events for 720 days, starting on 2024-01-01:

``` 
python3 days.py 2024-01-01 -n 720 > output/days-2025-2026.ics
```
To debug:
```
python3 days.py 2024-01-01 -n 5 -d 
```



### Holiday Events Generator:
This module helps creating events for Persian bank holidays. To use it, you should put the bank holidays of the year in a text file with their persian dates.  

Generating bank holidays for the Persian year 1404:
```
python3 holidays.py input/1404.txt > output/1404.ics
```
To debug:

```bash
python3 holidays.py input/1403.txt -d
```




