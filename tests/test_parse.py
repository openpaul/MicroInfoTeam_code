import os
import random
import string
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
        
        fake_name = "".join(random.sample(string.punctuation + string.ascii_uppercase + string.digits, 15))
        header = ">" + fake_name + " # 135 # 938 # -1 # ID=1_2;" + \
                 "partial=00;start_type=ATG;rbs_motif=AGGA;rbs_spacer=5-10bp;gc_cont=0.415"
        
        faa = faafile(faa_single)

        result = faa._parse([header])

        assert result.name == fake_name
        assert result.start == 135
        assert result.end == 938
        assert result.strand == -1
        assert result.metadata == {
            "ID": "1_2",
            "partial": "00",
            "start_type": "ATG",
            "rbs_motif": "AGGA",
            "rbs_spacer": "5-10bp",
            "gc_cont": "0.415"
        }
    
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
