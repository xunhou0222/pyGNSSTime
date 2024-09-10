import datetime

from .UtilFunc import sys_week_dow_check, year_doy_check
from .UtilFunc import date2doy, doy2date
from .UtilFunc import date2week, week2date
from .UtilFunc import week2doy, doy2week
from .UtilFunc import UTCFlag, LeapSeconds
from .UtilFunc import fromTAI, toTAI


class GNSSTime:
    '''
    A class that can represent epoch with year/month/day/hour/min/sec, week/sow or year/doy/sod.

    Constructors:
        __new__

        fromDateTime

        fromWeekSow

        fromDOYSod

    Operators:
        __eq__, __ne__, __gt__, __lt__, __ge__, __le__,
        __add__, __radd__, __iadd__, __sub__

    Properties (readonly):
        flag
        year, month, day, hour, minute, second
        week, sow, dow
        doy, sod

    Methods:
        new_convert
        self_convert
        date
        MJD
        isset
        StrFormat

    Static methods:
        
    '''


    def __new__(cls):
        self = object.__new__(cls)

        self._flag = b'G'
        self._year = 1
        self._month = 1
        self._day = 1
        self._hour = 0
        self._minute = 0
        self._second = 0
        self._doy = 1
        self._sod = 0
        self._week = -103260
        self._dow = 1
        self._sow = 86400


    @classmethod
    def fromDateTime(cls, flag: bytes, year: int, month: int, day: int, hour: int, minute: int, second: float):
        self = object.__new__(cls)

        try:
            week, dow = date2week(flag, year, month, day)
        except ValueError as e:
            raise(e)
            return _GNSSTime0

        if hour < 0 or hour > 23:
            raise ValueError(f"hour must be in 0 ... 23, but {hour:d} is given!")
            return _GNSSTime0
        elif minute < 0 or minute > 59:
            raise ValueError(f"minute must be in 0 ... 59, but {minute:d} is given!")
            return _GNSSTime0

        sec_limit = 60
 
        if flag == b'U' or flag  == b'u' or flag == b'R' or flag  == b'r':
            sec_limit += UTCFlag(datetime.date(year, month, day))

        if second < 0 or second >= sec_limit:
            raise ValueError(f"second must be in 0 ... {sec_limit:d} (excluded) for this date, "
                             f"but {second:f} is given!")
            return _GNSSTime0
        
        self._flag = flag
        self._year, self._month, self._day = year, month, day
        self._hour, self._minute, self._second = hour, minute, second
        self._doy = date2doy(year, month, day)
        self._sod = hour*3600 + minute*60 + second
        self._week = week
        self._sow = dow*86400 + self._sod

        if flag == b'U' or flag == b'u':
            self._sow += LeapSeconds(datetime.date(year, month, day)) - 10
        elif flag == b'R' or flag  == b'r':
            d = datetime.date(year, month, day)

            if hour < 3 and year >= 1972:
                d -= datetime.timedelta(days=1)

            self._sow += LeapSeconds(d) - 10
        elif flag == b'E' or flag  == b'e':
            self._sow += 13

        if self._sow >= 604800:
            self._week += 1
            self._sow -= 604800
        elif self._sow < 0:
            self._week -= 1
            self._sow += 604800

        self._dow = int(self._sow/86400)
        
        return self


    @classmethod
    def fromWeekSow(cls, flag: bytes, week: int, sow: float):
        self = object.__new__(cls)

        dow = int(sow/86400)

        try:
            sys_week_dow_check(flag, week, dow)
        except ValueError as e:
            raise(e)
            return _GNSSTime0

        if sow < 0 or sow >= 604800:
            raise ValueError(f"sow must be in 0...606800 (excluded), but {sow:f} is given!")
            return _GNSSTime0
        
        self._flag = flag
        self._week = week
        self._sow = sow
        self._dow = int(self._sow/86400)
        self._year, self._month, self._day = week2date(flag, week, dow)
        self._sod = sow - dow*86400

        if flag == b'U' or flag == b'u':
            d = datetime.date(self._year, self._month, self._day)
            self._sod -= LeapSeconds(d) - 10
    
            if (self._sod < 0):
                d -= datetime.timedelta(days=1)
                self._year = d.year
                self._month = d.month
                self._day = d.day
                self._sod += 86400 + UTCFlag(d)
        elif flag == b'R' or flag == b'r':
            d = datetime.date(self._year, self._month, self._day)

            if self._sod < 10800 and self._year >= 1972:
                d -= datetime.timedelta(days=1)
            
            self._sod -= LeapSeconds(d) - 10
    
            if (self._sod < 0):
                d -= datetime.timedelta(days=1)
                self._year = d.year
                self._month = d.month
                self._day = d.day
                self._sod += 86400 + UTCFlag(d)
        elif flag == b'E' or flag == b'e':
            if ( int(self._sow)%86400 < 13 ):
                d = datetime.date(self._year, self._month, self._day)
                d -= datetime.timedelta(days=1)
                self._year = d.year
                self._month = d.month
                self._day = d.day

            self._sod -= 13

            if self._sod < 0:
                self._sod += 86400

        self._hour = int(self._sod/3600)

        if self._hour == 24:
            self._hour -= 1

        self._minute = int( (self._sod - self._hour*3600) / 60 )

        if self._minute == 60:
            self._minute -= 1

        self._second = self._sod - self._hour*3600 - self._minute*60
        self._doy = date2doy(self._year, self._month, self._day)

        return self


    @classmethod
    def fromDOYSod(cls, flag: bytes, year: int, doy: int, sod: float):
        self = object.__new__(cls)

        try:
            year_doy_check(year, doy)
        except ValueError as e:
            raise(e)
            return _GNSSTime0
    
        self._week, dow = doy2week(flag, year, doy)
        self._month, self._day = doy2date(year, doy)

        sod_limit = 86400

        if flag == b'U' or flag == b'u':
            sod_limit += UTCFlag(datetime.date(year, self._month, self._day))
        elif flag == b'R' or flag == b'r':
            d = datetime.date(year, self._month, self._day) 

            if sod < 10800 and year >= 1972:
                d -= datetime.timedelta(days=1)

            sod_limit += UTCFlag(d)
            
        if sod < 0 or sod >= sod_limit:
            raise ValueError("sod (second of day) must be in 0...{sod_limit:d} (excluded), but {sod:f} is given!")
            return _GNSSTime0

        self._flag = flag
        self._year = year
        self._doy = doy
        self._sod = sod  
        self._hour = int(sod/3600)
        
        if self._hour == 24:
            self._hour -= 1
        
        self._minute = int( (sod - self._hour*3600) / 60 )

        if self._minute == 60:
            self._minute -= 1

        self._second = sod - self._hour*3600 - self._minute*60
        self._sow = self._sod + dow*86400

        if flag == b'U' or flag == b'u':
            self._sow += LeapSeconds(datetime.date(self._year, self._month, self._day)) - 10
        elif flag == b'R' or flag == b'r':
            d = datetime.date(self._year, self._month, self._day)

            if self._hour < 3 and self._year >= 1972:
                d -= datetime.timedelta(days=1)
            
            self._sow += LeapSeconds(d) - 10
        elif flag == b'E' or flag == b'e':
            self._sow += 13
    
        if self._sow >= 604800:
            self._sow -= 604800
            self._week += 1
        elif self._sow < 0:
            self._sow +=604800
            self._week -= 1

        self._dow = int(self._sow/86400)

        return self


    def __eq__(self, other):
        return cmp_GNSSTime(self, other) == 0

    def __gt__(self, other):
        return cmp_GNSSTime(self, other) > 0

    def __ge__(self, other):
        return cmp_GNSSTime(self, other) >= 0


    def __add__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError("Type mismatch: " + str(type(other)) + " is added to GNSSTime object!")
            return _GNSSTime0

        week = self._week
        sow = self._sow + other

        while sow >= 604800:
            sow -= 604800
            week += 1

        while sow < 0:
            sow += 604800
            week -= 1

        try:
            new_time = GNSSTime.fromWeekSow(self._flag, week, sow)
        except ValueError as e:
            raise ValueError(str(e) + " The seconds to be added is not appropriate, and the resulted GNSSTime is out of range!")
            return _GNSSTime0

        return new_time
    

    def __radd__(self, other):
        return self + other
    

    def __iadd__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Type mismatch: " + str(type(other)) + " is added to GNSSTime object!")
            return _GNSSTime0

        week = self._week
        sow = self._sow + other

        while sow >= 604800:
            sow -= 604800
            week += 1

        while sow < 0:
            sow += 604800
            week -= 1

        try:
            new_time = GNSSTime.fromWeekSow(self._flag, week, sow)
        except ValueError as e:
            raise ValueError(str(e) + " The seconds to be added is not appropriate, and the resulted GNSSTime is out of range!")
            return _GNSSTime0
        
        self._flag = new_time._flag
        self._year = new_time._year
        self._month = new_time._month
        self._day = new_time._day
        self._hour = new_time._hour
        self._minute = new_time._minute
        self._second = new_time._second
        self._doy = new_time._doy
        self._sod = new_time._sod
        self._week = new_time._week
        self._dow = new_time._dow
        self._sow = new_time._sow

        return self


    def __sub__(self, other):
        if isinstance(other, (int, float)):
            week = self._week
            sow = self._sow - other

            while sow >= 604800:
                sow -= 604800
                week += 1

            while sow < 0:
                sow += 604800
                week -= 1

            try:
                new_time = GNSSTime.fromWeekSow(self._flag, week, sow)
            except ValueError as e:
                raise ValueError(str(e) + " The seconds to be subtracted is not appropriate, and the resulted GNSSTime is out of range!")
                return _GNSSTime0

            return new_time
        elif isinstance(other, GNSSTime):
            if other._flag == self._flag:
                return (self._week - other._week)*604800 + (self._sow - other._sow)
            else:
                other_new = other.new_convert(self._flag)
                return (self._week - other_new._week)*604800 + (self._sow - other_new._sow)
        else:
            raise TypeError("Type mismatch: " + str(type(other)) + " is subtracted from GNSSTime object!")
            return _GNSSTime0


    def __isub__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Type mismatch: " + str(type(other)) + " is subtracted from GNSSTime object!")
            return _GNSSTime0
        
        week = self._week
        sow = self._sow - other

        while sow >= 604800:
            sow -= 604800
            week += 1

        while sow < 0:
            sow += 604800
            week -= 1

        try:
            new_time = GNSSTime.fromWeekSow(self._flag, week, sow)
        except ValueError as e:
            raise ValueError(str(e) + " The seconds to be subtracted is not appropriate, and the resulted GNSSTime is out of range!")
            return _GNSSTime0

        self._flag = new_time._flag
        self._year = new_time._year
        self._month = new_time._month
        self._day = new_time._day
        self._hour = new_time._hour
        self._minute = new_time._minute
        self._second = new_time._second
        self._doy = new_time._doy
        self._sod = new_time._sod
        self._week = new_time._week
        self._dow = new_time._dow
        self._sow = new_time._sow    

        return self


    @property
    def flag(self):
        return self._flag
    
    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month
    
    @property
    def day(self):
        return self._day

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute
    
    @property
    def second(self):
        return self._second

    @property
    def week(self):
        return self._week

    @property
    def dow(self):
        return self._dow

    @property
    def sow(self):
        return self._sow

    @property
    def doy(self):
        return self._doy

    @property
    def sod(self):
        return self._sod


    def new_convert(self, flag: bytes):
        ''' Copy the GNSSTime object and convert the new object to a desired time system! '''
        sys_week_dow_check(flag, 0, 0)
        
        if flag.upper() == self._flag.upper():
            return GNSSTime.fromWeekSow(flag, self._week, self._sow)
                
        if self._flag == b'A' or self._flag == b'a':    # From TAI to others.
            week, sow = fromTAI(self._week, self._sow, flag)
        elif flag == b'A' or flag == b'a':    # From others to TAI.
            week, sow = toTAI(self._flag, self._week, self._sow)
        else:    # From others to others.
            week, sow = toTAI(self._flag, self._week, self._sow)
            week, sow = fromTAI(week, sow, flag)

        return GNSSTime.fromWeekSow(flag, week, sow)


    def self_convert(self, flag: bytes):
        ''' Convert the object to a desired time system! '''
        new_time = self.new_convert(flag)

        self._flag = new_time._flag
        self._year = new_time._year
        self._month = new_time._month
        self._day = new_time._day
        self._hour = new_time._hour
        self._minute = new_time._minute
        self._second = new_time._second
        self._doy = new_time._doy
        self._sod = new_time._sod
        self._week = new_time._week
        self._dow = new_time._dow
        self._sow = new_time._sow


    def date(self) -> datetime.date:
        return datetime.date(self._year, self._month, self._day)
    

    def MJD(self) -> tuple[int, float]:
        date0 = datetime.date(1858, 11, 17)
        MJD_int = (self.date() - date0).days
        MJD_frac = self._sod/86400

        return MJD_int, MJD_frac


    def isset(self) -> bool :
        return False if self == _GNSSTime0 else True
    

    def StrFormat(self, fmt: str, n: int) -> str:
        week = self._week
        sow  = self._sow

        if n < 0:
            n = 0

        if 1.0 - sow + int(sow) < 0.5/pow(10.0, n):
            sow = int(sow) + 1.0
    
            if sow >= 604800:
                week += 1
                sow -= 604800

        t = GNSSTime.fromWeekSow(self._flag, week, sow)

        if fmt.find("{YEAR}") != -1:
            fmt = fmt.replace("{YEAR}", f"{t._year:d}")

        if fmt.find("{year}") != -1:
            if (t._year < 2000):
                yy = t._year - 1900
            else:
                yy = t._year - 2000

            fmt = fmt.replace("{year}", f"{yy:d}")
        
        if fmt.find("{MON}") != -1:
            fmt = fmt.replace("{MON}", f"{t._month:02d}")
    
        if fmt.find("{DAY}") != -1:
            fmt = fmt.replace("{DAY}", f"{t._day:02d}")
    
        if fmt.find("{HOUR}") != -1:
            fmt = fmt.replace("{HOUR}", f"{t._hour:02d}")
    
        if fmt.find("{MIN}") != -1:
            fmt = fmt.replace("{MIN}", f"{t._minute:02d}")
    
        if fmt.find("{SEC}") != -1:
            if n <= 0:
                w = 2
                p = 0
            else:
                w = n + 3
                p = n

            fmt = fmt.replace("{SEC}", f"{t._second:02.{p}f}")
    
        if fmt.find("{DOY}") != -1:
            fmt = fmt.replace("{DOY}", f"{t._doy:d}")

        if fmt.find("{SOD}") != -1:
            if n <= 0:
                w = 5
                p = 0
            else:
                w = n + 6
                p = n
            
            fmt = fmt.replace("{SOD}", f"{t._sod:.{p}f}")

        if fmt.find("{WEEK}") != -1:
            fmt = fmt.replace("{WEEK}", f"{t._week:d}")

        if fmt.find("{DOW}") != -1:
            fmt = fmt.replace("{DOW}", f"{t._dow:d}")

        if fmt.find("{SOW}") != -1:
            if n <= 0:
                w = 6
                p = 0
            else:
                w = n + 7
                p = n
            fmt = fmt.replace("{SOW}", f"{t._sow:.{p}f}")

        return fmt


    @classmethod
    def fromStr(cls, flag:bytes, strline:str) :
        token = strline.split()
        num = 0

        for i in range( len(token) ):
            try:
                float(token[i])
            except:
                continue

            num += 1

        try:
            if num == 6:
                return cls.fromDateTime(flag, int(token[0]), int(token[1]), int(token[2]), 
                                              int(token[3]), int(token[4]), float(token[5]))
            elif num == 2:
                return cls.fromWeekSow(flag, int(token[0]), float(token[1]))
            elif num == 3:
                return cls.fromDOYSod(flag, int(token[0]), int(token[1]), float(token[2]))
            else:
                return _GNSSTime0
        except:
            return _GNSSTime0
        
        return _GNSSTime0


    @classmethod
    def now(cls):
        t = datetime.datetime.now()

        return cls.fromDateTime(b'U', t.year, t.month, t.day, t.hour, t.minute, t.second)


_GNSSTime0 = GNSSTime() 


def cmp_GNSSTime(t1:GNSSTime, t2:GNSSTime):
    if not isinstance(t1, GNSSTime) or not isinstance(t2, GNSSTime):
        raise ValueError(f"Type mismatch: {str(type(t1))} object is compared to {str(type(t2))} object!")

    week, sow = t1.week, t1.sow

    if t1.flag.upper() == t2.flag.upper():
        week2, sow2 = t2.week, t2.sow
    else:
        t2_new = t2.new_convert(t1.flag)
        week2, sow2 = t2_new.week, t2_new.sow
        
    if (week, sow) < (week2, sow2):
        return -1
    elif (week, sow) == (week2, sow2):
        return 0 
    else:
        return 1