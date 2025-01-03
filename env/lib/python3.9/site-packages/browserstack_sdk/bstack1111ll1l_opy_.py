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
import multiprocessing
import os
import json
from time import sleep
import bstack_utils.bstack111ll1ll_opy_ as bstack1111111l_opy_
from browserstack_sdk.bstack11l11111_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1llllll1l_opy_
class bstack111l111l_opy_:
    def __init__(self, args, logger, bstack1111l111_opy_, bstack1lllllll1_opy_):
        self.args = args
        self.logger = logger
        self.bstack1111l111_opy_ = bstack1111l111_opy_
        self.bstack1lllllll1_opy_ = bstack1lllllll1_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack111l1lll_opy_ = []
        self.bstack111ll11l_opy_ = None
        self.bstack111l11ll_opy_ = []
        self.bstack111l1ll1_opy_ = self.bstack11111ll1_opy_()
        self.bstack11111l11_opy_ = -1
    def bstack111ll1l1_opy_(self, bstack111111ll_opy_):
        self.parse_args()
        self.bstack111l11l1_opy_()
        self.bstack111lll1l_opy_(bstack111111ll_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack1llllllll_opy_():
        import importlib
        if getattr(importlib, bstack111l1ll_opy_ (u"ࠨࡨ࡬ࡲࡩࡥ࡬ࡰࡣࡧࡩࡷ࠭শ"), False):
            bstack1lllll1ll_opy_ = importlib.find_loader(bstack111l1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࠫষ"))
        else:
            bstack1lllll1ll_opy_ = importlib.util.find_spec(bstack111l1ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠬস"))
    def bstack11111l1l_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack11111l11_opy_ = -1
        if self.bstack1lllllll1_opy_ and bstack111l1ll_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫহ") in self.bstack1111l111_opy_:
            self.bstack11111l11_opy_ = int(self.bstack1111l111_opy_[bstack111l1ll_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ঺")])
        try:
            bstack1111llll_opy_ = [bstack111l1ll_opy_ (u"࠭࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠨ঻"), bstack111l1ll_opy_ (u"ࠧ࠮࠯ࡳࡰࡺ࡭ࡩ࡯ࡵ়ࠪ"), bstack111l1ll_opy_ (u"ࠨ࠯ࡳࠫঽ")]
            if self.bstack11111l11_opy_ >= 0:
                bstack1111llll_opy_.extend([bstack111l1ll_opy_ (u"ࠩ࠰࠱ࡳࡻ࡭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪা"), bstack111l1ll_opy_ (u"ࠪ࠱ࡳ࠭ি")])
            for arg in bstack1111llll_opy_:
                self.bstack11111l1l_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack111l11l1_opy_(self):
        bstack111ll11l_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack111ll11l_opy_ = bstack111ll11l_opy_
        return bstack111ll11l_opy_
    def bstack11111111_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack1llllllll_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1llllll1l_opy_)
    def bstack111lll1l_opy_(self, bstack111111ll_opy_):
        bstack1111lll1_opy_ = Config.bstack11111lll_opy_()
        if bstack111111ll_opy_:
            self.bstack111ll11l_opy_.append(bstack111l1ll_opy_ (u"ࠫ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨী"))
            self.bstack111ll11l_opy_.append(bstack111l1ll_opy_ (u"࡚ࠬࡲࡶࡧࠪু"))
        if bstack1111lll1_opy_.bstack111ll111_opy_():
            self.bstack111ll11l_opy_.append(bstack111l1ll_opy_ (u"࠭࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬূ"))
            self.bstack111ll11l_opy_.append(bstack111l1ll_opy_ (u"ࠧࡕࡴࡸࡩࠬৃ"))
        self.bstack111ll11l_opy_.append(bstack111l1ll_opy_ (u"ࠨ࠯ࡳࠫৄ"))
        self.bstack111ll11l_opy_.append(bstack111l1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡱ࡮ࡸ࡫࡮ࡴࠧ৅"))
        self.bstack111ll11l_opy_.append(bstack111l1ll_opy_ (u"ࠪ࠱࠲ࡪࡲࡪࡸࡨࡶࠬ৆"))
        self.bstack111ll11l_opy_.append(bstack111l1ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫে"))
        if self.bstack11111l11_opy_ > 1:
            self.bstack111ll11l_opy_.append(bstack111l1ll_opy_ (u"ࠬ࠳࡮ࠨৈ"))
            self.bstack111ll11l_opy_.append(str(self.bstack11111l11_opy_))
    def bstack1111ll11_opy_(self):
        bstack111l11ll_opy_ = []
        for spec in self.bstack111l1lll_opy_:
            bstack1111l1l1_opy_ = [spec]
            bstack1111l1l1_opy_ += self.bstack111ll11l_opy_
            bstack111l11ll_opy_.append(bstack1111l1l1_opy_)
        self.bstack111l11ll_opy_ = bstack111l11ll_opy_
        return bstack111l11ll_opy_
    def bstack11111ll1_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack111l1ll1_opy_ = True
            return True
        except Exception as e:
            self.bstack111l1ll1_opy_ = False
        return self.bstack111l1ll1_opy_
    def bstack1111l1ll_opy_(self, bstack111lll11_opy_, bstack111ll1l1_opy_):
        bstack111ll1l1_opy_[bstack111l1ll_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭৉")] = self.bstack1111l111_opy_
        multiprocessing.set_start_method(bstack111l1ll_opy_ (u"ࠧࡴࡲࡤࡻࡳ࠭৊"))
        bstack111111l1_opy_ = []
        manager = multiprocessing.Manager()
        bstack1111l11l_opy_ = manager.list()
        if bstack111l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫো") in self.bstack1111l111_opy_:
            for index, platform in enumerate(self.bstack1111l111_opy_[bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬৌ")]):
                bstack111111l1_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack111lll11_opy_,
                                                            args=(self.bstack111ll11l_opy_, bstack111ll1l1_opy_, bstack1111l11l_opy_)))
            bstack111l1l11_opy_ = len(self.bstack1111l111_opy_[bstack111l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ্࠭")])
        else:
            bstack111111l1_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack111lll11_opy_,
                                                        args=(self.bstack111ll11l_opy_, bstack111ll1l1_opy_, bstack1111l11l_opy_)))
            bstack111l1l11_opy_ = 1
        i = 0
        for t in bstack111111l1_opy_:
            os.environ[bstack111l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫৎ")] = str(i)
            if bstack111l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ৏") in self.bstack1111l111_opy_:
                os.environ[bstack111l1ll_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧ৐")] = json.dumps(self.bstack1111l111_opy_[bstack111l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ৑")][i % bstack111l1l11_opy_])
            i += 1
            t.start()
        for t in bstack111111l1_opy_:
            t.join()
        return list(bstack1111l11l_opy_)
    @staticmethod
    def bstack111llll1_opy_(driver, bstack1llllll11_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack111l1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬ৒"), None)
        if item and getattr(item, bstack111l1ll_opy_ (u"ࠩࡢࡥ࠶࠷ࡹࡠࡶࡨࡷࡹࡥࡣࡢࡵࡨࠫ৓"), None) and not getattr(item, bstack111l1ll_opy_ (u"ࠪࡣࡦ࠷࠱ࡺࡡࡶࡸࡴࡶ࡟ࡥࡱࡱࡩࠬ৔"), False):
            logger.info(
                bstack111l1ll_opy_ (u"ࠦࡆࡻࡴࡰ࡯ࡤࡸࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠥ࡮ࡡࡴࠢࡨࡲࡩ࡫ࡤ࠯ࠢࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡮ࡹࠠࡶࡰࡧࡩࡷࡽࡡࡺ࠰ࠥ৕"))
            bstack111l1l1l_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1111111l_opy_.bstack111l1111_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)