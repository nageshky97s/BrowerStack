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
from uuid import uuid4
from bstack_utils.helper import bstack1l1lllll_opy_, bstack1111l11l1l_opy_
from bstack_utils.bstack1l11ll111l_opy_ import bstack1ll1ll1ll1l_opy_
class bstack11ll1l1l_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, bstack1l1ll111_opy_=None, framework=None, tags=[], scope=[], bstack1ll1l1l11ll_opy_=None, bstack1ll1l1l11l1_opy_=True, bstack1ll1l11l1l1_opy_=None, bstack11l1111111_opy_=None, result=None, duration=None, bstack1l111l11_opy_=None, meta={}):
        self.bstack1l111l11_opy_ = bstack1l111l11_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack1ll1l1l11l1_opy_:
            self.uuid = uuid4().__str__()
        self.bstack1l1ll111_opy_ = bstack1l1ll111_opy_
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack1ll1l1l11ll_opy_ = bstack1ll1l1l11ll_opy_
        self.bstack1ll1l11l1l1_opy_ = bstack1ll1l11l1l1_opy_
        self.bstack11l1111111_opy_ = bstack11l1111111_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1l111l1l_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack1l1llll1_opy_(self, meta):
        self.meta = meta
    def bstack1l1l1lll_opy_(self, hooks):
        self.hooks = hooks
    def bstack1ll1l11l11l_opy_(self):
        bstack1ll1l1l111l_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack111l1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪᚫ"): bstack1ll1l1l111l_opy_,
            bstack111l1ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪᚬ"): bstack1ll1l1l111l_opy_,
            bstack111l1ll_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧᚭ"): bstack1ll1l1l111l_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack111l1ll_opy_ (u"࡙ࠥࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡹࡲ࡫࡮ࡵ࠼ࠣࠦᚮ") + key)
            setattr(self, key, val)
    def bstack1ll1l111l11_opy_(self):
        return {
            bstack111l1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᚯ"): self.name,
            bstack111l1ll_opy_ (u"ࠬࡨ࡯ࡥࡻࠪᚰ"): {
                bstack111l1ll_opy_ (u"࠭࡬ࡢࡰࡪࠫᚱ"): bstack111l1ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧᚲ"),
                bstack111l1ll_opy_ (u"ࠨࡥࡲࡨࡪ࠭ᚳ"): self.code
            },
            bstack111l1ll_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩᚴ"): self.scope,
            bstack111l1ll_opy_ (u"ࠪࡸࡦ࡭ࡳࠨᚵ"): self.tags,
            bstack111l1ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᚶ"): self.framework,
            bstack111l1ll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᚷ"): self.bstack1l1ll111_opy_
        }
    def bstack1ll1l11ll11_opy_(self):
        return {
         bstack111l1ll_opy_ (u"࠭࡭ࡦࡶࡤࠫᚸ"): self.meta
        }
    def bstack1ll1l11l111_opy_(self):
        return {
            bstack111l1ll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪᚹ"): {
                bstack111l1ll_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬᚺ"): self.bstack1ll1l1l11ll_opy_
            }
        }
    def bstack1ll1l11lll1_opy_(self, bstack1ll1l111l1l_opy_, details):
        step = next(filter(lambda st: st[bstack111l1ll_opy_ (u"ࠩ࡬ࡨࠬᚻ")] == bstack1ll1l111l1l_opy_, self.meta[bstack111l1ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᚼ")]), None)
        step.update(details)
    def bstack1lll1l11_opy_(self, bstack1ll1l111l1l_opy_):
        step = next(filter(lambda st: st[bstack111l1ll_opy_ (u"ࠫ࡮ࡪࠧᚽ")] == bstack1ll1l111l1l_opy_, self.meta[bstack111l1ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᚾ")]), None)
        step.update({
            bstack111l1ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᚿ"): bstack1l1lllll_opy_()
        })
    def bstack1l1ll1l1_opy_(self, bstack1ll1l111l1l_opy_, result, duration=None):
        bstack1ll1l11l1l1_opy_ = bstack1l1lllll_opy_()
        if bstack1ll1l111l1l_opy_ is not None and self.meta.get(bstack111l1ll_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ᛀ")):
            step = next(filter(lambda st: st[bstack111l1ll_opy_ (u"ࠨ࡫ࡧࠫᛁ")] == bstack1ll1l111l1l_opy_, self.meta[bstack111l1ll_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᛂ")]), None)
            step.update({
                bstack111l1ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᛃ"): bstack1ll1l11l1l1_opy_,
                bstack111l1ll_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ᛄ"): duration if duration else bstack1111l11l1l_opy_(step[bstack111l1ll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᛅ")], bstack1ll1l11l1l1_opy_),
                bstack111l1ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᛆ"): result.result,
                bstack111l1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨᛇ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack1ll1l111lll_opy_):
        if self.meta.get(bstack111l1ll_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᛈ")):
            self.meta[bstack111l1ll_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᛉ")].append(bstack1ll1l111lll_opy_)
        else:
            self.meta[bstack111l1ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᛊ")] = [ bstack1ll1l111lll_opy_ ]
    def bstack1ll1l111ll1_opy_(self):
        return {
            bstack111l1ll_opy_ (u"ࠫࡺࡻࡩࡥࠩᛋ"): self.bstack1l111l1l_opy_(),
            **self.bstack1ll1l111l11_opy_(),
            **self.bstack1ll1l11l11l_opy_(),
            **self.bstack1ll1l11ll11_opy_()
        }
    def bstack1ll1l11l1ll_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack111l1ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᛌ"): self.bstack1ll1l11l1l1_opy_,
            bstack111l1ll_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧᛍ"): self.duration,
            bstack111l1ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᛎ"): self.result.result
        }
        if data[bstack111l1ll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᛏ")] == bstack111l1ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᛐ"):
            data[bstack111l1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩᛑ")] = self.result.bstack1lllll1l1_opy_()
            data[bstack111l1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬᛒ")] = [{bstack111l1ll_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᛓ"): self.result.bstack1111l11ll1_opy_()}]
        return data
    def bstack1ll1l1l1ll1_opy_(self):
        return {
            bstack111l1ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᛔ"): self.bstack1l111l1l_opy_(),
            **self.bstack1ll1l111l11_opy_(),
            **self.bstack1ll1l11l11l_opy_(),
            **self.bstack1ll1l11l1ll_opy_(),
            **self.bstack1ll1l11ll11_opy_()
        }
    def bstack11ll11ll_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack111l1ll_opy_ (u"ࠧࡔࡶࡤࡶࡹ࡫ࡤࠨᛕ") in event:
            return self.bstack1ll1l111ll1_opy_()
        elif bstack111l1ll_opy_ (u"ࠨࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᛖ") in event:
            return self.bstack1ll1l1l1ll1_opy_()
    def bstack11ll1lll_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll1l11l1l1_opy_ = time if time else bstack1l1lllll_opy_()
        self.duration = duration if duration else bstack1111l11l1l_opy_(self.bstack1l1ll111_opy_, self.bstack1ll1l11l1l1_opy_)
        if result:
            self.result = result
class bstack1lll1111_opy_(bstack11ll1l1l_opy_):
    def __init__(self, hooks=[], bstack1llll111_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1llll111_opy_ = bstack1llll111_opy_
        super().__init__(*args, **kwargs, bstack11l1111111_opy_=bstack111l1ll_opy_ (u"ࠩࡷࡩࡸࡺࠧᛗ"))
    @classmethod
    def bstack1ll1l11llll_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack111l1ll_opy_ (u"ࠪ࡭ࡩ࠭ᛘ"): id(step),
                bstack111l1ll_opy_ (u"ࠫࡹ࡫ࡸࡵࠩᛙ"): step.name,
                bstack111l1ll_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭ᛚ"): step.keyword,
            })
        return bstack1lll1111_opy_(
            **kwargs,
            meta={
                bstack111l1ll_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࠧᛛ"): {
                    bstack111l1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᛜ"): feature.name,
                    bstack111l1ll_opy_ (u"ࠨࡲࡤࡸ࡭࠭ᛝ"): feature.filename,
                    bstack111l1ll_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧᛞ"): feature.description
                },
                bstack111l1ll_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬᛟ"): {
                    bstack111l1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᛠ"): scenario.name
                },
                bstack111l1ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᛡ"): steps,
                bstack111l1ll_opy_ (u"࠭ࡥࡹࡣࡰࡴࡱ࡫ࡳࠨᛢ"): bstack1ll1ll1ll1l_opy_(test)
            }
        )
    def bstack1ll1l1l1l1l_opy_(self):
        return {
            bstack111l1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᛣ"): self.hooks
        }
    def bstack1ll1l11ll1l_opy_(self):
        if self.bstack1llll111_opy_:
            return {
                bstack111l1ll_opy_ (u"ࠨ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠧᛤ"): self.bstack1llll111_opy_
            }
        return {}
    def bstack1ll1l1l1ll1_opy_(self):
        return {
            **super().bstack1ll1l1l1ll1_opy_(),
            **self.bstack1ll1l1l1l1l_opy_()
        }
    def bstack1ll1l111ll1_opy_(self):
        return {
            **super().bstack1ll1l111ll1_opy_(),
            **self.bstack1ll1l11ll1l_opy_()
        }
    def bstack11ll1lll_opy_(self):
        return bstack111l1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫᛥ")
class bstack1l1l11ll_opy_(bstack11ll1l1l_opy_):
    def __init__(self, hook_type, *args,bstack1llll111_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1ll1l1l1l11_opy_ = None
        self.bstack1llll111_opy_ = bstack1llll111_opy_
        super().__init__(*args, **kwargs, bstack11l1111111_opy_=bstack111l1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᛦ"))
    def bstack11lll1ll_opy_(self):
        return self.hook_type
    def bstack1ll1l1l1111_opy_(self):
        return {
            bstack111l1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᛧ"): self.hook_type
        }
    def bstack1ll1l1l1ll1_opy_(self):
        return {
            **super().bstack1ll1l1l1ll1_opy_(),
            **self.bstack1ll1l1l1111_opy_()
        }
    def bstack1ll1l111ll1_opy_(self):
        return {
            **super().bstack1ll1l111ll1_opy_(),
            bstack111l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡪࡦࠪᛨ"): self.bstack1ll1l1l1l11_opy_,
            **self.bstack1ll1l1l1111_opy_()
        }
    def bstack11ll1lll_opy_(self):
        return bstack111l1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࠨᛩ")
    def bstack1lll11l1_opy_(self, bstack1ll1l1l1l11_opy_):
        self.bstack1ll1l1l1l11_opy_ = bstack1ll1l1l1l11_opy_