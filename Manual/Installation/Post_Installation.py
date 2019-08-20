import os
import configparser

def script_updated(logo, url, cf, cs, csv):
    #updates plugin script 
    replace_variable = ['logoImagePath', 'urlWithParams', 'filename', 'section', 'csv_path']  
    replace_string = ['        logoImagePath = {}\n'.format(logo),'        urlWithParams = {}\n'.format(url), '        con_filename = {}\n'.format(cf), '        con_section = {}\n'.format(cs), '                csv_path = {}\n'.format(csv)]
    file_list = []
    with open(pyscript, 'r') as lines:
        count = 0
        for line in lines:
            if '~~~' in line:
                if any(x in line for x in replace_variable):
                    line = replace_string[count]
                    count += 1
                    file_list.append(line)
            else:
                file_list.append(line)
    with open(pyscript,'w') as py:
        py.writelines(file_list)

def plugin_checkon(qg_config)
    #Turn on plugin for QGIS polugin manager files (config file)
    config = configparser.ConfigParser()
    config.read(qg_config)
    config.sections()
    config.set('PythonPlugins', 'fn_bline', 'true')
    with open(qg_config, 'w') as configfile:
        config.write(configfile)

if __name__ == "__main__":
#SET THESE VARIABLE:
    #QGIS ini file location     ex:   os.path.join(os.getenv('appdata'), r'QGIS\QGIS3\profiles\default\QGIS\QGIS3.ini')
    qg_config = r""
    
    #script location variable:
    directory = r"" #directory path to plugin script      ex:   os.path.join(os.getenv('appdata'), r'QGIS\QGIS3\profiles\default\python\plugins\fn_bline')
    pyscript = os.path.join(directory,'FN_BLine.py')

    #script variables:
    logo = r"" #path to small logo to be placed within the pdf
    url = r""  #wms url for basemap
    cf = r""   #config.ini file path
    cs = ""    #config.ini section name
    csv = r""  #csv file path for intersecting layers

    script_updated(logo,url,cf,cs,csv)