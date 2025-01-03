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
from browserstack_sdk.bstack1111ll1l_opy_ import bstack111l111l_opy_
from browserstack_sdk.bstack11llll11_opy_ import RobotHandler
def bstack11ll11111l_opy_(framework):
    if framework.lower() == bstack111l1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬጰ"):
        return bstack111l111l_opy_.version()
    elif framework.lower() == bstack111l1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬጱ"):
        return RobotHandler.version()
    elif framework.lower() == bstack111l1ll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧጲ"):
        import behave
        return behave.__version__
    else:
        return bstack111l1ll_opy_ (u"ࠨࡷࡱ࡯ࡳࡵࡷ࡯ࠩጳ")