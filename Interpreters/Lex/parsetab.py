
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADJECTIVE ADVERB ARTICLE NOUN PREPOSITION VERBsentence : noun_phrase verb_phrasenoun_phrase : ARTICLE NOUN\n                   | ARTICLE ADJECTIVE NOUNverb_phrase : VERB\n                   | VERB noun_phrase\n                   | VERB ADVERB noun_phrase\n                   | VERB PREPOSITION noun_phrase'
    
_lr_action_items = {'ARTICLE':([0,5,9,10,],[3,3,3,3,]),'$end':([1,4,5,6,8,11,12,13,],[0,-1,-4,-2,-5,-3,-6,-7,]),'VERB':([2,6,11,],[5,-2,-3,]),'NOUN':([3,7,],[6,11,]),'ADJECTIVE':([3,],[7,]),'ADVERB':([5,],[9,]),'PREPOSITION':([5,],[10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentence':([0,],[1,]),'noun_phrase':([0,5,9,10,],[2,8,12,13,]),'verb_phrase':([2,],[4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentence","S'",1,None,None,None),
  ('sentence -> noun_phrase verb_phrase','sentence',2,'p_sentence','grammars.py',45),
  ('noun_phrase -> ARTICLE NOUN','noun_phrase',2,'p_noun_phrase','grammars.py',49),
  ('noun_phrase -> ARTICLE ADJECTIVE NOUN','noun_phrase',3,'p_noun_phrase','grammars.py',50),
  ('verb_phrase -> VERB','verb_phrase',1,'p_verb_phrase','grammars.py',54),
  ('verb_phrase -> VERB noun_phrase','verb_phrase',2,'p_verb_phrase','grammars.py',55),
  ('verb_phrase -> VERB ADVERB noun_phrase','verb_phrase',3,'p_verb_phrase','grammars.py',56),
  ('verb_phrase -> VERB PREPOSITION noun_phrase','verb_phrase',3,'p_verb_phrase','grammars.py',57),
]
