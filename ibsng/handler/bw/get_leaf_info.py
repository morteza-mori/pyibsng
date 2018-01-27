"""Get leaf info API method."""
from ibsng.handler.handler import Handler


class getLeafInfo(Handler):
    """Get leaf info class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.leaf_name, str)

    def setup(self, leaf_name):
        """Setup required parameters.

        :param str leaf_name: leaf name

        :return: None
        :rtype: None
        """
        self.leaf_name = leaf_name