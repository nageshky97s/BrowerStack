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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack1llllll1l11_opy_
from browserstack_sdk.bstack1111ll1l_opy_ import bstack111l111l_opy_
def _1llll1lllll_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack1llll1lll11_opy_:
    def __init__(self, handler):
        self._1lllll11l1l_opy_ = {}
        self._1lllll11l11_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack111l111l_opy_.version()
        if bstack1llllll1l11_opy_(pytest_version, bstack111l1ll_opy_ (u"ࠢ࠹࠰࠴࠲࠶ࠨᔎ")) >= 0:
            self._1lllll11l1l_opy_[bstack111l1ll_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᔏ")] = Module._register_setup_function_fixture
            self._1lllll11l1l_opy_[bstack111l1ll_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᔐ")] = Module._register_setup_module_fixture
            self._1lllll11l1l_opy_[bstack111l1ll_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᔑ")] = Class._register_setup_class_fixture
            self._1lllll11l1l_opy_[bstack111l1ll_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᔒ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack1llll1ll1l1_opy_(bstack111l1ll_opy_ (u"ࠬ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᔓ"))
            Module._register_setup_module_fixture = self.bstack1llll1ll1l1_opy_(bstack111l1ll_opy_ (u"࠭࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᔔ"))
            Class._register_setup_class_fixture = self.bstack1llll1ll1l1_opy_(bstack111l1ll_opy_ (u"ࠧࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᔕ"))
            Class._register_setup_method_fixture = self.bstack1llll1ll1l1_opy_(bstack111l1ll_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᔖ"))
        else:
            self._1lllll11l1l_opy_[bstack111l1ll_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᔗ")] = Module._inject_setup_function_fixture
            self._1lllll11l1l_opy_[bstack111l1ll_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᔘ")] = Module._inject_setup_module_fixture
            self._1lllll11l1l_opy_[bstack111l1ll_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᔙ")] = Class._inject_setup_class_fixture
            self._1lllll11l1l_opy_[bstack111l1ll_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᔚ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack1llll1ll1l1_opy_(bstack111l1ll_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᔛ"))
            Module._inject_setup_module_fixture = self.bstack1llll1ll1l1_opy_(bstack111l1ll_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᔜ"))
            Class._inject_setup_class_fixture = self.bstack1llll1ll1l1_opy_(bstack111l1ll_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᔝ"))
            Class._inject_setup_method_fixture = self.bstack1llll1ll1l1_opy_(bstack111l1ll_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᔞ"))
    def bstack1llll1ll111_opy_(self, bstack1llll1lll1l_opy_, hook_type):
        bstack1lllll11111_opy_ = id(bstack1llll1lll1l_opy_.__class__)
        if (bstack1lllll11111_opy_, hook_type) in self._1lllll11l11_opy_:
            return
        meth = getattr(bstack1llll1lll1l_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._1lllll11l11_opy_[(bstack1lllll11111_opy_, hook_type)] = meth
            setattr(bstack1llll1lll1l_opy_, hook_type, self.bstack1lllll111ll_opy_(hook_type, bstack1lllll11111_opy_))
    def bstack1lllll111l1_opy_(self, instance, bstack1llll1l1ll1_opy_):
        if bstack1llll1l1ll1_opy_ == bstack111l1ll_opy_ (u"ࠥࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪࠨᔟ"):
            self.bstack1llll1ll111_opy_(instance.obj, bstack111l1ll_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠧᔠ"))
            self.bstack1llll1ll111_opy_(instance.obj, bstack111l1ll_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠤᔡ"))
        if bstack1llll1l1ll1_opy_ == bstack111l1ll_opy_ (u"ࠨ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠢᔢ"):
            self.bstack1llll1ll111_opy_(instance.obj, bstack111l1ll_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࠨᔣ"))
            self.bstack1llll1ll111_opy_(instance.obj, bstack111l1ll_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠥᔤ"))
        if bstack1llll1l1ll1_opy_ == bstack111l1ll_opy_ (u"ࠤࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠤᔥ"):
            self.bstack1llll1ll111_opy_(instance.obj, bstack111l1ll_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠣᔦ"))
            self.bstack1llll1ll111_opy_(instance.obj, bstack111l1ll_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠧᔧ"))
        if bstack1llll1l1ll1_opy_ == bstack111l1ll_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࠨᔨ"):
            self.bstack1llll1ll111_opy_(instance.obj, bstack111l1ll_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠧᔩ"))
            self.bstack1llll1ll111_opy_(instance.obj, bstack111l1ll_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠤᔪ"))
    @staticmethod
    def bstack1llll1llll1_opy_(hook_type, func, args):
        if hook_type in [bstack111l1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧᔫ"), bstack111l1ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫᔬ")]:
            _1llll1lllll_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack1lllll111ll_opy_(self, hook_type, bstack1lllll11111_opy_):
        def bstack1llll1ll1ll_opy_(arg=None):
            self.handler(hook_type, bstack111l1ll_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪᔭ"))
            result = None
            try:
                bstack1llll1ll11l_opy_ = self._1lllll11l11_opy_[(bstack1lllll11111_opy_, hook_type)]
                self.bstack1llll1llll1_opy_(hook_type, bstack1llll1ll11l_opy_, (arg,))
                result = Result(result=bstack111l1ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᔮ"))
            except Exception as e:
                result = Result(result=bstack111l1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᔯ"), exception=e)
                self.handler(hook_type, bstack111l1ll_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬᔰ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack111l1ll_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ᔱ"), result)
        def bstack1lllll11ll1_opy_(this, arg=None):
            self.handler(hook_type, bstack111l1ll_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨᔲ"))
            result = None
            exception = None
            try:
                self.bstack1llll1llll1_opy_(hook_type, self._1lllll11l11_opy_[hook_type], (this, arg))
                result = Result(result=bstack111l1ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᔳ"))
            except Exception as e:
                result = Result(result=bstack111l1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᔴ"), exception=e)
                self.handler(hook_type, bstack111l1ll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪᔵ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack111l1ll_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫᔶ"), result)
        if hook_type in [bstack111l1ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠬᔷ"), bstack111l1ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩᔸ")]:
            return bstack1lllll11ll1_opy_
        return bstack1llll1ll1ll_opy_
    def bstack1llll1ll1l1_opy_(self, bstack1llll1l1ll1_opy_):
        def bstack1lllll1111l_opy_(this, *args, **kwargs):
            self.bstack1lllll111l1_opy_(this, bstack1llll1l1ll1_opy_)
            self._1lllll11l1l_opy_[bstack1llll1l1ll1_opy_](this, *args, **kwargs)
        return bstack1lllll1111l_opy_