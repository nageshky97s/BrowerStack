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
import datetime
import inspect
import logging
import os
import signal
import threading
from uuid import uuid4
from bstack_utils.percy_sdk import PercySDK
import tempfile
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack1111l1l1l_opy_, bstack111l11l1l_opy_, update, bstack1111lll1l_opy_,
                                       bstack11ll1llll1_opy_, bstack1lll111lll_opy_, bstack11ll1ll111_opy_, bstack11ll1l1111_opy_,
                                       bstack11l111ll1l_opy_, bstack111ll1lll_opy_, bstack1lll111l1_opy_, bstack1l111l1l11_opy_,
                                       bstack1ll1ll1lll_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack11llllll11_opy_)
from browserstack_sdk.bstack1111ll1l_opy_ import bstack111l111l_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack1llllll1l1_opy_
from bstack_utils.capture import bstack1ll1ll1l_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack1ll1l11lll_opy_, bstack1l1ll11ll1_opy_, bstack11l1111ll1_opy_, \
    bstack11l1ll1ll1_opy_
from bstack_utils.helper import bstack1ll111l1_opy_, bstack1lllll1l11l_opy_, bstack1l11lll1_opy_, bstack1l1ll11l1_opy_, bstack1111ll1l1l_opy_, bstack1l1lllll_opy_, \
    bstack1111l11111_opy_, \
    bstack11111l111l_opy_, bstack11lll1111_opy_, bstack1ll1111ll1_opy_, bstack1111llll11_opy_, bstack1l1lll111l_opy_, Notset, \
    bstack1l1lll1ll_opy_, bstack1111l11l1l_opy_, bstack1111l1l11l_opy_, Result, bstack1lllll1l1ll_opy_, bstack11111111l1_opy_, bstack11l1111l_opy_, \
    bstack1l1l111l1l_opy_, bstack111l1ll11_opy_, bstack1l1l111lll_opy_, bstack1111ll1111_opy_
from bstack_utils.bstack1llll1l1lll_opy_ import bstack1llll1lll11_opy_
from bstack_utils.messages import bstack1lll1ll11_opy_, bstack1ll11l1ll1_opy_, bstack1llllll111_opy_, bstack1lll11111l_opy_, bstack1llllll1l_opy_, \
    bstack11l1l1l111_opy_, bstack1l11111l1_opy_, bstack1lllllllll_opy_, bstack1ll1l11l11_opy_, bstack111ll11ll_opy_, \
    bstack1lll11lll_opy_, bstack1l1ll11l1l_opy_
from bstack_utils.proxy import bstack111111ll1_opy_, bstack11111l1ll_opy_
from bstack_utils.bstack1l11ll111l_opy_ import bstack1ll1lll1ll1_opy_, bstack1ll1lll1111_opy_, bstack1ll1ll1lll1_opy_, bstack1ll1lll1l11_opy_, \
    bstack1ll1lll111l_opy_, bstack1ll1ll1llll_opy_, bstack1ll1llll111_opy_, bstack11l1ll1ll_opy_, bstack1ll1lll1lll_opy_
from bstack_utils.bstack1ll111l1ll_opy_ import bstack11l11l1ll1_opy_
from bstack_utils.bstack1l1l1l11ll_opy_ import bstack1l11ll1ll1_opy_, bstack1l1ll1l111_opy_, bstack1ll1lll1l_opy_, \
    bstack11ll111l1l_opy_, bstack1l1l1lll1l_opy_
from bstack_utils.bstack1lll1ll1_opy_ import bstack1lll1111_opy_
from bstack_utils.bstack1ll11l11_opy_ import bstack1l1l1l11_opy_
import bstack_utils.bstack111ll1ll_opy_ as bstack1111111l_opy_
from bstack_utils.bstack1l1lll11_opy_ import bstack1ll11l1l_opy_
from bstack_utils.bstack1ll1l1l11l_opy_ import bstack1ll1l1l11l_opy_
from browserstack_sdk.__init__ import bstack11ll11ll1l_opy_
bstack1ll11ll11_opy_ = None
bstack11ll11lll1_opy_ = None
bstack1l1111lll1_opy_ = None
bstack1l1ll1ll1l_opy_ = None
bstack1ll11ll111_opy_ = None
bstack1l11l11l1_opy_ = None
bstack1ll11l1l11_opy_ = None
bstack1l1111llll_opy_ = None
bstack11lll1lll1_opy_ = None
bstack1llll1111l_opy_ = None
bstack11l11lll1l_opy_ = None
bstack1l1l11111l_opy_ = None
bstack1ll111lll1_opy_ = None
bstack111llllll1_opy_ = bstack111l1ll_opy_ (u"ࠨࠩᠻ")
CONFIG = {}
bstack1l11l1111_opy_ = False
bstack11111l1l1_opy_ = bstack111l1ll_opy_ (u"ࠩࠪᠼ")
bstack1l111ll1l_opy_ = bstack111l1ll_opy_ (u"ࠪࠫᠽ")
bstack11l11l1l11_opy_ = False
bstack1ll111l11l_opy_ = []
bstack1lllllll1l_opy_ = bstack1ll1l11lll_opy_
bstack1l1llll1lll_opy_ = bstack111l1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᠾ")
bstack1lllll111l_opy_ = {}
bstack11ll1ll1l_opy_ = False
logger = bstack1llllll1l1_opy_.get_logger(__name__, bstack1lllllll1l_opy_)
store = {
    bstack111l1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᠿ"): []
}
bstack1ll111l111l_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_11l1l1ll_opy_ = {}
current_test_uuid = None
def bstack1l1lll1l1_opy_(page, bstack11l111111_opy_):
    try:
        page.evaluate(bstack111l1ll_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᡀ"),
                      bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠫᡁ") + json.dumps(
                          bstack11l111111_opy_) + bstack111l1ll_opy_ (u"ࠣࡿࢀࠦᡂ"))
    except Exception as e:
        print(bstack111l1ll_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤࢀࢃࠢᡃ"), e)
def bstack11l1111l1_opy_(page, message, level):
    try:
        page.evaluate(bstack111l1ll_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦᡄ"), bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩᡅ") + json.dumps(
            message) + bstack111l1ll_opy_ (u"ࠬ࠲ࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠨᡆ") + json.dumps(level) + bstack111l1ll_opy_ (u"࠭ࡽࡾࠩᡇ"))
    except Exception as e:
        print(bstack111l1ll_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡥࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠠࡼࡿࠥᡈ"), e)
def pytest_configure(config):
    bstack1111lll1_opy_ = Config.bstack11111lll_opy_()
    config.args = bstack1l1l1l11_opy_.bstack1ll111l1l11_opy_(config.args)
    bstack1111lll1_opy_.bstack1ll111111_opy_(bstack1l1l111lll_opy_(config.getoption(bstack111l1ll_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬᡉ"))))
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    bstack1ll1111111l_opy_ = item.config.getoption(bstack111l1ll_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᡊ"))
    plugins = item.config.getoption(bstack111l1ll_opy_ (u"ࠥࡴࡱࡻࡧࡪࡰࡶࠦᡋ"))
    report = outcome.get_result()
    bstack1ll1111l111_opy_(item, call, report)
    if bstack111l1ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡳࡰࡺ࡭ࡩ࡯ࠤᡌ") not in plugins or bstack1l1lll111l_opy_():
        return
    summary = []
    driver = getattr(item, bstack111l1ll_opy_ (u"ࠧࡥࡤࡳ࡫ࡹࡩࡷࠨᡍ"), None)
    page = getattr(item, bstack111l1ll_opy_ (u"ࠨ࡟ࡱࡣࡪࡩࠧᡎ"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None):
        bstack1ll1111llll_opy_(item, report, summary, bstack1ll1111111l_opy_)
    if (page is not None):
        bstack1l1llllll11_opy_(item, report, summary, bstack1ll1111111l_opy_)
def bstack1ll1111llll_opy_(item, report, summary, bstack1ll1111111l_opy_):
    if report.when == bstack111l1ll_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ᡏ") and report.skipped:
        bstack1ll1lll1lll_opy_(report)
    if report.when in [bstack111l1ll_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢᡐ"), bstack111l1ll_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦᡑ")]:
        return
    if not bstack1111ll1l1l_opy_():
        return
    try:
        if (str(bstack1ll1111111l_opy_).lower() != bstack111l1ll_opy_ (u"ࠪࡸࡷࡻࡥࠨᡒ")):
            item._driver.execute_script(
                bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩᡓ") + json.dumps(
                    report.nodeid) + bstack111l1ll_opy_ (u"ࠬࢃࡽࠨᡔ"))
        os.environ[bstack111l1ll_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩᡕ")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack111l1ll_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦ࠼ࠣࡿ࠵ࢃࠢᡖ").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack111l1ll_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥᡗ")))
    bstack111ll1111_opy_ = bstack111l1ll_opy_ (u"ࠤࠥᡘ")
    bstack1ll1lll1lll_opy_(report)
    if not passed:
        try:
            bstack111ll1111_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack111l1ll_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡸࡥࡢࡵࡲࡲ࠿ࠦࡻ࠱ࡿࠥᡙ").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack111ll1111_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack111l1ll_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨᡚ")))
        bstack111ll1111_opy_ = bstack111l1ll_opy_ (u"ࠧࠨᡛ")
        if not passed:
            try:
                bstack111ll1111_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack111l1ll_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡴࡨࡥࡸࡵ࡮࠻ࠢࡾ࠴ࢂࠨᡜ").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack111ll1111_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack111l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡨࡦࡺࡡࠣ࠼ࠣࠫᡝ")
                    + json.dumps(bstack111l1ll_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠢࠤᡞ"))
                    + bstack111l1ll_opy_ (u"ࠤ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࠧᡟ")
                )
            else:
                item._driver.execute_script(
                    bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡥࡣࡷࡥࠧࡀࠠࠨᡠ")
                    + json.dumps(str(bstack111ll1111_opy_))
                    + bstack111l1ll_opy_ (u"ࠦࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࠢᡡ")
                )
        except Exception as e:
            summary.append(bstack111l1ll_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡥࡳࡴ࡯ࡵࡣࡷࡩ࠿ࠦࡻ࠱ࡿࠥᡢ").format(e))
def bstack1ll11111l11_opy_(test_name, error_message):
    try:
        bstack1ll111l1111_opy_ = []
        bstack1l11l1111l_opy_ = os.environ.get(bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᡣ"), bstack111l1ll_opy_ (u"ࠧ࠱ࠩᡤ"))
        bstack1lll1l11l1_opy_ = {bstack111l1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᡥ"): test_name, bstack111l1ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᡦ"): error_message, bstack111l1ll_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᡧ"): bstack1l11l1111l_opy_}
        bstack1ll1111l11l_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1ll_opy_ (u"ࠫࡵࡽ࡟ࡱࡻࡷࡩࡸࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩᡨ"))
        if os.path.exists(bstack1ll1111l11l_opy_):
            with open(bstack1ll1111l11l_opy_) as f:
                bstack1ll111l1111_opy_ = json.load(f)
        bstack1ll111l1111_opy_.append(bstack1lll1l11l1_opy_)
        with open(bstack1ll1111l11l_opy_, bstack111l1ll_opy_ (u"ࠬࡽࠧᡩ")) as f:
            json.dump(bstack1ll111l1111_opy_, f)
    except Exception as e:
        logger.debug(bstack111l1ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡨࡶࡸ࡯ࡳࡵ࡫ࡱ࡫ࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡳࡽࡹ࡫ࡳࡵࠢࡨࡶࡷࡵࡲࡴ࠼ࠣࠫᡪ") + str(e))
def bstack1l1llllll11_opy_(item, report, summary, bstack1ll1111111l_opy_):
    if report.when in [bstack111l1ll_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨᡫ"), bstack111l1ll_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥᡬ")]:
        return
    if (str(bstack1ll1111111l_opy_).lower() != bstack111l1ll_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᡭ")):
        bstack1l1lll1l1_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack111l1ll_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧᡮ")))
    bstack111ll1111_opy_ = bstack111l1ll_opy_ (u"ࠦࠧᡯ")
    bstack1ll1lll1lll_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack111ll1111_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack111l1ll_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡳࡧࡤࡷࡴࡴ࠺ࠡࡽ࠳ࢁࠧᡰ").format(e)
                )
        try:
            if passed:
                bstack1l1l1lll1l_opy_(getattr(item, bstack111l1ll_opy_ (u"࠭࡟ࡱࡣࡪࡩࠬᡱ"), None), bstack111l1ll_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢᡲ"))
            else:
                error_message = bstack111l1ll_opy_ (u"ࠨࠩᡳ")
                if bstack111ll1111_opy_:
                    bstack11l1111l1_opy_(item._page, str(bstack111ll1111_opy_), bstack111l1ll_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣᡴ"))
                    bstack1l1l1lll1l_opy_(getattr(item, bstack111l1ll_opy_ (u"ࠪࡣࡵࡧࡧࡦࠩᡵ"), None), bstack111l1ll_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦᡶ"), str(bstack111ll1111_opy_))
                    error_message = str(bstack111ll1111_opy_)
                else:
                    bstack1l1l1lll1l_opy_(getattr(item, bstack111l1ll_opy_ (u"ࠬࡥࡰࡢࡩࡨࠫᡷ"), None), bstack111l1ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨᡸ"))
                bstack1ll11111l11_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack111l1ll_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡻࡰࡥࡣࡷࡩࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࡀࠠࡼ࠲ࢀࠦ᡹").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstack111l1ll_opy_ (u"ࠣ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ᡺"), default=bstack111l1ll_opy_ (u"ࠤࡉࡥࡱࡹࡥࠣ᡻"), help=bstack111l1ll_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡨࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠤ᡼"))
    parser.addoption(bstack111l1ll_opy_ (u"ࠦ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥ᡽"), default=bstack111l1ll_opy_ (u"ࠧࡌࡡ࡭ࡵࡨࠦ᡾"), help=bstack111l1ll_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡩࡤࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠧ᡿"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack111l1ll_opy_ (u"ࠢ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠤᢀ"), action=bstack111l1ll_opy_ (u"ࠣࡵࡷࡳࡷ࡫ࠢᢁ"), default=bstack111l1ll_opy_ (u"ࠤࡦ࡬ࡷࡵ࡭ࡦࠤᢂ"),
                         help=bstack111l1ll_opy_ (u"ࠥࡈࡷ࡯ࡶࡦࡴࠣࡸࡴࠦࡲࡶࡰࠣࡸࡪࡹࡴࡴࠤᢃ"))
def bstack1ll11111_opy_(log):
    if not (log[bstack111l1ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᢄ")] and log[bstack111l1ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᢅ")].strip()):
        return
    active = bstack1ll11lll_opy_()
    log = {
        bstack111l1ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᢆ"): log[bstack111l1ll_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᢇ")],
        bstack111l1ll_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫᢈ"): bstack1l11lll1_opy_().isoformat() + bstack111l1ll_opy_ (u"ࠩ࡝ࠫᢉ"),
        bstack111l1ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᢊ"): log[bstack111l1ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᢋ")],
    }
    if active:
        if active[bstack111l1ll_opy_ (u"ࠬࡺࡹࡱࡧࠪᢌ")] == bstack111l1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᢍ"):
            log[bstack111l1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᢎ")] = active[bstack111l1ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᢏ")]
        elif active[bstack111l1ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᢐ")] == bstack111l1ll_opy_ (u"ࠪࡸࡪࡹࡴࠨᢑ"):
            log[bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᢒ")] = active[bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᢓ")]
    bstack1ll11l1l_opy_.bstack1l1l1ll1_opy_([log])
def bstack1ll11lll_opy_():
    if len(store[bstack111l1ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᢔ")]) > 0 and store[bstack111l1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᢕ")][-1]:
        return {
            bstack111l1ll_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᢖ"): bstack111l1ll_opy_ (u"ࠩ࡫ࡳࡴࡱࠧᢗ"),
            bstack111l1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᢘ"): store[bstack111l1ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᢙ")][-1]
        }
    if store.get(bstack111l1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᢚ"), None):
        return {
            bstack111l1ll_opy_ (u"࠭ࡴࡺࡲࡨࠫᢛ"): bstack111l1ll_opy_ (u"ࠧࡵࡧࡶࡸࠬᢜ"),
            bstack111l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᢝ"): store[bstack111l1ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᢞ")]
        }
    return None
bstack1lll111l_opy_ = bstack1ll1ll1l_opy_(bstack1ll11111_opy_)
def pytest_runtest_call(item):
    try:
        global CONFIG
        item._1l1lllll1ll_opy_ = True
        bstack1l11llllll_opy_ = bstack1111111l_opy_.bstack1l111l1l1l_opy_(bstack11111l111l_opy_(item.own_markers))
        item._a11y_test_case = bstack1l11llllll_opy_
        if bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᢟ"), None):
            driver = getattr(item, bstack111l1ll_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬᢠ"), None)
            item._a11y_started = bstack1111111l_opy_.bstack11l111l1l_opy_(driver, bstack1l11llllll_opy_)
        if not bstack1ll11l1l_opy_.on() or bstack1l1llll1lll_opy_ != bstack111l1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᢡ"):
            return
        global current_test_uuid, bstack1lll111l_opy_
        bstack1lll111l_opy_.start()
        bstack11l11l11_opy_ = {
            bstack111l1ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᢢ"): uuid4().__str__(),
            bstack111l1ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᢣ"): bstack1l11lll1_opy_().isoformat() + bstack111l1ll_opy_ (u"ࠨ࡜ࠪᢤ")
        }
        current_test_uuid = bstack11l11l11_opy_[bstack111l1ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᢥ")]
        store[bstack111l1ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᢦ")] = bstack11l11l11_opy_[bstack111l1ll_opy_ (u"ࠫࡺࡻࡩࡥࠩᢧ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _11l1l1ll_opy_[item.nodeid] = {**_11l1l1ll_opy_[item.nodeid], **bstack11l11l11_opy_}
        bstack1ll111l11l1_opy_(item, _11l1l1ll_opy_[item.nodeid], bstack111l1ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᢨ"))
    except Exception as err:
        print(bstack111l1ll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡸࡵ࡯ࡶࡨࡷࡹࡥࡣࡢ࡮࡯࠾ࠥࢁࡽࠨᢩ"), str(err))
def pytest_runtest_setup(item):
    global bstack1ll111l111l_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack1111llll11_opy_():
        atexit.register(bstack11lll1ll1_opy_)
        if not bstack1ll111l111l_opy_:
            try:
                bstack1l1llllllll_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack1111ll1111_opy_():
                    bstack1l1llllllll_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1l1llllllll_opy_:
                    signal.signal(s, bstack1l1llllll1l_opy_)
                bstack1ll111l111l_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack111l1ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩ࡬࡯ࡳࡵࡧࡵࠤࡸ࡯ࡧ࡯ࡣ࡯ࠤ࡭ࡧ࡮ࡥ࡮ࡨࡶࡸࡀࠠࠣᢪ") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack1ll1lll1ll1_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack111l1ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ᢫")
    try:
        if not bstack1ll11l1l_opy_.on():
            return
        bstack1lll111l_opy_.start()
        uuid = uuid4().__str__()
        bstack11l11l11_opy_ = {
            bstack111l1ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ᢬"): uuid,
            bstack111l1ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ᢭"): bstack1l11lll1_opy_().isoformat() + bstack111l1ll_opy_ (u"ࠫ࡟࠭᢮"),
            bstack111l1ll_opy_ (u"ࠬࡺࡹࡱࡧࠪ᢯"): bstack111l1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᢰ"),
            bstack111l1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪᢱ"): bstack111l1ll_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭ᢲ"),
            bstack111l1ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬᢳ"): bstack111l1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᢴ")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack111l1ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨᢵ")] = item
        store[bstack111l1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᢶ")] = [uuid]
        if not _11l1l1ll_opy_.get(item.nodeid, None):
            _11l1l1ll_opy_[item.nodeid] = {bstack111l1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᢷ"): [], bstack111l1ll_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩᢸ"): []}
        _11l1l1ll_opy_[item.nodeid][bstack111l1ll_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᢹ")].append(bstack11l11l11_opy_[bstack111l1ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᢺ")])
        _11l1l1ll_opy_[item.nodeid + bstack111l1ll_opy_ (u"ࠪ࠱ࡸ࡫ࡴࡶࡲࠪᢻ")] = bstack11l11l11_opy_
        bstack1ll111l11ll_opy_(item, bstack11l11l11_opy_, bstack111l1ll_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᢼ"))
    except Exception as err:
        print(bstack111l1ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡷࡻ࡮ࡵࡧࡶࡸࡤࡹࡥࡵࡷࡳ࠾ࠥࢁࡽࠨᢽ"), str(err))
def pytest_runtest_teardown(item):
    try:
        global bstack1lllll111l_opy_
        bstack1l11l1111l_opy_ = 0
        if bstack11l11l1l11_opy_ is True:
            bstack1l11l1111l_opy_ = int(os.environ.get(bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᢾ")))
        if bstack1l111l1111_opy_.bstack1ll11lll11_opy_() == bstack111l1ll_opy_ (u"ࠢࡵࡴࡸࡩࠧᢿ"):
            if bstack1l111l1111_opy_.bstack1111l1ll1_opy_() == bstack111l1ll_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥᣀ"):
                bstack1l1lllll1l1_opy_ = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᣁ"), None)
                bstack1l1ll1ll11_opy_ = bstack1l1lllll1l1_opy_ + bstack111l1ll_opy_ (u"ࠥ࠱ࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᣂ")
                driver = getattr(item, bstack111l1ll_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬᣃ"), None)
                bstack1111111ll_opy_ = getattr(item, bstack111l1ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᣄ"), None)
                bstack1l1l1ll1l1_opy_ = getattr(item, bstack111l1ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᣅ"), None)
                PercySDK.screenshot(driver, bstack1l1ll1ll11_opy_, bstack1111111ll_opy_=bstack1111111ll_opy_, bstack1l1l1ll1l1_opy_=bstack1l1l1ll1l1_opy_, bstack11ll1lll1l_opy_=bstack1l11l1111l_opy_)
        if getattr(item, bstack111l1ll_opy_ (u"ࠧࡠࡣ࠴࠵ࡾࡥࡳࡵࡣࡵࡸࡪࡪࠧᣆ"), False):
            bstack111l111l_opy_.bstack111llll1_opy_(getattr(item, bstack111l1ll_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩᣇ"), None), bstack1lllll111l_opy_, logger, item)
        if not bstack1ll11l1l_opy_.on():
            return
        bstack11l11l11_opy_ = {
            bstack111l1ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᣈ"): uuid4().__str__(),
            bstack111l1ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᣉ"): bstack1l11lll1_opy_().isoformat() + bstack111l1ll_opy_ (u"ࠫ࡟࠭ᣊ"),
            bstack111l1ll_opy_ (u"ࠬࡺࡹࡱࡧࠪᣋ"): bstack111l1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᣌ"),
            bstack111l1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪᣍ"): bstack111l1ll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᣎ"),
            bstack111l1ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬᣏ"): bstack111l1ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬᣐ")
        }
        _11l1l1ll_opy_[item.nodeid + bstack111l1ll_opy_ (u"ࠫ࠲ࡺࡥࡢࡴࡧࡳࡼࡴࠧᣑ")] = bstack11l11l11_opy_
        bstack1ll111l11ll_opy_(item, bstack11l11l11_opy_, bstack111l1ll_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᣒ"))
    except Exception as err:
        print(bstack111l1ll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡸࡵ࡯ࡶࡨࡷࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮࠻ࠢࡾࢁࠬᣓ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if not bstack1ll11l1l_opy_.on():
        yield
        return
    start_time = datetime.datetime.now()
    if bstack1ll1lll1l11_opy_(fixturedef.argname):
        store[bstack111l1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠ࡯ࡲࡨࡺࡲࡥࡠ࡫ࡷࡩࡲ࠭ᣔ")] = request.node
    elif bstack1ll1lll111l_opy_(fixturedef.argname):
        store[bstack111l1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡦࡰࡦࡹࡳࡠ࡫ࡷࡩࡲ࠭ᣕ")] = request.node
    outcome = yield
    try:
        fixture = {
            bstack111l1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᣖ"): fixturedef.argname,
            bstack111l1ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᣗ"): bstack1111l11111_opy_(outcome),
            bstack111l1ll_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ᣘ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack111l1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩᣙ")]
        if not _11l1l1ll_opy_.get(current_test_item.nodeid, None):
            _11l1l1ll_opy_[current_test_item.nodeid] = {bstack111l1ll_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨᣚ"): []}
        _11l1l1ll_opy_[current_test_item.nodeid][bstack111l1ll_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩᣛ")].append(fixture)
    except Exception as err:
        logger.debug(bstack111l1ll_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡵࡨࡸࡺࡶ࠺ࠡࡽࢀࠫᣜ"), str(err))
if bstack1l1lll111l_opy_() and bstack1ll11l1l_opy_.on():
    def pytest_bdd_before_step(request, step):
        try:
            _11l1l1ll_opy_[request.node.nodeid][bstack111l1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᣝ")].bstack1lll1l11_opy_(id(step))
        except Exception as err:
            print(bstack111l1ll_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳ࠾ࠥࢁࡽࠨᣞ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        try:
            _11l1l1ll_opy_[request.node.nodeid][bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᣟ")].bstack1l1ll1l1_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack111l1ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡵࡷࡩࡵࡥࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠩᣠ"), str(err))
    def pytest_bdd_after_step(request, step):
        try:
            bstack1lll1ll1_opy_: bstack1lll1111_opy_ = _11l1l1ll_opy_[request.node.nodeid][bstack111l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩᣡ")]
            bstack1lll1ll1_opy_.bstack1l1ll1l1_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack111l1ll_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡷࡹ࡫ࡰࡠࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠫᣢ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1l1llll1lll_opy_
        try:
            if not bstack1ll11l1l_opy_.on() or bstack1l1llll1lll_opy_ != bstack111l1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬᣣ"):
                return
            global bstack1lll111l_opy_
            bstack1lll111l_opy_.start()
            driver = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨᣤ"), None)
            if not _11l1l1ll_opy_.get(request.node.nodeid, None):
                _11l1l1ll_opy_[request.node.nodeid] = {}
            bstack1lll1ll1_opy_ = bstack1lll1111_opy_.bstack1ll1l11llll_opy_(
                scenario, feature, request.node,
                name=bstack1ll1ll1llll_opy_(request.node, scenario),
                bstack1l1ll111_opy_=bstack1l1lllll_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack111l1ll_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶ࠰ࡧࡺࡩࡵ࡮ࡤࡨࡶࠬᣥ"),
                tags=bstack1ll1llll111_opy_(feature, scenario),
                bstack1llll111_opy_=bstack1ll11l1l_opy_.bstack1lll1l1l_opy_(driver) if driver and driver.session_id else {}
            )
            _11l1l1ll_opy_[request.node.nodeid][bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᣦ")] = bstack1lll1ll1_opy_
            bstack1ll11111111_opy_(bstack1lll1ll1_opy_.uuid)
            bstack1ll11l1l_opy_.bstack1ll1l11l_opy_(bstack111l1ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᣧ"), bstack1lll1ll1_opy_)
        except Exception as err:
            print(bstack111l1ll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲ࠾ࠥࢁࡽࠨᣨ"), str(err))
def bstack1l1lllll11l_opy_(bstack1l1ll11l_opy_):
    if bstack1l1ll11l_opy_ in store[bstack111l1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᣩ")]:
        store[bstack111l1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᣪ")].remove(bstack1l1ll11l_opy_)
def bstack1ll11111111_opy_(bstack1ll1llll_opy_):
    store[bstack111l1ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᣫ")] = bstack1ll1llll_opy_
    threading.current_thread().current_test_uuid = bstack1ll1llll_opy_
@bstack1ll11l1l_opy_.bstack1ll11lll111_opy_
def bstack1ll1111l111_opy_(item, call, report):
    global bstack1l1llll1lll_opy_
    bstack1111lllll_opy_ = bstack1l1lllll_opy_()
    if hasattr(report, bstack111l1ll_opy_ (u"ࠪࡷࡹࡵࡰࠨᣬ")):
        bstack1111lllll_opy_ = bstack1lllll1l1ll_opy_(report.stop)
    elif hasattr(report, bstack111l1ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࠪᣭ")):
        bstack1111lllll_opy_ = bstack1lllll1l1ll_opy_(report.start)
    try:
        if getattr(report, bstack111l1ll_opy_ (u"ࠬࡽࡨࡦࡰࠪᣮ"), bstack111l1ll_opy_ (u"࠭ࠧᣯ")) == bstack111l1ll_opy_ (u"ࠧࡤࡣ࡯ࡰࠬᣰ"):
            bstack1lll111l_opy_.reset()
        if getattr(report, bstack111l1ll_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭ᣱ"), bstack111l1ll_opy_ (u"ࠩࠪᣲ")) == bstack111l1ll_opy_ (u"ࠪࡧࡦࡲ࡬ࠨᣳ"):
            if bstack1l1llll1lll_opy_ == bstack111l1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᣴ"):
                _11l1l1ll_opy_[item.nodeid][bstack111l1ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᣵ")] = bstack1111lllll_opy_
                bstack1ll111l11l1_opy_(item, _11l1l1ll_opy_[item.nodeid], bstack111l1ll_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ᣶"), report, call)
                store[bstack111l1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ᣷")] = None
            elif bstack1l1llll1lll_opy_ == bstack111l1ll_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧ᣸"):
                bstack1lll1ll1_opy_ = _11l1l1ll_opy_[item.nodeid][bstack111l1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ᣹")]
                bstack1lll1ll1_opy_.set(hooks=_11l1l1ll_opy_[item.nodeid].get(bstack111l1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ᣺"), []))
                exception, bstack1ll1lll1_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack1ll1lll1_opy_ = [call.excinfo.exconly(), getattr(report, bstack111l1ll_opy_ (u"ࠫࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠪ᣻"), bstack111l1ll_opy_ (u"ࠬ࠭᣼"))]
                bstack1lll1ll1_opy_.stop(time=bstack1111lllll_opy_, result=Result(result=getattr(report, bstack111l1ll_opy_ (u"࠭࡯ࡶࡶࡦࡳࡲ࡫ࠧ᣽"), bstack111l1ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ᣾")), exception=exception, bstack1ll1lll1_opy_=bstack1ll1lll1_opy_))
                bstack1ll11l1l_opy_.bstack1ll1l11l_opy_(bstack111l1ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ᣿"), _11l1l1ll_opy_[item.nodeid][bstack111l1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᤀ")])
        elif getattr(report, bstack111l1ll_opy_ (u"ࠪࡻ࡭࡫࡮ࠨᤁ"), bstack111l1ll_opy_ (u"ࠫࠬᤂ")) in [bstack111l1ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᤃ"), bstack111l1ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨᤄ")]:
            bstack1l1lll1l_opy_ = item.nodeid + bstack111l1ll_opy_ (u"ࠧ࠮ࠩᤅ") + getattr(report, bstack111l1ll_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭ᤆ"), bstack111l1ll_opy_ (u"ࠩࠪᤇ"))
            if getattr(report, bstack111l1ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᤈ"), False):
                hook_type = bstack111l1ll_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩᤉ") if getattr(report, bstack111l1ll_opy_ (u"ࠬࡽࡨࡦࡰࠪᤊ"), bstack111l1ll_opy_ (u"࠭ࠧᤋ")) == bstack111l1ll_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ᤌ") else bstack111l1ll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᤍ")
                _11l1l1ll_opy_[bstack1l1lll1l_opy_] = {
                    bstack111l1ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᤎ"): uuid4().__str__(),
                    bstack111l1ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᤏ"): bstack1111lllll_opy_,
                    bstack111l1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᤐ"): hook_type
                }
            _11l1l1ll_opy_[bstack1l1lll1l_opy_][bstack111l1ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᤑ")] = bstack1111lllll_opy_
            bstack1l1lllll11l_opy_(_11l1l1ll_opy_[bstack1l1lll1l_opy_][bstack111l1ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᤒ")])
            bstack1ll111l11ll_opy_(item, _11l1l1ll_opy_[bstack1l1lll1l_opy_], bstack111l1ll_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᤓ"), report, call)
            if getattr(report, bstack111l1ll_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭ᤔ"), bstack111l1ll_opy_ (u"ࠩࠪᤕ")) == bstack111l1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᤖ"):
                if getattr(report, bstack111l1ll_opy_ (u"ࠫࡴࡻࡴࡤࡱࡰࡩࠬᤗ"), bstack111l1ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᤘ")) == bstack111l1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᤙ"):
                    bstack11l11l11_opy_ = {
                        bstack111l1ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᤚ"): uuid4().__str__(),
                        bstack111l1ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᤛ"): bstack1l1lllll_opy_(),
                        bstack111l1ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᤜ"): bstack1l1lllll_opy_()
                    }
                    _11l1l1ll_opy_[item.nodeid] = {**_11l1l1ll_opy_[item.nodeid], **bstack11l11l11_opy_}
                    bstack1ll111l11l1_opy_(item, _11l1l1ll_opy_[item.nodeid], bstack111l1ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᤝ"))
                    bstack1ll111l11l1_opy_(item, _11l1l1ll_opy_[item.nodeid], bstack111l1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᤞ"), report, call)
    except Exception as err:
        print(bstack111l1ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡧ࡮ࡥ࡮ࡨࡣࡴ࠷࠱ࡺࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡀࠠࡼࡿࠪ᤟"), str(err))
def bstack1l1lllllll1_opy_(test, bstack11l11l11_opy_, result=None, call=None, bstack11l1111111_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1lll1ll1_opy_ = {
        bstack111l1ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᤠ"): bstack11l11l11_opy_[bstack111l1ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᤡ")],
        bstack111l1ll_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᤢ"): bstack111l1ll_opy_ (u"ࠩࡷࡩࡸࡺࠧᤣ"),
        bstack111l1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨᤤ"): test.name,
        bstack111l1ll_opy_ (u"ࠫࡧࡵࡤࡺࠩᤥ"): {
            bstack111l1ll_opy_ (u"ࠬࡲࡡ࡯ࡩࠪᤦ"): bstack111l1ll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ᤧ"),
            bstack111l1ll_opy_ (u"ࠧࡤࡱࡧࡩࠬᤨ"): inspect.getsource(test.obj)
        },
        bstack111l1ll_opy_ (u"ࠨ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᤩ"): test.name,
        bstack111l1ll_opy_ (u"ࠩࡶࡧࡴࡶࡥࠨᤪ"): test.name,
        bstack111l1ll_opy_ (u"ࠪࡷࡨࡵࡰࡦࡵࠪᤫ"): bstack1l1l1l11_opy_.bstack1l11l1l1_opy_(test),
        bstack111l1ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ᤬"): file_path,
        bstack111l1ll_opy_ (u"ࠬࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠧ᤭"): file_path,
        bstack111l1ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭᤮"): bstack111l1ll_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨ᤯"),
        bstack111l1ll_opy_ (u"ࠨࡸࡦࡣ࡫࡯࡬ࡦࡲࡤࡸ࡭࠭ᤰ"): file_path,
        bstack111l1ll_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᤱ"): bstack11l11l11_opy_[bstack111l1ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᤲ")],
        bstack111l1ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᤳ"): bstack111l1ll_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸࠬᤴ"),
        bstack111l1ll_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡘࡥࡳࡷࡱࡔࡦࡸࡡ࡮ࠩᤵ"): {
            bstack111l1ll_opy_ (u"ࠧࡳࡧࡵࡹࡳࡥ࡮ࡢ࡯ࡨࠫᤶ"): test.nodeid
        },
        bstack111l1ll_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ᤷ"): bstack11111l111l_opy_(test.own_markers)
    }
    if bstack11l1111111_opy_ in [bstack111l1ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖ࡯࡮ࡶࡰࡦࡦࠪᤸ"), bstack111l1ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨ᤹ࠬ")]:
        bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"ࠫࡲ࡫ࡴࡢࠩ᤺")] = {
            bstack111l1ll_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹ᤻ࠧ"): bstack11l11l11_opy_.get(bstack111l1ll_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨ᤼"), [])
        }
    if bstack11l1111111_opy_ == bstack111l1ll_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨ᤽"):
        bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ᤾")] = bstack111l1ll_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ᤿")
        bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ᥀")] = bstack11l11l11_opy_[bstack111l1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ᥁")]
        bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ᥂")] = bstack11l11l11_opy_[bstack111l1ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ᥃")]
    if result:
        bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ᥄")] = result.outcome
        bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩ᥅")] = result.duration * 1000
        bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ᥆")] = bstack11l11l11_opy_[bstack111l1ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ᥇")]
        if result.failed:
            bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪ᥈")] = bstack1ll11l1l_opy_.bstack1lllll1l1_opy_(call.excinfo.typename)
            bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭᥉")] = bstack1ll11l1l_opy_.bstack1ll11l1ll11_opy_(call.excinfo, result)
        bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬ᥊")] = bstack11l11l11_opy_[bstack111l1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭᥋")]
    if outcome:
        bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ᥌")] = bstack1111l11111_opy_(outcome)
        bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪ᥍")] = 0
        bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ᥎")] = bstack11l11l11_opy_[bstack111l1ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ᥏")]
        if bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᥐ")] == bstack111l1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᥑ"):
            bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭ᥒ")] = bstack111l1ll_opy_ (u"ࠨࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠩᥓ")  # bstack1l1llll1ll1_opy_
            bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪᥔ")] = [{bstack111l1ll_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ᥕ"): [bstack111l1ll_opy_ (u"ࠫࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠨᥖ")]}]
        bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᥗ")] = bstack11l11l11_opy_[bstack111l1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᥘ")]
    return bstack1lll1ll1_opy_
def bstack1ll1111lll1_opy_(test, bstack11ll111l_opy_, bstack11l1111111_opy_, result, call, outcome, bstack1ll111111l1_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack11ll111l_opy_[bstack111l1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪᥙ")]
    hook_name = bstack11ll111l_opy_[bstack111l1ll_opy_ (u"ࠨࡪࡲࡳࡰࡥ࡮ࡢ࡯ࡨࠫᥚ")]
    hook_data = {
        bstack111l1ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᥛ"): bstack11ll111l_opy_[bstack111l1ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᥜ")],
        bstack111l1ll_opy_ (u"ࠫࡹࡿࡰࡦࠩᥝ"): bstack111l1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᥞ"),
        bstack111l1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᥟ"): bstack111l1ll_opy_ (u"ࠧࡼࡿࠪᥠ").format(bstack1ll1lll1111_opy_(hook_name)),
        bstack111l1ll_opy_ (u"ࠨࡤࡲࡨࡾ࠭ᥡ"): {
            bstack111l1ll_opy_ (u"ࠩ࡯ࡥࡳ࡭ࠧᥢ"): bstack111l1ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪᥣ"),
            bstack111l1ll_opy_ (u"ࠫࡨࡵࡤࡦࠩᥤ"): None
        },
        bstack111l1ll_opy_ (u"ࠬࡹࡣࡰࡲࡨࠫᥥ"): test.name,
        bstack111l1ll_opy_ (u"࠭ࡳࡤࡱࡳࡩࡸ࠭ᥦ"): bstack1l1l1l11_opy_.bstack1l11l1l1_opy_(test, hook_name),
        bstack111l1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪᥧ"): file_path,
        bstack111l1ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪᥨ"): file_path,
        bstack111l1ll_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᥩ"): bstack111l1ll_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫᥪ"),
        bstack111l1ll_opy_ (u"ࠫࡻࡩ࡟ࡧ࡫࡯ࡩࡵࡧࡴࡩࠩᥫ"): file_path,
        bstack111l1ll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᥬ"): bstack11ll111l_opy_[bstack111l1ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᥭ")],
        bstack111l1ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ᥮"): bstack111l1ll_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴ࠮ࡥࡸࡧࡺࡳࡢࡦࡴࠪ᥯") if bstack1l1llll1lll_opy_ == bstack111l1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭ᥰ") else bstack111l1ll_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶࠪᥱ"),
        bstack111l1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᥲ"): hook_type
    }
    bstack1ll1l1l1l11_opy_ = bstack11l1l111_opy_(_11l1l1ll_opy_.get(test.nodeid, None))
    if bstack1ll1l1l1l11_opy_:
        hook_data[bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡪࡦࠪᥳ")] = bstack1ll1l1l1l11_opy_
    if result:
        hook_data[bstack111l1ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᥴ")] = result.outcome
        hook_data[bstack111l1ll_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨ᥵")] = result.duration * 1000
        hook_data[bstack111l1ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭᥶")] = bstack11ll111l_opy_[bstack111l1ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ᥷")]
        if result.failed:
            hook_data[bstack111l1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩ᥸")] = bstack1ll11l1l_opy_.bstack1lllll1l1_opy_(call.excinfo.typename)
            hook_data[bstack111l1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬ᥹")] = bstack1ll11l1l_opy_.bstack1ll11l1ll11_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack111l1ll_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ᥺")] = bstack1111l11111_opy_(outcome)
        hook_data[bstack111l1ll_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧ᥻")] = 100
        hook_data[bstack111l1ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ᥼")] = bstack11ll111l_opy_[bstack111l1ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭᥽")]
        if hook_data[bstack111l1ll_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ᥾")] == bstack111l1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ᥿"):
            hook_data[bstack111l1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪᦀ")] = bstack111l1ll_opy_ (u"࡛ࠬ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷ࠭ᦁ")  # bstack1l1llll1ll1_opy_
            hook_data[bstack111l1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧᦂ")] = [{bstack111l1ll_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪᦃ"): [bstack111l1ll_opy_ (u"ࠨࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠬᦄ")]}]
    if bstack1ll111111l1_opy_:
        hook_data[bstack111l1ll_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᦅ")] = bstack1ll111111l1_opy_.result
        hook_data[bstack111l1ll_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫᦆ")] = bstack1111l11l1l_opy_(bstack11ll111l_opy_[bstack111l1ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᦇ")], bstack11ll111l_opy_[bstack111l1ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᦈ")])
        hook_data[bstack111l1ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᦉ")] = bstack11ll111l_opy_[bstack111l1ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᦊ")]
        if hook_data[bstack111l1ll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᦋ")] == bstack111l1ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᦌ"):
            hook_data[bstack111l1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩᦍ")] = bstack1ll11l1l_opy_.bstack1lllll1l1_opy_(bstack1ll111111l1_opy_.exception_type)
            hook_data[bstack111l1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬᦎ")] = [{bstack111l1ll_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᦏ"): bstack1111l1l11l_opy_(bstack1ll111111l1_opy_.exception)}]
    return hook_data
def bstack1ll111l11l1_opy_(test, bstack11l11l11_opy_, bstack11l1111111_opy_, result=None, call=None, outcome=None):
    bstack1lll1ll1_opy_ = bstack1l1lllllll1_opy_(test, bstack11l11l11_opy_, result, call, bstack11l1111111_opy_, outcome)
    driver = getattr(test, bstack111l1ll_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧᦐ"), None)
    if bstack11l1111111_opy_ == bstack111l1ll_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨᦑ") and driver:
        bstack1lll1ll1_opy_[bstack111l1ll_opy_ (u"ࠨ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠧᦒ")] = bstack1ll11l1l_opy_.bstack1lll1l1l_opy_(driver)
    if bstack11l1111111_opy_ == bstack111l1ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖ࡯࡮ࡶࡰࡦࡦࠪᦓ"):
        bstack11l1111111_opy_ = bstack111l1ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᦔ")
    bstack1l11llll_opy_ = {
        bstack111l1ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨᦕ"): bstack11l1111111_opy_,
        bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧᦖ"): bstack1lll1ll1_opy_
    }
    bstack1ll11l1l_opy_.bstack11ll1l11_opy_(bstack1l11llll_opy_)
    if bstack11l1111111_opy_ == bstack111l1ll_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᦗ"):
        threading.current_thread().bstackTestMeta = {bstack111l1ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᦘ"): bstack111l1ll_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩᦙ")}
    elif bstack11l1111111_opy_ == bstack111l1ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᦚ"):
        threading.current_thread().bstackTestMeta = {bstack111l1ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᦛ"): getattr(result, bstack111l1ll_opy_ (u"ࠫࡴࡻࡴࡤࡱࡰࡩࠬᦜ"), bstack111l1ll_opy_ (u"ࠬ࠭ᦝ"))}
def bstack1ll111l11ll_opy_(test, bstack11l11l11_opy_, bstack11l1111111_opy_, result=None, call=None, outcome=None, bstack1ll111111l1_opy_=None):
    hook_data = bstack1ll1111lll1_opy_(test, bstack11l11l11_opy_, bstack11l1111111_opy_, result, call, outcome, bstack1ll111111l1_opy_)
    bstack1l11llll_opy_ = {
        bstack111l1ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᦞ"): bstack11l1111111_opy_,
        bstack111l1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࠩᦟ"): hook_data
    }
    bstack1ll11l1l_opy_.bstack11ll1l11_opy_(bstack1l11llll_opy_)
def bstack11l1l111_opy_(bstack11l11l11_opy_):
    if not bstack11l11l11_opy_:
        return None
    if bstack11l11l11_opy_.get(bstack111l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᦠ"), None):
        return getattr(bstack11l11l11_opy_[bstack111l1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᦡ")], bstack111l1ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᦢ"), None)
    return bstack11l11l11_opy_.get(bstack111l1ll_opy_ (u"ࠫࡺࡻࡩࡥࠩᦣ"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    yield
    try:
        if not bstack1ll11l1l_opy_.on():
            return
        places = [bstack111l1ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᦤ"), bstack111l1ll_opy_ (u"࠭ࡣࡢ࡮࡯ࠫᦥ"), bstack111l1ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩᦦ")]
        bstack11l111ll_opy_ = []
        for bstack1ll11111lll_opy_ in places:
            records = caplog.get_records(bstack1ll11111lll_opy_)
            bstack1ll1111ll11_opy_ = bstack111l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᦧ") if bstack1ll11111lll_opy_ == bstack111l1ll_opy_ (u"ࠩࡦࡥࡱࡲࠧᦨ") else bstack111l1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᦩ")
            bstack1ll111111ll_opy_ = request.node.nodeid + (bstack111l1ll_opy_ (u"ࠫࠬᦪ") if bstack1ll11111lll_opy_ == bstack111l1ll_opy_ (u"ࠬࡩࡡ࡭࡮ࠪᦫ") else bstack111l1ll_opy_ (u"࠭࠭ࠨ᦬") + bstack1ll11111lll_opy_)
            bstack1ll1llll_opy_ = bstack11l1l111_opy_(_11l1l1ll_opy_.get(bstack1ll111111ll_opy_, None))
            if not bstack1ll1llll_opy_:
                continue
            for record in records:
                if bstack11111111l1_opy_(record.message):
                    continue
                bstack11l111ll_opy_.append({
                    bstack111l1ll_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ᦭"): bstack1lllll1l11l_opy_(record.created).isoformat() + bstack111l1ll_opy_ (u"ࠨ࡜ࠪ᦮"),
                    bstack111l1ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ᦯"): record.levelname,
                    bstack111l1ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᦰ"): record.message,
                    bstack1ll1111ll11_opy_: bstack1ll1llll_opy_
                })
        if len(bstack11l111ll_opy_) > 0:
            bstack1ll11l1l_opy_.bstack1l1l1ll1_opy_(bstack11l111ll_opy_)
    except Exception as err:
        print(bstack111l1ll_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡪࡩ࡯࡯ࡦࡢࡪ࡮ࡾࡴࡶࡴࡨ࠾ࠥࢁࡽࠨᦱ"), str(err))
def bstack1l1l1l1111_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack11ll1ll1l_opy_
    bstack1llll11ll1_opy_ = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩᦲ"), None) and bstack1ll111l1_opy_(
            threading.current_thread(), bstack111l1ll_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬᦳ"), None)
    bstack1l1l1l111l_opy_ = getattr(driver, bstack111l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧᦴ"), None) != None and getattr(driver, bstack111l1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨᦵ"), None) == True
    if sequence == bstack111l1ll_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩᦶ") and driver != None:
      if not bstack11ll1ll1l_opy_ and bstack1111ll1l1l_opy_() and bstack111l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᦷ") in CONFIG and CONFIG[bstack111l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᦸ")] == True and bstack1ll1l1l11l_opy_.bstack1l11l1l111_opy_(driver_command) and (bstack1l1l1l111l_opy_ or bstack1llll11ll1_opy_) and not bstack11llllll11_opy_(args):
        try:
          bstack11ll1ll1l_opy_ = True
          logger.debug(bstack111l1ll_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࢀࢃࠧᦹ").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack111l1ll_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡩࡷ࡬࡯ࡳ࡯ࠣࡷࡨࡧ࡮ࠡࡽࢀࠫᦺ").format(str(err)))
        bstack11ll1ll1l_opy_ = False
    if sequence == bstack111l1ll_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ᦻ"):
        if driver_command == bstack111l1ll_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬᦼ"):
            bstack1ll11l1l_opy_.bstack1ll1l1llll_opy_({
                bstack111l1ll_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨᦽ"): response[bstack111l1ll_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩᦾ")],
                bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᦿ"): store[bstack111l1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᧀ")]
            })
def bstack11lll1ll1_opy_():
    global bstack1ll111l11l_opy_
    bstack1llllll1l1_opy_.bstack1ll1ll111l_opy_()
    logging.shutdown()
    bstack1ll11l1l_opy_.bstack1l111ll1_opy_()
    for driver in bstack1ll111l11l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1l1llllll1l_opy_(*args):
    global bstack1ll111l11l_opy_
    bstack1ll11l1l_opy_.bstack1l111ll1_opy_()
    for driver in bstack1ll111l11l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1l1ll1111_opy_(self, *args, **kwargs):
    bstack11l111l1ll_opy_ = bstack1ll11ll11_opy_(self, *args, **kwargs)
    bstack1lllll1l11_opy_ = getattr(threading.current_thread(), bstack111l1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡚ࡥࡴࡶࡐࡩࡹࡧࠧᧁ"), None)
    if bstack1lllll1l11_opy_ and bstack1lllll1l11_opy_.get(bstack111l1ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᧂ"), bstack111l1ll_opy_ (u"ࠨࠩᧃ")) == bstack111l1ll_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪᧄ"):
        bstack1ll11l1l_opy_.bstack11lll1l11l_opy_(self)
    return bstack11l111l1ll_opy_
def bstack11l11ll1ll_opy_(framework_name):
    from bstack_utils.config import Config
    bstack1111lll1_opy_ = Config.bstack11111lll_opy_()
    if bstack1111lll1_opy_.get_property(bstack111l1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡱࡴࡪ࡟ࡤࡣ࡯ࡰࡪࡪࠧᧅ")):
        return
    bstack1111lll1_opy_.bstack11llll1ll1_opy_(bstack111l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡲࡵࡤࡠࡥࡤࡰࡱ࡫ࡤࠨᧆ"), True)
    global bstack111llllll1_opy_
    global bstack111l11111_opy_
    bstack111llllll1_opy_ = framework_name
    logger.info(bstack1l1ll11l1l_opy_.format(bstack111llllll1_opy_.split(bstack111l1ll_opy_ (u"ࠬ࠳ࠧᧇ"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1111ll1l1l_opy_():
            Service.start = bstack11ll1ll111_opy_
            Service.stop = bstack11ll1l1111_opy_
            webdriver.Remote.__init__ = bstack11l1l11l11_opy_
            webdriver.Remote.get = bstack111111111_opy_
            if not isinstance(os.getenv(bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡁࡓࡃࡏࡐࡊࡒࠧᧈ")), str):
                return
            WebDriver.close = bstack11l111ll1l_opy_
            WebDriver.quit = bstack111l1l1ll_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        if not bstack1111ll1l1l_opy_() and bstack1ll11l1l_opy_.on():
            webdriver.Remote.__init__ = bstack1l1ll1111_opy_
        bstack111l11111_opy_ = True
    except Exception as e:
        pass
    bstack11lll111ll_opy_()
    if os.environ.get(bstack111l1ll_opy_ (u"ࠧࡔࡇࡏࡉࡓࡏࡕࡎࡡࡒࡖࡤࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡌࡒࡘ࡚ࡁࡍࡎࡈࡈࠬᧉ")):
        bstack111l11111_opy_ = eval(os.environ.get(bstack111l1ll_opy_ (u"ࠨࡕࡈࡐࡊࡔࡉࡖࡏࡢࡓࡗࡥࡐࡍࡃ࡜࡛ࡗࡏࡇࡉࡖࡢࡍࡓ࡙ࡔࡂࡎࡏࡉࡉ࠭᧊")))
    if not bstack111l11111_opy_:
        bstack1lll111l1_opy_(bstack111l1ll_opy_ (u"ࠤࡓࡥࡨࡱࡡࡨࡧࡶࠤࡳࡵࡴࠡ࡫ࡱࡷࡹࡧ࡬࡭ࡧࡧࠦ᧋"), bstack1lll11lll_opy_)
    if bstack11l1l11111_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._1ll1l1l1l_opy_ = bstack1l1ll1111l_opy_
        except Exception as e:
            logger.error(bstack11l1l1l111_opy_.format(str(e)))
    if bstack111l1ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ᧌") in str(framework_name).lower():
        if not bstack1111ll1l1l_opy_():
            return
        try:
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
def bstack111l1l1ll_opy_(self):
    global bstack111llllll1_opy_
    global bstack11l1lllll_opy_
    global bstack11ll11lll1_opy_
    try:
        if bstack111l1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ᧍") in bstack111llllll1_opy_ and self.session_id != None and bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡖࡸࡦࡺࡵࡴࠩ᧎"), bstack111l1ll_opy_ (u"࠭ࠧ᧏")) != bstack111l1ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ᧐"):
            bstack1ll1lllll_opy_ = bstack111l1ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ᧑") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack111l1ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ᧒")
            bstack111l1ll11_opy_(logger, True)
            if self != None:
                bstack11ll111l1l_opy_(self, bstack1ll1lllll_opy_, bstack111l1ll_opy_ (u"ࠪ࠰ࠥ࠭᧓").join(threading.current_thread().bstackTestErrorMessages))
        item = store.get(bstack111l1ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨ᧔"), None)
        if item is not None and bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ᧕"), None):
            bstack111l111l_opy_.bstack111llll1_opy_(self, bstack1lllll111l_opy_, logger, item)
        threading.current_thread().testStatus = bstack111l1ll_opy_ (u"࠭ࠧ᧖")
    except Exception as e:
        logger.debug(bstack111l1ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦࡳࡵࡣࡷࡹࡸࡀࠠࠣ᧗") + str(e))
    bstack11ll11lll1_opy_(self)
    self.session_id = None
def bstack11l1l11l11_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack11l1lllll_opy_
    global bstack11lll1ll11_opy_
    global bstack11l11l1l11_opy_
    global bstack111llllll1_opy_
    global bstack1ll11ll11_opy_
    global bstack1ll111l11l_opy_
    global bstack11111l1l1_opy_
    global bstack1l111ll1l_opy_
    global bstack1lllll111l_opy_
    CONFIG[bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪ᧘")] = str(bstack111llllll1_opy_) + str(__version__)
    command_executor = bstack1ll1111ll1_opy_(bstack11111l1l1_opy_, CONFIG)
    logger.debug(bstack1lll11111l_opy_.format(command_executor))
    proxy = bstack1ll1ll1lll_opy_(CONFIG, proxy)
    bstack1l11l1111l_opy_ = 0
    try:
        if bstack11l11l1l11_opy_ is True:
            bstack1l11l1111l_opy_ = int(os.environ.get(bstack111l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ᧙")))
    except:
        bstack1l11l1111l_opy_ = 0
    bstack1lll1l11ll_opy_ = bstack1111l1l1l_opy_(CONFIG, bstack1l11l1111l_opy_)
    logger.debug(bstack1lllllllll_opy_.format(str(bstack1lll1l11ll_opy_)))
    bstack1lllll111l_opy_ = CONFIG.get(bstack111l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭᧚"))[bstack1l11l1111l_opy_]
    if bstack111l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ᧛") in CONFIG and CONFIG[bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ᧜")]:
        bstack1ll1lll1l_opy_(bstack1lll1l11ll_opy_, bstack1l111ll1l_opy_)
    if bstack1111111l_opy_.bstack11ll11l1l_opy_(CONFIG, bstack1l11l1111l_opy_) and bstack1111111l_opy_.bstack11l1111l11_opy_(bstack1lll1l11ll_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        bstack1111111l_opy_.set_capabilities(bstack1lll1l11ll_opy_, CONFIG)
    if desired_capabilities:
        bstack1l1ll11ll_opy_ = bstack111l11l1l_opy_(desired_capabilities)
        bstack1l1ll11ll_opy_[bstack111l1ll_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭᧝")] = bstack1l1lll1ll_opy_(CONFIG)
        bstack1l1llll111_opy_ = bstack1111l1l1l_opy_(bstack1l1ll11ll_opy_)
        if bstack1l1llll111_opy_:
            bstack1lll1l11ll_opy_ = update(bstack1l1llll111_opy_, bstack1lll1l11ll_opy_)
        desired_capabilities = None
    if options:
        bstack111ll1lll_opy_(options, bstack1lll1l11ll_opy_)
    if not options:
        options = bstack1111lll1l_opy_(bstack1lll1l11ll_opy_)
    if proxy and bstack11lll1111_opy_() >= version.parse(bstack111l1ll_opy_ (u"ࠧ࠵࠰࠴࠴࠳࠶ࠧ᧞")):
        options.proxy(proxy)
    if options and bstack11lll1111_opy_() >= version.parse(bstack111l1ll_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧ᧟")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack11lll1111_opy_() < version.parse(bstack111l1ll_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨ᧠")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1lll1l11ll_opy_)
    logger.info(bstack1llllll111_opy_)
    if bstack11lll1111_opy_() >= version.parse(bstack111l1ll_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪ᧡")):
        bstack1ll11ll11_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11lll1111_opy_() >= version.parse(bstack111l1ll_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪ᧢")):
        bstack1ll11ll11_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11lll1111_opy_() >= version.parse(bstack111l1ll_opy_ (u"ࠬ࠸࠮࠶࠵࠱࠴ࠬ᧣")):
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
        bstack1111l1111_opy_ = bstack111l1ll_opy_ (u"࠭ࠧ᧤")
        if bstack11lll1111_opy_() >= version.parse(bstack111l1ll_opy_ (u"ࠧ࠵࠰࠳࠲࠵ࡨ࠱ࠨ᧥")):
            bstack1111l1111_opy_ = self.caps.get(bstack111l1ll_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣ᧦"))
        else:
            bstack1111l1111_opy_ = self.capabilities.get(bstack111l1ll_opy_ (u"ࠤࡲࡴࡹ࡯࡭ࡢ࡮ࡋࡹࡧ࡛ࡲ࡭ࠤ᧧"))
        if bstack1111l1111_opy_:
            bstack1l1l111l1l_opy_(bstack1111l1111_opy_)
            if bstack11lll1111_opy_() <= version.parse(bstack111l1ll_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪ᧨")):
                self.command_executor._url = bstack111l1ll_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧ᧩") + bstack11111l1l1_opy_ + bstack111l1ll_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤ᧪")
            else:
                self.command_executor._url = bstack111l1ll_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣ᧫") + bstack1111l1111_opy_ + bstack111l1ll_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢࠣ᧬")
            logger.debug(bstack1ll11l1ll1_opy_.format(bstack1111l1111_opy_))
        else:
            logger.debug(bstack1lll1ll11_opy_.format(bstack111l1ll_opy_ (u"ࠣࡑࡳࡸ࡮ࡳࡡ࡭ࠢࡋࡹࡧࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥࠤ᧭")))
    except Exception as e:
        logger.debug(bstack1lll1ll11_opy_.format(e))
    bstack11l1lllll_opy_ = self.session_id
    if bstack111l1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ᧮") in bstack111llllll1_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack111l1ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧ᧯"), None)
        if item:
            bstack1ll1111ll1l_opy_ = getattr(item, bstack111l1ll_opy_ (u"ࠫࡤࡺࡥࡴࡶࡢࡧࡦࡹࡥࡠࡵࡷࡥࡷࡺࡥࡥࠩ᧰"), False)
            if not getattr(item, bstack111l1ll_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭᧱"), None) and bstack1ll1111ll1l_opy_:
                setattr(store[bstack111l1ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ᧲")], bstack111l1ll_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨ᧳"), self)
        bstack1lllll1l11_opy_ = getattr(threading.current_thread(), bstack111l1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡕࡧࡶࡸࡒ࡫ࡴࡢࠩ᧴"), None)
        if bstack1lllll1l11_opy_ and bstack1lllll1l11_opy_.get(bstack111l1ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ᧵"), bstack111l1ll_opy_ (u"ࠪࠫ᧶")) == bstack111l1ll_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ᧷"):
            bstack1ll11l1l_opy_.bstack11lll1l11l_opy_(self)
    bstack1ll111l11l_opy_.append(self)
    if bstack111l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ᧸") in CONFIG and bstack111l1ll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ᧹") in CONFIG[bstack111l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ᧺")][bstack1l11l1111l_opy_]:
        bstack11lll1ll11_opy_ = CONFIG[bstack111l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ᧻")][bstack1l11l1111l_opy_][bstack111l1ll_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ᧼")]
    logger.debug(bstack111ll11ll_opy_.format(bstack11l1lllll_opy_))
def bstack111111111_opy_(self, url):
    global bstack11lll1lll1_opy_
    global CONFIG
    try:
        bstack1l1ll1l111_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1ll1l11l11_opy_.format(str(err)))
    try:
        bstack11lll1lll1_opy_(self, url)
    except Exception as e:
        try:
            bstack1l11llll1_opy_ = str(e)
            if any(err_msg in bstack1l11llll1_opy_ for err_msg in bstack11l1111ll1_opy_):
                bstack1l1ll1l111_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1ll1l11l11_opy_.format(str(err)))
        raise e
def bstack1ll1l1lll_opy_(item, when):
    global bstack1l1l11111l_opy_
    try:
        bstack1l1l11111l_opy_(item, when)
    except Exception as e:
        pass
def bstack11ll1l11l_opy_(item, call, rep):
    global bstack1ll111lll1_opy_
    global bstack1ll111l11l_opy_
    name = bstack111l1ll_opy_ (u"ࠪࠫ᧽")
    try:
        if rep.when == bstack111l1ll_opy_ (u"ࠫࡨࡧ࡬࡭ࠩ᧾"):
            bstack11l1lllll_opy_ = threading.current_thread().bstackSessionId
            bstack1ll1111111l_opy_ = item.config.getoption(bstack111l1ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ᧿"))
            try:
                if (str(bstack1ll1111111l_opy_).lower() != bstack111l1ll_opy_ (u"࠭ࡴࡳࡷࡨࠫᨀ")):
                    name = str(rep.nodeid)
                    bstack1l1l1ll11_opy_ = bstack1l11ll1ll1_opy_(bstack111l1ll_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᨁ"), name, bstack111l1ll_opy_ (u"ࠨࠩᨂ"), bstack111l1ll_opy_ (u"ࠩࠪᨃ"), bstack111l1ll_opy_ (u"ࠪࠫᨄ"), bstack111l1ll_opy_ (u"ࠫࠬᨅ"))
                    os.environ[bstack111l1ll_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨᨆ")] = name
                    for driver in bstack1ll111l11l_opy_:
                        if bstack11l1lllll_opy_ == driver.session_id:
                            driver.execute_script(bstack1l1l1ll11_opy_)
            except Exception as e:
                logger.debug(bstack111l1ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠠࡧࡱࡵࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡵࡨࡷࡸ࡯࡯࡯࠼ࠣࡿࢂ࠭ᨇ").format(str(e)))
            try:
                bstack11l1ll1ll_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack111l1ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᨈ"):
                    status = bstack111l1ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᨉ") if rep.outcome.lower() == bstack111l1ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᨊ") else bstack111l1ll_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᨋ")
                    reason = bstack111l1ll_opy_ (u"ࠫࠬᨌ")
                    if status == bstack111l1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᨍ"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack111l1ll_opy_ (u"࠭ࡩ࡯ࡨࡲࠫᨎ") if status == bstack111l1ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᨏ") else bstack111l1ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᨐ")
                    data = name + bstack111l1ll_opy_ (u"ࠩࠣࡴࡦࡹࡳࡦࡦࠤࠫᨑ") if status == bstack111l1ll_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᨒ") else name + bstack111l1ll_opy_ (u"ࠫࠥ࡬ࡡࡪ࡮ࡨࡨࠦࠦࠧᨓ") + reason
                    bstack1l1l1ll1ll_opy_ = bstack1l11ll1ll1_opy_(bstack111l1ll_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧᨔ"), bstack111l1ll_opy_ (u"࠭ࠧᨕ"), bstack111l1ll_opy_ (u"ࠧࠨᨖ"), bstack111l1ll_opy_ (u"ࠨࠩᨗ"), level, data)
                    for driver in bstack1ll111l11l_opy_:
                        if bstack11l1lllll_opy_ == driver.session_id:
                            driver.execute_script(bstack1l1l1ll1ll_opy_)
            except Exception as e:
                logger.debug(bstack111l1ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡣࡰࡰࡷࡩࡽࡺࠠࡧࡱࡵࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡵࡨࡷࡸ࡯࡯࡯࠼ࠣࡿࢂᨘ࠭").format(str(e)))
    except Exception as e:
        logger.debug(bstack111l1ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡵࡣࡷࡩࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࢀࢃࠧᨙ").format(str(e)))
    bstack1ll111lll1_opy_(item, call, rep)
notset = Notset()
def bstack1l11l111l_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack11l11lll1l_opy_
    if str(name).lower() == bstack111l1ll_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࠫᨚ"):
        return bstack111l1ll_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠦᨛ")
    else:
        return bstack11l11lll1l_opy_(self, name, default, skip)
def bstack1l1ll1111l_opy_(self):
    global CONFIG
    global bstack1ll11l1l11_opy_
    try:
        proxy = bstack111111ll1_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack111l1ll_opy_ (u"࠭࠮ࡱࡣࡦࠫ᨜")):
                proxies = bstack11111l1ll_opy_(proxy, bstack1ll1111ll1_opy_())
                if len(proxies) > 0:
                    protocol, bstack1l1lllll1_opy_ = proxies.popitem()
                    if bstack111l1ll_opy_ (u"ࠢ࠻࠱࠲ࠦ᨝") in bstack1l1lllll1_opy_:
                        return bstack1l1lllll1_opy_
                    else:
                        return bstack111l1ll_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤ᨞") + bstack1l1lllll1_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack111l1ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡶࡲࡰࡺࡼࠤࡺࡸ࡬ࠡ࠼ࠣࡿࢂࠨ᨟").format(str(e)))
    return bstack1ll11l1l11_opy_(self)
def bstack11l1l11111_opy_():
    return (bstack111l1ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ᨠ") in CONFIG or bstack111l1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᨡ") in CONFIG) and bstack1l1ll11l1_opy_() and bstack11lll1111_opy_() >= version.parse(
        bstack1l1ll11ll1_opy_)
def bstack11l1l1111_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack11lll1ll11_opy_
    global bstack11l11l1l11_opy_
    global bstack111llllll1_opy_
    CONFIG[bstack111l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧᨢ")] = str(bstack111llllll1_opy_) + str(__version__)
    bstack1l11l1111l_opy_ = 0
    try:
        if bstack11l11l1l11_opy_ is True:
            bstack1l11l1111l_opy_ = int(os.environ.get(bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᨣ")))
    except:
        bstack1l11l1111l_opy_ = 0
    CONFIG[bstack111l1ll_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨᨤ")] = True
    bstack1lll1l11ll_opy_ = bstack1111l1l1l_opy_(CONFIG, bstack1l11l1111l_opy_)
    logger.debug(bstack1lllllllll_opy_.format(str(bstack1lll1l11ll_opy_)))
    if CONFIG.get(bstack111l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬᨥ")):
        bstack1ll1lll1l_opy_(bstack1lll1l11ll_opy_, bstack1l111ll1l_opy_)
    if bstack111l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᨦ") in CONFIG and bstack111l1ll_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᨧ") in CONFIG[bstack111l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᨨ")][bstack1l11l1111l_opy_]:
        bstack11lll1ll11_opy_ = CONFIG[bstack111l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᨩ")][bstack1l11l1111l_opy_][bstack111l1ll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᨪ")]
    import urllib
    import json
    if bstack111l1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫᨫ") in CONFIG and str(CONFIG[bstack111l1ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬᨬ")]).lower() != bstack111l1ll_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨᨭ"):
        bstack11l1ll11ll_opy_ = bstack11ll11ll1l_opy_()
        bstack11l1l11l1l_opy_ = bstack11l1ll11ll_opy_ + urllib.parse.quote(json.dumps(bstack1lll1l11ll_opy_))
    else:
        bstack11l1l11l1l_opy_ = bstack111l1ll_opy_ (u"ࠪࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠬᨮ") + urllib.parse.quote(json.dumps(bstack1lll1l11ll_opy_))
    browser = self.connect(bstack11l1l11l1l_opy_)
    return browser
def bstack11lll111ll_opy_():
    global bstack111l11111_opy_
    global bstack111llllll1_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1l111111l1_opy_
        if not bstack1111ll1l1l_opy_():
            global bstack1l111ll111_opy_
            if not bstack1l111ll111_opy_:
                from bstack_utils.helper import bstack1ll11l111l_opy_, bstack1l1l1111ll_opy_
                bstack1l111ll111_opy_ = bstack1ll11l111l_opy_()
                bstack1l1l1111ll_opy_(bstack111llllll1_opy_)
            BrowserType.connect = bstack1l111111l1_opy_
            return
        BrowserType.launch = bstack11l1l1111_opy_
        bstack111l11111_opy_ = True
    except Exception as e:
        pass
def bstack1ll11111l1l_opy_():
    global CONFIG
    global bstack1l11l1111_opy_
    global bstack11111l1l1_opy_
    global bstack1l111ll1l_opy_
    global bstack11l11l1l11_opy_
    global bstack1lllllll1l_opy_
    CONFIG = json.loads(os.environ.get(bstack111l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࠪᨯ")))
    bstack1l11l1111_opy_ = eval(os.environ.get(bstack111l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ᨰ")))
    bstack11111l1l1_opy_ = os.environ.get(bstack111l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡎࡕࡃࡡࡘࡖࡑ࠭ᨱ"))
    bstack1l111l1l11_opy_(CONFIG, bstack1l11l1111_opy_)
    bstack1lllllll1l_opy_ = bstack1llllll1l1_opy_.bstack1lll111l1l_opy_(CONFIG, bstack1lllllll1l_opy_)
    global bstack1ll11ll11_opy_
    global bstack11ll11lll1_opy_
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
    except Exception as e:
        pass
    if (bstack111l1ll_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᨲ") in CONFIG or bstack111l1ll_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬᨳ") in CONFIG) and bstack1l1ll11l1_opy_():
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
        logger.debug(bstack111l1ll_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡱࠣࡶࡺࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࡵࠪᨴ"))
    bstack1l111ll1l_opy_ = CONFIG.get(bstack111l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧᨵ"), {}).get(bstack111l1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᨶ"))
    bstack11l11l1l11_opy_ = True
    bstack11l11ll1ll_opy_(bstack11l1ll1ll1_opy_)
if (bstack1111llll11_opy_()):
    bstack1ll11111l1l_opy_()
@bstack11l1111l_opy_(class_method=False)
def bstack1ll1111l1l1_opy_(hook_name, event, bstack1ll11111ll1_opy_=None):
    if hook_name not in [bstack111l1ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᨷ"), bstack111l1ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪᨸ"), bstack111l1ll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭ᨹ"), bstack111l1ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪᨺ"), bstack111l1ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧᨻ"), bstack111l1ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫᨼ"), bstack111l1ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠪᨽ"), bstack111l1ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡧࡷ࡬ࡴࡪࠧᨾ")]:
        return
    node = store[bstack111l1ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪᨿ")]
    if hook_name in [bstack111l1ll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭ᩀ"), bstack111l1ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪᩁ")]:
        node = store[bstack111l1ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡱࡴࡪࡵ࡭ࡧࡢ࡭ࡹ࡫࡭ࠨᩂ")]
    elif hook_name in [bstack111l1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨᩃ"), bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬᩄ")]:
        node = store[bstack111l1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡣ࡭ࡣࡶࡷࡤ࡯ࡴࡦ࡯ࠪᩅ")]
    if event == bstack111l1ll_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪ࠭ᩆ"):
        hook_type = bstack1ll1ll1lll1_opy_(hook_name)
        uuid = uuid4().__str__()
        bstack11ll111l_opy_ = {
            bstack111l1ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᩇ"): uuid,
            bstack111l1ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᩈ"): bstack1l1lllll_opy_(),
            bstack111l1ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᩉ"): bstack111l1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᩊ"),
            bstack111l1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᩋ"): hook_type,
            bstack111l1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨᩌ"): hook_name
        }
        store[bstack111l1ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᩍ")].append(uuid)
        bstack1l1llll1l1l_opy_ = node.nodeid
        if hook_type == bstack111l1ll_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬᩎ"):
            if not _11l1l1ll_opy_.get(bstack1l1llll1l1l_opy_, None):
                _11l1l1ll_opy_[bstack1l1llll1l1l_opy_] = {bstack111l1ll_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᩏ"): []}
            _11l1l1ll_opy_[bstack1l1llll1l1l_opy_][bstack111l1ll_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᩐ")].append(bstack11ll111l_opy_[bstack111l1ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᩑ")])
        _11l1l1ll_opy_[bstack1l1llll1l1l_opy_ + bstack111l1ll_opy_ (u"ࠫ࠲࠭ᩒ") + hook_name] = bstack11ll111l_opy_
        bstack1ll111l11ll_opy_(node, bstack11ll111l_opy_, bstack111l1ll_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᩓ"))
    elif event == bstack111l1ll_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬᩔ"):
        bstack1l1lll1l_opy_ = node.nodeid + bstack111l1ll_opy_ (u"ࠧ࠮ࠩᩕ") + hook_name
        _11l1l1ll_opy_[bstack1l1lll1l_opy_][bstack111l1ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᩖ")] = bstack1l1lllll_opy_()
        bstack1l1lllll11l_opy_(_11l1l1ll_opy_[bstack1l1lll1l_opy_][bstack111l1ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᩗ")])
        bstack1ll111l11ll_opy_(node, _11l1l1ll_opy_[bstack1l1lll1l_opy_], bstack111l1ll_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᩘ"), bstack1ll111111l1_opy_=bstack1ll11111ll1_opy_)
def bstack1ll1111l1ll_opy_():
    global bstack1l1llll1lll_opy_
    if bstack1l1lll111l_opy_():
        bstack1l1llll1lll_opy_ = bstack111l1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠨᩙ")
    else:
        bstack1l1llll1lll_opy_ = bstack111l1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᩚ")
@bstack1ll11l1l_opy_.bstack1ll11lll111_opy_
def bstack1l1lllll111_opy_():
    bstack1ll1111l1ll_opy_()
    if bstack1l1ll11l1_opy_():
        bstack11l11l1ll1_opy_(bstack1l1l1l1111_opy_)
    try:
        bstack1llll1lll11_opy_(bstack1ll1111l1l1_opy_)
    except Exception as e:
        logger.debug(bstack111l1ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࡶࠤࡵࡧࡴࡤࡪ࠽ࠤࢀࢃࠢᩛ").format(e))
bstack1l1lllll111_opy_()