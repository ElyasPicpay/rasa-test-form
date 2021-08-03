import re
from typing import Dict, List

from rasa_sdk import Tracker
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher


class ValidateExemploForm(FormValidationAction):
    def name(self) -> str:
        return "validate_exemplo_form"

    def validate_email(
        self,
        value: str,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[str, dict],
    ) -> List[Dict[str, dict]]:
        """Validate email value."""
        regex = r"[^ @]+@[^ @]+\.[^ @]+"
        if not re.match(regex, value):
            dispatcher.utter_message(template="utter_wrong_email")
            value = None

        return {"email": value}
