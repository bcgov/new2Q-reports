# Manual


## Working with the Plugin
### Setup
1. Open Qgis
2. Create new project
  * Project > New (ctrl+n)
3. To input AOI using plugin skip to Plugin Step 1
4. Drag and drop your AOI into QGIS
5. Check box to turn layer visibility on
   ![p5](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Layer Visibility")
### Plugin 
   ![p6m](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Complete Plugin")
1. Open the plugin
   * Plugins > FNBLine
2. Select AOI
   * Option 1 (Vector Layer):  
   -If AOI is loaded in QGIS (Drag and Drop), select  
   the vectory layer using the dropdown arrow
   * Option 2 (Path):  
   - If AOI is loaded from a path, select Browse  
   - Locate and select the file. Click "Open"
   * Option 2 (Table Name):  
   - If AOI is an Oracle Database Table, copy  
   and paste the schema.table name in the text bar
3. Input Database Connection Info
   * Add username and password 
4. Identify PDF Output Path 
   i.   Select Browse
   ii.  Select the output folder
   iii. Click "Select Folder"
5. Click "OK"
6. Wait until tool is fully complete
   * Green sucess bar at the top of the map will appear  
   ![p11](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Sucess Bar")   
   * To see where the PDFs exported Click "Show More"  
   ![p11b](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Show More")
  
## Working with QGIS
### Layers and Data
  * To access Layer information, right click on layer name and select "Open Attribute Table"
  * Layers are loaded into QGIS after the plugin is complete
  * Layers can be visually turned on and off (See: Working with the Plugin > Setup > 5)
  * To zoom into layer right click layer name and select "Zoom to Layer"
  * Layer order can be adjusted
    1. Click on the layer name (layer will be highlighted in blue)
    2. Click and hold on the layer name and drag above or below other layers

## Working with the CSV
### Adding Data
**Name** | **Feature Name** | **Location** | **Special Query** | **Grouping** | **Expansion Field**
--- | --- | --- | --- | --- | ---
`Mandatory` | `Mandatory` | `Mandatory` | `Optional` | `Mandatory` | `Optional`
name that will appear in the Pdf table | schema.table | Oracle Database | SQL statement | integer that groups layers into seperate PDFS| field/column name
name that will appear in the Pdf table | shp file name | *C:\path\file.shp* | SQL statement | integer that groups layers into seperate PDFS | field/column name
name that will appear in the Pdf table | feature class name | *C:\path\folder.gdb* | SQL statement | integer that groups layers into seperate PDFS | field/column name

1. Open the CSV file
2. Add in accurate data 
   * Follow the above table for guidance 
3. Save file
   * Confirm that file is still a CSV



