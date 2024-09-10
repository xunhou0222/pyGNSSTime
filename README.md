# pyGNSSTime

## 简介

pyGNSSTime是一个基于PyQT6实现的GNSS时间转换GUI程序，支持GNSS领域常见的时间系统（GPST、BDT、GST、UTC、TT与TAI等）及其不同格式（“年-月-日 时:分:秒”、“周 周内秒”、“年 年积日 天内秒”、RJD与MJD等）之间的转换。

pyGNSSTime主要由两部分构成：其一是名为GNSSTime的class，封装时间系统的表示及转换算法（注：该class的实现里吸收了python标准库datetime的部分思想，例如假设1年1月1日至9999年12月31日均采用现行格里历，故GNSSTime的有效时间范围也大大致如是；其二是基于PyQt6的GUI界面封装。

## 依赖

- python 3.7+
- PyQt6
- pyinstaller（Windows下可执行程序打包）
- py2app（MacOS下app打包）

## 其他
- 如有bug，敬请反馈
- pyGNSSTime的ICON图片来源于网络，如有侵权，请联系删除
