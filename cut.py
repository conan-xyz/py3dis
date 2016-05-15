#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

basedir = ""
orPATH = "{0}/cut_tmp".format(basedir)
fiPATH = "{0}/cut".format(basedir)

filename = sorted([f for f in os.listdir(orPATH) if re.search(r'.*[0-9]$', f)])[-1]


def format_time(s):
    if not 'T' in s:
        return False
    sp = ' '
    li = re.split(r'[T+]', s)
    return sp.join(li[:2])


def format_ip(s):
    ip_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]"
    if not re.search(ip_regex, s):
        return False
    return s


def format_str(s):
    if not s.startswith('/?'):
        return False

    s = s[2:]
    return s


newfile = "{0}/{1}".format(fiPATH, filename)
oldfile = "{0}/{1}".format(orPATH, filename)

with open(newfile, 'w') as nf:
    with open(oldfile, 'r') as f:

        for line in f.readlines():
            if re.findall('actionname=', line):
                datalist = line.split()

                time = format_time(datalist[0])
                ip = datalist[1]
                message = format_str(datalist[3])

                comma = ','

                if time and ip and message:
                    newline = '{0}, {1}, {2}'.format(time, ip, message)
                else:
                    continue

                nf.write(newline + '\n')
