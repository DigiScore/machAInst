# -*- coding: utf-8 -*-

# Headers
FILE_HEADER = b"MThd"
TRACK_HEADER = b"MTrk"

# MIDI Channel Events
NOTE_OFF = 0x08
NOTE_ON = 0x09
NOTE_AFTERTOUCH = 0x0A
CONTROLLER = 0x0B
PROGRAM_CHANGE = 0x0C
CHANNEL_AFTERTOUCH = 0x0D
PITCH_BEND = 0x0E
META_EVENT = b"\xff"

# MIDI Controller Type
BANK_SELECT = 0x00
MODULATION = 0x01
BREATH_CONTROLLER = 0x02
FOOT_CONTROLLER = 0x04
PORTAMENTO_TIME = 0x05
DATA_ENTRY_MSB = 0x06
MAIN_VOLUME = 0x07
BALANCE = 0x08
PAN = 0x0A
EXPRESSION_CONTROLLER = 0x0B
EFFECT_CONTROL_1 = 0x0C
EFFECT_CONTROL_2 = 0x0D

# Meta Events
SEQUENCE_NUMBER = b"\x00"
TEXT_EVENT = b"\x01"
COPYRIGHT_NOTICE = b"\x02"
TRACK_NAME = b"\x03"
INSTRUMENT_NAME = b"\x04"
LYRICS = b"\x05"
MARKER = b"\x06"
CUE_POINT = b"\x07"
MIDI_CHANNEL_PREFIX = b"\x20"
END_OF_TRACK = b"\x2F"
SET_TEMPO = b"\x51"
SMPTE_OFFSET = b"\x54"
TIME_SIGNATURE = b"\x58"
KEY_SIGNATURE = b"\x59"
