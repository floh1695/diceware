#!/usr/bin/env python3

import re

class Duration:
    def __init__(self, coded: str):
        duration, scale = re.match(r'(\d+)\s*(\w+)', coded.strip()).groups()
        self._seconds = int(duration) * Duration.scale_code(scale)

    @property
    def seconds(self):
        return self._seconds

    @classmethod
    def scale_code(cls, code: str):
        seconds = 1.0
        minutes = seconds * 60
        hours = minutes * 60
        days = hours * 24
        years = days * 365.25
        decades = years * 10
        centuries = decades * 10
        millennium = centuries * 10

        if code in Duration.split_code_word('seconds'):
            return seconds
        elif code in Duration.split_code_word('minutes'):
            return minutes
        elif code in Duration.split_code_word('hours'):
            return hours
        elif code in Duration.split_code_word('days'):
            return days
        elif code in Duration.split_code_word('years'):
            return years
        elif code in Duration.split_code_word('decades'):
            return decades
        elif code in Duration.split_code_word('centuries'):
            return centuries
        elif code in Duration.split_code_word('millennium'):
            return millennium

    @classmethod
    def split_code_word(cls, code: str):
        passes = []
        while len(code) > 0:
            passes.append(code)
            code = code[0:-1]

        return passes
