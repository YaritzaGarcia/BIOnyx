from Bio.PDB import *
from Bio.PDB.MMCIF2Dict import *
import nglview as nv
from texttable import Texttable
import sys, os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

# Print bold
start = "\033[1m"
end = "\033[0;0m"

# # https://www.tutorialspoint.com/biopython/biopython_pdb_module.htm

def infoID(ID):
    idPdb = PDBList()
    idPdb.retrieve_pdb_file(ID, pdir='.', file_format='mmCif')
    fileName = ID + ".cif"
    # mmcif_dict = MMCIF2Dict(fileName)
    mmcif_Parser = MMCIFParser(QUIET=True)
    idStructure = mmcif_Parser.get_structure(ID, fileName.lower())
    # for idModel in idStructure:
    #     for residue in idModel.get_residues():
    #         print(residue)
    residues = idStructure.get_residues() # returns a generator object
    [print(item) for item in residues]

# infoID("1atp")

def model(ID):
    # Searching for the pdb file
    pdbServer = PDBList()
    pdbServer.retrieve_pdb_file(ID, pdir='.', file_format='mmCif')

    # Getting the protein structure
    mmcif_Parser = MMCIFParser(QUIET=True)
    fileName = ID + ".cif"
    idStructure = mmcif_Parser.get_structure(ID, fileName.lower())
    
    for model in idStructure:
        for chain in model:
            print('%s - Chain: %s. Number of residues: %d. Number of atoms: %d.')

    # # Modeling the protein structure
    # idModel = nv.show_biopython(idStructure)
    # return(idModel)

# model("2FAT")

def getFile(ID, path):
    # Searching for the pdb file
    pdbServer = PDBList()
    pdbServer.retrieve_pdb_file(ID, pdir=path, file_format='mmCif')
    return("The file has been saved in " + path)

def getPolypeptides(ID):

    # Creating rows for the Polypeptide table
    polypeptidesRows = [
        ["Polypeptide Number", "Polypeptide Sequence", "Sequence Length"]]

    # Searching for the pdb file
    blockPrint()
    getFile(ID, '.')
    enablePrint()

    # Getting the protein structure
    mmcif_Parser = MMCIFParser(QUIET=True)
    fileName = ID + ".cif"
    idStructure = mmcif_Parser.get_structure(ID, fileName.lower())

    # Getting Polypeptide information
    builder = PPBuilder()
    polypeptideNum = 1
    for polypeptide in builder.build_peptides(idStructure):
        seq = polypeptide.get_sequence()
        polypeptidesRows.append([polypeptideNum, seq, len(seq)])
        polypeptideNum += 1

    # Creating and printing the table
    polypeptidesTable = Texttable()
    polypeptidesTable.add_rows(polypeptidesRows)
    polypeptidesTable.set_cols_align(['c', 'c', 'c'])
    print("This table contains all the polypeptides of the protein " + start + ID + end)
    print(polypeptidesTable.draw())

# getPolypeptides("2FAT")


def getAminoAcids(ID):
    aminoAcidsTable = Texttable()
    aminoAcidsTable.add_rows(
        [
            ["No.", "Name", "Grade", "Age"],
            [1, "Bob", 6, 11],
            [2, "Freddy", 4, 10],
            [3, "John", 7, 13],
        ]
    )
    aminoAcidsTable.set_cols_align(['c', 'c', 'c', 'c'])
    print(aminoAcidsTable.draw())

# getAminoAcids("1atp")