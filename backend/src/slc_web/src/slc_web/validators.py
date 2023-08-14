from slc_web import _
from z3c.form.validator import SimpleFieldValidator
from zope.interface import Invalid

import re


# email re w/o leading '^'
EMAIL_RE = r"([0-9a-zA-Z_&.'+-]+!)*[0-9a-zA-Z_&.'+-]+@(([0-9a-zA-Z]([0-9a-zA-Z-]*[0-9a-z-A-Z])?\.)+[a-zA-Z]{2,}|([0-9]{1,3}\.){3}[0-9]{1,3})$"  # noqa


class isEmail(SimpleFieldValidator):
    """An Email Field Validator

    Args:
        SimpleFieldValidator (class): Simple Field Validator Class
    """

    def validate(self, value):
        """A validation for Email link.

        Args:
            value (str): Email link string

        Raises:
            Invalid: Show an invalid message
        """
        super().validate(value)
        prog = re.compile("^" + EMAIL_RE)
        result = prog.match(value)
        if result is None:
            raise Invalid(_("is not a valid email address."))


class isHTTP(SimpleFieldValidator):
    """An URL Field Validator

    Args:
        SimpleFieldValidator (class): Simple Field Validator Class
    """

    def validate(self, value):
        """A validation for Website link.

        Args:
            value (str): Website URL string

        Raises:
            Invalid: Show an invalid message
        """
        super().validate(value)
        if value is None or value.strip() == "":
            return
        if not value.startswith("http://") and not value.startswith("https://"):
            raise Invalid(_("web address must start with http:// or https://"))


class isImage(SimpleFieldValidator):
    """An Image Field Validator

    Args:
        SimpleFieldValidator (class): Simple Field Validator Class
    """

    def validate(self, value):
        """We make sure the file type are jpg, jpeg and png.

        Args:
            value (str): Image file

        Raises:
            Invalid: Show an invalid message
        """
        super().validate(value)
        # TODO: Implement the Image Field Validator


class isPhone(SimpleFieldValidator):
    """A z3c.form validator class for international phone numbers

    Args:
        SimpleFieldValidator (class): Simple Field Validator Class
    """

    def validate(self, value):
        """Validate international phone number on input.

        Args:
            value (str): Phone string

        Raises:
            Invalid: Show an invalid message
        """
        super().validate(value)

        allowed_characters = "+- () / 0123456789"

        if value is not None:

            value = value.strip()

            if value == "":
                # Assume empty string = no input
                raise Invalid(_("Phone number string is empty"))

            # The value is not required
            for c in value:
                if c not in allowed_characters:
                    raise Invalid(_("Phone number contains bad characters"))

            if len(value) < 7:
                raise Invalid(_("Phone number is too short"))
