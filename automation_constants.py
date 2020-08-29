import enum

class WorkingStatus(enum.Enum): 
    OnLeave = 2
    WorkFromHome = 3
    WorkFromOffice = 4
    
class AarogyaSetuStatus(enum.Enum): 
    Safe = 2
    Unsafe = 3

class NetworkConnectionType(enum.Enum): 
    Broadband = 2
    DialUp = 3