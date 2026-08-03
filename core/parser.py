"""
EDITH RECON
Target Parser
Version: 1.1.0
"""

from urllib.parse import urlparse

from core.target import Target

class TargetParser:

    def parse(self, user_input: str) -> Target:

        target = Target()

        user_input = user_input.strip()

        target.original = user_input

        parsed = urlparse(user_input)

        return target