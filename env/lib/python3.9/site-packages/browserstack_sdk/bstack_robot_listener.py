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
import threading
from uuid import uuid4
from itertools import zip_longest
from collections import OrderedDict
from robot.libraries.BuiltIn import BuiltIn
from browserstack_sdk.bstack11llll11_opy_ import RobotHandler
from bstack_utils.capture import bstack1ll1ll1l_opy_
from bstack_utils.bstack1lll1ll1_opy_ import bstack11ll1l1l_opy_, bstack1l1l11ll_opy_, bstack1lll1111_opy_
from bstack_utils.bstack1ll11l11_opy_ import bstack1l1l1l11_opy_
from bstack_utils.bstack1l1lll11_opy_ import bstack1ll11l1l_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1ll111l1_opy_, bstack1l1lllll_opy_, Result, \
    bstack11l1111l_opy_, bstack1l11lll1_opy_
class bstack_robot_listener:
    ROBOT_LISTENER_API_VERSION = 2
    store = {
        bstack111l1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ࣪"): [],
        bstack111l1ll_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡠࡪࡲࡳࡰࡹࠧ࣫"): [],
        bstack111l1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸ࠭࣬"): []
    }
    bstack1l11l111_opy_ = []
    bstack1l111lll_opy_ = []
    @staticmethod
    def bstack1ll11111_opy_(log):
        if not (log[bstack111l1ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨ࣭ࠫ")] and log[bstack111l1ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩ࣮ࠬ")].strip()):
            return
        active = bstack1l1l1l11_opy_.bstack1ll11lll_opy_()
        log = {
            bstack111l1ll_opy_ (u"ࠬࡲࡥࡷࡧ࡯࣯ࠫ"): log[bstack111l1ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࣰࠬ")],
            bstack111l1ll_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࣱࠪ"): bstack1l11lll1_opy_().isoformat() + bstack111l1ll_opy_ (u"ࠨ࡜ࣲࠪ"),
            bstack111l1ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪࣳ"): log[bstack111l1ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫࣴ")],
        }
        if active:
            if active[bstack111l1ll_opy_ (u"ࠫࡹࡿࡰࡦࠩࣵ")] == bstack111l1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࣶࠪ"):
                log[bstack111l1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ࣷ")] = active[bstack111l1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧࣸ")]
            elif active[bstack111l1ll_opy_ (u"ࠨࡶࡼࡴࡪࣹ࠭")] == bstack111l1ll_opy_ (u"ࠩࡷࡩࡸࡺࣺࠧ"):
                log[bstack111l1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪࣻ")] = active[bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫࣼ")]
        bstack1ll11l1l_opy_.bstack1l1l1ll1_opy_([log])
    def __init__(self):
        self.messages = Messages()
        self._1l1111l1_opy_ = None
        self._11l11lll_opy_ = None
        self._11l1l1ll_opy_ = OrderedDict()
        self.bstack1lll111l_opy_ = bstack1ll1ll1l_opy_(self.bstack1ll11111_opy_)
    @bstack11l1111l_opy_(class_method=True)
    def start_suite(self, name, attrs):
        self.messages.bstack11ll11l1_opy_()
        if not self._11l1l1ll_opy_.get(attrs.get(bstack111l1ll_opy_ (u"ࠬ࡯ࡤࠨࣽ")), None):
            self._11l1l1ll_opy_[attrs.get(bstack111l1ll_opy_ (u"࠭ࡩࡥࠩࣾ"))] = {}
        bstack1l1l1111_opy_ = bstack1lll1111_opy_(
                bstack1l111l11_opy_=attrs.get(bstack111l1ll_opy_ (u"ࠧࡪࡦࠪࣿ")),
                name=name,
                bstack1l1ll111_opy_=bstack1l1lllll_opy_(),
                file_path=os.path.relpath(attrs[bstack111l1ll_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨऀ")], start=os.getcwd()) if attrs.get(bstack111l1ll_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩँ")) != bstack111l1ll_opy_ (u"ࠪࠫं") else bstack111l1ll_opy_ (u"ࠫࠬः"),
                framework=bstack111l1ll_opy_ (u"ࠬࡘ࡯ࡣࡱࡷࠫऄ")
            )
        threading.current_thread().current_suite_id = attrs.get(bstack111l1ll_opy_ (u"࠭ࡩࡥࠩअ"), None)
        self._11l1l1ll_opy_[attrs.get(bstack111l1ll_opy_ (u"ࠧࡪࡦࠪआ"))][bstack111l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫइ")] = bstack1l1l1111_opy_
    @bstack11l1111l_opy_(class_method=True)
    def end_suite(self, name, attrs):
        messages = self.messages.bstack1l11l11l_opy_()
        self._11l11l1l_opy_(messages)
        for bstack11lllll1_opy_ in self.bstack1l11l111_opy_:
            bstack11lllll1_opy_[bstack111l1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫई")][bstack111l1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩउ")].extend(self.store[bstack111l1ll_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡣ࡭ࡵ࡯࡬ࡵࠪऊ")])
            bstack1ll11l1l_opy_.bstack11ll1l11_opy_(bstack11lllll1_opy_)
        self.bstack1l11l111_opy_ = []
        self.store[bstack111l1ll_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰࡤ࡮࡯ࡰ࡭ࡶࠫऋ")] = []
    @bstack11l1111l_opy_(class_method=True)
    def start_test(self, name, attrs):
        self.bstack1lll111l_opy_.start()
        if not self._11l1l1ll_opy_.get(attrs.get(bstack111l1ll_opy_ (u"࠭ࡩࡥࠩऌ")), None):
            self._11l1l1ll_opy_[attrs.get(bstack111l1ll_opy_ (u"ࠧࡪࡦࠪऍ"))] = {}
        driver = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧऎ"), None)
        bstack1lll1ll1_opy_ = bstack1lll1111_opy_(
            bstack1l111l11_opy_=attrs.get(bstack111l1ll_opy_ (u"ࠩ࡬ࡨࠬए")),
            name=name,
            bstack1l1ll111_opy_=bstack1l1lllll_opy_(),
            file_path=os.path.relpath(attrs[bstack111l1ll_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪऐ")], start=os.getcwd()),
            scope=RobotHandler.bstack1l11l1l1_opy_(attrs.get(bstack111l1ll_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫऑ"), None)),
            framework=bstack111l1ll_opy_ (u"ࠬࡘ࡯ࡣࡱࡷࠫऒ"),
            tags=attrs[bstack111l1ll_opy_ (u"࠭ࡴࡢࡩࡶࠫओ")],
            hooks=self.store[bstack111l1ll_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࡟ࡩࡱࡲ࡯ࡸ࠭औ")],
            bstack1llll111_opy_=bstack1ll11l1l_opy_.bstack1lll1l1l_opy_(driver) if driver and driver.session_id else {},
            meta={},
            code=bstack111l1ll_opy_ (u"ࠣࡽࢀࠤࡡࡴࠠࡼࡿࠥक").format(bstack111l1ll_opy_ (u"ࠤࠣࠦख").join(attrs[bstack111l1ll_opy_ (u"ࠪࡸࡦ࡭ࡳࠨग")]), name) if attrs[bstack111l1ll_opy_ (u"ࠫࡹࡧࡧࡴࠩघ")] else name
        )
        self._11l1l1ll_opy_[attrs.get(bstack111l1ll_opy_ (u"ࠬ࡯ࡤࠨङ"))][bstack111l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩच")] = bstack1lll1ll1_opy_
        threading.current_thread().current_test_uuid = bstack1lll1ll1_opy_.bstack1l111l1l_opy_()
        threading.current_thread().current_test_id = attrs.get(bstack111l1ll_opy_ (u"ࠧࡪࡦࠪछ"), None)
        self.bstack1ll1l11l_opy_(bstack111l1ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩज"), bstack1lll1ll1_opy_)
    @bstack11l1111l_opy_(class_method=True)
    def end_test(self, name, attrs):
        self.bstack1lll111l_opy_.reset()
        bstack11ll1111_opy_ = bstack11lll111_opy_.get(attrs.get(bstack111l1ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩझ")), bstack111l1ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫञ"))
        self._11l1l1ll_opy_[attrs.get(bstack111l1ll_opy_ (u"ࠫ࡮ࡪࠧट"))][bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨठ")].stop(time=bstack1l1lllll_opy_(), duration=int(attrs.get(bstack111l1ll_opy_ (u"࠭ࡥ࡭ࡣࡳࡷࡪࡪࡴࡪ࡯ࡨࠫड"), bstack111l1ll_opy_ (u"ࠧ࠱ࠩढ"))), result=Result(result=bstack11ll1111_opy_, exception=attrs.get(bstack111l1ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩण")), bstack1ll1lll1_opy_=[attrs.get(bstack111l1ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪत"))]))
        self.bstack1ll1l11l_opy_(bstack111l1ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬथ"), self._11l1l1ll_opy_[attrs.get(bstack111l1ll_opy_ (u"ࠫ࡮ࡪࠧद"))][bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨध")], True)
        self.store[bstack111l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠪन")] = []
        threading.current_thread().current_test_uuid = None
        threading.current_thread().current_test_id = None
    @bstack11l1111l_opy_(class_method=True)
    def start_keyword(self, name, attrs):
        self.messages.bstack11ll11l1_opy_()
        current_test_id = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡥࠩऩ"), None)
        bstack11l1l11l_opy_ = current_test_id if bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡦࠪप"), None) else bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡷࡺ࡯ࡴࡦࡡ࡬ࡨࠬफ"), None)
        if attrs.get(bstack111l1ll_opy_ (u"ࠪࡸࡾࡶࡥࠨब"), bstack111l1ll_opy_ (u"ࠫࠬभ")).lower() in [bstack111l1ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫम"), bstack111l1ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨय")]:
            hook_type = bstack1l1111ll_opy_(attrs.get(bstack111l1ll_opy_ (u"ࠧࡵࡻࡳࡩࠬर")), bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬऱ"), None))
            hook_name = bstack111l1ll_opy_ (u"ࠩࡾࢁࠬल").format(attrs.get(bstack111l1ll_opy_ (u"ࠪ࡯ࡼࡴࡡ࡮ࡧࠪळ"), bstack111l1ll_opy_ (u"ࠫࠬऴ")))
            if hook_type in [bstack111l1ll_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩव"), bstack111l1ll_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡇࡌࡍࠩश")]:
                hook_name = bstack111l1ll_opy_ (u"ࠧ࡜ࡽࢀࡡࠥࢁࡽࠨष").format(bstack11l1lll1_opy_.get(hook_type), attrs.get(bstack111l1ll_opy_ (u"ࠨ࡭ࡺࡲࡦࡳࡥࠨस"), bstack111l1ll_opy_ (u"ࠩࠪह")))
            bstack11ll111l_opy_ = bstack1l1l11ll_opy_(
                bstack1l111l11_opy_=bstack11l1l11l_opy_ + bstack111l1ll_opy_ (u"ࠪ࠱ࠬऺ") + attrs.get(bstack111l1ll_opy_ (u"ࠫࡹࡿࡰࡦࠩऻ"), bstack111l1ll_opy_ (u"़ࠬ࠭")).lower(),
                name=hook_name,
                bstack1l1ll111_opy_=bstack1l1lllll_opy_(),
                file_path=os.path.relpath(attrs.get(bstack111l1ll_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ऽ")), start=os.getcwd()),
                framework=bstack111l1ll_opy_ (u"ࠧࡓࡱࡥࡳࡹ࠭ा"),
                tags=attrs[bstack111l1ll_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ि")],
                scope=RobotHandler.bstack1l11l1l1_opy_(attrs.get(bstack111l1ll_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩी"), None)),
                hook_type=hook_type,
                meta={}
            )
            threading.current_thread().current_hook_uuid = bstack11ll111l_opy_.bstack1l111l1l_opy_()
            threading.current_thread().current_hook_id = bstack11l1l11l_opy_ + bstack111l1ll_opy_ (u"ࠪ࠱ࠬु") + attrs.get(bstack111l1ll_opy_ (u"ࠫࡹࡿࡰࡦࠩू"), bstack111l1ll_opy_ (u"ࠬ࠭ृ")).lower()
            self.store[bstack111l1ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪॄ")] = [bstack11ll111l_opy_.bstack1l111l1l_opy_()]
            if bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫॅ"), None):
                self.store[bstack111l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࠬॆ")].append(bstack11ll111l_opy_.bstack1l111l1l_opy_())
            else:
                self.store[bstack111l1ll_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭ࡡ࡫ࡳࡴࡱࡳࠨे")].append(bstack11ll111l_opy_.bstack1l111l1l_opy_())
            if bstack11l1l11l_opy_:
                self._11l1l1ll_opy_[bstack11l1l11l_opy_ + bstack111l1ll_opy_ (u"ࠪ࠱ࠬै") + attrs.get(bstack111l1ll_opy_ (u"ࠫࡹࡿࡰࡦࠩॉ"), bstack111l1ll_opy_ (u"ࠬ࠭ॊ")).lower()] = { bstack111l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩो"): bstack11ll111l_opy_ }
            bstack1ll11l1l_opy_.bstack1ll1l11l_opy_(bstack111l1ll_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨौ"), bstack11ll111l_opy_)
        else:
            bstack1ll1l1ll_opy_ = {
                bstack111l1ll_opy_ (u"ࠨ࡫ࡧ्ࠫ"): uuid4().__str__(),
                bstack111l1ll_opy_ (u"ࠩࡷࡩࡽࡺࠧॎ"): bstack111l1ll_opy_ (u"ࠪࡿࢂࠦࡻࡾࠩॏ").format(attrs.get(bstack111l1ll_opy_ (u"ࠫࡰࡽ࡮ࡢ࡯ࡨࠫॐ")), attrs.get(bstack111l1ll_opy_ (u"ࠬࡧࡲࡨࡵࠪ॑"), bstack111l1ll_opy_ (u"॒࠭ࠧ"))) if attrs.get(bstack111l1ll_opy_ (u"ࠧࡢࡴࡪࡷࠬ॓"), []) else attrs.get(bstack111l1ll_opy_ (u"ࠨ࡭ࡺࡲࡦࡳࡥࠨ॔")),
                bstack111l1ll_opy_ (u"ࠩࡶࡸࡪࡶ࡟ࡢࡴࡪࡹࡲ࡫࡮ࡵࠩॕ"): attrs.get(bstack111l1ll_opy_ (u"ࠪࡥࡷ࡭ࡳࠨॖ"), []),
                bstack111l1ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨॗ"): bstack1l1lllll_opy_(),
                bstack111l1ll_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬक़"): bstack111l1ll_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧख़"),
                bstack111l1ll_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬग़"): attrs.get(bstack111l1ll_opy_ (u"ࠨࡦࡲࡧࠬज़"), bstack111l1ll_opy_ (u"ࠩࠪड़"))
            }
            if attrs.get(bstack111l1ll_opy_ (u"ࠪࡰ࡮ࡨ࡮ࡢ࡯ࡨࠫढ़"), bstack111l1ll_opy_ (u"ࠫࠬफ़")) != bstack111l1ll_opy_ (u"ࠬ࠭य़"):
                bstack1ll1l1ll_opy_[bstack111l1ll_opy_ (u"࠭࡫ࡦࡻࡺࡳࡷࡪࠧॠ")] = attrs.get(bstack111l1ll_opy_ (u"ࠧ࡭࡫ࡥࡲࡦࡳࡥࠨॡ"))
            if not self.bstack1l111lll_opy_:
                self._11l1l1ll_opy_[self._11l1ll1l_opy_()][bstack111l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫॢ")].add_step(bstack1ll1l1ll_opy_)
                threading.current_thread().current_step_uuid = bstack1ll1l1ll_opy_[bstack111l1ll_opy_ (u"ࠩ࡬ࡨࠬॣ")]
            self.bstack1l111lll_opy_.append(bstack1ll1l1ll_opy_)
    @bstack11l1111l_opy_(class_method=True)
    def end_keyword(self, name, attrs):
        messages = self.messages.bstack1l11l11l_opy_()
        self._11l11l1l_opy_(messages)
        current_test_id = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡨࠬ।"), None)
        bstack11l1l11l_opy_ = current_test_id if current_test_id else bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡹࡵࡪࡶࡨࡣ࡮ࡪࠧ॥"), None)
        bstack11lll11l_opy_ = bstack11lll111_opy_.get(attrs.get(bstack111l1ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ०")), bstack111l1ll_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧ१"))
        bstack1l11ll1l_opy_ = attrs.get(bstack111l1ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ२"))
        if bstack11lll11l_opy_ != bstack111l1ll_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩ३") and not attrs.get(bstack111l1ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ४")) and self._1l1111l1_opy_:
            bstack1l11ll1l_opy_ = self._1l1111l1_opy_
        bstack1ll1ll11_opy_ = Result(result=bstack11lll11l_opy_, exception=bstack1l11ll1l_opy_, bstack1ll1lll1_opy_=[bstack1l11ll1l_opy_])
        if attrs.get(bstack111l1ll_opy_ (u"ࠪࡸࡾࡶࡥࠨ५"), bstack111l1ll_opy_ (u"ࠫࠬ६")).lower() in [bstack111l1ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ७"), bstack111l1ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ८")]:
            bstack11l1l11l_opy_ = current_test_id if current_test_id else bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡵࡸ࡭ࡹ࡫࡟ࡪࡦࠪ९"), None)
            if bstack11l1l11l_opy_:
                bstack1l1lll1l_opy_ = bstack11l1l11l_opy_ + bstack111l1ll_opy_ (u"ࠣ࠯ࠥ॰") + attrs.get(bstack111l1ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧॱ"), bstack111l1ll_opy_ (u"ࠪࠫॲ")).lower()
                self._11l1l1ll_opy_[bstack1l1lll1l_opy_][bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧॳ")].stop(time=bstack1l1lllll_opy_(), duration=int(attrs.get(bstack111l1ll_opy_ (u"ࠬ࡫࡬ࡢࡲࡶࡩࡩࡺࡩ࡮ࡧࠪॴ"), bstack111l1ll_opy_ (u"࠭࠰ࠨॵ"))), result=bstack1ll1ll11_opy_)
                bstack1ll11l1l_opy_.bstack1ll1l11l_opy_(bstack111l1ll_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩॶ"), self._11l1l1ll_opy_[bstack1l1lll1l_opy_][bstack111l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫॷ")])
        else:
            bstack11l1l11l_opy_ = current_test_id if current_test_id else bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠ࡫ࡧࠫॸ"), None)
            if bstack11l1l11l_opy_ and len(self.bstack1l111lll_opy_) == 1:
                current_step_uuid = bstack1ll111l1_opy_(threading.current_thread(), bstack111l1ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡸࡺࡥࡱࡡࡸࡹ࡮ࡪࠧॹ"), None)
                self._11l1l1ll_opy_[bstack11l1l11l_opy_][bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧॺ")].bstack1l1ll1l1_opy_(current_step_uuid, duration=int(attrs.get(bstack111l1ll_opy_ (u"ࠬ࡫࡬ࡢࡲࡶࡩࡩࡺࡩ࡮ࡧࠪॻ"), bstack111l1ll_opy_ (u"࠭࠰ࠨॼ"))), result=bstack1ll1ll11_opy_)
            else:
                self.bstack11llll1l_opy_(attrs)
            self.bstack1l111lll_opy_.pop()
    def log_message(self, message):
        try:
            if message.get(bstack111l1ll_opy_ (u"ࠧࡩࡶࡰࡰࠬॽ"), bstack111l1ll_opy_ (u"ࠨࡰࡲࠫॾ")) == bstack111l1ll_opy_ (u"ࠩࡼࡩࡸ࠭ॿ"):
                return
            self.messages.push(message)
            bstack11l111ll_opy_ = []
            if bstack1l1l1l11_opy_.bstack1ll11lll_opy_():
                bstack11l111ll_opy_.append({
                    bstack111l1ll_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ঀ"): bstack1l1lllll_opy_(),
                    bstack111l1ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬঁ"): message.get(bstack111l1ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ং")),
                    bstack111l1ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬঃ"): message.get(bstack111l1ll_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭঄")),
                    **bstack1l1l1l11_opy_.bstack1ll11lll_opy_()
                })
                if len(bstack11l111ll_opy_) > 0:
                    bstack1ll11l1l_opy_.bstack1l1l1ll1_opy_(bstack11l111ll_opy_)
        except Exception as err:
            pass
    def close(self):
        bstack1ll11l1l_opy_.bstack1l111ll1_opy_()
    def bstack11llll1l_opy_(self, bstack1l1l111l_opy_):
        if not bstack1l1l1l11_opy_.bstack1ll11lll_opy_():
            return
        kwname = bstack111l1ll_opy_ (u"ࠨࡽࢀࠤࢀࢃࠧঅ").format(bstack1l1l111l_opy_.get(bstack111l1ll_opy_ (u"ࠩ࡮ࡻࡳࡧ࡭ࡦࠩআ")), bstack1l1l111l_opy_.get(bstack111l1ll_opy_ (u"ࠪࡥࡷ࡭ࡳࠨই"), bstack111l1ll_opy_ (u"ࠫࠬঈ"))) if bstack1l1l111l_opy_.get(bstack111l1ll_opy_ (u"ࠬࡧࡲࡨࡵࠪউ"), []) else bstack1l1l111l_opy_.get(bstack111l1ll_opy_ (u"࠭࡫ࡸࡰࡤࡱࡪ࠭ঊ"))
        error_message = bstack111l1ll_opy_ (u"ࠢ࡬ࡹࡱࡥࡲ࡫࠺ࠡ࡞ࠥࡿ࠵ࢃ࡜ࠣࠢࡿࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࡢࠢࡼ࠳ࢀࡠࠧࠦࡼࠡࡧࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࡢࠢࡼ࠴ࢀࡠࠧࠨঋ").format(kwname, bstack1l1l111l_opy_.get(bstack111l1ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨঌ")), str(bstack1l1l111l_opy_.get(bstack111l1ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ঍"))))
        bstack11l11ll1_opy_ = bstack111l1ll_opy_ (u"ࠥ࡯ࡼࡴࡡ࡮ࡧ࠽ࠤࡡࠨࡻ࠱ࡿ࡟ࠦࠥࢂࠠࡴࡶࡤࡸࡺࡹ࠺ࠡ࡞ࠥࡿ࠶ࢃ࡜ࠣࠤ঎").format(kwname, bstack1l1l111l_opy_.get(bstack111l1ll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫএ")))
        bstack1l11l1ll_opy_ = error_message if bstack1l1l111l_opy_.get(bstack111l1ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ঐ")) else bstack11l11ll1_opy_
        bstack1l11111l_opy_ = {
            bstack111l1ll_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ঑"): self.bstack1l111lll_opy_[-1].get(bstack111l1ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ঒"), bstack1l1lllll_opy_()),
            bstack111l1ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩও"): bstack1l11l1ll_opy_,
            bstack111l1ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨঔ"): bstack111l1ll_opy_ (u"ࠪࡉࡗࡘࡏࡓࠩক") if bstack1l1l111l_opy_.get(bstack111l1ll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫখ")) == bstack111l1ll_opy_ (u"ࠬࡌࡁࡊࡎࠪগ") else bstack111l1ll_opy_ (u"࠭ࡉࡏࡈࡒࠫঘ"),
            **bstack1l1l1l11_opy_.bstack1ll11lll_opy_()
        }
        bstack1ll11l1l_opy_.bstack1l1l1ll1_opy_([bstack1l11111l_opy_])
    def _11l1ll1l_opy_(self):
        for bstack1l111l11_opy_ in reversed(self._11l1l1ll_opy_):
            bstack11l1l1l1_opy_ = bstack1l111l11_opy_
            data = self._11l1l1ll_opy_[bstack1l111l11_opy_][bstack111l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪঙ")]
            if isinstance(data, bstack1l1l11ll_opy_):
                if not bstack111l1ll_opy_ (u"ࠨࡇࡄࡇࡍ࠭চ") in data.bstack11lll1ll_opy_():
                    return bstack11l1l1l1_opy_
            else:
                return bstack11l1l1l1_opy_
    def _11l11l1l_opy_(self, messages):
        try:
            bstack11l1ll11_opy_ = BuiltIn().get_variable_value(bstack111l1ll_opy_ (u"ࠤࠧࡿࡑࡕࡇࠡࡎࡈ࡚ࡊࡒࡽࠣছ")) in (bstack1l111111_opy_.DEBUG, bstack1l111111_opy_.TRACE)
            for message, bstack11llllll_opy_ in zip_longest(messages, messages[1:]):
                name = message.get(bstack111l1ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫজ"))
                level = message.get(bstack111l1ll_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪঝ"))
                if level == bstack1l111111_opy_.FAIL:
                    self._1l1111l1_opy_ = name or self._1l1111l1_opy_
                    self._11l11lll_opy_ = bstack11llllll_opy_.get(bstack111l1ll_opy_ (u"ࠧࡳࡥࡴࡵࡤ࡫ࡪࠨঞ")) if bstack11l1ll11_opy_ and bstack11llllll_opy_ else self._11l11lll_opy_
        except:
            pass
    @classmethod
    def bstack1ll1l11l_opy_(self, event: str, bstack1l11ll11_opy_: bstack11ll1l1l_opy_, bstack11ll1ll1_opy_=False):
        if event == bstack111l1ll_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨট"):
            bstack1l11ll11_opy_.set(hooks=self.store[bstack111l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠫঠ")])
        if event == bstack111l1ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩড"):
            event = bstack111l1ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫঢ")
        if bstack11ll1ll1_opy_:
            bstack1l11llll_opy_ = {
                bstack111l1ll_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧণ"): event,
                bstack1l11ll11_opy_.bstack11ll1lll_opy_(): bstack1l11ll11_opy_.bstack11ll11ll_opy_(event)
            }
            self.bstack1l11l111_opy_.append(bstack1l11llll_opy_)
        else:
            bstack1ll11l1l_opy_.bstack1ll1l11l_opy_(event, bstack1l11ll11_opy_)
class Messages:
    def __init__(self):
        self._11l1llll_opy_ = []
    def bstack11ll11l1_opy_(self):
        self._11l1llll_opy_.append([])
    def bstack1l11l11l_opy_(self):
        return self._11l1llll_opy_.pop() if self._11l1llll_opy_ else list()
    def push(self, message):
        self._11l1llll_opy_[-1].append(message) if self._11l1llll_opy_ else self._11l1llll_opy_.append([message])
class bstack1l111111_opy_:
    FAIL = bstack111l1ll_opy_ (u"ࠫࡋࡇࡉࡍࠩত")
    ERROR = bstack111l1ll_opy_ (u"ࠬࡋࡒࡓࡑࡕࠫথ")
    WARNING = bstack111l1ll_opy_ (u"࠭ࡗࡂࡔࡑࠫদ")
    bstack11lll1l1_opy_ = bstack111l1ll_opy_ (u"ࠧࡊࡐࡉࡓࠬধ")
    DEBUG = bstack111l1ll_opy_ (u"ࠨࡆࡈࡆ࡚ࡍࠧন")
    TRACE = bstack111l1ll_opy_ (u"ࠩࡗࡖࡆࡉࡅࠨ঩")
    bstack11l111l1_opy_ = [FAIL, ERROR]
def bstack11l1l111_opy_(bstack11l11l11_opy_):
    if not bstack11l11l11_opy_:
        return None
    if bstack11l11l11_opy_.get(bstack111l1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭প"), None):
        return getattr(bstack11l11l11_opy_[bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧফ")], bstack111l1ll_opy_ (u"ࠬࡻࡵࡪࡦࠪব"), None)
    return bstack11l11l11_opy_.get(bstack111l1ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫভ"), None)
def bstack1l1111ll_opy_(hook_type, current_test_uuid):
    if hook_type.lower() not in [bstack111l1ll_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ম"), bstack111l1ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪয")]:
        return
    if hook_type.lower() == bstack111l1ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨর"):
        if current_test_uuid is None:
            return bstack111l1ll_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡅࡑࡒࠧ঱")
        else:
            return bstack111l1ll_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩল")
    elif hook_type.lower() == bstack111l1ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧ঳"):
        if current_test_uuid is None:
            return bstack111l1ll_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡇࡌࡍࠩ঴")
        else:
            return bstack111l1ll_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫ঵")