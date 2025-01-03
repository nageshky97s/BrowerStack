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
import os
class RobotHandler():
    def __init__(self, args, logger, bstack1111l111_opy_, bstack1lllllll1_opy_):
        self.args = args
        self.logger = logger
        self.bstack1111l111_opy_ = bstack1111l111_opy_
        self.bstack1lllllll1_opy_ = bstack1lllllll1_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l11l1l1_opy_(bstack1llll1lll_opy_):
        bstack1lllll111_opy_ = []
        if bstack1llll1lll_opy_:
            tokens = str(os.path.basename(bstack1llll1lll_opy_)).split(bstack111l1ll_opy_ (u"ࠧࡥࠢ৖"))
            camelcase_name = bstack111l1ll_opy_ (u"ࠨࠠࠣৗ").join(t.title() for t in tokens)
            suite_name, bstack1lllll11l_opy_ = os.path.splitext(camelcase_name)
            bstack1lllll111_opy_.append(suite_name)
        return bstack1lllll111_opy_
    @staticmethod
    def bstack1lllll1l1_opy_(typename):
        if bstack111l1ll_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥ৘") in typename:
            return bstack111l1ll_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤ৙")
        return bstack111l1ll_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥ৚")