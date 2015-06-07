from telex.plugin import TelexPlugin

class WhiskeyPlugin(TelexPlugin):
    """
    Pass the whiskey.
    """

    patterns = [
        "^!whiskey(.*)"
    ]

    usage = [
        "!whiskey"
    ]

    def run(self, msg, matches):
        return "Pass the whiskey."

