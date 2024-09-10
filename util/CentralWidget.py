from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout, QGroupBox
from PyQt6.QtWidgets import QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QKeyEvent, QFont
from PyQt6.QtCore import Qt, QDateTime

from datetime import date, timedelta
from math import floor

from util.GNSSTime import GNSSTime


__all__ = ['myCentralWiget']


class myCentralWiget(QWidget):
    def __init__(self, win:QMainWindow):
        super().__init__()

        self._win = win

        self._items = [ 'GPST_date', 'GPST_week', 'GPST_doy',            'GPST_rjd', 
                        'BDT_date',  'BDT_week',  'BDT_doy',             'BDT_rjd',
                        'GST_date',  'GST_week',  'GST_doy',             'GST_rjd',
                        'UTC_date',               'UTC_doy',  'UTC_mjd', 'UTC_rjd', 
                        'TAI_date',               'TAI_doy',             'TAI_rjd', 
                        'TT_date',                 'TT_doy',             'TT_rjd'    ]
        # 1. Initialize caches.
        self._caches = { item : ''    for item in self._items }
        # 2. Initialize text.
        self._texts = { item : ''    for item in self._items }
        # 3. Set widgets.
        self._widgets = { item : QLineEdit()    for item in self._items }
        self.SetWidgets()

    
    def keyPressEvent(self, event:QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            self.btn_click()


    def SetWidgets(self):
        lay = QGridLayout()

        # 1. GPST entries (GPS).
        GPST_box = QGroupBox('GPST')
        GPST_lay = QGridLayout()

        self._widgets['GPST_date'].setPlaceholderText('年-月-日    时:分:秒')
        self._widgets['GPST_date'].setClearButtonEnabled(True)
        self._widgets['GPST_date'].setFont(QFont('SimHei', 12))
        GPST_lay.addWidget(self._widgets['GPST_date'], 0, 0)

        self._widgets['GPST_week'].setPlaceholderText('周    周内秒')
        self._widgets['GPST_week'].setClearButtonEnabled(True)
        self._widgets['GPST_week'].setFont(QFont('SimHei', 12))
        GPST_lay.addWidget(self._widgets['GPST_week'], 1, 0)

        self._widgets['GPST_doy'].setPlaceholderText('年    年积日    天内秒')
        self._widgets['GPST_doy'].setClearButtonEnabled(True)
        self._widgets['GPST_doy'].setFont(QFont('SimHei', 12))
        GPST_lay.addWidget(self._widgets['GPST_doy'], 2, 0)

        self._widgets['GPST_rjd'].setPlaceholderText('RJD  (日  天内秒)')
        self._widgets['GPST_rjd'].setClearButtonEnabled(True)
        self._widgets['GPST_rjd'].setFont(QFont('SimHei', 12))
        GPST_lay.addWidget(self._widgets['GPST_rjd'], 3, 0)

        GPST_box.setLayout(GPST_lay)
        GPST_box.setStyleSheet("QGroupBox {border:1px solid black; margin-top:18px; font-weight:bold; font-size:14px;} "
                               "QGroupBox::title {subcontrol-position: top left; top:-18px}")
        lay.addWidget(GPST_box, 0, 0, 4, 3)

        # 2. BDT entries (BDS).
        BDT_box = QGroupBox('BDT')
        BDT_lay = QGridLayout()

        self._widgets['BDT_date'].setPlaceholderText('年-月-日     时:分:秒')
        self._widgets['BDT_date'].setClearButtonEnabled(True)
        self._widgets['BDT_date'].setFont(QFont('SimHei', 12))
        BDT_lay.addWidget(self._widgets['BDT_date'], 0, 0)

        self._widgets['BDT_week'].setPlaceholderText('周    周内秒')
        self._widgets['BDT_week'].setClearButtonEnabled(True)
        self._widgets['BDT_week'].setFont(QFont('SimHei', 12))
        BDT_lay.addWidget(self._widgets['BDT_week'], 1, 0)

        self._widgets['BDT_doy'].setPlaceholderText('年    年积日    天内秒')
        self._widgets['BDT_doy'].setClearButtonEnabled(True)
        self._widgets['BDT_doy'].setFont(QFont('SimHei', 12))
        BDT_lay.addWidget(self._widgets['BDT_doy'], 2, 0)

        self._widgets['BDT_rjd'].setPlaceholderText('RJD  (日  天内秒)')
        self._widgets['BDT_rjd'].setClearButtonEnabled(True)
        self._widgets['BDT_rjd'].setFont(QFont('SimHei', 12))
        BDT_lay.addWidget(self._widgets['BDT_rjd'], 3, 0)

        BDT_box.setLayout(BDT_lay)
        BDT_box.setStyleSheet("QGroupBox {border:1px solid black; margin-top:18px; font-weight:bold; font-size:14px;} "
                              "QGroupBox::title {subcontrol-position: top left; top:-18px}")
        lay.addWidget(BDT_box, 0, 3, 4, 3)

        # 3. GST entries (GALILEO).
        GST_box = QGroupBox('GST')
        GST_lay = QGridLayout()

        self._widgets['GST_date'].setPlaceholderText('年-月-日     时:分:秒')
        self._widgets['GST_date'].setClearButtonEnabled(True)
        self._widgets['GST_date'].setFont(QFont('SimHei', 12))
        GST_lay.addWidget(self._widgets['GST_date'], 0, 0, 1, 1)

        self._widgets['GST_week'].setPlaceholderText('周    周内秒')
        self._widgets['GST_week'].setClearButtonEnabled(True)
        self._widgets['GST_week'].setFont(QFont('SimHei', 12))
        GST_lay.addWidget(self._widgets['GST_week'], 1, 0)

        self._widgets['GST_doy'].setPlaceholderText('年    年积日    天内秒')
        self._widgets['GST_doy'].setClearButtonEnabled(True)
        self._widgets['GST_doy'].setFont(QFont('SimHei', 12))
        GST_lay.addWidget(self._widgets['GST_doy'], 2, 0)

        self._widgets['GST_rjd'].setPlaceholderText('RJD  (日  天内秒)')
        self._widgets['GST_rjd'].setClearButtonEnabled(True)
        self._widgets['GST_rjd'].setFont(QFont('SimHei', 12))
        GST_lay.addWidget(self._widgets['GST_rjd'], 3, 0)

        GST_box.setLayout(GST_lay)
        GST_box.setStyleSheet("QGroupBox {border:1px solid black; margin-top:18px; font-weight:bold; font-size:14px;} "
                              "QGroupBox::title {subcontrol-position: top left; top:-18px}")
        lay.addWidget(GST_box, 4, 0, 4, 3)

        # 4. UTC
        UTC_box = QGroupBox('UTC')
        UTC_lay = QGridLayout()

        self._widgets['UTC_date'].setPlaceholderText('年-月-日    时:分:秒')
        self._widgets['UTC_date'].setClearButtonEnabled(True)
        self._widgets['UTC_date'].setFont(QFont('SimHei', 12))
        UTC_lay.addWidget(self._widgets['UTC_date'], 0, 0)

        self._widgets['UTC_doy'].setPlaceholderText('年    年积日    天内秒')
        self._widgets['UTC_doy'].setClearButtonEnabled(True)
        self._widgets['UTC_doy'].setFont(QFont('SimHei', 12))
        UTC_lay.addWidget(self._widgets['UTC_doy'], 1, 0)

        self._widgets['UTC_mjd'].setPlaceholderText('MJD  (日  天内秒)')
        self._widgets['UTC_mjd'].setClearButtonEnabled(True)
        self._widgets['UTC_mjd'].setFont(QFont('SimHei', 12))
        UTC_lay.addWidget(self._widgets['UTC_mjd'], 2, 0)

        self._widgets['UTC_rjd'].setPlaceholderText('RJD  (日  天内秒)')
        self._widgets['UTC_rjd'].setClearButtonEnabled(True)
        self._widgets['UTC_rjd'].setFont(QFont('SimHei', 12))
        UTC_lay.addWidget(self._widgets['UTC_rjd'], 3, 0)

        UTC_box.setLayout(UTC_lay)
        UTC_box.setStyleSheet("QGroupBox {border:1px solid black; margin-top:18px; font-weight:bold; font-size:14px;} "
                              "QGroupBox::title {subcontrol-position: top left; top:-18px}")
        lay.addWidget(UTC_box, 4, 3, 4, 3)

        # 5. TAI
        TAI_box = QGroupBox('TAI')
        TAI_lay = QGridLayout()

        self._widgets['TAI_date'].setPlaceholderText('年-月-日    时:分:秒')
        self._widgets['TAI_date'].setClearButtonEnabled(True)
        self._widgets['TAI_date'].setFont(QFont('SimHei', 12))
        TAI_lay.addWidget(self._widgets['TAI_date'], 0, 0)

        self._widgets['TAI_doy'].setPlaceholderText('年    年积日    天内秒')
        self._widgets['TAI_doy'].setClearButtonEnabled(True)
        self._widgets['TAI_doy'].setFont(QFont('SimHei', 12))
        TAI_lay.addWidget(self._widgets['TAI_doy'], 1, 0)

        self._widgets['TAI_rjd'].setPlaceholderText('RJD  (日  天内秒)')
        self._widgets['TAI_rjd'].setClearButtonEnabled(True)
        self._widgets['TAI_rjd'].setFont(QFont('SimHei', 12))
        TAI_lay.addWidget(self._widgets['TAI_rjd'], 2, 0)

        TAI_box.setLayout(TAI_lay)
        TAI_box.setStyleSheet("QGroupBox {border:1px solid black; margin-top:18px; font-weight:bold; font-size:14px;} "
                              "QGroupBox::title {subcontrol-position: top left; top:-18px}")
        lay.addWidget(TAI_box, 8, 0, 4, 3)

        # 6. TT
        TT_box = QGroupBox('TT')
        TT_lay = QGridLayout()

        self._widgets['TT_date'].setPlaceholderText('年-月-日    时:分:秒')
        self._widgets['TT_date'].setClearButtonEnabled(True)
        self._widgets['TT_date'].setFont(QFont('SimHei', 12))
        TT_lay.addWidget(self._widgets['TT_date'], 0, 0)

        self._widgets['TT_doy'].setPlaceholderText('年    年积日    天内秒')
        self._widgets['TT_doy'].setClearButtonEnabled(True)
        self._widgets['TT_doy'].setFont(QFont('SimHei', 12))
        TT_lay.addWidget(self._widgets['TT_doy'], 1, 0)

        self._widgets['TT_rjd'].setPlaceholderText('RJD  (日  天内秒)')
        self._widgets['TT_rjd'].setClearButtonEnabled(True)
        self._widgets['TT_rjd'].setFont(QFont('SimHei', 12))
        TT_lay.addWidget(self._widgets['TT_rjd'], 2, 0)

        TT_box.setLayout(TT_lay)
        TT_box.setStyleSheet("QGroupBox {border:1px solid black; margin-top:18px; font-weight:bold; font-size:14px;} "
                             "QGroupBox::title {subcontrol-position: top left; top:-18px}")
        lay.addWidget(TT_box, 8, 3, 4, 3)

        # 6. Buttons
        btn_wig = QWidget()

        btn1 = QPushButton('转换')
        btn1.clicked.connect(self.btn_click)
        btn1.setFont(QFont('SimHei', 12))

        lay.addWidget(btn1, 12, 2, 1, 1)

        btn2 = QPushButton('关闭')
        btn2.clicked.connect(self._win.close)
        btn2.setFont(QFont('SimHei', 12))

        lay.addWidget(btn2, 12, 3, 1, 1)

        lay.setContentsMargins(50, 30, 50, 30)
        lay.setSpacing(20)
        self.setLayout(lay)
        

    def btn_click(self):
        item_get = ''
        str_get  = ''

        for item in self._items:
            self._texts[item] = self._widgets[item].text()

            if self._texts[item] != self._caches[item]:
                item_get = item
                str_get  = self._texts[item]

        if not item_get or not str_get:    # 输入框未输入，则获取当前时间
            t_u = QDateTime.currentDateTimeUtc()

            try:
                t = GNSSTime.fromDateTime(b'U', t_u.date().year(), t_u.date().month(), t_u.date().day(), 
                                          t_u.time().hour(), t_u.time().minute(), t_u.time().second() + t_u.time().msec()/1000)
            except:
                QMessageBox.critical(self._win, 'FATAL', '获取当前UTC时间错误!')
                return
        else:
            if 'GPST' in item_get:
                flag = b'G'
            elif 'BDT' in item_get:
                flag = b'C'
            elif 'GST' in item_get:
                flag = b'E'
            elif 'TAI' in item_get:
                flag = b'A'
            elif 'TT' in item_get:
                flag = b'T'
            elif 'UTC' in item_get:
                flag = b'U'

            try:
                token = str_get.split()

                if 'date' in item_get:
                    date_tokens = token[0].split('-')
                    time_tokens = token[1].split(':')
                    year = int(date_tokens[0])
                    mon  = int(date_tokens[1])
                    day  = int(date_tokens[2])
                    hour = int(time_tokens[0])
                    min  = int(time_tokens[1])
                    sec  = float(time_tokens[2])
                    t = GNSSTime.fromDateTime(flag, year, mon, day, hour, min, sec)
                elif 'week' in item_get:
                    week = int(token[0])
                    sow = float(token[1])
                    t = GNSSTime.fromWeekSow(flag, week, sow)
                elif 'doy' in item_get:
                    year = int(token[0])
                    doy  = int(token[1])
                    sod  = float(token[2])
                    t = GNSSTime.fromDOYSod(flag, year, doy, sod)
                elif 'mjd' in item_get:
                    mjd  = int(token[0])
                    sod = float(token[1])
                    d = date(1858, 11, 17) + timedelta(days=mjd)
                    
                    t = GNSSTime.fromDateTime(flag, d.year, d.month, d.day, 0, 0, 0) + sod
                else:
                    rjd = float(token[0])
                    rjd_int = floor(rjd)
                    rjd_part = rjd - rjd_int

                    if rjd_part != 0.5:
                        QMessageBox.critical(self._win, 'FATAL', '输入的时间错误!')

                    sod = float(token[1])
                    d = date(2000, 1, 1) + timedelta(days=rjd_int + 1)
                    t = GNSSTime.fromDateTime(flag, d.year, d.month, d.day, 0, 0, 0) + sod
            except Exception as e:
                QMessageBox.critical(self._win, 'FATAL', '输入的时间错误!')
                return
        
        t_gps = t.new_convert(b'G')
        t_bds = t.new_convert(b'C')
        t_gal = t.new_convert(b'E')
        t_utc = t.new_convert(b'U')
        t_tai = t.new_convert(b'A')
        t_tt  = t.new_convert(b'T')

        self._caches['GPST_date'] = self._texts['GPST_date'] = t_gps.StrFormat('{YEAR}-{MON}-{DAY}    {HOUR}:{MIN}:{SEC}', 5)
        self._caches['GPST_week'] = self._texts['GPST_week'] = t_gps.StrFormat('{WEEK}    {SOW}', 5)
        self._caches['GPST_doy']  = self._texts['GPST_doy']  = t_gps.StrFormat('{YEAR}    {DOY}    {SOD}', 5)
        rjd = ( t_gps.date() - date(2000, 1, 1) ).days - 0.5
        self._caches['GPST_rjd']  = self._texts['GPST_rjd']  = f"{rjd:.1f}    {t_gps.sod:.5f}"

        self._caches['BDT_date'] = self._texts['BDT_date'] = t_bds.StrFormat('{YEAR}-{MON}-{DAY}    {HOUR}:{MIN}:{SEC}', 5)
        self._caches['BDT_week'] = self._texts['BDT_week'] = t_bds.StrFormat('{WEEK}    {SOW}', 5)
        self._caches['BDT_doy']  = self._texts['BDT_doy']  = t_bds.StrFormat('{YEAR}    {DOY}   {SOD}', 5)
        rjd = ( t_bds.date() - date(2000, 1, 1) ).days - 0.5
        self._caches['BDT_rjd']  = self._texts['BDT_rjd']  = f"{rjd:.1f}    {t_bds.sod:.5f}"

        self._caches['GST_date'] = self._texts['GST_date'] = t_gal.StrFormat('{YEAR}-{MON}-{DAY}    {HOUR}:{MIN}:{SEC}', 5)
        self._caches['GST_week'] = self._texts['GST_week'] = t_gal.StrFormat('{WEEK}    {SOW}', 5)
        self._caches['GST_doy']  = self._texts['GST_doy']  = t_gal.StrFormat('{YEAR}    {DOY}   {SOD}', 5)
        rjd = ( t_gal.date() - date(2000, 1, 1) ).days - 0.5
        self._caches['GST_rjd']  = self._texts['GST_rjd']  = f"{rjd:.1f}    {t_gal.sod:.5f}"

        self._caches['UTC_date'] = self._texts['UTC_date'] = t_utc.StrFormat('{YEAR}-{MON}-{DAY}    {HOUR}:{MIN}:{SEC}', 5)
        self._caches['UTC_doy']  = self._texts['UTC_doy']  = t_utc.StrFormat('{YEAR}    {DOY}    {SOD}', 5)
        mjd = ( t_utc.date() - date(1858, 11, 17) ).days
        self._caches['UTC_mjd']  = self._texts['UTC_mjd']  = f"{mjd:d}    {t_utc.sod:.5f}"
        rjd = ( t_utc.date() - date(2000, 1, 1) ).days - 0.5
        self._caches['UTC_rjd']  = self._texts['UTC_rjd']  = f"{rjd:.1f}    {t_utc.sod:.5f}"

        self._caches['TAI_date'] = self._texts['TAI_date'] = t_tai.StrFormat('{YEAR}-{MON}-{DAY}    {HOUR}:{MIN}:{SEC}', 5)
        self._caches['TAI_doy']  = self._texts['TAI_doy']  = t_tai.StrFormat('{YEAR}    {DOY}    {SOD}', 5)
        rjd = ( t_tai.date() - date(2000, 1, 1) ).days - 0.5
        self._caches['TAI_rjd']  = self._texts['TAI_rjd']  = f"{rjd:.1f}    {t_tai.sod:.5f}"

        self._caches['TT_date'] = self._texts['TT_date'] = t_tt.StrFormat('{YEAR}-{MON}-{DAY}    {HOUR}:{MIN}:{SEC}', 5)
        self._caches['TT_doy']  = self._texts['TT_doy']  = t_tt.StrFormat('{YEAR}    {DOY}    {SOD}', 5)
        rjd = ( t_tt.date() - date(2000, 1, 1) ).days - 0.5
        self._caches['TT_rjd']  = self._texts['TT_rjd']  = f"{rjd:.1f}    {t_tt.sod:.5f}"

        for item in self._items:
            self._widgets[item].setText(self._texts[item])
