#!/usr/bin/env python3

from typing import Callable
from enum import Enum

from termcolor import colored

LogOperation = Callable[['LogLevel', list[str]], None]

class LogLevel(Enum):
    Error = 2
    Warn = 1
    Info = 0
    Debug = -1
    Trace = -2

    @classmethod
    def from_value(cls, value: int) -> 'LogLevel':
        lower = LogLevel.Trace
        upper = LogLevel.Error
        value = min(upper.value, max(value, lower.value))
        for member in cls:
            if member.value == value:
                return member
            
        raise ValueError("Value '{ value }' not valid for LogLevel")
    
    @classmethod
    def logger(cls, cutoff: 'LogLevel', wrap: Callable[[str], None] = print) -> Callable[['LogLevel', list[str]], None]:
        def log(level: LogLevel, *messages: list[str]):
            if level.value < cutoff.value:
                return
            
            color = LogLevel.colorer(level)
            message = color(' '.join(map(str, messages)))

            wrap(message)

        return log

    @classmethod
    def color(cls, level: 'LogLevel') -> str:
        if level == LogLevel.Error:
            return 'red'
        elif level == LogLevel.Warn:
            return 'yellow'
        elif level == LogLevel.Info:
            return 'white'
        elif level == LogLevel.Debug:
            return 'magenta'
        elif level == LogLevel.Trace:
            return 'cyan'
        else:
            raise 'Unregistered LogLevel'

    @classmethod
    def colorer(cls, level: 'LogLevel') -> str:
        color = LogLevel.color(level)

        def color_text(message: str):
            return colored(message, color)

        return color_text
