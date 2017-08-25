# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import nose.tools as nt

from traitlets import Bool, Tuple, List

from .utils import setup, teardown

from ..widget import Widget

# A widget with simple traits
class SimpleWidget(Widget):
    a = Bool().tag(sync=True)
    b = Tuple(Bool(), Bool(), Bool(), default_value=(False, False, False)).tag(sync=True)
    c = List(Bool()).tag(sync=True)

def test_empty_send_state():
    w = SimpleWidget()
    w.send_state([])
    nt.assert_equal(w.comm.messages, [])

def test_empty_hold_sync():
    w = SimpleWidget()
    with w.hold_sync():
        pass
    nt.assert_equal(w.comm.messages, [])
