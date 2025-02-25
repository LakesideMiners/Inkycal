#!python
"""
Tests config
"""
import os
from enum import Enum
from dotenv import load_dotenv

# relative import
basedir = os.path.abspath(os.path.dirname(__file__))

# load config from corresponding file
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    get = os.environ.get

    # show generated images via preview?
    USE_PREVIEW = False

    # ical_parser_test
    OPENWEATHERMAP_API_KEY = get("OPENWEATHERMAP_API_KEY")
    TEST_ICAL_URL = get("TEST_ICAL_URL")

    # inkycal_agenda_test & inkycal_calendar_test
    SAMPLE_ICAL_URL = get("SAMPLE_ICAL_URL")

    # inkycal_todoist_test
    TODOIST_API_KEY = get("TODOIST_API_KEY")





