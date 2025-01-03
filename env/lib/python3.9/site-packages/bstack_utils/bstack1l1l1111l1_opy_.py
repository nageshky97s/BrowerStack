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
import datetime
import threading
from bstack_utils.helper import bstack111ll111l1_opy_, bstack11l1l111l_opy_, get_host_info, bstack1llllll11ll_opy_, \
 bstack11ll1lll1_opy_, bstack1ll111l1_opy_, bstack11l1111l_opy_, bstack1111l111ll_opy_, bstack1l1lllll_opy_
import bstack_utils.bstack111ll1ll_opy_ as bstack1111111l_opy_
from bstack_utils.bstack1ll11l11_opy_ import bstack1l1l1l11_opy_
from bstack_utils.percy import bstack1l111l1111_opy_
from bstack_utils.config import Config
bstack1111lll1_opy_ = Config.bstack11111lll_opy_()
logger = logging.getLogger(__name__)
percy = bstack1l111l1111_opy_()
@bstack11l1111l_opy_(class_method=False)
def bstack1ll11l11l1l_opy_(bs_config, bstack1ll1l1l1ll_opy_):
  try:
    data = {
        bstack111l1ll_opy_ (u"ࠪࡪࡴࡸ࡭ࡢࡶࠪ៛"): bstack111l1ll_opy_ (u"ࠫ࡯ࡹ࡯࡯ࠩៜ"),
        bstack111l1ll_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡥ࡮ࡢ࡯ࡨࠫ៝"): bs_config.get(bstack111l1ll_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫ៞"), bstack111l1ll_opy_ (u"ࠧࠨ៟")),
        bstack111l1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭០"): bs_config.get(bstack111l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ១"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack111l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭២"): bs_config.get(bstack111l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭៣")),
        bstack111l1ll_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ៤"): bs_config.get(bstack111l1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡉ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩ៥"), bstack111l1ll_opy_ (u"ࠧࠨ៦")),
        bstack111l1ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ៧"): bstack1l1lllll_opy_(),
        bstack111l1ll_opy_ (u"ࠩࡷࡥ࡬ࡹࠧ៨"): bstack1llllll11ll_opy_(bs_config),
        bstack111l1ll_opy_ (u"ࠪ࡬ࡴࡹࡴࡠ࡫ࡱࡪࡴ࠭៩"): get_host_info(),
        bstack111l1ll_opy_ (u"ࠫࡨ࡯࡟ࡪࡰࡩࡳࠬ៪"): bstack11l1l111l_opy_(),
        bstack111l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣࡷࡻ࡮ࡠ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ៫"): os.environ.get(bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡗ࡛ࡎࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ៬")),
        bstack111l1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪ࡟ࡵࡧࡶࡸࡸࡥࡲࡦࡴࡸࡲࠬ៭"): os.environ.get(bstack111l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓ࠭៮"), False),
        bstack111l1ll_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࡢࡧࡴࡴࡴࡳࡱ࡯ࠫ៯"): bstack111ll111l1_opy_(),
        bstack111l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ៰"): bstack1ll111ll1ll_opy_(),
        bstack111l1ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡥࡧࡷࡥ࡮ࡲࡳࠨ៱"): bstack1ll11l111l1_opy_(bstack1ll1l1l1ll_opy_),
        bstack111l1ll_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪ៲"): bstack1ll1l11ll_opy_(bs_config, bstack1ll1l1l1ll_opy_.get(bstack111l1ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡸࡷࡪࡪࠧ៳"), bstack111l1ll_opy_ (u"ࠧࠨ៴"))),
        bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪ៵"): bstack11ll1lll1_opy_(bs_config),
    }
    return data
  except Exception as error:
    logger.error(bstack111l1ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡰࡢࡻ࡯ࡳࡦࡪࠠࡧࡱࡵࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࠦࠠࡼࡿࠥ៶").format(str(error)))
    return None
def bstack1ll11l111l1_opy_(framework):
  return {
    bstack111l1ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡔࡡ࡮ࡧࠪ៷"): framework.get(bstack111l1ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࠬ៸"), bstack111l1ll_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸࠬ៹")),
    bstack111l1ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩ៺"): framework.get(bstack111l1ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫ៻")),
    bstack111l1ll_opy_ (u"ࠨࡵࡧ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ៼"): framework.get(bstack111l1ll_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ៽")),
    bstack111l1ll_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࠬ៾"): bstack111l1ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ៿"),
    bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ᠀"): framework.get(bstack111l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭᠁"))
  }
def bstack1ll1l11ll_opy_(bs_config, framework):
  bstack11l11ll1l_opy_ = False
  bstack111lll111_opy_ = False
  bstack1ll111lll11_opy_ = False
  if bstack111l1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ᠂") in bs_config:
    bstack1ll111lll11_opy_ = True
  elif bstack111l1ll_opy_ (u"ࠨࡣࡳࡴࠬ᠃") in bs_config:
    bstack11l11ll1l_opy_ = True
  else:
    bstack111lll111_opy_ = True
  bstack111lllll1_opy_ = {
    bstack111l1ll_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ᠄"): bstack1l1l1l11_opy_.bstack1ll11l1111l_opy_(bs_config, framework),
    bstack111l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ᠅"): bstack1111111l_opy_.bstack111lll11l1_opy_(bs_config),
    bstack111l1ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ᠆"): bs_config.get(bstack111l1ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ᠇"), False),
    bstack111l1ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨ᠈"): bstack111lll111_opy_,
    bstack111l1ll_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭᠉"): bstack11l11ll1l_opy_,
    bstack111l1ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬ᠊"): bstack1ll111lll11_opy_
  }
  return bstack111lllll1_opy_
@bstack11l1111l_opy_(class_method=False)
def bstack1ll111ll1ll_opy_():
  try:
    bstack1ll111lll1l_opy_ = json.loads(os.getenv(bstack111l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ᠋"), bstack111l1ll_opy_ (u"ࠪࡿࢂ࠭᠌")))
    return {
        bstack111l1ll_opy_ (u"ࠫࡸ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭᠍"): bstack1ll111lll1l_opy_
    }
  except Exception as error:
    logger.error(bstack111l1ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡪࡩࡹࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠡࡨࡲࡶ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࠡࡽࢀࠦ᠎").format(str(error)))
    return {}
def bstack1ll11llll11_opy_(array, bstack1ll11l11l11_opy_, bstack1ll11l11111_opy_):
  result = {}
  for o in array:
    key = o[bstack1ll11l11l11_opy_]
    result[key] = o[bstack1ll11l11111_opy_]
  return result
def bstack1ll1l11111l_opy_(bstack11l1111111_opy_=bstack111l1ll_opy_ (u"࠭ࠧ᠏")):
  bstack1ll111llll1_opy_ = bstack1111111l_opy_.on()
  bstack1ll11l111ll_opy_ = bstack1l1l1l11_opy_.on()
  bstack1ll111ll1l1_opy_ = percy.bstack1ll11lll11_opy_()
  if bstack1ll111ll1l1_opy_ and not bstack1ll11l111ll_opy_ and not bstack1ll111llll1_opy_:
    return bstack11l1111111_opy_ not in [bstack111l1ll_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫ᠐"), bstack111l1ll_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ᠑")]
  elif bstack1ll111llll1_opy_ and not bstack1ll11l111ll_opy_:
    return bstack11l1111111_opy_ not in [bstack111l1ll_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ᠒"), bstack111l1ll_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ᠓"), bstack111l1ll_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨ᠔")]
  return bstack1ll111llll1_opy_ or bstack1ll11l111ll_opy_ or bstack1ll111ll1l1_opy_
@bstack11l1111l_opy_(class_method=False)
def bstack1ll11lll11l_opy_(bstack11l1111111_opy_, test=None):
  bstack1ll111lllll_opy_ = bstack1111111l_opy_.on()
  if not bstack1ll111lllll_opy_ or bstack11l1111111_opy_ not in [bstack111l1ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ᠕")] or test == None:
    return None
  return {
    bstack111l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭᠖"): bstack1ll111lllll_opy_ and bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭᠗"), None) == True and bstack1111111l_opy_.bstack1l111l1l1l_opy_(test[bstack111l1ll_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭᠘")])
  }