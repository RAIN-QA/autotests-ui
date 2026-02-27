from enum import Enum

class AllureEpics(str, Enum):
    LMS = "LMS system"
    STUDENT = "Student system"
    ADMINISTRATOR = "Administrator system"