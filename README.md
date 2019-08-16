# New2Q-Reports
QGIS based reporting plugin
* To learn how to use this plugin please refer to the [Manual]( https://github.com/bcgov/new2Q-reports/tree/master/Manual)

## About
This is a plugin designed for the GIS software QGIS. New2Q-Reports takes a geospatial input such as a kml or shp file and compares it to predetermined layers. Any layers that intersect with the Area of Interest (AOI) will be summarized in a PDF report. New2Q-Reports is capable of intersecting a variety of layers. The layers can be local datasets such as a SHP file or Feature Class from a Geodatabase. It is also capable of handling Oracle Database tables as both the intersecting layer or an AOI.  This report identifies useful information about each of the intersecting layers and produces a PDF which includes a map, legend and a table. 

Along with the plugin, there are a couple of files that are crucial for New2Q-Reports to be operational. The first file is a CSV which details the location and filename of the predetermined intersecting layers. The CSV includes further information about the datasets allowing the user to customize and explore the data they are interested in. A Grouping function allows users to produce multiple PDFs based on similar datasets. A Query function allows users to refine the intersecting layers using SQL. An Expansion function lets users further explore the dataset by providing the column title/field name of interest. This field will then be expanded in the reports table. 

## Contributing
It is encouraged to contribute to this plugin and help us build it towards a fully open source platform. 
* Please fork a copy to your personal repository so you can work on the code
* Once complete, send a Pull Request 
All edits will be taken into account and assessed prior to merging 

## License
    Copyright 2019 BC Provincial Government
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
