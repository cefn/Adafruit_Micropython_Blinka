import unittest
import agnostic

class TestMicrocontrollerModule(unittest.TestCase):

    def test_pins_exist(self):
        """The microcontroller module should contain pin references"""
        import microcontroller
        import microcontroller.pin as pin
        from testing.platform import pin_count
        entries = [getattr(pin, key) for key in dir(pin)]
        # is this filter line needed? any other types valid in pin module?
        entries = list(filter(lambda val: type(val) is microcontroller.Pin, entries))
        self.assertTrue(len(entries) > 0)
        self.assertTrue(len(entries) == pin_count)