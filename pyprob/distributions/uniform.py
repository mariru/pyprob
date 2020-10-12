import torch

from . import Distribution
from .. import util


class Uniform(Distribution):
    def __init__(self, low, high):
        low = util.to_tensor(low)
        high = util.to_tensor(high)
        super().__init__(name='Uniform', address_suffix='Uniform', torch_dist=torch.distributions.Uniform(low, high))

    def __repr__(self):
        return 'Uniform(low={}, high={})'.format(self.low.detach().cpu().numpy().tolist(), self.high.detach().cpu().numpy().tolist())

    @property
    def low(self):
        return self._torch_dist.low

    @property
    def high(self):
        return self._torch_dist.high

    def to(self, device):
        return Uniform(low=self.low.to(device), high=self.high.to(device))
