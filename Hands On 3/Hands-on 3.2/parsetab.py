
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDORrightNOTAND BOOLEAN LPAREN NOT OR RPARENexpr : expr AND term\n            | expr OR termexpr : termterm : NOT factorterm : factorfactor : LPAREN expr RPARENfactor : BOOLEAN'
    
_lr_action_items = {'NOT':([0,5,7,8,],[3,3,3,3,]),'LPAREN':([0,3,5,7,8,],[5,5,5,5,5,]),'BOOLEAN':([0,3,5,7,8,],[6,6,6,6,6,]),'$end':([1,2,4,6,9,11,12,13,],[0,-3,-5,-7,-4,-1,-2,-6,]),'AND':([1,2,4,6,9,10,11,12,13,],[7,-3,-5,-7,-4,7,-1,-2,-6,]),'OR':([1,2,4,6,9,10,11,12,13,],[8,-3,-5,-7,-4,8,-1,-2,-6,]),'RPAREN':([2,4,6,9,10,11,12,13,],[-3,-5,-7,-4,13,-1,-2,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr':([0,5,],[1,10,]),'term':([0,5,7,8,],[2,2,11,12,]),'factor':([0,3,5,7,8,],[4,9,4,4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> expr AND term','expr',3,'p_expr_binop','validador.py',10),
  ('expr -> expr OR term','expr',3,'p_expr_binop','validador.py',11),
  ('expr -> term','expr',1,'p_expr_term','validador.py',15),
  ('term -> NOT factor','term',2,'p_term_not','validador.py',19),
  ('term -> factor','term',1,'p_term_factor','validador.py',23),
  ('factor -> LPAREN expr RPAREN','factor',3,'p_factor_group','validador.py',27),
  ('factor -> BOOLEAN','factor',1,'p_factor_boolean','validador.py',31),
]
