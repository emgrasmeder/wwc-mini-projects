from pyroman import converter  # assumes pyroman is added to PYTHONPATH
from unittest import TestCase

class Test_A_Couple_Basic_Known_Cases(TestCase):
    def test_one_through_five(self):
        # Note: These tests will fail because main() doesn't return *anything*
        self.assertEqual(converter.main(1), "I")
        self.assertEqual(converter.main(2), "II")
        self.assertEqual(converter.main(3), "III")
        self.assertEqual(converter.main(4), "IV")
        self.assertEqual(converter.main(5), "V")

if __name__ == "__main__":
    from unittest import main
    main()
