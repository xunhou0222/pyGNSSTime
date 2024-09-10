import datetime

from .Const import MINTAIWEEK, MINTAIWEEK_MINDOW, MAXTAIWEEK, MAXTAIWEEK_MAXDOW
from .Const import MINTTWEEK, MINTTWEEK_MINDOW, MAXTTWEEK, MAXTTWEEK_MAXDOW
from .Const import MINUTCWEEK, MINUTCWEEK_MINDOW, MAXUTCWEEK, MAXUTCWEEK_MAXDOW
from .Const import MINGPSWEEK, MINGPSWEEK_MINDOW, MAXGPSWEEK, MAXGPSWEEK_MAXDOW
from .Const import MINGLOWEEK, MINGLOWEEK_MINDOW, MAXGLOWEEK, MAXGLOWEEK_MAXDOW
from .Const import MINBDSWEEK, MINBDSWEEK_MINDOW, MAXBDSWEEK, MAXBDSWEEK_MAXDOW
from .Const import MINGALWEEK, MINGALWEEK_MINDOW, MAXGALWEEK, MAXGALWEEK_MAXDOW
from .Const import _LeapSecD1,  _LeapSecD2,  _LeapSecD3,  _LeapSecD4,  _LeapSecD5
from .Const import _LeapSecD6,  _LeapSecD7,  _LeapSecD8,  _LeapSecD9,  _LeapSecD10
from .Const import _LeapSecD11, _LeapSecD12, _LeapSecD13, _LeapSecD14, _LeapSecD15
from .Const import _LeapSecD16, _LeapSecD17, _LeapSecD18, _LeapSecD19, _LeapSecD20
from .Const import _LeapSecD21, _LeapSecD22, _LeapSecD23, _LeapSecD24, _LeapSecD25
from .Const import _LeapSecD26, _LeapSecD27


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def sys_week_dow_check(flag: bytes, week: int, dow: int) -> datetime.date:
    if flag == b'A' or flag == b'a':
        if week < MINTAIWEEK or week > MAXTAIWEEK:
            raise ValueError(f"TAI week must be in {MINTAIWEEK:d}...{MAXTAIWEEK:d}"
                             f", but {week:d} is given!")
            return datetime.date(1, 1, 1)
        elif dow < 0 or dow > 6:
            raise ValueError(f"dow must be in 0...6, but {dow:d} is given!")
            return datetime.date(1, 1, 1)
        elif week == MINTAIWEEK and dow < MINTAIWEEK_MINDOW:
            raise ValueError(f"When TAI week is equal to {MINTAIWEEK:d}" 
                             f", dow must not be less than {MINTAIWEEK_MINDOW:d}"
                             f", but {dow:d} is given!")
            return datetime.date(1, 1, 1)
        elif week == MAXTAIWEEK and dow > MAXTAIWEEK_MAXDOW:
            raise ValueError(f"When TAI week is equal to {MAXTAIWEEK:d}" 
                             f", dow must not be greater than {MAXTAIWEEK_MAXDOW:d}"
                             f", but {dow:d} is given!")
            return datetime.date(1, 1, 1)

        return datetime.date(1958, 1, 1)
    elif flag == b'T' or flag == b't':
        if week < MINTTWEEK or week > MAXTTWEEK:
            raise ValueError(f"TT week must be in {MINTTWEEK:d}...{MAXTTWEEK:d}"
                             f", but {week:d} is given!")
            return datetime.date(1, 1, 1)
        elif dow < 0 or dow > 6:
            raise ValueError(f"dow must be in 0...6, but {dow:d} is given!")
            return datetime.date(1, 1, 1)
        elif week == MINTTWEEK and dow < MINTTWEEK_MINDOW:
            raise ValueError(f"When TT week is equal to {MINTTWEEK:d}" 
                             f", dow must not be less than {MINTTWEEK_MINDOW:d}"
                             f", but {dow:d} is given!")
            return datetime.date(1, 1, 1)
        elif week == MAXTTWEEK and dow > MAXTTWEEK_MAXDOW:
            raise ValueError(f"When TT week is equal to {MAXTTWEEK:d}" 
                             f", dow must not be greater than {MAXTTWEEK_MAXDOW:d}"
                             f", but {dow:d} is given!")
            return datetime.date(1, 1, 1)

        return datetime.date(1977, 1, 1)
    elif flag == b'U' or flag == b'u':
        if week < MINUTCWEEK or week > MAXUTCWEEK:
            raise ValueError(f"UTC week must be in {MINUTCWEEK:d}...{MAXUTCWEEK:d}"
                             f", but {week:d} is given!")
            return datetime.date(1, 1, 1)
        elif dow < 0 or dow > 6:
            raise ValueError(f"dow must be in 0...6, but {dow:d} is given!")
            return datetime.date(1, 1, 1)
        elif week == MINUTCWEEK and dow < MINUTCWEEK_MINDOW:
            raise ValueError(f"When UTC week is equal to {MINUTCWEEK:d}" 
                             f", dow must not be less than {MINUTCWEEK_MINDOW:d}"
                             f", but {dow:d} is given!")
            return datetime.date(1, 1, 1)
        elif week == MAXUTCWEEK and dow > MAXUTCWEEK_MAXDOW:
            raise ValueError(f"When UTC week is equal to {MAXUTCWEEK:d}" 
                             f", dow must not be greater than {MAXUTCWEEK_MAXDOW:d}"
                             f", but {dow:d} is given!")
            return datetime.date(1, 1, 1)

        return datetime.date(1972, 1, 1)
    elif flag == b'G' or flag == b'g':
        if week < MINGPSWEEK or week > MAXGPSWEEK:
            raise ValueError(f"GPS week must be in {MINGPSWEEK:d}...{MAXGPSWEEK:d}"
                             f", but {week:d} is given!")
            return datetime.date(1, 1, 1)
        elif dow < 0 or dow > 6:
            raise ValueError(f"dow must be in 0...6, but {dow:d} is given!")
            return datetime.date(1, 1, 1)
        elif week == MINGPSWEEK and dow < MINGPSWEEK_MINDOW:
            raise ValueError(f"When GPS week is equal to {MINGPSWEEK:d}" 
                             f", dow must not be less than {MINGPSWEEK_MINDOW:d}"
                             f", but {dow:d} is given!")
            return datetime.date(1, 1, 1)
        elif week == MAXGPSWEEK and dow > MAXGPSWEEK_MAXDOW:
            raise ValueError(f"When GPS week is equal to {MAXGPSWEEK:d}" 
                             f", dow must not be greater than {MAXGPSWEEK_MAXDOW:d}"
                             f", but {dow:d} is given!")
            return datetime.date(1, 1, 1)

        return datetime.date(1980, 1, 6)
    elif flag == b'R' or flag == b'r':
        if week < MINGLOWEEK or week > MAXGLOWEEK:
            raise ValueError(f"GLO week must be in {MINGLOWEEK:d}...{MAXGLOWEEK:d}"
                             f", but {week:d} is given!")
            return datetime.date(1, 1, 1)
        elif dow < 0 or dow > 6:
            raise ValueError(f"dow must be in 0...6, but {dow:d} is given!")
            return datetime.date(1, 1, 1)
        elif week == MINGLOWEEK and dow < MINGLOWEEK_MINDOW:
            raise ValueError(f"When GLO week is equal to {MINGLOWEEK:d}" 
                             f", dow must not be less than {MINGLOWEEK_MINDOW:d}"
                             f", but {dow:d} is given!")
            return datetime.date(1, 1, 1)
        elif week == MAXGLOWEEK and dow > MAXGLOWEEK_MAXDOW:
            raise ValueError(f"When GLO week is equal to {MAXGLOWEEK:d}" 
                             f", dow must not be greater than {MAXGLOWEEK_MAXDOW:d}"
                             f", but {dow:d} is given!")
            return datetime.date(1, 1, 1)

        return datetime.date(1972, 1, 1)
    elif flag == b'C' or flag == b'c':
        if week < MINBDSWEEK or week > MAXBDSWEEK:
            raise ValueError(f"BDS week must be in {MINBDSWEEK:d}...{MAXBDSWEEK:d}"
                             f", but {week:d} is given!")
            return datetime.date(1, 1, 1)
        elif dow < 0 or dow > 6:
            raise ValueError(f"dow must be in 0...6, but {dow:d} is given!")
            return datetime.date(1, 1, 1)
        elif week == MINBDSWEEK and dow < MINBDSWEEK_MINDOW:
            raise ValueError(f"When BDS week is equal to {MINBDSWEEK:d}" 
                             f", dow must not be less than {MINBDSWEEK_MINDOW:d}"
                             f", but {dow:d} is given!")
            return datetime.date(1, 1, 1)
        elif week == MAXBDSWEEK and dow > MAXBDSWEEK_MAXDOW:
            raise ValueError(f"When BDS week is equal to {MAXBDSWEEK:d}" 
                             f", dow must not be greater than {MAXBDSWEEK_MAXDOW:d}"
                             f", but {dow:d} is given!")
            return datetime.date(1, 1, 1)

        return datetime.date(2006, 1, 1)
    elif flag == b'E' or flag == b'e':
        if week < MINGALWEEK or week > MAXGALWEEK:
            raise ValueError(f"GAL week must be in {MINGALWEEK:d}...{MAXGALWEEK:d}"
                             f", but {week:d} is given!")
            return datetime.date(1, 1, 1)
        elif dow < 0 or dow > 6:
            raise ValueError(f"dow must be in 0...6, but {dow:d} is given!")
            return datetime.date(1, 1, 1)
        elif week == MINGALWEEK and dow < MINGALWEEK_MINDOW:
            raise ValueError(f"When GAL week is equal to {MINGALWEEK:d}" 
                             f", dow must not be less than {MINGALWEEK_MINDOW:d}"
                             f", but {dow:d} is given!")
            return datetime.date(1, 1, 1)
        elif week == MAXGALWEEK and dow > MAXGALWEEK_MAXDOW:
            raise ValueError(f"When GAL week is equal to {MAXGALWEEK:d}" 
                             f", dow must not be greater than {MAXGALWEEK_MAXDOW:d}"
                             f", but {dow:d} is given!")
            return datetime.date(1, 1, 1)

        return datetime.date(1999, 8, 22)
    else:
        raise ValueError(f'Unsupported GNSS time system: "{str(flag)}"!\n'
                         "Supported: \n"
                         "    'A' or 'a' for TAI\n"
                         "    'T' or 't' for TT\n"
                         "    'U' or 'u' for UTC\n" 
                         "    'G' or 'g' for GPST\n"
                         "    'R' or 'r' for GLONASS UTC\n"
                         "    'C' or 'c' for BDT\n"
                         "    'E' or 'e' for GST"
                         )
        return(datetime.date(1, 1, 1))


def year_doy_check(year: int, doy: int) -> None:
    if year < datetime.MINYEAR or year > datetime.MAXYEAR:
        raise ValueError(f"year must be in {datetime.MINYEAR:d}...{datetime.MAXYEAR:d}"
                         f", but {year:d} is given!")
    else:
        max_doy = 365

        if is_leap_year(year):
            max_doy += 1

        if doy < 1 or doy > max_doy:
            raise ValueError(f"For year {year:d}, doy must be in 1 ...{max_doy:d}, but {doy:d} is given!")


def date2week(flag: bytes, year: int, month: int, day:int) -> tuple[int, int]:
    '''
    Convert year/month/day to GNSS week/dow.

    Arguments:
        flag    Time system

        year, month, day

    Return:
        week, dow
    '''
    date00 = sys_week_dow_check(flag, 0, 0)
    date = datetime.date(year, month, day)

    delta = (date - date00).days
    week = int(delta/7)
    dow = int(delta%7)

    if delta < 0:
        week -= 1

    return week, dow


def week2date(flag: bytes, week: int, dow: int) -> tuple[int, int, int]:
    '''
    Convert GNSS week/dow to year/month/day.

    Arguments:
        flag    Time system
        week, dow

    Return:
        year, month, day
    '''
    date00 = sys_week_dow_check(flag, week, dow)
    date = date00 + datetime.timedelta(week*7 + dow)

    return date.year, date.month, date.day


def date2doy(year: int, month: int, day: int) -> int:
    '''
    Convert year/month/day to year/doy.

    Arguments:
        year, month, day

    Return:
        doy
    '''
    date = datetime.date(year, month, day)
    date00 = datetime.date(year, 1, 1)

    doy = (date - date00).days + 1

    return doy


def doy2date(year: int, doy: int) -> tuple[int, int]:
    '''
    Convert year/doy to year/month/day.

    Arguments:
        year, doy

    Return:
        month, day
    '''
    year_doy_check(year, doy)
    date = datetime.date(year, 1, 1) + datetime.timedelta(doy - 1)

    return date.month, date.day


def week2doy(flag: bytes, week: int, dow: int) -> tuple[int, int]:
    '''
    Convert GNSS week/dow to year/doy.

    Arguments:
        flag    Time system
        
        week, dow

    Return:
        year, doy
    '''
    date00 = sys_week_dow_check(flag, week, dow)
    date = date00 + datetime.timedelta(week*7 + dow)
    date0 = datetime.date(date.year, 1, 1)

    return date.year, (date - date0).days + 1


def doy2week(flag: bytes, year: int, doy: int) -> tuple[int, int]:
    '''
    Convert year/doy to GNSS week/dow.

    Arguments:
        flag    Time system
        
        year, doy

    Return:
        week, dow
    '''
    date00 = sys_week_dow_check(flag, 0, 0)
    year_doy_check(year, doy)

    date0 = datetime.date(year, 1, 1)
    date = date0 + datetime.timedelta(doy - 1)
    delta = (date - date00).days
    week = int(delta/7)
    dow = int(delta%7)

    if delta < 0:
        week -= 1

    return week, dow


def UTCFlag(d: datetime.date) -> int:
    '''
    Given a UTC date, determine whether there is a leap second in that day.

    Arguments:
        d    datetime.date

    Return:
        0, -1 or 1 for non-leap, negative-leap and positive-leap.
    '''
    if ( d == _LeapSecD1  or d == _LeapSecD2  or d == _LeapSecD3  or d == _LeapSecD4  or
         d == _LeapSecD5  or d == _LeapSecD6  or d == _LeapSecD7  or d == _LeapSecD8  or
         d == _LeapSecD9  or d == _LeapSecD10 or d == _LeapSecD11 or d == _LeapSecD12 or
         d == _LeapSecD13 or d == _LeapSecD14 or d == _LeapSecD15 or d == _LeapSecD16 or
         d == _LeapSecD17 or d == _LeapSecD18 or d == _LeapSecD19 or d == _LeapSecD20 or
         d == _LeapSecD21 or d == _LeapSecD22 or d == _LeapSecD23 or d == _LeapSecD24 or
         d == _LeapSecD25 or d == _LeapSecD26 or d == _LeapSecD27 ):
        return 1
    else:
        return 0


def LeapSeconds(d: datetime.date) -> int:
    '''
    Calculate the value of leap seconds given a UTC date.

    Arguments:
        d    datetime.date

    Return:
        the value of leap seconds.
    '''
    if d <= _LeapSecD1:
        return 10
    elif (d > _LeapSecD1 and d <= _LeapSecD2):
        return 11
    elif (d > _LeapSecD2 and d <= _LeapSecD3):
        return 12
    elif (d > _LeapSecD3 and d <= _LeapSecD4):
        return 13
    elif (d > _LeapSecD4 and d <= _LeapSecD5):
        return 14
    elif (d > _LeapSecD5 and d <= _LeapSecD6):
        return 15
    elif (d > _LeapSecD6 and d <= _LeapSecD7):
        return 16
    elif (d > _LeapSecD7 and d <= _LeapSecD8):
        return 17
    elif (d > _LeapSecD8 and d <= _LeapSecD9):
        return 18
    elif (d > _LeapSecD9 and d <= _LeapSecD10):
        return 19
    elif (d > _LeapSecD10 and d <= _LeapSecD11):
        return 20
    elif (d > _LeapSecD11 and d <= _LeapSecD12):
        return 21
    elif (d > _LeapSecD12 and d <= _LeapSecD13):
        return 22
    elif (d > _LeapSecD13 and d <= _LeapSecD14):
        return 23
    elif (d > _LeapSecD14 and d <= _LeapSecD15):
        return 24
    elif (d > _LeapSecD15 and d <= _LeapSecD16):
        return 25
    elif (d > _LeapSecD16 and d <= _LeapSecD17):
        return 26
    elif (d > _LeapSecD17 and d <= _LeapSecD18):
        return 27
    elif (d > _LeapSecD18 and d <= _LeapSecD19):
        return 28
    elif (d > _LeapSecD19 and d <= _LeapSecD20):
        return 29
    elif (d > _LeapSecD20 and d <= _LeapSecD21):
        return 30
    elif (d > _LeapSecD21 and d <= _LeapSecD22):
        return 31
    elif (d > _LeapSecD22 and d <= _LeapSecD23):
        return 32
    elif (d > _LeapSecD23 and d <= _LeapSecD24):
        return 33
    elif (d > _LeapSecD24 and d <= _LeapSecD25):
        return 34
    elif (d > _LeapSecD25 and d <= _LeapSecD26):
        return 35
    elif (d > _LeapSecD26 and d <= _LeapSecD27):
        return 36
    else:
        return 37
    

def fromTAI(week: int, sow: float, flag: bytes) -> tuple[int, float]:
    '''
    Convert TAI (in week/sow format) to TT/UTC/GPST/GLONASS-UTC/BDT/GST.

    Arguments:
        week    Week number in TAI.

        sow     Second od week in TAI.

        flag    The target time system.

    Return:
        Week/sow in the target time system.
    '''
    if flag == b'T' or flag == b't':    # From TAI to TT.
        week -= 991
        sow  -= 259167.816    # 259200 - 32.184, 1977-01-01 00:00:00 (TAI) is TAI week 991, sow 259200.
    elif flag == b'U' or flag == b'u':    # From TAI to UTC.
        week -= 730
        sow  -= 259210    # 259200 + 10, 1972-01-01 00:00:00 (UTC) is TAI week 730, sow 259210.
    elif flag == b'G' or flag == b'g':    # From TAI to GPST.
        week -= 1148
        sow  -= 345619    # 345600 + 19, 1980-01-06 00:00:00 (UTC) is TAI week 1148, sow 345619.
    elif flag == b'R' or flag == b'r':    # From TAI to GLONASS-UTC.
        week -= 730
        sow  -= 248410    # 259200 + 10 - 3*3600, 1971-12-31 21:00:00 (UTC) is TAI week 730, sow 248410.
    elif flag == b'C' or flag == b'c':    # From TAI to BDT.
        week -= 2504
        sow  -= 345633    # 345600 + 33, 2006-01-01 00:00:00 (UTC) is TAI week 2504, sow 345633.
    elif flag == b'E' or flag == b'e':    # From TAI to GPST.
        week -= 2172
        sow  -= 345619    # 345600 + 19, 1999-08-21 23:59:47 (UTC) is TAI week 2172, sow 345619.

    if sow < 0:
        sow += 604800
        week -= 1

    return week, sow


def toTAI(flag: bytes, week: int, sow: float) -> tuple[int, float]:
    '''
    Convert TT/UTC/GPST/GLONASS-UTC/BDT/GST (in week/sow format) to TAI.

    Arguments:
        flag    The original time system.

        week    Week number in the original time system.

        sow     Second od week in the original time system.

    Return:
        Week/sow in TAI.
    '''
    if flag == b'T' or flag == b't':    # From TT to TAI.
        week += 991
        sow  += 259167.816    # 259200 - 32.184, 1977-01-01 00:00:00 (TAI) is TAI week 991, sow 259200.
    elif flag == b'U' or flag == b'u':    # From UTC to TAI.
        week += 730
        sow += 259210    # 259200 + 10, 1972-01-01 00:00:00 (UTC) is TAI week 730, sow 259210.
    elif flag == b'G' or flag == b'g':    # From GPST to TAI.
        week += 1148
        sow += 345619    # 345600 + 19, 1980-01-06 00:00:00 (UTC) is TAI week 1148, sow 345619.
    elif flag == b'R' or flag == b'r':    # From GLONASS-UTC to TAI.
        week += 730
        sow  += 248410    # 259200 + 10 - 3*3600, 1971-12-31 21:00:00 (UTC) is TAI week 730, sow 248410.
    elif flag == b'C' or flag == b'c':    # From BDT to TAI.
        week += 2504
        sow += 345633    # 345600 + 33, 2006-01-01 00:00:00 (UTC) is TAI week 2504, sow 345633.
    elif flag == b'E' or flag == b'e':    # From TAI to GPST.
        week += 2172
        sow  += 345619    # 345600 + 19, 1999-08-21 23:59:47 (UTC) is TAI week 2172, sow 345619.

    if sow >= 604800:
        sow -= 604800
        week += 1
        
    return week, sow
