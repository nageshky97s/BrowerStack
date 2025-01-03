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
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1llll1l1_opy_ = {}
        bstack1llll11l_opy_ = os.environ.get(bstack111l1ll_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫࡶ"), bstack111l1ll_opy_ (u"ࠫࠬࡷ"))
        if not bstack1llll11l_opy_:
            return bstack1llll1l1_opy_
        try:
            bstack1llll1ll_opy_ = json.loads(bstack1llll11l_opy_)
            if bstack111l1ll_opy_ (u"ࠧࡵࡳࠣࡸ") in bstack1llll1ll_opy_:
                bstack1llll1l1_opy_[bstack111l1ll_opy_ (u"ࠨ࡯ࡴࠤࡹ")] = bstack1llll1ll_opy_[bstack111l1ll_opy_ (u"ࠢࡰࡵࠥࡺ")]
            if bstack111l1ll_opy_ (u"ࠣࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧࡻ") in bstack1llll1ll_opy_ or bstack111l1ll_opy_ (u"ࠤࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠧࡼ") in bstack1llll1ll_opy_:
                bstack1llll1l1_opy_[bstack111l1ll_opy_ (u"ࠥࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳࠨࡽ")] = bstack1llll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠦࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣࡾ"), bstack1llll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠧࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠣࡿ")))
            if bstack111l1ll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࠢࢀ") in bstack1llll1ll_opy_ or bstack111l1ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠧࢁ") in bstack1llll1ll_opy_:
                bstack1llll1l1_opy_[bstack111l1ll_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࠨࢂ")] = bstack1llll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࠥࢃ"), bstack1llll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣࢄ")))
            if bstack111l1ll_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳࠨࢅ") in bstack1llll1ll_opy_ or bstack111l1ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨࢆ") in bstack1llll1ll_opy_:
                bstack1llll1l1_opy_[bstack111l1ll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠢࢇ")] = bstack1llll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠤ࢈"), bstack1llll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤࢉ")))
            if bstack111l1ll_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࠤࢊ") in bstack1llll1ll_opy_ or bstack111l1ll_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠢࢋ") in bstack1llll1ll_opy_:
                bstack1llll1l1_opy_[bstack111l1ll_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠣࢌ")] = bstack1llll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࠧࢍ"), bstack1llll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠥࢎ")))
            if bstack111l1ll_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠤ࢏") in bstack1llll1ll_opy_ or bstack111l1ll_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢ࢐") in bstack1llll1ll_opy_:
                bstack1llll1l1_opy_[bstack111l1ll_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣ࢑")] = bstack1llll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࠧ࢒"), bstack1llll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥ࢓")))
            if bstack111l1ll_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣ࢔") in bstack1llll1ll_opy_ or bstack111l1ll_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣ࢕") in bstack1llll1ll_opy_:
                bstack1llll1l1_opy_[bstack111l1ll_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤ࢖")] = bstack1llll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠦࢗ"), bstack1llll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦ࢘")))
            if bstack111l1ll_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷ࢙ࠧ") in bstack1llll1ll_opy_:
                bstack1llll1l1_opy_[bstack111l1ll_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸࠨ࢚")] = bstack1llll1ll_opy_[bstack111l1ll_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱ࡛ࡧࡲࡪࡣࡥࡰࡪࡹ࢛ࠢ")]
        except Exception as error:
            logger.error(bstack111l1ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡦࡹࡷࡸࡥ࡯ࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡪࡡࡵࡣ࠽ࠤࠧ࢜") +  str(error))
        return bstack1llll1l1_opy_