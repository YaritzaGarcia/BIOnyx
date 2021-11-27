
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA DIVIDE FINISHER FINVOCATION GETAMINOACIDSINFO GETFILE GETPOLYPEPTIDES ID INFOID MINUS MODEL NUMBER PLUS STRING TIMESexpression : INFOID FINVOCATION STRING FINISHERexpression : MODEL FINVOCATION STRING FINISHERexpression : GETFILE FINVOCATION STRING COMMA STRING FINISHERexpression : GETPOLYPEPTIDES FINVOCATION STRING FINISHERexpression : GETAMINOACIDSINFO FINVOCATION STRING FINISHERexpression : NUMBER PLUS NUMBERexpression : NUMBER MINUS NUMBERexpression : NUMBER TIMES NUMBERexpression : NUMBER DIVIDE NUMBERexpression : ID'
    
_lr_action_items = {'INFOID':([0,],[2,]),'MODEL':([0,],[3,]),'GETFILE':([0,],[4,]),'GETPOLYPEPTIDES':([0,],[5,]),'GETAMINOACIDSINFO':([0,],[6,]),'NUMBER':([0,14,15,16,17,],[7,23,24,25,26,]),'ID':([0,],[8,]),'$end':([1,8,23,24,25,26,27,28,30,31,33,],[0,-10,-6,-7,-8,-9,-1,-2,-4,-5,-3,]),'FINVOCATION':([2,3,4,5,6,],[9,10,11,12,13,]),'PLUS':([7,],[14,]),'MINUS':([7,],[15,]),'TIMES':([7,],[16,]),'DIVIDE':([7,],[17,]),'STRING':([9,10,11,12,13,29,],[18,19,20,21,22,32,]),'FINISHER':([18,19,21,22,32,],[27,28,30,31,33,]),'COMMA':([20,],[29,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> INFOID FINVOCATION STRING FINISHER','expression',4,'p_expression_infoID','parser.py',6),
  ('expression -> MODEL FINVOCATION STRING FINISHER','expression',4,'p_expression_model','parser.py',11),
  ('expression -> GETFILE FINVOCATION STRING COMMA STRING FINISHER','expression',6,'p_expression_getFile','parser.py',16),
  ('expression -> GETPOLYPEPTIDES FINVOCATION STRING FINISHER','expression',4,'p_expression_getPolypeptides','parser.py',21),
  ('expression -> GETAMINOACIDSINFO FINVOCATION STRING FINISHER','expression',4,'p_expression_getAminoAcidsInfo','parser.py',26),
  ('expression -> NUMBER PLUS NUMBER','expression',3,'p_expression_plus','parser.py',31),
  ('expression -> NUMBER MINUS NUMBER','expression',3,'p_expression_minus','parser.py',35),
  ('expression -> NUMBER TIMES NUMBER','expression',3,'p_expression_times','parser.py',39),
  ('expression -> NUMBER DIVIDE NUMBER','expression',3,'p_expression_divide','parser.py',43),
  ('expression -> ID','expression',1,'p_expression_id','parser.py',47),
]