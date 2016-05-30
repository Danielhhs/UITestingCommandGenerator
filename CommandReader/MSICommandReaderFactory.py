__author__ = 'huanghongsen'

from CommandReader.MSICommandReader import MSICommandReader
from CommandReader.MSIMonkeyTalkCommandReader import MSIMonkeyTalkCommandReader
from CommandReader.MSIInputCommandReader import MSIInputCommandReader

class MSICommandReaderFactory:
    @staticmethod
    def commandReaderForName(name):
        if name == 'MonkeyTalk':
            return MSIMonkeyTalkCommandReader()
        elif name == 'Input':
            return MSIInputCommandReader()