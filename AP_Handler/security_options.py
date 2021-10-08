"""
This file consists of all the possible security settings for APs. I did this because we don't want to be throwing
strings around classes, this is a much more cleaner and maintainable way.
"""


class SecurityOptions:
    class WPA:
        def __init__(self):
            raise NotImplementedError()

    class WPA2:
        def __int__(self, key: "", pmf: False):
            self.key = key
            self.pmf = pmf

    class WPA3:
        def __init__(self):
            raise NotImplementedError()

    class WPA2Enterprise:
        def __init__(self):
            raise NotImplementedError()

    class Open:
        def __init__(self):
            raise NotImplementedError()

    class WPA3Enterprise:
        def __init__(self):
            raise NotImplementedError()

    class WPA2WPA3MixedMode:
        def __init__(self):
            raise NotImplementedError()
