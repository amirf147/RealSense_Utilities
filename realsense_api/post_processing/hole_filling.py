# https://dev.intelrealsense.com/docs/post-processing-filters
from option import OptionValues, OptionType, OptionDict, FilterOptions

class HoleFillingOptions(FilterOptions):
    def __init__(self) -> None:
        self.options: OptionDict = {
            OptionType.MAGNITUDE : OptionValues(
                option_value=1,
                option_value_increment=1,
                option_min_value=0,
                option_max_value=2
            )
        }

    def increment(self, option: OptionValues) -> None:
        option.option_value += option.option_value_increment
        if option.option_value > option.option_max_value:
            option.option_value = option.option_min_value