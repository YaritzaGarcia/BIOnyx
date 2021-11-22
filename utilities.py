from typing import Sequence
from Bio.PDB import *
from Bio.PDB.MMCIF2Dict import *
from Bio.SeqUtils.ProtParam import ProteinAnalysis
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

# https://www.tutorialspoint.com/biopython/biopython_pdb_module.htm

# Methods that are working
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

def getAminoAcidsInfo(ID):
    resultDict = {}
    tableRows = [["Polypeptide Number", "Amino Acid Information in the Polypeptide"]]

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
        resultDict[polypeptideNum] = {}
        pSequence = polypeptide.get_sequence()
        pAnalysis = ProteinAnalysis(str(pSequence))
        aminoRows = [['Amino Acid', 'Amount', 'Percentage']]
        aminoCount = pAnalysis.count_amino_acids()
        aminoPercent = pAnalysis.get_amino_acids_percent()
        for key in aminoCount:
            aminoRows.append([key, aminoCount[key], str(aminoPercent[key] * 100)[0:4] + " %"])
            resultDict[polypeptideNum][key] = {}
            resultDict[polypeptideNum][key]["Amount"] = aminoCount[key]
            resultDict[polypeptideNum][key]["Percentage"] = str(aminoPercent[key] * 100)[0:4]

        aminoAcidsTable = Texttable()
        aminoAcidsTable.add_rows(aminoRows)
        aminoAcidsTable.set_cols_align(['c', 'c', 'c'])
        tableRows.append([polypeptideNum, aminoAcidsTable.draw()])
        polypeptideNum += 1
    
    table = Texttable()
    table.add_rows(tableRows)
    table.set_cols_align(['c', 'c'])
    print(table.draw())
    return resultDict

# Methods in process
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