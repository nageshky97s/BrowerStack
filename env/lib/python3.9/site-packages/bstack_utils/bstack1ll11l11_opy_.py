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
import logging
import os
import threading
from bstack_utils.helper import bstack1l1l111lll_opy_
from bstack_utils.constants import bstack111l111l11_opy_
logger = logging.getLogger(__name__)
class bstack1l1l1l11_opy_:
    bstack1ll1l1lllll_opy_ = None
    @classmethod
    def bstack11lll1l111_opy_(cls):
        if cls.on():
            logger.info(
                bstack111l1ll_opy_ (u"࡙ࠩ࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽࠡࡶࡲࠤࡻ࡯ࡥࡸࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡴࡴࡸࡴ࠭ࠢ࡬ࡲࡸ࡯ࡧࡩࡶࡶ࠰ࠥࡧ࡮ࡥࠢࡰࡥࡳࡿࠠ࡮ࡱࡵࡩࠥࡪࡥࡣࡷࡪ࡫࡮ࡴࡧࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳࠦࡡ࡭࡮ࠣࡥࡹࠦ࡯࡯ࡧࠣࡴࡱࡧࡣࡦࠣ࡟ࡲࠬ᠙").format(os.environ[bstack111l1ll_opy_ (u"ࠥࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠤ᠚")]))
    @classmethod
    def on(cls):
        if os.environ.get(bstack111l1ll_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬ᠛"), None) is None or os.environ[bstack111l1ll_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭᠜")] == bstack111l1ll_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ᠝"):
            return False
        return True
    @classmethod
    def bstack1ll11l1111l_opy_(cls, bs_config, framework=bstack111l1ll_opy_ (u"ࠢࠣ᠞")):
        if bstack111l1ll_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ᠟") in framework:
            return bstack1l1l111lll_opy_(bs_config.get(bstack111l1ll_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᠠ")))
        bstack1ll111ll11l_opy_ = False
        for fw in bstack111l111l11_opy_:
            if fw in framework:
                bstack1ll111ll11l_opy_ = True
        return bstack1l1l111lll_opy_(bs_config.get(bstack111l1ll_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᠡ"), bstack1ll111ll11l_opy_))
    @classmethod
    def bstack1ll111l1l1l_opy_(cls, framework):
        return framework in bstack111l111l11_opy_
    @classmethod
    def bstack1ll11lllll1_opy_(cls, bs_config, framework):
        return cls.bstack1ll11l1111l_opy_(bs_config, framework) is True and cls.bstack1ll111l1l1l_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack111l1ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᠢ"), None)
    @staticmethod
    def bstack1ll11lll_opy_():
        if getattr(threading.current_thread(), bstack111l1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᠣ"), None):
            return {
                bstack111l1ll_opy_ (u"࠭ࡴࡺࡲࡨࠫᠤ"): bstack111l1ll_opy_ (u"ࠧࡵࡧࡶࡸࠬᠥ"),
                bstack111l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᠦ"): getattr(threading.current_thread(), bstack111l1ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᠧ"), None)
            }
        if getattr(threading.current_thread(), bstack111l1ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᠨ"), None):
            return {
                bstack111l1ll_opy_ (u"ࠫࡹࡿࡰࡦࠩᠩ"): bstack111l1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᠪ"),
                bstack111l1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᠫ"): getattr(threading.current_thread(), bstack111l1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᠬ"), None)
            }
        return None
    @staticmethod
    def bstack1ll111ll111_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l1l1l11_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l11l1l1_opy_(test, hook_name=None):
        bstack1ll111l1ll1_opy_ = test.parent
        if hook_name in [bstack111l1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭ᠭ"), bstack111l1ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪᠮ"), bstack111l1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩᠯ"), bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪ࠭ᠰ")]:
            bstack1ll111l1ll1_opy_ = test
        scope = []
        while bstack1ll111l1ll1_opy_ is not None:
            scope.append(bstack1ll111l1ll1_opy_.name)
            bstack1ll111l1ll1_opy_ = bstack1ll111l1ll1_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack1ll111l1lll_opy_(hook_type):
        if hook_type == bstack111l1ll_opy_ (u"ࠧࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠥᠱ"):
            return bstack111l1ll_opy_ (u"ࠨࡓࡦࡶࡸࡴࠥ࡮࡯ࡰ࡭ࠥᠲ")
        elif hook_type == bstack111l1ll_opy_ (u"ࠢࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠦᠳ"):
            return bstack111l1ll_opy_ (u"ࠣࡖࡨࡥࡷࡪ࡯ࡸࡰࠣ࡬ࡴࡵ࡫ࠣᠴ")
    @staticmethod
    def bstack1ll111l1l11_opy_(bstack111l1lll_opy_):
        try:
            if not bstack1l1l1l11_opy_.on():
                return bstack111l1lll_opy_
            if os.environ.get(bstack111l1ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔࠢᠵ"), None) == bstack111l1ll_opy_ (u"ࠥࡸࡷࡻࡥࠣᠶ"):
                tests = os.environ.get(bstack111l1ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࡡࡗࡉࡘ࡚ࡓࠣᠷ"), None)
                if tests is None or tests == bstack111l1ll_opy_ (u"ࠧࡴࡵ࡭࡮ࠥᠸ"):
                    return bstack111l1lll_opy_
                bstack111l1lll_opy_ = tests.split(bstack111l1ll_opy_ (u"࠭ࠬࠨᠹ"))
                return bstack111l1lll_opy_
        except Exception as exc:
            print(bstack111l1ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡲࡦࡴࡸࡲࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࡀࠠࠣᠺ"), str(exc))
        return bstack111l1lll_opy_