# coding: UTF-8
import sys
bstack11l1l11_opy_ = sys.version_info [0] == 2
bstack1l11l11_opy_ = 2048
bstack11_opy_ = 7
def bstack111l1ll_opy_ (bstack11lll11_opy_):
    global bstack1ll1l11_opy_
    bstack1ll11_opy_ = ord (bstack11lll11_opy_ [-1])
    bstack111l11_opy_ = bstack11lll11_opy_ [:-1]
    bstack11l11l1_opy_ = bstack1ll11_opy_ % len (bstack111l11_opy_)
    bstack11ll1l_opy_ = bstack111l11_opy_ [:bstack11l11l1_opy_] + bstack111l11_opy_ [bstack11l11l1_opy_:]
    if bstack11l1l11_opy_:
        bstack11ll1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l11_opy_ - (bstack1l1_opy_ + bstack1ll11_opy_) % bstack11_opy_) for bstack1l1_opy_, char in enumerate (bstack11ll1l_opy_)])
    else:
        bstack11ll1l1_opy_ = str () .join ([chr (ord (char) - bstack1l11l11_opy_ - (bstack1l1_opy_ + bstack1ll11_opy_) % bstack11_opy_) for bstack1l1_opy_, char in enumerate (bstack11ll1l_opy_)])
    return eval (bstack11ll1l1_opy_)
from collections import deque
from bstack_utils.constants import *
class bstack11ll1l11ll_opy_:
    def __init__(self):
        self._1lll111l1ll_opy_ = deque()
        self._1lll1111ll1_opy_ = {}
        self._1lll111ll11_opy_ = False
    def bstack1lll1111l1l_opy_(self, test_name, bstack1lll111l11l_opy_):
        bstack1lll11111l1_opy_ = self._1lll1111ll1_opy_.get(test_name, {})
        return bstack1lll11111l1_opy_.get(bstack1lll111l11l_opy_, 0)
    def bstack1lll111l111_opy_(self, test_name, bstack1lll111l11l_opy_):
        bstack1lll1111l11_opy_ = self.bstack1lll1111l1l_opy_(test_name, bstack1lll111l11l_opy_)
        self.bstack1lll111ll1l_opy_(test_name, bstack1lll111l11l_opy_)
        return bstack1lll1111l11_opy_
    def bstack1lll111ll1l_opy_(self, test_name, bstack1lll111l11l_opy_):
        if test_name not in self._1lll1111ll1_opy_:
            self._1lll1111ll1_opy_[test_name] = {}
        bstack1lll11111l1_opy_ = self._1lll1111ll1_opy_[test_name]
        bstack1lll1111l11_opy_ = bstack1lll11111l1_opy_.get(bstack1lll111l11l_opy_, 0)
        bstack1lll11111l1_opy_[bstack1lll111l11l_opy_] = bstack1lll1111l11_opy_ + 1
    def bstack1l1llll11l_opy_(self, bstack1lll11111ll_opy_, bstack1lll1111111_opy_):
        bstack1lll1111lll_opy_ = self.bstack1lll111l111_opy_(bstack1lll11111ll_opy_, bstack1lll1111111_opy_)
        event_name = bstack111l1111ll_opy_[bstack1lll1111111_opy_]
        bstack1lll111111l_opy_ = bstack111l1ll_opy_ (u"ࠥࡿࢂ࠳ࡻࡾ࠯ࡾࢁࠧᘛ").format(bstack1lll11111ll_opy_, event_name, bstack1lll1111lll_opy_)
        self._1lll111l1ll_opy_.append(bstack1lll111111l_opy_)
    def bstack11lllll1ll_opy_(self):
        return len(self._1lll111l1ll_opy_) == 0
    def bstack1l1111111_opy_(self):
        bstack1lll111l1l1_opy_ = self._1lll111l1ll_opy_.popleft()
        return bstack1lll111l1l1_opy_
    def capturing(self):
        return self._1lll111ll11_opy_
    def bstack1lllll1ll1_opy_(self):
        self._1lll111ll11_opy_ = True
    def bstack1lll1l11l_opy_(self):
        self._1lll111ll11_opy_ = False