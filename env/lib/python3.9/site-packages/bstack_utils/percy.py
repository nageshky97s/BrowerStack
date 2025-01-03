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
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack11lll1l1l_opy_, bstack11l11l1111_opy_
class bstack1l111l1111_opy_:
  working_dir = os.getcwd()
  bstack11l1l111ll_opy_ = False
  config = {}
  binary_path = bstack111l1ll_opy_ (u"ࠧࠨᖨ")
  bstack1lll1lll1ll_opy_ = bstack111l1ll_opy_ (u"ࠨࠩᖩ")
  bstack1lll11l111_opy_ = False
  bstack1lll1l1ll11_opy_ = None
  bstack1lll11ll11l_opy_ = {}
  bstack1lll1l1l1l1_opy_ = 300
  bstack1llll11111l_opy_ = False
  logger = None
  bstack1lll1lll111_opy_ = False
  bstack1llllll1ll_opy_ = False
  bstack1ll111111l_opy_ = None
  bstack1lll1l1l1ll_opy_ = bstack111l1ll_opy_ (u"ࠩࠪᖪ")
  bstack1lll11l1l11_opy_ = {
    bstack111l1ll_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪᖫ") : 1,
    bstack111l1ll_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬᖬ") : 2,
    bstack111l1ll_opy_ (u"ࠬ࡫ࡤࡨࡧࠪᖭ") : 3,
    bstack111l1ll_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠭ᖮ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1lll1lll11l_opy_(self):
    bstack1lll11llll1_opy_ = bstack111l1ll_opy_ (u"ࠧࠨᖯ")
    bstack1lll1l1lll1_opy_ = sys.platform
    bstack1lll1l11l11_opy_ = bstack111l1ll_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧᖰ")
    if re.match(bstack111l1ll_opy_ (u"ࠤࡧࡥࡷࡽࡩ࡯ࡾࡰࡥࡨࠦ࡯ࡴࠤᖱ"), bstack1lll1l1lll1_opy_) != None:
      bstack1lll11llll1_opy_ = bstack111l1111l1_opy_ + bstack111l1ll_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡳࡸࡾ࠮ࡻ࡫ࡳࠦᖲ")
      self.bstack1lll1l1l1ll_opy_ = bstack111l1ll_opy_ (u"ࠫࡲࡧࡣࠨᖳ")
    elif re.match(bstack111l1ll_opy_ (u"ࠧࡳࡳࡸ࡫ࡱࢀࡲࡹࡹࡴࡾࡰ࡭ࡳ࡭ࡷࡽࡥࡼ࡫ࡼ࡯࡮ࡽࡤࡦࡧࡼ࡯࡮ࡽࡹ࡬ࡲࡨ࡫ࡼࡦ࡯ࡦࢀࡼ࡯࡮࠴࠴ࠥᖴ"), bstack1lll1l1lll1_opy_) != None:
      bstack1lll11llll1_opy_ = bstack111l1111l1_opy_ + bstack111l1ll_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳ࡷࡪࡰ࠱ࡾ࡮ࡶࠢᖵ")
      bstack1lll1l11l11_opy_ = bstack111l1ll_opy_ (u"ࠢࡱࡧࡵࡧࡾ࠴ࡥࡹࡧࠥᖶ")
      self.bstack1lll1l1l1ll_opy_ = bstack111l1ll_opy_ (u"ࠨࡹ࡬ࡲࠬᖷ")
    else:
      bstack1lll11llll1_opy_ = bstack111l1111l1_opy_ + bstack111l1ll_opy_ (u"ࠤ࠲ࡴࡪࡸࡣࡺ࠯࡯࡭ࡳࡻࡸ࠯ࡼ࡬ࡴࠧᖸ")
      self.bstack1lll1l1l1ll_opy_ = bstack111l1ll_opy_ (u"ࠪࡰ࡮ࡴࡵࡹࠩᖹ")
    return bstack1lll11llll1_opy_, bstack1lll1l11l11_opy_
  def bstack1lll1ll1l11_opy_(self):
    try:
      bstack1lll1l1111l_opy_ = [os.path.join(expanduser(bstack111l1ll_opy_ (u"ࠦࢃࠨᖺ")), bstack111l1ll_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᖻ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1lll1l1111l_opy_:
        if(self.bstack1lll1llll1l_opy_(path)):
          return path
      raise bstack111l1ll_opy_ (u"ࠨࡕ࡯ࡣ࡯ࡦࡪࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠥᖼ")
    except Exception as e:
      self.logger.error(bstack111l1ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡪ࡮ࡴࡤࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨࠤࡵࡧࡴࡩࠢࡩࡳࡷࠦࡰࡦࡴࡦࡽࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࠲ࠦࡻࡾࠤᖽ").format(e))
  def bstack1lll1llll1l_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1lll111lll1_opy_(self, bstack1lll11llll1_opy_, bstack1lll1l11l11_opy_):
    try:
      bstack1lll1l1l11l_opy_ = self.bstack1lll1ll1l11_opy_()
      bstack1lll11l11l1_opy_ = os.path.join(bstack1lll1l1l11l_opy_, bstack111l1ll_opy_ (u"ࠨࡲࡨࡶࡨࡿ࠮ࡻ࡫ࡳࠫᖾ"))
      bstack1lll111llll_opy_ = os.path.join(bstack1lll1l1l11l_opy_, bstack1lll1l11l11_opy_)
      if os.path.exists(bstack1lll111llll_opy_):
        self.logger.info(bstack111l1ll_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡿࢂ࠲ࠠࡴ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠦᖿ").format(bstack1lll111llll_opy_))
        return bstack1lll111llll_opy_
      if os.path.exists(bstack1lll11l11l1_opy_):
        self.logger.info(bstack111l1ll_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡽ࡭ࡵࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡽࢀ࠰ࠥࡻ࡮ࡻ࡫ࡳࡴ࡮ࡴࡧࠣᗀ").format(bstack1lll11l11l1_opy_))
        return self.bstack1lll1ll11l1_opy_(bstack1lll11l11l1_opy_, bstack1lll1l11l11_opy_)
      self.logger.info(bstack111l1ll_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡨࡵࡳࡲࠦࡻࡾࠤᗁ").format(bstack1lll11llll1_opy_))
      response = bstack11l11l1111_opy_(bstack111l1ll_opy_ (u"ࠬࡍࡅࡕࠩᗂ"), bstack1lll11llll1_opy_, {}, {})
      if response.status_code == 200:
        with open(bstack1lll11l11l1_opy_, bstack111l1ll_opy_ (u"࠭ࡷࡣࠩᗃ")) as file:
          file.write(response.content)
        self.logger.info(bstack111l1ll_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥࡧࡧࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡥࡳࡪࠠࡴࡣࡹࡩࡩࠦࡡࡵࠢࡾࢁࠧᗄ").format(bstack1lll11l11l1_opy_))
        return self.bstack1lll1ll11l1_opy_(bstack1lll11l11l1_opy_, bstack1lll1l11l11_opy_)
      else:
        raise(bstack111l1ll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡴࡩࡧࠣࡪ࡮ࡲࡥ࠯ࠢࡖࡸࡦࡺࡵࡴࠢࡦࡳࡩ࡫࠺ࠡࡽࢀࠦᗅ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack111l1ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࡀࠠࡼࡿࠥᗆ").format(e))
  def bstack1lll11ll1l1_opy_(self, bstack1lll11llll1_opy_, bstack1lll1l11l11_opy_):
    try:
      retry = 2
      bstack1lll111llll_opy_ = None
      bstack1lll11l1lll_opy_ = False
      while retry > 0:
        bstack1lll111llll_opy_ = self.bstack1lll111lll1_opy_(bstack1lll11llll1_opy_, bstack1lll1l11l11_opy_)
        bstack1lll11l1lll_opy_ = self.bstack1lll1ll1111_opy_(bstack1lll11llll1_opy_, bstack1lll1l11l11_opy_, bstack1lll111llll_opy_)
        if bstack1lll11l1lll_opy_:
          break
        retry -= 1
      return bstack1lll111llll_opy_, bstack1lll11l1lll_opy_
    except Exception as e:
      self.logger.error(bstack111l1ll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡧࡦࡶࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡳࡥࡹ࡮ࠢᗇ").format(e))
    return bstack1lll111llll_opy_, False
  def bstack1lll1ll1111_opy_(self, bstack1lll11llll1_opy_, bstack1lll1l11l11_opy_, bstack1lll111llll_opy_, bstack1lll1ll1l1l_opy_ = 0):
    if bstack1lll1ll1l1l_opy_ > 1:
      return False
    if bstack1lll111llll_opy_ == None or os.path.exists(bstack1lll111llll_opy_) == False:
      self.logger.warn(bstack111l1ll_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡴࡦࡺࡨࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧ࠰ࠥࡸࡥࡵࡴࡼ࡭ࡳ࡭ࠠࡥࡱࡺࡲࡱࡵࡡࡥࠤᗈ"))
      return False
    bstack1lll11ll1ll_opy_ = bstack111l1ll_opy_ (u"ࠧࡤ࠮ࠫࡂࡳࡩࡷࡩࡹ࡝࠱ࡦࡰ࡮ࠦ࡜ࡥ࠰࡟ࡨ࠰࠴࡜ࡥ࠭ࠥᗉ")
    command = bstack111l1ll_opy_ (u"࠭ࡻࡾࠢ࠰࠱ࡻ࡫ࡲࡴ࡫ࡲࡲࠬᗊ").format(bstack1lll111llll_opy_)
    bstack1lll1l1ll1l_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1lll11ll1ll_opy_, bstack1lll1l1ll1l_opy_) != None:
      return True
    else:
      self.logger.error(bstack111l1ll_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡤࡪࡨࡧࡰࠦࡦࡢ࡫࡯ࡩࡩࠨᗋ"))
      return False
  def bstack1lll1ll11l1_opy_(self, bstack1lll11l11l1_opy_, bstack1lll1l11l11_opy_):
    try:
      working_dir = os.path.dirname(bstack1lll11l11l1_opy_)
      shutil.unpack_archive(bstack1lll11l11l1_opy_, working_dir)
      bstack1lll111llll_opy_ = os.path.join(working_dir, bstack1lll1l11l11_opy_)
      os.chmod(bstack1lll111llll_opy_, 0o755)
      return bstack1lll111llll_opy_
    except Exception as e:
      self.logger.error(bstack111l1ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡺࡴࡺࡪࡲࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠤᗌ"))
  def bstack1llll111111_opy_(self):
    try:
      bstack1lll1ll1lll_opy_ = self.config.get(bstack111l1ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨᗍ"))
      bstack1llll111111_opy_ = bstack1lll1ll1lll_opy_ or (bstack1lll1ll1lll_opy_ is None and self.bstack11l1l111ll_opy_)
      if not bstack1llll111111_opy_ or self.config.get(bstack111l1ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ᗎ"), None) not in bstack1111lllll1_opy_:
        return False
      self.bstack1lll11l111_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack111l1ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡧࡷࡩࡨࡺࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᗏ").format(e))
  def bstack1lll1ll1ll1_opy_(self):
    try:
      bstack1lll1ll1ll1_opy_ = self.bstack1lll1l11ll1_opy_
      return bstack1lll1ll1ll1_opy_
    except Exception as e:
      self.logger.error(bstack111l1ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡨࡸࡪࡩࡴࠡࡲࡨࡶࡨࡿࠠࡤࡣࡳࡸࡺࡸࡥࠡ࡯ࡲࡨࡪ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᗐ").format(e))
  def init(self, bstack11l1l111ll_opy_, config, logger):
    self.bstack11l1l111ll_opy_ = bstack11l1l111ll_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1llll111111_opy_():
      return
    self.bstack1lll11ll11l_opy_ = config.get(bstack111l1ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࡔࡶࡴࡪࡱࡱࡷࠬᗑ"), {})
    self.bstack1lll1l11ll1_opy_ = config.get(bstack111l1ll_opy_ (u"ࠧࡱࡧࡵࡧࡾࡉࡡࡱࡶࡸࡶࡪࡓ࡯ࡥࡧࠪᗒ"))
    try:
      bstack1lll11llll1_opy_, bstack1lll1l11l11_opy_ = self.bstack1lll1lll11l_opy_()
      bstack1lll111llll_opy_, bstack1lll11l1lll_opy_ = self.bstack1lll11ll1l1_opy_(bstack1lll11llll1_opy_, bstack1lll1l11l11_opy_)
      if bstack1lll11l1lll_opy_:
        self.binary_path = bstack1lll111llll_opy_
        thread = Thread(target=self.bstack1lll11lllll_opy_)
        thread.start()
      else:
        self.bstack1lll1lll111_opy_ = True
        self.logger.error(bstack111l1ll_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡳࡩࡷࡩࡹࠡࡲࡤࡸ࡭ࠦࡦࡰࡷࡱࡨࠥ࠳ࠠࡼࡿ࠯ࠤ࡚ࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡐࡦࡴࡦࡽࠧᗓ").format(bstack1lll111llll_opy_))
    except Exception as e:
      self.logger.error(bstack111l1ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᗔ").format(e))
  def bstack1lll1lll1l1_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack111l1ll_opy_ (u"ࠪࡰࡴ࡭ࠧᗕ"), bstack111l1ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻ࠱ࡰࡴ࡭ࠧᗖ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack111l1ll_opy_ (u"ࠧࡖࡵࡴࡪ࡬ࡲ࡬ࠦࡰࡦࡴࡦࡽࠥࡲ࡯ࡨࡵࠣࡥࡹࠦࡻࡾࠤᗗ").format(logfile))
      self.bstack1lll1lll1ll_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack111l1ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡩࡹࠦࡰࡦࡴࡦࡽࠥࡲ࡯ࡨࠢࡳࡥࡹ࡮ࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᗘ").format(e))
  def bstack1lll11lllll_opy_(self):
    bstack1lll1llllll_opy_ = self.bstack1lll1lllll1_opy_()
    if bstack1lll1llllll_opy_ == None:
      self.bstack1lll1lll111_opy_ = True
      self.logger.error(bstack111l1ll_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡴࡰ࡭ࡨࡲࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤ࠭ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻࠥᗙ"))
      return False
    command_args = [bstack111l1ll_opy_ (u"ࠣࡣࡳࡴ࠿࡫ࡸࡦࡥ࠽ࡷࡹࡧࡲࡵࠤᗚ") if self.bstack11l1l111ll_opy_ else bstack111l1ll_opy_ (u"ࠩࡨࡼࡪࡩ࠺ࡴࡶࡤࡶࡹ࠭ᗛ")]
    bstack1lll11l1l1l_opy_ = self.bstack1lll11l111l_opy_()
    if bstack1lll11l1l1l_opy_ != None:
      command_args.append(bstack111l1ll_opy_ (u"ࠥ࠱ࡨࠦࡻࡾࠤᗜ").format(bstack1lll11l1l1l_opy_))
    env = os.environ.copy()
    env[bstack111l1ll_opy_ (u"ࠦࡕࡋࡒࡄ࡛ࡢࡘࡔࡑࡅࡏࠤᗝ")] = bstack1lll1llllll_opy_
    env[bstack111l1ll_opy_ (u"࡚ࠧࡈࡠࡄࡘࡍࡑࡊ࡟ࡖࡗࡌࡈࠧᗞ")] = os.environ.get(bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᗟ"), bstack111l1ll_opy_ (u"ࠧࠨᗠ"))
    bstack1lll1l111l1_opy_ = [self.binary_path]
    self.bstack1lll1lll1l1_opy_()
    self.bstack1lll1l1ll11_opy_ = self.bstack1lll11l11ll_opy_(bstack1lll1l111l1_opy_ + command_args, env)
    self.logger.debug(bstack111l1ll_opy_ (u"ࠣࡕࡷࡥࡷࡺࡩ࡯ࡩࠣࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠤᗡ"))
    bstack1lll1ll1l1l_opy_ = 0
    while self.bstack1lll1l1ll11_opy_.poll() == None:
      bstack1lll11l1111_opy_ = self.bstack1lll1llll11_opy_()
      if bstack1lll11l1111_opy_:
        self.logger.debug(bstack111l1ll_opy_ (u"ࠤࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠧᗢ"))
        self.bstack1llll11111l_opy_ = True
        return True
      bstack1lll1ll1l1l_opy_ += 1
      self.logger.debug(bstack111l1ll_opy_ (u"ࠥࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠢࡕࡩࡹࡸࡹࠡ࠯ࠣࡿࢂࠨᗣ").format(bstack1lll1ll1l1l_opy_))
      time.sleep(2)
    self.logger.error(bstack111l1ll_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽ࠱ࠦࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡌࡡࡪ࡮ࡨࡨࠥࡧࡦࡵࡧࡵࠤࢀࢃࠠࡢࡶࡷࡩࡲࡶࡴࡴࠤᗤ").format(bstack1lll1ll1l1l_opy_))
    self.bstack1lll1lll111_opy_ = True
    return False
  def bstack1lll1llll11_opy_(self, bstack1lll1ll1l1l_opy_ = 0):
    if bstack1lll1ll1l1l_opy_ > 10:
      return False
    try:
      bstack1lll1l1llll_opy_ = os.environ.get(bstack111l1ll_opy_ (u"ࠬࡖࡅࡓࡅ࡜ࡣࡘࡋࡒࡗࡇࡕࡣࡆࡊࡄࡓࡇࡖࡗࠬᗥ"), bstack111l1ll_opy_ (u"࠭ࡨࡵࡶࡳ࠾࠴࠵࡬ࡰࡥࡤࡰ࡭ࡵࡳࡵ࠼࠸࠷࠸࠾ࠧᗦ"))
      bstack1lll11lll1l_opy_ = bstack1lll1l1llll_opy_ + bstack1111llll1l_opy_
      response = requests.get(bstack1lll11lll1l_opy_)
      data = response.json()
      self.bstack1ll111111l_opy_ = data.get(bstack111l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩ࠭ᗧ"), {}).get(bstack111l1ll_opy_ (u"ࠨ࡫ࡧࠫᗨ"), None)
      return True
    except:
      self.logger.debug(bstack111l1ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡱࡦࡧࡺࡸࡲࡦࡦࠣࡻ࡭࡯࡬ࡦࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡨࡦࡣ࡯ࡸ࡭ࠦࡣࡩࡧࡦ࡯ࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠢᗩ"))
      return False
  def bstack1lll1lllll1_opy_(self):
    bstack1lll11lll11_opy_ = bstack111l1ll_opy_ (u"ࠪࡥࡵࡶࠧᗪ") if self.bstack11l1l111ll_opy_ else bstack111l1ll_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᗫ")
    bstack1lll1l11lll_opy_ = bstack111l1ll_opy_ (u"ࠧࡻ࡮ࡥࡧࡩ࡭ࡳ࡫ࡤࠣᗬ") if self.config.get(bstack111l1ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬᗭ")) is None else True
    bstack1111ll111l_opy_ = bstack111l1ll_opy_ (u"ࠢࡢࡲ࡬࠳ࡦࡶࡰࡠࡲࡨࡶࡨࡿ࠯ࡨࡧࡷࡣࡵࡸ࡯࡫ࡧࡦࡸࡤࡺ࡯࡬ࡧࡱࡃࡳࡧ࡭ࡦ࠿ࡾࢁࠫࡺࡹࡱࡧࡀࡿࢂࠬࡰࡦࡴࡦࡽࡂࢁࡽࠣᗮ").format(self.config[bstack111l1ll_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᗯ")], bstack1lll11lll11_opy_, bstack1lll1l11lll_opy_)
    if self.bstack1lll1l11ll1_opy_:
      bstack1111ll111l_opy_ += bstack111l1ll_opy_ (u"ࠤࠩࡴࡪࡸࡣࡺࡡࡦࡥࡵࡺࡵࡳࡧࡢࡱࡴࡪࡥ࠾ࡽࢀࠦᗰ").format(self.bstack1lll1l11ll1_opy_)
    uri = bstack11lll1l1l_opy_(bstack1111ll111l_opy_)
    try:
      response = bstack11l11l1111_opy_(bstack111l1ll_opy_ (u"ࠪࡋࡊ࡚ࠧᗱ"), uri, {}, {bstack111l1ll_opy_ (u"ࠫࡦࡻࡴࡩࠩᗲ"): (self.config[bstack111l1ll_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᗳ")], self.config[bstack111l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᗴ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1lll11l111_opy_ = data.get(bstack111l1ll_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨᗵ"))
        self.bstack1lll1l11ll1_opy_ = data.get(bstack111l1ll_opy_ (u"ࠨࡲࡨࡶࡨࡿ࡟ࡤࡣࡳࡸࡺࡸࡥࡠ࡯ࡲࡨࡪ࠭ᗶ"))
        os.environ[bstack111l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟ࠧᗷ")] = str(self.bstack1lll11l111_opy_)
        os.environ[bstack111l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࡠࡅࡄࡔ࡙࡛ࡒࡆࡡࡐࡓࡉࡋࠧᗸ")] = str(self.bstack1lll1l11ll1_opy_)
        if bstack1lll1l11lll_opy_ == bstack111l1ll_opy_ (u"ࠦࡺࡴࡤࡦࡨ࡬ࡲࡪࡪࠢᗹ") and str(self.bstack1lll11l111_opy_).lower() == bstack111l1ll_opy_ (u"ࠧࡺࡲࡶࡧࠥᗺ"):
          self.bstack1llllll1ll_opy_ = True
        if bstack111l1ll_opy_ (u"ࠨࡴࡰ࡭ࡨࡲࠧᗻ") in data:
          return data[bstack111l1ll_opy_ (u"ࠢࡵࡱ࡮ࡩࡳࠨᗼ")]
        else:
          raise bstack111l1ll_opy_ (u"ࠨࡖࡲ࡯ࡪࡴࠠࡏࡱࡷࠤࡋࡵࡵ࡯ࡦࠣ࠱ࠥࢁࡽࠨᗽ").format(data)
      else:
        raise bstack111l1ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡵ࡫ࡲࡤࡻࠣࡸࡴࡱࡥ࡯࠮ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥࡹࡴࡢࡶࡸࡷࠥ࠳ࠠࡼࡿ࠯ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡂࡰࡦࡼࠤ࠲ࠦࡻࡾࠤᗾ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack111l1ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡴࡷࡵࡪࡦࡥࡷࠦᗿ").format(e))
  def bstack1lll11l111l_opy_(self):
    bstack1lll1l111ll_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1ll_opy_ (u"ࠦࡵ࡫ࡲࡤࡻࡆࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠢᘀ"))
    try:
      if bstack111l1ll_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ᘁ") not in self.bstack1lll11ll11l_opy_:
        self.bstack1lll11ll11l_opy_[bstack111l1ll_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧᘂ")] = 2
      with open(bstack1lll1l111ll_opy_, bstack111l1ll_opy_ (u"ࠧࡸࠩᘃ")) as fp:
        json.dump(self.bstack1lll11ll11l_opy_, fp)
      return bstack1lll1l111ll_opy_
    except Exception as e:
      self.logger.error(bstack111l1ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡨࡸࡥࡢࡶࡨࠤࡵ࡫ࡲࡤࡻࠣࡧࡴࡴࡦ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᘄ").format(e))
  def bstack1lll11l11ll_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1lll1l1l1ll_opy_ == bstack111l1ll_opy_ (u"ࠩࡺ࡭ࡳ࠭ᘅ"):
        bstack1lll1ll111l_opy_ = [bstack111l1ll_opy_ (u"ࠪࡧࡲࡪ࠮ࡦࡺࡨࠫᘆ"), bstack111l1ll_opy_ (u"ࠫ࠴ࡩࠧᘇ")]
        cmd = bstack1lll1ll111l_opy_ + cmd
      cmd = bstack111l1ll_opy_ (u"ࠬࠦࠧᘈ").join(cmd)
      self.logger.debug(bstack111l1ll_opy_ (u"ࠨࡒࡶࡰࡱ࡭ࡳ࡭ࠠࡼࡿࠥᘉ").format(cmd))
      with open(self.bstack1lll1lll1ll_opy_, bstack111l1ll_opy_ (u"ࠢࡢࠤᘊ")) as bstack1lll1ll11ll_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1lll1ll11ll_opy_, text=True, stderr=bstack1lll1ll11ll_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1lll1lll111_opy_ = True
      self.logger.error(bstack111l1ll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺࠢࡺ࡭ࡹ࡮ࠠࡤ࡯ࡧࠤ࠲ࠦࡻࡾ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࡼࡿࠥᘋ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1llll11111l_opy_:
        self.logger.info(bstack111l1ll_opy_ (u"ࠤࡖࡸࡴࡶࡰࡪࡰࡪࠤࡕ࡫ࡲࡤࡻࠥᘌ"))
        cmd = [self.binary_path, bstack111l1ll_opy_ (u"ࠥࡩࡽ࡫ࡣ࠻ࡵࡷࡳࡵࠨᘍ")]
        self.bstack1lll11l11ll_opy_(cmd)
        self.bstack1llll11111l_opy_ = False
    except Exception as e:
      self.logger.error(bstack111l1ll_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡲࡴࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡷࡪࡶ࡫ࠤࡨࡵ࡭࡮ࡣࡱࡨࠥ࠳ࠠࡼࡿ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠦᘎ").format(cmd, e))
  def bstack1l11111l11_opy_(self):
    if not self.bstack1lll11l111_opy_:
      return
    try:
      bstack1llll1111l1_opy_ = 0
      while not self.bstack1llll11111l_opy_ and bstack1llll1111l1_opy_ < self.bstack1lll1l1l1l1_opy_:
        if self.bstack1lll1lll111_opy_:
          self.logger.info(bstack111l1ll_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡸ࡫ࡴࡶࡲࠣࡪࡦ࡯࡬ࡦࡦࠥᘏ"))
          return
        time.sleep(1)
        bstack1llll1111l1_opy_ += 1
      os.environ[bstack111l1ll_opy_ (u"࠭ࡐࡆࡔࡆ࡝ࡤࡈࡅࡔࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࠬᘐ")] = str(self.bstack1lll11ll111_opy_())
      self.logger.info(bstack111l1ll_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡳࡦࡶࡸࡴࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡫ࡤࠣᘑ"))
    except Exception as e:
      self.logger.error(bstack111l1ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸ࡫ࡴࡶࡲࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᘒ").format(e))
  def bstack1lll11ll111_opy_(self):
    if self.bstack11l1l111ll_opy_:
      return
    try:
      bstack1lll11l1ll1_opy_ = [platform[bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧᘓ")].lower() for platform in self.config.get(bstack111l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ᘔ"), [])]
      bstack1lll1l1l111_opy_ = sys.maxsize
      bstack1lll1l11l1l_opy_ = bstack111l1ll_opy_ (u"ࠫࠬᘕ")
      for browser in bstack1lll11l1ll1_opy_:
        if browser in self.bstack1lll11l1l11_opy_:
          bstack1lll1l11111_opy_ = self.bstack1lll11l1l11_opy_[browser]
        if bstack1lll1l11111_opy_ < bstack1lll1l1l111_opy_:
          bstack1lll1l1l111_opy_ = bstack1lll1l11111_opy_
          bstack1lll1l11l1l_opy_ = browser
      return bstack1lll1l11l1l_opy_
    except Exception as e:
      self.logger.error(bstack111l1ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡢࡦࡵࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᘖ").format(e))
  @classmethod
  def bstack1ll11lll11_opy_(self):
    return os.getenv(bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࠫᘗ"), bstack111l1ll_opy_ (u"ࠧࡇࡣ࡯ࡷࡪ࠭ᘘ")).lower()
  @classmethod
  def bstack1111l1ll1_opy_(self):
    return os.getenv(bstack111l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞ࡥࡃࡂࡒࡗ࡙ࡗࡋ࡟ࡎࡑࡇࡉࠬᘙ"), bstack111l1ll_opy_ (u"ࠩࠪᘚ"))