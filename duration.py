#!/usr/bin/env python3

import re

class Duration:
    def __init__(self, coded: str):
        duration, scale = re.match(r'(\d*\.?\d*)\s*(\w+)', coded.strip()).groups()
        self._seconds = float(duration) * Duration.scale_code(scale)

    @property
    def seconds(self) -> float:
        return self._seconds

    @property
    def minutes(self) -> float:
        return self.seconds / 60
    
    @property
    def hours(self) -> float:
        return self.minutes / 60

    @property
    def days(self) -> float:
        return self.hours / 24

    @property
    def years(self) -> float:
        return self.days / 365.25

    @classmethod
    def scale_code(cls, code: str):
        seconds = 1.0
        if code in Duration.split_code_word('seconds'):
            return seconds

        minutes = seconds * 60
        if code in Duration.split_code_word('minutes'):
            return minutes

        hours = minutes * 60
        if code in Duration.split_code_word('hours'):
            return hours

        days = hours * 24
        if code in Duration.split_code_word('days'):
            return days

        years = days * 365.25
        if code in Duration.split_code_word('years'):
            return years

        decades = years * 10
        if code in Duration.split_code_word('decades'):
            return decades

        centuries = decades * 10
        if code in Duration.split_code_word('centuries'):
            return centuries

        millennium = centuries * 10
        if code in Duration.split_code_word('millennium'):
            return millennium
        
        raise 'Invalid duration code!'

    @classmethod
    def split_code_word(cls, code: str):
        passes = []
        while len(code) > 0:
            passes.append(code)
            code = code[0:-1]

        return passes
