from telex.plugin import TelexPlugin

class WhiskeyPlugin(TelexPlugin):
    """
    Pass the whiskey.
    """

    patterns = {
        "^!whiskey": 'run'
    }

    usage = [
        "!whiskey"
    ]

    def run(self, msg, matches):
        return "Pass the whiskey."

