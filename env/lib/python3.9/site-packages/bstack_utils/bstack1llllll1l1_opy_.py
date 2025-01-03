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
import sys
import logging
import tarfile
import io
import os
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack111l11ll11_opy_, bstack111l111l1l_opy_
import tempfile
import json
bstack1llll11ll11_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡥࡧࡥࡹ࡬࠴࡬ࡰࡩࠪᔹ"))
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack111l1ll_opy_ (u"ࠩ࡟ࡲࠪ࠮ࡡࡴࡥࡷ࡭ࡲ࡫ࠩࡴࠢ࡞ࠩ࠭ࡴࡡ࡮ࡧࠬࡷࡢࡡࠥࠩ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨ࠭ࡸࡣࠠ࠮ࠢࠨࠬࡲ࡫ࡳࡴࡣࡪࡩ࠮ࡹࠧᔺ"),
      datefmt=bstack111l1ll_opy_ (u"ࠪࠩࡍࡀࠥࡎ࠼ࠨࡗࠬᔻ"),
      stream=sys.stdout
    )
  return logger
def bstack1llll11l1l1_opy_():
  global bstack1llll11ll11_opy_
  if os.path.exists(bstack1llll11ll11_opy_):
    os.remove(bstack1llll11ll11_opy_)
def bstack1ll1ll111l_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def bstack1lll111l1l_opy_(config, log_level):
  bstack1llll11l11l_opy_ = log_level
  if bstack111l1ll_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭ᔼ") in config and config[bstack111l1ll_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧᔽ")] in bstack111l11ll11_opy_:
    bstack1llll11l11l_opy_ = bstack111l11ll11_opy_[config[bstack111l1ll_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨᔾ")]]
  if config.get(bstack111l1ll_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩᔿ"), False):
    logging.getLogger().setLevel(bstack1llll11l11l_opy_)
    return bstack1llll11l11l_opy_
  global bstack1llll11ll11_opy_
  bstack1ll1ll111l_opy_()
  bstack1llll11llll_opy_ = logging.Formatter(
    fmt=bstack111l1ll_opy_ (u"ࠨ࡞ࡱࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭ᕀ"),
    datefmt=bstack111l1ll_opy_ (u"ࠩࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫᕁ")
  )
  bstack1llll1l11l1_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack1llll11ll11_opy_)
  file_handler.setFormatter(bstack1llll11llll_opy_)
  bstack1llll1l11l1_opy_.setFormatter(bstack1llll11llll_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack1llll1l11l1_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack111l1ll_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲ࠯ࡴࡨࡱࡴࡺࡥ࠯ࡴࡨࡱࡴࡺࡥࡠࡥࡲࡲࡳ࡫ࡣࡵ࡫ࡲࡲࠬᕂ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack1llll1l11l1_opy_.setLevel(bstack1llll11l11l_opy_)
  logging.getLogger().addHandler(bstack1llll1l11l1_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack1llll11l11l_opy_
def bstack1llll1l1l1l_opy_(config):
  try:
    bstack1llll11ll1l_opy_ = set(bstack111l111l1l_opy_)
    bstack1llll1l1111_opy_ = bstack111l1ll_opy_ (u"ࠫࠬᕃ")
    with open(bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠨᕄ")) as bstack1llll11l1ll_opy_:
      bstack1llll11l111_opy_ = bstack1llll11l1ll_opy_.read()
      bstack1llll1l1111_opy_ = re.sub(bstack111l1ll_opy_ (u"ࡸࠧ࡟ࠪ࡟ࡷ࠰࠯࠿ࠤ࠰࠭ࠨࡡࡴࠧᕅ"), bstack111l1ll_opy_ (u"ࠧࠨᕆ"), bstack1llll11l111_opy_, flags=re.M)
      bstack1llll1l1111_opy_ = re.sub(
        bstack111l1ll_opy_ (u"ࡳࠩࡡࠬࡡࡹࠫࠪࡁࠫࠫᕇ") + bstack111l1ll_opy_ (u"ࠩࡿࠫᕈ").join(bstack1llll11ll1l_opy_) + bstack111l1ll_opy_ (u"ࠪ࠭࠳࠰ࠤࠨᕉ"),
        bstack111l1ll_opy_ (u"ࡶࠬࡢ࠲࠻ࠢ࡞ࡖࡊࡊࡁࡄࡖࡈࡈࡢ࠭ᕊ"),
        bstack1llll1l1111_opy_, flags=re.M | re.I
      )
    def bstack1llll11lll1_opy_(dic):
      bstack1llll1l111l_opy_ = {}
      for key, value in dic.items():
        if key in bstack1llll11ll1l_opy_:
          bstack1llll1l111l_opy_[key] = bstack111l1ll_opy_ (u"ࠬࡡࡒࡆࡆࡄࡇ࡙ࡋࡄ࡞ࠩᕋ")
        else:
          if isinstance(value, dict):
            bstack1llll1l111l_opy_[key] = bstack1llll11lll1_opy_(value)
          else:
            bstack1llll1l111l_opy_[key] = value
      return bstack1llll1l111l_opy_
    bstack1llll1l111l_opy_ = bstack1llll11lll1_opy_(config)
    return {
      bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩᕌ"): bstack1llll1l1111_opy_,
      bstack111l1ll_opy_ (u"ࠧࡧ࡫ࡱࡥࡱࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪᕍ"): json.dumps(bstack1llll1l111l_opy_)
    }
  except Exception as e:
    return {}
def bstack1l1l1ll1_opy_(config):
  global bstack1llll11ll11_opy_
  try:
    if config.get(bstack111l1ll_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡃࡸࡸࡴࡉࡡࡱࡶࡸࡶࡪࡒ࡯ࡨࡵࠪᕎ"), False):
      return
    uuid = os.getenv(bstack111l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᕏ"))
    if not uuid or uuid == bstack111l1ll_opy_ (u"ࠪࡲࡺࡲ࡬ࠨᕐ"):
      return
    bstack1llll1l1l11_opy_ = [bstack111l1ll_opy_ (u"ࠫࡷ࡫ࡱࡶ࡫ࡵࡩࡲ࡫࡮ࡵࡵ࠱ࡸࡽࡺࠧᕑ"), bstack111l1ll_opy_ (u"ࠬࡖࡩࡱࡨ࡬ࡰࡪ࠭ᕒ"), bstack111l1ll_opy_ (u"࠭ࡰࡺࡲࡵࡳ࡯࡫ࡣࡵ࠰ࡷࡳࡲࡲࠧᕓ"), bstack1llll11ll11_opy_]
    bstack1ll1ll111l_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack111l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠭࡭ࡱࡪࡷ࠲࠭ᕔ") + uuid + bstack111l1ll_opy_ (u"ࠨ࠰ࡷࡥࡷ࠴ࡧࡻࠩᕕ"))
    with tarfile.open(output_file, bstack111l1ll_opy_ (u"ࠤࡺ࠾࡬ࢀࠢᕖ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack1llll1l1l11_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack1llll1l1l1l_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack1llll1l11ll_opy_ = data.encode()
        tarinfo.size = len(bstack1llll1l11ll_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack1llll1l11ll_opy_))
    bstack1l1l1ll1l_opy_ = MultipartEncoder(
      fields= {
        bstack111l1ll_opy_ (u"ࠪࡨࡦࡺࡡࠨᕗ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack111l1ll_opy_ (u"ࠫࡷࡨࠧᕘ")), bstack111l1ll_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲ࡼ࠲࡭ࡺࡪࡲࠪᕙ")),
        bstack111l1ll_opy_ (u"࠭ࡣ࡭࡫ࡨࡲࡹࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨᕚ"): uuid
      }
    )
    response = requests.post(
      bstack111l1ll_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࡷࡳࡰࡴࡧࡤ࠮ࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡨࡲࡩࡦࡰࡷ࠱ࡱࡵࡧࡴ࠱ࡸࡴࡱࡵࡡࡥࠤᕛ"),
      data=bstack1l1l1ll1l_opy_,
      headers={bstack111l1ll_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧᕜ"): bstack1l1l1ll1l_opy_.content_type},
      auth=(config[bstack111l1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᕝ")], config[bstack111l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᕞ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack111l1ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡹࡵࡲ࡯ࡢࡦࠣࡰࡴ࡭ࡳ࠻ࠢࠪᕟ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack111l1ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸ࡫࡮ࡥ࡫ࡱ࡫ࠥࡲ࡯ࡨࡵ࠽ࠫᕠ") + str(e))
  finally:
    try:
      bstack1llll11l1l1_opy_()
    except:
      pass