from dino_runner.utils.constants import FREEZE, FREEZE_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Freeze(PowerUp):
    def __init__(self):
        self.image = FREEZE
        self.type = FREEZE_TYPE
        super().__init__(self.image, self.type)
