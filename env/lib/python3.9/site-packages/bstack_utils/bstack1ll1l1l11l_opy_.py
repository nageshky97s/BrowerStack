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
class bstack111l1ll111_opy_(object):
  bstack11ll1l1l11_opy_ = os.path.join(os.path.expanduser(bstack111l1ll_opy_ (u"ࠩࢁࠫဤ")), bstack111l1ll_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪဥ"))
  bstack111l1l1lll_opy_ = os.path.join(bstack11ll1l1l11_opy_, bstack111l1ll_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠴ࡪࡴࡱࡱࠫဦ"))
  bstack111l1ll11l_opy_ = None
  perform_scan = None
  bstack1ll1111l1_opy_ = None
  bstack11llll1111_opy_ = None
  bstack111ll11lll_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack111l1ll_opy_ (u"ࠬ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠧဧ")):
      cls.instance = super(bstack111l1ll111_opy_, cls).__new__(cls)
      cls.instance.bstack111l1ll1l1_opy_()
    return cls.instance
  def bstack111l1ll1l1_opy_(self):
    try:
      with open(self.bstack111l1l1lll_opy_, bstack111l1ll_opy_ (u"࠭ࡲࠨဨ")) as bstack111111l1l_opy_:
        bstack111l1l1l1l_opy_ = bstack111111l1l_opy_.read()
        data = json.loads(bstack111l1l1l1l_opy_)
        if bstack111l1ll_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩဩ") in data:
          self.bstack111l1ll1ll_opy_(data[bstack111l1ll_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪဪ")])
        if bstack111l1ll_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪါ") in data:
          self.bstack111ll111ll_opy_(data[bstack111l1ll_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫာ")])
    except:
      pass
  def bstack111ll111ll_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts[bstack111l1ll_opy_ (u"ࠫࡸࡩࡡ࡯ࠩိ")]
      self.bstack1ll1111l1_opy_ = scripts[bstack111l1ll_opy_ (u"ࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠩီ")]
      self.bstack11llll1111_opy_ = scripts[bstack111l1ll_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠪု")]
      self.bstack111ll11lll_opy_ = scripts[bstack111l1ll_opy_ (u"ࠧࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠬူ")]
  def bstack111l1ll1ll_opy_(self, bstack111l1ll11l_opy_):
    if bstack111l1ll11l_opy_ != None and len(bstack111l1ll11l_opy_) != 0:
      self.bstack111l1ll11l_opy_ = bstack111l1ll11l_opy_
  def store(self):
    try:
      with open(self.bstack111l1l1lll_opy_, bstack111l1ll_opy_ (u"ࠨࡹࠪေ")) as file:
        json.dump({
          bstack111l1ll_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡶࠦဲ"): self.bstack111l1ll11l_opy_,
          bstack111l1ll_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࡶࠦဳ"): {
            bstack111l1ll_opy_ (u"ࠦࡸࡩࡡ࡯ࠤဴ"): self.perform_scan,
            bstack111l1ll_opy_ (u"ࠧ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠤဵ"): self.bstack1ll1111l1_opy_,
            bstack111l1ll_opy_ (u"ࠨࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠥံ"): self.bstack11llll1111_opy_,
            bstack111l1ll_opy_ (u"ࠢࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷ့ࠧ"): self.bstack111ll11lll_opy_
          }
        }, file)
    except:
      pass
  def bstack1l11l1l111_opy_(self, bstack111l1l1ll1_opy_):
    try:
      return any(command.get(bstack111l1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭း")) == bstack111l1l1ll1_opy_ for command in self.bstack111l1ll11l_opy_)
    except:
      return False
bstack1ll1l1l11l_opy_ = bstack111l1ll111_opy_()