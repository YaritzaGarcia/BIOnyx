
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA DICTIONARY DIVIDE EQUALS FINISHER FINVOCATION GETAMINOACIDSINFO GETFILE GETPOLYPEPTIDES IDENTIFIER MINUS MOLECULARWEIGHT NUMBER PLUS STRING TIMESstatement : IDENTIFIER EQUALS expressionstatement : expressionexpression : IDENTIFIERexpression : expression PLUS expressionexpression : expression MINUS expressionexpression : expression TIMES expressionexpression : expression DIVIDE expressionexpression : NUMBERexpression : STRINGexpression : DICTIONARYexpression : GETFILE FINVOCATION STRING COMMA STRING FINISHERexpression : GETPOLYPEPTIDES FINVOCATION STRING FINISHERexpression : GETAMINOACIDSINFO FINVOCATION STRING FINISHERexpression : MOLECULARWEIGHT FINVOCATION STRING FINISHER'
    
_lr_action_items = {'IDENTIFIER':([0,11,12,13,14,15,],[2,20,20,20,20,20,]),'NUMBER':([0,11,12,13,14,15,],[4,4,4,4,4,4,]),'STRING':([0,11,12,13,14,15,16,17,18,19,30,],[5,5,5,5,5,5,26,27,28,29,34,]),'DICTIONARY':([0,11,12,13,14,15,],[6,6,6,6,6,6,]),'GETFILE':([0,11,12,13,14,15,],[7,7,7,7,7,7,]),'GETPOLYPEPTIDES':([0,11,12,13,14,15,],[8,8,8,8,8,8,]),'GETAMINOACIDSINFO':([0,11,12,13,14,15,],[9,9,9,9,9,9,]),'MOLECULARWEIGHT':([0,11,12,13,14,15,],[10,10,10,10,10,10,]),'$end':([1,2,3,4,5,6,20,21,22,23,24,25,31,32,33,35,],[0,-3,-2,-8,-9,-10,-3,-1,-4,-5,-6,-7,-12,-13,-14,-11,]),'EQUALS':([2,],[11,]),'PLUS':([2,3,4,5,6,20,21,22,23,24,25,31,32,33,35,],[-3,12,-8,-9,-10,-3,12,12,12,12,12,-12,-13,-14,-11,]),'MINUS':([2,3,4,5,6,20,21,22,23,24,25,31,32,33,35,],[-3,13,-8,-9,-10,-3,13,13,13,13,13,-12,-13,-14,-11,]),'TIMES':([2,3,4,5,6,20,21,22,23,24,25,31,32,33,35,],[-3,14,-8,-9,-10,-3,14,14,14,14,14,-12,-13,-14,-11,]),'DIVIDE':([2,3,4,5,6,20,21,22,23,24,25,31,32,33,35,],[-3,15,-8,-9,-10,-3,15,15,15,15,15,-12,-13,-14,-11,]),'FINVOCATION':([7,8,9,10,],[16,17,18,19,]),'COMMA':([26,],[30,]),'FINISHER':([27,28,29,34,],[31,32,33,35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,11,12,13,14,15,],[3,21,22,23,24,25,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> IDENTIFIER EQUALS expression','statement',3,'p_statement_identifier','parser.py',10),
  ('statement -> expression','statement',1,'p_statement_expr','parser.py',15),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','parser.py',20),
  ('expression -> expression PLUS expression','expression',3,'p_expression_plus','parser.py',28),
  ('expression -> expression MINUS expression','expression',3,'p_expression_minus','parser.py',33),
  ('expression -> expression TIMES expression','expression',3,'p_expression_times','parser.py',38),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_divide','parser.py',43),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',48),
  ('expression -> STRING','expression',1,'p_expression_string','parser.py',53),
  ('expression -> DICTIONARY','expression',1,'p_expression_dictionary','parser.py',58),
  ('expression -> GETFILE FINVOCATION STRING COMMA STRING FINISHER','expression',6,'p_expression_getFile','parser.py',63),
  ('expression -> GETPOLYPEPTIDES FINVOCATION STRING FINISHER','expression',4,'p_expression_getPolypeptides','parser.py',69),
  ('expression -> GETAMINOACIDSINFO FINVOCATION STRING FINISHER','expression',4,'p_expression_getAminoAcidsInfo','parser.py',75),
  ('expression -> MOLECULARWEIGHT FINVOCATION STRING FINISHER','expression',4,'p_expression_MolecularWeight','parser.py',81),
]
