#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 ctf <hailongeric@gmail.com>
#
# Distributed under terms of the MIT license.

"""
https://ctf.sixstars.team/challenges#journey_sparc
reverse 2018 Google CTF sparc
https://www.gaisler.com/doc/sparcv8.pdf
af6712f206cf001481641e000f8f2fd6
"""
from hashlib import *

CONSTS = [0xC,0xC1,0x75,0xB9,0xC0,0xF1,0xB6,0xA8,0x31,0xC3,0x99,0xE2,0x69,0x77,0x26,0x61,0xF0,0x35,0x7A,0x3F,0x15,0x4B,0xC2,0xFF,0xE2,0xBF,0xF5,0x50,0x55,0x45,0x70,0x68,0x84,0xB8,0x7C,0x17,0x12,0xE7,0x22,7,0xF9,0x84,0xE3,0x42,0x2A,0x11,0x41,0xDC,0xA8,0x6E,0x5B,0xF2,0x5C,8,0x92,2,0x2F,0x45,0xA6,0x6E,0x20,0x41,8,0xD6,9,0xA6,0x9D,0xFD,0x18,0xAA,0xBD,0x87,0x9F,0xED,0x72,0xB2,0x73,0xA1,0x9C,0x90,0x6A,0xAE,0x9A,0xE7,0x41,0xD9,0x57,0x9A,0x18,0x60,0x43,0x51,0xA9,0x76,0xA7,0xA4,0xAC,0xAD,0x2A,0xF3,0x7D,0x26,0x14,0x4A,8,0x4A,0xB3,0xD2,0x42,0xFC,0xE3,0x2E,0xE,0x30,0x70,0xFB,0x99,0xA7,0xCE,0x9E,3,0x4E,0x78,0x87,0x17,0x3B,0x56,0xEF,0x1C,0x68,0xDB,0xCE,0x35,0x9C,0xB4,0x11,0x25,0xEE,0xAE,7,0xA,0xE1,0x86,0xAF,0xBA,0x63,0xE1,0x49,0xD0,0x14,0xAD,4,0x13,0xFE,0x7D,0xDF,0x79,0xBC,0xCD,0x95,0xCA,0xC9,0xBA,0x45,0x9D,0x2E,0x2F,0x67,0xB8,0x1B,0xE5,0x61,0x4B,0x2F,0xDF,0x40,1,0xDB,0xD0,0xCC,0x1F,0x47,0x67,0x32,0x5F,0xF0,0x2F,0xB5,0x23,0x93,0x43,0xC5,0xBD,0xB0,0x31,0x2A,0xCB,0x81,0x17,0x5C,0xDD,0x40,0xCB,0x73,0xD9,0xF4,0xC0,0x91,0x76,0x49,0xD4,6,0x89,0xC7,0xE5,0xE6,0xA8,0xC7,0xE1,0x93,0xF3,0x1D,0x37,0x27,0xB4,0x3D,0xE7,0xAC,0x1E,0xCD,0xDB,5,0x53,0xA4,0x94,0xDF,0xB8,0x98,0x67,0xCE,0xCC,0x19,0xDC,0xF5,0xA9,0xD7,0x82,0xAD,0xE0,0xBA,0x85,0x94,0xB,0x39,0x64,0xB9,0x69,0xB4,0x62,0xC8,0x62,0x7B,0x56,0x91,0xF2,0xCE,0xCB,0x84,0,0x90,0x23,0xF8,0x62,0x21,0x25,0x35,0x33,0x4E,0x7B,0x14,0xB,0x76,0x10,0x49,0x6F,0x32,0x63,0xB6,0x9B,0xA,0xC0,0x76,0x2B,0x3A,0xAD,0x18,0xD6,4,0xF2,0x44,0xDA,0xDB,0xEC,0x9E,0xA8,0xF0,0x48,0x5A,0x4D,0x1F,0x45,0x99,0x4C,0x7B,0xB8,0x92,0x8E,0xDE,0xA,0x1D,0xDE,0xA6,0x72,0xC9,0xF3,0xB7,0xAC,0x7B,0xA4,0x22,0x78,0x45,0x39,0x1A,0x37,0x1C,0xEA,0x29,0xC,0xD2,0x6B,0x32,0x45,0xD6,0xE,0x18,0x38,0x46,0xA7,0xDE,0x17,0x60,0x44,0x5E,0x3F,0xE5,0xE5,0xC3,0x35,0xF0,0xA5,0x86,0xAE,0xE,0x30,0x38,0x19,0xF9,0x91,0x17,0xC0,0xF3,0x7E,0x6A,0x21,0x5F,0x86,0x58,0xE0,0x15,0xF5,0x68,0x60,9,0x9A,0x1B,0xF7,0xC4,0xD,0x41,0x98,0xF3,0xD6,0xD7,0xDE,0x28,0x29,0x8A,0x4F,0x7D,0x2E,6,0x46,0xEF,0x93,0x90,0x5F,0xCE,6,0xB9,0xBD,0xD,0x2C,0x8B,0x47,0xD4,0x55,0x70,0x45,0x6D,0x63,0xA1,0x7A,0x59,0x56,0x35,0xD5,0x75,0x4C,0xEA,0x8F,0xE7,0x71,0xB2,0x9F,0x16,0xFA,0x1C,0xB1,0x34,0xC3,0x68,0x65,0x49,0x36,0x1A,0x91,0x5D,0x10,0x91,0x14,0x3A,0x4E,0x6B,0xA2,0x46,0x20,0x72,0x16,0x68,0x87,0x4F,0x1B,0xDD,0x52,2,0x1D,0x1E,0x1A,0x9F,0x5C,0x1C,0x9C,0x46,0x68,0x9B,0x7A,0xB2,0xA4,0xE6,0x5B,0x45,0xA6,0x28,0xC4,0x8B,0xB9,0xA7,0xC,0xDB,0xF0,0x97,0xD1,0x13,0xB1,0xAC,0x91,0x62,9,0x8A,0xE,0x8A,0x13,0x3D,0x11,0xEE,0xF5,0xF6,0x46,0x3E,0xB6,0x70]
aim = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
CONSTS0 = [hex(i)[2:] for i in CONSTS]
CONSTS = ['0'*(2-len(i))+i for i in CONSTS0]
st = ''

for i in range(32):
	has_ = CONSTS[i*16:i*16+16]
	has_ = ''.join(has_)
	for j in aim:
		m5 = md5()
		m5.update(st+j)
		if m5.hexdigest() == has_:
			st = st + j
			break
print st