from Bio.PDB import *
import nglview as nv
from rdkit import Chem

# https://www.tutorialspoint.com/biopython/biopython_pdb_module.htm

pdbl = PDBList() 

# # Getting pdb file
# pdbl.retrieve_pdb_file('2FAT', pdir = '.', file_format = 'pdb')
# pdb_parser = PDBParser(QUIET = True)
# # Modeling pdb file 
# data = pdb_parser.get_structure("2FAT", "2FAT.pdb")
# view = nv.show_biopython(data)
# view

# Getting mmCif file
pdbl.retrieve_pdb_file('2FAT', pdir = 'C:/Users/User/Desktop', file_format = 'mmCif')
# Modeling cif file
parser = MMCIFParser(QUIET = True) 
data = parser.get_structure("2FAT", "Data/2fat.cif")
view = nv.show_biopython(data)
view



     