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
import atexit
import os
import signal
import sys
import yaml
import requests
import logging
import threading
import socket
import datetime
import string
import random
import json
import collections.abc
import re
import multiprocessing
import traceback
import copy
import tempfile
from packaging import version
from uuid import uuid4
from browserstack.local import Local
from urllib.parse import urlparse
from dotenv import load_dotenv
from bstack_utils.constants import *
from bstack_utils.percy import *
from browserstack_sdk.bstack1lllll11_opy_ import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack11l11l11l1_opy_ import bstack11ll1l11ll_opy_
import time
import requests
def bstack11lllll111_opy_():
  global CONFIG
  headers = {
        bstack111l1ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩ৛"): bstack111l1ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧড়"),
      }
  proxies = bstack1l1l1l1ll_opy_(CONFIG, bstack1ll1lll1ll_opy_)
  try:
    response = requests.get(bstack1ll1lll1ll_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack11l1llll1_opy_ = response.json()[bstack111l1ll_opy_ (u"ࠬ࡮ࡵࡣࡵࠪঢ়")]
      logger.debug(bstack1llll1l111_opy_.format(response.json()))
      return bstack11l1llll1_opy_
    else:
      logger.debug(bstack1ll111ll11_opy_.format(bstack111l1ll_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧ৞")))
  except Exception as e:
    logger.debug(bstack1ll111ll11_opy_.format(e))
def bstack1l1l11lll_opy_(hub_url):
  global CONFIG
  url = bstack111l1ll_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤয়")+  hub_url + bstack111l1ll_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣৠ")
  headers = {
        bstack111l1ll_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨৡ"): bstack111l1ll_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ৢ"),
      }
  proxies = bstack1l1l1l1ll_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack11llll1l1_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1llll11111_opy_.format(hub_url, e))
def bstack1l111llll1_opy_():
  try:
    global bstack11111l1l1_opy_
    bstack11l1llll1_opy_ = bstack11lllll111_opy_()
    bstack1l111lll1l_opy_ = []
    results = []
    for bstack11ll1l1l1_opy_ in bstack11l1llll1_opy_:
      bstack1l111lll1l_opy_.append(bstack111lllll_opy_(target=bstack1l1l11lll_opy_,args=(bstack11ll1l1l1_opy_,)))
    for t in bstack1l111lll1l_opy_:
      t.start()
    for t in bstack1l111lll1l_opy_:
      results.append(t.join())
    bstack1ll111lll_opy_ = {}
    for item in results:
      hub_url = item[bstack111l1ll_opy_ (u"ࠫ࡭ࡻࡢࡠࡷࡵࡰࠬৣ")]
      latency = item[bstack111l1ll_opy_ (u"ࠬࡲࡡࡵࡧࡱࡧࡾ࠭৤")]
      bstack1ll111lll_opy_[hub_url] = latency
    bstack1l111111ll_opy_ = min(bstack1ll111lll_opy_, key= lambda x: bstack1ll111lll_opy_[x])
    bstack11111l1l1_opy_ = bstack1l111111ll_opy_
    logger.debug(bstack1ll1l111l1_opy_.format(bstack1l111111ll_opy_))
  except Exception as e:
    logger.debug(bstack1lll1l1l1l_opy_.format(e))
from bstack_utils.messages import *
from bstack_utils import bstack1llllll1l1_opy_
from bstack_utils.config import Config
from bstack_utils.helper import bstack11ll1111l_opy_, bstack11l11l1111_opy_, bstack11lll1l1l_opy_, bstack1ll111l1_opy_, bstack11ll1lll1_opy_, \
  Notset, bstack1l1lll1ll_opy_, \
  bstack1llllllll1_opy_, bstack11ll11l11l_opy_, bstack11l1llll1l_opy_, bstack11l1l111l_opy_, bstack1l1lll111l_opy_, bstack1l1ll11l1_opy_, \
  bstack1llll1llll_opy_, \
  bstack11ll1l111l_opy_, bstack1lll1ll11l_opy_, bstack1l1l111l1l_opy_, bstack1lll1llll_opy_, \
  bstack111l1ll11_opy_, bstack1l111l111l_opy_, bstack1l1l111lll_opy_, bstack1lllll1111_opy_
from bstack_utils.bstack1ll11l1l1_opy_ import bstack11ll11111l_opy_
from bstack_utils.bstack1ll111l1ll_opy_ import bstack11l11l1ll1_opy_
from bstack_utils.bstack1l1l1l11ll_opy_ import bstack11ll111l1l_opy_, bstack1l1l1lll1l_opy_
from bstack_utils.bstack1l1lll11_opy_ import bstack1ll11l1l_opy_
from bstack_utils.bstack1ll11l11_opy_ import bstack1l1l1l11_opy_
from bstack_utils.bstack1ll1l1l11l_opy_ import bstack1ll1l1l11l_opy_
from bstack_utils.proxy import bstack11111l1ll_opy_, bstack1l1l1l1ll_opy_, bstack111111ll1_opy_, bstack1l1l11ll11_opy_
import bstack_utils.bstack111ll1ll_opy_ as bstack1111111l_opy_
from browserstack_sdk.bstack1111ll1l_opy_ import *
from browserstack_sdk.bstack11l11111_opy_ import *
from bstack_utils.bstack1l11ll111l_opy_ import bstack11l1ll1ll_opy_
from browserstack_sdk.bstack1lll11ll_opy_ import *
import requests
from bstack_utils.constants import *
def bstack1l1l1111l_opy_():
    global bstack11111l1l1_opy_
    try:
        bstack11l1l11lll_opy_ = bstack1ll1lllll1_opy_()
        bstack1lll11l1l1_opy_(bstack11l1l11lll_opy_)
        hub_url = bstack11l1l11lll_opy_.get(bstack111l1ll_opy_ (u"ࠨࡵࡳ࡮ࠥ৥"), bstack111l1ll_opy_ (u"ࠢࠣ০"))
        if hub_url.endswith(bstack111l1ll_opy_ (u"ࠨ࠱ࡺࡨ࠴࡮ࡵࡣࠩ১")):
            hub_url = hub_url.rsplit(bstack111l1ll_opy_ (u"ࠩ࠲ࡻࡩ࠵ࡨࡶࡤࠪ২"), 1)[0]
        if hub_url.startswith(bstack111l1ll_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࠫ৩")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack111l1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴࠭৪")):
            hub_url = hub_url[8:]
        bstack11111l1l1_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack1ll1lllll1_opy_():
    global CONFIG
    bstack1l111l111_opy_ = CONFIG.get(bstack111l1ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ৫"), {}).get(bstack111l1ll_opy_ (u"࠭ࡧࡳ࡫ࡧࡒࡦࡳࡥࠨ৬"), bstack111l1ll_opy_ (u"ࠧࡏࡑࡢࡋࡗࡏࡄࡠࡐࡄࡑࡊࡥࡐࡂࡕࡖࡉࡉ࠭৭"))
    if not isinstance(bstack1l111l111_opy_, str):
        raise ValueError(bstack111l1ll_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡈࡴ࡬ࡨࠥࡴࡡ࡮ࡧࠣࡱࡺࡹࡴࠡࡤࡨࠤࡦࠦࡶࡢ࡮࡬ࡨࠥࡹࡴࡳ࡫ࡱ࡫ࠧ৮"))
    try:
        bstack11l1l11lll_opy_ = bstack11l1l11ll_opy_(bstack1l111l111_opy_)
        return bstack11l1l11lll_opy_
    except Exception as e:
        logger.error(bstack111l1ll_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣ৯").format(str(e)))
        return {}
def bstack11l1l11ll_opy_(bstack1l111l111_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack111l1ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬৰ")] or not CONFIG[bstack111l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧৱ")]:
            raise ValueError(bstack111l1ll_opy_ (u"ࠧࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡻࡳࡦࡴࡱࡥࡲ࡫ࠠࡰࡴࠣࡥࡨࡩࡥࡴࡵࠣ࡯ࡪࡿࠢ৲"))
        url = bstack1lll111l11_opy_ + bstack1l111l111_opy_
        auth = (CONFIG[bstack111l1ll_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ৳")], CONFIG[bstack111l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ৴")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack1lllll11l1_opy_ = json.loads(response.text)
            return bstack1lllll11l1_opy_
    except ValueError as ve:
        logger.error(bstack111l1ll_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣ৵").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack111l1ll_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥ࡭ࡲࡪࡦࠣࡨࡪࡺࡡࡪ࡮ࡶࠤ࠿ࠦࡻࡾࠤ৶").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack1lll11l1l1_opy_(bstack1ll1lll111_opy_):
    global CONFIG
    if bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ৷") not in CONFIG or str(CONFIG[bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ৸")]).lower() == bstack111l1ll_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ৹"):
        CONFIG[bstack111l1ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬ৺")] = False
    elif bstack111l1ll_opy_ (u"ࠧࡪࡵࡗࡶ࡮ࡧ࡬ࡈࡴ࡬ࡨࠬ৻") in bstack1ll1lll111_opy_:
        bstack1lll11lll1_opy_ = CONFIG.get(bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬৼ"), {})
        logger.debug(bstack111l1ll_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡰࡴࡩࡡ࡭ࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࠪࡹࠢ৽"), bstack1lll11lll1_opy_)
        bstack11ll1lllll_opy_ = bstack1ll1lll111_opy_.get(bstack111l1ll_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯ࡕࡩࡵ࡫ࡡࡵࡧࡵࡷࠧ৾"), [])
        bstack11l1l1llll_opy_ = bstack111l1ll_opy_ (u"ࠦ࠱ࠨ৿").join(bstack11ll1lllll_opy_)
        logger.debug(bstack111l1ll_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡈࡻࡳࡵࡱࡰࠤࡷ࡫ࡰࡦࡣࡷࡩࡷࠦࡳࡵࡴ࡬ࡲ࡬ࡀࠠࠦࡵࠥ਀"), bstack11l1l1llll_opy_)
        bstack11lll11l11_opy_ = {
            bstack111l1ll_opy_ (u"ࠨ࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣਁ"): bstack111l1ll_opy_ (u"ࠢࡢࡶࡶ࠱ࡷ࡫ࡰࡦࡣࡷࡩࡷࠨਂ"),
            bstack111l1ll_opy_ (u"ࠣࡨࡲࡶࡨ࡫ࡌࡰࡥࡤࡰࠧਃ"): bstack111l1ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ਄"),
            bstack111l1ll_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࠰ࡶࡪࡶࡥࡢࡶࡨࡶࠧਅ"): bstack11l1l1llll_opy_
        }
        bstack1lll11lll1_opy_.update(bstack11lll11l11_opy_)
        logger.debug(bstack111l1ll_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼࡙ࠣࡵࡪࡡࡵࡧࡧࠤࡱࡵࡣࡢ࡮ࠣࡳࡵࡺࡩࡰࡰࡶ࠾ࠥࠫࡳࠣਆ"), bstack1lll11lll1_opy_)
        CONFIG[bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩਇ")] = bstack1lll11lll1_opy_
        logger.debug(bstack111l1ll_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡌࡩ࡯ࡣ࡯ࠤࡈࡕࡎࡇࡋࡊ࠾ࠥࠫࡳࠣਈ"), CONFIG)
def bstack11ll11ll1l_opy_():
    bstack11l1l11lll_opy_ = bstack1ll1lllll1_opy_()
    if not bstack11l1l11lll_opy_[bstack111l1ll_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࡙ࡷࡲࠧਉ")]:
      raise ValueError(bstack111l1ll_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࡚ࡸ࡬ࠡ࡫ࡶࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࡬ࡲࡰ࡯ࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴ࠰ࠥਊ"))
    return bstack11l1l11lll_opy_[bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࡛ࡲ࡭ࠩ਋")] + bstack111l1ll_opy_ (u"ࠪࡃࡨࡧࡰࡴ࠿ࠪ਌")
def bstack1l1ll1l11_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack111l1ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭਍")], CONFIG[bstack111l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ਎")])
        url = bstack1l11ll1ll_opy_
        logger.debug(bstack111l1ll_opy_ (u"ࠨࡁࡵࡶࡨࡱࡵࡺࡩ࡯ࡩࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷࠥ࡬ࡲࡰ࡯ࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡗࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࠦࡁࡑࡋࠥਏ"))
        try:
            response = requests.get(url, auth=auth, headers={bstack111l1ll_opy_ (u"ࠢࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪࠨਐ"): bstack111l1ll_opy_ (u"ࠣࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠦ਑")})
            if response.status_code == 200:
                bstack1lll11l11_opy_ = json.loads(response.text)
                bstack11l11111l1_opy_ = bstack1lll11l11_opy_.get(bstack111l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡴࠩ਒"), [])
                if bstack11l11111l1_opy_:
                    bstack111lllllll_opy_ = bstack11l11111l1_opy_[0]
                    bstack1ll1llllll_opy_ = bstack111lllllll_opy_.get(bstack111l1ll_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ਓ"))
                    bstack1ll1111l1l_opy_ = bstack11l11l1ll_opy_ + bstack1ll1llllll_opy_
                    result.extend([bstack1ll1llllll_opy_, bstack1ll1111l1l_opy_])
                    logger.info(bstack1lll1llll1_opy_.format(bstack1ll1111l1l_opy_))
                    bstack111lll11l_opy_ = CONFIG[bstack111l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧਔ")]
                    if bstack111l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧਕ") in CONFIG:
                      bstack111lll11l_opy_ += bstack111l1ll_opy_ (u"࠭ࠠࠨਖ") + CONFIG[bstack111l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩਗ")]
                    if bstack111lll11l_opy_ != bstack111lllllll_opy_.get(bstack111l1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ਘ")):
                      logger.debug(bstack1l11l1lll1_opy_.format(bstack111lllllll_opy_.get(bstack111l1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧਙ")), bstack111lll11l_opy_))
                    return result
                else:
                    logger.debug(bstack111l1ll_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡑࡳࠥࡨࡵࡪ࡮ࡧࡷࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡵࡪࡨࠤࡷ࡫ࡳࡱࡱࡱࡷࡪ࠴ࠢਚ"))
            else:
                logger.debug(bstack111l1ll_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷ࠳ࠨਛ"))
        except Exception as e:
            logger.error(bstack111l1ll_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࡹࠠ࠻ࠢࡾࢁࠧਜ").format(str(e)))
    else:
        logger.debug(bstack111l1ll_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡉࡏࡏࡈࡌࡋࠥ࡯ࡳࠡࡰࡲࡸࠥࡹࡥࡵ࠰࡙ࠣࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷ࠳ࠨਝ"))
    return [None, None]
import bstack_utils.bstack1l1l1111l1_opy_ as bstack11lll1111l_opy_
import bstack_utils.bstack11ll11llll_opy_ as bstack11l1lll1l1_opy_
bstack1lll1lllll_opy_ = bstack111l1ll_opy_ (u"ࠧࠡࠢ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࠠࠡ࡫ࡩࠬࡵࡧࡧࡦࠢࡀࡁࡂࠦࡶࡰ࡫ࡧࠤ࠵࠯ࠠࡼ࡞ࡱࠤࠥࠦࡴࡳࡻࡾࡠࡳࠦࡣࡰࡰࡶࡸࠥ࡬ࡳࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࡡ࠭ࡦࡴ࡞ࠪ࠭ࡀࡢ࡮ࠡࠢࠣࠤࠥ࡬ࡳ࠯ࡣࡳࡴࡪࡴࡤࡇ࡫࡯ࡩࡘࡿ࡮ࡤࠪࡥࡷࡹࡧࡣ࡬ࡡࡳࡥࡹ࡮ࠬࠡࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡳࡣ࡮ࡴࡤࡦࡺࠬࠤ࠰ࠦࠢ࠻ࠤࠣ࠯ࠥࡐࡓࡐࡐ࠱ࡷࡹࡸࡩ࡯ࡩ࡬ࡪࡾ࠮ࡊࡔࡑࡑ࠲ࡵࡧࡲࡴࡧࠫࠬࡦࡽࡡࡪࡶࠣࡲࡪࡽࡐࡢࡩࡨ࠶࠳࡫ࡶࡢ࡮ࡸࡥࡹ࡫ࠨࠣࠪࠬࠤࡂࡄࠠࡼࡿࠥ࠰ࠥࡢࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡨࡧࡷࡗࡪࡹࡳࡪࡱࡱࡈࡪࡺࡡࡪ࡮ࡶࠦࢂࡢࠧࠪࠫࠬ࡟ࠧ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠣ࡟ࠬࠤ࠰ࠦࠢ࠭࡞࡟ࡲࠧ࠯࡜࡯ࠢࠣࠤࠥࢃࡣࡢࡶࡦ࡬࠭࡫ࡸࠪࡽ࡟ࡲࠥࠦࠠࠡࡿ࡟ࡲࠥࠦࡽ࡝ࡰࠣࠤ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵ࠧਞ")
bstack11111llll_opy_ = bstack111l1ll_opy_ (u"ࠨ࡞ࡱ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࡢ࡮ࡤࡱࡱࡷࡹࠦࡢࡴࡶࡤࡧࡰࡥࡰࡢࡶ࡫ࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳࡞࡞ࡱࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠴ࡡࡡࡴࡣࡰࡰࡶࡸࠥࡶ࡟ࡪࡰࡧࡩࡽࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠴ࡠࡠࡳࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡹ࡬ࡪࡥࡨࠬ࠵࠲ࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࠬࡠࡳࡩ࡯࡯ࡵࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬ࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ࠭ࡀࡢ࡮ࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯࠳ࡩࡨࡳࡱࡰ࡭ࡺࡳ࠮࡭ࡣࡸࡲࡨ࡮ࠠ࠾ࠢࡤࡷࡾࡴࡣࠡࠪ࡯ࡥࡺࡴࡣࡩࡑࡳࡸ࡮ࡵ࡮ࡴࠫࠣࡁࡃࠦࡻ࡝ࡰ࡯ࡩࡹࠦࡣࡢࡲࡶ࠿ࡡࡴࡴࡳࡻࠣࡿࡡࡴࡣࡢࡲࡶࠤࡂࠦࡊࡔࡑࡑ࠲ࡵࡧࡲࡴࡧࠫࡦࡸࡺࡡࡤ࡭ࡢࡧࡦࡶࡳࠪ࡞ࡱࠤࠥࢃࠠࡤࡣࡷࡧ࡭࠮ࡥࡹࠫࠣࡿࡡࡴࠠࠡࠢࠣࢁࡡࡴࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࡣࡺࡥ࡮ࡺࠠࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯࠳ࡩࡨࡳࡱࡰ࡭ࡺࡳ࠮ࡤࡱࡱࡲࡪࡩࡴࠩࡽ࡟ࡲࠥࠦࠠࠡࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸ࠿ࠦࡠࡸࡵࡶ࠾࠴࠵ࡣࡥࡲ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡂࡧࡦࡶࡳ࠾ࠦࡾࡩࡳࡩ࡯ࡥࡧࡘࡖࡎࡉ࡯࡮ࡲࡲࡲࡪࡴࡴࠩࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡦࡥࡵࡹࠩࠪࡿࡣ࠰ࡡࡴࠠࠡࠢࠣ࠲࠳࠴࡬ࡢࡷࡱࡧ࡭ࡕࡰࡵ࡫ࡲࡲࡸࡢ࡮ࠡࠢࢀ࠭ࡡࡴࡽ࡝ࡰ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࠧਟ")
from ._version import __version__
bstack1llll1l1ll_opy_ = None
CONFIG = {}
bstack11llllll1_opy_ = {}
bstack1111l1l11_opy_ = {}
bstack11l1lllll_opy_ = None
bstack11l111ll1_opy_ = None
bstack11lll1ll11_opy_ = None
bstack1l1111l1ll_opy_ = -1
bstack11l1ll11l_opy_ = 0
bstack1lllllll1l_opy_ = bstack1ll1l11lll_opy_
bstack1ll111ll1_opy_ = 1
bstack11l11l1l11_opy_ = False
bstack1l1llllll_opy_ = False
bstack111llllll1_opy_ = bstack111l1ll_opy_ (u"ࠩࠪਠ")
bstack1l111ll1l_opy_ = bstack111l1ll_opy_ (u"ࠪࠫਡ")
bstack1l11l1111_opy_ = False
bstack11ll1l111_opy_ = True
bstack1l1ll1lll_opy_ = bstack111l1ll_opy_ (u"ࠫࠬਢ")
bstack1ll111l11l_opy_ = []
bstack11111l1l1_opy_ = bstack111l1ll_opy_ (u"ࠬ࠭ਣ")
bstack111l11111_opy_ = False
bstack1l1l111ll_opy_ = None
bstack1l11l1llll_opy_ = None
bstack11l11l11ll_opy_ = None
bstack1llll11l11_opy_ = -1
bstack11l1111ll_opy_ = os.path.join(os.path.expanduser(bstack111l1ll_opy_ (u"࠭ࡾࠨਤ")), bstack111l1ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧਥ"), bstack111l1ll_opy_ (u"ࠨ࠰ࡵࡳࡧࡵࡴ࠮ࡴࡨࡴࡴࡸࡴ࠮ࡪࡨࡰࡵ࡫ࡲ࠯࡬ࡶࡳࡳ࠭ਦ"))
bstack1ll1lll11l_opy_ = 0
bstack1l1111ll1_opy_ = 0
bstack11l111l11l_opy_ = []
bstack1llll1ll11_opy_ = []
bstack11l11l111_opy_ = []
bstack1ll11llll_opy_ = []
bstack111llll1l_opy_ = bstack111l1ll_opy_ (u"ࠩࠪਧ")
bstack11llll111_opy_ = bstack111l1ll_opy_ (u"ࠪࠫਨ")
bstack111ll1l11_opy_ = False
bstack1l1l1lll11_opy_ = False
bstack1lllll111l_opy_ = {}
bstack1ll11ll11_opy_ = None
bstack11ll11lll1_opy_ = None
bstack11l11ll11l_opy_ = None
bstack11lll11l1_opy_ = None
bstack1lll11111_opy_ = None
bstack1l1ll111ll_opy_ = None
bstack1l1111lll1_opy_ = None
bstack1l1ll1ll1l_opy_ = None
bstack1l11l111ll_opy_ = None
bstack1ll11ll111_opy_ = None
bstack1l11l11l1_opy_ = None
bstack1ll11l1l11_opy_ = None
bstack1l1111llll_opy_ = None
bstack11lll1lll1_opy_ = None
bstack1llll1111l_opy_ = None
bstack11l11lll1l_opy_ = None
bstack1l1l11111l_opy_ = None
bstack11l1l111l1_opy_ = None
bstack1ll111lll1_opy_ = None
bstack1l1111ll1l_opy_ = None
bstack111111lll_opy_ = None
bstack1l111ll111_opy_ = None
bstack11ll1ll1l_opy_ = False
bstack11l1111l1l_opy_ = bstack111l1ll_opy_ (u"ࠦࠧ਩")
logger = bstack1llllll1l1_opy_.get_logger(__name__, bstack1lllllll1l_opy_)
bstack1111lll1_opy_ = Config.bstack11111lll_opy_()
percy = bstack1l111l1111_opy_()
bstack1lll11l111_opy_ = bstack11ll1l11ll_opy_()
bstack11l11ll11_opy_ = bstack1lll11ll_opy_()
def bstack1ll1l1111l_opy_():
  global CONFIG
  global bstack111ll1l11_opy_
  global bstack1111lll1_opy_
  bstack11l11l1lll_opy_ = bstack1ll1l1lll1_opy_(CONFIG)
  if bstack11ll1lll1_opy_(CONFIG):
    if (bstack111l1ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧਪ") in bstack11l11l1lll_opy_ and str(bstack11l11l1lll_opy_[bstack111l1ll_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨਫ")]).lower() == bstack111l1ll_opy_ (u"ࠧࡵࡴࡸࡩࠬਬ")):
      bstack111ll1l11_opy_ = True
    bstack1111lll1_opy_.bstack1ll111111_opy_(bstack11l11l1lll_opy_.get(bstack111l1ll_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬਭ"), False))
  else:
    bstack111ll1l11_opy_ = True
    bstack1111lll1_opy_.bstack1ll111111_opy_(True)
def bstack11lll11ll_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack11lll1111_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack11111111l_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack111l1ll_opy_ (u"ࠤ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡦࡳࡳ࡬ࡩࡨࡨ࡬ࡰࡪࠨਮ") == args[i].lower() or bstack111l1ll_opy_ (u"ࠥ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡮ࡧ࡫ࡪࠦਯ") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1l1ll1lll_opy_
      bstack1l1ll1lll_opy_ += bstack111l1ll_opy_ (u"ࠫ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡈࡵ࡮ࡧ࡫ࡪࡊ࡮ࡲࡥࠡࠩਰ") + path
      return path
  return None
bstack1ll111l11_opy_ = re.compile(bstack111l1ll_opy_ (u"ࡷࠨ࠮ࠫࡁ࡟ࠨࢀ࠮࠮ࠫࡁࠬࢁ࠳࠰࠿ࠣ਱"))
def bstack1l111l11ll_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1ll111l11_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack111l1ll_opy_ (u"ࠨࠤࡼࠤਲ") + group + bstack111l1ll_opy_ (u"ࠢࡾࠤਲ਼"), os.environ.get(group))
  return value
def bstack11l11ll111_opy_():
  bstack1l1l11llll_opy_ = bstack11111111l_opy_()
  if bstack1l1l11llll_opy_ and os.path.exists(os.path.abspath(bstack1l1l11llll_opy_)):
    fileName = bstack1l1l11llll_opy_
  if bstack111l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍ࡟ࡇࡋࡏࡉࠬ਴") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack111l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࡠࡈࡌࡐࡊ࠭ਵ")])) and not bstack111l1ll_opy_ (u"ࠪࡪ࡮ࡲࡥࡏࡣࡰࡩࠬਸ਼") in locals():
    fileName = os.environ[bstack111l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨ਷")]
  if bstack111l1ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡑࡥࡲ࡫ࠧਸ") in locals():
    bstack11111l_opy_ = os.path.abspath(fileName)
  else:
    bstack11111l_opy_ = bstack111l1ll_opy_ (u"࠭ࠧਹ")
  bstack1ll1ll1ll1_opy_ = os.getcwd()
  bstack1l1l111l1_opy_ = bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪ਺")
  bstack1ll11l11ll_opy_ = bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺࡣࡰࡰࠬ਻")
  while (not os.path.exists(bstack11111l_opy_)) and bstack1ll1ll1ll1_opy_ != bstack111l1ll_opy_ (u"ࠤ਼ࠥ"):
    bstack11111l_opy_ = os.path.join(bstack1ll1ll1ll1_opy_, bstack1l1l111l1_opy_)
    if not os.path.exists(bstack11111l_opy_):
      bstack11111l_opy_ = os.path.join(bstack1ll1ll1ll1_opy_, bstack1ll11l11ll_opy_)
    if bstack1ll1ll1ll1_opy_ != os.path.dirname(bstack1ll1ll1ll1_opy_):
      bstack1ll1ll1ll1_opy_ = os.path.dirname(bstack1ll1ll1ll1_opy_)
    else:
      bstack1ll1ll1ll1_opy_ = bstack111l1ll_opy_ (u"ࠥࠦ਽")
  if not os.path.exists(bstack11111l_opy_):
    bstack111ll1ll1_opy_(
      bstack11ll11lll_opy_.format(os.getcwd()))
  try:
    with open(bstack11111l_opy_, bstack111l1ll_opy_ (u"ࠫࡷ࠭ਾ")) as stream:
      yaml.add_implicit_resolver(bstack111l1ll_opy_ (u"ࠧࠧࡰࡢࡶ࡫ࡩࡽࠨਿ"), bstack1ll111l11_opy_)
      yaml.add_constructor(bstack111l1ll_opy_ (u"ࠨࠡࡱࡣࡷ࡬ࡪࡾࠢੀ"), bstack1l111l11ll_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      return config
  except:
    with open(bstack11111l_opy_, bstack111l1ll_opy_ (u"ࠧࡳࠩੁ")) as stream:
      try:
        config = yaml.safe_load(stream)
        return config
      except yaml.YAMLError as exc:
        bstack111ll1ll1_opy_(bstack1l11ll11l_opy_.format(str(exc)))
def bstack1l111l11l_opy_(config):
  bstack11l111l111_opy_ = bstack1l11l1ll1l_opy_(config)
  for option in list(bstack11l111l111_opy_):
    if option.lower() in bstack1l11ll1111_opy_ and option != bstack1l11ll1111_opy_[option.lower()]:
      bstack11l111l111_opy_[bstack1l11ll1111_opy_[option.lower()]] = bstack11l111l111_opy_[option]
      del bstack11l111l111_opy_[option]
  return config
def bstack1l1l1l1l1l_opy_():
  global bstack1111l1l11_opy_
  for key, bstack11lllll11l_opy_ in bstack1l11ll111_opy_.items():
    if isinstance(bstack11lllll11l_opy_, list):
      for var in bstack11lllll11l_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1111l1l11_opy_[key] = os.environ[var]
          break
    elif bstack11lllll11l_opy_ in os.environ and os.environ[bstack11lllll11l_opy_] and str(os.environ[bstack11lllll11l_opy_]).strip():
      bstack1111l1l11_opy_[key] = os.environ[bstack11lllll11l_opy_]
  if bstack111l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪੂ") in os.environ:
    bstack1111l1l11_opy_[bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭੃")] = {}
    bstack1111l1l11_opy_[bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ੄")][bstack111l1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭੅")] = os.environ[bstack111l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ੆")]
def bstack1l1l111ll1_opy_():
  global bstack11llllll1_opy_
  global bstack1l1ll1lll_opy_
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) and bstack111l1ll_opy_ (u"࠭࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩੇ").lower() == val.lower():
      bstack11llllll1_opy_[bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫੈ")] = {}
      bstack11llllll1_opy_[bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ੉")][bstack111l1ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ੊")] = sys.argv[idx + 1]
      del sys.argv[idx:idx + 2]
      break
  for key, bstack11llll1lll_opy_ in bstack1l11l1l1ll_opy_.items():
    if isinstance(bstack11llll1lll_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack11llll1lll_opy_:
          if idx < len(sys.argv) and bstack111l1ll_opy_ (u"ࠪ࠱࠲࠭ੋ") + var.lower() == val.lower() and not key in bstack11llllll1_opy_:
            bstack11llllll1_opy_[key] = sys.argv[idx + 1]
            bstack1l1ll1lll_opy_ += bstack111l1ll_opy_ (u"ࠫࠥ࠳࠭ࠨੌ") + var + bstack111l1ll_opy_ (u"੍ࠬࠦࠧ") + sys.argv[idx + 1]
            del sys.argv[idx:idx + 2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx < len(sys.argv) and bstack111l1ll_opy_ (u"࠭࠭࠮ࠩ੎") + bstack11llll1lll_opy_.lower() == val.lower() and not key in bstack11llllll1_opy_:
          bstack11llllll1_opy_[key] = sys.argv[idx + 1]
          bstack1l1ll1lll_opy_ += bstack111l1ll_opy_ (u"ࠧࠡ࠯࠰ࠫ੏") + bstack11llll1lll_opy_ + bstack111l1ll_opy_ (u"ࠨࠢࠪ੐") + sys.argv[idx + 1]
          del sys.argv[idx:idx + 2]
def bstack111l11l1l_opy_(config):
  bstack1ll111l111_opy_ = config.keys()
  for bstack1l1l1l111_opy_, bstack11lll11ll1_opy_ in bstack1l1l1ll11l_opy_.items():
    if bstack11lll11ll1_opy_ in bstack1ll111l111_opy_:
      config[bstack1l1l1l111_opy_] = config[bstack11lll11ll1_opy_]
      del config[bstack11lll11ll1_opy_]
  for bstack1l1l1l111_opy_, bstack11lll11ll1_opy_ in bstack1l1ll11l11_opy_.items():
    if isinstance(bstack11lll11ll1_opy_, list):
      for bstack11ll1ll1ll_opy_ in bstack11lll11ll1_opy_:
        if bstack11ll1ll1ll_opy_ in bstack1ll111l111_opy_:
          config[bstack1l1l1l111_opy_] = config[bstack11ll1ll1ll_opy_]
          del config[bstack11ll1ll1ll_opy_]
          break
    elif bstack11lll11ll1_opy_ in bstack1ll111l111_opy_:
      config[bstack1l1l1l111_opy_] = config[bstack11lll11ll1_opy_]
      del config[bstack11lll11ll1_opy_]
  for bstack11ll1ll1ll_opy_ in list(config):
    for bstack111l1l1l1_opy_ in bstack11lll111l1_opy_:
      if bstack11ll1ll1ll_opy_.lower() == bstack111l1l1l1_opy_.lower() and bstack11ll1ll1ll_opy_ != bstack111l1l1l1_opy_:
        config[bstack111l1l1l1_opy_] = config[bstack11ll1ll1ll_opy_]
        del config[bstack11ll1ll1ll_opy_]
  bstack1l11ll1l1_opy_ = [{}]
  if not config.get(bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬੑ")):
    config[bstack111l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭੒")] = [{}]
  bstack1l11ll1l1_opy_ = config[bstack111l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ੓")]
  for platform in bstack1l11ll1l1_opy_:
    for bstack11ll1ll1ll_opy_ in list(platform):
      for bstack111l1l1l1_opy_ in bstack11lll111l1_opy_:
        if bstack11ll1ll1ll_opy_.lower() == bstack111l1l1l1_opy_.lower() and bstack11ll1ll1ll_opy_ != bstack111l1l1l1_opy_:
          platform[bstack111l1l1l1_opy_] = platform[bstack11ll1ll1ll_opy_]
          del platform[bstack11ll1ll1ll_opy_]
  for bstack1l1l1l111_opy_, bstack11lll11ll1_opy_ in bstack1l1ll11l11_opy_.items():
    for platform in bstack1l11ll1l1_opy_:
      if isinstance(bstack11lll11ll1_opy_, list):
        for bstack11ll1ll1ll_opy_ in bstack11lll11ll1_opy_:
          if bstack11ll1ll1ll_opy_ in platform:
            platform[bstack1l1l1l111_opy_] = platform[bstack11ll1ll1ll_opy_]
            del platform[bstack11ll1ll1ll_opy_]
            break
      elif bstack11lll11ll1_opy_ in platform:
        platform[bstack1l1l1l111_opy_] = platform[bstack11lll11ll1_opy_]
        del platform[bstack11lll11ll1_opy_]
  for bstack111l1111l_opy_ in bstack1ll1l111l_opy_:
    if bstack111l1111l_opy_ in config:
      if not bstack1ll1l111l_opy_[bstack111l1111l_opy_] in config:
        config[bstack1ll1l111l_opy_[bstack111l1111l_opy_]] = {}
      config[bstack1ll1l111l_opy_[bstack111l1111l_opy_]].update(config[bstack111l1111l_opy_])
      del config[bstack111l1111l_opy_]
  for platform in bstack1l11ll1l1_opy_:
    for bstack111l1111l_opy_ in bstack1ll1l111l_opy_:
      if bstack111l1111l_opy_ in list(platform):
        if not bstack1ll1l111l_opy_[bstack111l1111l_opy_] in platform:
          platform[bstack1ll1l111l_opy_[bstack111l1111l_opy_]] = {}
        platform[bstack1ll1l111l_opy_[bstack111l1111l_opy_]].update(platform[bstack111l1111l_opy_])
        del platform[bstack111l1111l_opy_]
  config = bstack1l111l11l_opy_(config)
  return config
def bstack11l1llll11_opy_(config):
  global bstack1l111ll1l_opy_
  bstack1l1l1l11l1_opy_ = False
  if bstack111l1ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ੔") in config and str(config[bstack111l1ll_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ੕")]).lower() != bstack111l1ll_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭੖"):
    if bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ੗") not in config or str(config[bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭੘")]).lower() == bstack111l1ll_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩਖ਼"):
      config[bstack111l1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪਗ਼")] = False
    else:
      bstack11l1l11lll_opy_ = bstack1ll1lllll1_opy_()
      if bstack111l1ll_opy_ (u"ࠬ࡯ࡳࡕࡴ࡬ࡥࡱࡍࡲࡪࡦࠪਜ਼") in bstack11l1l11lll_opy_:
        if not bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪੜ") in config:
          config[bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ੝")] = {}
        config[bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬਫ਼")][bstack111l1ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ੟")] = bstack111l1ll_opy_ (u"ࠪࡥࡹࡹ࠭ࡳࡧࡳࡩࡦࡺࡥࡳࠩ੠")
        bstack1l1l1l11l1_opy_ = True
        bstack1l111ll1l_opy_ = config[bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ੡")].get(bstack111l1ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ੢"))
  if bstack11ll1lll1_opy_(config) and bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ੣") in config and str(config[bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ੤")]).lower() != bstack111l1ll_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ੥") and not bstack1l1l1l11l1_opy_:
    if not bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭੦") in config:
      config[bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ੧")] = {}
    if not config[bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ੨")].get(bstack111l1ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠩ੩")) and not bstack111l1ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ੪") in config[bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ੫")]:
      bstack1l1lllll_opy_ = datetime.datetime.now()
      bstack1ll11ll11l_opy_ = bstack1l1lllll_opy_.strftime(bstack111l1ll_opy_ (u"ࠨࠧࡧࡣࠪࡨ࡟ࠦࡊࠨࡑࠬ੬"))
      hostname = socket.gethostname()
      bstack1ll11l11l_opy_ = bstack111l1ll_opy_ (u"ࠩࠪ੭").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack111l1ll_opy_ (u"ࠪࡿࢂࡥࡻࡾࡡࡾࢁࠬ੮").format(bstack1ll11ll11l_opy_, hostname, bstack1ll11l11l_opy_)
      config[bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ੯")][bstack111l1ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧੰ")] = identifier
    bstack1l111ll1l_opy_ = config[bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪੱ")].get(bstack111l1ll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩੲ"))
  return config
def bstack1l1ll11lll_opy_():
  bstack1ll1lll1l1_opy_ =  bstack11l1l111l_opy_()[bstack111l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠧੳ")]
  return bstack1ll1lll1l1_opy_ if bstack1ll1lll1l1_opy_ else -1
def bstack11l11l1l1l_opy_(bstack1ll1lll1l1_opy_):
  global CONFIG
  if not bstack111l1ll_opy_ (u"ࠩࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫੴ") in CONFIG[bstack111l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬੵ")]:
    return
  CONFIG[bstack111l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭੶")] = CONFIG[bstack111l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ੷")].replace(
    bstack111l1ll_opy_ (u"࠭ࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨ੸"),
    str(bstack1ll1lll1l1_opy_)
  )
def bstack111l11lll_opy_():
  global CONFIG
  if not bstack111l1ll_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭੹") in CONFIG[bstack111l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ੺")]:
    return
  bstack1l1lllll_opy_ = datetime.datetime.now()
  bstack1ll11ll11l_opy_ = bstack1l1lllll_opy_.strftime(bstack111l1ll_opy_ (u"ࠩࠨࡨ࠲ࠫࡢ࠮ࠧࡋ࠾ࠪࡓࠧ੻"))
  CONFIG[bstack111l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ੼")] = CONFIG[bstack111l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭੽")].replace(
    bstack111l1ll_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫ੾"),
    bstack1ll11ll11l_opy_
  )
def bstack11l1ll111l_opy_():
  global CONFIG
  if bstack111l1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ੿") in CONFIG and not bool(CONFIG[bstack111l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ઀")]):
    del CONFIG[bstack111l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪઁ")]
    return
  if not bstack111l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫં") in CONFIG:
    CONFIG[bstack111l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬઃ")] = bstack111l1ll_opy_ (u"ࠫࠨࠪࡻࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࢃࠧ઄")
  if bstack111l1ll_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫઅ") in CONFIG[bstack111l1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨઆ")]:
    bstack111l11lll_opy_()
    os.environ[bstack111l1ll_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫઇ")] = CONFIG[bstack111l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪઈ")]
  if not bstack111l1ll_opy_ (u"ࠩࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫઉ") in CONFIG[bstack111l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬઊ")]:
    return
  bstack1ll1lll1l1_opy_ = bstack111l1ll_opy_ (u"ࠫࠬઋ")
  bstack1l11ll1lll_opy_ = bstack1l1ll11lll_opy_()
  if bstack1l11ll1lll_opy_ != -1:
    bstack1ll1lll1l1_opy_ = bstack111l1ll_opy_ (u"ࠬࡉࡉࠡࠩઌ") + str(bstack1l11ll1lll_opy_)
  if bstack1ll1lll1l1_opy_ == bstack111l1ll_opy_ (u"࠭ࠧઍ"):
    bstack111l1l111_opy_ = bstack1lll1l1lll_opy_(CONFIG[bstack111l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ઎")])
    if bstack111l1l111_opy_ != -1:
      bstack1ll1lll1l1_opy_ = str(bstack111l1l111_opy_)
  if bstack1ll1lll1l1_opy_:
    bstack11l11l1l1l_opy_(bstack1ll1lll1l1_opy_)
    os.environ[bstack111l1ll_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬએ")] = CONFIG[bstack111l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫઐ")]
def bstack11l1l1ll1_opy_(bstack1l111llll_opy_, bstack11ll11l111_opy_, path):
  bstack1l11l11lll_opy_ = {
    bstack111l1ll_opy_ (u"ࠪ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧઑ"): bstack11ll11l111_opy_
  }
  if os.path.exists(path):
    bstack1lll11ll11_opy_ = json.load(open(path, bstack111l1ll_opy_ (u"ࠫࡷࡨࠧ઒")))
  else:
    bstack1lll11ll11_opy_ = {}
  bstack1lll11ll11_opy_[bstack1l111llll_opy_] = bstack1l11l11lll_opy_
  with open(path, bstack111l1ll_opy_ (u"ࠧࡽࠫࠣઓ")) as outfile:
    json.dump(bstack1lll11ll11_opy_, outfile)
def bstack1lll1l1lll_opy_(bstack1l111llll_opy_):
  bstack1l111llll_opy_ = str(bstack1l111llll_opy_)
  bstack11ll1l1l11_opy_ = os.path.join(os.path.expanduser(bstack111l1ll_opy_ (u"࠭ࡾࠨઔ")), bstack111l1ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧક"))
  try:
    if not os.path.exists(bstack11ll1l1l11_opy_):
      os.makedirs(bstack11ll1l1l11_opy_)
    file_path = os.path.join(os.path.expanduser(bstack111l1ll_opy_ (u"ࠨࢀࠪખ")), bstack111l1ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩગ"), bstack111l1ll_opy_ (u"ࠪ࠲ࡧࡻࡩ࡭ࡦ࠰ࡲࡦࡳࡥ࠮ࡥࡤࡧ࡭࡫࠮࡫ࡵࡲࡲࠬઘ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack111l1ll_opy_ (u"ࠫࡼ࠭ઙ")):
        pass
      with open(file_path, bstack111l1ll_opy_ (u"ࠧࡽࠫࠣચ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack111l1ll_opy_ (u"࠭ࡲࠨછ")) as bstack111111l1l_opy_:
      bstack11l11l1l1_opy_ = json.load(bstack111111l1l_opy_)
    if bstack1l111llll_opy_ in bstack11l11l1l1_opy_:
      bstack11ll11111_opy_ = bstack11l11l1l1_opy_[bstack1l111llll_opy_][bstack111l1ll_opy_ (u"ࠧࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫજ")]
      bstack1l11lllll1_opy_ = int(bstack11ll11111_opy_) + 1
      bstack11l1l1ll1_opy_(bstack1l111llll_opy_, bstack1l11lllll1_opy_, file_path)
      return bstack1l11lllll1_opy_
    else:
      bstack11l1l1ll1_opy_(bstack1l111llll_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack11lll11l1l_opy_.format(str(e)))
    return -1
def bstack11llll11ll_opy_(config):
  if not config[bstack111l1ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪઝ")] or not config[bstack111l1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬઞ")]:
    return True
  else:
    return False
def bstack1llllll11l_opy_(config, index=0):
  global bstack1l11l1111_opy_
  bstack1l11ll1l11_opy_ = {}
  caps = bstack111l11ll1_opy_ + bstack1ll1ll11l1_opy_
  if config.get(bstack111l1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧટ"), False):
    bstack1l11ll1l11_opy_[bstack111l1ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨઠ")] = True
    bstack1l11ll1l11_opy_[bstack111l1ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩડ")] = config.get(bstack111l1ll_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪઢ"), {})
  if bstack1l11l1111_opy_:
    caps += bstack111lllll1l_opy_
  for key in config:
    if key in caps + [bstack111l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪણ")]:
      continue
    bstack1l11ll1l11_opy_[key] = config[key]
  if bstack111l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫત") in config:
    for bstack1l1lll11l1_opy_ in config[bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬથ")][index]:
      if bstack1l1lll11l1_opy_ in caps:
        continue
      bstack1l11ll1l11_opy_[bstack1l1lll11l1_opy_] = config[bstack111l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭દ")][index][bstack1l1lll11l1_opy_]
  bstack1l11ll1l11_opy_[bstack111l1ll_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭ધ")] = socket.gethostname()
  if bstack111l1ll_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ન") in bstack1l11ll1l11_opy_:
    del (bstack1l11ll1l11_opy_[bstack111l1ll_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧ઩")])
  return bstack1l11ll1l11_opy_
def bstack1l1l1lllll_opy_(config):
  global bstack1l11l1111_opy_
  bstack11ll1ll11l_opy_ = {}
  caps = bstack1ll1ll11l1_opy_
  if bstack1l11l1111_opy_:
    caps += bstack111lllll1l_opy_
  for key in caps:
    if key in config:
      bstack11ll1ll11l_opy_[key] = config[key]
  return bstack11ll1ll11l_opy_
def bstack11lllll1l_opy_(bstack1l11ll1l11_opy_, bstack11ll1ll11l_opy_):
  bstack11lll11lll_opy_ = {}
  for key in bstack1l11ll1l11_opy_.keys():
    if key in bstack1l1l1ll11l_opy_:
      bstack11lll11lll_opy_[bstack1l1l1ll11l_opy_[key]] = bstack1l11ll1l11_opy_[key]
    else:
      bstack11lll11lll_opy_[key] = bstack1l11ll1l11_opy_[key]
  for key in bstack11ll1ll11l_opy_:
    if key in bstack1l1l1ll11l_opy_:
      bstack11lll11lll_opy_[bstack1l1l1ll11l_opy_[key]] = bstack11ll1ll11l_opy_[key]
    else:
      bstack11lll11lll_opy_[key] = bstack11ll1ll11l_opy_[key]
  return bstack11lll11lll_opy_
def bstack1111l1l1l_opy_(config, index=0):
  global bstack1l11l1111_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack11111l111_opy_ = bstack11ll1111l_opy_(bstack1ll11l1l1l_opy_, config, logger)
  bstack11ll1ll11l_opy_ = bstack1l1l1lllll_opy_(config)
  bstack11111lll1_opy_ = bstack1ll1ll11l1_opy_
  bstack11111lll1_opy_ += bstack1l1ll1llll_opy_
  bstack11ll1ll11l_opy_ = update(bstack11ll1ll11l_opy_, bstack11111l111_opy_)
  if bstack1l11l1111_opy_:
    bstack11111lll1_opy_ += bstack111lllll1l_opy_
  if bstack111l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪપ") in config:
    if bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ફ") in config[bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬબ")][index]:
      caps[bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨભ")] = config[bstack111l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧમ")][index][bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪય")]
    if bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧર") in config[bstack111l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ઱")][index]:
      caps[bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩલ")] = str(config[bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬળ")][index][bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ઴")])
    bstack1l1l11l1ll_opy_ = bstack11ll1111l_opy_(bstack1ll11l1l1l_opy_, config[bstack111l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧવ")][index], logger)
    bstack11111lll1_opy_ += list(bstack1l1l11l1ll_opy_.keys())
    for bstack1lll11llll_opy_ in bstack11111lll1_opy_:
      if bstack1lll11llll_opy_ in config[bstack111l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨશ")][index]:
        if bstack1lll11llll_opy_ == bstack111l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨષ"):
          try:
            bstack1l1l11l1ll_opy_[bstack1lll11llll_opy_] = str(config[bstack111l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪસ")][index][bstack1lll11llll_opy_] * 1.0)
          except:
            bstack1l1l11l1ll_opy_[bstack1lll11llll_opy_] = str(config[bstack111l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫહ")][index][bstack1lll11llll_opy_])
        else:
          bstack1l1l11l1ll_opy_[bstack1lll11llll_opy_] = config[bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ઺")][index][bstack1lll11llll_opy_]
        del (config[bstack111l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭઻")][index][bstack1lll11llll_opy_])
    bstack11ll1ll11l_opy_ = update(bstack11ll1ll11l_opy_, bstack1l1l11l1ll_opy_)
  bstack1l11ll1l11_opy_ = bstack1llllll11l_opy_(config, index)
  for bstack11ll1ll1ll_opy_ in bstack1ll1ll11l1_opy_ + list(bstack11111l111_opy_.keys()):
    if bstack11ll1ll1ll_opy_ in bstack1l11ll1l11_opy_:
      bstack11ll1ll11l_opy_[bstack11ll1ll1ll_opy_] = bstack1l11ll1l11_opy_[bstack11ll1ll1ll_opy_]
      del (bstack1l11ll1l11_opy_[bstack11ll1ll1ll_opy_])
  if bstack1l1lll1ll_opy_(config):
    bstack1l11ll1l11_opy_[bstack111l1ll_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆ઼ࠫ")] = True
    caps.update(bstack11ll1ll11l_opy_)
    caps[bstack111l1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ઽ")] = bstack1l11ll1l11_opy_
  else:
    bstack1l11ll1l11_opy_[bstack111l1ll_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ા")] = False
    caps.update(bstack11lllll1l_opy_(bstack1l11ll1l11_opy_, bstack11ll1ll11l_opy_))
    if bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬિ") in caps:
      caps[bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩી")] = caps[bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧુ")]
      del (caps[bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨૂ")])
    if bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬૃ") in caps:
      caps[bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧૄ")] = caps[bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧૅ")]
      del (caps[bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ૆")])
  return caps
def bstack1ll1111ll1_opy_():
  global bstack11111l1l1_opy_
  global CONFIG
  if bstack11lll1111_opy_() <= version.parse(bstack111l1ll_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨે")):
    if bstack11111l1l1_opy_ != bstack111l1ll_opy_ (u"ࠩࠪૈ"):
      return bstack111l1ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦૉ") + bstack11111l1l1_opy_ + bstack111l1ll_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣ૊")
    return bstack11111ll11_opy_
  if bstack11111l1l1_opy_ != bstack111l1ll_opy_ (u"ࠬ࠭ો"):
    return bstack111l1ll_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣૌ") + bstack11111l1l1_opy_ + bstack111l1ll_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢ્ࠣ")
  return bstack1lll1l111_opy_
def bstack1llll111ll_opy_(options):
  return hasattr(options, bstack111l1ll_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩ૎"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1ll1lll11_opy_(options, bstack11l1ll1l1_opy_):
  for bstack11l111lll_opy_ in bstack11l1ll1l1_opy_:
    if bstack11l111lll_opy_ in [bstack111l1ll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ૏"), bstack111l1ll_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧૐ")]:
      continue
    if bstack11l111lll_opy_ in options._experimental_options:
      options._experimental_options[bstack11l111lll_opy_] = update(options._experimental_options[bstack11l111lll_opy_],
                                                         bstack11l1ll1l1_opy_[bstack11l111lll_opy_])
    else:
      options.add_experimental_option(bstack11l111lll_opy_, bstack11l1ll1l1_opy_[bstack11l111lll_opy_])
  if bstack111l1ll_opy_ (u"ࠫࡦࡸࡧࡴࠩ૑") in bstack11l1ll1l1_opy_:
    for arg in bstack11l1ll1l1_opy_[bstack111l1ll_opy_ (u"ࠬࡧࡲࡨࡵࠪ૒")]:
      options.add_argument(arg)
    del (bstack11l1ll1l1_opy_[bstack111l1ll_opy_ (u"࠭ࡡࡳࡩࡶࠫ૓")])
  if bstack111l1ll_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ૔") in bstack11l1ll1l1_opy_:
    for ext in bstack11l1ll1l1_opy_[bstack111l1ll_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ૕")]:
      options.add_extension(ext)
    del (bstack11l1ll1l1_opy_[bstack111l1ll_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭૖")])
def bstack11l1lll1l_opy_(options, bstack1l11lllll_opy_):
  if bstack111l1ll_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩ૗") in bstack1l11lllll_opy_:
    for bstack1l1lll11l_opy_ in bstack1l11lllll_opy_[bstack111l1ll_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ૘")]:
      if bstack1l1lll11l_opy_ in options._preferences:
        options._preferences[bstack1l1lll11l_opy_] = update(options._preferences[bstack1l1lll11l_opy_], bstack1l11lllll_opy_[bstack111l1ll_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ૙")][bstack1l1lll11l_opy_])
      else:
        options.set_preference(bstack1l1lll11l_opy_, bstack1l11lllll_opy_[bstack111l1ll_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ૚")][bstack1l1lll11l_opy_])
  if bstack111l1ll_opy_ (u"ࠧࡢࡴࡪࡷࠬ૛") in bstack1l11lllll_opy_:
    for arg in bstack1l11lllll_opy_[bstack111l1ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭૜")]:
      options.add_argument(arg)
def bstack11l1lll1ll_opy_(options, bstack11l1lllll1_opy_):
  if bstack111l1ll_opy_ (u"ࠩࡺࡩࡧࡼࡩࡦࡹࠪ૝") in bstack11l1lllll1_opy_:
    options.use_webview(bool(bstack11l1lllll1_opy_[bstack111l1ll_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࠫ૞")]))
  bstack1ll1lll11_opy_(options, bstack11l1lllll1_opy_)
def bstack1ll1l1l11_opy_(options, bstack1l11l1l11l_opy_):
  for bstack111ll1l1l_opy_ in bstack1l11l1l11l_opy_:
    if bstack111ll1l1l_opy_ in [bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨ૟"), bstack111l1ll_opy_ (u"ࠬࡧࡲࡨࡵࠪૠ")]:
      continue
    options.set_capability(bstack111ll1l1l_opy_, bstack1l11l1l11l_opy_[bstack111ll1l1l_opy_])
  if bstack111l1ll_opy_ (u"࠭ࡡࡳࡩࡶࠫૡ") in bstack1l11l1l11l_opy_:
    for arg in bstack1l11l1l11l_opy_[bstack111l1ll_opy_ (u"ࠧࡢࡴࡪࡷࠬૢ")]:
      options.add_argument(arg)
  if bstack111l1ll_opy_ (u"ࠨࡶࡨࡧ࡭ࡴ࡯࡭ࡱࡪࡽࡕࡸࡥࡷ࡫ࡨࡻࠬૣ") in bstack1l11l1l11l_opy_:
    options.bstack11llll1ll_opy_(bool(bstack1l11l1l11l_opy_[bstack111l1ll_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭૤")]))
def bstack1ll11lll1l_opy_(options, bstack1l111ll11l_opy_):
  for bstack111ll111l_opy_ in bstack1l111ll11l_opy_:
    if bstack111ll111l_opy_ in [bstack111l1ll_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ૥"), bstack111l1ll_opy_ (u"ࠫࡦࡸࡧࡴࠩ૦")]:
      continue
    options._options[bstack111ll111l_opy_] = bstack1l111ll11l_opy_[bstack111ll111l_opy_]
  if bstack111l1ll_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ૧") in bstack1l111ll11l_opy_:
    for bstack11l111lll1_opy_ in bstack1l111ll11l_opy_[bstack111l1ll_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ૨")]:
      options.bstack11l11lll1_opy_(
        bstack11l111lll1_opy_, bstack1l111ll11l_opy_[bstack111l1ll_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ૩")][bstack11l111lll1_opy_])
  if bstack111l1ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭૪") in bstack1l111ll11l_opy_:
    for arg in bstack1l111ll11l_opy_[bstack111l1ll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ૫")]:
      options.add_argument(arg)
def bstack1lll1ll111_opy_(options, caps):
  if not hasattr(options, bstack111l1ll_opy_ (u"ࠪࡏࡊ࡟ࠧ૬")):
    return
  if options.KEY == bstack111l1ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ૭") and options.KEY in caps:
    bstack1ll1lll11_opy_(options, caps[bstack111l1ll_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ૮")])
  elif options.KEY == bstack111l1ll_opy_ (u"࠭࡭ࡰࡼ࠽ࡪ࡮ࡸࡥࡧࡱࡻࡓࡵࡺࡩࡰࡰࡶࠫ૯") and options.KEY in caps:
    bstack11l1lll1l_opy_(options, caps[bstack111l1ll_opy_ (u"ࠧ࡮ࡱࡽ࠾࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬ૰")])
  elif options.KEY == bstack111l1ll_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ૱") and options.KEY in caps:
    bstack1ll1l1l11_opy_(options, caps[bstack111l1ll_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪ૲")])
  elif options.KEY == bstack111l1ll_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫ૳") and options.KEY in caps:
    bstack11l1lll1ll_opy_(options, caps[bstack111l1ll_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬ૴")])
  elif options.KEY == bstack111l1ll_opy_ (u"ࠬࡹࡥ࠻࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫ૵") and options.KEY in caps:
    bstack1ll11lll1l_opy_(options, caps[bstack111l1ll_opy_ (u"࠭ࡳࡦ࠼࡬ࡩࡔࡶࡴࡪࡱࡱࡷࠬ૶")])
def bstack1111lll1l_opy_(caps):
  global bstack1l11l1111_opy_
  if isinstance(os.environ.get(bstack111l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ૷")), str):
    bstack1l11l1111_opy_ = eval(os.getenv(bstack111l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ૸")))
  if bstack1l11l1111_opy_:
    if bstack11lll11ll_opy_() < version.parse(bstack111l1ll_opy_ (u"ࠩ࠵࠲࠸࠴࠰ࠨૹ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack111l1ll_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪૺ")
    if bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩૻ") in caps:
      browser = caps[bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪૼ")]
    elif bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧ૽") in caps:
      browser = caps[bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨ૾")]
    browser = str(browser).lower()
    if browser == bstack111l1ll_opy_ (u"ࠨ࡫ࡳ࡬ࡴࡴࡥࠨ૿") or browser == bstack111l1ll_opy_ (u"ࠩ࡬ࡴࡦࡪࠧ଀"):
      browser = bstack111l1ll_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪଁ")
    if browser == bstack111l1ll_opy_ (u"ࠫࡸࡧ࡭ࡴࡷࡱ࡫ࠬଂ"):
      browser = bstack111l1ll_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬଃ")
    if browser not in [bstack111l1ll_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭଄"), bstack111l1ll_opy_ (u"ࠧࡦࡦࡪࡩࠬଅ"), bstack111l1ll_opy_ (u"ࠨ࡫ࡨࠫଆ"), bstack111l1ll_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࠩଇ"), bstack111l1ll_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫଈ")]:
      return None
    try:
      package = bstack111l1ll_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳ࠰ࡾࢁ࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭ଉ").format(browser)
      name = bstack111l1ll_opy_ (u"ࠬࡕࡰࡵ࡫ࡲࡲࡸ࠭ଊ")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1llll111ll_opy_(options):
        return None
      for bstack11ll1ll1ll_opy_ in caps.keys():
        options.set_capability(bstack11ll1ll1ll_opy_, caps[bstack11ll1ll1ll_opy_])
      bstack1lll1ll111_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack111ll1lll_opy_(options, bstack1lll1l11ll_opy_):
  if not bstack1llll111ll_opy_(options):
    return
  for bstack11ll1ll1ll_opy_ in bstack1lll1l11ll_opy_.keys():
    if bstack11ll1ll1ll_opy_ in bstack1l1ll1llll_opy_:
      continue
    if bstack11ll1ll1ll_opy_ in options._caps and type(options._caps[bstack11ll1ll1ll_opy_]) in [dict, list]:
      options._caps[bstack11ll1ll1ll_opy_] = update(options._caps[bstack11ll1ll1ll_opy_], bstack1lll1l11ll_opy_[bstack11ll1ll1ll_opy_])
    else:
      options.set_capability(bstack11ll1ll1ll_opy_, bstack1lll1l11ll_opy_[bstack11ll1ll1ll_opy_])
  bstack1lll1ll111_opy_(options, bstack1lll1l11ll_opy_)
  if bstack111l1ll_opy_ (u"࠭࡭ࡰࡼ࠽ࡨࡪࡨࡵࡨࡩࡨࡶࡆࡪࡤࡳࡧࡶࡷࠬଋ") in options._caps:
    if options._caps[bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬଌ")] and options._caps[bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭଍")].lower() != bstack111l1ll_opy_ (u"ࠩࡩ࡭ࡷ࡫ࡦࡰࡺࠪ଎"):
      del options._caps[bstack111l1ll_opy_ (u"ࠪࡱࡴࢀ࠺ࡥࡧࡥࡹ࡬࡭ࡥࡳࡃࡧࡨࡷ࡫ࡳࡴࠩଏ")]
def bstack1l1ll111l1_opy_(proxy_config):
  if bstack111l1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨଐ") in proxy_config:
    proxy_config[bstack111l1ll_opy_ (u"ࠬࡹࡳ࡭ࡒࡵࡳࡽࡿࠧ଑")] = proxy_config[bstack111l1ll_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ଒")]
    del (proxy_config[bstack111l1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫଓ")])
  if bstack111l1ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫଔ") in proxy_config and proxy_config[bstack111l1ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬକ")].lower() != bstack111l1ll_opy_ (u"ࠪࡨ࡮ࡸࡥࡤࡶࠪଖ"):
    proxy_config[bstack111l1ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧଗ")] = bstack111l1ll_opy_ (u"ࠬࡳࡡ࡯ࡷࡤࡰࠬଘ")
  if bstack111l1ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࡆࡻࡴࡰࡥࡲࡲ࡫࡯ࡧࡖࡴ࡯ࠫଙ") in proxy_config:
    proxy_config[bstack111l1ll_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪଚ")] = bstack111l1ll_opy_ (u"ࠨࡲࡤࡧࠬଛ")
  return proxy_config
def bstack1ll1ll1lll_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack111l1ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨଜ") in config:
    return proxy
  config[bstack111l1ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩଝ")] = bstack1l1ll111l1_opy_(config[bstack111l1ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪଞ")])
  if proxy == None:
    proxy = Proxy(config[bstack111l1ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫଟ")])
  return proxy
def bstack1l1ll1111l_opy_(self):
  global CONFIG
  global bstack1ll11l1l11_opy_
  try:
    proxy = bstack111111ll1_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack111l1ll_opy_ (u"࠭࠮ࡱࡣࡦࠫଠ")):
        proxies = bstack11111l1ll_opy_(proxy, bstack1ll1111ll1_opy_())
        if len(proxies) > 0:
          protocol, bstack1l1lllll1_opy_ = proxies.popitem()
          if bstack111l1ll_opy_ (u"ࠢ࠻࠱࠲ࠦଡ") in bstack1l1lllll1_opy_:
            return bstack1l1lllll1_opy_
          else:
            return bstack111l1ll_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤଢ") + bstack1l1lllll1_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack111l1ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡶࡲࡰࡺࡼࠤࡺࡸ࡬ࠡ࠼ࠣࡿࢂࠨଣ").format(str(e)))
  return bstack1ll11l1l11_opy_(self)
def bstack11l1l11111_opy_():
  global CONFIG
  return bstack1l1l11ll11_opy_(CONFIG) and bstack1l1ll11l1_opy_() and bstack11lll1111_opy_() >= version.parse(bstack1l1ll11ll1_opy_)
def bstack1ll1111l11_opy_():
  global CONFIG
  return (bstack111l1ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ତ") in CONFIG or bstack111l1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨଥ") in CONFIG) and bstack1llll1llll_opy_()
def bstack1l11l1ll1l_opy_(config):
  bstack11l111l111_opy_ = {}
  if bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩଦ") in config:
    bstack11l111l111_opy_ = config[bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪଧ")]
  if bstack111l1ll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ନ") in config:
    bstack11l111l111_opy_ = config[bstack111l1ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ଩")]
  proxy = bstack111111ll1_opy_(config)
  if proxy:
    if proxy.endswith(bstack111l1ll_opy_ (u"ࠩ࠱ࡴࡦࡩࠧପ")) and os.path.isfile(proxy):
      bstack11l111l111_opy_[bstack111l1ll_opy_ (u"ࠪ࠱ࡵࡧࡣ࠮ࡨ࡬ࡰࡪ࠭ଫ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack111l1ll_opy_ (u"ࠫ࠳ࡶࡡࡤࠩବ")):
        proxies = bstack1l1l1l1ll_opy_(config, bstack1ll1111ll1_opy_())
        if len(proxies) > 0:
          protocol, bstack1l1lllll1_opy_ = proxies.popitem()
          if bstack111l1ll_opy_ (u"ࠧࡀ࠯࠰ࠤଭ") in bstack1l1lllll1_opy_:
            parsed_url = urlparse(bstack1l1lllll1_opy_)
          else:
            parsed_url = urlparse(protocol + bstack111l1ll_opy_ (u"ࠨ࠺࠰࠱ࠥମ") + bstack1l1lllll1_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack11l111l111_opy_[bstack111l1ll_opy_ (u"ࠧࡱࡴࡲࡼࡾࡎ࡯ࡴࡶࠪଯ")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack11l111l111_opy_[bstack111l1ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡰࡴࡷࠫର")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack11l111l111_opy_[bstack111l1ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡖࡵࡨࡶࠬ଱")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack11l111l111_opy_[bstack111l1ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡤࡷࡸ࠭ଲ")] = str(parsed_url.password)
  return bstack11l111l111_opy_
def bstack1ll1l1lll1_opy_(config):
  if bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠩଳ") in config:
    return config[bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠪ଴")]
  return {}
def bstack1ll1lll1l_opy_(caps):
  global bstack1l111ll1l_opy_
  if bstack111l1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧଵ") in caps:
    caps[bstack111l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨଶ")][bstack111l1ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࠧଷ")] = True
    if bstack1l111ll1l_opy_:
      caps[bstack111l1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪସ")][bstack111l1ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬହ")] = bstack1l111ll1l_opy_
  else:
    caps[bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࠩ଺")] = True
    if bstack1l111ll1l_opy_:
      caps[bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭଻")] = bstack1l111ll1l_opy_
def bstack11lllllll_opy_():
  global CONFIG
  if not bstack11ll1lll1_opy_(CONFIG):
    return
  if bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮଼ࠪ") in CONFIG and bstack1l1l111lll_opy_(CONFIG[bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫଽ")]):
    if (
      bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬା") in CONFIG
      and bstack1l1l111lll_opy_(CONFIG[bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ି")].get(bstack111l1ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡃ࡫ࡱࡥࡷࡿࡉ࡯࡫ࡷ࡭ࡦࡲࡩࡴࡣࡷ࡭ࡴࡴࠧୀ")))
    ):
      logger.debug(bstack111l1ll_opy_ (u"ࠦࡑࡵࡣࡢ࡮ࠣࡦ࡮ࡴࡡࡳࡻࠣࡲࡴࡺࠠࡴࡶࡤࡶࡹ࡫ࡤࠡࡣࡶࠤࡸࡱࡩࡱࡄ࡬ࡲࡦࡸࡹࡊࡰ࡬ࡸ࡮ࡧ࡬ࡪࡵࡤࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࡪࡴࡡࡣ࡮ࡨࡨࠧୁ"))
      return
    bstack11l111l111_opy_ = bstack1l11l1ll1l_opy_(CONFIG)
    bstack1llll1111_opy_(CONFIG[bstack111l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨୂ")], bstack11l111l111_opy_)
def bstack1llll1111_opy_(key, bstack11l111l111_opy_):
  global bstack1llll1l1ll_opy_
  logger.info(bstack1l11l1l1l_opy_)
  try:
    bstack1llll1l1ll_opy_ = Local()
    bstack1l11l11ll1_opy_ = {bstack111l1ll_opy_ (u"࠭࡫ࡦࡻࠪୃ"): key}
    bstack1l11l11ll1_opy_.update(bstack11l111l111_opy_)
    logger.debug(bstack11111l11l_opy_.format(str(bstack1l11l11ll1_opy_)))
    bstack1llll1l1ll_opy_.start(**bstack1l11l11ll1_opy_)
    if bstack1llll1l1ll_opy_.isRunning():
      logger.info(bstack1ll11l1lll_opy_)
  except Exception as e:
    bstack111ll1ll1_opy_(bstack1l1ll11111_opy_.format(str(e)))
def bstack1111l1lll_opy_():
  global bstack1llll1l1ll_opy_
  if bstack1llll1l1ll_opy_.isRunning():
    logger.info(bstack11l1ll1lll_opy_)
    bstack1llll1l1ll_opy_.stop()
  bstack1llll1l1ll_opy_ = None
def bstack1ll11111ll_opy_(bstack11ll1l1l1l_opy_=[]):
  global CONFIG
  bstack1ll111llll_opy_ = []
  bstack1lll1l1l1_opy_ = [bstack111l1ll_opy_ (u"ࠧࡰࡵࠪୄ"), bstack111l1ll_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫ୅"), bstack111l1ll_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭୆"), bstack111l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬେ"), bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩୈ"), bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭୉")]
  try:
    for err in bstack11ll1l1l1l_opy_:
      bstack1lllllll11_opy_ = {}
      for k in bstack1lll1l1l1_opy_:
        val = CONFIG[bstack111l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ୊")][int(err[bstack111l1ll_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ୋ")])].get(k)
        if val:
          bstack1lllllll11_opy_[k] = val
      if(err[bstack111l1ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧୌ")] != bstack111l1ll_opy_ (u"୍ࠩࠪ")):
        bstack1lllllll11_opy_[bstack111l1ll_opy_ (u"ࠪࡸࡪࡹࡴࡴࠩ୎")] = {
          err[bstack111l1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ୏")]: err[bstack111l1ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ୐")]
        }
        bstack1ll111llll_opy_.append(bstack1lllllll11_opy_)
  except Exception as e:
    logger.debug(bstack111l1ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡲࡶࡲࡧࡴࡵ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࡀࠠࠨ୑") + str(e))
  finally:
    return bstack1ll111llll_opy_
def bstack1l1ll111l_opy_(file_name):
  bstack1111lll11_opy_ = []
  try:
    bstack1lll1111l1_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1lll1111l1_opy_):
      with open(bstack1lll1111l1_opy_) as f:
        bstack111l1llll_opy_ = json.load(f)
        bstack1111lll11_opy_ = bstack111l1llll_opy_
      os.remove(bstack1lll1111l1_opy_)
    return bstack1111lll11_opy_
  except Exception as e:
    logger.debug(bstack111l1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩ࡭ࡳࡪࡩ࡯ࡩࠣࡩࡷࡸ࡯ࡳࠢ࡯࡭ࡸࡺ࠺ࠡࠩ୒") + str(e))
    return bstack1111lll11_opy_
def bstack11lll1ll1_opy_():
  global bstack11l1111l1l_opy_
  global bstack1ll111l11l_opy_
  global bstack11l111l11l_opy_
  global bstack1llll1ll11_opy_
  global bstack11l11l111_opy_
  global bstack11llll111_opy_
  global CONFIG
  bstack1llll1ll1l_opy_ = os.environ.get(bstack111l1ll_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩ୓"))
  if bstack1llll1ll1l_opy_ in [bstack111l1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ୔"), bstack111l1ll_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ୕")]:
    bstack1lll1111ll_opy_()
  percy.shutdown()
  if bstack11l1111l1l_opy_:
    logger.warning(bstack1l111ll1l1_opy_.format(str(bstack11l1111l1l_opy_)))
  else:
    try:
      bstack1lll11ll11_opy_ = bstack1llllllll1_opy_(bstack111l1ll_opy_ (u"ࠫ࠳ࡨࡳࡵࡣࡦ࡯࠲ࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪୖ"), logger)
      if bstack1lll11ll11_opy_.get(bstack111l1ll_opy_ (u"ࠬࡴࡵࡥࡩࡨࡣࡱࡵࡣࡢ࡮ࠪୗ")) and bstack1lll11ll11_opy_.get(bstack111l1ll_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫ୘")).get(bstack111l1ll_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩ୙")):
        logger.warning(bstack1l111ll1l1_opy_.format(str(bstack1lll11ll11_opy_[bstack111l1ll_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭୚")][bstack111l1ll_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫ୛")])))
    except Exception as e:
      logger.error(e)
  logger.info(bstack11l11ll1l1_opy_)
  global bstack1llll1l1ll_opy_
  if bstack1llll1l1ll_opy_:
    bstack1111l1lll_opy_()
  try:
    for driver in bstack1ll111l11l_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack11ll11ll1_opy_)
  if bstack11llll111_opy_ == bstack111l1ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩଡ଼"):
    bstack11l11l111_opy_ = bstack1l1ll111l_opy_(bstack111l1ll_opy_ (u"ࠫࡷࡵࡢࡰࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬଢ଼"))
  if bstack11llll111_opy_ == bstack111l1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ୞") and len(bstack1llll1ll11_opy_) == 0:
    bstack1llll1ll11_opy_ = bstack1l1ll111l_opy_(bstack111l1ll_opy_ (u"࠭ࡰࡸࡡࡳࡽࡹ࡫ࡳࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫୟ"))
    if len(bstack1llll1ll11_opy_) == 0:
      bstack1llll1ll11_opy_ = bstack1l1ll111l_opy_(bstack111l1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡱࡲࡳࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ୠ"))
  bstack1l11l11111_opy_ = bstack111l1ll_opy_ (u"ࠨࠩୡ")
  if len(bstack11l111l11l_opy_) > 0:
    bstack1l11l11111_opy_ = bstack1ll11111ll_opy_(bstack11l111l11l_opy_)
  elif len(bstack1llll1ll11_opy_) > 0:
    bstack1l11l11111_opy_ = bstack1ll11111ll_opy_(bstack1llll1ll11_opy_)
  elif len(bstack11l11l111_opy_) > 0:
    bstack1l11l11111_opy_ = bstack1ll11111ll_opy_(bstack11l11l111_opy_)
  elif len(bstack1ll11llll_opy_) > 0:
    bstack1l11l11111_opy_ = bstack1ll11111ll_opy_(bstack1ll11llll_opy_)
  if bool(bstack1l11l11111_opy_):
    bstack1l1lll1ll1_opy_(bstack1l11l11111_opy_)
  else:
    bstack1l1lll1ll1_opy_()
  bstack11ll11l11l_opy_(bstack11l111l11_opy_, logger)
  bstack1llllll1l1_opy_.bstack1l1l1ll1_opy_(CONFIG)
  if len(bstack11l11l111_opy_) > 0:
    sys.exit(len(bstack11l11l111_opy_))
def bstack1l111ll11_opy_(bstack11ll1lll11_opy_, frame):
  global bstack1111lll1_opy_
  logger.error(bstack1l1lll111_opy_)
  bstack1111lll1_opy_.bstack11llll1ll1_opy_(bstack111l1ll_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡑࡳࠬୢ"), bstack11ll1lll11_opy_)
  if hasattr(signal, bstack111l1ll_opy_ (u"ࠪࡗ࡮࡭࡮ࡢ࡮ࡶࠫୣ")):
    bstack1111lll1_opy_.bstack11llll1ll1_opy_(bstack111l1ll_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡘ࡯ࡧ࡯ࡣ࡯ࠫ୤"), signal.Signals(bstack11ll1lll11_opy_).name)
  else:
    bstack1111lll1_opy_.bstack11llll1ll1_opy_(bstack111l1ll_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬ୥"), bstack111l1ll_opy_ (u"࠭ࡓࡊࡉࡘࡒࡐࡔࡏࡘࡐࠪ୦"))
  bstack1llll1ll1l_opy_ = os.environ.get(bstack111l1ll_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨ୧"))
  if bstack1llll1ll1l_opy_ == bstack111l1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ୨"):
    bstack1ll11l1l_opy_.stop(bstack1111lll1_opy_.get_property(bstack111l1ll_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡖ࡭࡬ࡴࡡ࡭ࠩ୩")))
  bstack11lll1ll1_opy_()
  sys.exit(1)
def bstack111ll1ll1_opy_(err):
  logger.critical(bstack11ll11l11_opy_.format(str(err)))
  bstack1l1lll1ll1_opy_(bstack11ll11l11_opy_.format(str(err)), True)
  atexit.unregister(bstack11lll1ll1_opy_)
  bstack1lll1111ll_opy_()
  sys.exit(1)
def bstack1lll111l1_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1l1lll1ll1_opy_(message, True)
  atexit.unregister(bstack11lll1ll1_opy_)
  bstack1lll1111ll_opy_()
  sys.exit(1)
def bstack1l1llll1l1_opy_():
  global CONFIG
  global bstack11llllll1_opy_
  global bstack1111l1l11_opy_
  global bstack11ll1l111_opy_
  CONFIG = bstack11l11ll111_opy_()
  load_dotenv(CONFIG.get(bstack111l1ll_opy_ (u"ࠪࡩࡳࡼࡆࡪ࡮ࡨࠫ୪")))
  bstack1l1l1l1l1l_opy_()
  bstack1l1l111ll1_opy_()
  CONFIG = bstack111l11l1l_opy_(CONFIG)
  update(CONFIG, bstack1111l1l11_opy_)
  update(CONFIG, bstack11llllll1_opy_)
  CONFIG = bstack11l1llll11_opy_(CONFIG)
  bstack11ll1l111_opy_ = bstack11ll1lll1_opy_(CONFIG)
  os.environ[bstack111l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧ୫")] = bstack11ll1l111_opy_.__str__()
  bstack1111lll1_opy_.bstack11llll1ll1_opy_(bstack111l1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭୬"), bstack11ll1l111_opy_)
  if (bstack111l1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ୭") in CONFIG and bstack111l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ୮") in bstack11llllll1_opy_) or (
          bstack111l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ୯") in CONFIG and bstack111l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ୰") not in bstack1111l1l11_opy_):
    if os.getenv(bstack111l1ll_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧୱ")):
      CONFIG[bstack111l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭୲")] = os.getenv(bstack111l1ll_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩ୳"))
    else:
      bstack11l1ll111l_opy_()
  elif (bstack111l1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ୴") not in CONFIG and bstack111l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ୵") in CONFIG) or (
          bstack111l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ୶") in bstack1111l1l11_opy_ and bstack111l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ୷") not in bstack11llllll1_opy_):
    del (CONFIG[bstack111l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ୸")])
  if bstack11llll11ll_opy_(CONFIG):
    bstack111ll1ll1_opy_(bstack1l11lll1l1_opy_)
  bstack11llll1l1l_opy_()
  bstack1lllll1lll_opy_()
  if bstack1l11l1111_opy_:
    CONFIG[bstack111l1ll_opy_ (u"ࠫࡦࡶࡰࠨ୹")] = bstack1llll1lll1_opy_(CONFIG)
    logger.info(bstack11l1lll111_opy_.format(CONFIG[bstack111l1ll_opy_ (u"ࠬࡧࡰࡱࠩ୺")]))
  if not bstack11ll1l111_opy_:
    CONFIG[bstack111l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ୻")] = [{}]
def bstack1l111l1l11_opy_(config, bstack11l1l111ll_opy_):
  global CONFIG
  global bstack1l11l1111_opy_
  CONFIG = config
  bstack1l11l1111_opy_ = bstack11l1l111ll_opy_
def bstack1lllll1lll_opy_():
  global CONFIG
  global bstack1l11l1111_opy_
  if bstack111l1ll_opy_ (u"ࠧࡢࡲࡳࠫ୼") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1lll111l1_opy_(e, bstack1ll1l1ll1_opy_)
    bstack1l11l1111_opy_ = True
    bstack1111lll1_opy_.bstack11llll1ll1_opy_(bstack111l1ll_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ୽"), True)
def bstack1llll1lll1_opy_(config):
  bstack11lll1ll1l_opy_ = bstack111l1ll_opy_ (u"ࠩࠪ୾")
  app = config[bstack111l1ll_opy_ (u"ࠪࡥࡵࡶࠧ୿")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack111l1l11l_opy_:
      if os.path.exists(app):
        bstack11lll1ll1l_opy_ = bstack1111ll111_opy_(config, app)
      elif bstack1ll11l1ll_opy_(app):
        bstack11lll1ll1l_opy_ = app
      else:
        bstack111ll1ll1_opy_(bstack1ll1l1l111_opy_.format(app))
    else:
      if bstack1ll11l1ll_opy_(app):
        bstack11lll1ll1l_opy_ = app
      elif os.path.exists(app):
        bstack11lll1ll1l_opy_ = bstack1111ll111_opy_(app)
      else:
        bstack111ll1ll1_opy_(bstack11ll11l1ll_opy_)
  else:
    if len(app) > 2:
      bstack111ll1ll1_opy_(bstack11lll1l1l1_opy_)
    elif len(app) == 2:
      if bstack111l1ll_opy_ (u"ࠫࡵࡧࡴࡩࠩ஀") in app and bstack111l1ll_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨ஁") in app:
        if os.path.exists(app[bstack111l1ll_opy_ (u"࠭ࡰࡢࡶ࡫ࠫஂ")]):
          bstack11lll1ll1l_opy_ = bstack1111ll111_opy_(config, app[bstack111l1ll_opy_ (u"ࠧࡱࡣࡷ࡬ࠬஃ")], app[bstack111l1ll_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠫ஄")])
        else:
          bstack111ll1ll1_opy_(bstack1ll1l1l111_opy_.format(app))
      else:
        bstack111ll1ll1_opy_(bstack11lll1l1l1_opy_)
    else:
      for key in app:
        if key in bstack1111111l1_opy_:
          if key == bstack111l1ll_opy_ (u"ࠩࡳࡥࡹ࡮ࠧஅ"):
            if os.path.exists(app[key]):
              bstack11lll1ll1l_opy_ = bstack1111ll111_opy_(config, app[key])
            else:
              bstack111ll1ll1_opy_(bstack1ll1l1l111_opy_.format(app))
          else:
            bstack11lll1ll1l_opy_ = app[key]
        else:
          bstack111ll1ll1_opy_(bstack1lllll1l1l_opy_)
  return bstack11lll1ll1l_opy_
def bstack1ll11l1ll_opy_(bstack11lll1ll1l_opy_):
  import re
  bstack1l11111l1l_opy_ = re.compile(bstack111l1ll_opy_ (u"ࡵࠦࡣࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫࠦࠥஆ"))
  bstack1111l111l_opy_ = re.compile(bstack111l1ll_opy_ (u"ࡶࠧࡤ࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬ࠲࡟ࡦ࠳ࡺࡂ࠯࡝࠴࠲࠿࡜ࡠ࠰࡟࠱ࡢ࠰ࠤࠣஇ"))
  if bstack111l1ll_opy_ (u"ࠬࡨࡳ࠻࠱࠲ࠫஈ") in bstack11lll1ll1l_opy_ or re.fullmatch(bstack1l11111l1l_opy_, bstack11lll1ll1l_opy_) or re.fullmatch(bstack1111l111l_opy_, bstack11lll1ll1l_opy_):
    return True
  else:
    return False
def bstack1111ll111_opy_(config, path, bstack1ll1111ll_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack111l1ll_opy_ (u"࠭ࡲࡣࠩஉ")).read()).hexdigest()
  bstack1l1llll11_opy_ = bstack1l1111lll_opy_(md5_hash)
  bstack11lll1ll1l_opy_ = None
  if bstack1l1llll11_opy_:
    logger.info(bstack11lllll1l1_opy_.format(bstack1l1llll11_opy_, md5_hash))
    return bstack1l1llll11_opy_
  bstack1l1l1ll1l_opy_ = MultipartEncoder(
    fields={
      bstack111l1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࠬஊ"): (os.path.basename(path), open(os.path.abspath(path), bstack111l1ll_opy_ (u"ࠨࡴࡥࠫ஋")), bstack111l1ll_opy_ (u"ࠩࡷࡩࡽࡺ࠯ࡱ࡮ࡤ࡭ࡳ࠭஌")),
      bstack111l1ll_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭஍"): bstack1ll1111ll_opy_
    }
  )
  response = requests.post(bstack1l1111l11l_opy_, data=bstack1l1l1ll1l_opy_,
                           headers={bstack111l1ll_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪஎ"): bstack1l1l1ll1l_opy_.content_type},
                           auth=(config[bstack111l1ll_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧஏ")], config[bstack111l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩஐ")]))
  try:
    res = json.loads(response.text)
    bstack11lll1ll1l_opy_ = res[bstack111l1ll_opy_ (u"ࠧࡢࡲࡳࡣࡺࡸ࡬ࠨ஑")]
    logger.info(bstack1ll1ll1111_opy_.format(bstack11lll1ll1l_opy_))
    bstack11lll1l1ll_opy_(md5_hash, bstack11lll1ll1l_opy_)
  except ValueError as err:
    bstack111ll1ll1_opy_(bstack1l1lllll11_opy_.format(str(err)))
  return bstack11lll1ll1l_opy_
def bstack11llll1l1l_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1ll111ll1_opy_
  bstack1llll1l1_opy_ = 1
  bstack111llllll_opy_ = 1
  if bstack111l1ll_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨஒ") in CONFIG:
    bstack111llllll_opy_ = CONFIG[bstack111l1ll_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩஓ")]
  else:
    bstack111llllll_opy_ = bstack1ll11111l1_opy_(framework_name, args) or 1
  if bstack111l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ஔ") in CONFIG:
    bstack1llll1l1_opy_ = len(CONFIG[bstack111l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧக")])
  bstack1ll111ll1_opy_ = int(bstack111llllll_opy_) * int(bstack1llll1l1_opy_)
def bstack1ll11111l1_opy_(framework_name, args):
  if framework_name == bstack1llll11l1_opy_ and args and bstack111l1ll_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ஖") in args:
      bstack11l1l11ll1_opy_ = args.index(bstack111l1ll_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫ஗"))
      return int(args[bstack11l1l11ll1_opy_ + 1]) or 1
  return 1
def bstack1l1111lll_opy_(md5_hash):
  bstack11lll1lll_opy_ = os.path.join(os.path.expanduser(bstack111l1ll_opy_ (u"ࠧࡿࠩ஘")), bstack111l1ll_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨங"), bstack111l1ll_opy_ (u"ࠩࡤࡴࡵ࡛ࡰ࡭ࡱࡤࡨࡒࡊ࠵ࡉࡣࡶ࡬࠳ࡰࡳࡰࡰࠪச"))
  if os.path.exists(bstack11lll1lll_opy_):
    bstack1lll1lll1l_opy_ = json.load(open(bstack11lll1lll_opy_, bstack111l1ll_opy_ (u"ࠪࡶࡧ࠭஛")))
    if md5_hash in bstack1lll1lll1l_opy_:
      bstack1ll1l11l1l_opy_ = bstack1lll1lll1l_opy_[md5_hash]
      bstack1111lllll_opy_ = datetime.datetime.now()
      bstack11ll111lll_opy_ = datetime.datetime.strptime(bstack1ll1l11l1l_opy_[bstack111l1ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧஜ")], bstack111l1ll_opy_ (u"ࠬࠫࡤ࠰ࠧࡰ࠳ࠪ࡟ࠠࠦࡊ࠽ࠩࡒࡀࠥࡔࠩ஝"))
      if (bstack1111lllll_opy_ - bstack11ll111lll_opy_).days > 30:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack1ll1l11l1l_opy_[bstack111l1ll_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫஞ")]):
        return None
      return bstack1ll1l11l1l_opy_[bstack111l1ll_opy_ (u"ࠧࡪࡦࠪட")]
  else:
    return None
def bstack11lll1l1ll_opy_(md5_hash, bstack11lll1ll1l_opy_):
  bstack11ll1l1l11_opy_ = os.path.join(os.path.expanduser(bstack111l1ll_opy_ (u"ࠨࢀࠪ஠")), bstack111l1ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ஡"))
  if not os.path.exists(bstack11ll1l1l11_opy_):
    os.makedirs(bstack11ll1l1l11_opy_)
  bstack11lll1lll_opy_ = os.path.join(os.path.expanduser(bstack111l1ll_opy_ (u"ࠪࢂࠬ஢")), bstack111l1ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫண"), bstack111l1ll_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭த"))
  bstack1ll11ll1l1_opy_ = {
    bstack111l1ll_opy_ (u"࠭ࡩࡥࠩ஥"): bstack11lll1ll1l_opy_,
    bstack111l1ll_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ஦"): datetime.datetime.strftime(datetime.datetime.now(), bstack111l1ll_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬ஧")),
    bstack111l1ll_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧந"): str(__version__)
  }
  if os.path.exists(bstack11lll1lll_opy_):
    bstack1lll1lll1l_opy_ = json.load(open(bstack11lll1lll_opy_, bstack111l1ll_opy_ (u"ࠪࡶࡧ࠭ன")))
  else:
    bstack1lll1lll1l_opy_ = {}
  bstack1lll1lll1l_opy_[md5_hash] = bstack1ll11ll1l1_opy_
  with open(bstack11lll1lll_opy_, bstack111l1ll_opy_ (u"ࠦࡼ࠱ࠢப")) as outfile:
    json.dump(bstack1lll1lll1l_opy_, outfile)
def bstack11ll1ll111_opy_(self):
  return
def bstack11ll1l1111_opy_(self):
  return
def bstack11l111ll1l_opy_(self):
  global bstack1l1111llll_opy_
  bstack1l1111llll_opy_(self)
def bstack1l1l11l11l_opy_():
  global bstack11l11l11ll_opy_
  bstack11l11l11ll_opy_ = True
def bstack111l1l1ll_opy_(self):
  global bstack111llllll1_opy_
  global bstack11l1lllll_opy_
  global bstack11ll11lll1_opy_
  try:
    if bstack111l1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ஫") in bstack111llllll1_opy_ and self.session_id != None and bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡗࡹࡧࡴࡶࡵࠪ஬"), bstack111l1ll_opy_ (u"ࠧࠨ஭")) != bstack111l1ll_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩம"):
      bstack1ll1lllll_opy_ = bstack111l1ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩய") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack111l1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪர")
      if bstack1ll1lllll_opy_ == bstack111l1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫற"):
        bstack111l1ll11_opy_(logger)
      if self != None:
        bstack11ll111l1l_opy_(self, bstack1ll1lllll_opy_, bstack111l1ll_opy_ (u"ࠬ࠲ࠠࠨல").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack111l1ll_opy_ (u"࠭ࠧள")
    if bstack111l1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧழ") in bstack111llllll1_opy_ and getattr(threading.current_thread(), bstack111l1ll_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧவ"), None):
      bstack111l111l_opy_.bstack111llll1_opy_(self, bstack1lllll111l_opy_, logger, wait=True)
    if bstack111l1ll_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩஶ") in bstack111llllll1_opy_:
      if not threading.currentThread().behave_test_status:
        bstack11ll111l1l_opy_(self, bstack111l1ll_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥஷ"))
      bstack11l1lll1l1_opy_.bstack1llll111l_opy_(self)
  except Exception as e:
    logger.debug(bstack111l1ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࠧஸ") + str(e))
  bstack11ll11lll1_opy_(self)
  self.session_id = None
def bstack1l111lllll_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack1ll11111l_opy_
    global bstack111llllll1_opy_
    command_executor = kwargs.get(bstack111l1ll_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠨஹ"), bstack111l1ll_opy_ (u"࠭ࠧ஺"))
    bstack11ll111l1_opy_ = False
    if type(command_executor) == str and bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪ஻") in command_executor:
      bstack11ll111l1_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫ஼") in str(getattr(command_executor, bstack111l1ll_opy_ (u"ࠩࡢࡹࡷࡲࠧ஽"), bstack111l1ll_opy_ (u"ࠪࠫா"))):
      bstack11ll111l1_opy_ = True
    else:
      return bstack1ll11ll11_opy_(self, *args, **kwargs)
    if bstack11ll111l1_opy_:
      bstack111lllll1_opy_ = bstack11lll1111l_opy_.bstack1ll1l11ll_opy_(CONFIG, bstack111llllll1_opy_)
      if kwargs.get(bstack111l1ll_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬி")):
        kwargs[bstack111l1ll_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ீ")] = bstack1ll11111l_opy_(kwargs[bstack111l1ll_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧு")], bstack111llllll1_opy_, bstack111lllll1_opy_)
      elif kwargs.get(bstack111l1ll_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧூ")):
        kwargs[bstack111l1ll_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ௃")] = bstack1ll11111l_opy_(kwargs[bstack111l1ll_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ௄")], bstack111llllll1_opy_, bstack111lllll1_opy_)
  except Exception as e:
    logger.error(bstack111l1ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡘࡊࡋࠡࡥࡤࡴࡸࡀࠠࡼࡿࠥ௅").format(str(e)))
  return bstack1ll11ll11_opy_(self, *args, **kwargs)
def bstack1l1ll1111_opy_(self, command_executor=bstack111l1ll_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳࠶࠸࠷࠯࠲࠱࠴࠳࠷࠺࠵࠶࠷࠸ࠧெ"), *args, **kwargs):
  bstack11l111l1ll_opy_ = bstack1l111lllll_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1l1l1l11_opy_.on():
    return bstack11l111l1ll_opy_
  try:
    logger.debug(bstack111l1ll_opy_ (u"ࠬࡉ࡯࡮࡯ࡤࡲࡩࠦࡅࡹࡧࡦࡹࡹࡵࡲࠡࡹ࡫ࡩࡳࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢ࡬ࡷࠥ࡬ࡡ࡭ࡵࡨࠤ࠲ࠦࡻࡾࠩே").format(str(command_executor)))
    logger.debug(bstack111l1ll_opy_ (u"࠭ࡈࡶࡤ࡙ࠣࡗࡒࠠࡪࡵࠣ࠱ࠥࢁࡽࠨை").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪ௉") in command_executor._url:
      bstack1111lll1_opy_.bstack11llll1ll1_opy_(bstack111l1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩொ"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬோ") in command_executor):
    bstack1111lll1_opy_.bstack11llll1ll1_opy_(bstack111l1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫௌ"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1lllll1l11_opy_ = getattr(threading.current_thread(), bstack111l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡘࡪࡹࡴࡎࡧࡷࡥ்ࠬ"), None)
  if bstack111l1ll_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ௎") in bstack111llllll1_opy_ or bstack111l1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ௏") in bstack111llllll1_opy_:
    bstack1ll11l1l_opy_.bstack11lll1l11l_opy_(self)
  if bstack111l1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧௐ") in bstack111llllll1_opy_ and bstack1lllll1l11_opy_ and bstack1lllll1l11_opy_.get(bstack111l1ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ௑"), bstack111l1ll_opy_ (u"ࠩࠪ௒")) == bstack111l1ll_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫ௓"):
    bstack1ll11l1l_opy_.bstack11lll1l11l_opy_(self)
  return bstack11l111l1ll_opy_
def bstack11llllll11_opy_(args):
  return bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠬ௔") in str(args)
def bstack1l1111l111_opy_(self, driver_command, *args, **kwargs):
  global bstack1l1111ll1l_opy_
  global bstack11ll1ll1l_opy_
  bstack1llll11ll1_opy_ = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ௕"), None) and bstack1ll111l1_opy_(
          threading.current_thread(), bstack111l1ll_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ௖"), None)
  bstack1l1l1l111l_opy_ = getattr(self, bstack111l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧௗ"), None) != None and getattr(self, bstack111l1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨ௘"), None) == True
  if not bstack11ll1ll1l_opy_ and bstack11ll1l111_opy_ and bstack111l1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ௙") in CONFIG and CONFIG[bstack111l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ௚")] == True and bstack1ll1l1l11l_opy_.bstack1l11l1l111_opy_(driver_command) and (bstack1l1l1l111l_opy_ or bstack1llll11ll1_opy_) and not bstack11llllll11_opy_(args):
    try:
      bstack11ll1ll1l_opy_ = True
      logger.debug(bstack111l1ll_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡦࡰࡴࠣࡿࢂ࠭௛").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack111l1ll_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡨࡶ࡫ࡵࡲ࡮ࠢࡶࡧࡦࡴࠠࡼࡿࠪ௜").format(str(err)))
    bstack11ll1ll1l_opy_ = False
  response = bstack1l1111ll1l_opy_(self, driver_command, *args, **kwargs)
  if (bstack111l1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ௝") in str(bstack111llllll1_opy_).lower() or bstack111l1ll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ௞") in str(bstack111llllll1_opy_).lower()) and bstack1l1l1l11_opy_.on():
    try:
      if driver_command == bstack111l1ll_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬ௟"):
        bstack1ll11l1l_opy_.bstack1ll1l1llll_opy_({
            bstack111l1ll_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ௠"): response[bstack111l1ll_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩ௡")],
            bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ௢"): bstack1ll11l1l_opy_.current_test_uuid() if bstack1ll11l1l_opy_.current_test_uuid() else bstack1l1l1l11_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
def bstack11l1l11l11_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack11l1lllll_opy_
  global bstack1l1111l1ll_opy_
  global bstack11lll1ll11_opy_
  global bstack11l11l1l11_opy_
  global bstack1l1llllll_opy_
  global bstack111llllll1_opy_
  global bstack1ll11ll11_opy_
  global bstack1ll111l11l_opy_
  global bstack1llll11l11_opy_
  global bstack1lllll111l_opy_
  CONFIG[bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ௣")] = str(bstack111llllll1_opy_) + str(__version__)
  bstack111111l11_opy_ = os.environ[bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ௤")]
  bstack111lllll1_opy_ = bstack11lll1111l_opy_.bstack1ll1l11ll_opy_(CONFIG, bstack111llllll1_opy_)
  CONFIG[bstack111l1ll_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪ௥")] = bstack111111l11_opy_
  CONFIG[bstack111l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪ௦")] = bstack111lllll1_opy_
  command_executor = bstack1ll1111ll1_opy_()
  logger.debug(bstack1lll11111l_opy_.format(command_executor))
  proxy = bstack1ll1ll1lll_opy_(CONFIG, proxy)
  bstack1l11l1111l_opy_ = 0 if bstack1l1111l1ll_opy_ < 0 else bstack1l1111l1ll_opy_
  try:
    if bstack11l11l1l11_opy_ is True:
      bstack1l11l1111l_opy_ = int(multiprocessing.current_process().name)
    elif bstack1l1llllll_opy_ is True:
      bstack1l11l1111l_opy_ = int(threading.current_thread().name)
  except:
    bstack1l11l1111l_opy_ = 0
  bstack1lll1l11ll_opy_ = bstack1111l1l1l_opy_(CONFIG, bstack1l11l1111l_opy_)
  logger.debug(bstack1lllllllll_opy_.format(str(bstack1lll1l11ll_opy_)))
  if bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭௧") in CONFIG and bstack1l1l111lll_opy_(CONFIG[bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ௨")]):
    bstack1ll1lll1l_opy_(bstack1lll1l11ll_opy_)
  if bstack1111111l_opy_.bstack11ll11l1l_opy_(CONFIG, bstack1l11l1111l_opy_) and bstack1111111l_opy_.bstack11l1111l11_opy_(bstack1lll1l11ll_opy_, options, desired_capabilities):
    threading.current_thread().a11yPlatform = True
    bstack1111111l_opy_.set_capabilities(bstack1lll1l11ll_opy_, CONFIG)
  if desired_capabilities:
    bstack1l1ll11ll_opy_ = bstack111l11l1l_opy_(desired_capabilities)
    bstack1l1ll11ll_opy_[bstack111l1ll_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫ௩")] = bstack1l1lll1ll_opy_(CONFIG)
    bstack1l1llll111_opy_ = bstack1111l1l1l_opy_(bstack1l1ll11ll_opy_)
    if bstack1l1llll111_opy_:
      bstack1lll1l11ll_opy_ = update(bstack1l1llll111_opy_, bstack1lll1l11ll_opy_)
    desired_capabilities = None
  if options:
    bstack111ll1lll_opy_(options, bstack1lll1l11ll_opy_)
  if not options:
    options = bstack1111lll1l_opy_(bstack1lll1l11ll_opy_)
  bstack1lllll111l_opy_ = CONFIG.get(bstack111l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ௪"))[bstack1l11l1111l_opy_]
  if proxy and bstack11lll1111_opy_() >= version.parse(bstack111l1ll_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭௫")):
    options.proxy(proxy)
  if options and bstack11lll1111_opy_() >= version.parse(bstack111l1ll_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭௬")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack11lll1111_opy_() < version.parse(bstack111l1ll_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧ௭")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1lll1l11ll_opy_)
  logger.info(bstack1llllll111_opy_)
  if bstack11lll1111_opy_() >= version.parse(bstack111l1ll_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩ௮")):
    bstack1ll11ll11_opy_(self, command_executor=command_executor,
              options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
  elif bstack11lll1111_opy_() >= version.parse(bstack111l1ll_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩ௯")):
    bstack1ll11ll11_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities, options=options,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  elif bstack11lll1111_opy_() >= version.parse(bstack111l1ll_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫ௰")):
    bstack1ll11ll11_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack1ll11ll11_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive)
  try:
    bstack1111l1111_opy_ = bstack111l1ll_opy_ (u"ࠬ࠭௱")
    if bstack11lll1111_opy_() >= version.parse(bstack111l1ll_opy_ (u"࠭࠴࠯࠲࠱࠴ࡧ࠷ࠧ௲")):
      bstack1111l1111_opy_ = self.caps.get(bstack111l1ll_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢ௳"))
    else:
      bstack1111l1111_opy_ = self.capabilities.get(bstack111l1ll_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣ௴"))
    if bstack1111l1111_opy_:
      bstack1l1l111l1l_opy_(bstack1111l1111_opy_)
      if bstack11lll1111_opy_() <= version.parse(bstack111l1ll_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩ௵")):
        self.command_executor._url = bstack111l1ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦ௶") + bstack11111l1l1_opy_ + bstack111l1ll_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣ௷")
      else:
        self.command_executor._url = bstack111l1ll_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢ௸") + bstack1111l1111_opy_ + bstack111l1ll_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢ௹")
      logger.debug(bstack1ll11l1ll1_opy_.format(bstack1111l1111_opy_))
    else:
      logger.debug(bstack1lll1ll11_opy_.format(bstack111l1ll_opy_ (u"ࠢࡐࡲࡷ࡭ࡲࡧ࡬ࠡࡊࡸࡦࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤࠣ௺")))
  except Exception as e:
    logger.debug(bstack1lll1ll11_opy_.format(e))
  if bstack111l1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ௻") in bstack111llllll1_opy_:
    bstack1ll111l1l_opy_(bstack1l1111l1ll_opy_, bstack1llll11l11_opy_)
  bstack11l1lllll_opy_ = self.session_id
  if bstack111l1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ௼") in bstack111llllll1_opy_ or bstack111l1ll_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ௽") in bstack111llllll1_opy_ or bstack111l1ll_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ௾") in bstack111llllll1_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack1lllll1l11_opy_ = getattr(threading.current_thread(), bstack111l1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࡙࡫ࡳࡵࡏࡨࡸࡦ࠭௿"), None)
  if bstack111l1ll_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ఀ") in bstack111llllll1_opy_ or bstack111l1ll_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ఁ") in bstack111llllll1_opy_:
    bstack1ll11l1l_opy_.bstack11lll1l11l_opy_(self)
  if bstack111l1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨం") in bstack111llllll1_opy_ and bstack1lllll1l11_opy_ and bstack1lllll1l11_opy_.get(bstack111l1ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩః"), bstack111l1ll_opy_ (u"ࠪࠫఄ")) == bstack111l1ll_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬఅ"):
    bstack1ll11l1l_opy_.bstack11lll1l11l_opy_(self)
  bstack1ll111l11l_opy_.append(self)
  if bstack111l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨఆ") in CONFIG and bstack111l1ll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫఇ") in CONFIG[bstack111l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪఈ")][bstack1l11l1111l_opy_]:
    bstack11lll1ll11_opy_ = CONFIG[bstack111l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫఉ")][bstack1l11l1111l_opy_][bstack111l1ll_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧఊ")]
  logger.debug(bstack111ll11ll_opy_.format(bstack11l1lllll_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack11ll11ll1l_opy_
    def bstack1l11lll11_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack111l11111_opy_
      if(bstack111l1ll_opy_ (u"ࠥ࡭ࡳࡪࡥࡹ࠰࡭ࡷࠧఋ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack111l1ll_opy_ (u"ࠫࢃ࠭ఌ")), bstack111l1ll_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ఍"), bstack111l1ll_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨఎ")), bstack111l1ll_opy_ (u"ࠧࡸࠩఏ")) as fp:
          fp.write(bstack111l1ll_opy_ (u"ࠣࠤఐ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack111l1ll_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦ఑")))):
          with open(args[1], bstack111l1ll_opy_ (u"ࠪࡶࠬఒ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack111l1ll_opy_ (u"ࠫࡦࡹࡹ࡯ࡥࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࡥ࡮ࡦࡹࡓࡥ࡬࡫ࠨࡤࡱࡱࡸࡪࡾࡴ࠭ࠢࡳࡥ࡬࡫ࠠ࠾ࠢࡹࡳ࡮ࡪࠠ࠱ࠫࠪఓ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1lll1lllll_opy_)
            if bstack111l1ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩఔ") in CONFIG and str(CONFIG[bstack111l1ll_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪక")]).lower() != bstack111l1ll_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ఖ"):
                bstack11l1l11l1l_opy_ = bstack11ll11ll1l_opy_()
                bstack11111llll_opy_ = bstack111l1ll_opy_ (u"ࠨࠩࠪࠎ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵ࠊࡤࡱࡱࡷࡹࠦࡢࡴࡶࡤࡧࡰࡥࡰࡢࡶ࡫ࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳࡞࠽ࠍࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠴ࡡࡀࠐࡣࡰࡰࡶࡸࠥࡶ࡟ࡪࡰࡧࡩࡽࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠴ࡠ࠿ࠏࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡹ࡬ࡪࡥࡨࠬ࠵࠲ࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࠬ࠿ࠏࡩ࡯࡯ࡵࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬ࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ࠭ࡀࠐࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴࡬ࡢࡷࡱࡧ࡭ࠦ࠽ࠡࡣࡶࡽࡳࡩࠠࠩ࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳࠪࠢࡀࡂࠥࢁࡻࠋࠢࠣࡰࡪࡺࠠࡤࡣࡳࡷࡀࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࡴࡳࡻࠣࡿࢀࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࡦࡥࡵࡹࠠ࠾ࠢࡍࡗࡔࡔ࠮ࡱࡣࡵࡷࡪ࠮ࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶ࠭ࡀࠐࠠࠡࡿࢀࠤࡨࡧࡴࡤࡪࠣࠬࡪࡾࠩࠡࡽࡾࠎࠥࠦࠠࠡࡥࡲࡲࡸࡵ࡬ࡦ࠰ࡨࡶࡷࡵࡲࠩࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ࠽ࠦ࠱ࠦࡥࡹࠫ࠾ࠎࠥࠦࡽࡾࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࡶࡪࡺࡵࡳࡰࠣࡥࡼࡧࡩࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰ࡦࡳࡳࡴࡥࡤࡶࠫࡿࢀࠐࠠࠡࠢࠣࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺ࠺ࠡࠩࡾࡧࡩࡶࡕࡳ࡮ࢀࠫࠥ࠱ࠠࡦࡰࡦࡳࡩ࡫ࡕࡓࡋࡆࡳࡲࡶ࡯࡯ࡧࡱࡸ࠭ࡐࡓࡐࡐ࠱ࡷࡹࡸࡩ࡯ࡩ࡬ࡪࡾ࠮ࡣࡢࡲࡶ࠭࠮࠲ࠊࠡࠢࠣࠤ࠳࠴࠮࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹࠊࠡࠢࢀࢁ࠮ࡁࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠎࢂࢃ࠻ࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠎ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵ࠊࠨࠩࠪగ").format(bstack11l1l11l1l_opy_=bstack11l1l11l1l_opy_)
            lines.insert(1, bstack11111llll_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack111l1ll_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦఘ")), bstack111l1ll_opy_ (u"ࠪࡻࠬఙ")) as bstack1l1ll1l1ll_opy_:
              bstack1l1ll1l1ll_opy_.writelines(lines)
        CONFIG[bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭చ")] = str(bstack111llllll1_opy_) + str(__version__)
        bstack111111l11_opy_ = os.environ[bstack111l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪఛ")]
        bstack111lllll1_opy_ = bstack11lll1111l_opy_.bstack1ll1l11ll_opy_(CONFIG, bstack111llllll1_opy_)
        CONFIG[bstack111l1ll_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩజ")] = bstack111111l11_opy_
        CONFIG[bstack111l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩఝ")] = bstack111lllll1_opy_
        bstack1l11l1111l_opy_ = 0 if bstack1l1111l1ll_opy_ < 0 else bstack1l1111l1ll_opy_
        try:
          if bstack11l11l1l11_opy_ is True:
            bstack1l11l1111l_opy_ = int(multiprocessing.current_process().name)
          elif bstack1l1llllll_opy_ is True:
            bstack1l11l1111l_opy_ = int(threading.current_thread().name)
        except:
          bstack1l11l1111l_opy_ = 0
        CONFIG[bstack111l1ll_opy_ (u"ࠣࡷࡶࡩ࡜࠹ࡃࠣఞ")] = False
        CONFIG[bstack111l1ll_opy_ (u"ࠤ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣట")] = True
        bstack1lll1l11ll_opy_ = bstack1111l1l1l_opy_(CONFIG, bstack1l11l1111l_opy_)
        logger.debug(bstack1lllllllll_opy_.format(str(bstack1lll1l11ll_opy_)))
        if CONFIG.get(bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧఠ")):
          bstack1ll1lll1l_opy_(bstack1lll1l11ll_opy_)
        if bstack111l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧడ") in CONFIG and bstack111l1ll_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪఢ") in CONFIG[bstack111l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩణ")][bstack1l11l1111l_opy_]:
          bstack11lll1ll11_opy_ = CONFIG[bstack111l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪత")][bstack1l11l1111l_opy_][bstack111l1ll_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭థ")]
        args.append(os.path.join(os.path.expanduser(bstack111l1ll_opy_ (u"ࠩࢁࠫద")), bstack111l1ll_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪధ"), bstack111l1ll_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭న")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1lll1l11ll_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack111l1ll_opy_ (u"ࠧ࡯࡮ࡥࡧࡻࡣࡧࡹࡴࡢࡥ࡮࠲࡯ࡹࠢ఩"))
      bstack111l11111_opy_ = True
      return bstack1llll1111l_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack11l1l1111_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack1l1111l1ll_opy_
    global bstack11lll1ll11_opy_
    global bstack11l11l1l11_opy_
    global bstack1l1llllll_opy_
    global bstack111llllll1_opy_
    CONFIG[bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨప")] = str(bstack111llllll1_opy_) + str(__version__)
    bstack111111l11_opy_ = os.environ[bstack111l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬఫ")]
    bstack111lllll1_opy_ = bstack11lll1111l_opy_.bstack1ll1l11ll_opy_(CONFIG, bstack111llllll1_opy_)
    CONFIG[bstack111l1ll_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫబ")] = bstack111111l11_opy_
    CONFIG[bstack111l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫభ")] = bstack111lllll1_opy_
    bstack1l11l1111l_opy_ = 0 if bstack1l1111l1ll_opy_ < 0 else bstack1l1111l1ll_opy_
    try:
      if bstack11l11l1l11_opy_ is True:
        bstack1l11l1111l_opy_ = int(multiprocessing.current_process().name)
      elif bstack1l1llllll_opy_ is True:
        bstack1l11l1111l_opy_ = int(threading.current_thread().name)
    except:
      bstack1l11l1111l_opy_ = 0
    CONFIG[bstack111l1ll_opy_ (u"ࠥ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤమ")] = True
    bstack1lll1l11ll_opy_ = bstack1111l1l1l_opy_(CONFIG, bstack1l11l1111l_opy_)
    logger.debug(bstack1lllllllll_opy_.format(str(bstack1lll1l11ll_opy_)))
    if CONFIG.get(bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨయ")):
      bstack1ll1lll1l_opy_(bstack1lll1l11ll_opy_)
    if bstack111l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨర") in CONFIG and bstack111l1ll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫఱ") in CONFIG[bstack111l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪల")][bstack1l11l1111l_opy_]:
      bstack11lll1ll11_opy_ = CONFIG[bstack111l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫళ")][bstack1l11l1111l_opy_][bstack111l1ll_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧఴ")]
    import urllib
    import json
    if bstack111l1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧవ") in CONFIG and str(CONFIG[bstack111l1ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨశ")]).lower() != bstack111l1ll_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫష"):
        bstack11l1ll11ll_opy_ = bstack11ll11ll1l_opy_()
        bstack11l1l11l1l_opy_ = bstack11l1ll11ll_opy_ + urllib.parse.quote(json.dumps(bstack1lll1l11ll_opy_))
    else:
        bstack11l1l11l1l_opy_ = bstack111l1ll_opy_ (u"࠭ࡷࡴࡵ࠽࠳࠴ࡩࡤࡱ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡁࡦࡥࡵࡹ࠽ࠨస") + urllib.parse.quote(json.dumps(bstack1lll1l11ll_opy_))
    browser = self.connect(bstack11l1l11l1l_opy_)
    return browser
except Exception as e:
    pass
def bstack11lll111ll_opy_():
    global bstack111l11111_opy_
    global bstack111llllll1_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1l111111l1_opy_
        global bstack1111lll1_opy_
        if not bstack11ll1l111_opy_:
          global bstack1l111ll111_opy_
          if not bstack1l111ll111_opy_:
            from bstack_utils.helper import bstack1ll11l111l_opy_, bstack1l1l1111ll_opy_, bstack111l11l11_opy_
            bstack1l111ll111_opy_ = bstack1ll11l111l_opy_()
            bstack1l1l1111ll_opy_(bstack111llllll1_opy_)
            bstack111lllll1_opy_ = bstack11lll1111l_opy_.bstack1ll1l11ll_opy_(CONFIG, bstack111llllll1_opy_)
            bstack1111lll1_opy_.bstack11llll1ll1_opy_(bstack111l1ll_opy_ (u"ࠢࡑࡎࡄ࡝࡜ࡘࡉࡈࡊࡗࡣࡕࡘࡏࡅࡗࡆࡘࡤࡓࡁࡑࠤహ"), bstack111lllll1_opy_)
          BrowserType.connect = bstack1l111111l1_opy_
          return
        BrowserType.launch = bstack11l1l1111_opy_
        bstack111l11111_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1l11lll11_opy_
      bstack111l11111_opy_ = True
    except Exception as e:
      pass
def bstack1l1lll1l1_opy_(context, bstack11l111111_opy_):
  try:
    context.page.evaluate(bstack111l1ll_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ఺"), bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿࠭఻")+ json.dumps(bstack11l111111_opy_) + bstack111l1ll_opy_ (u"ࠥࢁࢂࠨ఼"))
  except Exception as e:
    logger.debug(bstack111l1ll_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡻࡾࠤఽ"), e)
def bstack11l1111l1_opy_(context, message, level):
  try:
    context.page.evaluate(bstack111l1ll_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨా"), bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫి") + json.dumps(message) + bstack111l1ll_opy_ (u"ࠧ࠭ࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠪీ") + json.dumps(level) + bstack111l1ll_opy_ (u"ࠨࡿࢀࠫు"))
  except Exception as e:
    logger.debug(bstack111l1ll_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠢࡾࢁࠧూ"), e)
def bstack111111111_opy_(self, url):
  global bstack11lll1lll1_opy_
  try:
    bstack1l1ll1l111_opy_(url)
  except Exception as err:
    logger.debug(bstack1ll1l11l11_opy_.format(str(err)))
  try:
    bstack11lll1lll1_opy_(self, url)
  except Exception as e:
    try:
      bstack1l11llll1_opy_ = str(e)
      if any(err_msg in bstack1l11llll1_opy_ for err_msg in bstack11l1111ll1_opy_):
        bstack1l1ll1l111_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1ll1l11l11_opy_.format(str(err)))
    raise e
def bstack1ll1l1ll11_opy_(self):
  global bstack1l11l1llll_opy_
  bstack1l11l1llll_opy_ = self
  return
def bstack1lll11l1ll_opy_(self):
  global bstack1l1l111ll_opy_
  bstack1l1l111ll_opy_ = self
  return
def bstack11ll11ll11_opy_(test_name, bstack1lll1ll1ll_opy_):
  global CONFIG
  if percy.bstack1ll11lll11_opy_() == bstack111l1ll_opy_ (u"ࠥࡸࡷࡻࡥࠣృ"):
    bstack1l111111l_opy_ = os.path.relpath(bstack1lll1ll1ll_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1l111111l_opy_)
    bstack11ll111ll1_opy_ = suite_name + bstack111l1ll_opy_ (u"ࠦ࠲ࠨౄ") + test_name
    threading.current_thread().percySessionName = bstack11ll111ll1_opy_
def bstack11l111llll_opy_(self, test, *args, **kwargs):
  global bstack11l11ll11l_opy_
  test_name = None
  bstack1lll1ll1ll_opy_ = None
  if test:
    test_name = str(test.name)
    bstack1lll1ll1ll_opy_ = str(test.source)
  bstack11ll11ll11_opy_(test_name, bstack1lll1ll1ll_opy_)
  bstack11l11ll11l_opy_(self, test, *args, **kwargs)
def bstack11l1l1l1l_opy_(driver, bstack11ll111ll1_opy_):
  if not bstack111ll1l11_opy_ and bstack11ll111ll1_opy_:
      bstack1ll1111lll_opy_ = {
          bstack111l1ll_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬ౅"): bstack111l1ll_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧె"),
          bstack111l1ll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪే"): {
              bstack111l1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ై"): bstack11ll111ll1_opy_
          }
      }
      bstack1l1ll1ll1_opy_ = bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧ౉").format(json.dumps(bstack1ll1111lll_opy_))
      driver.execute_script(bstack1l1ll1ll1_opy_)
  if bstack11l111ll1_opy_:
      bstack111lll1l1_opy_ = {
          bstack111l1ll_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪొ"): bstack111l1ll_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ో"),
          bstack111l1ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨౌ"): {
              bstack111l1ll_opy_ (u"࠭ࡤࡢࡶࡤ్ࠫ"): bstack11ll111ll1_opy_ + bstack111l1ll_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤࠢࠩ౎"),
              bstack111l1ll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ౏"): bstack111l1ll_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧ౐")
          }
      }
      if bstack11l111ll1_opy_.status == bstack111l1ll_opy_ (u"ࠪࡔࡆ࡙ࡓࠨ౑"):
          bstack1l1ll1lll1_opy_ = bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩ౒").format(json.dumps(bstack111lll1l1_opy_))
          driver.execute_script(bstack1l1ll1lll1_opy_)
          bstack11ll111l1l_opy_(driver, bstack111l1ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ౓"))
      elif bstack11l111ll1_opy_.status == bstack111l1ll_opy_ (u"࠭ࡆࡂࡋࡏࠫ౔"):
          reason = bstack111l1ll_opy_ (u"ౕࠢࠣ")
          bstack11l1l1lll1_opy_ = bstack11ll111ll1_opy_ + bstack111l1ll_opy_ (u"ࠨࠢࡩࡥ࡮ࡲࡥࡥౖࠩ")
          if bstack11l111ll1_opy_.message:
              reason = str(bstack11l111ll1_opy_.message)
              bstack11l1l1lll1_opy_ = bstack11l1l1lll1_opy_ + bstack111l1ll_opy_ (u"ࠩࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸ࠺ࠡࠩ౗") + reason
          bstack111lll1l1_opy_[bstack111l1ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ౘ")] = {
              bstack111l1ll_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪౙ"): bstack111l1ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫౚ"),
              bstack111l1ll_opy_ (u"࠭ࡤࡢࡶࡤࠫ౛"): bstack11l1l1lll1_opy_
          }
          bstack1l1ll1lll1_opy_ = bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬ౜").format(json.dumps(bstack111lll1l1_opy_))
          driver.execute_script(bstack1l1ll1lll1_opy_)
          bstack11ll111l1l_opy_(driver, bstack111l1ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨౝ"), reason)
          bstack1l111l111l_opy_(reason, str(bstack11l111ll1_opy_), str(bstack1l1111l1ll_opy_), logger)
def bstack1l11lll1l_opy_(driver, test):
  if percy.bstack1ll11lll11_opy_() == bstack111l1ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ౞") and percy.bstack1111l1ll1_opy_() == bstack111l1ll_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧ౟"):
      bstack1l1ll1ll11_opy_ = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧౠ"), None)
      bstack11l1l1111l_opy_(driver, bstack1l1ll1ll11_opy_, test)
  if bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩౡ"), None) and bstack1ll111l1_opy_(
          threading.current_thread(), bstack111l1ll_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬౢ"), None):
      logger.info(bstack111l1ll_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠥࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡹࡳࡪࡥࡳࡹࡤࡽ࠳ࠦࠢౣ"))
      bstack1111111l_opy_.bstack111l1111_opy_(driver, name=test.name, path=test.source)
def bstack1l11l1ll1_opy_(test, bstack11ll111ll1_opy_):
    try:
      data = {}
      if test:
        data[bstack111l1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭౤")] = bstack11ll111ll1_opy_
      if bstack11l111ll1_opy_:
        if bstack11l111ll1_opy_.status == bstack111l1ll_opy_ (u"ࠩࡓࡅࡘ࡙ࠧ౥"):
          data[bstack111l1ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ౦")] = bstack111l1ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ౧")
        elif bstack11l111ll1_opy_.status == bstack111l1ll_opy_ (u"ࠬࡌࡁࡊࡎࠪ౨"):
          data[bstack111l1ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭౩")] = bstack111l1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ౪")
          if bstack11l111ll1_opy_.message:
            data[bstack111l1ll_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨ౫")] = str(bstack11l111ll1_opy_.message)
      user = CONFIG[bstack111l1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ౬")]
      key = CONFIG[bstack111l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭౭")]
      url = bstack111l1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࢁࡽ࠻ࡽࢀࡄࡦࡶࡩ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡳࡦࡵࡶ࡭ࡴࡴࡳ࠰ࡽࢀ࠲࡯ࡹ࡯࡯ࠩ౮").format(user, key, bstack11l1lllll_opy_)
      headers = {
        bstack111l1ll_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫ౯"): bstack111l1ll_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ౰"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack1ll1111111_opy_.format(str(e)))
def bstack1lll11l1l_opy_(test, bstack11ll111ll1_opy_):
  global CONFIG
  global bstack1l1l111ll_opy_
  global bstack1l11l1llll_opy_
  global bstack11l1lllll_opy_
  global bstack11l111ll1_opy_
  global bstack11lll1ll11_opy_
  global bstack11lll11l1_opy_
  global bstack1lll11111_opy_
  global bstack1l1ll111ll_opy_
  global bstack111111lll_opy_
  global bstack1ll111l11l_opy_
  global bstack1lllll111l_opy_
  try:
    if not bstack11l1lllll_opy_:
      with open(os.path.join(os.path.expanduser(bstack111l1ll_opy_ (u"ࠧࡿࠩ౱")), bstack111l1ll_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ౲"), bstack111l1ll_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫ౳"))) as f:
        bstack1llll1l1l1_opy_ = json.loads(bstack111l1ll_opy_ (u"ࠥࡿࠧ౴") + f.read().strip() + bstack111l1ll_opy_ (u"ࠫࠧࡾࠢ࠻ࠢࠥࡽࠧ࠭౵") + bstack111l1ll_opy_ (u"ࠧࢃࠢ౶"))
        bstack11l1lllll_opy_ = bstack1llll1l1l1_opy_[str(threading.get_ident())]
  except:
    pass
  if bstack1ll111l11l_opy_:
    for driver in bstack1ll111l11l_opy_:
      if bstack11l1lllll_opy_ == driver.session_id:
        if test:
          bstack1l11lll1l_opy_(driver, test)
        bstack11l1l1l1l_opy_(driver, bstack11ll111ll1_opy_)
  elif bstack11l1lllll_opy_:
    bstack1l11l1ll1_opy_(test, bstack11ll111ll1_opy_)
  if bstack1l1l111ll_opy_:
    bstack1lll11111_opy_(bstack1l1l111ll_opy_)
  if bstack1l11l1llll_opy_:
    bstack1l1ll111ll_opy_(bstack1l11l1llll_opy_)
  if bstack11l11l11ll_opy_:
    bstack111111lll_opy_()
def bstack11ll1l1lll_opy_(self, test, *args, **kwargs):
  bstack11ll111ll1_opy_ = None
  if test:
    bstack11ll111ll1_opy_ = str(test.name)
  bstack1lll11l1l_opy_(test, bstack11ll111ll1_opy_)
  bstack11lll11l1_opy_(self, test, *args, **kwargs)
def bstack1ll1ll111_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1l1111lll1_opy_
  global CONFIG
  global bstack1ll111l11l_opy_
  global bstack11l1lllll_opy_
  bstack1lll1l111l_opy_ = None
  try:
    if bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ౷"), None):
      try:
        if not bstack11l1lllll_opy_:
          with open(os.path.join(os.path.expanduser(bstack111l1ll_opy_ (u"ࠧࡿࠩ౸")), bstack111l1ll_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ౹"), bstack111l1ll_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫ౺"))) as f:
            bstack1llll1l1l1_opy_ = json.loads(bstack111l1ll_opy_ (u"ࠥࡿࠧ౻") + f.read().strip() + bstack111l1ll_opy_ (u"ࠫࠧࡾࠢ࠻ࠢࠥࡽࠧ࠭౼") + bstack111l1ll_opy_ (u"ࠧࢃࠢ౽"))
            bstack11l1lllll_opy_ = bstack1llll1l1l1_opy_[str(threading.get_ident())]
      except:
        pass
      if bstack1ll111l11l_opy_:
        for driver in bstack1ll111l11l_opy_:
          if bstack11l1lllll_opy_ == driver.session_id:
            bstack1lll1l111l_opy_ = driver
    bstack1l11llllll_opy_ = bstack1111111l_opy_.bstack1l111l1l1l_opy_(test.tags)
    if bstack1lll1l111l_opy_:
      threading.current_thread().isA11yTest = bstack1111111l_opy_.bstack11l111l1l_opy_(bstack1lll1l111l_opy_, bstack1l11llllll_opy_)
    else:
      threading.current_thread().isA11yTest = bstack1l11llllll_opy_
  except:
    pass
  bstack1l1111lll1_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack11l111ll1_opy_
  bstack11l111ll1_opy_ = self._test
def bstack1ll11l1111_opy_():
  global bstack11l1111ll_opy_
  try:
    if os.path.exists(bstack11l1111ll_opy_):
      os.remove(bstack11l1111ll_opy_)
  except Exception as e:
    logger.debug(bstack111l1ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡦࡨࡰࡪࡺࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩ౾") + str(e))
def bstack11lllll11_opy_():
  global bstack11l1111ll_opy_
  bstack1lll11ll11_opy_ = {}
  try:
    if not os.path.isfile(bstack11l1111ll_opy_):
      with open(bstack11l1111ll_opy_, bstack111l1ll_opy_ (u"ࠧࡸࠩ౿")):
        pass
      with open(bstack11l1111ll_opy_, bstack111l1ll_opy_ (u"ࠣࡹ࠮ࠦಀ")) as outfile:
        json.dump({}, outfile)
    if os.path.exists(bstack11l1111ll_opy_):
      bstack1lll11ll11_opy_ = json.load(open(bstack11l1111ll_opy_, bstack111l1ll_opy_ (u"ࠩࡵࡦࠬಁ")))
  except Exception as e:
    logger.debug(bstack111l1ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬಂ") + str(e))
  finally:
    return bstack1lll11ll11_opy_
def bstack1ll111l1l_opy_(platform_index, item_index):
  global bstack11l1111ll_opy_
  try:
    bstack1lll11ll11_opy_ = bstack11lllll11_opy_()
    bstack1lll11ll11_opy_[item_index] = platform_index
    with open(bstack11l1111ll_opy_, bstack111l1ll_opy_ (u"ࠦࡼ࠱ࠢಃ")) as outfile:
      json.dump(bstack1lll11ll11_opy_, outfile)
  except Exception as e:
    logger.debug(bstack111l1ll_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡸࡴ࡬ࡸ࡮ࡴࡧࠡࡶࡲࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪ಄") + str(e))
def bstack1l1111111l_opy_(bstack1ll1llll1_opy_):
  global CONFIG
  bstack1l111l1l1_opy_ = bstack111l1ll_opy_ (u"࠭ࠧಅ")
  if not bstack111l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪಆ") in CONFIG:
    logger.info(bstack111l1ll_opy_ (u"ࠨࡐࡲࠤࡵࡲࡡࡵࡨࡲࡶࡲࡹࠠࡱࡣࡶࡷࡪࡪࠠࡶࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡴࡥࡳࡣࡷࡩࠥࡸࡥࡱࡱࡵࡸࠥ࡬࡯ࡳࠢࡕࡳࡧࡵࡴࠡࡴࡸࡲࠬಇ"))
  try:
    platform = CONFIG[bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಈ")][bstack1ll1llll1_opy_]
    if bstack111l1ll_opy_ (u"ࠪࡳࡸ࠭ಉ") in platform:
      bstack1l111l1l1_opy_ += str(platform[bstack111l1ll_opy_ (u"ࠫࡴࡹࠧಊ")]) + bstack111l1ll_opy_ (u"ࠬ࠲ࠠࠨಋ")
    if bstack111l1ll_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩಌ") in platform:
      bstack1l111l1l1_opy_ += str(platform[bstack111l1ll_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪ಍")]) + bstack111l1ll_opy_ (u"ࠨ࠮ࠣࠫಎ")
    if bstack111l1ll_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭ಏ") in platform:
      bstack1l111l1l1_opy_ += str(platform[bstack111l1ll_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧಐ")]) + bstack111l1ll_opy_ (u"ࠫ࠱ࠦࠧ಑")
    if bstack111l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧಒ") in platform:
      bstack1l111l1l1_opy_ += str(platform[bstack111l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨಓ")]) + bstack111l1ll_opy_ (u"ࠧ࠭ࠢࠪಔ")
    if bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ಕ") in platform:
      bstack1l111l1l1_opy_ += str(platform[bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧಖ")]) + bstack111l1ll_opy_ (u"ࠪ࠰ࠥ࠭ಗ")
    if bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬಘ") in platform:
      bstack1l111l1l1_opy_ += str(platform[bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ಙ")]) + bstack111l1ll_opy_ (u"࠭ࠬࠡࠩಚ")
  except Exception as e:
    logger.debug(bstack111l1ll_opy_ (u"ࠧࡔࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡱࡩࡷࡧࡴࡪࡰࡪࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡳࡵࡴ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡶࡪࡶ࡯ࡳࡶࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡴࡴࠧಛ") + str(e))
  finally:
    if bstack1l111l1l1_opy_[len(bstack1l111l1l1_opy_) - 2:] == bstack111l1ll_opy_ (u"ࠨ࠮ࠣࠫಜ"):
      bstack1l111l1l1_opy_ = bstack1l111l1l1_opy_[:-2]
    return bstack1l111l1l1_opy_
def bstack1llll11ll_opy_(path, bstack1l111l1l1_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1ll11llll1_opy_ = ET.parse(path)
    bstack1l1l1llll1_opy_ = bstack1ll11llll1_opy_.getroot()
    bstack1l11l11ll_opy_ = None
    for suite in bstack1l1l1llll1_opy_.iter(bstack111l1ll_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨಝ")):
      if bstack111l1ll_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪಞ") in suite.attrib:
        suite.attrib[bstack111l1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩಟ")] += bstack111l1ll_opy_ (u"ࠬࠦࠧಠ") + bstack1l111l1l1_opy_
        bstack1l11l11ll_opy_ = suite
    bstack1l11l1l11_opy_ = None
    for robot in bstack1l1l1llll1_opy_.iter(bstack111l1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬಡ")):
      bstack1l11l1l11_opy_ = robot
    bstack1l111l1ll1_opy_ = len(bstack1l11l1l11_opy_.findall(bstack111l1ll_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ಢ")))
    if bstack1l111l1ll1_opy_ == 1:
      bstack1l11l1l11_opy_.remove(bstack1l11l1l11_opy_.findall(bstack111l1ll_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧಣ"))[0])
      bstack111lll1ll_opy_ = ET.Element(bstack111l1ll_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨತ"), attrib={bstack111l1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨಥ"): bstack111l1ll_opy_ (u"ࠫࡘࡻࡩࡵࡧࡶࠫದ"), bstack111l1ll_opy_ (u"ࠬ࡯ࡤࠨಧ"): bstack111l1ll_opy_ (u"࠭ࡳ࠱ࠩನ")})
      bstack1l11l1l11_opy_.insert(1, bstack111lll1ll_opy_)
      bstack1ll1ll11l_opy_ = None
      for suite in bstack1l11l1l11_opy_.iter(bstack111l1ll_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭಩")):
        bstack1ll1ll11l_opy_ = suite
      bstack1ll1ll11l_opy_.append(bstack1l11l11ll_opy_)
      bstack1l1l11l1l_opy_ = None
      for status in bstack1l11l11ll_opy_.iter(bstack111l1ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨಪ")):
        bstack1l1l11l1l_opy_ = status
      bstack1ll1ll11l_opy_.append(bstack1l1l11l1l_opy_)
    bstack1ll11llll1_opy_.write(path)
  except Exception as e:
    logger.debug(bstack111l1ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡲࡴ࡫ࡱ࡫ࠥࡽࡨࡪ࡮ࡨࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡴࡧࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠧಫ") + str(e))
def bstack1l1lllll1l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack11l1l111l1_opy_
  global CONFIG
  if bstack111l1ll_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡳࡥࡹ࡮ࠢಬ") in options:
    del options[bstack111l1ll_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡴࡦࡺࡨࠣಭ")]
  bstack1l11l11lll_opy_ = bstack11lllll11_opy_()
  for bstack11lllllll1_opy_ in bstack1l11l11lll_opy_.keys():
    path = os.path.join(os.getcwd(), bstack111l1ll_opy_ (u"ࠬࡶࡡࡣࡱࡷࡣࡷ࡫ࡳࡶ࡮ࡷࡷࠬಮ"), str(bstack11lllllll1_opy_), bstack111l1ll_opy_ (u"࠭࡯ࡶࡶࡳࡹࡹ࠴ࡸ࡮࡮ࠪಯ"))
    bstack1llll11ll_opy_(path, bstack1l1111111l_opy_(bstack1l11l11lll_opy_[bstack11lllllll1_opy_]))
  bstack1ll11l1111_opy_()
  return bstack11l1l111l1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1l1ll1l1l1_opy_(self, ff_profile_dir):
  global bstack1l1ll1ll1l_opy_
  if not ff_profile_dir:
    return None
  return bstack1l1ll1ll1l_opy_(self, ff_profile_dir)
def bstack11l111l1l1_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1l111ll1l_opy_
  bstack1l1l1llll_opy_ = []
  if bstack111l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪರ") in CONFIG:
    bstack1l1l1llll_opy_ = CONFIG[bstack111l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಱ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack111l1ll_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࠥಲ")],
      pabot_args[bstack111l1ll_opy_ (u"ࠥࡺࡪࡸࡢࡰࡵࡨࠦಳ")],
      argfile,
      pabot_args.get(bstack111l1ll_opy_ (u"ࠦ࡭࡯ࡶࡦࠤ಴")),
      pabot_args[bstack111l1ll_opy_ (u"ࠧࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠣವ")],
      platform[0],
      bstack1l111ll1l_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack111l1ll_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡧ࡫࡯ࡩࡸࠨಶ")] or [(bstack111l1ll_opy_ (u"ࠢࠣಷ"), None)]
    for platform in enumerate(bstack1l1l1llll_opy_)
  ]
def bstack1l1llllll1_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1l111l1lll_opy_=bstack111l1ll_opy_ (u"ࠨࠩಸ")):
  global bstack1ll11ll111_opy_
  self.platform_index = platform_index
  self.bstack111l1ll1l_opy_ = bstack1l111l1lll_opy_
  bstack1ll11ll111_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack11ll111l11_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1l11l11l1_opy_
  global bstack1l1ll1lll_opy_
  bstack1111ll1l1_opy_ = copy.deepcopy(item)
  if not bstack111l1ll_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫಹ") in item.options:
    bstack1111ll1l1_opy_.options[bstack111l1ll_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ಺")] = []
  bstack1l1l1l1lll_opy_ = bstack1111ll1l1_opy_.options[bstack111l1ll_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭಻")].copy()
  for v in bstack1111ll1l1_opy_.options[bstack111l1ll_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫಼ࠧ")]:
    if bstack111l1ll_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜ࠬಽ") in v:
      bstack1l1l1l1lll_opy_.remove(v)
    if bstack111l1ll_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡃࡍࡋࡄࡖࡌ࡙ࠧಾ") in v:
      bstack1l1l1l1lll_opy_.remove(v)
    if bstack111l1ll_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬಿ") in v:
      bstack1l1l1l1lll_opy_.remove(v)
  bstack1l1l1l1lll_opy_.insert(0, bstack111l1ll_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡒࡏࡅ࡙ࡌࡏࡓࡏࡌࡒࡉࡋࡘ࠻ࡽࢀࠫೀ").format(bstack1111ll1l1_opy_.platform_index))
  bstack1l1l1l1lll_opy_.insert(0, bstack111l1ll_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡇࡉࡋࡒࡏࡄࡃࡏࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘ࠺ࡼࡿࠪು").format(bstack1111ll1l1_opy_.bstack111l1ll1l_opy_))
  bstack1111ll1l1_opy_.options[bstack111l1ll_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ೂ")] = bstack1l1l1l1lll_opy_
  if bstack1l1ll1lll_opy_:
    bstack1111ll1l1_opy_.options[bstack111l1ll_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧೃ")].insert(0, bstack111l1ll_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘࡀࡻࡾࠩೄ").format(bstack1l1ll1lll_opy_))
  return bstack1l11l11l1_opy_(caller_id, datasources, is_last, bstack1111ll1l1_opy_, outs_dir)
def bstack1l1lll1l1l_opy_(command, item_index):
  if bstack1111lll1_opy_.get_property(bstack111l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨ೅")):
    os.environ[bstack111l1ll_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩೆ")] = json.dumps(CONFIG[bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬೇ")][item_index % bstack11l1ll11l_opy_])
  global bstack1l1ll1lll_opy_
  if bstack1l1ll1lll_opy_:
    command[0] = command[0].replace(bstack111l1ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩೈ"), bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡷࡩࡱࠠࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠡ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠠࠨ೉") + str(
      item_index) + bstack111l1ll_opy_ (u"ࠬࠦࠧೊ") + bstack1l1ll1lll_opy_, 1)
  else:
    command[0] = command[0].replace(bstack111l1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬೋ"),
                                    bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠳ࡳࡥ࡭ࠣࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠣࠫೌ") + str(item_index), 1)
def bstack1l11111ll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1l11l111ll_opy_
  bstack1l1lll1l1l_opy_(command, item_index)
  return bstack1l11l111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack11lll11111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1l11l111ll_opy_
  bstack1l1lll1l1l_opy_(command, item_index)
  return bstack1l11l111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
def bstack1l11111111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1l11l111ll_opy_
  bstack1l1lll1l1l_opy_(command, item_index)
  return bstack1l11l111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack111llll1ll_opy_(self, runner, quiet=False, capture=True):
  global bstack1111llll1_opy_
  bstack1lll11l11l_opy_ = bstack1111llll1_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack111l1ll_opy_ (u"ࠨࡧࡻࡧࡪࡶࡴࡪࡱࡱࡣࡦࡸࡲࠨ್")):
      runner.exception_arr = []
    if not hasattr(runner, bstack111l1ll_opy_ (u"ࠩࡨࡼࡨࡥࡴࡳࡣࡦࡩࡧࡧࡣ࡬ࡡࡤࡶࡷ࠭೎")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1lll11l11l_opy_
def bstack1ll1ll1l11_opy_(runner, hook_name, context, element, bstack1lll1ll1l1_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack11l11ll11_opy_.bstack1ll1l1l1_opy_(hook_name, element)
    bstack1lll1ll1l1_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack11l11ll11_opy_.bstack1ll111ll_opy_(element)
      if hook_name not in [bstack111l1ll_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠧ೏"), bstack111l1ll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠧ೐")] and args and hasattr(args[0], bstack111l1ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡣࡲ࡫ࡳࡴࡣࡪࡩࠬ೑")):
        args[0].error_message = bstack111l1ll_opy_ (u"࠭ࠧ೒")
  except Exception as e:
    logger.debug(bstack111l1ll_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣ࡬ࡦࡴࡤ࡭ࡧࠣ࡬ࡴࡵ࡫ࡴࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩ࠿ࠦࡻࡾࠩ೓").format(str(e)))
def bstack11ll1l1ll1_opy_(runner, name, context, bstack1lll1ll1l1_opy_, *args):
    if runner.hooks.get(bstack111l1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧ೔")).__name__ != bstack111l1ll_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࡥࡤࡦࡨࡤࡹࡱࡺ࡟ࡩࡱࡲ࡯ࠧೕ"):
      bstack1ll1ll1l11_opy_(runner, name, context, runner, bstack1lll1ll1l1_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack1l1lll11ll_opy_(bstack111l1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩೖ")) else context.browser
      runner.driver_initialised = bstack111l1ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣ೗")
    except Exception as e:
      logger.debug(bstack111l1ll_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡪࡲࡪࡸࡨࡶࠥ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡦࠢࡤࡸࡹࡸࡩࡣࡷࡷࡩ࠿ࠦࡻࡾࠩ೘").format(str(e)))
def bstack11ll1l11l1_opy_(runner, name, context, bstack1lll1ll1l1_opy_, *args):
    bstack1ll1ll1l11_opy_(runner, name, context, context.feature, bstack1lll1ll1l1_opy_, *args)
    try:
      if not bstack111ll1l11_opy_:
        bstack1lll1l111l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lll11ll_opy_(bstack111l1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬ೙")) else context.browser
        if is_driver_active(bstack1lll1l111l_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack111l1ll_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠣ೚")
          bstack11l111111_opy_ = str(runner.feature.name)
          bstack1l1lll1l1_opy_(context, bstack11l111111_opy_)
          bstack1lll1l111l_opy_.execute_script(bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭೛") + json.dumps(bstack11l111111_opy_) + bstack111l1ll_opy_ (u"ࠩࢀࢁࠬ೜"))
    except Exception as e:
      logger.debug(bstack111l1ll_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢ࡬ࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪೝ").format(str(e)))
def bstack11ll11l1l1_opy_(runner, name, context, bstack1lll1ll1l1_opy_, *args):
    if hasattr(context, bstack111l1ll_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ೞ")):
        bstack11l11ll11_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack111l1ll_opy_ (u"ࠬࡹࡣࡦࡰࡤࡶ࡮ࡵࠧ೟")) else context.feature
    bstack1ll1ll1l11_opy_(runner, name, context, target, bstack1lll1ll1l1_opy_, *args)
def bstack1l11l111l1_opy_(runner, name, context, bstack1lll1ll1l1_opy_, *args):
    if len(context.scenario.tags) == 0: bstack11l11ll11_opy_.start_test(context)
    bstack1ll1ll1l11_opy_(runner, name, context, context.scenario, bstack1lll1ll1l1_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack11l1lll1l1_opy_.bstack1l1111l11_opy_(context, *args)
    try:
      bstack1lll1l111l_opy_ = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬೠ"), context.browser)
      if is_driver_active(bstack1lll1l111l_opy_):
        bstack1ll11l1l_opy_.bstack11lll1l11l_opy_(bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ೡ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack111l1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥೢ")
        if (not bstack111ll1l11_opy_):
          scenario_name = args[0].name
          feature_name = bstack11l111111_opy_ = str(runner.feature.name)
          bstack11l111111_opy_ = feature_name + bstack111l1ll_opy_ (u"ࠩࠣ࠱ࠥ࠭ೣ") + scenario_name
          if runner.driver_initialised == bstack111l1ll_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧ೤"):
            bstack1l1lll1l1_opy_(context, bstack11l111111_opy_)
            bstack1lll1l111l_opy_.execute_script(bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩ೥") + json.dumps(bstack11l111111_opy_) + bstack111l1ll_opy_ (u"ࠬࢃࡽࠨ೦"))
    except Exception as e:
      logger.debug(bstack111l1ll_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡦࡩࡳࡧࡲࡪࡱ࠽ࠤࢀࢃࠧ೧").format(str(e)))
def bstack1l11ll11l1_opy_(runner, name, context, bstack1lll1ll1l1_opy_, *args):
    bstack1ll1ll1l11_opy_(runner, name, context, args[0], bstack1lll1ll1l1_opy_, *args)
    try:
      bstack1lll1l111l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lll11ll_opy_(bstack111l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭೨")) else context.browser
      if is_driver_active(bstack1lll1l111l_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack111l1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨ೩")
        bstack11l11ll11_opy_.bstack1lll1l11_opy_(args[0])
        if runner.driver_initialised == bstack111l1ll_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢ೪"):
          feature_name = bstack11l111111_opy_ = str(runner.feature.name)
          bstack11l111111_opy_ = feature_name + bstack111l1ll_opy_ (u"ࠪࠤ࠲ࠦࠧ೫") + context.scenario.name
          bstack1lll1l111l_opy_.execute_script(bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩ೬") + json.dumps(bstack11l111111_opy_) + bstack111l1ll_opy_ (u"ࠬࢃࡽࠨ೭"))
    except Exception as e:
      logger.debug(bstack111l1ll_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡷࡩࡵࡀࠠࡼࡿࠪ೮").format(str(e)))
def bstack11l11lll11_opy_(runner, name, context, bstack1lll1ll1l1_opy_, *args):
  bstack11l11ll11_opy_.bstack1lll1lll_opy_(args[0])
  try:
    bstack1ll1l11111_opy_ = args[0].status.name
    bstack1lll1l111l_opy_ = threading.current_thread().bstackSessionDriver if bstack111l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭೯") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack1lll1l111l_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack111l1ll_opy_ (u"ࠨ࡫ࡱࡷࡹ࡫ࡰࠨ೰")
        feature_name = bstack11l111111_opy_ = str(runner.feature.name)
        bstack11l111111_opy_ = feature_name + bstack111l1ll_opy_ (u"ࠩࠣ࠱ࠥ࠭ೱ") + context.scenario.name
        bstack1lll1l111l_opy_.execute_script(bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨೲ") + json.dumps(bstack11l111111_opy_) + bstack111l1ll_opy_ (u"ࠫࢂࢃࠧೳ"))
    if str(bstack1ll1l11111_opy_).lower() == bstack111l1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ೴"):
      bstack111ll1111_opy_ = bstack111l1ll_opy_ (u"࠭ࠧ೵")
      bstack1ll11l11l1_opy_ = bstack111l1ll_opy_ (u"ࠧࠨ೶")
      bstack1ll11ll1l_opy_ = bstack111l1ll_opy_ (u"ࠨࠩ೷")
      try:
        import traceback
        bstack111ll1111_opy_ = runner.exception.__class__.__name__
        bstack1ll11ll1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1ll11l11l1_opy_ = bstack111l1ll_opy_ (u"ࠩࠣࠫ೸").join(bstack1ll11ll1_opy_)
        bstack1ll11ll1l_opy_ = bstack1ll11ll1_opy_[-1]
      except Exception as e:
        logger.debug(bstack1l11ll11ll_opy_.format(str(e)))
      bstack111ll1111_opy_ += bstack1ll11ll1l_opy_
      bstack11l1111l1_opy_(context, json.dumps(str(args[0].name) + bstack111l1ll_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤ೹") + str(bstack1ll11l11l1_opy_)),
                          bstack111l1ll_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥ೺"))
      if runner.driver_initialised == bstack111l1ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥ೻"):
        bstack1l1l1lll1l_opy_(getattr(context, bstack111l1ll_opy_ (u"࠭ࡰࡢࡩࡨࠫ೼"), None), bstack111l1ll_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ೽"), bstack111ll1111_opy_)
        bstack1lll1l111l_opy_.execute_script(bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭೾") + json.dumps(str(args[0].name) + bstack111l1ll_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣ೿") + str(bstack1ll11l11l1_opy_)) + bstack111l1ll_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪഀ"))
      if runner.driver_initialised == bstack111l1ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤഁ"):
        bstack11ll111l1l_opy_(bstack1lll1l111l_opy_, bstack111l1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬം"), bstack111l1ll_opy_ (u"ࠨࡓࡤࡧࡱࡥࡷ࡯࡯ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥഃ") + str(bstack111ll1111_opy_))
    else:
      bstack11l1111l1_opy_(context, bstack111l1ll_opy_ (u"ࠢࡑࡣࡶࡷࡪࡪࠡࠣഄ"), bstack111l1ll_opy_ (u"ࠣ࡫ࡱࡪࡴࠨഅ"))
      if runner.driver_initialised == bstack111l1ll_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢആ"):
        bstack1l1l1lll1l_opy_(getattr(context, bstack111l1ll_opy_ (u"ࠪࡴࡦ࡭ࡥࠨഇ"), None), bstack111l1ll_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦഈ"))
      bstack1lll1l111l_opy_.execute_script(bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪഉ") + json.dumps(str(args[0].name) + bstack111l1ll_opy_ (u"ࠨࠠ࠮ࠢࡓࡥࡸࡹࡥࡥࠣࠥഊ")) + bstack111l1ll_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭ഋ"))
      if runner.driver_initialised == bstack111l1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨഌ"):
        bstack11ll111l1l_opy_(bstack1lll1l111l_opy_, bstack111l1ll_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ഍"))
  except Exception as e:
    logger.debug(bstack111l1ll_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡴࡶࡨࡴ࠿ࠦࡻࡾࠩഎ").format(str(e)))
  bstack1ll1ll1l11_opy_(runner, name, context, args[0], bstack1lll1ll1l1_opy_, *args)
def bstack1lll11ll1_opy_(runner, name, context, bstack1lll1ll1l1_opy_, *args):
  bstack11l11ll11_opy_.end_test(args[0])
  try:
    bstack1llll111l1_opy_ = args[0].status.name
    bstack1lll1l111l_opy_ = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪഏ"), context.browser)
    bstack11l1lll1l1_opy_.bstack1llll111l_opy_(bstack1lll1l111l_opy_)
    if str(bstack1llll111l1_opy_).lower() == bstack111l1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬഐ"):
      bstack111ll1111_opy_ = bstack111l1ll_opy_ (u"࠭ࠧ഑")
      bstack1ll11l11l1_opy_ = bstack111l1ll_opy_ (u"ࠧࠨഒ")
      bstack1ll11ll1l_opy_ = bstack111l1ll_opy_ (u"ࠨࠩഓ")
      try:
        import traceback
        bstack111ll1111_opy_ = runner.exception.__class__.__name__
        bstack1ll11ll1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1ll11l11l1_opy_ = bstack111l1ll_opy_ (u"ࠩࠣࠫഔ").join(bstack1ll11ll1_opy_)
        bstack1ll11ll1l_opy_ = bstack1ll11ll1_opy_[-1]
      except Exception as e:
        logger.debug(bstack1l11ll11ll_opy_.format(str(e)))
      bstack111ll1111_opy_ += bstack1ll11ll1l_opy_
      bstack11l1111l1_opy_(context, json.dumps(str(args[0].name) + bstack111l1ll_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤക") + str(bstack1ll11l11l1_opy_)),
                          bstack111l1ll_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥഖ"))
      if runner.driver_initialised == bstack111l1ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢഗ") or runner.driver_initialised == bstack111l1ll_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭ഘ"):
        bstack1l1l1lll1l_opy_(getattr(context, bstack111l1ll_opy_ (u"ࠧࡱࡣࡪࡩࠬങ"), None), bstack111l1ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣച"), bstack111ll1111_opy_)
        bstack1lll1l111l_opy_.execute_script(bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧഛ") + json.dumps(str(args[0].name) + bstack111l1ll_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤജ") + str(bstack1ll11l11l1_opy_)) + bstack111l1ll_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣࡿࢀࠫഝ"))
      if runner.driver_initialised == bstack111l1ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢഞ") or runner.driver_initialised == bstack111l1ll_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭ട"):
        bstack11ll111l1l_opy_(bstack1lll1l111l_opy_, bstack111l1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧഠ"), bstack111l1ll_opy_ (u"ࠣࡕࡦࡩࡳࡧࡲࡪࡱࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧഡ") + str(bstack111ll1111_opy_))
    else:
      bstack11l1111l1_opy_(context, bstack111l1ll_opy_ (u"ࠤࡓࡥࡸࡹࡥࡥࠣࠥഢ"), bstack111l1ll_opy_ (u"ࠥ࡭ࡳ࡬࡯ࠣണ"))
      if runner.driver_initialised == bstack111l1ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨത") or runner.driver_initialised == bstack111l1ll_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬഥ"):
        bstack1l1l1lll1l_opy_(getattr(context, bstack111l1ll_opy_ (u"࠭ࡰࡢࡩࡨࠫദ"), None), bstack111l1ll_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢധ"))
      bstack1lll1l111l_opy_.execute_script(bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ന") + json.dumps(str(args[0].name) + bstack111l1ll_opy_ (u"ࠤࠣ࠱ࠥࡖࡡࡴࡵࡨࡨࠦࠨഩ")) + bstack111l1ll_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࡽࡾࠩപ"))
      if runner.driver_initialised == bstack111l1ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨഫ") or runner.driver_initialised == bstack111l1ll_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬബ"):
        bstack11ll111l1l_opy_(bstack1lll1l111l_opy_, bstack111l1ll_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨഭ"))
  except Exception as e:
    logger.debug(bstack111l1ll_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩമ").format(str(e)))
  bstack1ll1ll1l11_opy_(runner, name, context, context.scenario, bstack1lll1ll1l1_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack1111l11l1_opy_(runner, name, context, bstack1lll1ll1l1_opy_, *args):
    target = context.scenario if hasattr(context, bstack111l1ll_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪയ")) else context.feature
    bstack1ll1ll1l11_opy_(runner, name, context, target, bstack1lll1ll1l1_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack11l11l111l_opy_(runner, name, context, bstack1lll1ll1l1_opy_, *args):
    try:
      bstack1lll1l111l_opy_ = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨര"), context.browser)
      if context.failed is True:
        bstack1l1ll1l1l_opy_ = []
        bstack1ll1l11ll1_opy_ = []
        bstack1lll1l1111_opy_ = []
        bstack1l11llll1l_opy_ = bstack111l1ll_opy_ (u"ࠪࠫറ")
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack1l1ll1l1l_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack1ll11ll1_opy_ = traceback.format_tb(exc_tb)
            bstack111l1lll1_opy_ = bstack111l1ll_opy_ (u"ࠫࠥ࠭ല").join(bstack1ll11ll1_opy_)
            bstack1ll1l11ll1_opy_.append(bstack111l1lll1_opy_)
            bstack1lll1l1111_opy_.append(bstack1ll11ll1_opy_[-1])
        except Exception as e:
          logger.debug(bstack1l11ll11ll_opy_.format(str(e)))
        bstack111ll1111_opy_ = bstack111l1ll_opy_ (u"ࠬ࠭ള")
        for i in range(len(bstack1l1ll1l1l_opy_)):
          bstack111ll1111_opy_ += bstack1l1ll1l1l_opy_[i] + bstack1lll1l1111_opy_[i] + bstack111l1ll_opy_ (u"࠭࡜࡯ࠩഴ")
        bstack1l11llll1l_opy_ = bstack111l1ll_opy_ (u"ࠧࠡࠩവ").join(bstack1ll1l11ll1_opy_)
        if runner.driver_initialised in [bstack111l1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤശ"), bstack111l1ll_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨഷ")]:
          bstack11l1111l1_opy_(context, bstack1l11llll1l_opy_, bstack111l1ll_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤസ"))
          bstack1l1l1lll1l_opy_(getattr(context, bstack111l1ll_opy_ (u"ࠫࡵࡧࡧࡦࠩഹ"), None), bstack111l1ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧഺ"), bstack111ll1111_opy_)
          bstack1lll1l111l_opy_.execute_script(bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽഻ࠫ") + json.dumps(bstack1l11llll1l_opy_) + bstack111l1ll_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦࢂࢃ഼ࠧ"))
          bstack11ll111l1l_opy_(bstack1lll1l111l_opy_, bstack111l1ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣഽ"), bstack111l1ll_opy_ (u"ࠤࡖࡳࡲ࡫ࠠࡴࡥࡨࡲࡦࡸࡩࡰࡵࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࡡࡴࠢാ") + str(bstack111ll1111_opy_))
          bstack1lll1l11l1_opy_ = bstack1lll1llll_opy_(bstack1l11llll1l_opy_, runner.feature.name, logger)
          if (bstack1lll1l11l1_opy_ != None):
            bstack1ll11llll_opy_.append(bstack1lll1l11l1_opy_)
      else:
        if runner.driver_initialised in [bstack111l1ll_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠦി"), bstack111l1ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣീ")]:
          bstack11l1111l1_opy_(context, bstack111l1ll_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣു") + str(runner.feature.name) + bstack111l1ll_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣൂ"), bstack111l1ll_opy_ (u"ࠢࡪࡰࡩࡳࠧൃ"))
          bstack1l1l1lll1l_opy_(getattr(context, bstack111l1ll_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭ൄ"), None), bstack111l1ll_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ൅"))
          bstack1lll1l111l_opy_.execute_script(bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨെ") + json.dumps(bstack111l1ll_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢേ") + str(runner.feature.name) + bstack111l1ll_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢൈ")) + bstack111l1ll_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬ൉"))
          bstack11ll111l1l_opy_(bstack1lll1l111l_opy_, bstack111l1ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧൊ"))
          bstack1lll1l11l1_opy_ = bstack1lll1llll_opy_(bstack1l11llll1l_opy_, runner.feature.name, logger)
          if (bstack1lll1l11l1_opy_ != None):
            bstack1ll11llll_opy_.append(bstack1lll1l11l1_opy_)
    except Exception as e:
      logger.debug(bstack111l1ll_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪോ").format(str(e)))
    bstack1ll1ll1l11_opy_(runner, name, context, context.feature, bstack1lll1ll1l1_opy_, *args)
def bstack11l11llll_opy_(runner, name, context, bstack1lll1ll1l1_opy_, *args):
    bstack1ll1ll1l11_opy_(runner, name, context, runner, bstack1lll1ll1l1_opy_, *args)
def bstack1ll1llll1l_opy_(self, name, context, *args):
  if bstack11ll1l111_opy_:
    platform_index = int(threading.current_thread()._name) % bstack11l1ll11l_opy_
    bstack11l1lll11_opy_ = CONFIG[bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬൌ")][platform_index]
    os.environ[bstack111l1ll_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄ്ࠫ")] = json.dumps(bstack11l1lll11_opy_)
  global bstack1lll1ll1l1_opy_
  if not hasattr(self, bstack111l1ll_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࡹࡥࡥࠩൎ")):
    self.driver_initialised = None
  bstack1l1ll1l11l_opy_ = {
      bstack111l1ll_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠩ൏"): bstack11ll1l1ll1_opy_,
      bstack111l1ll_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠧ൐"): bstack11ll1l11l1_opy_,
      bstack111l1ll_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡵࡣࡪࠫ൑"): bstack11ll11l1l1_opy_,
      bstack111l1ll_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪ൒"): bstack1l11l111l1_opy_,
      bstack111l1ll_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠧ൓"): bstack1l11ll11l1_opy_,
      bstack111l1ll_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡸࡪࡶࠧൔ"): bstack11l11lll11_opy_,
      bstack111l1ll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬൕ"): bstack1lll11ll1_opy_,
      bstack111l1ll_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡹࡧࡧࠨൖ"): bstack1111l11l1_opy_,
      bstack111l1ll_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭ൗ"): bstack11l11l111l_opy_,
      bstack111l1ll_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠪ൘"): bstack11l11llll_opy_
  }
  handler = bstack1l1ll1l11l_opy_.get(name, bstack1lll1ll1l1_opy_)
  handler(self, name, context, bstack1lll1ll1l1_opy_, *args)
  if name in [bstack111l1ll_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨ൙"), bstack111l1ll_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪ൚"), bstack111l1ll_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡤࡰࡱ࠭൛")]:
    try:
      bstack1lll1l111l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lll11ll_opy_(bstack111l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ൜")) else context.browser
      bstack1l11llll11_opy_ = (
        (name == bstack111l1ll_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡦࡲ࡬ࠨ൝") and self.driver_initialised == bstack111l1ll_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥ൞")) or
        (name == bstack111l1ll_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫ࠧൟ") and self.driver_initialised == bstack111l1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤൠ")) or
        (name == bstack111l1ll_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪൡ") and self.driver_initialised in [bstack111l1ll_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧൢ"), bstack111l1ll_opy_ (u"ࠦ࡮ࡴࡳࡵࡧࡳࠦൣ")]) or
        (name == bstack111l1ll_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡺࡥࡱࠩ൤") and self.driver_initialised == bstack111l1ll_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦ൥"))
      )
      if bstack1l11llll11_opy_:
        self.driver_initialised = None
        bstack1lll1l111l_opy_.quit()
    except Exception:
      pass
def bstack11ll1llll1_opy_(config, startdir):
  return bstack111l1ll_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࠳ࢁࠧ൦").format(bstack111l1ll_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢ൧"))
notset = Notset()
def bstack1l11l111l_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack11l11lll1l_opy_
  if str(name).lower() == bstack111l1ll_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࠩ൨"):
    return bstack111l1ll_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤ൩")
  else:
    return bstack11l11lll1l_opy_(self, name, default, skip)
def bstack1ll1l1lll_opy_(item, when):
  global bstack1l1l11111l_opy_
  try:
    bstack1l1l11111l_opy_(item, when)
  except Exception as e:
    pass
def bstack1lll111lll_opy_():
  return
def bstack1l11ll1ll1_opy_(type, name, status, reason, bstack1l1l1l11l_opy_, bstack1l11lll1ll_opy_):
  bstack1ll1111lll_opy_ = {
    bstack111l1ll_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫ൪"): type,
    bstack111l1ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ൫"): {}
  }
  if type == bstack111l1ll_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨ൬"):
    bstack1ll1111lll_opy_[bstack111l1ll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ൭")][bstack111l1ll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ൮")] = bstack1l1l1l11l_opy_
    bstack1ll1111lll_opy_[bstack111l1ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ൯")][bstack111l1ll_opy_ (u"ࠪࡨࡦࡺࡡࠨ൰")] = json.dumps(str(bstack1l11lll1ll_opy_))
  if type == bstack111l1ll_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ൱"):
    bstack1ll1111lll_opy_[bstack111l1ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ൲")][bstack111l1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ൳")] = name
  if type == bstack111l1ll_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪ൴"):
    bstack1ll1111lll_opy_[bstack111l1ll_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ൵")][bstack111l1ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ൶")] = status
    if status == bstack111l1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ൷"):
      bstack1ll1111lll_opy_[bstack111l1ll_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ൸")][bstack111l1ll_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬ൹")] = json.dumps(str(reason))
  bstack1l1ll1ll1_opy_ = bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫൺ").format(json.dumps(bstack1ll1111lll_opy_))
  return bstack1l1ll1ll1_opy_
def bstack1l1l1l1111_opy_(driver_command, response):
    if driver_command == bstack111l1ll_opy_ (u"ࠧࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠫൻ"):
        bstack1ll11l1l_opy_.bstack1ll1l1llll_opy_({
            bstack111l1ll_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ࠧർ"): response[bstack111l1ll_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨൽ")],
            bstack111l1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪൾ"): bstack1ll11l1l_opy_.current_test_uuid()
        })
def bstack11ll1l11l_opy_(item, call, rep):
  global bstack1ll111lll1_opy_
  global bstack1ll111l11l_opy_
  global bstack111ll1l11_opy_
  name = bstack111l1ll_opy_ (u"ࠫࠬൿ")
  try:
    if rep.when == bstack111l1ll_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ඀"):
      bstack11l1lllll_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack111ll1l11_opy_:
          name = str(rep.nodeid)
          bstack1l1l1ll11_opy_ = bstack1l11ll1ll1_opy_(bstack111l1ll_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧඁ"), name, bstack111l1ll_opy_ (u"ࠧࠨං"), bstack111l1ll_opy_ (u"ࠨࠩඃ"), bstack111l1ll_opy_ (u"ࠩࠪ඄"), bstack111l1ll_opy_ (u"ࠪࠫඅ"))
          threading.current_thread().bstack1l1lll1lll_opy_ = name
          for driver in bstack1ll111l11l_opy_:
            if bstack11l1lllll_opy_ == driver.session_id:
              driver.execute_script(bstack1l1l1ll11_opy_)
      except Exception as e:
        logger.debug(bstack111l1ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫආ").format(str(e)))
      try:
        bstack11l1ll1ll_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack111l1ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ඇ"):
          status = bstack111l1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ඈ") if rep.outcome.lower() == bstack111l1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧඉ") else bstack111l1ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨඊ")
          reason = bstack111l1ll_opy_ (u"ࠩࠪඋ")
          if status == bstack111l1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪඌ"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack111l1ll_opy_ (u"ࠫ࡮ࡴࡦࡰࠩඍ") if status == bstack111l1ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬඎ") else bstack111l1ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬඏ")
          data = name + bstack111l1ll_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤࠢࠩඐ") if status == bstack111l1ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨඑ") else name + bstack111l1ll_opy_ (u"ࠩࠣࡪࡦ࡯࡬ࡦࡦࠤࠤࠬඒ") + reason
          bstack1l1l1ll1ll_opy_ = bstack1l11ll1ll1_opy_(bstack111l1ll_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬඓ"), bstack111l1ll_opy_ (u"ࠫࠬඔ"), bstack111l1ll_opy_ (u"ࠬ࠭ඕ"), bstack111l1ll_opy_ (u"࠭ࠧඖ"), level, data)
          for driver in bstack1ll111l11l_opy_:
            if bstack11l1lllll_opy_ == driver.session_id:
              driver.execute_script(bstack1l1l1ll1ll_opy_)
      except Exception as e:
        logger.debug(bstack111l1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡨࡵ࡮ࡵࡧࡻࡸࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫ඗").format(str(e)))
  except Exception as e:
    logger.debug(bstack111l1ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡸࡺࡡࡵࡧࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࡾࢁࠬ඘").format(str(e)))
  bstack1ll111lll1_opy_(item, call, rep)
def bstack11l1l1111l_opy_(driver, bstack11l1ll111_opy_, test=None):
  global bstack1l1111l1ll_opy_
  if test != None:
    bstack1111111ll_opy_ = getattr(test, bstack111l1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ඙"), None)
    bstack1l1l1ll1l1_opy_ = getattr(test, bstack111l1ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨක"), None)
    PercySDK.screenshot(driver, bstack11l1ll111_opy_, bstack1111111ll_opy_=bstack1111111ll_opy_, bstack1l1l1ll1l1_opy_=bstack1l1l1ll1l1_opy_, bstack11ll1lll1l_opy_=bstack1l1111l1ll_opy_)
  else:
    PercySDK.screenshot(driver, bstack11l1ll111_opy_)
def bstack1lll111ll_opy_(driver):
  if bstack1lll11l111_opy_.bstack11lllll1ll_opy_() is True or bstack1lll11l111_opy_.capturing() is True:
    return
  bstack1lll11l111_opy_.bstack1lllll1ll1_opy_()
  while not bstack1lll11l111_opy_.bstack11lllll1ll_opy_():
    bstack1l111lll1_opy_ = bstack1lll11l111_opy_.bstack1l1111111_opy_()
    bstack11l1l1111l_opy_(driver, bstack1l111lll1_opy_)
  bstack1lll11l111_opy_.bstack1lll1l11l_opy_()
def bstack1ll1ll1ll_opy_(sequence, driver_command, response = None, bstack1l1l11l1l1_opy_ = None, args = None):
    try:
      if sequence != bstack111l1ll_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫඛ"):
        return
      if percy.bstack1ll11lll11_opy_() == bstack111l1ll_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦග"):
        return
      bstack1l111lll1_opy_ = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩඝ"), None)
      for command in bstack1l1l1ll111_opy_:
        if command == driver_command:
          for driver in bstack1ll111l11l_opy_:
            bstack1lll111ll_opy_(driver)
      bstack1l1l11lll1_opy_ = percy.bstack1111l1ll1_opy_()
      if driver_command in bstack1111ll1ll_opy_[bstack1l1l11lll1_opy_]:
        bstack1lll11l111_opy_.bstack1l1llll11l_opy_(bstack1l111lll1_opy_, driver_command)
    except Exception as e:
      pass
def bstack11l11ll1ll_opy_(framework_name):
  if bstack1111lll1_opy_.get_property(bstack111l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫඞ")):
      return
  bstack1111lll1_opy_.bstack11llll1ll1_opy_(bstack111l1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬඟ"), True)
  global bstack111llllll1_opy_
  global bstack111l11111_opy_
  global bstack1l1l1lll11_opy_
  bstack111llllll1_opy_ = framework_name
  logger.info(bstack1l1ll11l1l_opy_.format(bstack111llllll1_opy_.split(bstack111l1ll_opy_ (u"ࠩ࠰ࠫච"))[0]))
  bstack1ll1l1111l_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack11ll1l111_opy_:
      Service.start = bstack11ll1ll111_opy_
      Service.stop = bstack11ll1l1111_opy_
      webdriver.Remote.get = bstack111111111_opy_
      WebDriver.close = bstack11l111ll1l_opy_
      WebDriver.quit = bstack111l1l1ll_opy_
      webdriver.Remote.__init__ = bstack11l1l11l11_opy_
      WebDriver.getAccessibilityResults = getAccessibilityResults
      WebDriver.get_accessibility_results = getAccessibilityResults
      WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
      WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
      WebDriver.performScan = perform_scan
      WebDriver.perform_scan = perform_scan
    if not bstack11ll1l111_opy_:
        webdriver.Remote.__init__ = bstack1l1ll1111_opy_
    WebDriver.execute = bstack1l1111l111_opy_
    bstack111l11111_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack11ll1l111_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1l1l11l11l_opy_
  except Exception as e:
    pass
  bstack11lll111ll_opy_()
  if not bstack111l11111_opy_:
    bstack1lll111l1_opy_(bstack111l1ll_opy_ (u"ࠥࡔࡦࡩ࡫ࡢࡩࡨࡷࠥࡴ࡯ࡵࠢ࡬ࡲࡸࡺࡡ࡭࡮ࡨࡨࠧඡ"), bstack1lll11lll_opy_)
  if bstack11l1l11111_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      RemoteConnection._1ll1l1l1l_opy_ = bstack1l1ll1111l_opy_
    except Exception as e:
      logger.error(bstack11l1l1l111_opy_.format(str(e)))
  if bstack1ll1111l11_opy_():
    bstack11ll1l111l_opy_(CONFIG, logger)
  if (bstack111l1ll_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪජ") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1ll11lll11_opy_() == bstack111l1ll_opy_ (u"ࠧࡺࡲࡶࡧࠥඣ"):
          bstack11l11l1ll1_opy_(bstack1ll1ll1ll_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1l1ll1l1l1_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1lll11l1ll_opy_
      except Exception as e:
        logger.warn(bstack1lll1lll1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1ll1l1ll11_opy_
      except Exception as e:
        logger.debug(bstack1ll11ll1ll_opy_ + str(e))
    except Exception as e:
      bstack1lll111l1_opy_(e, bstack1lll1lll1_opy_)
    Output.start_test = bstack11l111llll_opy_
    Output.end_test = bstack11ll1l1lll_opy_
    TestStatus.__init__ = bstack1ll1ll111_opy_
    QueueItem.__init__ = bstack1l1llllll1_opy_
    pabot._create_items = bstack11l111l1l1_opy_
    try:
      from pabot import __version__ as bstack1ll11lll1_opy_
      if version.parse(bstack1ll11lll1_opy_) >= version.parse(bstack111l1ll_opy_ (u"࠭࠲࠯࠳࠸࠲࠵࠭ඤ")):
        pabot._run = bstack1l11111111_opy_
      elif version.parse(bstack1ll11lll1_opy_) >= version.parse(bstack111l1ll_opy_ (u"ࠧ࠳࠰࠴࠷࠳࠶ࠧඥ")):
        pabot._run = bstack11lll11111_opy_
      else:
        pabot._run = bstack1l11111ll1_opy_
    except Exception as e:
      pabot._run = bstack1l11111ll1_opy_
    pabot._create_command_for_execution = bstack11ll111l11_opy_
    pabot._report_results = bstack1l1lllll1l_opy_
  if bstack111l1ll_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨඦ") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1lll111l1_opy_(e, bstack1l11lll111_opy_)
    Runner.run_hook = bstack1ll1llll1l_opy_
    Step.run = bstack111llll1ll_opy_
  if bstack111l1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩට") in str(framework_name).lower():
    if not bstack11ll1l111_opy_:
      return
    try:
      if percy.bstack1ll11lll11_opy_() == bstack111l1ll_opy_ (u"ࠥࡸࡷࡻࡥࠣඨ"):
          bstack11l11l1ll1_opy_(bstack1ll1ll1ll_opy_)
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack11ll1llll1_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1lll111lll_opy_
      Config.getoption = bstack1l11l111l_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack11ll1l11l_opy_
    except Exception as e:
      pass
def bstack1ll1ll1l1_opy_():
  global CONFIG
  if bstack111l1ll_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫඩ") in CONFIG and int(CONFIG[bstack111l1ll_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬඪ")]) > 1:
    logger.warn(bstack1l11l11l11_opy_)
def bstack11l1ll1l11_opy_(arg, bstack111ll1l1_opy_, bstack1111lll11_opy_=None):
  global CONFIG
  global bstack11111l1l1_opy_
  global bstack1l11l1111_opy_
  global bstack11ll1l111_opy_
  global bstack1111lll1_opy_
  bstack1llll1ll1l_opy_ = bstack111l1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ණ")
  if bstack111ll1l1_opy_ and isinstance(bstack111ll1l1_opy_, str):
    bstack111ll1l1_opy_ = eval(bstack111ll1l1_opy_)
  CONFIG = bstack111ll1l1_opy_[bstack111l1ll_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧඬ")]
  bstack11111l1l1_opy_ = bstack111ll1l1_opy_[bstack111l1ll_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩත")]
  bstack1l11l1111_opy_ = bstack111ll1l1_opy_[bstack111l1ll_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫථ")]
  bstack11ll1l111_opy_ = bstack111ll1l1_opy_[bstack111l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ද")]
  bstack1111lll1_opy_.bstack11llll1ll1_opy_(bstack111l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬධ"), bstack11ll1l111_opy_)
  os.environ[bstack111l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧන")] = bstack1llll1ll1l_opy_
  os.environ[bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࠬ඲")] = json.dumps(CONFIG)
  os.environ[bstack111l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡈࡖࡄࡢ࡙ࡗࡒࠧඳ")] = bstack11111l1l1_opy_
  os.environ[bstack111l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩප")] = str(bstack1l11l1111_opy_)
  os.environ[bstack111l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡏ࡙ࡌࡏࡎࠨඵ")] = str(True)
  if bstack11l1llll1l_opy_(arg, [bstack111l1ll_opy_ (u"ࠪ࠱ࡳ࠭බ"), bstack111l1ll_opy_ (u"ࠫ࠲࠳࡮ࡶ࡯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬභ")]) != -1:
    os.environ[bstack111l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡇࡒࡂࡎࡏࡉࡑ࠭ම")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack111llll11_opy_)
    return
  bstack1lll1l1ll_opy_()
  global bstack1ll111ll1_opy_
  global bstack1l1111l1ll_opy_
  global bstack1l111ll1l_opy_
  global bstack1l1ll1lll_opy_
  global bstack1llll1ll11_opy_
  global bstack1l1l1lll11_opy_
  global bstack11l11l1l11_opy_
  arg.append(bstack111l1ll_opy_ (u"ࠨ࠭ࡘࠤඹ"))
  arg.append(bstack111l1ll_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡫࠺ࡎࡱࡧࡹࡱ࡫ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡ࡫ࡰࡴࡴࡸࡴࡦࡦ࠽ࡴࡾࡺࡥࡴࡶ࠱ࡔࡾࡺࡥࡴࡶ࡚ࡥࡷࡴࡩ࡯ࡩࠥය"))
  arg.append(bstack111l1ll_opy_ (u"ࠣ࠯࡚ࠦර"))
  arg.append(bstack111l1ll_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡦ࠼ࡗ࡬ࡪࠦࡨࡰࡱ࡮࡭ࡲࡶ࡬ࠣ඼"))
  global bstack1ll11ll11_opy_
  global bstack11ll11lll1_opy_
  global bstack1l1111ll1l_opy_
  global bstack1l1111lll1_opy_
  global bstack1l1ll1ll1l_opy_
  global bstack1ll11ll111_opy_
  global bstack1l11l11l1_opy_
  global bstack1l1111llll_opy_
  global bstack11lll1lll1_opy_
  global bstack1ll11l1l11_opy_
  global bstack11l11lll1l_opy_
  global bstack1l1l11111l_opy_
  global bstack1ll111lll1_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1ll11ll11_opy_ = webdriver.Remote.__init__
    bstack11ll11lll1_opy_ = WebDriver.quit
    bstack1l1111llll_opy_ = WebDriver.close
    bstack11lll1lll1_opy_ = WebDriver.get
    bstack1l1111ll1l_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack1l1l11ll11_opy_(CONFIG) and bstack1l1ll11l1_opy_():
    if bstack11lll1111_opy_() < version.parse(bstack1l1ll11ll1_opy_):
      logger.error(bstack1l11111l1_opy_.format(bstack11lll1111_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1ll11l1l11_opy_ = RemoteConnection._1ll1l1l1l_opy_
      except Exception as e:
        logger.error(bstack11l1l1l111_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack11l11lll1l_opy_ = Config.getoption
    from _pytest import runner
    bstack1l1l11111l_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1llllll1l_opy_)
  try:
    from pytest_bdd import reporting
    bstack1ll111lll1_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack111l1ll_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡲࠤࡷࡻ࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࡶࠫල"))
  bstack1l111ll1l_opy_ = CONFIG.get(bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ඾"), {}).get(bstack111l1ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ඿"))
  bstack11l11l1l11_opy_ = True
  bstack11l11ll1ll_opy_(bstack11l1ll1ll1_opy_)
  os.environ[bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧව")] = CONFIG[bstack111l1ll_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩශ")]
  os.environ[bstack111l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ࠫෂ")] = CONFIG[bstack111l1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬස")]
  os.environ[bstack111l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭හ")] = bstack11ll1l111_opy_.__str__()
  from _pytest.config import main as bstack11ll1ll11_opy_
  bstack11l1ll11l1_opy_ = []
  try:
    bstack1lllll11ll_opy_ = bstack11ll1ll11_opy_(arg)
    if bstack111l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴࠨළ") in multiprocessing.current_process().__dict__.keys():
      for bstack11l1l1ll1l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11l1ll11l1_opy_.append(bstack11l1l1ll1l_opy_)
    try:
      bstack1l1l1l1l11_opy_ = (bstack11l1ll11l1_opy_, int(bstack1lllll11ll_opy_))
      bstack1111lll11_opy_.append(bstack1l1l1l1l11_opy_)
    except:
      bstack1111lll11_opy_.append((bstack11l1ll11l1_opy_, bstack1lllll11ll_opy_))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack11l1ll11l1_opy_.append({bstack111l1ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪෆ"): bstack111l1ll_opy_ (u"࠭ࡐࡳࡱࡦࡩࡸࡹࠠࠨ෇") + os.environ.get(bstack111l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ෈")), bstack111l1ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ෉"): traceback.format_exc(), bstack111l1ll_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ්"): int(os.environ.get(bstack111l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪ෋")))})
    bstack1111lll11_opy_.append((bstack11l1ll11l1_opy_, 1))
def bstack111ll11l1_opy_(arg):
  global bstack1l1111ll1_opy_
  bstack11l11ll1ll_opy_(bstack1ll1l11l1_opy_)
  os.environ[bstack111l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ෌")] = str(bstack1l11l1111_opy_)
  from behave.__main__ import main as bstack11l1l11l1_opy_
  status_code = bstack11l1l11l1_opy_(arg)
  if status_code != 0:
    bstack1l1111ll1_opy_ = status_code
def bstack1lll1l1l11_opy_():
  logger.info(bstack11l1l1ll11_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack111l1ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ෍"), help=bstack111l1ll_opy_ (u"࠭ࡇࡦࡰࡨࡶࡦࡺࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡤࡱࡱࡪ࡮࡭ࠧ෎"))
  parser.add_argument(bstack111l1ll_opy_ (u"ࠧ࠮ࡷࠪා"), bstack111l1ll_opy_ (u"ࠨ࠯࠰ࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬැ"), help=bstack111l1ll_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡵࡴࡧࡵࡲࡦࡳࡥࠨෑ"))
  parser.add_argument(bstack111l1ll_opy_ (u"ࠪ࠱ࡰ࠭ි"), bstack111l1ll_opy_ (u"ࠫ࠲࠳࡫ࡦࡻࠪී"), help=bstack111l1ll_opy_ (u"ࠬ࡟࡯ࡶࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡤࡧࡨ࡫ࡳࡴࠢ࡮ࡩࡾ࠭ු"))
  parser.add_argument(bstack111l1ll_opy_ (u"࠭࠭ࡧࠩ෕"), bstack111l1ll_opy_ (u"ࠧ࠮࠯ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬූ"), help=bstack111l1ll_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ෗"))
  bstack111lllll11_opy_ = parser.parse_args()
  try:
    bstack11l11111ll_opy_ = bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡩࡨࡲࡪࡸࡩࡤ࠰ࡼࡱࡱ࠴ࡳࡢ࡯ࡳࡰࡪ࠭ෘ")
    if bstack111lllll11_opy_.framework and bstack111lllll11_opy_.framework not in (bstack111l1ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪෙ"), bstack111l1ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬේ")):
      bstack11l11111ll_opy_ = bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠮ࡺ࡯࡯࠲ࡸࡧ࡭ࡱ࡮ࡨࠫෛ")
    bstack11l1l1lll_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l11111ll_opy_)
    bstack1l11ll1l1l_opy_ = open(bstack11l1l1lll_opy_, bstack111l1ll_opy_ (u"࠭ࡲࠨො"))
    bstack1ll11l111_opy_ = bstack1l11ll1l1l_opy_.read()
    bstack1l11ll1l1l_opy_.close()
    if bstack111lllll11_opy_.username:
      bstack1ll11l111_opy_ = bstack1ll11l111_opy_.replace(bstack111l1ll_opy_ (u"࡚ࠧࡑࡘࡖࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧෝ"), bstack111lllll11_opy_.username)
    if bstack111lllll11_opy_.key:
      bstack1ll11l111_opy_ = bstack1ll11l111_opy_.replace(bstack111l1ll_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪෞ"), bstack111lllll11_opy_.key)
    if bstack111lllll11_opy_.framework:
      bstack1ll11l111_opy_ = bstack1ll11l111_opy_.replace(bstack111l1ll_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪෟ"), bstack111lllll11_opy_.framework)
    file_name = bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭෠")
    file_path = os.path.abspath(file_name)
    bstack1l111l1ll_opy_ = open(file_path, bstack111l1ll_opy_ (u"ࠫࡼ࠭෡"))
    bstack1l111l1ll_opy_.write(bstack1ll11l111_opy_)
    bstack1l111l1ll_opy_.close()
    logger.info(bstack11lll1l11_opy_)
    try:
      os.environ[bstack111l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧ෢")] = bstack111lllll11_opy_.framework if bstack111lllll11_opy_.framework != None else bstack111l1ll_opy_ (u"ࠨࠢ෣")
      config = yaml.safe_load(bstack1ll11l111_opy_)
      config[bstack111l1ll_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ෤")] = bstack111l1ll_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠮ࡵࡨࡸࡺࡶࠧ෥")
      bstack1l11111ll_opy_(bstack1l1llll1ll_opy_, config)
    except Exception as e:
      logger.debug(bstack1111ll11l_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1ll1l111ll_opy_.format(str(e)))
def bstack1l11111ll_opy_(bstack11l1111111_opy_, config, bstack11lll1llll_opy_={}):
  global bstack11ll1l111_opy_
  global bstack11llll111_opy_
  global bstack1111lll1_opy_
  if not config:
    return
  bstack1l1l1lll1_opy_ = bstack11l1ll1111_opy_ if not bstack11ll1l111_opy_ else (
    bstack11l111ll11_opy_ if bstack111l1ll_opy_ (u"ࠩࡤࡴࡵ࠭෦") in config else (
        bstack1lll111ll1_opy_ if config.get(bstack111l1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ෧")) else bstack1lll1lll11_opy_
    )
)
  bstack11l11ll1l_opy_ = False
  bstack111lll111_opy_ = False
  if bstack11ll1l111_opy_ is True:
      if bstack111l1ll_opy_ (u"ࠫࡦࡶࡰࠨ෨") in config:
          bstack11l11ll1l_opy_ = True
      else:
          bstack111lll111_opy_ = True
  bstack111lllll1_opy_ = bstack11lll1111l_opy_.bstack1ll1l11ll_opy_(config, bstack11llll111_opy_)
  data = {
    bstack111l1ll_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ෩"): config[bstack111l1ll_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ෪")],
    bstack111l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ෫"): config[bstack111l1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ෬")],
    bstack111l1ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭෭"): bstack11l1111111_opy_,
    bstack111l1ll_opy_ (u"ࠪࡨࡪࡺࡥࡤࡶࡨࡨࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ෮"): os.environ.get(bstack111l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭෯"), bstack11llll111_opy_),
    bstack111l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ෰"): bstack111llll1l_opy_,
    bstack111l1ll_opy_ (u"࠭࡯ࡱࡶ࡬ࡱࡦࡲ࡟ࡩࡷࡥࡣࡺࡸ࡬ࠨ෱"): bstack1lll1ll11l_opy_(),
    bstack111l1ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪෲ"): {
      bstack111l1ll_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ෳ"): str(config[bstack111l1ll_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ෴")]) if bstack111l1ll_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ෵") in config else bstack111l1ll_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࠧ෶"),
      bstack111l1ll_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࡖࡦࡴࡶ࡭ࡴࡴࠧ෷"): sys.version,
      bstack111l1ll_opy_ (u"࠭ࡲࡦࡨࡨࡶࡷ࡫ࡲࠨ෸"): bstack1l11l1ll11_opy_(os.getenv(bstack111l1ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠤ෹"), bstack111l1ll_opy_ (u"ࠣࠤ෺"))),
      bstack111l1ll_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫ෻"): bstack111l1ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ෼"),
      bstack111l1ll_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬ෽"): bstack1l1l1lll1_opy_,
      bstack111l1ll_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪ෾"): bstack111lllll1_opy_,
      bstack111l1ll_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨ࡟ࡶࡷ࡬ࡨࠬ෿"): os.environ[bstack111l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ฀")],
      bstack111l1ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫก"): bstack11ll11111l_opy_(os.environ.get(bstack111l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫข"), bstack11llll111_opy_)),
      bstack111l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ฃ"): config[bstack111l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧค")] if config[bstack111l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨฅ")] else bstack111l1ll_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢฆ"),
      bstack111l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩง"): str(config[bstack111l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪจ")]) if bstack111l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫฉ") in config else bstack111l1ll_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࠦช"),
      bstack111l1ll_opy_ (u"ࠫࡴࡹࠧซ"): sys.platform,
      bstack111l1ll_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧฌ"): socket.gethostname(),
      bstack111l1ll_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨญ"): bstack1111lll1_opy_.get_property(bstack111l1ll_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩฎ"))
    }
  }
  if not bstack1111lll1_opy_.get_property(bstack111l1ll_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨฏ")) is None:
    data[bstack111l1ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬฐ")][bstack111l1ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡒ࡫ࡴࡢࡦࡤࡸࡦ࠭ฑ")] = {
      bstack111l1ll_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫฒ"): bstack111l1ll_opy_ (u"ࠬࡻࡳࡦࡴࡢ࡯࡮ࡲ࡬ࡦࡦࠪณ"),
      bstack111l1ll_opy_ (u"࠭ࡳࡪࡩࡱࡥࡱ࠭ด"): bstack1111lll1_opy_.get_property(bstack111l1ll_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧต")),
      bstack111l1ll_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࡏࡷࡰࡦࡪࡸࠧถ"): bstack1111lll1_opy_.get_property(bstack111l1ll_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡑࡳࠬท"))
    }
  if bstack11l1111111_opy_ == bstack11ll1l1ll_opy_:
    data[bstack111l1ll_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭ธ")][bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡆࡳࡳ࡬ࡩࡨࠩน")] = bstack1lllll1111_opy_(config)
    data[bstack111l1ll_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨบ")][bstack111l1ll_opy_ (u"࠭ࡩࡴࡒࡨࡶࡨࡿࡁࡶࡶࡲࡉࡳࡧࡢ࡭ࡧࡧࠫป")] = percy.bstack1llllll1ll_opy_
    data[bstack111l1ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪผ")][bstack111l1ll_opy_ (u"ࠨࡲࡨࡶࡨࡿࡂࡶ࡫࡯ࡨࡎࡪࠧฝ")] = percy.bstack1ll111111l_opy_
  update(data[bstack111l1ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬพ")], bstack11lll1llll_opy_)
  try:
    response = bstack11l11l1111_opy_(bstack111l1ll_opy_ (u"ࠪࡔࡔ࡙ࡔࠨฟ"), bstack11lll1l1l_opy_(bstack1l1lll1l11_opy_), data, {
      bstack111l1ll_opy_ (u"ࠫࡦࡻࡴࡩࠩภ"): (config[bstack111l1ll_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧม")], config[bstack111l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩย")])
    })
    if response:
      logger.debug(bstack1ll1l1111_opy_.format(bstack11l1111111_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack11l1l1l1l1_opy_.format(str(e)))
def bstack1l11l1ll11_opy_(framework):
  return bstack111l1ll_opy_ (u"ࠢࡼࡿ࠰ࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࡽࢀࠦร").format(str(framework), __version__) if framework else bstack111l1ll_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵ࡻࡾࠤฤ").format(
    __version__)
def bstack1lll1l1ll_opy_():
  global CONFIG
  global bstack1lllllll1l_opy_
  if bool(CONFIG):
    return
  try:
    bstack1l1llll1l1_opy_()
    logger.debug(bstack11l1111lll_opy_.format(str(CONFIG)))
    bstack1lllllll1l_opy_ = bstack1llllll1l1_opy_.bstack1lll111l1l_opy_(CONFIG, bstack1lllllll1l_opy_)
    bstack1ll1l1111l_opy_()
  except Exception as e:
    logger.error(bstack111l1ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࡷࡳ࠰ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࠨล") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1ll111ll1l_opy_
  atexit.register(bstack11lll1ll1_opy_)
  signal.signal(signal.SIGINT, bstack1l111ll11_opy_)
  signal.signal(signal.SIGTERM, bstack1l111ll11_opy_)
def bstack1ll111ll1l_opy_(exctype, value, traceback):
  global bstack1ll111l11l_opy_
  try:
    for driver in bstack1ll111l11l_opy_:
      bstack11ll111l1l_opy_(driver, bstack111l1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪฦ"), bstack111l1ll_opy_ (u"ࠦࡘ࡫ࡳࡴ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢว") + str(value))
  except Exception:
    pass
  bstack1l1lll1ll1_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1l1lll1ll1_opy_(message=bstack111l1ll_opy_ (u"ࠬ࠭ศ"), bstack11l1ll1l1l_opy_ = False):
  global CONFIG
  bstack111l111ll_opy_ = bstack111l1ll_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠨษ") if bstack11l1ll1l1l_opy_ else bstack111l1ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ส")
  try:
    if message:
      bstack11lll1llll_opy_ = {
        bstack111l111ll_opy_ : str(message)
      }
      bstack1l11111ll_opy_(bstack11ll1l1ll_opy_, CONFIG, bstack11lll1llll_opy_)
    else:
      bstack1l11111ll_opy_(bstack11ll1l1ll_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1l1l11ll1_opy_.format(str(e)))
def bstack1l1l111111_opy_(bstack1111l11ll_opy_, size):
  bstack1l1111ll11_opy_ = []
  while len(bstack1111l11ll_opy_) > size:
    bstack11l11lllll_opy_ = bstack1111l11ll_opy_[:size]
    bstack1l1111ll11_opy_.append(bstack11l11lllll_opy_)
    bstack1111l11ll_opy_ = bstack1111l11ll_opy_[size:]
  bstack1l1111ll11_opy_.append(bstack1111l11ll_opy_)
  return bstack1l1111ll11_opy_
def bstack1llll1l11_opy_(args):
  if bstack111l1ll_opy_ (u"ࠨ࠯ࡰࠫห") in args and bstack111l1ll_opy_ (u"ࠩࡳࡨࡧ࠭ฬ") in args:
    return True
  return False
def run_on_browserstack(bstack1lll1l1ll1_opy_=None, bstack1111lll11_opy_=None, bstack11ll1111ll_opy_=False):
  global CONFIG
  global bstack11111l1l1_opy_
  global bstack1l11l1111_opy_
  global bstack11llll111_opy_
  global bstack1111lll1_opy_
  bstack1llll1ll1l_opy_ = bstack111l1ll_opy_ (u"ࠪࠫอ")
  bstack11ll11l11l_opy_(bstack11l111l11_opy_, logger)
  if bstack1lll1l1ll1_opy_ and isinstance(bstack1lll1l1ll1_opy_, str):
    bstack1lll1l1ll1_opy_ = eval(bstack1lll1l1ll1_opy_)
  if bstack1lll1l1ll1_opy_:
    CONFIG = bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫฮ")]
    bstack11111l1l1_opy_ = bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"ࠬࡎࡕࡃࡡࡘࡖࡑ࠭ฯ")]
    bstack1l11l1111_opy_ = bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨะ")]
    bstack1111lll1_opy_.bstack11llll1ll1_opy_(bstack111l1ll_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩั"), bstack1l11l1111_opy_)
    bstack1llll1ll1l_opy_ = bstack111l1ll_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨา")
  bstack1111lll1_opy_.bstack11llll1ll1_opy_(bstack111l1ll_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫำ"), uuid4().__str__())
  logger.debug(bstack111l1ll_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࡂ࠭ิ") + bstack1111lll1_opy_.get_property(bstack111l1ll_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭ี")))
  if not bstack11ll1111ll_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack111llll11_opy_)
      return
    if sys.argv[1] == bstack111l1ll_opy_ (u"ࠬ࠳࠭ࡷࡧࡵࡷ࡮ࡵ࡮ࠨึ") or sys.argv[1] == bstack111l1ll_opy_ (u"࠭࠭ࡷࠩื"):
      logger.info(bstack111l1ll_opy_ (u"ࠧࡃࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡐࡺࡶ࡫ࡳࡳࠦࡓࡅࡍࠣࡺࢀࢃุࠧ").format(__version__))
      return
    if sys.argv[1] == bstack111l1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶูࠧ"):
      bstack1lll1l1l11_opy_()
      return
  args = sys.argv
  bstack1lll1l1ll_opy_()
  global bstack1ll111ll1_opy_
  global bstack11l1ll11l_opy_
  global bstack11l11l1l11_opy_
  global bstack1l1llllll_opy_
  global bstack1l1111l1ll_opy_
  global bstack1l111ll1l_opy_
  global bstack1l1ll1lll_opy_
  global bstack11l111l11l_opy_
  global bstack1llll1ll11_opy_
  global bstack1l1l1lll11_opy_
  global bstack1ll1lll11l_opy_
  bstack11l1ll11l_opy_ = len(CONFIG.get(bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷฺࠬ"), []))
  if not bstack1llll1ll1l_opy_:
    if args[1] == bstack111l1ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ฻") or args[1] == bstack111l1ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬ฼"):
      bstack1llll1ll1l_opy_ = bstack111l1ll_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ฽")
      args = args[2:]
    elif args[1] == bstack111l1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ฾"):
      bstack1llll1ll1l_opy_ = bstack111l1ll_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭฿")
      args = args[2:]
    elif args[1] == bstack111l1ll_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧเ"):
      bstack1llll1ll1l_opy_ = bstack111l1ll_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨแ")
      args = args[2:]
    elif args[1] == bstack111l1ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫโ"):
      bstack1llll1ll1l_opy_ = bstack111l1ll_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬใ")
      args = args[2:]
    elif args[1] == bstack111l1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬไ"):
      bstack1llll1ll1l_opy_ = bstack111l1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ๅ")
      args = args[2:]
    elif args[1] == bstack111l1ll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧๆ"):
      bstack1llll1ll1l_opy_ = bstack111l1ll_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ็")
      args = args[2:]
    else:
      if not bstack111l1ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯่ࠬ") in CONFIG or str(CONFIG[bstack111l1ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ้࠭")]).lower() in [bstack111l1ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ๊ࠫ"), bstack111l1ll_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠸๋࠭")]:
        bstack1llll1ll1l_opy_ = bstack111l1ll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭์")
        args = args[1:]
      elif str(CONFIG[bstack111l1ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪํ")]).lower() == bstack111l1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ๎"):
        bstack1llll1ll1l_opy_ = bstack111l1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ๏")
        args = args[1:]
      elif str(CONFIG[bstack111l1ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭๐")]).lower() == bstack111l1ll_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ๑"):
        bstack1llll1ll1l_opy_ = bstack111l1ll_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ๒")
        args = args[1:]
      elif str(CONFIG[bstack111l1ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ๓")]).lower() == bstack111l1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ๔"):
        bstack1llll1ll1l_opy_ = bstack111l1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ๕")
        args = args[1:]
      elif str(CONFIG[bstack111l1ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ๖")]).lower() == bstack111l1ll_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ๗"):
        bstack1llll1ll1l_opy_ = bstack111l1ll_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ๘")
        args = args[1:]
      else:
        os.environ[bstack111l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧ๙")] = bstack1llll1ll1l_opy_
        bstack111ll1ll1_opy_(bstack11ll1111l1_opy_)
  os.environ[bstack111l1ll_opy_ (u"࠭ࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࡡࡘࡗࡊࡊࠧ๚")] = bstack1llll1ll1l_opy_
  bstack11llll111_opy_ = bstack1llll1ll1l_opy_
  global bstack1llll1111l_opy_
  global bstack1l111ll111_opy_
  if bstack1lll1l1ll1_opy_:
    try:
      os.environ[bstack111l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩ๛")] = bstack1llll1ll1l_opy_
      bstack1l11111ll_opy_(bstack1ll1l1ll1l_opy_, CONFIG)
    except Exception as e:
      logger.debug(bstack1l11111lll_opy_.format(str(e)))
  global bstack1ll11ll11_opy_
  global bstack11ll11lll1_opy_
  global bstack11l11ll11l_opy_
  global bstack11lll11l1_opy_
  global bstack1l1ll111ll_opy_
  global bstack1lll11111_opy_
  global bstack1l1111lll1_opy_
  global bstack1l1ll1ll1l_opy_
  global bstack1l11l111ll_opy_
  global bstack1ll11ll111_opy_
  global bstack1l11l11l1_opy_
  global bstack1l1111llll_opy_
  global bstack1lll1ll1l1_opy_
  global bstack1111llll1_opy_
  global bstack11lll1lll1_opy_
  global bstack1ll11l1l11_opy_
  global bstack11l11lll1l_opy_
  global bstack1l1l11111l_opy_
  global bstack11l1l111l1_opy_
  global bstack1ll111lll1_opy_
  global bstack1l1111ll1l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1ll11ll11_opy_ = webdriver.Remote.__init__
    bstack11ll11lll1_opy_ = WebDriver.quit
    bstack1l1111llll_opy_ = WebDriver.close
    bstack11lll1lll1_opy_ = WebDriver.get
    bstack1l1111ll1l_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1llll1111l_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack1ll11l111l_opy_
    bstack1l111ll111_opy_ = bstack1ll11l111l_opy_()
  except Exception as e:
    pass
  try:
    global bstack111111lll_opy_
    from QWeb.keywords import browser
    bstack111111lll_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack1l1l11ll11_opy_(CONFIG) and bstack1l1ll11l1_opy_():
    if bstack11lll1111_opy_() < version.parse(bstack1l1ll11ll1_opy_):
      logger.error(bstack1l11111l1_opy_.format(bstack11lll1111_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1ll11l1l11_opy_ = RemoteConnection._1ll1l1l1l_opy_
      except Exception as e:
        logger.error(bstack11l1l1l111_opy_.format(str(e)))
  if not CONFIG.get(bstack111l1ll_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡃࡸࡸࡴࡉࡡࡱࡶࡸࡶࡪࡒ࡯ࡨࡵࠪ๜"), False) and not bstack1lll1l1ll1_opy_:
    logger.info(bstack1ll1ll1l1l_opy_)
  if bstack111l1ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭๝") in CONFIG and str(CONFIG[bstack111l1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ๞")]).lower() != bstack111l1ll_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ๟"):
    bstack1l1l1111l_opy_()
  elif bstack1llll1ll1l_opy_ != bstack111l1ll_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ๠") or (bstack1llll1ll1l_opy_ == bstack111l1ll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭๡") and not bstack1lll1l1ll1_opy_):
    bstack1l111llll1_opy_()
  if (bstack1llll1ll1l_opy_ in [bstack111l1ll_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭๢"), bstack111l1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ๣"), bstack111l1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ๤")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1l1ll1l1l1_opy_
        bstack1lll11111_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1lll1lll1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1l1ll111ll_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1ll11ll1ll_opy_ + str(e))
    except Exception as e:
      bstack1lll111l1_opy_(e, bstack1lll1lll1_opy_)
    if bstack1llll1ll1l_opy_ != bstack111l1ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ๥"):
      bstack1ll11l1111_opy_()
    bstack11l11ll11l_opy_ = Output.start_test
    bstack11lll11l1_opy_ = Output.end_test
    bstack1l1111lll1_opy_ = TestStatus.__init__
    bstack1l11l111ll_opy_ = pabot._run
    bstack1ll11ll111_opy_ = QueueItem.__init__
    bstack1l11l11l1_opy_ = pabot._create_command_for_execution
    bstack11l1l111l1_opy_ = pabot._report_results
  if bstack1llll1ll1l_opy_ == bstack111l1ll_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ๦"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1lll111l1_opy_(e, bstack1l11lll111_opy_)
    bstack1lll1ll1l1_opy_ = Runner.run_hook
    bstack1111llll1_opy_ = Step.run
  if bstack1llll1ll1l_opy_ == bstack111l1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ๧"):
    try:
      from _pytest.config import Config
      bstack11l11lll1l_opy_ = Config.getoption
      from _pytest import runner
      bstack1l1l11111l_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1llllll1l_opy_)
    try:
      from pytest_bdd import reporting
      bstack1ll111lll1_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack111l1ll_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹࡵࠠࡳࡷࡱࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡨࡷࡹࡹࠧ๨"))
  try:
    framework_name = bstack111l1ll_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭๩") if bstack1llll1ll1l_opy_ in [bstack111l1ll_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ๪"), bstack111l1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ๫"), bstack111l1ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ๬")] else bstack11llllll1l_opy_(bstack1llll1ll1l_opy_)
    bstack1ll1l1l1ll_opy_ = {
      bstack111l1ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࠬ๭"): bstack111l1ll_opy_ (u"ࠬࢁ࠰ࡾ࠯ࡦࡹࡨࡻ࡭ࡣࡧࡵࠫ๮").format(framework_name) if bstack1llll1ll1l_opy_ == bstack111l1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭๯") and bstack1l1lll111l_opy_() else framework_name,
      bstack111l1ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫ๰"): bstack11ll11111l_opy_(framework_name),
      bstack111l1ll_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭๱"): __version__,
      bstack111l1ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡻࡳࡦࡦࠪ๲"): bstack1llll1ll1l_opy_
    }
    if bstack1llll1ll1l_opy_ in bstack1l1lllllll_opy_:
      if bstack11ll1l111_opy_ and bstack111l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ๳") in CONFIG and CONFIG[bstack111l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ๴")] == True:
        if bstack111l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ๵") in CONFIG:
          os.environ[bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ๶")] = os.getenv(bstack111l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ๷"), json.dumps(CONFIG[bstack111l1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ๸")]))
          CONFIG[bstack111l1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ๹")].pop(bstack111l1ll_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ๺"), None)
          CONFIG[bstack111l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ๻")].pop(bstack111l1ll_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ๼"), None)
        bstack1ll1l1l1ll_opy_[bstack111l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭๽")] = {
          bstack111l1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ๾"): bstack111l1ll_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࠪ๿"),
          bstack111l1ll_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪ຀"): str(bstack11lll1111_opy_())
        }
    if bstack1llll1ll1l_opy_ not in [bstack111l1ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫກ")]:
      bstack11llll111l_opy_ = bstack1ll11l1l_opy_.launch(CONFIG, bstack1ll1l1l1ll_opy_)
  except Exception as e:
    logger.debug(bstack1l1111l1l_opy_.format(bstack111l1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡊࡸࡦࠬຂ"), str(e)))
  if bstack1llll1ll1l_opy_ == bstack111l1ll_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ຃"):
    bstack11l11l1l11_opy_ = True
    if bstack1lll1l1ll1_opy_ and bstack11ll1111ll_opy_:
      bstack1l111ll1l_opy_ = CONFIG.get(bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪຄ"), {}).get(bstack111l1ll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ຅"))
      bstack11l11ll1ll_opy_(bstack1llll11l1l_opy_)
    elif bstack1lll1l1ll1_opy_:
      bstack1l111ll1l_opy_ = CONFIG.get(bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬຆ"), {}).get(bstack111l1ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫງ"))
      global bstack1ll111l11l_opy_
      try:
        if bstack1llll1l11_opy_(bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ຈ")]) and multiprocessing.current_process().name == bstack111l1ll_opy_ (u"ࠫ࠵࠭ຉ"):
          bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨຊ")].remove(bstack111l1ll_opy_ (u"࠭࠭࡮ࠩ຋"))
          bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪຌ")].remove(bstack111l1ll_opy_ (u"ࠨࡲࡧࡦࠬຍ"))
          bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬຎ")] = bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ຏ")][0]
          with open(bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧຐ")], bstack111l1ll_opy_ (u"ࠬࡸࠧຑ")) as f:
            bstack1llll1l1l_opy_ = f.read()
          bstack1lll111111_opy_ = bstack111l1ll_opy_ (u"ࠨࠢࠣࡨࡵࡳࡲࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡹࡤ࡬ࠢ࡬ࡱࡵࡵࡲࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡀࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡦࠪࡾࢁ࠮ࡁࠠࡧࡴࡲࡱࠥࡶࡤࡣࠢ࡬ࡱࡵࡵࡲࡵࠢࡓࡨࡧࡁࠠࡰࡩࡢࡨࡧࠦ࠽ࠡࡒࡧࡦ࠳ࡪ࡯ࡠࡤࡵࡩࡦࡱ࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡩ࡫ࡦࠡ࡯ࡲࡨࡤࡨࡲࡦࡣ࡮ࠬࡸ࡫࡬ࡧ࠮ࠣࡥࡷ࡭ࠬࠡࡶࡨࡱࡵࡵࡲࡢࡴࡼࠤࡂࠦ࠰ࠪ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡶࡵࡽ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡡࡳࡩࠣࡁࠥࡹࡴࡳࠪ࡬ࡲࡹ࠮ࡡࡳࡩࠬ࠯࠶࠶ࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡥࡹࡥࡨࡴࡹࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡤࡷࠥ࡫࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡲࡤࡷࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡴ࡭࡟ࡥࡤࠫࡷࡪࡲࡦ࠭ࡣࡵ࡫࠱ࡺࡥ࡮ࡲࡲࡶࡦࡸࡹࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡖࡤࡣ࠰ࡧࡳࡤࡨࠠ࠾ࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡒࡧࡦ࠳ࡪ࡯ࡠࡤࡵࡩࡦࡱࠠ࠾ࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡒࡧࡦ࠭࠯࠮ࡴࡧࡷࡣࡹࡸࡡࡤࡧࠫ࠭ࡡࡴࠢࠣࠤຒ").format(str(bstack1lll1l1ll1_opy_))
          bstack1lll1111l_opy_ = bstack1lll111111_opy_ + bstack1llll1l1l_opy_
          bstack11ll1ll1l1_opy_ = bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪຓ")] + bstack111l1ll_opy_ (u"ࠨࡡࡥࡷࡹࡧࡣ࡬ࡡࡷࡩࡲࡶ࠮ࡱࡻࠪດ")
          with open(bstack11ll1ll1l1_opy_, bstack111l1ll_opy_ (u"ࠩࡺࠫຕ")):
            pass
          with open(bstack11ll1ll1l1_opy_, bstack111l1ll_opy_ (u"ࠥࡻ࠰ࠨຖ")) as f:
            f.write(bstack1lll1111l_opy_)
          import subprocess
          bstack11l1llllll_opy_ = subprocess.run([bstack111l1ll_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࠦທ"), bstack11ll1ll1l1_opy_])
          if os.path.exists(bstack11ll1ll1l1_opy_):
            os.unlink(bstack11ll1ll1l1_opy_)
          os._exit(bstack11l1llllll_opy_.returncode)
        else:
          if bstack1llll1l11_opy_(bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨຘ")]):
            bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩນ")].remove(bstack111l1ll_opy_ (u"ࠧ࠮࡯ࠪບ"))
            bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫປ")].remove(bstack111l1ll_opy_ (u"ࠩࡳࡨࡧ࠭ຜ"))
            bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ຝ")] = bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧພ")][0]
          bstack11l11ll1ll_opy_(bstack1llll11l1l_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨຟ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack111l1ll_opy_ (u"࠭࡟ࡠࡰࡤࡱࡪࡥ࡟ࠨຠ")] = bstack111l1ll_opy_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩມ")
          mod_globals[bstack111l1ll_opy_ (u"ࠨࡡࡢࡪ࡮ࡲࡥࡠࡡࠪຢ")] = os.path.abspath(bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬຣ")])
          exec(open(bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭຤")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack111l1ll_opy_ (u"ࠫࡈࡧࡵࡨࡪࡷࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠫລ").format(str(e)))
          for driver in bstack1ll111l11l_opy_:
            bstack1111lll11_opy_.append({
              bstack111l1ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ຦"): bstack1lll1l1ll1_opy_[bstack111l1ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩວ")],
              bstack111l1ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ຨ"): str(e),
              bstack111l1ll_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧຩ"): multiprocessing.current_process().name
            })
            bstack11ll111l1l_opy_(driver, bstack111l1ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩສ"), bstack111l1ll_opy_ (u"ࠥࡗࡪࡹࡳࡪࡱࡱࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨຫ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1ll111l11l_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1l11l1111_opy_, CONFIG, logger)
      bstack11lllllll_opy_()
      bstack1ll1ll1l1_opy_()
      bstack111ll1l1_opy_ = {
        bstack111l1ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧຬ"): args[0],
        bstack111l1ll_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬອ"): CONFIG,
        bstack111l1ll_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧຮ"): bstack11111l1l1_opy_,
        bstack111l1ll_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩຯ"): bstack1l11l1111_opy_
      }
      percy.bstack1l11111l11_opy_()
      if bstack111l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫະ") in CONFIG:
        bstack111111l1_opy_ = []
        manager = multiprocessing.Manager()
        bstack1111l11l_opy_ = manager.list()
        if bstack1llll1l11_opy_(args):
          for index, platform in enumerate(CONFIG[bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬັ")]):
            if index == 0:
              bstack111ll1l1_opy_[bstack111l1ll_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭າ")] = args
            bstack111111l1_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack111ll1l1_opy_, bstack1111l11l_opy_)))
        else:
          for index, platform in enumerate(CONFIG[bstack111l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧຳ")]):
            bstack111111l1_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack111ll1l1_opy_, bstack1111l11l_opy_)))
        for t in bstack111111l1_opy_:
          t.start()
        for t in bstack111111l1_opy_:
          t.join()
        bstack11l111l11l_opy_ = list(bstack1111l11l_opy_)
      else:
        if bstack1llll1l11_opy_(args):
          bstack111ll1l1_opy_[bstack111l1ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨິ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack111ll1l1_opy_,))
          test.start()
          test.join()
        else:
          bstack11l11ll1ll_opy_(bstack1llll11l1l_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack111l1ll_opy_ (u"࠭࡟ࡠࡰࡤࡱࡪࡥ࡟ࠨີ")] = bstack111l1ll_opy_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩຶ")
          mod_globals[bstack111l1ll_opy_ (u"ࠨࡡࡢࡪ࡮ࡲࡥࡠࡡࠪື")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1llll1ll1l_opy_ == bstack111l1ll_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨຸ") or bstack1llll1ll1l_opy_ == bstack111l1ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵູࠩ"):
    percy.init(bstack1l11l1111_opy_, CONFIG, logger)
    percy.bstack1l11111l11_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1lll111l1_opy_(e, bstack1lll1lll1_opy_)
    bstack11lllllll_opy_()
    bstack11l11ll1ll_opy_(bstack1llll11l1_opy_)
    if bstack11ll1l111_opy_:
      bstack11llll1l1l_opy_(bstack1llll11l1_opy_, args)
      if bstack111l1ll_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴ຺ࠩ") in args:
        i = args.index(bstack111l1ll_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪົ"))
        args.pop(i)
        args.pop(i)
      if bstack111l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩຼ") not in CONFIG:
        CONFIG[bstack111l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪຽ")] = [{}]
        bstack11l1ll11l_opy_ = 1
      if bstack1ll111ll1_opy_ == 0:
        bstack1ll111ll1_opy_ = 1
      args.insert(0, str(bstack1ll111ll1_opy_))
      args.insert(0, str(bstack111l1ll_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭຾")))
    if bstack1ll11l1l_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack1llll1ll1_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack11ll1llll_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack111l1ll_opy_ (u"ࠤࡕࡓࡇࡕࡔࡠࡑࡓࡘࡎࡕࡎࡔࠤ຿"),
        ).parse_args(bstack1llll1ll1_opy_)
        bstack11llllllll_opy_ = args.index(bstack1llll1ll1_opy_[0]) if len(bstack1llll1ll1_opy_) > 0 else len(args)
        args.insert(bstack11llllllll_opy_, str(bstack111l1ll_opy_ (u"ࠪ࠱࠲ࡲࡩࡴࡶࡨࡲࡪࡸࠧເ")))
        args.insert(bstack11llllllll_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack111l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡷࡵࡢࡰࡶࡢࡰ࡮ࡹࡴࡦࡰࡨࡶ࠳ࡶࡹࠨແ"))))
        if bstack1l1l111lll_opy_(os.environ.get(bstack111l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࠪໂ"))) and str(os.environ.get(bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࡣ࡙ࡋࡓࡕࡕࠪໃ"), bstack111l1ll_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬໄ"))) != bstack111l1ll_opy_ (u"ࠨࡰࡸࡰࡱ࠭໅"):
          for bstack1l1111l1l1_opy_ in bstack11ll1llll_opy_:
            args.remove(bstack1l1111l1l1_opy_)
          bstack11l1l1l11l_opy_ = os.environ.get(bstack111l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔ࡟ࡕࡇࡖࡘࡘ࠭ໆ")).split(bstack111l1ll_opy_ (u"ࠪ࠰ࠬ໇"))
          for bstack1l1l1l1l1_opy_ in bstack11l1l1l11l_opy_:
            args.append(bstack1l1l1l1l1_opy_)
      except Exception as e:
        logger.error(bstack111l1ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡤࡸࡹࡧࡣࡩ࡫ࡱ࡫ࠥࡲࡩࡴࡶࡨࡲࡪࡸࠠࡧࡱࡵࠤࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼ࠲ࠥࡋࡲࡳࡱࡵࠤ࠲່ࠦࠢ").format(e))
    pabot.main(args)
  elif bstack1llll1ll1l_opy_ == bstack111l1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ້࠭"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1lll111l1_opy_(e, bstack1lll1lll1_opy_)
    for a in args:
      if bstack111l1ll_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜໊ࠬ") in a:
        bstack1l1111l1ll_opy_ = int(a.split(bstack111l1ll_opy_ (u"ࠧ࠻໋ࠩ"))[1])
      if bstack111l1ll_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ໌") in a:
        bstack1l111ll1l_opy_ = str(a.split(bstack111l1ll_opy_ (u"ࠩ࠽ࠫໍ"))[1])
      if bstack111l1ll_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡆࡐࡎࡇࡒࡈࡕࠪ໎") in a:
        bstack1l1ll1lll_opy_ = str(a.split(bstack111l1ll_opy_ (u"ࠫ࠿࠭໏"))[1])
    bstack11l1lll11l_opy_ = None
    if bstack111l1ll_opy_ (u"ࠬ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠫ໐") in args:
      i = args.index(bstack111l1ll_opy_ (u"࠭࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠬ໑"))
      args.pop(i)
      bstack11l1lll11l_opy_ = args.pop(i)
    if bstack11l1lll11l_opy_ is not None:
      global bstack1llll11l11_opy_
      bstack1llll11l11_opy_ = bstack11l1lll11l_opy_
    bstack11l11ll1ll_opy_(bstack1llll11l1_opy_)
    run_cli(args)
    if bstack111l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷࠫ໒") in multiprocessing.current_process().__dict__.keys():
      for bstack11l1l1ll1l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1111lll11_opy_.append(bstack11l1l1ll1l_opy_)
  elif bstack1llll1ll1l_opy_ == bstack111l1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ໓"):
    percy.init(bstack1l11l1111_opy_, CONFIG, logger)
    percy.bstack1l11111l11_opy_()
    bstack1l111l11l1_opy_ = bstack111l111l_opy_(args, logger, CONFIG, bstack11ll1l111_opy_)
    bstack1l111l11l1_opy_.bstack11111111_opy_()
    bstack11lllllll_opy_()
    bstack1l1llllll_opy_ = True
    bstack1l1l1lll11_opy_ = bstack1l111l11l1_opy_.bstack11111ll1_opy_()
    bstack1l111l11l1_opy_.bstack111ll1l1_opy_(bstack111ll1l11_opy_)
    bstack1l111lll11_opy_ = bstack1l111l11l1_opy_.bstack1111l1ll_opy_(bstack11l1ll1l11_opy_, {
      bstack111l1ll_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪ໔"): bstack11111l1l1_opy_,
      bstack111l1ll_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ໕"): bstack1l11l1111_opy_,
      bstack111l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧ໖"): bstack11ll1l111_opy_
    })
    try:
      bstack11l1ll11l1_opy_, bstack11llll1l11_opy_ = map(list, zip(*bstack1l111lll11_opy_))
      bstack1llll1ll11_opy_ = bstack11l1ll11l1_opy_[0]
      for status_code in bstack11llll1l11_opy_:
        if status_code != 0:
          bstack1ll1lll11l_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack111l1ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡤࡺࡪࠦࡥࡳࡴࡲࡶࡸࠦࡡ࡯ࡦࠣࡷࡹࡧࡴࡶࡵࠣࡧࡴࡪࡥ࠯ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡀࠠࡼࡿࠥ໗").format(str(e)))
  elif bstack1llll1ll1l_opy_ == bstack111l1ll_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭໘"):
    try:
      from behave.__main__ import main as bstack11l1l11l1_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1lll111l1_opy_(e, bstack1l11lll111_opy_)
    bstack11lllllll_opy_()
    bstack1l1llllll_opy_ = True
    bstack11111l11_opy_ = 1
    if bstack111l1ll_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ໙") in CONFIG:
      bstack11111l11_opy_ = CONFIG[bstack111l1ll_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ໚")]
    if bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ໛") in CONFIG:
      bstack11ll111ll_opy_ = int(bstack11111l11_opy_) * int(len(CONFIG[bstack111l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ໜ")]))
    else:
      bstack11ll111ll_opy_ = int(bstack11111l11_opy_)
    config = Configuration(args)
    bstack11l1l1l11_opy_ = config.paths
    if len(bstack11l1l1l11_opy_) == 0:
      import glob
      pattern = bstack111l1ll_opy_ (u"ࠫ࠯࠰࠯ࠫ࠰ࡩࡩࡦࡺࡵࡳࡧࠪໝ")
      bstack11111ll1l_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack11111ll1l_opy_)
      config = Configuration(args)
      bstack11l1l1l11_opy_ = config.paths
    bstack111l1lll_opy_ = [os.path.normpath(item) for item in bstack11l1l1l11_opy_]
    bstack11llll11l1_opy_ = [os.path.normpath(item) for item in args]
    bstack1ll1l1l1l1_opy_ = [item for item in bstack11llll11l1_opy_ if item not in bstack111l1lll_opy_]
    import platform as pf
    if pf.system().lower() == bstack111l1ll_opy_ (u"ࠬࡽࡩ࡯ࡦࡲࡻࡸ࠭ໞ"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack111l1lll_opy_ = [str(PurePosixPath(PureWindowsPath(bstack11l111111l_opy_)))
                    for bstack11l111111l_opy_ in bstack111l1lll_opy_]
    bstack111l11ll_opy_ = []
    for spec in bstack111l1lll_opy_:
      bstack1111l1l1_opy_ = []
      bstack1111l1l1_opy_ += bstack1ll1l1l1l1_opy_
      bstack1111l1l1_opy_.append(spec)
      bstack111l11ll_opy_.append(bstack1111l1l1_opy_)
    execution_items = []
    for bstack1111l1l1_opy_ in bstack111l11ll_opy_:
      if bstack111l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩໟ") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack111l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ໠")]):
          item = {}
          item[bstack111l1ll_opy_ (u"ࠨࡣࡵ࡫ࠬ໡")] = bstack111l1ll_opy_ (u"ࠩࠣࠫ໢").join(bstack1111l1l1_opy_)
          item[bstack111l1ll_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ໣")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack111l1ll_opy_ (u"ࠫࡦࡸࡧࠨ໤")] = bstack111l1ll_opy_ (u"ࠬࠦࠧ໥").join(bstack1111l1l1_opy_)
        item[bstack111l1ll_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ໦")] = 0
        execution_items.append(item)
    bstack1l1l11l111_opy_ = bstack1l1l111111_opy_(execution_items, bstack11ll111ll_opy_)
    for execution_item in bstack1l1l11l111_opy_:
      bstack111111l1_opy_ = []
      for item in execution_item:
        bstack111111l1_opy_.append(bstack111lllll_opy_(name=str(item[bstack111l1ll_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭໧")]),
                                             target=bstack111ll11l1_opy_,
                                             args=(item[bstack111l1ll_opy_ (u"ࠨࡣࡵ࡫ࠬ໨")],)))
      for t in bstack111111l1_opy_:
        t.start()
      for t in bstack111111l1_opy_:
        t.join()
  else:
    bstack111ll1ll1_opy_(bstack11ll1111l1_opy_)
  if not bstack1lll1l1ll1_opy_:
    bstack1lll1111ll_opy_()
  bstack1llllll1l1_opy_.bstack1ll1ll111l_opy_()
def browserstack_initialize(bstack1l1lll1111_opy_=None):
  run_on_browserstack(bstack1l1lll1111_opy_, None, True)
def bstack1lll1111ll_opy_():
  global CONFIG
  global bstack11llll111_opy_
  global bstack1ll1lll11l_opy_
  global bstack1l1111ll1_opy_
  global bstack1111lll1_opy_
  bstack1ll11l1l_opy_.stop()
  bstack1l1l1l11_opy_.bstack11lll1l111_opy_()
  if bstack111l1ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭໩") in CONFIG and str(CONFIG[bstack111l1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ໪")]).lower() != bstack111l1ll_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ໫"):
    bstack1l1l111l11_opy_, bstack1ll1111l1l_opy_ = bstack1l1ll1l11_opy_()
  else:
    bstack1l1l111l11_opy_, bstack1ll1111l1l_opy_ = get_build_link()
  bstack1ll1llll11_opy_(bstack1l1l111l11_opy_)
  if bstack1l1l111l11_opy_ is not None and bstack1l1ll11lll_opy_() != -1:
    sessions = bstack1l1l11ll1l_opy_(bstack1l1l111l11_opy_)
    bstack1l11l11l1l_opy_(sessions, bstack1ll1111l1l_opy_)
  if bstack11llll111_opy_ == bstack111l1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ໬") and bstack1ll1lll11l_opy_ != 0:
    sys.exit(bstack1ll1lll11l_opy_)
  if bstack11llll111_opy_ == bstack111l1ll_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭໭") and bstack1l1111ll1_opy_ != 0:
    sys.exit(bstack1l1111ll1_opy_)
def bstack1ll1llll11_opy_(new_id):
    global bstack111llll1l_opy_
    bstack111llll1l_opy_ = new_id
def bstack11llllll1l_opy_(bstack1l11l1lll_opy_):
  if bstack1l11l1lll_opy_:
    return bstack1l11l1lll_opy_.capitalize()
  else:
    return bstack111l1ll_opy_ (u"ࠧࠨ໮")
def bstack11l11l11l_opy_(bstack11lll111l_opy_):
  if bstack111l1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭໯") in bstack11lll111l_opy_ and bstack11lll111l_opy_[bstack111l1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ໰")] != bstack111l1ll_opy_ (u"ࠪࠫ໱"):
    return bstack11lll111l_opy_[bstack111l1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ໲")]
  else:
    bstack11ll111ll1_opy_ = bstack111l1ll_opy_ (u"ࠧࠨ໳")
    if bstack111l1ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭໴") in bstack11lll111l_opy_ and bstack11lll111l_opy_[bstack111l1ll_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ໵")] != None:
      bstack11ll111ll1_opy_ += bstack11lll111l_opy_[bstack111l1ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ໶")] + bstack111l1ll_opy_ (u"ࠤ࠯ࠤࠧ໷")
      if bstack11lll111l_opy_[bstack111l1ll_opy_ (u"ࠪࡳࡸ࠭໸")] == bstack111l1ll_opy_ (u"ࠦ࡮ࡵࡳࠣ໹"):
        bstack11ll111ll1_opy_ += bstack111l1ll_opy_ (u"ࠧ࡯ࡏࡔࠢࠥ໺")
      bstack11ll111ll1_opy_ += (bstack11lll111l_opy_[bstack111l1ll_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪ໻")] or bstack111l1ll_opy_ (u"ࠧࠨ໼"))
      return bstack11ll111ll1_opy_
    else:
      bstack11ll111ll1_opy_ += bstack11llllll1l_opy_(bstack11lll111l_opy_[bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩ໽")]) + bstack111l1ll_opy_ (u"ࠤࠣࠦ໾") + (
              bstack11lll111l_opy_[bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ໿")] or bstack111l1ll_opy_ (u"ࠫࠬༀ")) + bstack111l1ll_opy_ (u"ࠧ࠲ࠠࠣ༁")
      if bstack11lll111l_opy_[bstack111l1ll_opy_ (u"࠭࡯ࡴࠩ༂")] == bstack111l1ll_opy_ (u"ࠢࡘ࡫ࡱࡨࡴࡽࡳࠣ༃"):
        bstack11ll111ll1_opy_ += bstack111l1ll_opy_ (u"࡙ࠣ࡬ࡲࠥࠨ༄")
      bstack11ll111ll1_opy_ += bstack11lll111l_opy_[bstack111l1ll_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭༅")] or bstack111l1ll_opy_ (u"ࠪࠫ༆")
      return bstack11ll111ll1_opy_
def bstack1l1llll1l_opy_(bstack1llll1l11l_opy_):
  if bstack1llll1l11l_opy_ == bstack111l1ll_opy_ (u"ࠦࡩࡵ࡮ࡦࠤ༇"):
    return bstack111l1ll_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡨࡴࡨࡩࡳࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡨࡴࡨࡩࡳࠨ࠾ࡄࡱࡰࡴࡱ࡫ࡴࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ༈")
  elif bstack1llll1l11l_opy_ == bstack111l1ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ༉"):
    return bstack111l1ll_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡵࡩࡩࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡳࡧࡧࠦࡃࡌࡡࡪ࡮ࡨࡨࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪ༊")
  elif bstack1llll1l11l_opy_ == bstack111l1ll_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣ་"):
    return bstack111l1ll_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾࡬ࡸࡥࡦࡰ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦ࡬ࡸࡥࡦࡰࠥࡂࡕࡧࡳࡴࡧࡧࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩ༌")
  elif bstack1llll1l11l_opy_ == bstack111l1ll_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤ།"):
    return bstack111l1ll_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡲࡦࡦ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡷ࡫ࡤࠣࡀࡈࡶࡷࡵࡲ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭༎")
  elif bstack1llll1l11l_opy_ == bstack111l1ll_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨ༏"):
    return bstack111l1ll_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࠥࡨࡩࡦ࠹࠲࠷࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࠧࡪ࡫ࡡ࠴࠴࠹ࠦࡃ࡚ࡩ࡮ࡧࡲࡹࡹࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫ༐")
  elif bstack1llll1l11l_opy_ == bstack111l1ll_opy_ (u"ࠢࡳࡷࡱࡲ࡮ࡴࡧࠣ༑"):
    return bstack111l1ll_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡦࡱࡧࡣ࡬࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡦࡱࡧࡣ࡬ࠤࡁࡖࡺࡴ࡮ࡪࡰࡪࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩ༒")
  else:
    return bstack111l1ll_opy_ (u"ࠩ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡨ࡬ࡢࡥ࡮࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࡨ࡬ࡢࡥ࡮ࠦࡃ࠭༓") + bstack11llllll1l_opy_(
      bstack1llll1l11l_opy_) + bstack111l1ll_opy_ (u"ࠪࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩ༔")
def bstack1l111ll1ll_opy_(session):
  return bstack111l1ll_opy_ (u"ࠫࡁࡺࡲࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡴࡲࡻࠧࡄ࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠡࡵࡨࡷࡸ࡯࡯࡯࠯ࡱࡥࡲ࡫ࠢ࠿࠾ࡤࠤ࡭ࡸࡥࡧ࠿ࠥࡿࢂࠨࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣࡡࡥࡰࡦࡴ࡫ࠣࡀࡾࢁࡁ࠵ࡡ࠿࠾࠲ࡸࡩࡄࡻࡾࡽࢀࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂ࠯ࡵࡴࡁࠫ༕").format(
    session[bstack111l1ll_opy_ (u"ࠬࡶࡵࡣ࡮࡬ࡧࡤࡻࡲ࡭ࠩ༖")], bstack11l11l11l_opy_(session), bstack1l1llll1l_opy_(session[bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡹࡴࡢࡶࡸࡷࠬ༗")]),
    bstack1l1llll1l_opy_(session[bstack111l1ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹ༘ࠧ")]),
    bstack11llllll1l_opy_(session[bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳ༙ࠩ")] or session[bstack111l1ll_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩ༚")] or bstack111l1ll_opy_ (u"ࠪࠫ༛")) + bstack111l1ll_opy_ (u"ࠦࠥࠨ༜") + (session[bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ༝")] or bstack111l1ll_opy_ (u"࠭ࠧ༞")),
    session[bstack111l1ll_opy_ (u"ࠧࡰࡵࠪ༟")] + bstack111l1ll_opy_ (u"ࠣࠢࠥ༠") + session[bstack111l1ll_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭༡")], session[bstack111l1ll_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬ༢")] or bstack111l1ll_opy_ (u"ࠫࠬ༣"),
    session[bstack111l1ll_opy_ (u"ࠬࡩࡲࡦࡣࡷࡩࡩࡥࡡࡵࠩ༤")] if session[bstack111l1ll_opy_ (u"࠭ࡣࡳࡧࡤࡸࡪࡪ࡟ࡢࡶࠪ༥")] else bstack111l1ll_opy_ (u"ࠧࠨ༦"))
def bstack1l11l11l1l_opy_(sessions, bstack1ll1111l1l_opy_):
  try:
    bstack11l11llll1_opy_ = bstack111l1ll_opy_ (u"ࠣࠤ༧")
    if not os.path.exists(bstack1l11lll11l_opy_):
      os.mkdir(bstack1l11lll11l_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack111l1ll_opy_ (u"ࠩࡤࡷࡸ࡫ࡴࡴ࠱ࡵࡩࡵࡵࡲࡵ࠰࡫ࡸࡲࡲࠧ༨")), bstack111l1ll_opy_ (u"ࠪࡶࠬ༩")) as f:
      bstack11l11llll1_opy_ = f.read()
    bstack11l11llll1_opy_ = bstack11l11llll1_opy_.replace(bstack111l1ll_opy_ (u"ࠫࢀࠫࡒࡆࡕࡘࡐ࡙࡙࡟ࡄࡑࡘࡒ࡙ࠫࡽࠨ༪"), str(len(sessions)))
    bstack11l11llll1_opy_ = bstack11l11llll1_opy_.replace(bstack111l1ll_opy_ (u"ࠬࢁࠥࡃࡗࡌࡐࡉࡥࡕࡓࡎࠨࢁࠬ༫"), bstack1ll1111l1l_opy_)
    bstack11l11llll1_opy_ = bstack11l11llll1_opy_.replace(bstack111l1ll_opy_ (u"࠭ࡻࠦࡄࡘࡍࡑࡊ࡟ࡏࡃࡐࡉࠪࢃࠧ༬"),
                                              sessions[0].get(bstack111l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥ࡮ࡢ࡯ࡨࠫ༭")) if sessions[0] else bstack111l1ll_opy_ (u"ࠨࠩ༮"))
    with open(os.path.join(bstack1l11lll11l_opy_, bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡴࡨࡴࡴࡸࡴ࠯ࡪࡷࡱࡱ࠭༯")), bstack111l1ll_opy_ (u"ࠪࡻࠬ༰")) as stream:
      stream.write(bstack11l11llll1_opy_.split(bstack111l1ll_opy_ (u"ࠫࢀࠫࡓࡆࡕࡖࡍࡔࡔࡓࡠࡆࡄࡘࡆࠫࡽࠨ༱"))[0])
      for session in sessions:
        stream.write(bstack1l111ll1ll_opy_(session))
      stream.write(bstack11l11llll1_opy_.split(bstack111l1ll_opy_ (u"ࠬࢁࠥࡔࡇࡖࡗࡎࡕࡎࡔࡡࡇࡅ࡙ࡇࠥࡾࠩ༲"))[1])
    logger.info(bstack111l1ll_opy_ (u"࠭ࡇࡦࡰࡨࡶࡦࡺࡥࡥࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡤࡸ࡭ࡱࡪࠠࡢࡴࡷ࡭࡫ࡧࡣࡵࡵࠣࡥࡹࠦࡻࡾࠩ༳").format(bstack1l11lll11l_opy_));
  except Exception as e:
    logger.debug(bstack1ll1ll11ll_opy_.format(str(e)))
def bstack1l1l11ll1l_opy_(bstack1l1l111l11_opy_):
  global CONFIG
  try:
    host = bstack111l1ll_opy_ (u"ࠧࡢࡲ࡬࠱ࡨࡲ࡯ࡶࡦࠪ༴") if bstack111l1ll_opy_ (u"ࠨࡣࡳࡴ༵ࠬ") in CONFIG else bstack111l1ll_opy_ (u"ࠩࡤࡴ࡮࠭༶")
    user = CONFIG[bstack111l1ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩ༷ࠬ")]
    key = CONFIG[bstack111l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ༸")]
    bstack11ll111111_opy_ = bstack111l1ll_opy_ (u"ࠬࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨ༹ࠫ") if bstack111l1ll_opy_ (u"࠭ࡡࡱࡲࠪ༺") in CONFIG else (bstack111l1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫ༻") if CONFIG.get(bstack111l1ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬ༼")) else bstack111l1ll_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ༽"))
    url = bstack111l1ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࢀࢃ࠺ࡼࡿࡃࡿࢂ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡾࢁ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽ࠰ࡵࡨࡷࡸ࡯࡯࡯ࡵ࠱࡮ࡸࡵ࡮ࠨ༾").format(user, key, host, bstack11ll111111_opy_,
                                                                                bstack1l1l111l11_opy_)
    headers = {
      bstack111l1ll_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪ༿"): bstack111l1ll_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨཀ"),
    }
    proxies = bstack1l1l1l1ll_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.json():
      return list(map(lambda session: session[bstack111l1ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࠫཁ")], response.json()))
  except Exception as e:
    logger.debug(bstack1llll11lll_opy_.format(str(e)))
def get_build_link():
  global CONFIG
  global bstack111llll1l_opy_
  try:
    if bstack111l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪག") in CONFIG:
      host = bstack111l1ll_opy_ (u"ࠨࡣࡳ࡭࠲ࡩ࡬ࡰࡷࡧࠫགྷ") if bstack111l1ll_opy_ (u"ࠩࡤࡴࡵ࠭ང") in CONFIG else bstack111l1ll_opy_ (u"ࠪࡥࡵ࡯ࠧཅ")
      user = CONFIG[bstack111l1ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ཆ")]
      key = CONFIG[bstack111l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨཇ")]
      bstack11ll111111_opy_ = bstack111l1ll_opy_ (u"࠭ࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ཈") if bstack111l1ll_opy_ (u"ࠧࡢࡲࡳࠫཉ") in CONFIG else bstack111l1ll_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪཊ")
      url = bstack111l1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡿࢂࡀࡻࡾࡂࡾࢁ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡽࢀ࠳ࡧࡻࡩ࡭ࡦࡶ࠲࡯ࡹ࡯࡯ࠩཋ").format(user, key, host, bstack11ll111111_opy_)
      headers = {
        bstack111l1ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩཌ"): bstack111l1ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧཌྷ"),
      }
      if bstack111l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧཎ") in CONFIG:
        params = {bstack111l1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫཏ"): CONFIG[bstack111l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪཐ")], bstack111l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫད"): CONFIG[bstack111l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫདྷ")]}
      else:
        params = {bstack111l1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨན"): CONFIG[bstack111l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧཔ")]}
      proxies = bstack1l1l1l1ll_opy_(CONFIG, url)
      response = requests.get(url, params=params, headers=headers, proxies=proxies)
      if response.json():
        bstack1lll1ll1l_opy_ = response.json()[0][bstack111l1ll_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡥࡹ࡮ࡲࡤࠨཕ")]
        if bstack1lll1ll1l_opy_:
          bstack1ll1111l1l_opy_ = bstack1lll1ll1l_opy_[bstack111l1ll_opy_ (u"࠭ࡰࡶࡤ࡯࡭ࡨࡥࡵࡳ࡮ࠪབ")].split(bstack111l1ll_opy_ (u"ࠧࡱࡷࡥࡰ࡮ࡩ࠭ࡣࡷ࡬ࡰࡩ࠭བྷ"))[0] + bstack111l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡳ࠰ࠩམ") + bstack1lll1ll1l_opy_[
            bstack111l1ll_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬཙ")]
          logger.info(bstack1lll1llll1_opy_.format(bstack1ll1111l1l_opy_))
          bstack111llll1l_opy_ = bstack1lll1ll1l_opy_[bstack111l1ll_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ཚ")]
          bstack111lll11l_opy_ = CONFIG[bstack111l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧཛ")]
          if bstack111l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧཛྷ") in CONFIG:
            bstack111lll11l_opy_ += bstack111l1ll_opy_ (u"࠭ࠠࠨཝ") + CONFIG[bstack111l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩཞ")]
          if bstack111lll11l_opy_ != bstack1lll1ll1l_opy_[bstack111l1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ཟ")]:
            logger.debug(bstack1l11l1lll1_opy_.format(bstack1lll1ll1l_opy_[bstack111l1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧའ")], bstack111lll11l_opy_))
          return [bstack1lll1ll1l_opy_[bstack111l1ll_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ཡ")], bstack1ll1111l1l_opy_]
    else:
      logger.warn(bstack1l1l11l11_opy_)
  except Exception as e:
    logger.debug(bstack111l111l1_opy_.format(str(e)))
  return [None, None]
def bstack1l1ll1l111_opy_(url, bstack11l11111l_opy_=False):
  global CONFIG
  global bstack11l1111l1l_opy_
  if not bstack11l1111l1l_opy_:
    hostname = bstack1l1l1l1ll1_opy_(url)
    is_private = bstack1l1l11111_opy_(hostname)
    if (bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨར") in CONFIG and not bstack1l1l111lll_opy_(CONFIG[bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩལ")])) and (is_private or bstack11l11111l_opy_):
      bstack11l1111l1l_opy_ = hostname
def bstack1l1l1l1ll1_opy_(url):
  return urlparse(url).hostname
def bstack1l1l11111_opy_(hostname):
  for bstack11l1l1l1ll_opy_ in bstack1ll111l1l1_opy_:
    regex = re.compile(bstack11l1l1l1ll_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1l1lll11ll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1l1111l1ll_opy_
  bstack1lll11ll1l_opy_ = not (bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪཤ"), None) and bstack1ll111l1_opy_(
          threading.current_thread(), bstack111l1ll_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ཥ"), None))
  bstack1ll11lllll_opy_ = getattr(driver, bstack111l1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨས"), None) != True
  if not bstack1111111l_opy_.bstack11ll11l1l_opy_(CONFIG, bstack1l1111l1ll_opy_) or (bstack1ll11lllll_opy_ and bstack1lll11ll1l_opy_):
    logger.warning(bstack111l1ll_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶ࠲ࠧཧ"))
    return {}
  try:
    logger.debug(bstack111l1ll_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠧཨ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack1ll1l1l11l_opy_.bstack1ll1111l1_opy_)
    return results
  except Exception:
    logger.error(bstack111l1ll_opy_ (u"ࠦࡓࡵࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡹࡨࡶࡪࠦࡦࡰࡷࡱࡨ࠳ࠨཀྵ"))
    return {}
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1l1111l1ll_opy_
  bstack1lll11ll1l_opy_ = not (bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩཪ"), None) and bstack1ll111l1_opy_(
          threading.current_thread(), bstack111l1ll_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬཫ"), None))
  bstack1ll11lllll_opy_ = getattr(driver, bstack111l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧཬ"), None) != True
  if not bstack1111111l_opy_.bstack11ll11l1l_opy_(CONFIG, bstack1l1111l1ll_opy_) or (bstack1ll11lllll_opy_ and bstack1lll11ll1l_opy_):
    logger.warning(bstack111l1ll_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡷࡺࡳ࡭ࡢࡴࡼ࠲ࠧ཭"))
    return {}
  try:
    logger.debug(bstack111l1ll_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤࡧ࡫ࡦࡰࡴࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡳࡶ࡯ࡰࡥࡷࡿࠧ཮"))
    logger.debug(perform_scan(driver))
    bstack1l11l1l1l1_opy_ = driver.execute_async_script(bstack1ll1l1l11l_opy_.bstack11llll1111_opy_)
    return bstack1l11l1l1l1_opy_
  except Exception:
    logger.error(bstack111l1ll_opy_ (u"ࠥࡒࡴࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡳࡶ࡯ࡰࡥࡷࡿࠠࡸࡣࡶࠤ࡫ࡵࡵ࡯ࡦ࠱ࠦ཯"))
    return {}
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1l1111l1ll_opy_
  bstack1lll11ll1l_opy_ = not (bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ཰"), None) and bstack1ll111l1_opy_(
          threading.current_thread(), bstack111l1ll_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰཱࠫ"), None))
  bstack1ll11lllll_opy_ = getattr(driver, bstack111l1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳི࠭"), None) != True
  if not bstack1111111l_opy_.bstack11ll11l1l_opy_(CONFIG, bstack1l1111l1ll_opy_) or (bstack1ll11lllll_opy_ and bstack1lll11ll1l_opy_):
    logger.warning(bstack111l1ll_opy_ (u"ࠢࡏࡱࡷࠤࡦࡴࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡶࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡨࡧ࡮࠯ࠤཱི"))
    return {}
  try:
    bstack11llll11l_opy_ = driver.execute_async_script(bstack1ll1l1l11l_opy_.perform_scan, {bstack111l1ll_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨུ"): kwargs.get(bstack111l1ll_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࡡࡦࡳࡲࡳࡡ࡯ࡦཱུࠪ"), None) or bstack111l1ll_opy_ (u"ࠪࠫྲྀ")})
    return bstack11llll11l_opy_
  except Exception:
    logger.error(bstack111l1ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡳࡷࡱࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸࡩࡡ࡯࠰ࠥཷ"))
    return {}