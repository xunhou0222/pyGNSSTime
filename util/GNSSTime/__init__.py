'''
    GNSSTime is a python library used to represent several time systems that are frequently 
encountered in GNSS field. In this library, time is expressed in different format, e.g., 
"Y-M-D H:M:S", "week/sow", and "year/doy/sod", and in different systems such as TAI, TT
UTC, GPST, GLONASS-UTC, BDT and GST.
    The origins of time systems:
        TAI        1958-01-01 00:00:00 (TAI)        1958-01-01 00:00:00 (TAI)        1958-12-31 23:59:50 (UTC)
        TT         1977-01-01 00:00:00 (TT)         1976-12-31 23:59:27.816 (TAI)    1976-12-31 23:59:13.816 (UTC)
        UTC        1972-01-01 00:00:00 (UTC)        1972-01-01 00:00:10 (TAI)        1972-01-01 00:00:00 (UTC)  
        GPST       1980-01-06 00:00:00 (GPST)       1980-01-06 00:00:19 (TAI)        1980-01-06 00:00:00 (UTC)
        GLO-UTC    1972-01-01 00:00:00 (GLO-UTC)    1972-01-01 03:00:10 (TAI)        1972-01-01 03:00:00 (UTC)
        BDT        2006-01-01 00:00:00 (BDT)        2006-01-01 00:00:33 (TAI)        2006-01-01 00:00:00 (UTC)
        GST        1999-08-21 23:59:47 (GST)        1999-08-22 00:00:19 (TAI)        1999-08-21 23:59:47 (UTC)
    Among the time systems this library concerns, there are some suttle problems, which are 
mainly found in UTC. Due to leap seconds, UTC is not a consecutive time system like TAI 
and GPST. That means, there would be 86401 or 86399 seconds in some days. In this library, 
UTC is handled as below: 
    In year/doy/sod format, sod can be 86401 or 86399 seconds, but in week/sow format, sow 
must not exceed 604800. 
    Since GNSSTime is implemented on the basis of datetime.date, which can only represent year 
from 1 to 9999, there is a lowwer/upper limit for each GNSS time system (see Const.py). 
'''


from .Const import SUPPORTED_TIME_SYS
from .Const import MINTAIWEEK, MINTAIWEEK_MINDOW, MAXTAIWEEK, MAXTAIWEEK_MAXDOW
from .Const import MINTTWEEK, MINTTWEEK_MINDOW, MAXTTWEEK, MAXTTWEEK_MAXDOW
from .Const import MINUTCWEEK, MINUTCWEEK_MINDOW, MAXUTCWEEK, MAXUTCWEEK_MAXDOW
from .Const import MINGPSWEEK, MINGPSWEEK_MINDOW, MAXGPSWEEK, MAXGPSWEEK_MAXDOW
from .Const import MINGLOWEEK, MINGLOWEEK_MINDOW, MAXGLOWEEK, MAXGLOWEEK_MAXDOW
from .Const import MINBDSWEEK, MINBDSWEEK_MINDOW, MAXBDSWEEK, MAXBDSWEEK_MAXDOW
from .Const import MINGALWEEK, MINGALWEEK_MINDOW, MAXGALWEEK, MAXGALWEEK_MAXDOW

from .UtilFunc import date2week, week2date
from .UtilFunc import date2doy, doy2date
from .UtilFunc import week2doy, doy2week

from .GNSSTime import GNSSTime