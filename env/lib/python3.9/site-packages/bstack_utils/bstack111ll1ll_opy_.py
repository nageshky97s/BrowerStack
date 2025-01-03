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
import requests
import logging
import threading
from urllib.parse import urlparse
from bstack_utils.constants import bstack111llll1l1_opy_ as bstack111lll11ll_opy_
from bstack_utils.bstack1ll1l1l11l_opy_ import bstack1ll1l1l11l_opy_
from bstack_utils.helper import bstack1l1lllll_opy_, bstack1l11lll1_opy_, bstack11ll1lll1_opy_, bstack111ll1ll1l_opy_, bstack111lll111l_opy_, bstack11l1l111l_opy_, get_host_info, bstack111ll111l1_opy_, bstack11l11l1111_opy_, bstack11l1111l_opy_
from browserstack_sdk._version import __version__
logger = logging.getLogger(__name__)
@bstack11l1111l_opy_(class_method=False)
def _111l1llll1_opy_(driver, bstack1llllll11_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack111l1ll_opy_ (u"ࠬࡵࡳࡠࡰࡤࡱࡪ࠭ླྀ"): caps.get(bstack111l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠬཹ"), None),
        bstack111l1ll_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱེࠫ"): bstack1llllll11_opy_.get(bstack111l1ll_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱཻࠫ"), None),
        bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡲࡦࡳࡥࠨོ"): caps.get(bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨཽ"), None),
        bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ཾ"): caps.get(bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ཿ"), None)
    }
  except Exception as error:
    logger.debug(bstack111l1ll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡧࡩࡹࡧࡩ࡭ࡵࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸࠠ࠻ྀࠢࠪ") + str(error))
  return response
def on():
    if os.environ.get(bstack111l1ll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘཱྀࠬ"), None) is None or os.environ[bstack111l1ll_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ྂ")] == bstack111l1ll_opy_ (u"ࠤࡱࡹࡱࡲࠢྃ"):
        return False
    return True
def bstack111lll11l1_opy_(config):
  return config.get(bstack111l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻ྄ࠪ"), False) or any([p.get(bstack111l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ྅"), False) == True for p in config.get(bstack111l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ྆"), [])])
def bstack11ll11l1l_opy_(config, bstack1l11l1111l_opy_):
  try:
    if not bstack11ll1lll1_opy_(config):
      return False
    bstack111lll1111_opy_ = config.get(bstack111l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭྇"), False)
    if int(bstack1l11l1111l_opy_) < len(config.get(bstack111l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪྈ"), [])) and config[bstack111l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫྉ")][bstack1l11l1111l_opy_]:
      bstack111ll11l11_opy_ = config[bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬྊ")][bstack1l11l1111l_opy_].get(bstack111l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪྋ"), None)
    else:
      bstack111ll11l11_opy_ = config.get(bstack111l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫྌ"), None)
    if bstack111ll11l11_opy_ != None:
      bstack111lll1111_opy_ = bstack111ll11l11_opy_
    bstack111ll1l1ll_opy_ = os.getenv(bstack111l1ll_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪྍ")) is not None and len(os.getenv(bstack111l1ll_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫྎ"))) > 0 and os.getenv(bstack111l1ll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬྏ")) != bstack111l1ll_opy_ (u"ࠨࡰࡸࡰࡱ࠭ྐ")
    return bstack111lll1111_opy_ and bstack111ll1l1ll_opy_
  except Exception as error:
    logger.debug(bstack111l1ll_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡨࡶ࡮࡬ࡹࡪࡰࡪࠤࡹ࡮ࡥࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࠦ࠺ࠡࠩྑ") + str(error))
  return False
def bstack1l111l1l1l_opy_(test_tags):
  bstack111lll1l1l_opy_ = os.getenv(bstack111l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫྒ"))
  if bstack111lll1l1l_opy_ is None:
    return True
  bstack111lll1l1l_opy_ = json.loads(bstack111lll1l1l_opy_)
  try:
    include_tags = bstack111lll1l1l_opy_[bstack111l1ll_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩྒྷ")] if bstack111l1ll_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪྔ") in bstack111lll1l1l_opy_ and isinstance(bstack111lll1l1l_opy_[bstack111l1ll_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫྕ")], list) else []
    exclude_tags = bstack111lll1l1l_opy_[bstack111l1ll_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬྖ")] if bstack111l1ll_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ྗ") in bstack111lll1l1l_opy_ and isinstance(bstack111lll1l1l_opy_[bstack111l1ll_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ྘")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack111l1ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡸࡤࡰ࡮ࡪࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡨࡥࡧࡱࡵࡩࠥࡹࡣࡢࡰࡱ࡭ࡳ࡭࠮ࠡࡇࡵࡶࡴࡸࠠ࠻ࠢࠥྙ") + str(error))
  return False
def bstack111llll111_opy_(config, bstack111ll1llll_opy_, bstack111ll1ll11_opy_, bstack111ll1l11l_opy_):
  bstack111ll1l111_opy_ = bstack111ll1ll1l_opy_(config)
  bstack111lll1ll1_opy_ = bstack111lll111l_opy_(config)
  if bstack111ll1l111_opy_ is None or bstack111lll1ll1_opy_ is None:
    logger.error(bstack111l1ll_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡲࡶࡰࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥࡧࡵࡵࡪࡨࡲࡹ࡯ࡣࡢࡶ࡬ࡳࡳࠦࡴࡰ࡭ࡨࡲࠬྚ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack111l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ྛ"), bstack111l1ll_opy_ (u"࠭ࡻࡾࠩྜ")))
    data = {
        bstack111l1ll_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬྜྷ"): config[bstack111l1ll_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ྞ")],
        bstack111l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬྟ"): config.get(bstack111l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ྠ"), os.path.basename(os.getcwd())),
        bstack111l1ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡗ࡭ࡲ࡫ࠧྡ"): bstack1l1lllll_opy_(),
        bstack111l1ll_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪྡྷ"): config.get(bstack111l1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡉ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩྣ"), bstack111l1ll_opy_ (u"ࠧࠨྤ")),
        bstack111l1ll_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨྥ"): {
            bstack111l1ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡓࡧ࡭ࡦࠩྦ"): bstack111ll1llll_opy_,
            bstack111l1ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ྦྷ"): bstack111ll1ll11_opy_,
            bstack111l1ll_opy_ (u"ࠫࡸࡪ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨྨ"): __version__,
            bstack111l1ll_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧྩ"): bstack111l1ll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ྪ"),
            bstack111l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧྫ"): bstack111l1ll_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࠪྫྷ"),
            bstack111l1ll_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩྭ"): bstack111ll1l11l_opy_
        },
        bstack111l1ll_opy_ (u"ࠪࡷࡪࡺࡴࡪࡰࡪࡷࠬྮ"): settings,
        bstack111l1ll_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࡈࡵ࡮ࡵࡴࡲࡰࠬྯ"): bstack111ll111l1_opy_(),
        bstack111l1ll_opy_ (u"ࠬࡩࡩࡊࡰࡩࡳࠬྰ"): bstack11l1l111l_opy_(),
        bstack111l1ll_opy_ (u"࠭ࡨࡰࡵࡷࡍࡳ࡬࡯ࠨྱ"): get_host_info(),
        bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩྲ"): bstack11ll1lll1_opy_(config)
    }
    headers = {
        bstack111l1ll_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧླ"): bstack111l1ll_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬྴ"),
    }
    config = {
        bstack111l1ll_opy_ (u"ࠪࡥࡺࡺࡨࠨྵ"): (bstack111ll1l111_opy_, bstack111lll1ll1_opy_),
        bstack111l1ll_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬྶ"): headers
    }
    response = bstack11l11l1111_opy_(bstack111l1ll_opy_ (u"ࠬࡖࡏࡔࡖࠪྷ"), bstack111lll11ll_opy_ + bstack111l1ll_opy_ (u"࠭࠯ࡷ࠴࠲ࡸࡪࡹࡴࡠࡴࡸࡲࡸ࠭ྸ"), data, config)
    bstack111ll1111l_opy_ = response.json()
    if bstack111ll1111l_opy_[bstack111l1ll_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨྐྵ")]:
      parsed = json.loads(os.getenv(bstack111l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩྺ"), bstack111l1ll_opy_ (u"ࠩࡾࢁࠬྻ")))
      parsed[bstack111l1ll_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫྼ")] = bstack111ll1111l_opy_[bstack111l1ll_opy_ (u"ࠫࡩࡧࡴࡢࠩ྽")][bstack111l1ll_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭྾")]
      os.environ[bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ྿")] = json.dumps(parsed)
      bstack1ll1l1l11l_opy_.bstack111ll111ll_opy_(bstack111ll1111l_opy_[bstack111l1ll_opy_ (u"ࠧࡥࡣࡷࡥࠬ࿀")][bstack111l1ll_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩ࿁")])
      bstack1ll1l1l11l_opy_.bstack111l1ll1ll_opy_(bstack111ll1111l_opy_[bstack111l1ll_opy_ (u"ࠩࡧࡥࡹࡧࠧ࿂")][bstack111l1ll_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷࠬ࿃")])
      bstack1ll1l1l11l_opy_.store()
      return bstack111ll1111l_opy_[bstack111l1ll_opy_ (u"ࠫࡩࡧࡴࡢࠩ࿄")][bstack111l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࡙ࡵ࡫ࡦࡰࠪ࿅")], bstack111ll1111l_opy_[bstack111l1ll_opy_ (u"࠭ࡤࡢࡶࡤ࿆ࠫ")][bstack111l1ll_opy_ (u"ࠧࡪࡦࠪ࿇")]
    else:
      logger.error(bstack111l1ll_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡶࡺࡴ࡮ࡪࡰࡪࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࠩ࿈") + bstack111ll1111l_opy_[bstack111l1ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ࿉")])
      if bstack111ll1111l_opy_[bstack111l1ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ࿊")] == bstack111l1ll_opy_ (u"ࠫࡎࡴࡶࡢ࡮࡬ࡨࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥࡶࡡࡴࡵࡨࡨ࠳࠭࿋"):
        for bstack111l1lllll_opy_ in bstack111ll1111l_opy_[bstack111l1ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬ࿌")]:
          logger.error(bstack111l1lllll_opy_[bstack111l1ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ࿍")])
      return None, None
  except Exception as error:
    logger.error(bstack111l1ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡵࡹࡳࠦࡦࡰࡴࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡀࠠࠣ࿎") +  str(error))
    return None, None
def bstack111ll11l1l_opy_():
  if os.getenv(bstack111l1ll_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭࿏")) is None:
    return {
        bstack111l1ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ࿐"): bstack111l1ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ࿑"),
        bstack111l1ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ࿒"): bstack111l1ll_opy_ (u"ࠬࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡨࡢࡦࠣࡪࡦ࡯࡬ࡦࡦ࠱ࠫ࿓")
    }
  data = {bstack111l1ll_opy_ (u"࠭ࡥ࡯ࡦࡗ࡭ࡲ࡫ࠧ࿔"): bstack1l1lllll_opy_()}
  headers = {
      bstack111l1ll_opy_ (u"ࠧࡂࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧ࿕"): bstack111l1ll_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࠩ࿖") + os.getenv(bstack111l1ll_opy_ (u"ࠤࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠢ࿗")),
      bstack111l1ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ࿘"): bstack111l1ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ࿙")
  }
  response = bstack11l11l1111_opy_(bstack111l1ll_opy_ (u"ࠬࡖࡕࡕࠩ࿚"), bstack111lll11ll_opy_ + bstack111l1ll_opy_ (u"࠭࠯ࡵࡧࡶࡸࡤࡸࡵ࡯ࡵ࠲ࡷࡹࡵࡰࠨ࿛"), data, { bstack111l1ll_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ࿜"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack111l1ll_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤ࡙࡫ࡳࡵࠢࡕࡹࡳࠦ࡭ࡢࡴ࡮ࡩࡩࠦࡡࡴࠢࡦࡳࡲࡶ࡬ࡦࡶࡨࡨࠥࡧࡴࠡࠤ࿝") + bstack1l11lll1_opy_().isoformat() + bstack111l1ll_opy_ (u"ࠩ࡝ࠫ࿞"))
      return {bstack111l1ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ࿟"): bstack111l1ll_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ࿠"), bstack111l1ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭࿡"): bstack111l1ll_opy_ (u"࠭ࠧ࿢")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack111l1ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡧࡴࡳࡰ࡭ࡧࡷ࡭ࡴࡴࠠࡰࡨࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡔࡦࡵࡷࠤࡗࡻ࡮࠻ࠢࠥ࿣") + str(error))
    return {
        bstack111l1ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ࿤"): bstack111l1ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ࿥"),
        bstack111l1ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ࿦"): str(error)
    }
def bstack11l1111l11_opy_(caps, options, desired_capabilities={}):
  try:
    bstack111lll1l11_opy_ = caps.get(bstack111l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ࿧"), {}).get(bstack111l1ll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩ࿨"), caps.get(bstack111l1ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭࿩"), bstack111l1ll_opy_ (u"ࠧࠨ࿪")))
    if bstack111lll1l11_opy_:
      logger.warn(bstack111l1ll_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡆࡨࡷࡰࡺ࡯ࡱࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧ࿫"))
      return False
    if options:
      bstack111ll1l1l1_opy_ = options.to_capabilities()
    elif desired_capabilities:
      bstack111ll1l1l1_opy_ = desired_capabilities
    else:
      bstack111ll1l1l1_opy_ = {}
    browser = caps.get(bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ࿬"), bstack111l1ll_opy_ (u"ࠪࠫ࿭")).lower() or bstack111ll1l1l1_opy_.get(bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ࿮"), bstack111l1ll_opy_ (u"ࠬ࠭࿯")).lower()
    if browser != bstack111l1ll_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭࿰"):
      logger.warn(bstack111l1ll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡄࡪࡵࡳࡲ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࡴ࠰ࠥ࿱"))
      return False
    browser_version = caps.get(bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ࿲")) or caps.get(bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ࿳")) or bstack111ll1l1l1_opy_.get(bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ࿴")) or bstack111ll1l1l1_opy_.get(bstack111l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ࿵"), {}).get(bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭࿶")) or bstack111ll1l1l1_opy_.get(bstack111l1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ࿷"), {}).get(bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ࿸"))
    if browser_version and browser_version != bstack111l1ll_opy_ (u"ࠨ࡮ࡤࡸࡪࡹࡴࠨ࿹") and int(browser_version.split(bstack111l1ll_opy_ (u"ࠩ࠱ࠫ࿺"))[0]) <= 98:
      logger.warn(bstack111l1ll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥ࡭ࡲࡦࡣࡷࡩࡷࠦࡴࡩࡣࡱࠤ࠾࠾࠮ࠣ࿻"))
      return False
    if not options:
      bstack111l1lll11_opy_ = caps.get(bstack111l1ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ࿼")) or bstack111ll1l1l1_opy_.get(bstack111l1ll_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ࿽"), {})
      if bstack111l1ll_opy_ (u"࠭࠭࠮ࡪࡨࡥࡩࡲࡥࡴࡵࠪ࿾") in bstack111l1lll11_opy_.get(bstack111l1ll_opy_ (u"ࠧࡢࡴࡪࡷࠬ࿿"), []):
        logger.warn(bstack111l1ll_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡲࡴࡺࠠࡳࡷࡱࠤࡴࡴࠠ࡭ࡧࡪࡥࡨࡿࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠡࡕࡺ࡭ࡹࡩࡨࠡࡶࡲࠤࡳ࡫ࡷࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥࠡࡱࡵࠤࡦࡼ࡯ࡪࡦࠣࡹࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠥက"))
        return False
    return True
  except Exception as error:
    logger.debug(bstack111l1ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡤࡰ࡮ࡪࡡࡵࡧࠣࡥ࠶࠷ࡹࠡࡵࡸࡴࡵࡵࡲࡵࠢ࠽ࠦခ") + str(error))
    return False
def set_capabilities(caps, config):
  try:
    bstack111ll1lll1_opy_ = config.get(bstack111l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪဂ"), {})
    bstack111ll1lll1_opy_[bstack111l1ll_opy_ (u"ࠫࡦࡻࡴࡩࡖࡲ࡯ࡪࡴࠧဃ")] = os.getenv(bstack111l1ll_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪင"))
    bstack111lll1lll_opy_ = json.loads(os.getenv(bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧစ"), bstack111l1ll_opy_ (u"ࠧࡼࡿࠪဆ"))).get(bstack111l1ll_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩဇ"))
    caps[bstack111l1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩဈ")] = True
    if bstack111l1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫဉ") in caps:
      caps[bstack111l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬည")][bstack111l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬဋ")] = bstack111ll1lll1_opy_
      caps[bstack111l1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧဌ")][bstack111l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧဍ")][bstack111l1ll_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩဎ")] = bstack111lll1lll_opy_
    else:
      caps[bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨဏ")] = bstack111ll1lll1_opy_
      caps[bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩတ")][bstack111l1ll_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬထ")] = bstack111lll1lll_opy_
  except Exception as error:
    logger.debug(bstack111l1ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶ࠲ࠥࡋࡲࡳࡱࡵ࠾ࠥࠨဒ") +  str(error))
def bstack11l111l1l_opy_(driver, bstack111llll11l_opy_):
  try:
    setattr(driver, bstack111l1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭ဓ"), True)
    session = driver.session_id
    if session:
      bstack111ll11ll1_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack111ll11ll1_opy_ = False
      bstack111ll11ll1_opy_ = url.scheme in [bstack111l1ll_opy_ (u"ࠢࡩࡶࡷࡴࠧန"), bstack111l1ll_opy_ (u"ࠣࡪࡷࡸࡵࡹࠢပ")]
      if bstack111ll11ll1_opy_:
        if bstack111llll11l_opy_:
          logger.info(bstack111l1ll_opy_ (u"ࠤࡖࡩࡹࡻࡰࠡࡨࡲࡶࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡨࡢࡵࠣࡷࡹࡧࡲࡵࡧࡧ࠲ࠥࡇࡵࡵࡱࡰࡥࡹ࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡧ࡫ࡧࡪࡰࠣࡱࡴࡳࡥ࡯ࡶࡤࡶ࡮ࡲࡹ࠯ࠤဖ"))
      return bstack111llll11l_opy_
  except Exception as e:
    logger.error(bstack111l1ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡦࡸࡴࡪࡰࡪࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡦࡥࡳࠦࡦࡰࡴࠣࡸ࡭࡯ࡳࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨဗ") + str(e))
    return False
def bstack111l1111_opy_(driver, name, path):
  try:
    bstack111l1lll1l_opy_ = {
        bstack111l1ll_opy_ (u"ࠫࡹ࡮ࡔࡦࡵࡷࡖࡺࡴࡕࡶ࡫ࡧࠫဘ"): threading.current_thread().current_test_uuid,
        bstack111l1ll_opy_ (u"ࠬࡺࡨࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪမ"): os.environ.get(bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫယ"), bstack111l1ll_opy_ (u"ࠧࠨရ")),
        bstack111l1ll_opy_ (u"ࠨࡶ࡫ࡎࡼࡺࡔࡰ࡭ࡨࡲࠬလ"): os.environ.get(bstack111l1ll_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪဝ"), bstack111l1ll_opy_ (u"ࠪࠫသ"))
    }
    logger.debug(bstack111l1ll_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡢࡸ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠧဟ"))
    logger.debug(driver.execute_async_script(bstack1ll1l1l11l_opy_.perform_scan, {bstack111l1ll_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࠧဠ"): name}))
    logger.debug(driver.execute_async_script(bstack1ll1l1l11l_opy_.bstack111ll11lll_opy_, bstack111l1lll1l_opy_))
    logger.info(bstack111l1ll_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡮ࡡࡴࠢࡨࡲࡩ࡫ࡤ࠯ࠤအ"))
  except Exception as bstack111ll11111_opy_:
    logger.error(bstack111l1ll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡥࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡧ࡫ࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡪࡴࡸࠠࡵࡪࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫࠺ࠡࠤဢ") + str(path) + bstack111l1ll_opy_ (u"ࠣࠢࡈࡶࡷࡵࡲࠡ࠼ࠥဣ") + str(bstack111ll11111_opy_))