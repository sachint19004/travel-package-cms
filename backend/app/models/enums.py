from enum import Enum


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    EDITOR = "EDITOR"
    CONSULTANT = "CONSULTANT"


class PackageStatus(str, Enum):
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"


class EnquiryStatus(str, Enum):
    NEW = "NEW"
    ASSIGNED = "ASSIGNED"
    REPLIED = "REPLIED"
    CLOSED = "CLOSED"