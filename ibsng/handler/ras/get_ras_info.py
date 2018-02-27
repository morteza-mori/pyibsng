"""Get ras info API method."""
from ibsng.handler.handler import Handler


class getRasInfo(Handler):
    """Get ras info method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.ras_ip, int)
        self.is_valid_content(self.ras_ip, self.IP_PATTERN)

    def setup(self, ras_ip):
        """Setup required parameters.

        :param str ras_ip: ras ip address

        :return: None
        :rtype: None
        """
        self.ras_ip = ras_ip
