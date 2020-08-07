import os
import random
# import string
from proteinparse.fasta import faafile

faa_mixed = os.path.join(os.path.dirname(__file__), "test_files/test_mixed.faa")
faa_single = os.path.join(os.path.dirname(__file__), "test_files/single.faa")


class Test_faaparse:
    
    def test_single_sequence(self):
        # open fasta
        faa = faafile(faa_single)
        # check that the first sequence name is:
        expected_name = "ERZ1039804.100001-NODE-100001-length-950-cov-2.385475_2"
        for rec in faa:
            assert rec.name == expected_name
            break
    
    def test_random_seq_name(self):
        """Test a random header fasta name
        """
        
        #fake_string = ''.join(random.sample(string.letters, 15))
        
        pass
    
    def test_mixed_values(self):
        expected_values = [
                        {"name": "ERZ1039804.100001-NODE-100001-length-950-cov-2.385475_1",
                        "start" : 1,
                        "end": 132},
                        {"name": "ERZ1039804.100001-NODE-100001-length-950-cov-2.385475_2",
                        "start": 135,
                        "end": 938,
                        "strand": -1,
                        "sequence": "MRIKLNCIFLFLILICSGQNSHAQFEIPPIPKTQTSVYDYIGVLAPNESKALEQKLIRYADSTSTQIVLATINSTEGEYINYLATNWAQSWGIGQDKKDNGVFILLAKNDRKINISTGYGVEHLLTDKMCSRIIQEHFIPSFKKNKYAEGLNAGADAIFEVLTGAYKASPKQKTSEVPFGLILFLLVIFIIFVAALSKRANGKNKGNRAPPTSLLDAIILSNMGRGNYRKSKSTGGLFGGTGSFGGGGFGGGFGGGGFGGGGASGGW"},
                        {"name": "ERZ1039804.275493-NODE-275493-length-500-cov-0.829213",
                        "genecaller": "FGS",
                        "sequence": "MCACIPIYMPAEACRIHVQPFLFLHRHAHRQRHRAVHRHMRRHVCRNVCTCERPFQAAGPSRAMTARTASVQTCVQTWRAARLYIGIADGN"}
                        ]
                        
        faa = faafile(faa_mixed)
        for faa_entry, expected in zip(faa, expected_values):
            for key, value in expected.items():
                assert getattr(faa_entry, key) == value
