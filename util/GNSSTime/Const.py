import datetime


SUPPORTED_TIME_SYS = [b'A', b'a', b'T', b't', b'U', b'u', b'G', b'g', b'R', b'r', b'C', b'c', b'E', b'e']

MINTAIWEEK        = -102112    # 1-1-1
MINTAIWEEK_MINDOW = 5    # If week == MINTAIWEEK, dow must >= MINTAIWEEK_MINDOW 
MAXTAIWEEK        = 419611    # 9999/12/31
MAXTAIWEEK_MAXDOW = 2    # If week == MAXTAIWEEK, dow must <= MAXTAIWEEK_MAXDOW

MINTTWEEK         = -103103    # 1-1-1
MINTTWEEK_MINDOW  = 2    # If week == MINTTWEEK, dow must >= MINTTWEEK_MINDOW 
MAXTTWEEK         = 418619    # 9999/12/31
MAXTTWEEK_MAXDOW  = 6    # If week == MAXTTWEEK, dow must <= MAXTTWEEK_MAXDOW

MINUTCWEEK        = -102842    # 1-1-1
MINUTCWEEK_MINDOW = 2    # If week == MINUTCWEEK, dow must >= MINUTCWEEK_MINDOW 
MAXUTCWEEK        = 418881    # 9999/12/31
MAXUTCWEEK_MAXDOW = 0    # If week == MAXUTCWEEK, dow must <= MAXUTCWEEK_MAXDOW

MINGPSWEEK        = -103260    # 1-1-1
MINGPSWEEK_MINDOW = 1    # If week == MINGPSWEEK, dow must >= MINGPSWEEK_MINDOW 
MAXGPSWEEK        = 418462    # 9999/12/31
MAXGPSWEEK_MAXDOW = 5    # If week == MAXGPSWEEK, dow must <= MAXGPSWEEK_MAXDOW

MINGLOWEEK        = -102842;    # 1-1-1
MINGLOWEEK_MINDOW = 2;    # If week == MINGLOWEEK, dow must >= MINGLOWEEK_MINDOW 
MAXGLOWEEK        = 418881;    # 9999/12/31
MAXGLOWEEK_MAXDOW = 0;    # If week == MAXGLOWEEK, dow must <= MAXGLOWEEK_MAXDOW

MINBDSWEEK        = -104616    # 1-1-1
MINBDSWEEK_MINDOW = 1    # If week == MINBDSWEEK, dow must >= MINBDSWEEK_MINDOW
MAXBDSWEEK        = 417106
MAXBDSWEEK_MAXDOW = 5    # If week == MAXBDSWEEK, dow must <= MAXBDSWEEK_MAXDOW

MINGALWEEK        = -104284;    # 1-1-1
MINGALWEEK_MINDOW = 1;    # If week == MINGALWEEK, dow must >= MINGALWEEK_MINDOW 
MAXGALWEEK        = 417438;    # 9999/12/31
MAXGALWEEK_MAXDOW = 5;    # If week == MAXGALWEEK, dow must <= MAXGALWEEK_MAXDOW


# Dates with leap seconds.
_LeapSecD1  = datetime.date(1972,  6, 30)
_LeapSecD2  = datetime.date(1972, 12, 31)
_LeapSecD3  = datetime.date(1973, 12, 31)
_LeapSecD4  = datetime.date(1974, 12, 31)
_LeapSecD5  = datetime.date(1975, 12, 31)
_LeapSecD6  = datetime.date(1976, 12, 31)
_LeapSecD7  = datetime.date(1977, 12, 31)
_LeapSecD8  = datetime.date(1978, 12, 31)
_LeapSecD9  = datetime.date(1979, 12, 31)
_LeapSecD10 = datetime.date(1981,  6, 30)
_LeapSecD11 = datetime.date(1982,  6, 30)
_LeapSecD12 = datetime.date(1983,  6, 30)
_LeapSecD13 = datetime.date(1985,  6, 30)
_LeapSecD14 = datetime.date(1987, 12, 31)
_LeapSecD15 = datetime.date(1989, 12, 31)
_LeapSecD16 = datetime.date(1990, 12, 31)
_LeapSecD17 = datetime.date(1992,  6, 30)
_LeapSecD18 = datetime.date(1993,  6, 30)
_LeapSecD19 = datetime.date(1994,  6, 30)
_LeapSecD20 = datetime.date(1995, 12, 31)
_LeapSecD21 = datetime.date(1997,  6, 30)
_LeapSecD22 = datetime.date(1998, 12, 31)
_LeapSecD23 = datetime.date(2005, 12, 31)
_LeapSecD24 = datetime.date(2008, 12, 31)
_LeapSecD25 = datetime.date(2012,  6, 30)
_LeapSecD26 = datetime.date(2015,  6, 30)
_LeapSecD27 = datetime.date(2016, 12, 31)