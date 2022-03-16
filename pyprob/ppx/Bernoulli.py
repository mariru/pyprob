# automatically generated by the FlatBuffers compiler, do not modify

# namespace: ppx

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Bernoulli(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Bernoulli()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsBernoulli(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def BernoulliBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x50\x50\x58\x46", size_prefixed=size_prefixed)

    # Bernoulli
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Bernoulli
    def Probs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from ppx.Tensor import Tensor
            obj = Tensor()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def Start(builder): builder.StartObject(1)
def BernoulliStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddProbs(builder, probs): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(probs), 0)
def BernoulliAddProbs(builder, probs):
    """This method is deprecated. Please switch to AddProbs."""
    return AddProbs(builder, probs)
def End(builder): return builder.EndObject()
def BernoulliEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)