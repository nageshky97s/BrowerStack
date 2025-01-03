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
import json
import logging
import os
import datetime
import threading
from bstack_utils.helper import bstack111ll1ll1l_opy_, bstack111lll111l_opy_, bstack11l11l1111_opy_, bstack11l1111l_opy_, bstack111111lll1_opy_, bstack1111l1l1ll_opy_, bstack1111l111ll_opy_, bstack1l1lllll_opy_
from bstack_utils.bstack1ll1l1lllll_opy_ import bstack1ll1ll1l11l_opy_
import bstack_utils.bstack1l1l1111l1_opy_ as bstack11lll1111l_opy_
from bstack_utils.bstack1ll11l11_opy_ import bstack1l1l1l11_opy_
import bstack_utils.bstack111ll1ll_opy_ as bstack1111111l_opy_
from bstack_utils.bstack1ll1l1l11l_opy_ import bstack1ll1l1l11l_opy_
from bstack_utils.bstack1lll1ll1_opy_ import bstack11ll1l1l_opy_
bstack1ll11ll1lll_opy_ = bstack111l1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡥࡲࡰࡱ࡫ࡣࡵࡱࡵ࠱ࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧᛪ")
logger = logging.getLogger(__name__)
class bstack1ll11l1l_opy_:
    bstack1ll1l1lllll_opy_ = None
    bs_config = None
    bstack1ll1l1l1ll_opy_ = None
    @classmethod
    @bstack11l1111l_opy_(class_method=True)
    def launch(cls, bs_config, bstack1ll1l1l1ll_opy_):
        cls.bs_config = bs_config
        cls.bstack1ll1l1l1ll_opy_ = bstack1ll1l1l1ll_opy_
        try:
            cls.bstack1ll11ll1l11_opy_()
            bstack111ll1l111_opy_ = bstack111ll1ll1l_opy_(bs_config)
            bstack111lll1ll1_opy_ = bstack111lll111l_opy_(bs_config)
            data = bstack11lll1111l_opy_.bstack1ll11l11l1l_opy_(bs_config, bstack1ll1l1l1ll_opy_)
            config = {
                bstack111l1ll_opy_ (u"ࠨࡣࡸࡸ࡭࠭᛫"): (bstack111ll1l111_opy_, bstack111lll1ll1_opy_),
                bstack111l1ll_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪ᛬"): cls.default_headers()
            }
            response = bstack11l11l1111_opy_(bstack111l1ll_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ᛭"), cls.request_url(bstack111l1ll_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠵࠳ࡧࡻࡩ࡭ࡦࡶࠫᛮ")), data, config)
            if response.status_code != 200:
                bstack1ll11lll1ll_opy_ = response.json()
                if bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭ᛯ")] == False:
                    cls.bstack1ll1l111111_opy_(bstack1ll11lll1ll_opy_)
                    return
                cls.bstack1ll11l11ll1_opy_(bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᛰ")])
                cls.bstack1ll11ll11ll_opy_(bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᛱ")])
                return None
            bstack1ll11l11lll_opy_ = cls.bstack1ll11lll1l1_opy_(response)
            return bstack1ll11l11lll_opy_
        except Exception as error:
            logger.error(bstack111l1ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࠤ࡫ࡵࡲࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࡿࢂࠨᛲ").format(str(error)))
            return None
    @classmethod
    @bstack11l1111l_opy_(class_method=True)
    def stop(cls, bstack1ll11l1ll1l_opy_=None):
        if not bstack1l1l1l11_opy_.on() and not bstack1111111l_opy_.on():
            return
        if os.environ.get(bstack111l1ll_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᛳ")) == bstack111l1ll_opy_ (u"ࠥࡲࡺࡲ࡬ࠣᛴ") or os.environ.get(bstack111l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᛵ")) == bstack111l1ll_opy_ (u"ࠧࡴࡵ࡭࡮ࠥᛶ"):
            logger.error(bstack111l1ll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡰࡲࠣࡦࡺ࡯࡬ࡥࠢࡵࡩࡶࡻࡥࡴࡶࠣࡸࡴࠦࡔࡦࡵࡷࡌࡺࡨ࠺ࠡࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡤࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧࡦࡺࡩࡰࡰࠣࡸࡴࡱࡥ࡯ࠩᛷ"))
            return {
                bstack111l1ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᛸ"): bstack111l1ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ᛹"),
                bstack111l1ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ᛺"): bstack111l1ll_opy_ (u"ࠪࡘࡴࡱࡥ࡯࠱ࡥࡹ࡮ࡲࡤࡊࡆࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡪ࡮ࡴࡥࡥ࠮ࠣࡦࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤࡲ࡯ࡧࡩࡶࠣ࡬ࡦࡼࡥࠡࡨࡤ࡭ࡱ࡫ࡤࠨ᛻")
            }
        try:
            cls.bstack1ll1l1lllll_opy_.shutdown()
            data = {
                bstack111l1ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ᛼"): bstack1l1lllll_opy_()
            }
            if not bstack1ll11l1ll1l_opy_ is None:
                data[bstack111l1ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟࡮ࡧࡷࡥࡩࡧࡴࡢࠩ᛽")] = [{
                    bstack111l1ll_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭᛾"): bstack111l1ll_opy_ (u"ࠧࡶࡵࡨࡶࡤࡱࡩ࡭࡮ࡨࡨࠬ᛿"),
                    bstack111l1ll_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࠨᜀ"): bstack1ll11l1ll1l_opy_
                }]
            config = {
                bstack111l1ll_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪᜁ"): cls.default_headers()
            }
            bstack1111ll111l_opy_ = bstack111l1ll_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂ࠵ࡳࡵࡱࡳࠫᜂ").format(os.environ[bstack111l1ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤᜃ")])
            bstack1ll11llll1l_opy_ = cls.request_url(bstack1111ll111l_opy_)
            response = bstack11l11l1111_opy_(bstack111l1ll_opy_ (u"ࠬࡖࡕࡕࠩᜄ"), bstack1ll11llll1l_opy_, data, config)
            if not response.ok:
                raise Exception(bstack111l1ll_opy_ (u"ࠨࡓࡵࡱࡳࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡴ࡯ࡵࠢࡲ࡯ࠧᜅ"))
        except Exception as error:
            logger.error(bstack111l1ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡵࡱࡳࠤࡧࡻࡩ࡭ࡦࠣࡶࡪࡷࡵࡦࡵࡷࠤࡹࡵࠠࡕࡧࡶࡸࡍࡻࡢ࠻࠼ࠣࠦᜆ") + str(error))
            return {
                bstack111l1ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᜇ"): bstack111l1ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᜈ"),
                bstack111l1ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᜉ"): str(error)
            }
    @classmethod
    @bstack11l1111l_opy_(class_method=True)
    def bstack1ll11lll1l1_opy_(cls, response):
        bstack1ll11lll1ll_opy_ = response.json()
        bstack1ll11l11lll_opy_ = {}
        if bstack1ll11lll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠫ࡯ࡽࡴࠨᜊ")) is None:
            os.environ[bstack111l1ll_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᜋ")] = bstack111l1ll_opy_ (u"࠭࡮ࡶ࡮࡯ࠫᜌ")
        else:
            os.environ[bstack111l1ll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᜍ")] = bstack1ll11lll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠨ࡬ࡺࡸࠬᜎ"), bstack111l1ll_opy_ (u"ࠩࡱࡹࡱࡲࠧᜏ"))
        os.environ[bstack111l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᜐ")] = bstack1ll11lll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ᜑ"), bstack111l1ll_opy_ (u"ࠬࡴࡵ࡭࡮ࠪᜒ"))
        if bstack1l1l1l11_opy_.bstack1ll11lllll1_opy_(cls.bs_config, cls.bstack1ll1l1l1ll_opy_.get(bstack111l1ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡸࡷࡪࡪࠧᜓ"), bstack111l1ll_opy_ (u"ࠧࠨ᜔"))) is True:
            bstack1ll11l1l1l1_opy_, bstack1ll1llllll_opy_, bstack1ll11ll111l_opy_ = cls.bstack1ll11l1l111_opy_(bstack1ll11lll1ll_opy_)
            if bstack1ll11l1l1l1_opy_ != None and bstack1ll1llllll_opy_ != None:
                bstack1ll11l11lll_opy_[bstack111l1ll_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ᜕")] = {
                    bstack111l1ll_opy_ (u"ࠩ࡭ࡻࡹࡥࡴࡰ࡭ࡨࡲࠬ᜖"): bstack1ll11l1l1l1_opy_,
                    bstack111l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ᜗"): bstack1ll1llllll_opy_,
                    bstack111l1ll_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨ᜘"): bstack1ll11ll111l_opy_
                }
            else:
                bstack1ll11l11lll_opy_[bstack111l1ll_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ᜙")] = {}
        else:
            bstack1ll11l11lll_opy_[bstack111l1ll_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭᜚")] = {}
        if bstack1111111l_opy_.bstack111lll11l1_opy_(cls.bs_config) is True:
            bstack1ll11ll1l1l_opy_, bstack1ll1llllll_opy_ = cls.bstack1ll11l1l11l_opy_(bstack1ll11lll1ll_opy_)
            if bstack1ll11ll1l1l_opy_ != None and bstack1ll1llllll_opy_ != None:
                bstack1ll11l11lll_opy_[bstack111l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ᜛")] = {
                    bstack111l1ll_opy_ (u"ࠨࡣࡸࡸ࡭ࡥࡴࡰ࡭ࡨࡲࠬ᜜"): bstack1ll11ll1l1l_opy_,
                    bstack111l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ᜝"): bstack1ll1llllll_opy_,
                }
            else:
                bstack1ll11l11lll_opy_[bstack111l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ᜞")] = {}
        else:
            bstack1ll11l11lll_opy_[bstack111l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᜟ")] = {}
        if bstack1ll11l11lll_opy_[bstack111l1ll_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬᜠ")].get(bstack111l1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨᜡ")) != None or bstack1ll11l11lll_opy_[bstack111l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᜢ")].get(bstack111l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪᜣ")) != None:
            cls.bstack1ll11ll1111_opy_(bstack1ll11lll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠩ࡭ࡻࡹ࠭ᜤ")), bstack1ll11lll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬᜥ")))
        return bstack1ll11l11lll_opy_
    @classmethod
    def bstack1ll11l1l111_opy_(cls, bstack1ll11lll1ll_opy_):
        if bstack1ll11lll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫᜦ")) == None:
            cls.bstack1ll11l11ll1_opy_()
            return [None, None, None]
        if bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬᜧ")][bstack111l1ll_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧᜨ")] != True:
            cls.bstack1ll11l11ll1_opy_(bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᜩ")])
            return [None, None, None]
        logger.debug(bstack111l1ll_opy_ (u"ࠨࡖࡨࡷࡹࠦࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࠦࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡔࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࠥࠬᜪ"))
        os.environ[bstack111l1ll_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡉࡏࡎࡒࡏࡉ࡙ࡋࡄࠨᜫ")] = bstack111l1ll_opy_ (u"ࠪࡸࡷࡻࡥࠨᜬ")
        if bstack1ll11lll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠫ࡯ࡽࡴࠨᜭ")):
            os.environ[bstack111l1ll_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭ᜮ")] = bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"࠭ࡪࡸࡶࠪᜯ")]
            os.environ[bstack111l1ll_opy_ (u"ࠧࡄࡔࡈࡈࡊࡔࡔࡊࡃࡏࡗࡤࡌࡏࡓࡡࡆࡖࡆ࡙ࡈࡠࡔࡈࡔࡔࡘࡔࡊࡐࡊࠫᜰ")] = json.dumps({
                bstack111l1ll_opy_ (u"ࠨࡷࡶࡩࡷࡴࡡ࡮ࡧࠪᜱ"): bstack111ll1ll1l_opy_(cls.bs_config),
                bstack111l1ll_opy_ (u"ࠩࡳࡥࡸࡹࡷࡰࡴࡧࠫᜲ"): bstack111lll111l_opy_(cls.bs_config)
            })
        if bstack1ll11lll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬᜳ")):
            os.environ[bstack111l1ll_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆ᜴ࠪ")] = bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ᜵")]
        if bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭᜶")].get(bstack111l1ll_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨ᜷"), {}).get(bstack111l1ll_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬ᜸")):
            os.environ[bstack111l1ll_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪ᜹")] = str(bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ᜺")][bstack111l1ll_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ᜻")][bstack111l1ll_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩ᜼")])
        return [bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"࠭ࡪࡸࡶࠪ᜽")], bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ᜾")], os.environ[bstack111l1ll_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡇࡌࡍࡑ࡚ࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࡔࠩ᜿")]]
    @classmethod
    def bstack1ll11l1l11l_opy_(cls, bstack1ll11lll1ll_opy_):
        if bstack1ll11lll1ll_opy_.get(bstack111l1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᝀ")) == None:
            cls.bstack1ll11ll11ll_opy_()
            return [None, None]
        if bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᝁ")][bstack111l1ll_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬᝂ")] != True:
            cls.bstack1ll11ll11ll_opy_(bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᝃ")])
            return [None, None]
        if bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᝄ")].get(bstack111l1ll_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨᝅ")):
            logger.debug(bstack111l1ll_opy_ (u"ࠨࡖࡨࡷࡹࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡔࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࠥࠬᝆ"))
            parsed = json.loads(os.getenv(bstack111l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪᝇ"), bstack111l1ll_opy_ (u"ࠪࡿࢂ࠭ᝈ")))
            capabilities = bstack11lll1111l_opy_.bstack1ll11llll11_opy_(bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᝉ")][bstack111l1ll_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ᝊ")][bstack111l1ll_opy_ (u"࠭ࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬᝋ")], bstack111l1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᝌ"), bstack111l1ll_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧᝍ"))
            bstack1ll11ll1l1l_opy_ = capabilities[bstack111l1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡖࡲ࡯ࡪࡴࠧᝎ")]
            os.environ[bstack111l1ll_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨᝏ")] = bstack1ll11ll1l1l_opy_
            parsed[bstack111l1ll_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᝐ")] = capabilities[bstack111l1ll_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᝑ")]
            os.environ[bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧᝒ")] = json.dumps(parsed)
            scripts = bstack11lll1111l_opy_.bstack1ll11llll11_opy_(bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᝓ")][bstack111l1ll_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩ᝔")][bstack111l1ll_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪ᝕")], bstack111l1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨ᝖"), bstack111l1ll_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࠬ᝗"))
            bstack1ll1l1l11l_opy_.bstack111ll111ll_opy_(scripts)
            commands = bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ᝘")][bstack111l1ll_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ᝙")][bstack111l1ll_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࡖࡲ࡛ࡷࡧࡰࠨ᝚")].get(bstack111l1ll_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪ᝛"))
            bstack1ll1l1l11l_opy_.bstack111l1ll1ll_opy_(commands)
            bstack1ll1l1l11l_opy_.store()
        return [bstack1ll11ll1l1l_opy_, bstack1ll11lll1ll_opy_[bstack111l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ᝜")]]
    @classmethod
    def bstack1ll11l11ll1_opy_(cls, response=None):
        os.environ[bstack111l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ᝝")] = bstack111l1ll_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ᝞")
        os.environ[bstack111l1ll_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡅࡒࡑࡕࡒࡅࡕࡇࡇࠫ᝟")] = bstack111l1ll_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬᝠ")
        os.environ[bstack111l1ll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᝡ")] = bstack111l1ll_opy_ (u"ࠨࡰࡸࡰࡱ࠭ᝢ")
        os.environ[bstack111l1ll_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡊࡘࡖࠪᝣ")] = bstack111l1ll_opy_ (u"ࠪࡲࡺࡲ࡬ࠨᝤ")
        os.environ[bstack111l1ll_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪᝥ")] = bstack111l1ll_opy_ (u"ࠧࡴࡵ࡭࡮ࠥᝦ")
        os.environ[bstack111l1ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧᝧ")] = bstack111l1ll_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᝨ")
        cls.bstack1ll1l111111_opy_(response, bstack111l1ll_opy_ (u"ࠣࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠣᝩ"))
        return [None, None, None]
    @classmethod
    def bstack1ll11ll11ll_opy_(cls, response=None):
        os.environ[bstack111l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᝪ")] = bstack111l1ll_opy_ (u"ࠪࡲࡺࡲ࡬ࠨᝫ")
        os.environ[bstack111l1ll_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩᝬ")] = bstack111l1ll_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ᝭")
        os.environ[bstack111l1ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧᝮ")] = bstack111l1ll_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬᝯ")
        cls.bstack1ll1l111111_opy_(response, bstack111l1ll_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠣᝰ"))
        return [None, None, None]
    @classmethod
    def bstack1ll11ll1111_opy_(cls, bstack1ll1l1111l1_opy_, bstack1ll1llllll_opy_):
        os.environ[bstack111l1ll_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ᝱")] = bstack1ll1l1111l1_opy_
        os.environ[bstack111l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᝲ")] = bstack1ll1llllll_opy_
    @classmethod
    def bstack1ll1l111111_opy_(cls, response=None, product=bstack111l1ll_opy_ (u"ࠦࠧᝳ")):
        if response == None:
            logger.error(product + bstack111l1ll_opy_ (u"ࠧࠦࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠢ᝴"))
        for error in response[bstack111l1ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭᝵")]:
            bstack1111lll11l_opy_ = error[bstack111l1ll_opy_ (u"ࠧ࡬ࡧࡼࠫ᝶")]
            error_message = error[bstack111l1ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ᝷")]
            if error_message:
                if bstack1111lll11l_opy_ == bstack111l1ll_opy_ (u"ࠤࡈࡖࡗࡕࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡆࡈࡒࡎࡋࡄࠣ᝸"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack111l1ll_opy_ (u"ࠥࡈࡦࡺࡡࠡࡷࡳࡰࡴࡧࡤࠡࡶࡲࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࠦ᝹") + product + bstack111l1ll_opy_ (u"ࠦࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡪࡵࡦࠢࡷࡳࠥࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠤ᝺"))
    @classmethod
    def bstack1ll11ll1l11_opy_(cls):
        if cls.bstack1ll1l1lllll_opy_ is not None:
            return
        cls.bstack1ll1l1lllll_opy_ = bstack1ll1ll1l11l_opy_(cls.bstack1ll11l1lll1_opy_)
        cls.bstack1ll1l1lllll_opy_.start()
    @classmethod
    def bstack1l111ll1_opy_(cls):
        if cls.bstack1ll1l1lllll_opy_ is None:
            return
        cls.bstack1ll1l1lllll_opy_.shutdown()
    @classmethod
    @bstack11l1111l_opy_(class_method=True)
    def bstack1ll11l1lll1_opy_(cls, bstack1l11ll11_opy_, bstack1ll11ll11l1_opy_=bstack111l1ll_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡡࡵࡥ࡫ࠫ᝻")):
        config = {
            bstack111l1ll_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ᝼"): cls.default_headers()
        }
        response = bstack11l11l1111_opy_(bstack111l1ll_opy_ (u"ࠧࡑࡑࡖࡘࠬ᝽"), cls.request_url(bstack1ll11ll11l1_opy_), bstack1l11ll11_opy_, config)
        bstack111ll1111l_opy_ = response.json()
    @classmethod
    def bstack11ll1l11_opy_(cls, bstack1l11ll11_opy_, bstack1ll11ll11l1_opy_=bstack111l1ll_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡤࡸࡨ࡮ࠧ᝾")):
        if not bstack11lll1111l_opy_.bstack1ll1l11111l_opy_(bstack1l11ll11_opy_[bstack111l1ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭᝿")]):
            return
        bstack111lllll1_opy_ = bstack11lll1111l_opy_.bstack1ll11lll11l_opy_(bstack1l11ll11_opy_[bstack111l1ll_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧក")], bstack1l11ll11_opy_.get(bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭ខ")))
        if bstack111lllll1_opy_ != None:
            if bstack1l11ll11_opy_.get(bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧគ")) != None:
                bstack1l11ll11_opy_[bstack111l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨឃ")][bstack111l1ll_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬង")] = bstack111lllll1_opy_
            else:
                bstack1l11ll11_opy_[bstack111l1ll_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭ច")] = bstack111lllll1_opy_
        if bstack1ll11ll11l1_opy_ == bstack111l1ll_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨឆ"):
            cls.bstack1ll11ll1l11_opy_()
            cls.bstack1ll1l1lllll_opy_.add(bstack1l11ll11_opy_)
        elif bstack1ll11ll11l1_opy_ == bstack111l1ll_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨជ"):
            cls.bstack1ll11l1lll1_opy_([bstack1l11ll11_opy_], bstack1ll11ll11l1_opy_)
    @classmethod
    @bstack11l1111l_opy_(class_method=True)
    def bstack1l1l1ll1_opy_(cls, bstack11l111ll_opy_):
        bstack1ll11llllll_opy_ = []
        for log in bstack11l111ll_opy_:
            bstack1ll11l1llll_opy_ = {
                bstack111l1ll_opy_ (u"ࠫࡰ࡯࡮ࡥࠩឈ"): bstack111l1ll_opy_ (u"࡚ࠬࡅࡔࡖࡢࡐࡔࡍࠧញ"),
                bstack111l1ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬដ"): log[bstack111l1ll_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ឋ")],
                bstack111l1ll_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫឌ"): log[bstack111l1ll_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬឍ")],
                bstack111l1ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡠࡴࡨࡷࡵࡵ࡮ࡴࡧࠪណ"): {},
                bstack111l1ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬត"): log[bstack111l1ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ថ")],
            }
            if bstack111l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ទ") in log:
                bstack1ll11l1llll_opy_[bstack111l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧធ")] = log[bstack111l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨន")]
            elif bstack111l1ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩប") in log:
                bstack1ll11l1llll_opy_[bstack111l1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪផ")] = log[bstack111l1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫព")]
            bstack1ll11llllll_opy_.append(bstack1ll11l1llll_opy_)
        cls.bstack11ll1l11_opy_({
            bstack111l1ll_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩភ"): bstack111l1ll_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪម"),
            bstack111l1ll_opy_ (u"ࠧ࡭ࡱࡪࡷࠬយ"): bstack1ll11llllll_opy_
        })
    @classmethod
    @bstack11l1111l_opy_(class_method=True)
    def bstack1ll11l1l1ll_opy_(cls, steps):
        bstack1ll11ll1ll1_opy_ = []
        for step in steps:
            bstack1ll1l1111ll_opy_ = {
                bstack111l1ll_opy_ (u"ࠨ࡭࡬ࡲࡩ࠭រ"): bstack111l1ll_opy_ (u"ࠩࡗࡉࡘ࡚࡟ࡔࡖࡈࡔࠬល"),
                bstack111l1ll_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩវ"): step[bstack111l1ll_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪឝ")],
                bstack111l1ll_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨឞ"): step[bstack111l1ll_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩស")],
                bstack111l1ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨហ"): step[bstack111l1ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩឡ")],
                bstack111l1ll_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫអ"): step[bstack111l1ll_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬឣ")]
            }
            if bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫឤ") in step:
                bstack1ll1l1111ll_opy_[bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬឥ")] = step[bstack111l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ឦ")]
            elif bstack111l1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧឧ") in step:
                bstack1ll1l1111ll_opy_[bstack111l1ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨឨ")] = step[bstack111l1ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩឩ")]
            bstack1ll11ll1ll1_opy_.append(bstack1ll1l1111ll_opy_)
        cls.bstack11ll1l11_opy_({
            bstack111l1ll_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧឪ"): bstack111l1ll_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨឫ"),
            bstack111l1ll_opy_ (u"ࠬࡲ࡯ࡨࡵࠪឬ"): bstack1ll11ll1ll1_opy_
        })
    @classmethod
    @bstack11l1111l_opy_(class_method=True)
    def bstack1ll1l1llll_opy_(cls, screenshot):
        cls.bstack11ll1l11_opy_({
            bstack111l1ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪឭ"): bstack111l1ll_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫឮ"),
            bstack111l1ll_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭ឯ"): [{
                bstack111l1ll_opy_ (u"ࠩ࡮࡭ࡳࡪࠧឰ"): bstack111l1ll_opy_ (u"ࠪࡘࡊ࡙ࡔࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࠬឱ"),
                bstack111l1ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧឲ"): datetime.datetime.utcnow().isoformat() + bstack111l1ll_opy_ (u"ࠬࡠࠧឳ"),
                bstack111l1ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ឴"): screenshot[bstack111l1ll_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭឵")],
                bstack111l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨា"): screenshot[bstack111l1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩិ")]
            }]
        }, bstack1ll11ll11l1_opy_=bstack111l1ll_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨី"))
    @classmethod
    @bstack11l1111l_opy_(class_method=True)
    def bstack11lll1l11l_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack11ll1l11_opy_({
            bstack111l1ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨឹ"): bstack111l1ll_opy_ (u"ࠬࡉࡂࡕࡕࡨࡷࡸ࡯࡯࡯ࡅࡵࡩࡦࡺࡥࡥࠩឺ"),
            bstack111l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨុ"): {
                bstack111l1ll_opy_ (u"ࠢࡶࡷ࡬ࡨࠧូ"): cls.current_test_uuid(),
                bstack111l1ll_opy_ (u"ࠣ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠢួ"): cls.bstack1lll1l1l_opy_(driver)
            }
        })
    @classmethod
    def bstack1ll1l11l_opy_(cls, event: str, bstack1l11ll11_opy_: bstack11ll1l1l_opy_):
        bstack1l11llll_opy_ = {
            bstack111l1ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ើ"): event,
            bstack1l11ll11_opy_.bstack11ll1lll_opy_(): bstack1l11ll11_opy_.bstack11ll11ll_opy_(event)
        }
        cls.bstack11ll1l11_opy_(bstack1l11llll_opy_)
        result = getattr(bstack1l11ll11_opy_, bstack111l1ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪឿ"), None)
        if event == bstack111l1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬៀ"):
            threading.current_thread().bstackTestMeta = {bstack111l1ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬេ"): bstack111l1ll_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧែ")}
        elif event == bstack111l1ll_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩៃ"):
            threading.current_thread().bstackTestMeta = {bstack111l1ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨោ"): getattr(result, bstack111l1ll_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩៅ"), bstack111l1ll_opy_ (u"ࠪࠫំ"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack111l1ll_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬះ"), None) is None or os.environ[bstack111l1ll_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭ៈ")] == bstack111l1ll_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ៉")) and (os.environ.get(bstack111l1ll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ៊"), None) is None or os.environ[bstack111l1ll_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭់")] == bstack111l1ll_opy_ (u"ࠤࡱࡹࡱࡲࠢ៌")):
            return False
        return True
    @staticmethod
    def bstack1ll11lll111_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1ll11l1l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack111l1ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ៍"): bstack111l1ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ៎"),
            bstack111l1ll_opy_ (u"ࠬ࡞࠭ࡃࡕࡗࡅࡈࡑ࠭ࡕࡇࡖࡘࡔࡖࡓࠨ៏"): bstack111l1ll_opy_ (u"࠭ࡴࡳࡷࡨࠫ័")
        }
        if os.environ.get(bstack111l1ll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ៑"), None):
            headers[bstack111l1ll_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨ្")] = bstack111l1ll_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬ៓").format(os.environ[bstack111l1ll_opy_ (u"ࠥࡆࡘࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠦ។")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack111l1ll_opy_ (u"ࠫࢀࢃ࠯ࡼࡿࠪ៕").format(bstack1ll11ll1lll_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack111l1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ៖"), None)
    @staticmethod
    def bstack1lll1l1l_opy_(driver):
        return {
            bstack111111lll1_opy_(): bstack1111l1l1ll_opy_(driver)
        }
    @staticmethod
    def bstack1ll11l1ll11_opy_(exception_info, report):
        return [{bstack111l1ll_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩៗ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack1lllll1l1_opy_(typename):
        if bstack111l1ll_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥ៘") in typename:
            return bstack111l1ll_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤ៙")
        return bstack111l1ll_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥ៚")