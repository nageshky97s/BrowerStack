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
import threading
import os
import logging
from uuid import uuid4
from bstack_utils.bstack1lll1ll1_opy_ import bstack1l1l11ll_opy_, bstack1lll1111_opy_
from bstack_utils.bstack1ll11l11_opy_ import bstack1l1l1l11_opy_
from bstack_utils.helper import bstack1ll111l1_opy_, bstack1l1lllll_opy_, Result
from bstack_utils.bstack1l1lll11_opy_ import bstack1ll11l1l_opy_
from bstack_utils.capture import bstack1ll1ll1l_opy_
from bstack_utils.constants import *
logger = logging.getLogger(__name__)
class bstack1lll11ll_opy_:
    def __init__(self):
        self.bstack1lll111l_opy_ = bstack1ll1ll1l_opy_(self.bstack1ll11111_opy_)
        self.tests = {}
    @staticmethod
    def bstack1ll11111_opy_(log):
        if not (log[bstack111l1ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ࢝")] and log[bstack111l1ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ࢞")].strip()):
            return
        active = bstack1l1l1l11_opy_.bstack1ll11lll_opy_()
        log = {
            bstack111l1ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ࢟"): log[bstack111l1ll_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩࢠ")],
            bstack111l1ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧࢡ"): bstack1l1lllll_opy_(),
            bstack111l1ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ࢢ"): log[bstack111l1ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧࢣ")],
        }
        if active:
            if active[bstack111l1ll_opy_ (u"ࠧࡵࡻࡳࡩࠬࢤ")] == bstack111l1ll_opy_ (u"ࠨࡪࡲࡳࡰ࠭ࢥ"):
                log[bstack111l1ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩࢦ")] = active[bstack111l1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪࢧ")]
            elif active[bstack111l1ll_opy_ (u"ࠫࡹࡿࡰࡦࠩࢨ")] == bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶࠪࢩ"):
                log[bstack111l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ࢪ")] = active[bstack111l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧࢫ")]
        bstack1ll11l1l_opy_.bstack1l1l1ll1_opy_([log])
    def start_test(self, attrs):
        bstack1ll1llll_opy_ = uuid4().__str__()
        self.tests[bstack1ll1llll_opy_] = {}
        self.bstack1lll111l_opy_.start()
        driver = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧࢬ"), None)
        bstack1lll1ll1_opy_ = bstack1lll1111_opy_(
            name=attrs.scenario.name,
            uuid=bstack1ll1llll_opy_,
            bstack1l1ll111_opy_=bstack1l1lllll_opy_(),
            file_path=attrs.feature.filename,
            result=bstack111l1ll_opy_ (u"ࠤࡳࡩࡳࡪࡩ࡯ࡩࠥࢭ"),
            framework=bstack111l1ll_opy_ (u"ࠪࡆࡪ࡮ࡡࡷࡧࠪࢮ"),
            scope=[attrs.feature.name],
            bstack1llll111_opy_=bstack1ll11l1l_opy_.bstack1lll1l1l_opy_(driver) if driver and driver.session_id else {},
            meta={},
            tags=attrs.scenario.tags
        )
        self.tests[bstack1ll1llll_opy_][bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧࢯ")] = bstack1lll1ll1_opy_
        threading.current_thread().current_test_uuid = bstack1ll1llll_opy_
        bstack1ll11l1l_opy_.bstack1ll1l11l_opy_(bstack111l1ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ࢰ"), bstack1lll1ll1_opy_)
    def end_test(self, attrs):
        bstack1ll1111l_opy_ = {
            bstack111l1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦࢱ"): attrs.feature.name,
            bstack111l1ll_opy_ (u"ࠢࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠧࢲ"): attrs.feature.description
        }
        current_test_uuid = threading.current_thread().current_test_uuid
        bstack1lll1ll1_opy_ = self.tests[current_test_uuid][bstack111l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫࢳ")]
        meta = {
            bstack111l1ll_opy_ (u"ࠤࡩࡩࡦࡺࡵࡳࡧࠥࢴ"): bstack1ll1111l_opy_,
            bstack111l1ll_opy_ (u"ࠥࡷࡹ࡫ࡰࡴࠤࢵ"): bstack1lll1ll1_opy_.meta.get(bstack111l1ll_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪࢶ"), []),
            bstack111l1ll_opy_ (u"ࠧࡹࡣࡦࡰࡤࡶ࡮ࡵࠢࢷ"): {
                bstack111l1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦࢸ"): attrs.feature.scenarios[0].name if len(attrs.feature.scenarios) else None
            }
        }
        bstack1lll1ll1_opy_.bstack1l1llll1_opy_(meta)
        bstack1lll1ll1_opy_.bstack1l1l1lll_opy_(bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࠬࢹ"), []))
        bstack1ll1l111_opy_, exception = self._1l1l1l1l_opy_(attrs)
        bstack1ll1ll11_opy_ = Result(result=attrs.status.name, exception=exception, bstack1ll1lll1_opy_=[bstack1ll1l111_opy_])
        self.tests[threading.current_thread().current_test_uuid][bstack111l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫࢺ")].stop(time=bstack1l1lllll_opy_(), duration=int(attrs.duration)*1000, result=bstack1ll1ll11_opy_)
        bstack1ll11l1l_opy_.bstack1ll1l11l_opy_(bstack111l1ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫࢻ"), self.tests[threading.current_thread().current_test_uuid][bstack111l1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ࢼ")])
    def bstack1lll1l11_opy_(self, attrs):
        bstack1ll1l1ll_opy_ = {
            bstack111l1ll_opy_ (u"ࠫ࡮ࡪࠧࢽ"): uuid4().__str__(),
            bstack111l1ll_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭ࢾ"): attrs.keyword,
            bstack111l1ll_opy_ (u"࠭ࡳࡵࡧࡳࡣࡦࡸࡧࡶ࡯ࡨࡲࡹ࠭ࢿ"): [],
            bstack111l1ll_opy_ (u"ࠧࡵࡧࡻࡸࠬࣀ"): attrs.name,
            bstack111l1ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬࣁ"): bstack1l1lllll_opy_(),
            bstack111l1ll_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩࣂ"): bstack111l1ll_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫࣃ"),
            bstack111l1ll_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩࣄ"): bstack111l1ll_opy_ (u"ࠬ࠭ࣅ")
        }
        self.tests[threading.current_thread().current_test_uuid][bstack111l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩࣆ")].add_step(bstack1ll1l1ll_opy_)
        threading.current_thread().current_step_uuid = bstack1ll1l1ll_opy_[bstack111l1ll_opy_ (u"ࠧࡪࡦࠪࣇ")]
    def bstack1lll1lll_opy_(self, attrs):
        current_test_id = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬࣈ"), None)
        current_step_uuid = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡷࡹ࡫ࡰࡠࡷࡸ࡭ࡩ࠭ࣉ"), None)
        bstack1ll1l111_opy_, exception = self._1l1l1l1l_opy_(attrs)
        bstack1ll1ll11_opy_ = Result(result=attrs.status.name, exception=exception, bstack1ll1lll1_opy_=[bstack1ll1l111_opy_])
        self.tests[current_test_id][bstack111l1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭࣊")].bstack1l1ll1l1_opy_(current_step_uuid, duration=int(attrs.duration)*1000, result=bstack1ll1ll11_opy_)
        threading.current_thread().current_step_uuid = None
    def bstack1ll1l1l1_opy_(self, name, attrs):
        try:
            bstack1l1ll11l_opy_ = uuid4().__str__()
            self.tests[bstack1l1ll11l_opy_] = {}
            self.bstack1lll111l_opy_.start()
            scopes = []
            driver = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ࣋"), None)
            current_thread = threading.current_thread()
            if not hasattr(current_thread, bstack111l1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠪ࣌")):
                current_thread.current_test_hooks = []
            current_thread.current_test_hooks.append(bstack1l1ll11l_opy_)
            if name in [bstack111l1ll_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥ࣍"), bstack111l1ll_opy_ (u"ࠢࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠥ࣎")]:
                file_path = os.path.join(attrs.config.base_dir, attrs.config.environment_file)
                scopes = [attrs.config.environment_file]
            elif name in [bstack111l1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤ࣏"), bstack111l1ll_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠤ࣐")]:
                file_path = attrs.filename
                scopes = [attrs.name]
            else:
                file_path = attrs.filename
                if hasattr(attrs, bstack111l1ll_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨ࣑ࠫ")):
                    scopes =  [attrs.feature.name]
            hook_data = bstack1l1l11ll_opy_(
                name=name,
                uuid=bstack1l1ll11l_opy_,
                bstack1l1ll111_opy_=bstack1l1lllll_opy_(),
                file_path=file_path,
                framework=bstack111l1ll_opy_ (u"ࠦࡇ࡫ࡨࡢࡸࡨ࣒ࠦ"),
                bstack1llll111_opy_=bstack1ll11l1l_opy_.bstack1lll1l1l_opy_(driver) if driver and driver.session_id else {},
                scope=scopes,
                result=bstack111l1ll_opy_ (u"ࠧࡶࡥ࡯ࡦ࡬ࡲ࡬ࠨ࣓"),
                hook_type=name
            )
            self.tests[bstack1l1ll11l_opy_][bstack111l1ll_opy_ (u"ࠨࡴࡦࡵࡷࡣࡩࡧࡴࡢࠤࣔ")] = hook_data
            current_test_id = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠢࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠦࣕ"), None)
            if current_test_id:
                hook_data.bstack1lll11l1_opy_(current_test_id)
            if name == bstack111l1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧࣖ"):
                threading.current_thread().before_all_hook_uuid = bstack1l1ll11l_opy_
            threading.current_thread().current_hook_uuid = bstack1l1ll11l_opy_
            bstack1ll11l1l_opy_.bstack1ll1l11l_opy_(bstack111l1ll_opy_ (u"ࠤࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠥࣗ"), hook_data)
        except Exception as e:
            logger.debug(bstack111l1ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡲࡧࡨࡻࡲࡳࡧࡧࠤ࡮ࡴࠠࡴࡶࡤࡶࡹࠦࡨࡰࡱ࡮ࠤࡪࡼࡥ࡯ࡶࡶ࠰ࠥ࡮࡯ࡰ࡭ࠣࡲࡦࡳࡥ࠻ࠢࠨࡷ࠱ࠦࡥࡳࡴࡲࡶ࠿ࠦࠥࡴࠤࣘ"), name, e)
    def bstack1ll111ll_opy_(self, attrs):
        bstack1l1lll1l_opy_ = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨࣙ"), None)
        hook_data = self.tests[bstack1l1lll1l_opy_][bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨࣚ")]
        status = bstack111l1ll_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨࣛ")
        exception = None
        bstack1ll1l111_opy_ = None
        if hook_data.name == bstack111l1ll_opy_ (u"ࠢࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠥࣜ"):
            self.bstack1lll111l_opy_.reset()
            bstack1l1ll1ll_opy_ = self.tests[bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨࣝ"), None)][bstack111l1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬࣞ")].result.result
            if bstack1l1ll1ll_opy_ == bstack111l1ll_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥࣟ"):
                if attrs.hook_failures == 1:
                    status = bstack111l1ll_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦ࣠")
                elif attrs.hook_failures == 2:
                    status = bstack111l1ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ࣡")
            elif attrs.bstack1l1l11l1_opy_:
                status = bstack111l1ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ࣢")
            threading.current_thread().before_all_hook_uuid = None
        else:
            if hook_data.name == bstack111l1ll_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࣣࠫ") and attrs.hook_failures == 1:
                status = bstack111l1ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣࣤ")
            elif hasattr(attrs, bstack111l1ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࡠ࡯ࡨࡷࡸࡧࡧࡦࠩࣥ")) and attrs.error_message:
                status = bstack111l1ll_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࣦࠥ")
            bstack1ll1l111_opy_, exception = self._1l1l1l1l_opy_(attrs)
        bstack1ll1ll11_opy_ = Result(result=status, exception=exception, bstack1ll1lll1_opy_=[bstack1ll1l111_opy_])
        hook_data.stop(time=bstack1l1lllll_opy_(), duration=0, result=bstack1ll1ll11_opy_)
        bstack1ll11l1l_opy_.bstack1ll1l11l_opy_(bstack111l1ll_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ࣧ"), self.tests[bstack1l1lll1l_opy_][bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨࣨ")])
        threading.current_thread().current_hook_uuid = None
    def _1l1l1l1l_opy_(self, attrs):
        try:
            import traceback
            bstack1ll11ll1_opy_ = traceback.format_tb(attrs.exc_traceback)
            bstack1ll1l111_opy_ = bstack1ll11ll1_opy_[-1] if bstack1ll11ll1_opy_ else None
            exception = attrs.exception
        except Exception:
            logger.debug(bstack111l1ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡵࡣࡤࡷࡵࡶࡪࡪࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡤࡷࡶࡸࡴࡳࠠࡵࡴࡤࡧࡪࡨࡡࡤ࡭ࣩࠥ"))
            bstack1ll1l111_opy_ = None
            exception = None
        return bstack1ll1l111_opy_, exception