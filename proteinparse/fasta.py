#!/usr/bin/env python3
from pathlib import Path
import re


class faafile:
    """
    class to open faa file from disk. Exposes looping and maybe random acces
    to sequences
    """

    def __init__(self, path):
        # openfile
        self._path = Path(path)
        #self._open(_path)
        #return

    def __iter__(self):
        # check if file is there
        if not self._path.exists():
            # throw error
            raise OSError("File not found")

        # > header
        # sequence

        # if its there open it and loop it
        with open(self._path) as fin:  # file input
            lines = []
            for line in fin:
                line = line.strip()
                # each line
                if line.startswith(">") and len(lines) > 0:
                    # new sequence
                    yield self._parse(lines)
                    # reset lines tracker
                    lines = []
                # add new lines
                lines.append(line)
            yield self._parse(lines)

    def _parse(self, lines):
        header = lines[0]
        sequence = "".join(lines[1:])

        # >ERZ1039804.275493-NODE-275493-length-500-cov-0.829213_226_498_+
        rgs_regex = re.compile(r"^\>(?P<name>.*)_(?P<start>\d+)_(?P<end>\d+)_(?P<strand>[\-\+])$")

        m = rgs_regex.match(header)
        if m:
            # this is a FGS
            seq_name = m.group("name")
            start = m.group("start")
            end = m.group("end")
            # translate strand information to be homogenous (adapt prodigal format): +=1 -=-1
            strand = str(int(m.group("strand") + "1"))
            genecaller = "FGS"
            fields = {}

        else:
            # prodigal
            # >ERZ1039804.100005-NODE-100005-length-950-cov-2.344134_1 # 3 # 902 # 1 # ID=5_1;partial=10;start_type=Edge;rbs_motif=None;rbs_spacer=None;gc_cont=0.564
            column_char = " # "
            *_, start, end, strand, metadata = header.split(column_char)

            seq_name = column_char.join(_)[1:]
            genecaller = "Prodigal"
            fields = {}
            for field in metadata.split(";"):
                # name=value
                key, value = field.split("=")
                fields[key] = value

        # return a sequence object
        return Sequence(seq_name, sequence, start, end, strand, genecaller, fields)


class Sequence:
    """
    Sequence object. Gives access to properties of sequences
    """

    def __init__(self, name, sequence, start, end, strand, genecaller, metadata=None):
        self.name = name
        self.sequence = sequence
        self.start = int(start)
        self.end = int(end)
        self.strand = int(strand)
        self.genecaller = genecaller
        if metadata is None:
            self.metadata = {}
        else:
            self.metadata = metadata

    def __str__(self):
        """
        define what happens if this is printed
        """
        return ">{}\n{}".format(self.name, self.sequence)
