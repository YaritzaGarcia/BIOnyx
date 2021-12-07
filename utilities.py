from typing import Sequence
from Bio.PDB import *
from Bio.PDB.MMCIF2Dict import *
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import nglview as nv
from texttable import Texttable
import sys
import os

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
    blockPrint()
    pdbServer.retrieve_pdb_file(ID, pdir=path, file_format='mmCif')
    enablePrint()
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
    tableRows = [["Polypeptide Number",
                  "Amino Acid Information in the Polypeptide"]]

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
            aminoRows.append([key, aminoCount[key], str(
                aminoPercent[key] * 100)[0:4] + " %"])
            resultDict[polypeptideNum][key] = {}
            resultDict[polypeptideNum][key]["Amount"] = aminoCount[key]
            resultDict[polypeptideNum][key]["Percentage"] = str(
                aminoPercent[key] * 100)[0:4]

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
def getResidues(ID):
    pdb = PDBList()
    enablePrint()
    pdb.retrieve_pdb_file(ID, pdir='.', file_format='mmCif')
    fileName = ID + ".cif"
    mmcif_Parser = MMCIFParser(QUIET=True)
    structure = mmcif_Parser.get_structure(ID, fileName.lower())
    enablePrint()
    for model in structure:
        for residue in model.get_residues():
            print(residue)
# MW = molecular weight
# This functions returns an array of tuples that contains the sequence and its molecular weight
# for the given protein


def MolecularWeight(ID, method):
    # Acces the Data bank and gather the protein structure
    # Searching for the pdb file

    blockPrint()
    getFile(ID, '.')
    enablePrint()
    mwRows = [["Sequence Number", "Sequence", "Molecular Weight"]]

    mmcif_Parser = MMCIFParser(QUIET=True)
    fileName = ID + ".cif"
    structure = mmcif_Parser.get_structure(ID, fileName.lower())

    polypeptide_builder = CaPPBuilder()
    count = 1

    for polypeptide in polypeptide_builder.build_peptides(structure):
        seq = polypeptide.get_sequence()
        analyzed_seq = ProteinAnalysis(str(seq))
        mwRows.append([count, seq, analyzed_seq.molecular_weight()])
        # print(analyzed_seq.count_amino_acids())
        count += 1
    # Creating a table
    mwTable = Texttable()
    mwTable.add_rows(mwRows)
    mwTable.set_cols_align(['c', 'c', 'c'])
    print(mwTable.draw())