from Bio.PDB import *
import nglview as nv
import ipywidgets as widget


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
    parser = PDBParser(QUIET=True)
    fileName = ID + ".cif"
    return parser.get_structure(ID, fileName.lower()).get_full_id


# print(infoID("6VOY"))

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
