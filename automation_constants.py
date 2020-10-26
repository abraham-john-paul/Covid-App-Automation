import enum

class WorkingStatus(enum.Enum): 
    OnLeave = 1
    WorkFromHome = 2
    WorkFromOffice = 3
    BusinessTrip = 4
    WeekendsOrHolidays = 5
    
class AarogyaSetuStatus(enum.Enum): 
    Safe = 2
    Unsafe = 3

class NetworkConnectionType(enum.Enum): 
    Broadband = 2
    DialUp = 3
    MobileData = 4
