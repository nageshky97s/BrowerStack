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
class bstack11l11l1ll1_opy_:
    def __init__(self, handler):
        self._1ll1l1ll1ll_opy_ = None
        self.handler = handler
        self._1ll1l1llll1_opy_ = self.bstack1ll1l1lll1l_opy_()
        self.patch()
    def patch(self):
        self._1ll1l1ll1ll_opy_ = self._1ll1l1llll1_opy_.execute
        self._1ll1l1llll1_opy_.execute = self.bstack1ll1l1lll11_opy_()
    def bstack1ll1l1lll11_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack111l1ll_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࠤᙵ"), driver_command, None, this, args)
            response = self._1ll1l1ll1ll_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack111l1ll_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࠤᙶ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._1ll1l1llll1_opy_.execute = self._1ll1l1ll1ll_opy_
    @staticmethod
    def bstack1ll1l1lll1l_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver