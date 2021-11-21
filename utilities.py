from Bio.PDB import *
from Bio.PDB import MMCIF2Dict
import nglview as nv
import ipywidgets


# # https://www.tutorialspoint.com/biopython/biopython_pdb_module.htm

# pdbl = PDBList()

# # Getting pdb file
# pdbl.retrieve_pdb_file('2FAT', pdir = '.', file_format = 'pdb')
# pdb_parser = PDBParser(QUIET = True)
# # Modeling pdb file
# data = pdb_parser.get_structure("2FAT", "2FAT.pdb")
# view = nv.show_biopython(data)
# view

# # Getting mmCif file
# pdbl.retrieve_pdb_file('2FAT', pdir='.', file_format='mmCif')
# # Modeling cif file
# parser = MMCIFParser(QUIET=True)
# data = parser.get_structure("2FAT", "2FAT.cif")
# view = nv.show_biopython(data)
# view


def infoID(ID):
    idPdb = PDBList()
    idPdb.retrieve_pdb_file(ID, pdir='.', file_format='mmCif')
    mmcif_Parser = MMCIFParser(QUIET=True)
    fileName = ID + ".cif"
# The fastest way to access protein structure information
# is through the header, a metadata dictionary,
# available in both PDB and CIF format.
    # structure = mmcif_Parser.get_structure(ID, fileName.lower())
    # _pdbx_entry_details.nonpolymer_details
    # _pdbx_struct_mod_residue.details
    # _pdbx_struct_mod_residue.details (funcion structural details )
    # _struct_biol.details (biological structural details )
    # _struct.title (name of the protein based on id function )
    # mmcif_dict = MMCIF2Dict.MMCIF2Dict(fileName.lower())
    # for k, v in mmcif_dict.items():
    #     print(k,v)
    idStructure = mmcif_Parser.get_structure(ID, fileName.lower())
    return Selection.unfold_entities(idStructure, "R")  # R is for residues
    # return len(mmcif_dict)  # 689


print(infoID("1fat"))


def model(ID):
    # Searching for the pdb file
    pdbServer = PDBList()
    pdbServer.retrieve_pdb_file(ID, pdir='.', file_format='mmCif')

    # Getting the protein structure
    mmcif_Parser = MMCIFParser(QUIET=True)
    fileName = ID + ".cif"
    idStructure = mmcif_Parser.get_structure(ID, fileName.lower())

    # Modeling the protein structure
    idModel = nv.show_biopython(idStructure)
    return(idModel)


# model("2FAT")


def getFile(ID, path):
    # Searching for the pdb file
    pdbServer = PDBList()
    pdbServer.retrieve_pdb_file(ID, pdir=path, file_format='mmCif')
    print("The file has been saved in " + path)
