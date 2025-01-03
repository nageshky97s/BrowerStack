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
import threading
import logging
import bstack_utils.bstack111ll1ll_opy_ as bstack1111111l_opy_
from bstack_utils.helper import bstack1ll111l1_opy_
logger = logging.getLogger(__name__)
def bstack1l1lll11ll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack1l1111l11_opy_(context, *args):
    tags = getattr(args[0], bstack111l1ll_opy_ (u"ࠩࡷࡥ࡬ࡹ္ࠧ"), [])
    bstack1l11llllll_opy_ = bstack1111111l_opy_.bstack1l111l1l1l_opy_(tags)
    threading.current_thread().isA11yTest = bstack1l11llllll_opy_
    try:
      bstack1lll1l111l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lll11ll_opy_(bstack111l1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳ်ࠩ")) else context.browser
      if bstack1lll1l111l_opy_ and bstack1lll1l111l_opy_.session_id and bstack1l11llllll_opy_ and bstack1ll111l1_opy_(
              threading.current_thread(), bstack111l1ll_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪျ"), None):
          threading.current_thread().isA11yTest = bstack1111111l_opy_.bstack11l111l1l_opy_(bstack1lll1l111l_opy_, bstack1l11llllll_opy_)
    except Exception as e:
       logger.debug(bstack111l1ll_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡢ࠳࠴ࡽࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥ࠻ࠢࡾࢁࠬြ").format(str(e)))
def bstack1llll111l_opy_(bstack1lll1l111l_opy_):
    if bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪွ"), None) and bstack1ll111l1_opy_(
      threading.current_thread(), bstack111l1ll_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ှ"), None) and not bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠨࡣ࠴࠵ࡾࡥࡳࡵࡱࡳࠫဿ"), False):
      threading.current_thread().a11y_stop = True
      bstack1111111l_opy_.bstack111l1111_opy_(bstack1lll1l111l_opy_, name=bstack111l1ll_opy_ (u"ࠤࠥ၀"), path=bstack111l1ll_opy_ (u"ࠥࠦ၁"))