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
import re
from bstack_utils.bstack1l1l1l11ll_opy_ import bstack1ll1lll1l1l_opy_
def bstack1ll1lll11ll_opy_(fixture_name):
    if fixture_name.startswith(bstack111l1ll_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᙂ")):
        return bstack111l1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᙃ")
    elif fixture_name.startswith(bstack111l1ll_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᙄ")):
        return bstack111l1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩᙅ")
    elif fixture_name.startswith(bstack111l1ll_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᙆ")):
        return bstack111l1ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᙇ")
    elif fixture_name.startswith(bstack111l1ll_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᙈ")):
        return bstack111l1ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩᙉ")
def bstack1ll1lll11l1_opy_(fixture_name):
    return bool(re.match(bstack111l1ll_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤ࠮ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡽ࡯ࡲࡨࡺࡲࡥࠪࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᙊ"), fixture_name))
def bstack1ll1lll1l11_opy_(fixture_name):
    return bool(re.match(bstack111l1ll_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪᙋ"), fixture_name))
def bstack1ll1lll111l_opy_(fixture_name):
    return bool(re.match(bstack111l1ll_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪᙌ"), fixture_name))
def bstack1ll1ll1l1ll_opy_(fixture_name):
    if fixture_name.startswith(bstack111l1ll_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᙍ")):
        return bstack111l1ll_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᙎ"), bstack111l1ll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫᙏ")
    elif fixture_name.startswith(bstack111l1ll_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᙐ")):
        return bstack111l1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭࡮ࡱࡧࡹࡱ࡫ࠧᙑ"), bstack111l1ll_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ᙒ")
    elif fixture_name.startswith(bstack111l1ll_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᙓ")):
        return bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᙔ"), bstack111l1ll_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩᙕ")
    elif fixture_name.startswith(bstack111l1ll_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᙖ")):
        return bstack111l1ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩᙗ"), bstack111l1ll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫᙘ")
    return None, None
def bstack1ll1lll1111_opy_(hook_name):
    if hook_name in [bstack111l1ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨᙙ"), bstack111l1ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬᙚ")]:
        return hook_name.capitalize()
    return hook_name
def bstack1ll1ll1lll1_opy_(hook_name):
    if hook_name in [bstack111l1ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᙛ"), bstack111l1ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫᙜ")]:
        return bstack111l1ll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫᙝ")
    elif hook_name in [bstack111l1ll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭ᙞ"), bstack111l1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭ᙟ")]:
        return bstack111l1ll_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ᙠ")
    elif hook_name in [bstack111l1ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᙡ"), bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᙢ")]:
        return bstack111l1ll_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩᙣ")
    elif hook_name in [bstack111l1ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨᙤ"), bstack111l1ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨᙥ")]:
        return bstack111l1ll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫᙦ")
    return hook_name
def bstack1ll1ll1llll_opy_(node, scenario):
    if hasattr(node, bstack111l1ll_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫᙧ")):
        parts = node.nodeid.rsplit(bstack111l1ll_opy_ (u"ࠥ࡟ࠧᙨ"))
        params = parts[-1]
        return bstack111l1ll_opy_ (u"ࠦࢀࢃࠠ࡜ࡽࢀࠦᙩ").format(scenario.name, params)
    return scenario.name
def bstack1ll1ll1ll1l_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack111l1ll_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧᙪ")):
            examples = list(node.callspec.params[bstack111l1ll_opy_ (u"࠭࡟ࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡪࡾࡡ࡮ࡲ࡯ࡩࠬᙫ")].values())
        return examples
    except:
        return []
def bstack1ll1llll111_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack1ll1lll1lll_opy_(report):
    try:
        status = bstack111l1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᙬ")
        if report.passed or (report.failed and hasattr(report, bstack111l1ll_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥ᙭"))):
            status = bstack111l1ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ᙮")
        elif report.skipped:
            status = bstack111l1ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᙯ")
        bstack1ll1lll1l1l_opy_(status)
    except:
        pass
def bstack11l1ll1ll_opy_(status):
    try:
        bstack1ll1ll1ll11_opy_ = bstack111l1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᙰ")
        if status == bstack111l1ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᙱ"):
            bstack1ll1ll1ll11_opy_ = bstack111l1ll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᙲ")
        elif status == bstack111l1ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᙳ"):
            bstack1ll1ll1ll11_opy_ = bstack111l1ll_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᙴ")
        bstack1ll1lll1l1l_opy_(bstack1ll1ll1ll11_opy_)
    except:
        pass
def bstack1ll1lll1ll1_opy_(item=None, report=None, summary=None, extra=None):
    return