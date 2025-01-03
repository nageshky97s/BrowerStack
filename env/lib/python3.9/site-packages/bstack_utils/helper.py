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
import datetime
import json
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
import sys
import logging
from math import ceil
import urllib
from urllib.parse import urlparse
import copy
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import (bstack111l111ll1_opy_, bstack1ll111l1l1_opy_, bstack11111ll11_opy_, bstack1lll1l111_opy_,
                                    bstack111l11111l_opy_, bstack111l111lll_opy_, bstack111l111l1l_opy_, bstack111l11l11l_opy_)
from bstack_utils.messages import bstack11lll11l1l_opy_, bstack11l1l1l111_opy_
from bstack_utils.proxy import bstack1l1l1l1ll_opy_, bstack111111ll1_opy_
bstack1111lll1_opy_ = Config.bstack11111lll_opy_()
logger = logging.getLogger(__name__)
def bstack111ll1ll1l_opy_(config):
    return config[bstack111l1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫጴ")]
def bstack111lll111l_opy_(config):
    return config[bstack111l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ጵ")]
def bstack1llll1llll_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack11111l11ll_opy_(obj):
    values = []
    bstack1111ll1lll_opy_ = re.compile(bstack111l1ll_opy_ (u"ࡶࠧࡤࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢࡠࡩ࠱ࠤࠣጶ"), re.I)
    for key in obj.keys():
        if bstack1111ll1lll_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1llllll11ll_opy_(config):
    tags = []
    tags.extend(bstack11111l11ll_opy_(os.environ))
    tags.extend(bstack11111l11ll_opy_(config))
    return tags
def bstack11111l111l_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack1lllll1llll_opy_(bstack1lllll11lll_opy_):
    if not bstack1lllll11lll_opy_:
        return bstack111l1ll_opy_ (u"ࠬ࠭ጷ")
    return bstack111l1ll_opy_ (u"ࠨࡻࡾࠢࠫࡿࢂ࠯ࠢጸ").format(bstack1lllll11lll_opy_.name, bstack1lllll11lll_opy_.email)
def bstack111ll111l1_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack1111111lll_opy_ = repo.common_dir
        info = {
            bstack111l1ll_opy_ (u"ࠢࡴࡪࡤࠦጹ"): repo.head.commit.hexsha,
            bstack111l1ll_opy_ (u"ࠣࡵ࡫ࡳࡷࡺ࡟ࡴࡪࡤࠦጺ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack111l1ll_opy_ (u"ࠤࡥࡶࡦࡴࡣࡩࠤጻ"): repo.active_branch.name,
            bstack111l1ll_opy_ (u"ࠥࡸࡦ࡭ࠢጼ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack111l1ll_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡸࡪࡸࠢጽ"): bstack1lllll1llll_opy_(repo.head.commit.committer),
            bstack111l1ll_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡹ࡫ࡲࡠࡦࡤࡸࡪࠨጾ"): repo.head.commit.committed_datetime.isoformat(),
            bstack111l1ll_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࠨጿ"): bstack1lllll1llll_opy_(repo.head.commit.author),
            bstack111l1ll_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸ࡟ࡥࡣࡷࡩࠧፀ"): repo.head.commit.authored_datetime.isoformat(),
            bstack111l1ll_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡠ࡯ࡨࡷࡸࡧࡧࡦࠤፁ"): repo.head.commit.message,
            bstack111l1ll_opy_ (u"ࠤࡵࡳࡴࡺࠢፂ"): repo.git.rev_parse(bstack111l1ll_opy_ (u"ࠥ࠱࠲ࡹࡨࡰࡹ࠰ࡸࡴࡶ࡬ࡦࡸࡨࡰࠧፃ")),
            bstack111l1ll_opy_ (u"ࠦࡨࡵ࡭࡮ࡱࡱࡣ࡬࡯ࡴࡠࡦ࡬ࡶࠧፄ"): bstack1111111lll_opy_,
            bstack111l1ll_opy_ (u"ࠧࡽ࡯ࡳ࡭ࡷࡶࡪ࡫࡟ࡨ࡫ࡷࡣࡩ࡯ࡲࠣፅ"): subprocess.check_output([bstack111l1ll_opy_ (u"ࠨࡧࡪࡶࠥፆ"), bstack111l1ll_opy_ (u"ࠢࡳࡧࡹ࠱ࡵࡧࡲࡴࡧࠥፇ"), bstack111l1ll_opy_ (u"ࠣ࠯࠰࡫࡮ࡺ࠭ࡤࡱࡰࡱࡴࡴ࠭ࡥ࡫ࡵࠦፈ")]).strip().decode(
                bstack111l1ll_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨፉ")),
            bstack111l1ll_opy_ (u"ࠥࡰࡦࡹࡴࡠࡶࡤ࡫ࠧፊ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack111l1ll_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡷࡤࡹࡩ࡯ࡥࡨࡣࡱࡧࡳࡵࡡࡷࡥ࡬ࠨፋ"): repo.git.rev_list(
                bstack111l1ll_opy_ (u"ࠧࢁࡽ࠯࠰ࡾࢁࠧፌ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1111111l11_opy_ = []
        for remote in remotes:
            bstack1lllll1l1l1_opy_ = {
                bstack111l1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦፍ"): remote.name,
                bstack111l1ll_opy_ (u"ࠢࡶࡴ࡯ࠦፎ"): remote.url,
            }
            bstack1111111l11_opy_.append(bstack1lllll1l1l1_opy_)
        bstack11111lllll_opy_ = {
            bstack111l1ll_opy_ (u"ࠣࡰࡤࡱࡪࠨፏ"): bstack111l1ll_opy_ (u"ࠤࡪ࡭ࡹࠨፐ"),
            **info,
            bstack111l1ll_opy_ (u"ࠥࡶࡪࡳ࡯ࡵࡧࡶࠦፑ"): bstack1111111l11_opy_
        }
        bstack11111lllll_opy_ = bstack1llllll1l1l_opy_(bstack11111lllll_opy_)
        return bstack11111lllll_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack111l1ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡴࡶࡵ࡭ࡣࡷ࡭ࡳ࡭ࠠࡈ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢፒ").format(err))
        return {}
def bstack1llllll1l1l_opy_(bstack11111lllll_opy_):
    bstack1lllllll11l_opy_ = bstack1lllll1l111_opy_(bstack11111lllll_opy_)
    if bstack1lllllll11l_opy_ and bstack1lllllll11l_opy_ > bstack111l11111l_opy_:
        bstack11111ll11l_opy_ = bstack1lllllll11l_opy_ - bstack111l11111l_opy_
        bstack1llllll1111_opy_ = bstack1111l11l11_opy_(bstack11111lllll_opy_[bstack111l1ll_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡤࡳࡥࡴࡵࡤ࡫ࡪࠨፓ")], bstack11111ll11l_opy_)
        bstack11111lllll_opy_[bstack111l1ll_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢፔ")] = bstack1llllll1111_opy_
        logger.info(bstack111l1ll_opy_ (u"ࠢࡕࡪࡨࠤࡨࡵ࡭࡮࡫ࡷࠤ࡭ࡧࡳࠡࡤࡨࡩࡳࠦࡴࡳࡷࡱࡧࡦࡺࡥࡥ࠰ࠣࡗ࡮ࢀࡥࠡࡱࡩࠤࡨࡵ࡭࡮࡫ࡷࠤࡦ࡬ࡴࡦࡴࠣࡸࡷࡻ࡮ࡤࡣࡷ࡭ࡴࡴࠠࡪࡵࠣࡿࢂࠦࡋࡃࠤፕ")
                    .format(bstack1lllll1l111_opy_(bstack11111lllll_opy_) / 1024))
    return bstack11111lllll_opy_
def bstack1lllll1l111_opy_(bstack1l11l11lll_opy_):
    try:
        if bstack1l11l11lll_opy_:
            bstack1llllll11l1_opy_ = json.dumps(bstack1l11l11lll_opy_)
            bstack1111l1ll11_opy_ = sys.getsizeof(bstack1llllll11l1_opy_)
            return bstack1111l1ll11_opy_
    except Exception as e:
        logger.debug(bstack111l1ll_opy_ (u"ࠣࡕࡲࡱࡪࡺࡨࡪࡰࡪࠤࡼ࡫࡮ࡵࠢࡺࡶࡴࡴࡧࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡣ࡯ࡧࡺࡲࡡࡵ࡫ࡱ࡫ࠥࡹࡩࡻࡧࠣࡳ࡫ࠦࡊࡔࡑࡑࠤࡴࡨࡪࡦࡥࡷ࠾ࠥࢁࡽࠣፖ").format(e))
    return -1
def bstack1111l11l11_opy_(field, bstack11111l1ll1_opy_):
    try:
        bstack1lllllll111_opy_ = len(bytes(bstack111l111lll_opy_, bstack111l1ll_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨፗ")))
        bstack11111ll1ll_opy_ = bytes(field, bstack111l1ll_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩፘ"))
        bstack1lllllllll1_opy_ = len(bstack11111ll1ll_opy_)
        bstack11111lll1l_opy_ = ceil(bstack1lllllllll1_opy_ - bstack11111l1ll1_opy_ - bstack1lllllll111_opy_)
        if bstack11111lll1l_opy_ > 0:
            bstack11111111ll_opy_ = bstack11111ll1ll_opy_[:bstack11111lll1l_opy_].decode(bstack111l1ll_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪፙ"), errors=bstack111l1ll_opy_ (u"ࠬ࡯ࡧ࡯ࡱࡵࡩࠬፚ")) + bstack111l111lll_opy_
            return bstack11111111ll_opy_
    except Exception as e:
        logger.debug(bstack111l1ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡹࡸࡵ࡯ࡥࡤࡸ࡮ࡴࡧࠡࡨ࡬ࡩࡱࡪࠬࠡࡰࡲࡸ࡭࡯࡮ࡨࠢࡺࡥࡸࠦࡴࡳࡷࡱࡧࡦࡺࡥࡥࠢ࡫ࡩࡷ࡫࠺ࠡࡽࢀࠦ፛").format(e))
    return field
def bstack11l1l111l_opy_():
    env = os.environ
    if (bstack111l1ll_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡗࡕࡐࠧ፜") in env and len(env[bstack111l1ll_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑࠨ፝")]) > 0) or (
            bstack111l1ll_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢࡌࡔࡓࡅࠣ፞") in env and len(env[bstack111l1ll_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠤ፟")]) > 0):
        return {
            bstack111l1ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ፠"): bstack111l1ll_opy_ (u"ࠧࡐࡥ࡯࡭࡬ࡲࡸࠨ፡"),
            bstack111l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ።"): env.get(bstack111l1ll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥ፣")),
            bstack111l1ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ፤"): env.get(bstack111l1ll_opy_ (u"ࠤࡍࡓࡇࡥࡎࡂࡏࡈࠦ፥")),
            bstack111l1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ፦"): env.get(bstack111l1ll_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥ፧"))
        }
    if env.get(bstack111l1ll_opy_ (u"ࠧࡉࡉࠣ፨")) == bstack111l1ll_opy_ (u"ࠨࡴࡳࡷࡨࠦ፩") and bstack1l1l111lll_opy_(env.get(bstack111l1ll_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋࡃࡊࠤ፪"))):
        return {
            bstack111l1ll_opy_ (u"ࠣࡰࡤࡱࡪࠨ፫"): bstack111l1ll_opy_ (u"ࠤࡆ࡭ࡷࡩ࡬ࡦࡅࡌࠦ፬"),
            bstack111l1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ፭"): env.get(bstack111l1ll_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢ፮")),
            bstack111l1ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ፯"): env.get(bstack111l1ll_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡥࡊࡐࡄࠥ፰")),
            bstack111l1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ፱"): env.get(bstack111l1ll_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࠦ፲"))
        }
    if env.get(bstack111l1ll_opy_ (u"ࠤࡆࡍࠧ፳")) == bstack111l1ll_opy_ (u"ࠥࡸࡷࡻࡥࠣ፴") and bstack1l1l111lll_opy_(env.get(bstack111l1ll_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࠦ፵"))):
        return {
            bstack111l1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ፶"): bstack111l1ll_opy_ (u"ࠨࡔࡳࡣࡹ࡭ࡸࠦࡃࡊࠤ፷"),
            bstack111l1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ፸"): env.get(bstack111l1ll_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࡠࡄࡘࡍࡑࡊ࡟ࡘࡇࡅࡣ࡚ࡘࡌࠣ፹")),
            bstack111l1ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ፺"): env.get(bstack111l1ll_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧ፻")),
            bstack111l1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ፼"): env.get(bstack111l1ll_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦ፽"))
        }
    if env.get(bstack111l1ll_opy_ (u"ࠨࡃࡊࠤ፾")) == bstack111l1ll_opy_ (u"ࠢࡵࡴࡸࡩࠧ፿") and env.get(bstack111l1ll_opy_ (u"ࠣࡅࡌࡣࡓࡇࡍࡆࠤᎀ")) == bstack111l1ll_opy_ (u"ࠤࡦࡳࡩ࡫ࡳࡩ࡫ࡳࠦᎁ"):
        return {
            bstack111l1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᎂ"): bstack111l1ll_opy_ (u"ࠦࡈࡵࡤࡦࡵ࡫࡭ࡵࠨᎃ"),
            bstack111l1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᎄ"): None,
            bstack111l1ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᎅ"): None,
            bstack111l1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᎆ"): None
        }
    if env.get(bstack111l1ll_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡇࡘࡁࡏࡅࡋࠦᎇ")) and env.get(bstack111l1ll_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡉࡏࡎࡏࡌࡘࠧᎈ")):
        return {
            bstack111l1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᎉ"): bstack111l1ll_opy_ (u"ࠦࡇ࡯ࡴࡣࡷࡦ࡯ࡪࡺࠢᎊ"),
            bstack111l1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᎋ"): env.get(bstack111l1ll_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡊࡍ࡙ࡥࡈࡕࡖࡓࡣࡔࡘࡉࡈࡋࡑࠦᎌ")),
            bstack111l1ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᎍ"): None,
            bstack111l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᎎ"): env.get(bstack111l1ll_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᎏ"))
        }
    if env.get(bstack111l1ll_opy_ (u"ࠥࡇࡎࠨ᎐")) == bstack111l1ll_opy_ (u"ࠦࡹࡸࡵࡦࠤ᎑") and bstack1l1l111lll_opy_(env.get(bstack111l1ll_opy_ (u"ࠧࡊࡒࡐࡐࡈࠦ᎒"))):
        return {
            bstack111l1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᎓"): bstack111l1ll_opy_ (u"ࠢࡅࡴࡲࡲࡪࠨ᎔"),
            bstack111l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᎕"): env.get(bstack111l1ll_opy_ (u"ࠤࡇࡖࡔࡔࡅࡠࡄࡘࡍࡑࡊ࡟ࡍࡋࡑࡏࠧ᎖")),
            bstack111l1ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᎗"): None,
            bstack111l1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᎘"): env.get(bstack111l1ll_opy_ (u"ࠧࡊࡒࡐࡐࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥ᎙"))
        }
    if env.get(bstack111l1ll_opy_ (u"ࠨࡃࡊࠤ᎚")) == bstack111l1ll_opy_ (u"ࠢࡵࡴࡸࡩࠧ᎛") and bstack1l1l111lll_opy_(env.get(bstack111l1ll_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࠦ᎜"))):
        return {
            bstack111l1ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᎝"): bstack111l1ll_opy_ (u"ࠥࡗࡪࡳࡡࡱࡪࡲࡶࡪࠨ᎞"),
            bstack111l1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᎟"): env.get(bstack111l1ll_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࡠࡑࡕࡋࡆࡔࡉ࡛ࡃࡗࡍࡔࡔ࡟ࡖࡔࡏࠦᎠ")),
            bstack111l1ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᎡ"): env.get(bstack111l1ll_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᎢ")),
            bstack111l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᎣ"): env.get(bstack111l1ll_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࡤࡐࡏࡃࡡࡌࡈࠧᎤ"))
        }
    if env.get(bstack111l1ll_opy_ (u"ࠥࡇࡎࠨᎥ")) == bstack111l1ll_opy_ (u"ࠦࡹࡸࡵࡦࠤᎦ") and bstack1l1l111lll_opy_(env.get(bstack111l1ll_opy_ (u"ࠧࡍࡉࡕࡎࡄࡆࡤࡉࡉࠣᎧ"))):
        return {
            bstack111l1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᎨ"): bstack111l1ll_opy_ (u"ࠢࡈ࡫ࡷࡐࡦࡨࠢᎩ"),
            bstack111l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᎪ"): env.get(bstack111l1ll_opy_ (u"ࠤࡆࡍࡤࡐࡏࡃࡡࡘࡖࡑࠨᎫ")),
            bstack111l1ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᎬ"): env.get(bstack111l1ll_opy_ (u"ࠦࡈࡏ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᎭ")),
            bstack111l1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᎮ"): env.get(bstack111l1ll_opy_ (u"ࠨࡃࡊࡡࡍࡓࡇࡥࡉࡅࠤᎯ"))
        }
    if env.get(bstack111l1ll_opy_ (u"ࠢࡄࡋࠥᎰ")) == bstack111l1ll_opy_ (u"ࠣࡶࡵࡹࡪࠨᎱ") and bstack1l1l111lll_opy_(env.get(bstack111l1ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࠧᎲ"))):
        return {
            bstack111l1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᎳ"): bstack111l1ll_opy_ (u"ࠦࡇࡻࡩ࡭ࡦ࡮࡭ࡹ࡫ࠢᎴ"),
            bstack111l1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᎵ"): env.get(bstack111l1ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᎶ")),
            bstack111l1ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᎷ"): env.get(bstack111l1ll_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡑࡇࡂࡆࡎࠥᎸ")) or env.get(bstack111l1ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡏࡃࡐࡉࠧᎹ")),
            bstack111l1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᎺ"): env.get(bstack111l1ll_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᎻ"))
        }
    if bstack1l1l111lll_opy_(env.get(bstack111l1ll_opy_ (u"࡚ࠧࡆࡠࡄࡘࡍࡑࡊࠢᎼ"))):
        return {
            bstack111l1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᎽ"): bstack111l1ll_opy_ (u"ࠢࡗ࡫ࡶࡹࡦࡲࠠࡔࡶࡸࡨ࡮ࡵࠠࡕࡧࡤࡱ࡙ࠥࡥࡳࡸ࡬ࡧࡪࡹࠢᎾ"),
            bstack111l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᎿ"): bstack111l1ll_opy_ (u"ࠤࡾࢁࢀࢃࠢᏀ").format(env.get(bstack111l1ll_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡇࡑࡘࡒࡉࡇࡔࡊࡑࡑࡗࡊࡘࡖࡆࡔࡘࡖࡎ࠭Ꮑ")), env.get(bstack111l1ll_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡒࡕࡓࡏࡋࡃࡕࡋࡇࠫᏂ"))),
            bstack111l1ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᏃ"): env.get(bstack111l1ll_opy_ (u"ࠨࡓ࡚ࡕࡗࡉࡒࡥࡄࡆࡈࡌࡒࡎ࡚ࡉࡐࡐࡌࡈࠧᏄ")),
            bstack111l1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᏅ"): env.get(bstack111l1ll_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠣᏆ"))
        }
    if bstack1l1l111lll_opy_(env.get(bstack111l1ll_opy_ (u"ࠤࡄࡔࡕ࡜ࡅ࡚ࡑࡕࠦᏇ"))):
        return {
            bstack111l1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᏈ"): bstack111l1ll_opy_ (u"ࠦࡆࡶࡰࡷࡧࡼࡳࡷࠨᏉ"),
            bstack111l1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᏊ"): bstack111l1ll_opy_ (u"ࠨࡻࡾ࠱ࡳࡶࡴࡰࡥࡤࡶ࠲ࡿࢂ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁࠧᏋ").format(env.get(bstack111l1ll_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡘࡖࡑ࠭Ꮜ")), env.get(bstack111l1ll_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡅࡈࡉࡏࡖࡐࡗࡣࡓࡇࡍࡆࠩᏍ")), env.get(bstack111l1ll_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡕࡘࡏࡋࡇࡆࡘࡤ࡙ࡌࡖࡉࠪᏎ")), env.get(bstack111l1ll_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧᏏ"))),
            bstack111l1ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᏐ"): env.get(bstack111l1ll_opy_ (u"ࠧࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᏑ")),
            bstack111l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᏒ"): env.get(bstack111l1ll_opy_ (u"ࠢࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᏓ"))
        }
    if env.get(bstack111l1ll_opy_ (u"ࠣࡃ࡝࡙ࡗࡋ࡟ࡉࡖࡗࡔࡤ࡛ࡓࡆࡔࡢࡅࡌࡋࡎࡕࠤᏔ")) and env.get(bstack111l1ll_opy_ (u"ࠤࡗࡊࡤࡈࡕࡊࡎࡇࠦᏕ")):
        return {
            bstack111l1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᏖ"): bstack111l1ll_opy_ (u"ࠦࡆࢀࡵࡳࡧࠣࡇࡎࠨᏗ"),
            bstack111l1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᏘ"): bstack111l1ll_opy_ (u"ࠨࡻࡾࡽࢀ࠳ࡤࡨࡵࡪ࡮ࡧ࠳ࡷ࡫ࡳࡶ࡮ࡷࡷࡄࡨࡵࡪ࡮ࡧࡍࡩࡃࡻࡾࠤᏙ").format(env.get(bstack111l1ll_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡋࡕࡕࡏࡆࡄࡘࡎࡕࡎࡔࡇࡕ࡚ࡊࡘࡕࡓࡋࠪᏚ")), env.get(bstack111l1ll_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡖࡒࡐࡌࡈࡇ࡙࠭Ꮫ")), env.get(bstack111l1ll_opy_ (u"ࠩࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠩᏜ"))),
            bstack111l1ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᏝ"): env.get(bstack111l1ll_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠦᏞ")),
            bstack111l1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᏟ"): env.get(bstack111l1ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉࠨᏠ"))
        }
    if any([env.get(bstack111l1ll_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᏡ")), env.get(bstack111l1ll_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡗࡋࡓࡐࡎ࡙ࡉࡉࡥࡓࡐࡗࡕࡇࡊࡥࡖࡆࡔࡖࡍࡔࡔࠢᏢ")), env.get(bstack111l1ll_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤ࡙ࡏࡖࡔࡆࡉࡤ࡜ࡅࡓࡕࡌࡓࡓࠨᏣ"))]):
        return {
            bstack111l1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᏤ"): bstack111l1ll_opy_ (u"ࠦࡆ࡝ࡓࠡࡅࡲࡨࡪࡈࡵࡪ࡮ࡧࠦᏥ"),
            bstack111l1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᏦ"): env.get(bstack111l1ll_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡓ࡙ࡇࡒࡉࡄࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᏧ")),
            bstack111l1ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᏨ"): env.get(bstack111l1ll_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᏩ")),
            bstack111l1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᏪ"): env.get(bstack111l1ll_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣᏫ"))
        }
    if env.get(bstack111l1ll_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡧࡻࡩ࡭ࡦࡑࡹࡲࡨࡥࡳࠤᏬ")):
        return {
            bstack111l1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᏭ"): bstack111l1ll_opy_ (u"ࠨࡂࡢ࡯ࡥࡳࡴࠨᏮ"),
            bstack111l1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᏯ"): env.get(bstack111l1ll_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡤࡸ࡭ࡱࡪࡒࡦࡵࡸࡰࡹࡹࡕࡳ࡮ࠥᏰ")),
            bstack111l1ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᏱ"): env.get(bstack111l1ll_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡷ࡭ࡵࡲࡵࡌࡲࡦࡓࡧ࡭ࡦࠤᏲ")),
            bstack111l1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᏳ"): env.get(bstack111l1ll_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡒࡺࡳࡢࡦࡴࠥᏴ"))
        }
    if env.get(bstack111l1ll_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘࠢᏵ")) or env.get(bstack111l1ll_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡏࡄࡍࡓࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡕࡗࡅࡗ࡚ࡅࡅࠤ᏶")):
        return {
            bstack111l1ll_opy_ (u"ࠣࡰࡤࡱࡪࠨ᏷"): bstack111l1ll_opy_ (u"ࠤ࡚ࡩࡷࡩ࡫ࡦࡴࠥᏸ"),
            bstack111l1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᏹ"): env.get(bstack111l1ll_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᏺ")),
            bstack111l1ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᏻ"): bstack111l1ll_opy_ (u"ࠨࡍࡢ࡫ࡱࠤࡕ࡯ࡰࡦ࡮࡬ࡲࡪࠨᏼ") if env.get(bstack111l1ll_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡏࡄࡍࡓࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡕࡗࡅࡗ࡚ࡅࡅࠤᏽ")) else None,
            bstack111l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᏾"): env.get(bstack111l1ll_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡋࡎ࡚࡟ࡄࡑࡐࡑࡎ࡚ࠢ᏿"))
        }
    if any([env.get(bstack111l1ll_opy_ (u"ࠥࡋࡈࡖ࡟ࡑࡔࡒࡎࡊࡉࡔࠣ᐀")), env.get(bstack111l1ll_opy_ (u"ࠦࡌࡉࡌࡐࡗࡇࡣࡕࡘࡏࡋࡇࡆࡘࠧᐁ")), env.get(bstack111l1ll_opy_ (u"ࠧࡍࡏࡐࡉࡏࡉࡤࡉࡌࡐࡗࡇࡣࡕࡘࡏࡋࡇࡆࡘࠧᐂ"))]):
        return {
            bstack111l1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᐃ"): bstack111l1ll_opy_ (u"ࠢࡈࡱࡲ࡫ࡱ࡫ࠠࡄ࡮ࡲࡹࡩࠨᐄ"),
            bstack111l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᐅ"): None,
            bstack111l1ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᐆ"): env.get(bstack111l1ll_opy_ (u"ࠥࡔࡗࡕࡊࡆࡅࡗࡣࡎࡊࠢᐇ")),
            bstack111l1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᐈ"): env.get(bstack111l1ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢᐉ"))
        }
    if env.get(bstack111l1ll_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࠤᐊ")):
        return {
            bstack111l1ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᐋ"): bstack111l1ll_opy_ (u"ࠣࡕ࡫࡭ࡵࡶࡡࡣ࡮ࡨࠦᐌ"),
            bstack111l1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᐍ"): env.get(bstack111l1ll_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᐎ")),
            bstack111l1ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᐏ"): bstack111l1ll_opy_ (u"ࠧࡐ࡯ࡣࠢࠦࡿࢂࠨᐐ").format(env.get(bstack111l1ll_opy_ (u"࠭ࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡍࡓࡇࡥࡉࡅࠩᐑ"))) if env.get(bstack111l1ll_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡎࡔࡈ࡟ࡊࡆࠥᐒ")) else None,
            bstack111l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᐓ"): env.get(bstack111l1ll_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᐔ"))
        }
    if bstack1l1l111lll_opy_(env.get(bstack111l1ll_opy_ (u"ࠥࡒࡊ࡚ࡌࡊࡈ࡜ࠦᐕ"))):
        return {
            bstack111l1ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᐖ"): bstack111l1ll_opy_ (u"ࠧࡔࡥࡵ࡮࡬ࡪࡾࠨᐗ"),
            bstack111l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᐘ"): env.get(bstack111l1ll_opy_ (u"ࠢࡅࡇࡓࡐࡔ࡟࡟ࡖࡔࡏࠦᐙ")),
            bstack111l1ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᐚ"): env.get(bstack111l1ll_opy_ (u"ࠤࡖࡍ࡙ࡋ࡟ࡏࡃࡐࡉࠧᐛ")),
            bstack111l1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᐜ"): env.get(bstack111l1ll_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᐝ"))
        }
    if bstack1l1l111lll_opy_(env.get(bstack111l1ll_opy_ (u"ࠧࡍࡉࡕࡊࡘࡆࡤࡇࡃࡕࡋࡒࡒࡘࠨᐞ"))):
        return {
            bstack111l1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᐟ"): bstack111l1ll_opy_ (u"ࠢࡈ࡫ࡷࡌࡺࡨࠠࡂࡥࡷ࡭ࡴࡴࡳࠣᐠ"),
            bstack111l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᐡ"): bstack111l1ll_opy_ (u"ࠤࡾࢁ࠴ࢁࡽ࠰ࡣࡦࡸ࡮ࡵ࡮ࡴ࠱ࡵࡹࡳࡹ࠯ࡼࡿࠥᐢ").format(env.get(bstack111l1ll_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡗࡊࡘࡖࡆࡔࡢ࡙ࡗࡒࠧᐣ")), env.get(bstack111l1ll_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡗࡋࡐࡐࡕࡌࡘࡔࡘ࡙ࠨᐤ")), env.get(bstack111l1ll_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤࡘࡕࡏࡡࡌࡈࠬᐥ"))),
            bstack111l1ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᐦ"): env.get(bstack111l1ll_opy_ (u"ࠢࡈࡋࡗࡌ࡚ࡈ࡟ࡘࡑࡕࡏࡋࡒࡏࡘࠤᐧ")),
            bstack111l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᐨ"): env.get(bstack111l1ll_opy_ (u"ࠤࡊࡍ࡙ࡎࡕࡃࡡࡕ࡙ࡓࡥࡉࡅࠤᐩ"))
        }
    if env.get(bstack111l1ll_opy_ (u"ࠥࡇࡎࠨᐪ")) == bstack111l1ll_opy_ (u"ࠦࡹࡸࡵࡦࠤᐫ") and env.get(bstack111l1ll_opy_ (u"ࠧ࡜ࡅࡓࡅࡈࡐࠧᐬ")) == bstack111l1ll_opy_ (u"ࠨ࠱ࠣᐭ"):
        return {
            bstack111l1ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᐮ"): bstack111l1ll_opy_ (u"ࠣࡘࡨࡶࡨ࡫࡬ࠣᐯ"),
            bstack111l1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᐰ"): bstack111l1ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࡿࢂࠨᐱ").format(env.get(bstack111l1ll_opy_ (u"࡛ࠫࡋࡒࡄࡇࡏࡣ࡚ࡘࡌࠨᐲ"))),
            bstack111l1ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᐳ"): None,
            bstack111l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᐴ"): None,
        }
    if env.get(bstack111l1ll_opy_ (u"ࠢࡕࡇࡄࡑࡈࡏࡔ࡚ࡡ࡙ࡉࡗ࡙ࡉࡐࡐࠥᐵ")):
        return {
            bstack111l1ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᐶ"): bstack111l1ll_opy_ (u"ࠤࡗࡩࡦࡳࡣࡪࡶࡼࠦᐷ"),
            bstack111l1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᐸ"): None,
            bstack111l1ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᐹ"): env.get(bstack111l1ll_opy_ (u"࡚ࠧࡅࡂࡏࡆࡍ࡙࡟࡟ࡑࡔࡒࡎࡊࡉࡔࡠࡐࡄࡑࡊࠨᐺ")),
            bstack111l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᐻ"): env.get(bstack111l1ll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᐼ"))
        }
    if any([env.get(bstack111l1ll_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࠦᐽ")), env.get(bstack111l1ll_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡛ࡒࡍࠤᐾ")), env.get(bstack111l1ll_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡕࡔࡇࡕࡒࡆࡓࡅࠣᐿ")), env.get(bstack111l1ll_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡕࡇࡄࡑࠧᑀ"))]):
        return {
            bstack111l1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᑁ"): bstack111l1ll_opy_ (u"ࠨࡃࡰࡰࡦࡳࡺࡸࡳࡦࠤᑂ"),
            bstack111l1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᑃ"): None,
            bstack111l1ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᑄ"): env.get(bstack111l1ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᑅ")) or None,
            bstack111l1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᑆ"): env.get(bstack111l1ll_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᑇ"), 0)
        }
    if env.get(bstack111l1ll_opy_ (u"ࠧࡍࡏࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᑈ")):
        return {
            bstack111l1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᑉ"): bstack111l1ll_opy_ (u"ࠢࡈࡱࡆࡈࠧᑊ"),
            bstack111l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᑋ"): None,
            bstack111l1ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᑌ"): env.get(bstack111l1ll_opy_ (u"ࠥࡋࡔࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᑍ")),
            bstack111l1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᑎ"): env.get(bstack111l1ll_opy_ (u"ࠧࡍࡏࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡇࡔ࡛ࡎࡕࡇࡕࠦᑏ"))
        }
    if env.get(bstack111l1ll_opy_ (u"ࠨࡃࡇࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᑐ")):
        return {
            bstack111l1ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᑑ"): bstack111l1ll_opy_ (u"ࠣࡅࡲࡨࡪࡌࡲࡦࡵ࡫ࠦᑒ"),
            bstack111l1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᑓ"): env.get(bstack111l1ll_opy_ (u"ࠥࡇࡋࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᑔ")),
            bstack111l1ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᑕ"): env.get(bstack111l1ll_opy_ (u"ࠧࡉࡆࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡒࡆࡓࡅࠣᑖ")),
            bstack111l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᑗ"): env.get(bstack111l1ll_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᑘ"))
        }
    return {bstack111l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᑙ"): None}
def get_host_info():
    return {
        bstack111l1ll_opy_ (u"ࠤ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠦᑚ"): platform.node(),
        bstack111l1ll_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࠧᑛ"): platform.system(),
        bstack111l1ll_opy_ (u"ࠦࡹࡿࡰࡦࠤᑜ"): platform.machine(),
        bstack111l1ll_opy_ (u"ࠧࡼࡥࡳࡵ࡬ࡳࡳࠨᑝ"): platform.version(),
        bstack111l1ll_opy_ (u"ࠨࡡࡳࡥ࡫ࠦᑞ"): platform.architecture()[0]
    }
def bstack1l1ll11l1_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111111lll1_opy_():
    if bstack1111lll1_opy_.get_property(bstack111l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨᑟ")):
        return bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᑠ")
    return bstack111l1ll_opy_ (u"ࠩࡸࡲࡰࡴ࡯ࡸࡰࡢ࡫ࡷ࡯ࡤࠨᑡ")
def bstack1111l1l1ll_opy_(driver):
    info = {
        bstack111l1ll_opy_ (u"ࠪࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩᑢ"): driver.capabilities,
        bstack111l1ll_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠨᑣ"): driver.session_id,
        bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ᑤ"): driver.capabilities.get(bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫᑥ"), None),
        bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᑦ"): driver.capabilities.get(bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᑧ"), None),
        bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࠫᑨ"): driver.capabilities.get(bstack111l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩᑩ"), None),
    }
    if bstack111111lll1_opy_() == bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᑪ"):
        if bstack11l1l111ll_opy_():
            info[bstack111l1ll_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᑫ")] = bstack111l1ll_opy_ (u"࠭ࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᑬ")
        elif driver.capabilities.get(bstack111l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᑭ"), {}).get(bstack111l1ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬᑮ"), False):
            info[bstack111l1ll_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࠪᑯ")] = bstack111l1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧᑰ")
        else:
            info[bstack111l1ll_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬᑱ")] = bstack111l1ll_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᑲ")
    return info
def bstack11l1l111ll_opy_():
    if bstack1111lll1_opy_.get_property(bstack111l1ll_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᑳ")):
        return True
    if bstack1l1l111lll_opy_(os.environ.get(bstack111l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨᑴ"), None)):
        return True
    return False
def bstack11l11l1111_opy_(bstack111111ll11_opy_, url, data, config):
    headers = config.get(bstack111l1ll_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩᑵ"), None)
    proxies = bstack1l1l1l1ll_opy_(config, url)
    auth = config.get(bstack111l1ll_opy_ (u"ࠩࡤࡹࡹ࡮ࠧᑶ"), None)
    response = requests.request(
            bstack111111ll11_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1l1l111111_opy_(bstack1111l11ll_opy_, size):
    bstack1l1111ll11_opy_ = []
    while len(bstack1111l11ll_opy_) > size:
        bstack11l11lllll_opy_ = bstack1111l11ll_opy_[:size]
        bstack1l1111ll11_opy_.append(bstack11l11lllll_opy_)
        bstack1111l11ll_opy_ = bstack1111l11ll_opy_[size:]
    bstack1l1111ll11_opy_.append(bstack1111l11ll_opy_)
    return bstack1l1111ll11_opy_
def bstack1111l111ll_opy_(message, bstack1111l1llll_opy_=False):
    os.write(1, bytes(message, bstack111l1ll_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᑷ")))
    os.write(1, bytes(bstack111l1ll_opy_ (u"ࠫࡡࡴࠧᑸ"), bstack111l1ll_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᑹ")))
    if bstack1111l1llll_opy_:
        with open(bstack111l1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࠳࡯࠲࠳ࡼ࠱ࠬᑺ") + os.environ[bstack111l1ll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭ᑻ")] + bstack111l1ll_opy_ (u"ࠨ࠰࡯ࡳ࡬࠭ᑼ"), bstack111l1ll_opy_ (u"ࠩࡤࠫᑽ")) as f:
            f.write(message + bstack111l1ll_opy_ (u"ࠪࡠࡳ࠭ᑾ"))
def bstack1111ll1l1l_opy_():
    return os.environ[bstack111l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧᑿ")].lower() == bstack111l1ll_opy_ (u"ࠬࡺࡲࡶࡧࠪᒀ")
def bstack11lll1l1l_opy_(bstack1111ll111l_opy_):
    return bstack111l1ll_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬᒁ").format(bstack111l111ll1_opy_, bstack1111ll111l_opy_)
def bstack1l1lllll_opy_():
    return bstack1l11lll1_opy_().replace(tzinfo=None).isoformat() + bstack111l1ll_opy_ (u"࡛ࠧࠩᒂ")
def bstack1111l11l1l_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack111l1ll_opy_ (u"ࠨ࡜ࠪᒃ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack111l1ll_opy_ (u"ࠩ࡝ࠫᒄ")))).total_seconds() * 1000
def bstack1lllll1l1ll_opy_(timestamp):
    return bstack1lllll1l11l_opy_(timestamp).isoformat() + bstack111l1ll_opy_ (u"ࠪ࡞ࠬᒅ")
def bstack11111ll111_opy_(bstack1111l1ll1l_opy_):
    date_format = bstack111l1ll_opy_ (u"ࠫࠪ࡟ࠥ࡮ࠧࡧࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠴ࠥࡧࠩᒆ")
    bstack1lllllll1l1_opy_ = datetime.datetime.strptime(bstack1111l1ll1l_opy_, date_format)
    return bstack1lllllll1l1_opy_.isoformat() + bstack111l1ll_opy_ (u"ࠬࡠࠧᒇ")
def bstack1111l11111_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack111l1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᒈ")
    else:
        return bstack111l1ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᒉ")
def bstack1l1l111lll_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack111l1ll_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᒊ")
def bstack1111ll1ll1_opy_(val):
    return val.__str__().lower() == bstack111l1ll_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨᒋ")
def bstack11l1111l_opy_(bstack1111lll11l_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1111lll11l_opy_ as e:
                print(bstack111l1ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࢀࢃࠠ࠮ࡀࠣࡿࢂࡀࠠࡼࡿࠥᒌ").format(func.__name__, bstack1111lll11l_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack111111llll_opy_(bstack1lllll1ll1l_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1lllll1ll1l_opy_(cls, *args, **kwargs)
            except bstack1111lll11l_opy_ as e:
                print(bstack111l1ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࢁࡽࠡ࠯ࡁࠤࢀࢃ࠺ࠡࡽࢀࠦᒍ").format(bstack1lllll1ll1l_opy_.__name__, bstack1111lll11l_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack111111llll_opy_
    else:
        return decorator
def bstack11ll1lll1_opy_(bstack1111l111_opy_):
    if bstack111l1ll_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᒎ") in bstack1111l111_opy_ and bstack1111ll1ll1_opy_(bstack1111l111_opy_[bstack111l1ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᒏ")]):
        return False
    if bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᒐ") in bstack1111l111_opy_ and bstack1111ll1ll1_opy_(bstack1111l111_opy_[bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᒑ")]):
        return False
    return True
def bstack1l1lll111l_opy_():
    try:
        from pytest_bdd import reporting
        bstack111111l11l_opy_ = os.environ.get(bstack111l1ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡗࡖࡉࡗࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠤᒒ"), None)
        return bstack111111l11l_opy_ is None or bstack111111l11l_opy_ == bstack111l1ll_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠢᒓ")
    except Exception as e:
        return False
def bstack1ll1111ll1_opy_(hub_url, CONFIG):
    if bstack11lll1111_opy_() <= version.parse(bstack111l1ll_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫᒔ")):
        if hub_url != bstack111l1ll_opy_ (u"ࠬ࠭ᒕ"):
            return bstack111l1ll_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢᒖ") + hub_url + bstack111l1ll_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦᒗ")
        return bstack11111ll11_opy_
    if hub_url != bstack111l1ll_opy_ (u"ࠨࠩᒘ"):
        return bstack111l1ll_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦᒙ") + hub_url + bstack111l1ll_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦᒚ")
    return bstack1lll1l111_opy_
def bstack1111llll11_opy_():
    return isinstance(os.getenv(bstack111l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡑ࡛ࡇࡊࡐࠪᒛ")), str)
def bstack1l1l1l1ll1_opy_(url):
    return urlparse(url).hostname
def bstack1l1l11111_opy_(hostname):
    for bstack11l1l1l1ll_opy_ in bstack1ll111l1l1_opy_:
        regex = re.compile(bstack11l1l1l1ll_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack111111l111_opy_(bstack1111lll111_opy_, file_name, logger):
    bstack11ll1l1l11_opy_ = os.path.join(os.path.expanduser(bstack111l1ll_opy_ (u"ࠬࢄࠧᒜ")), bstack1111lll111_opy_)
    try:
        if not os.path.exists(bstack11ll1l1l11_opy_):
            os.makedirs(bstack11ll1l1l11_opy_)
        file_path = os.path.join(os.path.expanduser(bstack111l1ll_opy_ (u"࠭ࡾࠨᒝ")), bstack1111lll111_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack111l1ll_opy_ (u"ࠧࡸࠩᒞ")):
                pass
            with open(file_path, bstack111l1ll_opy_ (u"ࠣࡹ࠮ࠦᒟ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack11lll11l1l_opy_.format(str(e)))
def bstack1111l1lll1_opy_(file_name, key, value, logger):
    file_path = bstack111111l111_opy_(bstack111l1ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᒠ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1lll11ll11_opy_ = json.load(open(file_path, bstack111l1ll_opy_ (u"ࠪࡶࡧ࠭ᒡ")))
        else:
            bstack1lll11ll11_opy_ = {}
        bstack1lll11ll11_opy_[key] = value
        with open(file_path, bstack111l1ll_opy_ (u"ࠦࡼ࠱ࠢᒢ")) as outfile:
            json.dump(bstack1lll11ll11_opy_, outfile)
def bstack1llllllll1_opy_(file_name, logger):
    file_path = bstack111111l111_opy_(bstack111l1ll_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᒣ"), file_name, logger)
    bstack1lll11ll11_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack111l1ll_opy_ (u"࠭ࡲࠨᒤ")) as bstack111111l1l_opy_:
            bstack1lll11ll11_opy_ = json.load(bstack111111l1l_opy_)
    return bstack1lll11ll11_opy_
def bstack11ll11l11l_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack111l1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡧࡩࡱ࡫ࡴࡪࡰࡪࠤ࡫࡯࡬ࡦ࠼ࠣࠫᒥ") + file_path + bstack111l1ll_opy_ (u"ࠨࠢࠪᒦ") + str(e))
def bstack11lll1111_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack111l1ll_opy_ (u"ࠤ࠿ࡒࡔ࡚ࡓࡆࡖࡁࠦᒧ")
def bstack1l1lll1ll_opy_(config):
    if bstack111l1ll_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᒨ") in config:
        del (config[bstack111l1ll_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᒩ")])
        return False
    if bstack11lll1111_opy_() < version.parse(bstack111l1ll_opy_ (u"ࠬ࠹࠮࠵࠰࠳ࠫᒪ")):
        return False
    if bstack11lll1111_opy_() >= version.parse(bstack111l1ll_opy_ (u"࠭࠴࠯࠳࠱࠹ࠬᒫ")):
        return True
    if bstack111l1ll_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧᒬ") in config and config[bstack111l1ll_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨᒭ")] is False:
        return False
    else:
        return True
def bstack11l1llll1l_opy_(args_list, bstack111111l1ll_opy_):
    index = -1
    for value in bstack111111l1ll_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1ll1lll1_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1ll1lll1_opy_ = bstack1ll1lll1_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack111l1ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᒮ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack111l1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᒯ"), exception=exception)
    def bstack1lllll1l1_opy_(self):
        if self.result != bstack111l1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᒰ"):
            return None
        if isinstance(self.exception_type, str) and bstack111l1ll_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣᒱ") in self.exception_type:
            return bstack111l1ll_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢᒲ")
        return bstack111l1ll_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣᒳ")
    def bstack1111l11ll1_opy_(self):
        if self.result != bstack111l1ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᒴ"):
            return None
        if self.bstack1ll1lll1_opy_:
            return self.bstack1ll1lll1_opy_
        return bstack1111l1l11l_opy_(self.exception)
def bstack1111l1l11l_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack11111111l1_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1ll111l1_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack11ll1l111l_opy_(config, logger):
    try:
        import playwright
        bstack111111111l_opy_ = playwright.__file__
        bstack1111l11lll_opy_ = os.path.split(bstack111111111l_opy_)
        bstack11111l11l1_opy_ = bstack1111l11lll_opy_[0] + bstack111l1ll_opy_ (u"ࠩ࠲ࡨࡷ࡯ࡶࡦࡴ࠲ࡴࡦࡩ࡫ࡢࡩࡨ࠳ࡱ࡯ࡢ࠰ࡥ࡯࡭࠴ࡩ࡬ࡪ࠰࡭ࡷࠬᒵ")
        os.environ[bstack111l1ll_opy_ (u"ࠪࡋࡑࡕࡂࡂࡎࡢࡅࡌࡋࡎࡕࡡࡋࡘ࡙ࡖ࡟ࡑࡔࡒ࡜࡞࠭ᒶ")] = bstack111111ll1_opy_(config)
        with open(bstack11111l11l1_opy_, bstack111l1ll_opy_ (u"ࠫࡷ࠭ᒷ")) as f:
            bstack1llll1l1l_opy_ = f.read()
            bstack11111ll1l1_opy_ = bstack111l1ll_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠫᒸ")
            bstack11111l1lll_opy_ = bstack1llll1l1l_opy_.find(bstack11111ll1l1_opy_)
            if bstack11111l1lll_opy_ == -1:
              process = subprocess.Popen(bstack111l1ll_opy_ (u"ࠨ࡮ࡱ࡯ࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠥᒹ"), shell=True, cwd=bstack1111l11lll_opy_[0])
              process.wait()
              bstack1llllllll11_opy_ = bstack111l1ll_opy_ (u"ࠧࠣࡷࡶࡩࠥࡹࡴࡳ࡫ࡦࡸࠧࡁࠧᒺ")
              bstack1111111111_opy_ = bstack111l1ll_opy_ (u"ࠣࠤࠥࠤࡡࠨࡵࡴࡧࠣࡷࡹࡸࡩࡤࡶ࡟ࠦࡀࠦࡣࡰࡰࡶࡸࠥࢁࠠࡣࡱࡲࡸࡸࡺࡲࡢࡲࠣࢁࠥࡃࠠࡳࡧࡴࡹ࡮ࡸࡥࠩࠩࡪࡰࡴࡨࡡ࡭࠯ࡤ࡫ࡪࡴࡴࠨࠫ࠾ࠤ࡮࡬ࠠࠩࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡨࡲࡻ࠴ࡇࡍࡑࡅࡅࡑࡥࡁࡈࡇࡑࡘࡤࡎࡔࡕࡒࡢࡔࡗࡕࡘ࡚ࠫࠣࡦࡴࡵࡴࡴࡶࡵࡥࡵ࠮ࠩ࠼ࠢࠥࠦࠧᒻ")
              bstack11111lll11_opy_ = bstack1llll1l1l_opy_.replace(bstack1llllllll11_opy_, bstack1111111111_opy_)
              with open(bstack11111l11l1_opy_, bstack111l1ll_opy_ (u"ࠩࡺࠫᒼ")) as f:
                f.write(bstack11111lll11_opy_)
    except Exception as e:
        logger.error(bstack11l1l1l111_opy_.format(str(e)))
def bstack1lll1ll11l_opy_():
  try:
    bstack1111l111l1_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1ll_opy_ (u"ࠪࡳࡵࡺࡩ࡮ࡣ࡯ࡣ࡭ࡻࡢࡠࡷࡵࡰ࠳ࡰࡳࡰࡰࠪᒽ"))
    bstack1111l1l111_opy_ = []
    if os.path.exists(bstack1111l111l1_opy_):
      with open(bstack1111l111l1_opy_) as f:
        bstack1111l1l111_opy_ = json.load(f)
      os.remove(bstack1111l111l1_opy_)
    return bstack1111l1l111_opy_
  except:
    pass
  return []
def bstack1l1l111l1l_opy_(bstack1111l1111_opy_):
  try:
    bstack1111l1l111_opy_ = []
    bstack1111l111l1_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1ll_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠴ࡪࡴࡱࡱࠫᒾ"))
    if os.path.exists(bstack1111l111l1_opy_):
      with open(bstack1111l111l1_opy_) as f:
        bstack1111l1l111_opy_ = json.load(f)
    bstack1111l1l111_opy_.append(bstack1111l1111_opy_)
    with open(bstack1111l111l1_opy_, bstack111l1ll_opy_ (u"ࠬࡽࠧᒿ")) as f:
        json.dump(bstack1111l1l111_opy_, f)
  except:
    pass
def bstack111l1ll11_opy_(logger, bstack1111lll1l1_opy_ = False):
  try:
    test_name = os.environ.get(bstack111l1ll_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩᓀ"), bstack111l1ll_opy_ (u"ࠧࠨᓁ"))
    if test_name == bstack111l1ll_opy_ (u"ࠨࠩᓂ"):
        test_name = threading.current_thread().__dict__.get(bstack111l1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡄࡧࡨࡤࡺࡥࡴࡶࡢࡲࡦࡳࡥࠨᓃ"), bstack111l1ll_opy_ (u"ࠪࠫᓄ"))
    bstack111111ll1l_opy_ = bstack111l1ll_opy_ (u"ࠫ࠱ࠦࠧᓅ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack1111lll1l1_opy_:
        bstack1l11l1111l_opy_ = os.environ.get(bstack111l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬᓆ"), bstack111l1ll_opy_ (u"࠭࠰ࠨᓇ"))
        bstack1lll1l11l1_opy_ = {bstack111l1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᓈ"): test_name, bstack111l1ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᓉ"): bstack111111ll1l_opy_, bstack111l1ll_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᓊ"): bstack1l11l1111l_opy_}
        bstack1111111l1l_opy_ = []
        bstack11111l1l11_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡴࡵࡶ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩᓋ"))
        if os.path.exists(bstack11111l1l11_opy_):
            with open(bstack11111l1l11_opy_) as f:
                bstack1111111l1l_opy_ = json.load(f)
        bstack1111111l1l_opy_.append(bstack1lll1l11l1_opy_)
        with open(bstack11111l1l11_opy_, bstack111l1ll_opy_ (u"ࠫࡼ࠭ᓌ")) as f:
            json.dump(bstack1111111l1l_opy_, f)
    else:
        bstack1lll1l11l1_opy_ = {bstack111l1ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᓍ"): test_name, bstack111l1ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᓎ"): bstack111111ll1l_opy_, bstack111l1ll_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ᓏ"): str(multiprocessing.current_process().name)}
        if bstack111l1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸࠬᓐ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1lll1l11l1_opy_)
  except Exception as e:
      logger.warn(bstack111l1ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡵࡿࡴࡦࡵࡷࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢ࠼ࠣࡿࢂࠨᓑ").format(e))
def bstack1l111l111l_opy_(error_message, test_name, index, logger):
  try:
    bstack1lllll1lll1_opy_ = []
    bstack1lll1l11l1_opy_ = {bstack111l1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨᓒ"): test_name, bstack111l1ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᓓ"): error_message, bstack111l1ll_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᓔ"): index}
    bstack1111l1l1l1_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧᓕ"))
    if os.path.exists(bstack1111l1l1l1_opy_):
        with open(bstack1111l1l1l1_opy_) as f:
            bstack1lllll1lll1_opy_ = json.load(f)
    bstack1lllll1lll1_opy_.append(bstack1lll1l11l1_opy_)
    with open(bstack1111l1l1l1_opy_, bstack111l1ll_opy_ (u"ࠧࡸࠩᓖ")) as f:
        json.dump(bstack1lllll1lll1_opy_, f)
  except Exception as e:
    logger.warn(bstack111l1ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡶࡴࡨ࡯ࡵࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧ࠺ࠡࡽࢀࠦᓗ").format(e))
def bstack1lll1llll_opy_(bstack1l11llll1l_opy_, name, logger):
  try:
    bstack1lll1l11l1_opy_ = {bstack111l1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᓘ"): name, bstack111l1ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᓙ"): bstack1l11llll1l_opy_, bstack111l1ll_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᓚ"): str(threading.current_thread()._name)}
    return bstack1lll1l11l1_opy_
  except Exception as e:
    logger.warn(bstack111l1ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡧࡷࡱࡲࡪࡲࠠࡥࡣࡷࡥ࠿ࠦࡻࡾࠤᓛ").format(e))
  return
def bstack1111ll1111_opy_():
    return platform.system() == bstack111l1ll_opy_ (u"࠭ࡗࡪࡰࡧࡳࡼࡹࠧᓜ")
def bstack11ll1111l_opy_(bstack1111111ll1_opy_, config, logger):
    bstack11111llll1_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack1111111ll1_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack111l1ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪ࡮ࡲࡴࡦࡴࠣࡧࡴࡴࡦࡪࡩࠣ࡯ࡪࡿࡳࠡࡤࡼࠤࡷ࡫ࡧࡦࡺࠣࡱࡦࡺࡣࡩ࠼ࠣࡿࢂࠨᓝ").format(e))
    return bstack11111llll1_opy_
def bstack1llllll1l11_opy_(bstack1111ll11ll_opy_, bstack1llllllllll_opy_):
    bstack1111ll1l11_opy_ = version.parse(bstack1111ll11ll_opy_)
    bstack1111lll1ll_opy_ = version.parse(bstack1llllllllll_opy_)
    if bstack1111ll1l11_opy_ > bstack1111lll1ll_opy_:
        return 1
    elif bstack1111ll1l11_opy_ < bstack1111lll1ll_opy_:
        return -1
    else:
        return 0
def bstack1l11lll1_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack1lllll1l11l_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack1llllll1lll_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1ll11111l_opy_(options, framework, bstack111lllll1_opy_={}):
    if options is None:
        return
    if getattr(options, bstack111l1ll_opy_ (u"ࠨࡩࡨࡸࠬᓞ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1l11ll1l11_opy_ = caps.get(bstack111l1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᓟ"))
    bstack1llllllll1l_opy_ = True
    bstack111111l11_opy_ = os.environ[bstack111l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᓠ")]
    if bstack1111ll1ll1_opy_(caps.get(bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫ࡗ࠴ࡅࠪᓡ"))) or bstack1111ll1ll1_opy_(caps.get(bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡠࡹ࠶ࡧࠬᓢ"))):
        bstack1llllllll1l_opy_ = False
    if bstack1l1lll1ll_opy_({bstack111l1ll_opy_ (u"ࠨࡵࡴࡧ࡚࠷ࡈࠨᓣ"): bstack1llllllll1l_opy_}):
        bstack1l11ll1l11_opy_ = bstack1l11ll1l11_opy_ or {}
        bstack1l11ll1l11_opy_[bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩᓤ")] = bstack1llllll1lll_opy_(framework)
        bstack1l11ll1l11_opy_[bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᓥ")] = bstack1111ll1l1l_opy_()
        bstack1l11ll1l11_opy_[bstack111l1ll_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᓦ")] = bstack111111l11_opy_
        bstack1l11ll1l11_opy_[bstack111l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬᓧ")] = bstack111lllll1_opy_
        if getattr(options, bstack111l1ll_opy_ (u"ࠫࡸ࡫ࡴࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷࡽࠬᓨ"), None):
            options.set_capability(bstack111l1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᓩ"), bstack1l11ll1l11_opy_)
        else:
            options[bstack111l1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᓪ")] = bstack1l11ll1l11_opy_
    else:
        if getattr(options, bstack111l1ll_opy_ (u"ࠧࡴࡧࡷࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡹࠨᓫ"), None):
            options.set_capability(bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩᓬ"), bstack1llllll1lll_opy_(framework))
            options.set_capability(bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᓭ"), bstack1111ll1l1l_opy_())
            options.set_capability(bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᓮ"), bstack111111l11_opy_)
            options.set_capability(bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬᓯ"), bstack111lllll1_opy_)
        else:
            options[bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᓰ")] = bstack1llllll1lll_opy_(framework)
            options[bstack111l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᓱ")] = bstack1111ll1l1l_opy_()
            options[bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩᓲ")] = bstack111111l11_opy_
            options[bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩᓳ")] = bstack111lllll1_opy_
    return options
def bstack1llllll111l_opy_(bstack1lllll1ll11_opy_, framework):
    bstack111lllll1_opy_ = bstack1111lll1_opy_.get_property(bstack111l1ll_opy_ (u"ࠤࡓࡐࡆ࡟ࡗࡓࡋࡊࡌ࡙ࡥࡐࡓࡑࡇ࡙ࡈ࡚࡟ࡎࡃࡓࠦᓴ"))
    if bstack1lllll1ll11_opy_ and len(bstack1lllll1ll11_opy_.split(bstack111l1ll_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩᓵ"))) > 1:
        ws_url = bstack1lllll1ll11_opy_.split(bstack111l1ll_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪᓶ"))[0]
        if bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨᓷ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack1lllllll1ll_opy_ = json.loads(urllib.parse.unquote(bstack1lllll1ll11_opy_.split(bstack111l1ll_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬᓸ"))[1]))
            bstack1lllllll1ll_opy_ = bstack1lllllll1ll_opy_ or {}
            bstack111111l11_opy_ = os.environ[bstack111l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᓹ")]
            bstack1lllllll1ll_opy_[bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩᓺ")] = str(framework) + str(__version__)
            bstack1lllllll1ll_opy_[bstack111l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᓻ")] = bstack1111ll1l1l_opy_()
            bstack1lllllll1ll_opy_[bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᓼ")] = bstack111111l11_opy_
            bstack1lllllll1ll_opy_[bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬᓽ")] = bstack111lllll1_opy_
            bstack1lllll1ll11_opy_ = bstack1lllll1ll11_opy_.split(bstack111l1ll_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫᓾ"))[0] + bstack111l1ll_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬᓿ") + urllib.parse.quote(json.dumps(bstack1lllllll1ll_opy_))
    return bstack1lllll1ll11_opy_
def bstack1ll11l111l_opy_():
    global bstack1l111ll111_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1l111ll111_opy_ = BrowserType.connect
    return bstack1l111ll111_opy_
def bstack1l1l1111ll_opy_(framework_name):
    global bstack111llllll1_opy_
    bstack111llllll1_opy_ = framework_name
    return framework_name
def bstack1l111111l1_opy_(self, *args, **kwargs):
    global bstack1l111ll111_opy_
    try:
        global bstack111llllll1_opy_
        if bstack111l1ll_opy_ (u"ࠧࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷࠫᔀ") in kwargs:
            kwargs[bstack111l1ll_opy_ (u"ࠨࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸࠬᔁ")] = bstack1llllll111l_opy_(
                kwargs.get(bstack111l1ll_opy_ (u"ࠩࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹ࠭ᔂ"), None),
                bstack111llllll1_opy_
            )
    except Exception as e:
        logger.error(bstack111l1ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡘࡊࡋࠡࡥࡤࡴࡸࡀࠠࡼࡿࠥᔃ").format(str(e)))
    return bstack1l111ll111_opy_(self, *args, **kwargs)
def bstack1111ll11l1_opy_(bstack11111l1l1l_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1l1l1l1ll_opy_(bstack11111l1l1l_opy_, bstack111l1ll_opy_ (u"ࠦࠧᔄ"))
        if proxies and proxies.get(bstack111l1ll_opy_ (u"ࠧ࡮ࡴࡵࡲࡶࠦᔅ")):
            parsed_url = urlparse(proxies.get(bstack111l1ll_opy_ (u"ࠨࡨࡵࡶࡳࡷࠧᔆ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack111l1ll_opy_ (u"ࠧࡱࡴࡲࡼࡾࡎ࡯ࡴࡶࠪᔇ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack111l1ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡰࡴࡷࠫᔈ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack111l1ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡖࡵࡨࡶࠬᔉ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack111l1ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡤࡷࡸ࠭ᔊ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1lllll1111_opy_(bstack11111l1l1l_opy_):
    bstack11111l1111_opy_ = {
        bstack111l11l11l_opy_[bstack1111l1111l_opy_]: bstack11111l1l1l_opy_[bstack1111l1111l_opy_]
        for bstack1111l1111l_opy_ in bstack11111l1l1l_opy_
        if bstack1111l1111l_opy_ in bstack111l11l11l_opy_
    }
    bstack11111l1111_opy_[bstack111l1ll_opy_ (u"ࠦࡵࡸ࡯ࡹࡻࡖࡩࡹࡺࡩ࡯ࡩࡶࠦᔋ")] = bstack1111ll11l1_opy_(bstack11111l1l1l_opy_, bstack1111lll1_opy_.get_property(bstack111l1ll_opy_ (u"ࠧࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠧᔌ")))
    bstack1llllll1ll1_opy_ = [element.lower() for element in bstack111l111l1l_opy_]
    bstack111111l1l1_opy_(bstack11111l1111_opy_, bstack1llllll1ll1_opy_)
    return bstack11111l1111_opy_
def bstack111111l1l1_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack111l1ll_opy_ (u"ࠨࠪࠫࠬ࠭ࠦᔍ")
    for value in d.values():
        if isinstance(value, dict):
            bstack111111l1l1_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack111111l1l1_opy_(item, keys)