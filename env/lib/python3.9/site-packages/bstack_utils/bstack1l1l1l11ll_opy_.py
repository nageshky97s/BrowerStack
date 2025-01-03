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
import os
import threading
from bstack_utils.config import Config
from bstack_utils.helper import bstack111111l111_opy_, bstack1l1l1l1ll1_opy_, bstack1ll111l1_opy_, bstack1l1l11111_opy_, \
    bstack1111l1lll1_opy_
def bstack11lll1ll1_opy_(bstack1ll1l1ll1l1_opy_):
    for driver in bstack1ll1l1ll1l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack11ll111l1l_opy_(driver, status, reason=bstack111l1ll_opy_ (u"ࠫࠬᙷ")):
    bstack1111lll1_opy_ = Config.bstack11111lll_opy_()
    if bstack1111lll1_opy_.bstack111ll111_opy_():
        return
    bstack1l1l1ll11_opy_ = bstack1l11ll1ll1_opy_(bstack111l1ll_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᙸ"), bstack111l1ll_opy_ (u"࠭ࠧᙹ"), status, reason, bstack111l1ll_opy_ (u"ࠧࠨᙺ"), bstack111l1ll_opy_ (u"ࠨࠩᙻ"))
    driver.execute_script(bstack1l1l1ll11_opy_)
def bstack1l1l1lll1l_opy_(page, status, reason=bstack111l1ll_opy_ (u"ࠩࠪᙼ")):
    try:
        if page is None:
            return
        bstack1111lll1_opy_ = Config.bstack11111lll_opy_()
        if bstack1111lll1_opy_.bstack111ll111_opy_():
            return
        bstack1l1l1ll11_opy_ = bstack1l11ll1ll1_opy_(bstack111l1ll_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ᙽ"), bstack111l1ll_opy_ (u"ࠫࠬᙾ"), status, reason, bstack111l1ll_opy_ (u"ࠬ࠭ᙿ"), bstack111l1ll_opy_ (u"࠭ࠧ "))
        page.evaluate(bstack111l1ll_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣᚁ"), bstack1l1l1ll11_opy_)
    except Exception as e:
        print(bstack111l1ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡿࢂࠨᚂ"), e)
def bstack1l11ll1ll1_opy_(type, name, status, reason, bstack1l1l1l11l_opy_, bstack1l11lll1ll_opy_):
    bstack1ll1111lll_opy_ = {
        bstack111l1ll_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩᚃ"): type,
        bstack111l1ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᚄ"): {}
    }
    if type == bstack111l1ll_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ᚅ"):
        bstack1ll1111lll_opy_[bstack111l1ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᚆ")][bstack111l1ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᚇ")] = bstack1l1l1l11l_opy_
        bstack1ll1111lll_opy_[bstack111l1ll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᚈ")][bstack111l1ll_opy_ (u"ࠨࡦࡤࡸࡦ࠭ᚉ")] = json.dumps(str(bstack1l11lll1ll_opy_))
    if type == bstack111l1ll_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᚊ"):
        bstack1ll1111lll_opy_[bstack111l1ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᚋ")][bstack111l1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᚌ")] = name
    if type == bstack111l1ll_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᚍ"):
        bstack1ll1111lll_opy_[bstack111l1ll_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᚎ")][bstack111l1ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᚏ")] = status
        if status == bstack111l1ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᚐ") and str(reason) != bstack111l1ll_opy_ (u"ࠤࠥᚑ"):
            bstack1ll1111lll_opy_[bstack111l1ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᚒ")][bstack111l1ll_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᚓ")] = json.dumps(str(reason))
    bstack1l1ll1ll1_opy_ = bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪᚔ").format(json.dumps(bstack1ll1111lll_opy_))
    return bstack1l1ll1ll1_opy_
def bstack1l1ll1l111_opy_(url, config, logger, bstack11l11111l_opy_=False):
    hostname = bstack1l1l1l1ll1_opy_(url)
    is_private = bstack1l1l11111_opy_(hostname)
    try:
        if is_private or bstack11l11111l_opy_:
            file_path = bstack111111l111_opy_(bstack111l1ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᚕ"), bstack111l1ll_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ᚖ"), logger)
            if os.environ.get(bstack111l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭ᚗ")) and eval(
                    os.environ.get(bstack111l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧᚘ"))):
                return
            if (bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᚙ") in config and not config[bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨᚚ")]):
                os.environ[bstack111l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪ᚛")] = str(True)
                bstack1ll1l1ll111_opy_ = {bstack111l1ll_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨ᚜"): hostname}
                bstack1111l1lll1_opy_(bstack111l1ll_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭᚝"), bstack111l1ll_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭᚞"), bstack1ll1l1ll111_opy_, logger)
    except Exception as e:
        pass
def bstack1ll1lll1l_opy_(caps, bstack1ll1l1l1lll_opy_):
    if bstack111l1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ᚟") in caps:
        caps[bstack111l1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᚠ")][bstack111l1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪᚡ")] = True
        if bstack1ll1l1l1lll_opy_:
            caps[bstack111l1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᚢ")][bstack111l1ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᚣ")] = bstack1ll1l1l1lll_opy_
    else:
        caps[bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬᚤ")] = True
        if bstack1ll1l1l1lll_opy_:
            caps[bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᚥ")] = bstack1ll1l1l1lll_opy_
def bstack1ll1lll1l1l_opy_(bstack11ll1111_opy_):
    bstack1ll1l1ll11l_opy_ = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭ᚦ"), bstack111l1ll_opy_ (u"ࠪࠫᚧ"))
    if bstack1ll1l1ll11l_opy_ == bstack111l1ll_opy_ (u"ࠫࠬᚨ") or bstack1ll1l1ll11l_opy_ == bstack111l1ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᚩ"):
        threading.current_thread().testStatus = bstack11ll1111_opy_
    else:
        if bstack11ll1111_opy_ == bstack111l1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᚪ"):
            threading.current_thread().testStatus = bstack11ll1111_opy_