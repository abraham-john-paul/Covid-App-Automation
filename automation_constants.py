import enum
    
class AarogyaSetuStatus(enum.Enum): 
    Safe = 2
    UnSafe = 3

class NetworkConnectionType(enum.Enum): 
    Broadband = 2
    DialUp = 3
    MobileData = 4
