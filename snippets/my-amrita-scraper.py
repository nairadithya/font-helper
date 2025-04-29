#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "beautifulsoup4",
#     "pandas",
#     "requests",
# ]
# ///


import requests
from bs4 import BeautifulSoup

cookies = {"PHPSESSID": # INSERT YOUR COOKIE HERE }


def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def get_timetable_data(cookies):
    timetable_page = requests.get(
        "http://students.amrita.edu/client/class-attendance", cookies=cookies
    )

    soup = BeautifulSoup(timetable_page.text, "html.parser")

    rows = soup.find_all("tr")

    headers = [row.text for row in rows[0] if row.text != "\n"]

    data = rows[1:]

    attendance = {header: [] for header in headers}
    for item in data:
        for j, entry in enumerate(item):
            if is_float(entry.text):
                attendance[headers[j]].append(float(entry.text))
            else:
                attendance[headers[j]].append(entry.text)

    return attendance


attendance = get_timetable_data(cookies)


def get_min_attend():
    min_attend = min(attendance["Percentage"])
    index = attendance["Percentage"].index(min_attend)
    subj = attendance["Course"][index]
    return subj, min_attend


subj, min_attend = get_min_attend()

print("\n")

print(f"Your minimum attendance is {min_attend} for {subj}")
