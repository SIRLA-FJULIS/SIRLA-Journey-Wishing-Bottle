from django.shortcuts import render

from trips.models import Post

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .fusioncharts import FusionCharts
from collections import OrderedDict


#首頁
def home(request):
  post_list = Post.objects.all()
  TaiwanChart(request)
  return render(request, 'home.html', {'post_list': post_list})


def TaiwanChart(request):
  # Reference: https://www.fusioncharts.com/dev/api/fusioncharts/fusioncharts-events#dataplotclick-261
  # Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
  # The data is passed as a string in the `dataSource` as parameter.
  dataSource = OrderedDict()

  # The `chartConfig` dict contains key-value pairs of data for chart attribute
  chartConfig = OrderedDict()
  #chartConfig["caption"] = "SIRLA 旅遊許願瓶"
  #chartConfig["subcaption"] = "SIRLA 2020-07"
  chartConfig["showLabels"] = "0"
  chartConfig["borderThickness"] = "0.5"
  chartConfig["theme"] = "fusion" # fusion, gammel, candy, umber
  chartConfig["entityToolText"] = "<b>$lname</b>"
  dataSource["chart"] = chartConfig

  colorrange_chartConfig = OrderedDict()
  colorrange_chartConfig["minvalue"] = "20"
  colorrange_chartConfig["code"] = "#000000"

  dataSource["colorrange"] = colorrange_chartConfig

  dataSource["data"] = []
  # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
  # Insert the data into the `dataSource['data']` list.
  dataSource["data"].append({"ID": "01", "label": "彰化縣", "value": "70.0", "link": "/area?ID=10"})
  dataSource["data"].append({"ID": "02", "Label": "嘉義縣", "value": "52.3", "link": "/area?ID=12"})
  dataSource["data"].append({"ID": "03", "Label": "嘉義市", "value": "54.2", "link": "/area?ID=13"})
  dataSource["data"].append({"ID": "04", "Label": "新竹縣", "value": "55.3", "link": "/area?ID=5"})
  dataSource["data"].append({"ID": "05", "Label": "Hsinchu City", "value": "50.1", "link": "/area?ID=6"})
  dataSource["data"].append({"ID": "06", "Label": "Hualien County", "value": "28.5", "link": "/area?ID=19"})
  dataSource["data"].append({"ID": "09", "Label": "Keelung City", "value": "29.3", "link": "/area?ID=1"})
  dataSource["data"].append({"ID": "10", "Label": "Kinmen County", "value": "59.4", "link": "/area?ID=21"})
  dataSource["data"].append({"ID": "11", "Label": "Lienchiang County", "value": "26.6", "link": "/area?ID=22"})
  dataSource["data"].append({"ID": "12", "Label": "Miaoli County", "value": "44.4", "link": "/area?ID=7"})
  dataSource["data"].append({"ID": "13", "Label": "Nantou County", "value": "49.9", "link": "/area?ID=8"})
  dataSource["data"].append({"ID": "14", "Label": "Penghu County", "value": "28.7", "link": "/area?ID=20"})
  dataSource["data"].append({"ID": "16", "Label": "Pingtung County", "value": "42.7", "link": "/area?ID=16"})
  dataSource["data"].append({"ID": "20", "Label": "New Taipei City", "value": "32.0", "link": "/area?ID=3"})
  dataSource["data"].append({"ID": "21", "Label": "Taipei City", "value": "29.6", "link": "/area?ID=2"})
  dataSource["data"].append({"ID": "22", "Label": "Taitung County", "value": "28.9", "link": "/area?ID=17"})
  dataSource["data"].append({"ID": "23", "Label": "Taoyuan City", "value": "32.0", "link": "/area?ID=4"})
  dataSource["data"].append({"ID": "24", "Label": "Yilan County", "value": "28.6", "link": "/area?ID=18"})
  dataSource["data"].append({"ID": "25", "Label": "Yunlin County", "value": "45.2", "link": "/area?ID=11"})
  dataSource["data"].append({"ID": "26", "Label": "Taichung City", "value": "28.6", "link": "/area?ID=9"})
  dataSource["data"].append({"ID": "27", "Label": "Kaohsiung City", "value": "29.2", "link": "/area?ID=15"})
  dataSource["data"].append({"ID": "28", "Label": "Tainan City", "value": "29.2", "link": "/area?ID=14"})

  # Create an object for the map using the FusionCharts class constructor 
  # The chart data is passed to the `dataSource` parameter.
  fusionMap = FusionCharts("maps/taiwan", "TaiwanChart", "950", "750", "TaiwanChart-container", "json", dataSource)
  # returning complete JavaScript and HTML code, which is used to generate map in the browsers. 
  return render(request, 'home.html', {'output': fusionMap.render(), 'chartTitle': 'Taiwan Map'})