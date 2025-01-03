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
bstack1l1l1ll11l_opy_ = {
	bstack111l1ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ၐ"): bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡳࠩၑ"),
  bstack111l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩၒ"): bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡫ࡦࡻࠪၓ"),
  bstack111l1ll_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫၔ"): bstack111l1ll_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ၕ"),
  bstack111l1ll_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪၖ"): bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫࡟ࡸ࠵ࡦࠫၗ"),
  bstack111l1ll_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪၘ"): bstack111l1ll_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࠧၙ"),
  bstack111l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪၚ"): bstack111l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࠧၛ"),
  bstack111l1ll_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧၜ"): bstack111l1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨၝ"),
  bstack111l1ll_opy_ (u"ࠫࡩ࡫ࡢࡶࡩࠪၞ"): bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡩ࡫ࡢࡶࡩࠪၟ"),
  bstack111l1ll_opy_ (u"࠭ࡣࡰࡰࡶࡳࡱ࡫ࡌࡰࡩࡶࠫၠ"): bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰࡰࡶࡳࡱ࡫ࠧၡ"),
  bstack111l1ll_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸ࠭ၢ"): bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸ࠭ၣ"),
  bstack111l1ll_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯ࡏࡳ࡬ࡹࠧၤ"): bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡵࡶࡩࡶ࡯ࡏࡳ࡬ࡹࠧၥ"),
  bstack111l1ll_opy_ (u"ࠬࡼࡩࡥࡧࡲࠫၦ"): bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡼࡩࡥࡧࡲࠫၧ"),
  bstack111l1ll_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭ၨ"): bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭ၩ"),
  bstack111l1ll_opy_ (u"ࠩࡷࡩࡱ࡫࡭ࡦࡶࡵࡽࡑࡵࡧࡴࠩၪ"): bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡱ࡫࡭ࡦࡶࡵࡽࡑࡵࡧࡴࠩၫ"),
  bstack111l1ll_opy_ (u"ࠫ࡬࡫࡯ࡍࡱࡦࡥࡹ࡯࡯࡯ࠩၬ"): bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡬࡫࡯ࡍࡱࡦࡥࡹ࡯࡯࡯ࠩၭ"),
  bstack111l1ll_opy_ (u"࠭ࡴࡪ࡯ࡨࡾࡴࡴࡥࠨၮ"): bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡪ࡯ࡨࡾࡴࡴࡥࠨၯ"),
  bstack111l1ll_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪၰ"): bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡵࡨࡰࡪࡴࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫၱ"),
  bstack111l1ll_opy_ (u"ࠪࡱࡦࡹ࡫ࡄࡱࡰࡱࡦࡴࡤࡴࠩၲ"): bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡱࡦࡹ࡫ࡄࡱࡰࡱࡦࡴࡤࡴࠩၳ"),
  bstack111l1ll_opy_ (u"ࠬ࡯ࡤ࡭ࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪၴ"): bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡯ࡤ࡭ࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪၵ"),
  bstack111l1ll_opy_ (u"ࠧ࡮ࡣࡶ࡯ࡇࡧࡳࡪࡥࡄࡹࡹ࡮ࠧၶ"): bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡮ࡣࡶ࡯ࡇࡧࡳࡪࡥࡄࡹࡹ࡮ࠧၷ"),
  bstack111l1ll_opy_ (u"ࠩࡶࡩࡳࡪࡋࡦࡻࡶࠫၸ"): bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡶࡩࡳࡪࡋࡦࡻࡶࠫၹ"),
  bstack111l1ll_opy_ (u"ࠫࡦࡻࡴࡰ࡙ࡤ࡭ࡹ࠭ၺ"): bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡻࡴࡰ࡙ࡤ࡭ࡹ࠭ၻ"),
  bstack111l1ll_opy_ (u"࠭ࡨࡰࡵࡷࡷࠬၼ"): bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡨࡰࡵࡷࡷࠬၽ"),
  bstack111l1ll_opy_ (u"ࠨࡤࡩࡧࡦࡩࡨࡦࠩၾ"): bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡩࡧࡦࡩࡨࡦࠩၿ"),
  bstack111l1ll_opy_ (u"ࠪࡻࡸࡒ࡯ࡤࡣ࡯ࡗࡺࡶࡰࡰࡴࡷࠫႀ"): bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡻࡸࡒ࡯ࡤࡣ࡯ࡗࡺࡶࡰࡰࡴࡷࠫႁ"),
  bstack111l1ll_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡉ࡯ࡳࡵࡕࡩࡸࡺࡲࡪࡥࡷ࡭ࡴࡴࡳࠨႂ"): bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡪࡩࡴࡣࡥࡰࡪࡉ࡯ࡳࡵࡕࡩࡸࡺࡲࡪࡥࡷ࡭ࡴࡴࡳࠨႃ"),
  bstack111l1ll_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫႄ"): bstack111l1ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨႅ"),
  bstack111l1ll_opy_ (u"ࠩࡵࡩࡦࡲࡍࡰࡤ࡬ࡰࡪ࠭ႆ"): bstack111l1ll_opy_ (u"ࠪࡶࡪࡧ࡬ࡠ࡯ࡲࡦ࡮ࡲࡥࠨႇ"),
  bstack111l1ll_opy_ (u"ࠫࡦࡶࡰࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫႈ"): bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡶࡰࡪࡷࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬႉ"),
  bstack111l1ll_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡔࡥࡵࡹࡲࡶࡰ࠭ႊ"): bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡶࡵࡷࡳࡲࡔࡥࡵࡹࡲࡶࡰ࠭ႋ"),
  bstack111l1ll_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡒࡵࡳ࡫࡯࡬ࡦࠩႌ"): bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡰࡨࡸࡼࡵࡲ࡬ࡒࡵࡳ࡫࡯࡬ࡦႍࠩ"),
  bstack111l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡌࡲࡸ࡫ࡣࡶࡴࡨࡇࡪࡸࡴࡴࠩႎ"): bstack111l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡗࡸࡲࡃࡦࡴࡷࡷࠬႏ"),
  bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ႐"): bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ႑"),
  bstack111l1ll_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ႒"): bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡴࡱࡸࡶࡨ࡫ࠧ႓"),
  bstack111l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ႔"): bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ႕"),
  bstack111l1ll_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭႖"): bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡭ࡵࡳࡵࡐࡤࡱࡪ࠭႗"),
  bstack111l1ll_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪ࡙ࡩ࡮ࠩ႘"): bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡥ࡯ࡣࡥࡰࡪ࡙ࡩ࡮ࠩ႙"),
  bstack111l1ll_opy_ (u"ࠨࡵ࡬ࡱࡔࡶࡴࡪࡱࡱࡷࠬႚ"): bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡵ࡬ࡱࡔࡶࡴࡪࡱࡱࡷࠬႛ"),
  bstack111l1ll_opy_ (u"ࠪࡹࡵࡲ࡯ࡢࡦࡐࡩࡩ࡯ࡡࠨႜ"): bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡵࡲ࡯ࡢࡦࡐࡩࡩ࡯ࡡࠨႝ"),
  bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ႞"): bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ႟"),
  bstack111l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩႠ"): bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩႡ")
}
bstack111l11l1ll_opy_ = [
  bstack111l1ll_opy_ (u"ࠩࡲࡷࠬႢ"),
  bstack111l1ll_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭Ⴃ"),
  bstack111l1ll_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭Ⴄ"),
  bstack111l1ll_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪႥ"),
  bstack111l1ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪႦ"),
  bstack111l1ll_opy_ (u"ࠧࡳࡧࡤࡰࡒࡵࡢࡪ࡮ࡨࠫႧ"),
  bstack111l1ll_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨႨ"),
]
bstack1l11ll111_opy_ = {
  bstack111l1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫႩ"): [bstack111l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡘࡗࡊࡘࡎࡂࡏࡈࠫႪ"), bstack111l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡙ࡘࡋࡒࡠࡐࡄࡑࡊ࠭Ⴋ")],
  bstack111l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨႬ"): bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩႭ"),
  bstack111l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪႮ"): bstack111l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡎࡂࡏࡈࠫႯ"),
  bstack111l1ll_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧႰ"): bstack111l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡖࡔࡐࡅࡄࡖࡢࡒࡆࡓࡅࠨႱ"),
  bstack111l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭Ⴒ"): bstack111l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧႳ"),
  bstack111l1ll_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭Ⴔ"): bstack111l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡂࡔࡄࡐࡑࡋࡌࡔࡡࡓࡉࡗࡥࡐࡍࡃࡗࡊࡔࡘࡍࠨႵ"),
  bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬႶ"): bstack111l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒࠧႷ"),
  bstack111l1ll_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡖࡨࡷࡹࡹࠧႸ"): bstack111l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࡡࡗࡉࡘ࡚ࡓࠨႹ"),
  bstack111l1ll_opy_ (u"ࠬࡧࡰࡱࠩႺ"): [bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡐࡑࡡࡌࡈࠬႻ"), bstack111l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡑࡒࠪႼ")],
  bstack111l1ll_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪႽ"): bstack111l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡕࡇࡏࡤࡒࡏࡈࡎࡈ࡚ࡊࡒࠧႾ"),
  bstack111l1ll_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧႿ"): bstack111l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧჀ"),
  bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩჁ"): bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡓࡇ࡙ࡅࡓࡘࡄࡆࡎࡒࡉࡕ࡛ࠪჂ"),
  bstack111l1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫჃ"): bstack111l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡗࡕࡆࡔ࡙ࡃࡂࡎࡈࠫჄ")
}
bstack1l11l1l1ll_opy_ = {
  bstack111l1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫჅ"): [bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪࡸ࡟࡯ࡣࡰࡩࠬ჆"), bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫ࡲࡏࡣࡰࡩࠬჇ")],
  bstack111l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ჈"): [bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷࡤࡱࡥࡺࠩ჉"), bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ჊")],
  bstack111l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ჋"): bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ჌"),
  bstack111l1ll_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨჍ"): bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨ჎"),
  bstack111l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ჏"): bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧა"),
  bstack111l1ll_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧბ"): [bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡱࡲࡳࠫგ"), bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨდ")],
  bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧე"): bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࠩვ"),
  bstack111l1ll_opy_ (u"ࠬࡸࡥࡳࡷࡱࡘࡪࡹࡴࡴࠩზ"): bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡸࡥࡳࡷࡱࡘࡪࡹࡴࡴࠩთ"),
  bstack111l1ll_opy_ (u"ࠧࡢࡲࡳࠫი"): bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡲࡳࠫკ"),
  bstack111l1ll_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫლ"): bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫმ"),
  bstack111l1ll_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨნ"): bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨო")
}
bstack1l1ll11l11_opy_ = {
  bstack111l1ll_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩპ"): bstack111l1ll_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫჟ"),
  bstack111l1ll_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪრ"): [bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡵࡨࡰࡪࡴࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫს"), bstack111l1ll_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ტ")],
  bstack111l1ll_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩუ"): bstack111l1ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪფ"),
  bstack111l1ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪქ"): bstack111l1ll_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧღ"),
  bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ყ"): [bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪშ"), bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡳࡧ࡭ࡦࠩჩ")],
  bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬც"): bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧძ"),
  bstack111l1ll_opy_ (u"࠭ࡲࡦࡣ࡯ࡑࡴࡨࡩ࡭ࡧࠪწ"): bstack111l1ll_opy_ (u"ࠧࡳࡧࡤࡰࡤࡳ࡯ࡣ࡫࡯ࡩࠬჭ"),
  bstack111l1ll_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨხ"): [bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡳࡴ࡮ࡻ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩჯ"), bstack111l1ll_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫჰ")],
  bstack111l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡍࡳࡹࡥࡤࡷࡵࡩࡈ࡫ࡲࡵࡵࠪჱ"): [bstack111l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡘࡹ࡬ࡄࡧࡵࡸࡸ࠭ჲ"), bstack111l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡴࡹ࡙ࡳ࡭ࡅࡨࡶࡹ࠭ჳ")]
}
bstack1ll1ll11l1_opy_ = [
  bstack111l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡉ࡯ࡵࡨࡧࡺࡸࡥࡄࡧࡵࡸࡸ࠭ჴ"),
  bstack111l1ll_opy_ (u"ࠨࡲࡤ࡫ࡪࡒ࡯ࡢࡦࡖࡸࡷࡧࡴࡦࡩࡼࠫჵ"),
  bstack111l1ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨჶ"),
  bstack111l1ll_opy_ (u"ࠪࡷࡪࡺࡗࡪࡰࡧࡳࡼࡘࡥࡤࡶࠪჷ"),
  bstack111l1ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡱࡸࡸࡸ࠭ჸ"),
  bstack111l1ll_opy_ (u"ࠬࡹࡴࡳ࡫ࡦࡸࡋ࡯࡬ࡦࡋࡱࡸࡪࡸࡡࡤࡶࡤࡦ࡮ࡲࡩࡵࡻࠪჹ"),
  bstack111l1ll_opy_ (u"࠭ࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࡒࡵࡳࡲࡶࡴࡃࡧ࡫ࡥࡻ࡯࡯ࡳࠩჺ"),
  bstack111l1ll_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ჻"),
  bstack111l1ll_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ჼ"),
  bstack111l1ll_opy_ (u"ࠩࡰࡷ࠿࡫ࡤࡨࡧࡒࡴࡹ࡯࡯࡯ࡵࠪჽ"),
  bstack111l1ll_opy_ (u"ࠪࡷࡪࡀࡩࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩჾ"),
  bstack111l1ll_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬჿ"),
]
bstack111l11ll1_opy_ = [
  bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩᄀ"),
  bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪᄁ"),
  bstack111l1ll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ᄂ"),
  bstack111l1ll_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᄃ"),
  bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᄄ"),
  bstack111l1ll_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬᄅ"),
  bstack111l1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᄆ"),
  bstack111l1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᄇ"),
  bstack111l1ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩᄈ"),
  bstack111l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬᄉ"),
  bstack111l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬᄊ"),
  bstack111l1ll_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠫᄋ"),
  bstack111l1ll_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡗࡥ࡬࠭ᄌ"),
  bstack111l1ll_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᄍ"),
  bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᄎ"),
  bstack111l1ll_opy_ (u"࠭ࡲࡦࡴࡸࡲ࡙࡫ࡳࡵࡵࠪᄏ"),
  bstack111l1ll_opy_ (u"ࠧࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣ࠶࠭ᄐ"),
  bstack111l1ll_opy_ (u"ࠨࡅࡘࡗ࡙ࡕࡍࡠࡖࡄࡋࡤ࠸ࠧᄑ"),
  bstack111l1ll_opy_ (u"ࠩࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࠳ࠨᄒ"),
  bstack111l1ll_opy_ (u"ࠪࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࠵ࠩᄓ"),
  bstack111l1ll_opy_ (u"ࠫࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࠷ࠪᄔ"),
  bstack111l1ll_opy_ (u"ࠬࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࠹ࠫᄕ"),
  bstack111l1ll_opy_ (u"࠭ࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢ࠻ࠬᄖ"),
  bstack111l1ll_opy_ (u"ࠧࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣ࠽࠭ᄗ"),
  bstack111l1ll_opy_ (u"ࠨࡅࡘࡗ࡙ࡕࡍࡠࡖࡄࡋࡤ࠿ࠧᄘ"),
  bstack111l1ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨᄙ"),
  bstack111l1ll_opy_ (u"ࠪࡴࡪࡸࡣࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᄚ"),
  bstack111l1ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧᄛ"),
  bstack111l1ll_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇࡵࡵࡱࡆࡥࡵࡺࡵࡳࡧࡏࡳ࡬ࡹࠧᄜ"),
  bstack111l1ll_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪᄝ"),
  bstack111l1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫᄞ")
]
bstack111l11l111_opy_ = [
  bstack111l1ll_opy_ (u"ࠨࡷࡳࡰࡴࡧࡤࡎࡧࡧ࡭ࡦ࠭ᄟ"),
  bstack111l1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᄠ"),
  bstack111l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᄡ"),
  bstack111l1ll_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩᄢ"),
  bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡓࡶ࡮ࡵࡲࡪࡶࡼࠫᄣ"),
  bstack111l1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩᄤ"),
  bstack111l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩ࡚ࡡࡨࠩᄥ"),
  bstack111l1ll_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᄦ"),
  bstack111l1ll_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫᄧ"),
  bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨᄨ"),
  bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᄩ"),
  bstack111l1ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫᄪ"),
  bstack111l1ll_opy_ (u"࠭࡯ࡴࠩᄫ"),
  bstack111l1ll_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪᄬ"),
  bstack111l1ll_opy_ (u"ࠨࡪࡲࡷࡹࡹࠧᄭ"),
  bstack111l1ll_opy_ (u"ࠩࡤࡹࡹࡵࡗࡢ࡫ࡷࠫᄮ"),
  bstack111l1ll_opy_ (u"ࠪࡶࡪ࡭ࡩࡰࡰࠪᄯ"),
  bstack111l1ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡼࡲࡲࡪ࠭ᄰ"),
  bstack111l1ll_opy_ (u"ࠬࡳࡡࡤࡪ࡬ࡲࡪ࠭ᄱ"),
  bstack111l1ll_opy_ (u"࠭ࡲࡦࡵࡲࡰࡺࡺࡩࡰࡰࠪᄲ"),
  bstack111l1ll_opy_ (u"ࠧࡪࡦ࡯ࡩ࡙࡯࡭ࡦࡱࡸࡸࠬᄳ"),
  bstack111l1ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡐࡴ࡬ࡩࡳࡺࡡࡵ࡫ࡲࡲࠬᄴ"),
  bstack111l1ll_opy_ (u"ࠩࡹ࡭ࡩ࡫࡯ࠨᄵ"),
  bstack111l1ll_opy_ (u"ࠪࡲࡴࡖࡡࡨࡧࡏࡳࡦࡪࡔࡪ࡯ࡨࡳࡺࡺࠧᄶ"),
  bstack111l1ll_opy_ (u"ࠫࡧ࡬ࡣࡢࡥ࡫ࡩࠬᄷ"),
  bstack111l1ll_opy_ (u"ࠬࡪࡥࡣࡷࡪࠫᄸ"),
  bstack111l1ll_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࡙ࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᄹ"),
  bstack111l1ll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡓࡦࡰࡧࡏࡪࡿࡳࠨᄺ"),
  bstack111l1ll_opy_ (u"ࠨࡴࡨࡥࡱࡓ࡯ࡣ࡫࡯ࡩࠬᄻ"),
  bstack111l1ll_opy_ (u"ࠩࡱࡳࡕ࡯ࡰࡦ࡮࡬ࡲࡪ࠭ᄼ"),
  bstack111l1ll_opy_ (u"ࠪࡧ࡭࡫ࡣ࡬ࡗࡕࡐࠬᄽ"),
  bstack111l1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᄾ"),
  bstack111l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡈࡵ࡯࡬࡫ࡨࡷࠬᄿ"),
  bstack111l1ll_opy_ (u"࠭ࡣࡢࡲࡷࡹࡷ࡫ࡃࡳࡣࡶ࡬ࠬᅀ"),
  bstack111l1ll_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫᅁ"),
  bstack111l1ll_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᅂ"),
  bstack111l1ll_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᅃ"),
  bstack111l1ll_opy_ (u"ࠪࡲࡴࡈ࡬ࡢࡰ࡮ࡔࡴࡲ࡬ࡪࡰࡪࠫᅄ"),
  bstack111l1ll_opy_ (u"ࠫࡲࡧࡳ࡬ࡕࡨࡲࡩࡑࡥࡺࡵࠪᅅ"),
  bstack111l1ll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡑࡵࡧࡴࠩᅆ"),
  bstack111l1ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡏࡤࠨᅇ"),
  bstack111l1ll_opy_ (u"ࠧࡥࡧࡧ࡭ࡨࡧࡴࡦࡦࡇࡩࡻ࡯ࡣࡦࠩᅈ"),
  bstack111l1ll_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡑࡣࡵࡥࡲࡹࠧᅉ"),
  bstack111l1ll_opy_ (u"ࠩࡳ࡬ࡴࡴࡥࡏࡷࡰࡦࡪࡸࠧᅊ"),
  bstack111l1ll_opy_ (u"ࠪࡲࡪࡺࡷࡰࡴ࡮ࡐࡴ࡭ࡳࠨᅋ"),
  bstack111l1ll_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡑࡵࡧࡴࡑࡳࡸ࡮ࡵ࡮ࡴࠩᅌ"),
  bstack111l1ll_opy_ (u"ࠬࡩ࡯࡯ࡵࡲࡰࡪࡒ࡯ࡨࡵࠪᅍ"),
  bstack111l1ll_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ᅎ"),
  bstack111l1ll_opy_ (u"ࠧࡢࡲࡳ࡭ࡺࡳࡌࡰࡩࡶࠫᅏ"),
  bstack111l1ll_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡃ࡫ࡲࡱࡪࡺࡲࡪࡥࠪᅐ"),
  bstack111l1ll_opy_ (u"ࠩࡹ࡭ࡩ࡫࡯ࡗ࠴ࠪᅑ"),
  bstack111l1ll_opy_ (u"ࠪࡱ࡮ࡪࡓࡦࡵࡶ࡭ࡴࡴࡉ࡯ࡵࡷࡥࡱࡲࡁࡱࡲࡶࠫᅒ"),
  bstack111l1ll_opy_ (u"ࠫࡪࡹࡰࡳࡧࡶࡷࡴ࡙ࡥࡳࡸࡨࡶࠬᅓ"),
  bstack111l1ll_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡌࡰࡩࡶࠫᅔ"),
  bstack111l1ll_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡄࡦࡳࠫᅕ"),
  bstack111l1ll_opy_ (u"ࠧࡵࡧ࡯ࡩࡲ࡫ࡴࡳࡻࡏࡳ࡬ࡹࠧᅖ"),
  bstack111l1ll_opy_ (u"ࠨࡵࡼࡲࡨ࡚ࡩ࡮ࡧ࡚࡭ࡹ࡮ࡎࡕࡒࠪᅗ"),
  bstack111l1ll_opy_ (u"ࠩࡪࡩࡴࡒ࡯ࡤࡣࡷ࡭ࡴࡴࠧᅘ"),
  bstack111l1ll_opy_ (u"ࠪ࡫ࡵࡹࡌࡰࡥࡤࡸ࡮ࡵ࡮ࠨᅙ"),
  bstack111l1ll_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡕࡸ࡯ࡧ࡫࡯ࡩࠬᅚ"),
  bstack111l1ll_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡓ࡫ࡴࡸࡱࡵ࡯ࠬᅛ"),
  bstack111l1ll_opy_ (u"࠭ࡦࡰࡴࡦࡩࡈ࡮ࡡ࡯ࡩࡨࡎࡦࡸࠧᅜ"),
  bstack111l1ll_opy_ (u"ࠧࡹ࡯ࡶࡎࡦࡸࠧᅝ"),
  bstack111l1ll_opy_ (u"ࠨࡺࡰࡼࡏࡧࡲࠨᅞ"),
  bstack111l1ll_opy_ (u"ࠩࡰࡥࡸࡱࡃࡰ࡯ࡰࡥࡳࡪࡳࠨᅟ"),
  bstack111l1ll_opy_ (u"ࠪࡱࡦࡹ࡫ࡃࡣࡶ࡭ࡨࡇࡵࡵࡪࠪᅠ"),
  bstack111l1ll_opy_ (u"ࠫࡼࡹࡌࡰࡥࡤࡰࡘࡻࡰࡱࡱࡵࡸࠬᅡ"),
  bstack111l1ll_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡉ࡯ࡳࡵࡕࡩࡸࡺࡲࡪࡥࡷ࡭ࡴࡴࡳࠨᅢ"),
  bstack111l1ll_opy_ (u"࠭ࡡࡱࡲ࡙ࡩࡷࡹࡩࡰࡰࠪᅣ"),
  bstack111l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡉ࡯ࡵࡨࡧࡺࡸࡥࡄࡧࡵࡸࡸ࠭ᅤ"),
  bstack111l1ll_opy_ (u"ࠨࡴࡨࡷ࡮࡭࡮ࡂࡲࡳࠫᅥ"),
  bstack111l1ll_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡲ࡮ࡳࡡࡵ࡫ࡲࡲࡸ࠭ᅦ"),
  bstack111l1ll_opy_ (u"ࠪࡧࡦࡴࡡࡳࡻࠪᅧ"),
  bstack111l1ll_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬᅨ"),
  bstack111l1ll_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬᅩ"),
  bstack111l1ll_opy_ (u"࠭ࡩࡦࠩᅪ"),
  bstack111l1ll_opy_ (u"ࠧࡦࡦࡪࡩࠬᅫ"),
  bstack111l1ll_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨᅬ"),
  bstack111l1ll_opy_ (u"ࠩࡴࡹࡪࡻࡥࠨᅭ"),
  bstack111l1ll_opy_ (u"ࠪ࡭ࡳࡺࡥࡳࡰࡤࡰࠬᅮ"),
  bstack111l1ll_opy_ (u"ࠫࡦࡶࡰࡔࡶࡲࡶࡪࡉ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠬᅯ"),
  bstack111l1ll_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡈࡧ࡭ࡦࡴࡤࡍࡲࡧࡧࡦࡋࡱ࡮ࡪࡩࡴࡪࡱࡱࠫᅰ"),
  bstack111l1ll_opy_ (u"࠭࡮ࡦࡶࡺࡳࡷࡱࡌࡰࡩࡶࡉࡽࡩ࡬ࡶࡦࡨࡌࡴࡹࡴࡴࠩᅱ"),
  bstack111l1ll_opy_ (u"ࠧ࡯ࡧࡷࡻࡴࡸ࡫ࡍࡱࡪࡷࡎࡴࡣ࡭ࡷࡧࡩࡍࡵࡳࡵࡵࠪᅲ"),
  bstack111l1ll_opy_ (u"ࠨࡷࡳࡨࡦࡺࡥࡂࡲࡳࡗࡪࡺࡴࡪࡰࡪࡷࠬᅳ"),
  bstack111l1ll_opy_ (u"ࠩࡵࡩࡸ࡫ࡲࡷࡧࡇࡩࡻ࡯ࡣࡦࠩᅴ"),
  bstack111l1ll_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪᅵ"),
  bstack111l1ll_opy_ (u"ࠫࡸ࡫࡮ࡥࡍࡨࡽࡸ࠭ᅶ"),
  bstack111l1ll_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡕࡧࡳࡴࡥࡲࡨࡪ࠭ᅷ"),
  bstack111l1ll_opy_ (u"࠭ࡵࡱࡦࡤࡸࡪࡏ࡯ࡴࡆࡨࡺ࡮ࡩࡥࡔࡧࡷࡸ࡮ࡴࡧࡴࠩᅸ"),
  bstack111l1ll_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡁࡶࡦ࡬ࡳࡎࡴࡪࡦࡥࡷ࡭ࡴࡴࠧᅹ"),
  bstack111l1ll_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡂࡲࡳࡰࡪࡖࡡࡺࠩᅺ"),
  bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪᅻ"),
  bstack111l1ll_opy_ (u"ࠪࡻࡩ࡯࡯ࡔࡧࡵࡺ࡮ࡩࡥࠨᅼ"),
  bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᅽ"),
  bstack111l1ll_opy_ (u"ࠬࡶࡲࡦࡸࡨࡲࡹࡉࡲࡰࡵࡶࡗ࡮ࡺࡥࡕࡴࡤࡧࡰ࡯࡮ࡨࠩᅾ"),
  bstack111l1ll_opy_ (u"࠭ࡨࡪࡩ࡫ࡇࡴࡴࡴࡳࡣࡶࡸࠬᅿ"),
  bstack111l1ll_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡐࡳࡧࡩࡩࡷ࡫࡮ࡤࡧࡶࠫᆀ"),
  bstack111l1ll_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡔ࡫ࡰࠫᆁ"),
  bstack111l1ll_opy_ (u"ࠩࡶ࡭ࡲࡕࡰࡵ࡫ࡲࡲࡸ࠭ᆂ"),
  bstack111l1ll_opy_ (u"ࠪࡶࡪࡳ࡯ࡷࡧࡌࡓࡘࡇࡰࡱࡕࡨࡸࡹ࡯࡮ࡨࡵࡏࡳࡨࡧ࡬ࡪࡼࡤࡸ࡮ࡵ࡮ࠨᆃ"),
  bstack111l1ll_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭ᆄ"),
  bstack111l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᆅ"),
  bstack111l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠨᆆ"),
  bstack111l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭ᆇ"),
  bstack111l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪᆈ"),
  bstack111l1ll_opy_ (u"ࠩࡳࡥ࡬࡫ࡌࡰࡣࡧࡗࡹࡸࡡࡵࡧࡪࡽࠬᆉ"),
  bstack111l1ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩᆊ"),
  bstack111l1ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡱࡸࡸࡸ࠭ᆋ"),
  bstack111l1ll_opy_ (u"ࠬࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡑࡴࡲࡱࡵࡺࡂࡦࡪࡤࡺ࡮ࡵࡲࠨᆌ")
]
bstack1l11ll1111_opy_ = {
  bstack111l1ll_opy_ (u"࠭ࡶࠨᆍ"): bstack111l1ll_opy_ (u"ࠧࡷࠩᆎ"),
  bstack111l1ll_opy_ (u"ࠨࡨࠪᆏ"): bstack111l1ll_opy_ (u"ࠩࡩࠫᆐ"),
  bstack111l1ll_opy_ (u"ࠪࡪࡴࡸࡣࡦࠩᆑ"): bstack111l1ll_opy_ (u"ࠫ࡫ࡵࡲࡤࡧࠪᆒ"),
  bstack111l1ll_opy_ (u"ࠬࡵ࡮࡭ࡻࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᆓ"): bstack111l1ll_opy_ (u"࠭࡯࡯࡮ࡼࡅࡺࡺ࡯࡮ࡣࡷࡩࠬᆔ"),
  bstack111l1ll_opy_ (u"ࠧࡧࡱࡵࡧࡪࡲ࡯ࡤࡣ࡯ࠫᆕ"): bstack111l1ll_opy_ (u"ࠨࡨࡲࡶࡨ࡫࡬ࡰࡥࡤࡰࠬᆖ"),
  bstack111l1ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡩࡱࡶࡸࠬᆗ"): bstack111l1ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡊࡲࡷࡹ࠭ᆘ"),
  bstack111l1ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡳࡳࡷࡺࠧᆙ"): bstack111l1ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡴࡸࡴࠨᆚ"),
  bstack111l1ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࡺࡹࡥࡳࠩᆛ"): bstack111l1ll_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡛ࡳࡦࡴࠪᆜ"),
  bstack111l1ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࡰࡢࡵࡶࠫᆝ"): bstack111l1ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡣࡶࡷࠬᆞ"),
  bstack111l1ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡲࡵࡳࡽࡿࡨࡰࡵࡷࠫᆟ"): bstack111l1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡉࡱࡶࡸࠬᆠ"),
  bstack111l1ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡴࡷࡵࡸࡺࡲࡲࡶࡹ࠭ᆡ"): bstack111l1ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡓࡳࡷࡺࠧᆢ"),
  bstack111l1ll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡶࡲࡰࡺࡼࡹࡸ࡫ࡲࠨᆣ"): bstack111l1ll_opy_ (u"ࠨ࠯࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾ࡛ࡳࡦࡴࠪᆤ"),
  bstack111l1ll_opy_ (u"ࠩ࠰ࡰࡴࡩࡡ࡭ࡲࡵࡳࡽࡿࡵࡴࡧࡵࠫᆥ"): bstack111l1ll_opy_ (u"ࠪ࠱ࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡖࡵࡨࡶࠬᆦ"),
  bstack111l1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡳࡶࡴࡾࡹࡱࡣࡶࡷࠬᆧ"): bstack111l1ll_opy_ (u"ࠬ࠳࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡓࡥࡸࡹࠧᆨ"),
  bstack111l1ll_opy_ (u"࠭࠭࡭ࡱࡦࡥࡱࡶࡲࡰࡺࡼࡴࡦࡹࡳࠨᆩ"): bstack111l1ll_opy_ (u"ࠧ࠮࡮ࡲࡧࡦࡲࡐࡳࡱࡻࡽࡕࡧࡳࡴࠩᆪ"),
  bstack111l1ll_opy_ (u"ࠨࡤ࡬ࡲࡦࡸࡹࡱࡣࡷ࡬ࠬᆫ"): bstack111l1ll_opy_ (u"ࠩࡥ࡭ࡳࡧࡲࡺࡲࡤࡸ࡭࠭ᆬ"),
  bstack111l1ll_opy_ (u"ࠪࡴࡦࡩࡦࡪ࡮ࡨࠫᆭ"): bstack111l1ll_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧᆮ"),
  bstack111l1ll_opy_ (u"ࠬࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧᆯ"): bstack111l1ll_opy_ (u"࠭࠭ࡱࡣࡦ࠱࡫࡯࡬ࡦࠩᆰ"),
  bstack111l1ll_opy_ (u"ࠧ࠮ࡲࡤࡧ࠲࡬ࡩ࡭ࡧࠪᆱ"): bstack111l1ll_opy_ (u"ࠨ࠯ࡳࡥࡨ࠳ࡦࡪ࡮ࡨࠫᆲ"),
  bstack111l1ll_opy_ (u"ࠩ࡯ࡳ࡬࡬ࡩ࡭ࡧࠪᆳ"): bstack111l1ll_opy_ (u"ࠪࡰࡴ࡭ࡦࡪ࡮ࡨࠫᆴ"),
  bstack111l1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᆵ"): bstack111l1ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᆶ"),
  bstack111l1ll_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࠳ࡲࡦࡲࡨࡥࡹ࡫ࡲࠨᆷ"): bstack111l1ll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡲࡨࡥࡹ࡫ࡲࠨᆸ")
}
bstack111l1111l1_opy_ = bstack111l1ll_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡪ࡭ࡹ࡮ࡵࡣ࠰ࡦࡳࡲ࠵ࡰࡦࡴࡦࡽ࠴ࡩ࡬ࡪ࠱ࡵࡩࡱ࡫ࡡࡴࡧࡶ࠳ࡱࡧࡴࡦࡵࡷ࠳ࡩࡵࡷ࡯࡮ࡲࡥࡩࠨᆹ")
bstack1111llll1l_opy_ = bstack111l1ll_opy_ (u"ࠤ࠲ࡴࡪࡸࡣࡺ࠱࡫ࡩࡦࡲࡴࡩࡥ࡫ࡩࡨࡱࠢᆺ")
bstack1lll1l111_opy_ = bstack111l1ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳࡭ࡻࡢ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡼࡪ࠯ࡩࡷࡥࠫᆻ")
bstack11111ll11_opy_ = bstack111l1ll_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳࡭ࡻࡢ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠧᆼ")
bstack1ll1lll1ll_opy_ = bstack111l1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡨࡶࡤ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵࡮ࡦࡺࡷࡣ࡭ࡻࡢࡴࠩᆽ")
bstack111l11ll11_opy_ = {
  bstack111l1ll_opy_ (u"࠭ࡣࡳ࡫ࡷ࡭ࡨࡧ࡬ࠨᆾ"): 50,
  bstack111l1ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᆿ"): 40,
  bstack111l1ll_opy_ (u"ࠨࡹࡤࡶࡳ࡯࡮ࡨࠩᇀ"): 30,
  bstack111l1ll_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧᇁ"): 20,
  bstack111l1ll_opy_ (u"ࠪࡨࡪࡨࡵࡨࠩᇂ"): 10
}
bstack1ll1l11lll_opy_ = bstack111l11ll11_opy_[bstack111l1ll_opy_ (u"ࠫ࡮ࡴࡦࡰࠩᇃ")]
bstack1llll11l1l_opy_ = bstack111l1ll_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࠫᇄ")
bstack1llll11l1_opy_ = bstack111l1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࠫᇅ")
bstack1ll1l11l1_opy_ = bstack111l1ll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫࠭ࡱࡻࡷ࡬ࡴࡴࡡࡨࡧࡱࡸ࠴࠭ᇆ")
bstack11l1ll1ll1_opy_ = bstack111l1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵ࠧᇇ")
bstack1llllll1l_opy_ = bstack111l1ll_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶࠣࡥࡳࡪࠠࡱࡻࡷࡩࡸࡺ࠭ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠢࡳࡥࡨࡱࡡࡨࡧࡶ࠲ࠥࡦࡰࡪࡲࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷࠤࡵࡿࡴࡦࡵࡷ࠱ࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡦࠧᇈ")
bstack111l11l1l1_opy_ = [bstack111l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡘࡗࡊࡘࡎࡂࡏࡈࠫᇉ"), bstack111l1ll_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡘࡗࡊࡘࡎࡂࡏࡈࠫᇊ")]
bstack1111llllll_opy_ = [bstack111l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡉࡃࡆࡕࡖࡣࡐࡋ࡙ࠨᇋ"), bstack111l1ll_opy_ (u"࡙࠭ࡐࡗࡕࡣࡆࡉࡃࡆࡕࡖࡣࡐࡋ࡙ࠨᇌ")]
bstack1ll11l1l1l_opy_ = re.compile(bstack111l1ll_opy_ (u"ࠧ࡟࡝࡟ࡠࡼ࠳࡝ࠬ࠼࠱࠮ࠩ࠭ᇍ"))
bstack111lllll1l_opy_ = [
  bstack111l1ll_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡓࡧ࡭ࡦࠩᇎ"),
  bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫᇏ"),
  bstack111l1ll_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧᇐ"),
  bstack111l1ll_opy_ (u"ࠫࡳ࡫ࡷࡄࡱࡰࡱࡦࡴࡤࡕ࡫ࡰࡩࡴࡻࡴࠨᇑ"),
  bstack111l1ll_opy_ (u"ࠬࡧࡰࡱࠩᇒ"),
  bstack111l1ll_opy_ (u"࠭ࡵࡥ࡫ࡧࠫᇓ"),
  bstack111l1ll_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࠩᇔ"),
  bstack111l1ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡥࠨᇕ"),
  bstack111l1ll_opy_ (u"ࠩࡲࡶ࡮࡫࡮ࡵࡣࡷ࡭ࡴࡴࠧᇖ"),
  bstack111l1ll_opy_ (u"ࠪࡥࡺࡺ࡯ࡘࡧࡥࡺ࡮࡫ࡷࠨᇗ"),
  bstack111l1ll_opy_ (u"ࠫࡳࡵࡒࡦࡵࡨࡸࠬᇘ"), bstack111l1ll_opy_ (u"ࠬ࡬ࡵ࡭࡮ࡕࡩࡸ࡫ࡴࠨᇙ"),
  bstack111l1ll_opy_ (u"࠭ࡣ࡭ࡧࡤࡶࡘࡿࡳࡵࡧࡰࡊ࡮ࡲࡥࡴࠩᇚ"),
  bstack111l1ll_opy_ (u"ࠧࡦࡸࡨࡲࡹ࡚ࡩ࡮࡫ࡱ࡫ࡸ࠭ᇛ"),
  bstack111l1ll_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡑࡧࡵࡪࡴࡸ࡭ࡢࡰࡦࡩࡑࡵࡧࡨ࡫ࡱ࡫ࠬᇜ"),
  bstack111l1ll_opy_ (u"ࠩࡲࡸ࡭࡫ࡲࡂࡲࡳࡷࠬᇝ"),
  bstack111l1ll_opy_ (u"ࠪࡴࡷ࡯࡮ࡵࡒࡤ࡫ࡪ࡙࡯ࡶࡴࡦࡩࡔࡴࡆࡪࡰࡧࡊࡦ࡯࡬ࡶࡴࡨࠫᇞ"),
  bstack111l1ll_opy_ (u"ࠫࡦࡶࡰࡂࡥࡷ࡭ࡻ࡯ࡴࡺࠩᇟ"), bstack111l1ll_opy_ (u"ࠬࡧࡰࡱࡒࡤࡧࡰࡧࡧࡦࠩᇠ"), bstack111l1ll_opy_ (u"࠭ࡡࡱࡲ࡚ࡥ࡮ࡺࡁࡤࡶ࡬ࡺ࡮ࡺࡹࠨᇡ"), bstack111l1ll_opy_ (u"ࠧࡢࡲࡳ࡛ࡦ࡯ࡴࡑࡣࡦ࡯ࡦ࡭ࡥࠨᇢ"), bstack111l1ll_opy_ (u"ࠨࡣࡳࡴ࡜ࡧࡩࡵࡆࡸࡶࡦࡺࡩࡰࡰࠪᇣ"),
  bstack111l1ll_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡔࡨࡥࡩࡿࡔࡪ࡯ࡨࡳࡺࡺࠧᇤ"),
  bstack111l1ll_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡖࡨࡷࡹࡖࡡࡤ࡭ࡤ࡫ࡪࡹࠧᇥ"),
  bstack111l1ll_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࡈࡵࡶࡦࡴࡤ࡫ࡪ࠭ᇦ"), bstack111l1ll_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩࡉ࡯ࡷࡧࡵࡥ࡬࡫ࡅ࡯ࡦࡌࡲࡹ࡫࡮ࡵࠩᇧ"),
  bstack111l1ll_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡄࡦࡸ࡬ࡧࡪࡘࡥࡢࡦࡼࡘ࡮ࡳࡥࡰࡷࡷࠫᇨ"),
  bstack111l1ll_opy_ (u"ࠧࡢࡦࡥࡔࡴࡸࡴࠨᇩ"),
  bstack111l1ll_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡆࡨࡺ࡮ࡩࡥࡔࡱࡦ࡯ࡪࡺࠧᇪ"),
  bstack111l1ll_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡌࡲࡸࡺࡡ࡭࡮ࡗ࡭ࡲ࡫࡯ࡶࡶࠪᇫ"),
  bstack111l1ll_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࡍࡳࡹࡴࡢ࡮࡯ࡔࡦࡺࡨࠨᇬ"),
  bstack111l1ll_opy_ (u"ࠫࡦࡼࡤࠨᇭ"), bstack111l1ll_opy_ (u"ࠬࡧࡶࡥࡎࡤࡹࡳࡩࡨࡕ࡫ࡰࡩࡴࡻࡴࠨᇮ"), bstack111l1ll_opy_ (u"࠭ࡡࡷࡦࡕࡩࡦࡪࡹࡕ࡫ࡰࡩࡴࡻࡴࠨᇯ"), bstack111l1ll_opy_ (u"ࠧࡢࡸࡧࡅࡷ࡭ࡳࠨᇰ"),
  bstack111l1ll_opy_ (u"ࠨࡷࡶࡩࡐ࡫ࡹࡴࡶࡲࡶࡪ࠭ᇱ"), bstack111l1ll_opy_ (u"ࠩ࡮ࡩࡾࡹࡴࡰࡴࡨࡔࡦࡺࡨࠨᇲ"), bstack111l1ll_opy_ (u"ࠪ࡯ࡪࡿࡳࡵࡱࡵࡩࡕࡧࡳࡴࡹࡲࡶࡩ࠭ᇳ"),
  bstack111l1ll_opy_ (u"ࠫࡰ࡫ࡹࡂ࡮࡬ࡥࡸ࠭ᇴ"), bstack111l1ll_opy_ (u"ࠬࡱࡥࡺࡒࡤࡷࡸࡽ࡯ࡳࡦࠪᇵ"),
  bstack111l1ll_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶࡊࡾࡥࡤࡷࡷࡥࡧࡲࡥࠨᇶ"), bstack111l1ll_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡇࡲࡨࡵࠪᇷ"), bstack111l1ll_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡥࡴ࡬ࡺࡪࡸࡅࡹࡧࡦࡹࡹࡧࡢ࡭ࡧࡇ࡭ࡷ࠭ᇸ"), bstack111l1ll_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡦࡵ࡭ࡻ࡫ࡲࡄࡪࡵࡳࡲ࡫ࡍࡢࡲࡳ࡭ࡳ࡭ࡆࡪ࡮ࡨࠫᇹ"), bstack111l1ll_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡗࡶࡩࡘࡿࡳࡵࡧࡰࡉࡽ࡫ࡣࡶࡶࡤࡦࡱ࡫ࠧᇺ"),
  bstack111l1ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡓࡳࡷࡺࠧᇻ"), bstack111l1ll_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵࡔࡴࡸࡴࡴࠩᇼ"),
  bstack111l1ll_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶࡉ࡯ࡳࡢࡤ࡯ࡩࡇࡻࡩ࡭ࡦࡆ࡬ࡪࡩ࡫ࠨᇽ"),
  bstack111l1ll_opy_ (u"ࠧࡢࡷࡷࡳ࡜࡫ࡢࡷ࡫ࡨࡻ࡙࡯࡭ࡦࡱࡸࡸࠬᇾ"),
  bstack111l1ll_opy_ (u"ࠨ࡫ࡱࡸࡪࡴࡴࡂࡥࡷ࡭ࡴࡴࠧᇿ"), bstack111l1ll_opy_ (u"ࠩ࡬ࡲࡹ࡫࡮ࡵࡅࡤࡸࡪ࡭࡯ࡳࡻࠪሀ"), bstack111l1ll_opy_ (u"ࠪ࡭ࡳࡺࡥ࡯ࡶࡉࡰࡦ࡭ࡳࠨሁ"), bstack111l1ll_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡥࡱࡏ࡮ࡵࡧࡱࡸࡆࡸࡧࡶ࡯ࡨࡲࡹࡹࠧሂ"),
  bstack111l1ll_opy_ (u"ࠬࡪ࡯࡯ࡶࡖࡸࡴࡶࡁࡱࡲࡒࡲࡗ࡫ࡳࡦࡶࠪሃ"),
  bstack111l1ll_opy_ (u"࠭ࡵ࡯࡫ࡦࡳࡩ࡫ࡋࡦࡻࡥࡳࡦࡸࡤࠨሄ"), bstack111l1ll_opy_ (u"ࠧࡳࡧࡶࡩࡹࡑࡥࡺࡤࡲࡥࡷࡪࠧህ"),
  bstack111l1ll_opy_ (u"ࠨࡰࡲࡗ࡮࡭࡮ࠨሆ"),
  bstack111l1ll_opy_ (u"ࠩ࡬࡫ࡳࡵࡲࡦࡗࡱ࡭ࡲࡶ࡯ࡳࡶࡤࡲࡹ࡜ࡩࡦࡹࡶࠫሇ"),
  bstack111l1ll_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡳࡪࡲࡰ࡫ࡧ࡛ࡦࡺࡣࡩࡧࡵࡷࠬለ"),
  bstack111l1ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫሉ"),
  bstack111l1ll_opy_ (u"ࠬࡸࡥࡤࡴࡨࡥࡹ࡫ࡃࡩࡴࡲࡱࡪࡊࡲࡪࡸࡨࡶࡘ࡫ࡳࡴ࡫ࡲࡲࡸ࠭ሊ"),
  bstack111l1ll_opy_ (u"࠭࡮ࡢࡶ࡬ࡺࡪ࡝ࡥࡣࡕࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬላ"),
  bstack111l1ll_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡔࡥࡵࡩࡪࡴࡳࡩࡱࡷࡔࡦࡺࡨࠨሌ"),
  bstack111l1ll_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡕࡳࡩࡪࡪࠧል"),
  bstack111l1ll_opy_ (u"ࠩࡪࡴࡸࡋ࡮ࡢࡤ࡯ࡩࡩ࠭ሎ"),
  bstack111l1ll_opy_ (u"ࠪ࡭ࡸࡎࡥࡢࡦ࡯ࡩࡸࡹࠧሏ"),
  bstack111l1ll_opy_ (u"ࠫࡦࡪࡢࡆࡺࡨࡧ࡙࡯࡭ࡦࡱࡸࡸࠬሐ"),
  bstack111l1ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡩࡘࡩࡲࡪࡲࡷࠫሑ"),
  bstack111l1ll_opy_ (u"࠭ࡳ࡬࡫ࡳࡈࡪࡼࡩࡤࡧࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡦࡺࡩࡰࡰࠪሒ"),
  bstack111l1ll_opy_ (u"ࠧࡢࡷࡷࡳࡌࡸࡡ࡯ࡶࡓࡩࡷࡳࡩࡴࡵ࡬ࡳࡳࡹࠧሓ"),
  bstack111l1ll_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡐࡤࡸࡺࡸࡡ࡭ࡑࡵ࡭ࡪࡴࡴࡢࡶ࡬ࡳࡳ࠭ሔ"),
  bstack111l1ll_opy_ (u"ࠩࡶࡽࡸࡺࡥ࡮ࡒࡲࡶࡹ࠭ሕ"),
  bstack111l1ll_opy_ (u"ࠪࡶࡪࡳ࡯ࡵࡧࡄࡨࡧࡎ࡯ࡴࡶࠪሖ"),
  bstack111l1ll_opy_ (u"ࠫࡸࡱࡩࡱࡗࡱࡰࡴࡩ࡫ࠨሗ"), bstack111l1ll_opy_ (u"ࠬࡻ࡮࡭ࡱࡦ࡯࡙ࡿࡰࡦࠩመ"), bstack111l1ll_opy_ (u"࠭ࡵ࡯࡮ࡲࡧࡰࡑࡥࡺࠩሙ"),
  bstack111l1ll_opy_ (u"ࠧࡢࡷࡷࡳࡑࡧࡵ࡯ࡥ࡫ࠫሚ"),
  bstack111l1ll_opy_ (u"ࠨࡵ࡮࡭ࡵࡒ࡯ࡨࡥࡤࡸࡈࡧࡰࡵࡷࡵࡩࠬማ"),
  bstack111l1ll_opy_ (u"ࠩࡸࡲ࡮ࡴࡳࡵࡣ࡯ࡰࡔࡺࡨࡦࡴࡓࡥࡨࡱࡡࡨࡧࡶࠫሜ"),
  bstack111l1ll_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨ࡛࡮ࡴࡤࡰࡹࡄࡲ࡮ࡳࡡࡵ࡫ࡲࡲࠬም"),
  bstack111l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡗࡳࡴࡲࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨሞ"),
  bstack111l1ll_opy_ (u"ࠬ࡫࡮ࡧࡱࡵࡧࡪࡇࡰࡱࡋࡱࡷࡹࡧ࡬࡭ࠩሟ"),
  bstack111l1ll_opy_ (u"࠭ࡥ࡯ࡵࡸࡶࡪ࡝ࡥࡣࡸ࡬ࡩࡼࡹࡈࡢࡸࡨࡔࡦ࡭ࡥࡴࠩሠ"), bstack111l1ll_opy_ (u"ࠧࡸࡧࡥࡺ࡮࡫ࡷࡅࡧࡹࡸࡴࡵ࡬ࡴࡒࡲࡶࡹ࠭ሡ"), bstack111l1ll_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡘࡧࡥࡺ࡮࡫ࡷࡅࡧࡷࡥ࡮ࡲࡳࡄࡱ࡯ࡰࡪࡩࡴࡪࡱࡱࠫሢ"),
  bstack111l1ll_opy_ (u"ࠩࡵࡩࡲࡵࡴࡦࡃࡳࡴࡸࡉࡡࡤࡪࡨࡐ࡮ࡳࡩࡵࠩሣ"),
  bstack111l1ll_opy_ (u"ࠪࡧࡦࡲࡥ࡯ࡦࡤࡶࡋࡵࡲ࡮ࡣࡷࠫሤ"),
  bstack111l1ll_opy_ (u"ࠫࡧࡻ࡮ࡥ࡮ࡨࡍࡩ࠭ሥ"),
  bstack111l1ll_opy_ (u"ࠬࡲࡡࡶࡰࡦ࡬࡙࡯࡭ࡦࡱࡸࡸࠬሦ"),
  bstack111l1ll_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࡔࡧࡵࡺ࡮ࡩࡥࡴࡇࡱࡥࡧࡲࡥࡥࠩሧ"), bstack111l1ll_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࡕࡨࡶࡻ࡯ࡣࡦࡵࡄࡹࡹ࡮࡯ࡳ࡫ࡽࡩࡩ࠭ረ"),
  bstack111l1ll_opy_ (u"ࠨࡣࡸࡸࡴࡇࡣࡤࡧࡳࡸࡆࡲࡥࡳࡶࡶࠫሩ"), bstack111l1ll_opy_ (u"ࠩࡤࡹࡹࡵࡄࡪࡵࡰ࡭ࡸࡹࡁ࡭ࡧࡵࡸࡸ࠭ሪ"),
  bstack111l1ll_opy_ (u"ࠪࡲࡦࡺࡩࡷࡧࡌࡲࡸࡺࡲࡶ࡯ࡨࡲࡹࡹࡌࡪࡤࠪራ"),
  bstack111l1ll_opy_ (u"ࠫࡳࡧࡴࡪࡸࡨ࡛ࡪࡨࡔࡢࡲࠪሬ"),
  bstack111l1ll_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࡎࡴࡩࡵ࡫ࡤࡰ࡚ࡸ࡬ࠨር"), bstack111l1ll_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮ࡇ࡬࡭ࡱࡺࡔࡴࡶࡵࡱࡵࠪሮ"), bstack111l1ll_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࡉࡨࡰࡲࡶࡪࡌࡲࡢࡷࡧ࡛ࡦࡸ࡮ࡪࡰࡪࠫሯ"), bstack111l1ll_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࡐࡲࡨࡲࡑ࡯࡮࡬ࡵࡌࡲࡇࡧࡣ࡬ࡩࡵࡳࡺࡴࡤࠨሰ"),
  bstack111l1ll_opy_ (u"ࠩ࡮ࡩࡪࡶࡋࡦࡻࡆ࡬ࡦ࡯࡮ࡴࠩሱ"),
  bstack111l1ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭࡫ࡽࡥࡧࡲࡥࡔࡶࡵ࡭ࡳ࡭ࡳࡅ࡫ࡵࠫሲ"),
  bstack111l1ll_opy_ (u"ࠫࡵࡸ࡯ࡤࡧࡶࡷࡆࡸࡧࡶ࡯ࡨࡲࡹࡹࠧሳ"),
  bstack111l1ll_opy_ (u"ࠬ࡯࡮ࡵࡧࡵࡏࡪࡿࡄࡦ࡮ࡤࡽࠬሴ"),
  bstack111l1ll_opy_ (u"࠭ࡳࡩࡱࡺࡍࡔ࡙ࡌࡰࡩࠪስ"),
  bstack111l1ll_opy_ (u"ࠧࡴࡧࡱࡨࡐ࡫ࡹࡔࡶࡵࡥࡹ࡫ࡧࡺࠩሶ"),
  bstack111l1ll_opy_ (u"ࠨࡹࡨࡦࡰ࡯ࡴࡓࡧࡶࡴࡴࡴࡳࡦࡖ࡬ࡱࡪࡵࡵࡵࠩሷ"), bstack111l1ll_opy_ (u"ࠩࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹ࡝ࡡࡪࡶࡗ࡭ࡲ࡫࡯ࡶࡶࠪሸ"),
  bstack111l1ll_opy_ (u"ࠪࡶࡪࡳ࡯ࡵࡧࡇࡩࡧࡻࡧࡑࡴࡲࡼࡾ࠭ሹ"),
  bstack111l1ll_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡅࡸࡿ࡮ࡤࡇࡻࡩࡨࡻࡴࡦࡈࡵࡳࡲࡎࡴࡵࡲࡶࠫሺ"),
  bstack111l1ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡏࡳ࡬ࡉࡡࡱࡶࡸࡶࡪ࠭ሻ"),
  bstack111l1ll_opy_ (u"࠭ࡷࡦࡤ࡮࡭ࡹࡊࡥࡣࡷࡪࡔࡷࡵࡸࡺࡒࡲࡶࡹ࠭ሼ"),
  bstack111l1ll_opy_ (u"ࠧࡧࡷ࡯ࡰࡈࡵ࡮ࡵࡧࡻࡸࡑ࡯ࡳࡵࠩሽ"),
  bstack111l1ll_opy_ (u"ࠨࡹࡤ࡭ࡹࡌ࡯ࡳࡃࡳࡴࡘࡩࡲࡪࡲࡷࠫሾ"),
  bstack111l1ll_opy_ (u"ࠩࡺࡩࡧࡼࡩࡦࡹࡆࡳࡳࡴࡥࡤࡶࡕࡩࡹࡸࡩࡦࡵࠪሿ"),
  bstack111l1ll_opy_ (u"ࠪࡥࡵࡶࡎࡢ࡯ࡨࠫቀ"),
  bstack111l1ll_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡗࡘࡒࡃࡦࡴࡷࠫቁ"),
  bstack111l1ll_opy_ (u"ࠬࡺࡡࡱ࡙࡬ࡸ࡭࡙ࡨࡰࡴࡷࡔࡷ࡫ࡳࡴࡆࡸࡶࡦࡺࡩࡰࡰࠪቂ"),
  bstack111l1ll_opy_ (u"࠭ࡳࡤࡣ࡯ࡩࡋࡧࡣࡵࡱࡵࠫቃ"),
  bstack111l1ll_opy_ (u"ࠧࡸࡦࡤࡐࡴࡩࡡ࡭ࡒࡲࡶࡹ࠭ቄ"),
  bstack111l1ll_opy_ (u"ࠨࡵ࡫ࡳࡼ࡞ࡣࡰࡦࡨࡐࡴ࡭ࠧቅ"),
  bstack111l1ll_opy_ (u"ࠩ࡬ࡳࡸࡏ࡮ࡴࡶࡤࡰࡱࡖࡡࡶࡵࡨࠫቆ"),
  bstack111l1ll_opy_ (u"ࠪࡼࡨࡵࡤࡦࡅࡲࡲ࡫࡯ࡧࡇ࡫࡯ࡩࠬቇ"),
  bstack111l1ll_opy_ (u"ࠫࡰ࡫ࡹࡤࡪࡤ࡭ࡳࡖࡡࡴࡵࡺࡳࡷࡪࠧቈ"),
  bstack111l1ll_opy_ (u"ࠬࡻࡳࡦࡒࡵࡩࡧࡻࡩ࡭ࡶ࡚ࡈࡆ࠭቉"),
  bstack111l1ll_opy_ (u"࠭ࡰࡳࡧࡹࡩࡳࡺࡗࡅࡃࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠧቊ"),
  bstack111l1ll_opy_ (u"ࠧࡸࡧࡥࡈࡷ࡯ࡶࡦࡴࡄ࡫ࡪࡴࡴࡖࡴ࡯ࠫቋ"),
  bstack111l1ll_opy_ (u"ࠨ࡭ࡨࡽࡨ࡮ࡡࡪࡰࡓࡥࡹ࡮ࠧቌ"),
  bstack111l1ll_opy_ (u"ࠩࡸࡷࡪࡔࡥࡸ࡙ࡇࡅࠬቍ"),
  bstack111l1ll_opy_ (u"ࠪࡻࡩࡧࡌࡢࡷࡱࡧ࡭࡚ࡩ࡮ࡧࡲࡹࡹ࠭቎"), bstack111l1ll_opy_ (u"ࠫࡼࡪࡡࡄࡱࡱࡲࡪࡩࡴࡪࡱࡱࡘ࡮ࡳࡥࡰࡷࡷࠫ቏"),
  bstack111l1ll_opy_ (u"ࠬࡾࡣࡰࡦࡨࡓࡷ࡭ࡉࡥࠩቐ"), bstack111l1ll_opy_ (u"࠭ࡸࡤࡱࡧࡩࡘ࡯ࡧ࡯࡫ࡱ࡫ࡎࡪࠧቑ"),
  bstack111l1ll_opy_ (u"ࠧࡶࡲࡧࡥࡹ࡫ࡤࡘࡆࡄࡆࡺࡴࡤ࡭ࡧࡌࡨࠬቒ"),
  bstack111l1ll_opy_ (u"ࠨࡴࡨࡷࡪࡺࡏ࡯ࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡷࡺࡏ࡯࡮ࡼࠫቓ"),
  bstack111l1ll_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡗ࡭ࡲ࡫࡯ࡶࡶࡶࠫቔ"),
  bstack111l1ll_opy_ (u"ࠪࡻࡩࡧࡓࡵࡣࡵࡸࡺࡶࡒࡦࡶࡵ࡭ࡪࡹࠧቕ"), bstack111l1ll_opy_ (u"ࠫࡼࡪࡡࡔࡶࡤࡶࡹࡻࡰࡓࡧࡷࡶࡾࡏ࡮ࡵࡧࡵࡺࡦࡲࠧቖ"),
  bstack111l1ll_opy_ (u"ࠬࡩ࡯࡯ࡰࡨࡧࡹࡎࡡࡳࡦࡺࡥࡷ࡫ࡋࡦࡻࡥࡳࡦࡸࡤࠨ቗"),
  bstack111l1ll_opy_ (u"࠭࡭ࡢࡺࡗࡽࡵ࡯࡮ࡨࡈࡵࡩࡶࡻࡥ࡯ࡥࡼࠫቘ"),
  bstack111l1ll_opy_ (u"ࠧࡴ࡫ࡰࡴࡱ࡫ࡉࡴࡘ࡬ࡷ࡮ࡨ࡬ࡦࡅ࡫ࡩࡨࡱࠧ቙"),
  bstack111l1ll_opy_ (u"ࠨࡷࡶࡩࡈࡧࡲࡵࡪࡤ࡫ࡪ࡙ࡳ࡭ࠩቚ"),
  bstack111l1ll_opy_ (u"ࠩࡶ࡬ࡴࡻ࡬ࡥࡗࡶࡩࡘ࡯࡮ࡨ࡮ࡨࡸࡴࡴࡔࡦࡵࡷࡑࡦࡴࡡࡨࡧࡵࠫቛ"),
  bstack111l1ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡋ࡚ࡈࡕ࠭ቜ"),
  bstack111l1ll_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡗࡳࡺࡩࡨࡊࡦࡈࡲࡷࡵ࡬࡭ࠩቝ"),
  bstack111l1ll_opy_ (u"ࠬ࡯ࡧ࡯ࡱࡵࡩࡍ࡯ࡤࡥࡧࡱࡅࡵ࡯ࡐࡰ࡮࡬ࡧࡾࡋࡲࡳࡱࡵࠫ቞"),
  bstack111l1ll_opy_ (u"࠭࡭ࡰࡥ࡮ࡐࡴࡩࡡࡵ࡫ࡲࡲࡆࡶࡰࠨ቟"),
  bstack111l1ll_opy_ (u"ࠧ࡭ࡱࡪࡧࡦࡺࡆࡰࡴࡰࡥࡹ࠭በ"), bstack111l1ll_opy_ (u"ࠨ࡮ࡲ࡫ࡨࡧࡴࡇ࡫࡯ࡸࡪࡸࡓࡱࡧࡦࡷࠬቡ"),
  bstack111l1ll_opy_ (u"ࠩࡤࡰࡱࡵࡷࡅࡧ࡯ࡥࡾࡇࡤࡣࠩቢ"),
  bstack111l1ll_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡍࡩࡒ࡯ࡤࡣࡷࡳࡷࡇࡵࡵࡱࡦࡳࡲࡶ࡬ࡦࡶ࡬ࡳࡳ࠭ባ")
]
bstack1l1111l11l_opy_ = bstack111l1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠯ࡦࡰࡴࡻࡤ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡹࡵࡲ࡯ࡢࡦࠪቤ")
bstack111l1l11l_opy_ = [bstack111l1ll_opy_ (u"ࠬ࠴ࡡࡱ࡭ࠪብ"), bstack111l1ll_opy_ (u"࠭࠮ࡢࡣࡥࠫቦ"), bstack111l1ll_opy_ (u"ࠧ࠯࡫ࡳࡥࠬቧ")]
bstack1111111l1_opy_ = [bstack111l1ll_opy_ (u"ࠨ࡫ࡧࠫቨ"), bstack111l1ll_opy_ (u"ࠩࡳࡥࡹ࡮ࠧቩ"), bstack111l1ll_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭ቪ"), bstack111l1ll_opy_ (u"ࠫࡸ࡮ࡡࡳࡧࡤࡦࡱ࡫࡟ࡪࡦࠪቫ")]
bstack1ll1l111l_opy_ = {
  bstack111l1ll_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬቬ"): bstack111l1ll_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫቭ"),
  bstack111l1ll_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨቮ"): bstack111l1ll_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ቯ"),
  bstack111l1ll_opy_ (u"ࠩࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧተ"): bstack111l1ll_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫቱ"),
  bstack111l1ll_opy_ (u"ࠫ࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧቲ"): bstack111l1ll_opy_ (u"ࠬࡹࡥ࠻࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫታ"),
  bstack111l1ll_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮ࡕࡰࡵ࡫ࡲࡲࡸ࠭ቴ"): bstack111l1ll_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨት")
}
bstack1l1ll1llll_opy_ = [
  bstack111l1ll_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ቶ"),
  bstack111l1ll_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧቷ"),
  bstack111l1ll_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫቸ"),
  bstack111l1ll_opy_ (u"ࠫࡸ࡫࠺ࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪቹ"),
  bstack111l1ll_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭ቺ"),
]
bstack11lll111l1_opy_ = bstack111l11ll1_opy_ + bstack111l11l111_opy_ + bstack111lllll1l_opy_
bstack1ll111l1l1_opy_ = [
  bstack111l1ll_opy_ (u"࠭࡞࡭ࡱࡦࡥࡱ࡮࡯ࡴࡶࠧࠫቻ"),
  bstack111l1ll_opy_ (u"ࠧ࡟ࡤࡶ࠱ࡱࡵࡣࡢ࡮࠱ࡧࡴࡳࠤࠨቼ"),
  bstack111l1ll_opy_ (u"ࠨࡠ࠴࠶࠼࠴ࠧች"),
  bstack111l1ll_opy_ (u"ࠩࡡ࠵࠵࠴ࠧቾ"),
  bstack111l1ll_opy_ (u"ࠪࡢ࠶࠽࠲࠯࠳࡞࠺࠲࠿࡝࠯ࠩቿ"),
  bstack111l1ll_opy_ (u"ࠫࡣ࠷࠷࠳࠰࠵࡟࠵࠳࠹࡞࠰ࠪኀ"),
  bstack111l1ll_opy_ (u"ࠬࡤ࠱࠸࠴࠱࠷ࡠ࠶࠭࠲࡟࠱ࠫኁ"),
  bstack111l1ll_opy_ (u"࠭࡞࠲࠻࠵࠲࠶࠼࠸࠯ࠩኂ")
]
bstack111l111ll1_opy_ = bstack111l1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨኃ")
bstack1l1lll1l11_opy_ = bstack111l1ll_opy_ (u"ࠨࡵࡧ࡯࠴ࡼ࠱࠰ࡧࡹࡩࡳࡺࠧኄ")
bstack1lll1lll11_opy_ = [ bstack111l1ll_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫኅ") ]
bstack11l111ll11_opy_ = [ bstack111l1ll_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩኆ") ]
bstack1lll111ll1_opy_ = [bstack111l1ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨኇ")]
bstack11l1ll1111_opy_ = [ bstack111l1ll_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬኈ") ]
bstack1l1llll1ll_opy_ = bstack111l1ll_opy_ (u"࠭ࡓࡅࡍࡖࡩࡹࡻࡰࠨ኉")
bstack1ll1l1ll1l_opy_ = bstack111l1ll_opy_ (u"ࠧࡔࡆࡎࡘࡪࡹࡴࡂࡶࡷࡩࡲࡶࡴࡦࡦࠪኊ")
bstack11ll1l1ll_opy_ = bstack111l1ll_opy_ (u"ࠨࡕࡇࡏ࡙࡫ࡳࡵࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠬኋ")
bstack1l1ll11ll1_opy_ = bstack111l1ll_opy_ (u"ࠩ࠷࠲࠵࠴࠰ࠨኌ")
bstack11l1111ll1_opy_ = [
  bstack111l1ll_opy_ (u"ࠪࡉࡗࡘ࡟ࡇࡃࡌࡐࡊࡊࠧኍ"),
  bstack111l1ll_opy_ (u"ࠫࡊࡘࡒࡠࡖࡌࡑࡊࡊ࡟ࡐࡗࡗࠫ኎"),
  bstack111l1ll_opy_ (u"ࠬࡋࡒࡓࡡࡅࡐࡔࡉࡋࡆࡆࡢࡆ࡞ࡥࡃࡍࡋࡈࡒ࡙࠭኏"),
  bstack111l1ll_opy_ (u"࠭ࡅࡓࡔࡢࡒࡊ࡚ࡗࡐࡔࡎࡣࡈࡎࡁࡏࡉࡈࡈࠬነ"),
  bstack111l1ll_opy_ (u"ࠧࡆࡔࡕࡣࡘࡕࡃࡌࡇࡗࡣࡓࡕࡔࡠࡅࡒࡒࡓࡋࡃࡕࡇࡇࠫኑ"),
  bstack111l1ll_opy_ (u"ࠨࡇࡕࡖࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡆࡐࡔ࡙ࡅࡅࠩኒ"),
  bstack111l1ll_opy_ (u"ࠩࡈࡖࡗࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡖࡊ࡙ࡅࡕࠩና"),
  bstack111l1ll_opy_ (u"ࠪࡉࡗࡘ࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡗࡋࡆࡖࡕࡈࡈࠬኔ"),
  bstack111l1ll_opy_ (u"ࠫࡊࡘࡒࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡇࡂࡐࡔࡗࡉࡉ࠭ን"),
  bstack111l1ll_opy_ (u"ࠬࡋࡒࡓࡡࡆࡓࡓࡔࡅࡄࡖࡌࡓࡓࡥࡆࡂࡋࡏࡉࡉ࠭ኖ"),
  bstack111l1ll_opy_ (u"࠭ࡅࡓࡔࡢࡒࡆࡓࡅࡠࡐࡒࡘࡤࡘࡅࡔࡑࡏ࡚ࡊࡊࠧኗ"),
  bstack111l1ll_opy_ (u"ࠧࡆࡔࡕࡣࡆࡊࡄࡓࡇࡖࡗࡤࡏࡎࡗࡃࡏࡍࡉ࠭ኘ"),
  bstack111l1ll_opy_ (u"ࠨࡇࡕࡖࡤࡇࡄࡅࡔࡈࡗࡘࡥࡕࡏࡔࡈࡅࡈࡎࡁࡃࡎࡈࠫኙ"),
  bstack111l1ll_opy_ (u"ࠩࡈࡖࡗࡥࡔࡖࡐࡑࡉࡑࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡊࡆࡏࡌࡆࡆࠪኚ"),
  bstack111l1ll_opy_ (u"ࠪࡉࡗࡘ࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣ࡙ࡏࡍࡆࡆࡢࡓ࡚࡚ࠧኛ"),
  bstack111l1ll_opy_ (u"ࠫࡊࡘࡒࡠࡕࡒࡇࡐ࡙࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡋࡇࡉࡍࡇࡇࠫኜ"),
  bstack111l1ll_opy_ (u"ࠬࡋࡒࡓࡡࡖࡓࡈࡑࡓࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡎࡏࡔࡖࡢ࡙ࡓࡘࡅࡂࡅࡋࡅࡇࡒࡅࠨኝ"),
  bstack111l1ll_opy_ (u"࠭ࡅࡓࡔࡢࡔࡗࡕࡘ࡚ࡡࡆࡓࡓࡔࡅࡄࡖࡌࡓࡓࡥࡆࡂࡋࡏࡉࡉ࠭ኞ"),
  bstack111l1ll_opy_ (u"ࠧࡆࡔࡕࡣࡓࡇࡍࡆࡡࡑࡓ࡙ࡥࡒࡆࡕࡒࡐ࡛ࡋࡄࠨኟ"),
  bstack111l1ll_opy_ (u"ࠨࡇࡕࡖࡤࡔࡁࡎࡇࡢࡖࡊ࡙ࡏࡍࡗࡗࡍࡔࡔ࡟ࡇࡃࡌࡐࡊࡊࠧአ"),
  bstack111l1ll_opy_ (u"ࠩࡈࡖࡗࡥࡍࡂࡐࡇࡅ࡙ࡕࡒ࡚ࡡࡓࡖࡔ࡞࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠࡈࡄࡍࡑࡋࡄࠨኡ"),
]
bstack1l11lll11l_opy_ = bstack111l1ll_opy_ (u"ࠪ࠲࠴ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡦࡸࡴࡪࡨࡤࡧࡹࡹ࠯ࠨኢ")
bstack11l111l11_opy_ = os.path.join(os.path.expanduser(bstack111l1ll_opy_ (u"ࠫࢃ࠭ኣ")), bstack111l1ll_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬኤ"), bstack111l1ll_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬእ"))
bstack111llll1l1_opy_ = bstack111l1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡦࡶࡩࠨኦ")
bstack111l111l11_opy_ = [ bstack111l1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨኧ"), bstack111l1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨከ"), bstack111l1ll_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩኩ"), bstack111l1ll_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫኪ")]
bstack1l1lllllll_opy_ = [ bstack111l1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬካ"), bstack111l1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬኬ"), bstack111l1ll_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ክ"), bstack111l1ll_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨኮ") ]
bstack11lll111_opy_ = {
  bstack111l1ll_opy_ (u"ࠩࡓࡅࡘ࡙ࠧኯ"): bstack111l1ll_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪኰ"),
  bstack111l1ll_opy_ (u"ࠫࡋࡇࡉࡍࠩ኱"): bstack111l1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬኲ"),
  bstack111l1ll_opy_ (u"࠭ࡓࡌࡋࡓࠫኳ"): bstack111l1ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨኴ")
}
bstack1l1l1ll111_opy_ = [
  bstack111l1ll_opy_ (u"ࠣࡩࡨࡸࠧኵ"),
  bstack111l1ll_opy_ (u"ࠤࡪࡳࡇࡧࡣ࡬ࠤ኶"),
  bstack111l1ll_opy_ (u"ࠥ࡫ࡴࡌ࡯ࡳࡹࡤࡶࡩࠨ኷"),
  bstack111l1ll_opy_ (u"ࠦࡷ࡫ࡦࡳࡧࡶ࡬ࠧኸ"),
  bstack111l1ll_opy_ (u"ࠧࡩ࡬ࡪࡥ࡮ࡉࡱ࡫࡭ࡦࡰࡷࠦኹ"),
  bstack111l1ll_opy_ (u"ࠨࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠥኺ"),
  bstack111l1ll_opy_ (u"ࠢࡴࡷࡥࡱ࡮ࡺࡅ࡭ࡧࡰࡩࡳࡺࠢኻ"),
  bstack111l1ll_opy_ (u"ࠣࡵࡨࡲࡩࡑࡥࡺࡵࡗࡳࡊࡲࡥ࡮ࡧࡱࡸࠧኼ"),
  bstack111l1ll_opy_ (u"ࠤࡶࡩࡳࡪࡋࡦࡻࡶࡘࡴࡇࡣࡵ࡫ࡹࡩࡊࡲࡥ࡮ࡧࡱࡸࠧኽ"),
  bstack111l1ll_opy_ (u"ࠥࡧࡱ࡫ࡡࡳࡇ࡯ࡩࡲ࡫࡮ࡵࠤኾ"),
  bstack111l1ll_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࡷࠧ኿"),
  bstack111l1ll_opy_ (u"ࠧ࡫ࡸࡦࡥࡸࡸࡪ࡙ࡣࡳ࡫ࡳࡸࠧዀ"),
  bstack111l1ll_opy_ (u"ࠨࡥࡹࡧࡦࡹࡹ࡫ࡁࡴࡻࡱࡧࡘࡩࡲࡪࡲࡷࠦ዁"),
  bstack111l1ll_opy_ (u"ࠢࡤ࡮ࡲࡷࡪࠨዂ"),
  bstack111l1ll_opy_ (u"ࠣࡳࡸ࡭ࡹࠨዃ"),
  bstack111l1ll_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡗࡳࡺࡩࡨࡂࡥࡷ࡭ࡴࡴࠢዄ"),
  bstack111l1ll_opy_ (u"ࠥࡴࡪࡸࡦࡰࡴࡰࡑࡺࡲࡴࡪࡖࡲࡹࡨ࡮ࠢዅ"),
  bstack111l1ll_opy_ (u"ࠦࡸ࡮ࡡ࡬ࡧࠥ዆"),
  bstack111l1ll_opy_ (u"ࠧࡩ࡬ࡰࡵࡨࡅࡵࡶࠢ዇")
]
bstack111l111111_opy_ = [
  bstack111l1ll_opy_ (u"ࠨࡣ࡭࡫ࡦ࡯ࠧወ"),
  bstack111l1ll_opy_ (u"ࠢࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠦዉ"),
  bstack111l1ll_opy_ (u"ࠣࡣࡸࡸࡴࠨዊ"),
  bstack111l1ll_opy_ (u"ࠤࡰࡥࡳࡻࡡ࡭ࠤዋ"),
  bstack111l1ll_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧዌ")
]
bstack1111ll1ll_opy_ = {
  bstack111l1ll_opy_ (u"ࠦࡨࡲࡩࡤ࡭ࠥው"): [bstack111l1ll_opy_ (u"ࠧࡩ࡬ࡪࡥ࡮ࡉࡱ࡫࡭ࡦࡰࡷࠦዎ")],
  bstack111l1ll_opy_ (u"ࠨࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠥዏ"): [bstack111l1ll_opy_ (u"ࠢࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠦዐ")],
  bstack111l1ll_opy_ (u"ࠣࡣࡸࡸࡴࠨዑ"): [bstack111l1ll_opy_ (u"ࠤࡶࡩࡳࡪࡋࡦࡻࡶࡘࡴࡋ࡬ࡦ࡯ࡨࡲࡹࠨዒ"), bstack111l1ll_opy_ (u"ࠥࡷࡪࡴࡤࡌࡧࡼࡷ࡙ࡵࡁࡤࡶ࡬ࡺࡪࡋ࡬ࡦ࡯ࡨࡲࡹࠨዓ"), bstack111l1ll_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣዔ"), bstack111l1ll_opy_ (u"ࠧࡩ࡬ࡪࡥ࡮ࡉࡱ࡫࡭ࡦࡰࡷࠦዕ")],
  bstack111l1ll_opy_ (u"ࠨ࡭ࡢࡰࡸࡥࡱࠨዖ"): [bstack111l1ll_opy_ (u"ࠢ࡮ࡣࡱࡹࡦࡲࠢ዗")],
  bstack111l1ll_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥዘ"): [bstack111l1ll_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦዙ")],
}
bstack111l1111ll_opy_ = {
  bstack111l1ll_opy_ (u"ࠥࡧࡱ࡯ࡣ࡬ࡇ࡯ࡩࡲ࡫࡮ࡵࠤዚ"): bstack111l1ll_opy_ (u"ࠦࡨࡲࡩࡤ࡭ࠥዛ"),
  bstack111l1ll_opy_ (u"ࠧࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤዜ"): bstack111l1ll_opy_ (u"ࠨࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠥዝ"),
  bstack111l1ll_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࡖࡲࡉࡱ࡫࡭ࡦࡰࡷࠦዞ"): bstack111l1ll_opy_ (u"ࠣࡵࡨࡲࡩࡑࡥࡺࡵࠥዟ"),
  bstack111l1ll_opy_ (u"ࠤࡶࡩࡳࡪࡋࡦࡻࡶࡘࡴࡇࡣࡵ࡫ࡹࡩࡊࡲࡥ࡮ࡧࡱࡸࠧዠ"): bstack111l1ll_opy_ (u"ࠥࡷࡪࡴࡤࡌࡧࡼࡷࠧዡ"),
  bstack111l1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡥࡤࡷࡪࠨዢ"): bstack111l1ll_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢዣ")
}
bstack11l1lll1_opy_ = {
  bstack111l1ll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡁࡍࡎࠪዤ"): bstack111l1ll_opy_ (u"ࠧࡔࡷ࡬ࡸࡪࠦࡓࡦࡶࡸࡴࠬዥ"),
  bstack111l1ll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫዦ"): bstack111l1ll_opy_ (u"ࠩࡖࡹ࡮ࡺࡥࠡࡖࡨࡥࡷࡪ࡯ࡸࡰࠪዧ"),
  bstack111l1ll_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨየ"): bstack111l1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࠢࡖࡩࡹࡻࡰࠨዩ"),
  bstack111l1ll_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩዪ"): bstack111l1ll_opy_ (u"࠭ࡔࡦࡵࡷࠤ࡙࡫ࡡࡳࡦࡲࡻࡳ࠭ያ")
}
bstack111l11111l_opy_ = 65536
bstack111l111lll_opy_ = bstack111l1ll_opy_ (u"ࠧ࠯࠰࠱࡟࡙ࡘࡕࡏࡅࡄࡘࡊࡊ࡝ࠨዬ")
bstack111l111l1l_opy_ = [
      bstack111l1ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪይ"), bstack111l1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬዮ"), bstack111l1ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ዯ"), bstack111l1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨደ"), bstack111l1ll_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱ࡛ࡧࡲࡪࡣࡥࡰࡪࡹࠧዱ"),
      bstack111l1ll_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡚ࡹࡥࡳࠩዲ"), bstack111l1ll_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖࡡࡴࡵࠪዳ"), bstack111l1ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡐࡳࡱࡻࡽ࡚ࡹࡥࡳࠩዴ"), bstack111l1ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾࡖࡡࡴࡵࠪድ"),
      bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪࡸࡎࡢ࡯ࡨࠫዶ"), bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ዷ"), bstack111l1ll_opy_ (u"ࠬࡧࡵࡵࡪࡗࡳࡰ࡫࡮ࠨዸ")
    ]
bstack111l11l11l_opy_= {
  bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪዹ"): bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫዺ"),
  bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬዻ"): bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ዼ"),
  bstack111l1ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩዽ"): bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨዾ"),
  bstack111l1ll_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬዿ"): bstack111l1ll_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ጀ"),
  bstack111l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪጁ"): bstack111l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫጂ"),
  bstack111l1ll_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫጃ"): bstack111l1ll_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬጄ"),
  bstack111l1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧጅ"): bstack111l1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨጆ"),
  bstack111l1ll_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪጇ"): bstack111l1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫገ"),
  bstack111l1ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫጉ"): bstack111l1ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬጊ"),
  bstack111l1ll_opy_ (u"ࠪࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠨጋ"): bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠩጌ"),
  bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩግ"): bstack111l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪጎ"),
  bstack111l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫጏ"): bstack111l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬጐ"),
  bstack111l1ll_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠫ጑"): bstack111l1ll_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠬጒ"),
  bstack111l1ll_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨጓ"): bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧጔ"),
  bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨጕ"): bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩ጖"),
  bstack111l1ll_opy_ (u"ࠨࡴࡨࡶࡺࡴࡔࡦࡵࡷࡷࠬ጗"): bstack111l1ll_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡕࡧࡶࡸࡸ࠭ጘ"),
  bstack111l1ll_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩጙ"): bstack111l1ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪጚ"),
  bstack111l1ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࡓࡵࡺࡩࡰࡰࡶࠫጛ"): bstack111l1ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࡔࡶࡴࡪࡱࡱࡷࠬጜ"),
  bstack111l1ll_opy_ (u"ࠧࡱࡧࡵࡧࡾࡉࡡࡱࡶࡸࡶࡪࡓ࡯ࡥࡧࠪጝ"): bstack111l1ll_opy_ (u"ࠨࡲࡨࡶࡨࡿࡃࡢࡲࡷࡹࡷ࡫ࡍࡰࡦࡨࠫጞ"),
  bstack111l1ll_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫጟ"): bstack111l1ll_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬጠ"),
  bstack111l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫጡ"): bstack111l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬጢ"),
  bstack111l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ጣ"): bstack111l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧጤ"),
  bstack111l1ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬጥ"): bstack111l1ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ጦ"),
  bstack111l1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧጧ"): bstack111l1ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࡐࡲࡷ࡭ࡴࡴࡳࠨጨ"),
  bstack111l1ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠬጩ"): bstack111l1ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭ጪ")
}
bstack1111lllll1_opy_ = [bstack111l1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧጫ"), bstack111l1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧጬ")]
bstack1lll111l11_opy_ = bstack111l1ll_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠲ࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦ࠱ࡹ࠵࠴࡭ࡲࡪࡦࡶ࠳ࠧጭ")
bstack11l11l1ll_opy_ = bstack111l1ll_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳࡬ࡸࡩࡥ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡪࡡࡴࡪࡥࡳࡦࡸࡤ࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࠤጮ")
bstack1l11ll1ll_opy_ = bstack111l1ll_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡧࡵࡵࡱࡰࡥࡹ࡫࠭ࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨ࠳ࡻ࠷࠯ࡣࡷ࡬ࡰࡩࡹ࠮࡫ࡵࡲࡲࠧጯ")