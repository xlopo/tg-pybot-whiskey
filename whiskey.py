from telex.plugin import TelexPlugin

class WhiskeyPlugin(TelexPlugin):
    patterns = [
        '^!whiskey'
    ]

    usage = [
        "!whiskey"
    ]

    def run(self, msg, matches):
        return "Pass the whiskey."

