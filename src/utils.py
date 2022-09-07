
from dataclasses import dataclass
from typing import get_type_hints


@dataclass(frozen=True)
class ID:
    metric_chooser = 'metric-chooser'
    top_n_filter = 'top-n-filter'
    all_bar_charts_container = 'all-bar-charts-container'


@dataclass(frozen=True)
class Metrics:
    volume_sold_gallons: str = 'volume_sold_gallons'
    volume_sold_liters: str = 'volume_sold_liters'
    sale_dollars: str = 'sale_dollars'
    bottles_sold: str = 'bottles_sold'
    state_bottle_retail: str = 'state_bottle_retail'
    state_bottle_cost: str = 'state_bottle_cost'
    bottle_volume_ml: str = 'bottle_volume_ml'
    pack: str = 'pack'


all_metrics = [k for (k, _) in get_type_hints(Metrics).items()]


@dataclass(frozen=True)
class Dimensions:
    store_number: str = 'store_number'
    city: str = 'city'
    zip_code: str = 'zip_code'
    county: str = 'county'
    category_name: str = 'category_name'
    vendor_name: str = 'vendor_name'
    item_description: str = 'item_description'


all_dimensions = [k for (k, v) in get_type_hints(Dimensions).items()]


# These titles should be changed into sth meaningful
@dataclass(frozen=True)
class BarChartTitles:
    store_number: str = 'Title store_number'
    city: str = 'Title city'
    zip_code: str = 'Title zip_code'
    country: str = 'Title country'
    category_name: str = 'Title category_name'
    vendor_name: str = 'Title vendor_name'
    item_description: str = 'Title item_description'





