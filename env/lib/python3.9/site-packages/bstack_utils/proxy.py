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
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack1llll1111ll_opy_
bstack1111lll1_opy_ = Config.bstack11111lll_opy_()
def bstack1ll1llll1ll_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack1ll1llll1l1_opy_(bstack1ll1lllll11_opy_, bstack1ll1lllll1l_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack1ll1lllll11_opy_):
        with open(bstack1ll1lllll11_opy_) as f:
            pac = PACFile(f.read())
    elif bstack1ll1llll1ll_opy_(bstack1ll1lllll11_opy_):
        pac = get_pac(url=bstack1ll1lllll11_opy_)
    else:
        raise Exception(bstack111l1ll_opy_ (u"ࠫࡕࡧࡣࠡࡨ࡬ࡰࡪࠦࡤࡰࡧࡶࠤࡳࡵࡴࠡࡧࡻ࡭ࡸࡺ࠺ࠡࡽࢀࠫᘜ").format(bstack1ll1lllll11_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack111l1ll_opy_ (u"ࠧ࠾࠮࠹࠰࠻࠲࠽ࠨᘝ"), 80))
        bstack1ll1llll11l_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack1ll1llll11l_opy_ = bstack111l1ll_opy_ (u"࠭࠰࠯࠲࠱࠴࠳࠶ࠧᘞ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack1ll1lllll1l_opy_, bstack1ll1llll11l_opy_)
    return proxy_url
def bstack1l1l11ll11_opy_(config):
    return bstack111l1ll_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᘟ") in config or bstack111l1ll_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬᘠ") in config
def bstack111111ll1_opy_(config):
    if not bstack1l1l11ll11_opy_(config):
        return
    if config.get(bstack111l1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᘡ")):
        return config.get(bstack111l1ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ᘢ"))
    if config.get(bstack111l1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᘣ")):
        return config.get(bstack111l1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᘤ"))
def bstack1l1l1l1ll_opy_(config, bstack1ll1lllll1l_opy_):
    proxy = bstack111111ll1_opy_(config)
    proxies = {}
    if config.get(bstack111l1ll_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᘥ")) or config.get(bstack111l1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᘦ")):
        if proxy.endswith(bstack111l1ll_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭ᘧ")):
            proxies = bstack11111l1ll_opy_(proxy, bstack1ll1lllll1l_opy_)
        else:
            proxies = {
                bstack111l1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᘨ"): proxy
            }
    bstack1111lll1_opy_.bstack11llll1ll1_opy_(bstack111l1ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵࠪᘩ"), proxies)
    return proxies
def bstack11111l1ll_opy_(bstack1ll1lllll11_opy_, bstack1ll1lllll1l_opy_):
    proxies = {}
    global bstack1ll1llllll1_opy_
    if bstack111l1ll_opy_ (u"ࠫࡕࡇࡃࡠࡒࡕࡓ࡝࡟ࠧᘪ") in globals():
        return bstack1ll1llllll1_opy_
    try:
        proxy = bstack1ll1llll1l1_opy_(bstack1ll1lllll11_opy_, bstack1ll1lllll1l_opy_)
        if bstack111l1ll_opy_ (u"ࠧࡊࡉࡓࡇࡆࡘࠧᘫ") in proxy:
            proxies = {}
        elif bstack111l1ll_opy_ (u"ࠨࡈࡕࡖࡓࠦᘬ") in proxy or bstack111l1ll_opy_ (u"ࠢࡉࡖࡗࡔࡘࠨᘭ") in proxy or bstack111l1ll_opy_ (u"ࠣࡕࡒࡇࡐ࡙ࠢᘮ") in proxy:
            bstack1ll1lllllll_opy_ = proxy.split(bstack111l1ll_opy_ (u"ࠤࠣࠦᘯ"))
            if bstack111l1ll_opy_ (u"ࠥ࠾࠴࠵ࠢᘰ") in bstack111l1ll_opy_ (u"ࠦࠧᘱ").join(bstack1ll1lllllll_opy_[1:]):
                proxies = {
                    bstack111l1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᘲ"): bstack111l1ll_opy_ (u"ࠨࠢᘳ").join(bstack1ll1lllllll_opy_[1:])
                }
            else:
                proxies = {
                    bstack111l1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᘴ"): str(bstack1ll1lllllll_opy_[0]).lower() + bstack111l1ll_opy_ (u"ࠣ࠼࠲࠳ࠧᘵ") + bstack111l1ll_opy_ (u"ࠤࠥᘶ").join(bstack1ll1lllllll_opy_[1:])
                }
        elif bstack111l1ll_opy_ (u"ࠥࡔࡗࡕࡘ࡚ࠤᘷ") in proxy:
            bstack1ll1lllllll_opy_ = proxy.split(bstack111l1ll_opy_ (u"ࠦࠥࠨᘸ"))
            if bstack111l1ll_opy_ (u"ࠧࡀ࠯࠰ࠤᘹ") in bstack111l1ll_opy_ (u"ࠨࠢᘺ").join(bstack1ll1lllllll_opy_[1:]):
                proxies = {
                    bstack111l1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᘻ"): bstack111l1ll_opy_ (u"ࠣࠤᘼ").join(bstack1ll1lllllll_opy_[1:])
                }
            else:
                proxies = {
                    bstack111l1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᘽ"): bstack111l1ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᘾ") + bstack111l1ll_opy_ (u"ࠦࠧᘿ").join(bstack1ll1lllllll_opy_[1:])
                }
        else:
            proxies = {
                bstack111l1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᙀ"): proxy
            }
    except Exception as e:
        print(bstack111l1ll_opy_ (u"ࠨࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠥᙁ"), bstack1llll1111ll_opy_.format(bstack1ll1lllll11_opy_, str(e)))
    bstack1ll1llllll1_opy_ = proxies
    return proxies