from enum import Enum


class IngestionStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"


class CodeDescriptionEnum(Enum):
    def __init__(self, code: int, description: str):
        self.code = code
        self.description = description

    @classmethod
    def from_code(cls, code: int):
        for item in cls:
            if item.code == code:
                return item
        return None

class TaxiVendor(CodeDescriptionEnum):
    CREATIVE_MOBILE_TECHNOLOGIES = (1, "Creative Mobile Technologies, LLC")
    CURB_MOBILITY = (2, "Curb Mobility, LLC")
    MYLE_TECHNOLOGIES = (6, "Myle Technologies Inc")
    HELIX = (7, "Helix")


class RateCode(CodeDescriptionEnum):
    STANDARD_RATE = (1, "Standard rate")
    JFK = (2, "JFK")
    NEWARK = (3, "Newark")
    NASSAU_OR_WESTCHESTER = (4, "Nassau or Westchester")
    NEGOTIATED_FARE = (5, "Negotiated fare")
    GROUP_RIDE = (6, "Group ride")
    NULL_UNKNOWN = (99, "Null/unknown")


class PaymentType(CodeDescriptionEnum):
    FLEX_FARE_TRIP = (0, "Flex Fare trip")
    CREDIT_CARD = (1, "Credit card")
    CASH = (2, "Cash")
    NO_CHARGE = (3, "No charge")
    DISPUTE = (4, "Dispute")
    UNKNOWN = (5, "Unknown")
    VOIDED_TRIP = (6, "Voided trip")