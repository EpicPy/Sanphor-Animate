#Check for bin values

from . import patternDatabase

class DownloadError(BaseException):
    def __init__(self, msg) -> None:
        '''Download Failed Error'''
        super().__init__(msg)
try:
    if patternDatabase.animation==dict() or patternDatabase.static==dict():
        raise DownloadError('Download corrupted.Either animation or static default values are not installed properly. ')
except:
    raise DownloadError('Bin value(s) not found')