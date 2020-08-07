import unittest
import os
from proteinparse import faafile

faa_mixed = os.path.join(os.path.dirname(__file__), "test_files/multiline.fasta")
faa_single = os.path.join(os.path.dirname(__file__), "test_files/single.faa")


class Test_faaparse(unittest.TestCase):
    def test_single_sequence(self):
        # open fasta
        faa = faafile(faa_single)
        # check that the first sequence name is:
        expected_name = "ERZ1039804.100001-NODE-100001-length-950-cov-2.385475_2"
        for rec in faa:
            self.assertEqual(rec.name, expected_name)
            break
