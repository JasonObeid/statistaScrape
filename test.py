
frame = pd.DataFrame(sr)
frame.to_csv(index=False, path_or_buf=Path)

txt_dir = "captions/"
base_dir = "2Columns/"
other_dir = "multiColumn/"
metaPath = base_dir + "metadata.csv"
otherMetaPath = other_dir + "otherMetadata.csv"
meta_list = []
other_meta_list = []
ids = 0
multiIds = 0


def processData(captionText, dFrame):
    # save dataframe only if it has 2 columns
    dataPath = base_dir + str(ids) + ".csv"
    xAxis = dFrame.columns[0]
    yAxis = dFrame.columns[1]
    if (xAxis.lower() == 'year'):
        chartType = "line"
    else:
        chartType = 'bar'
    # list of metadata contains item id, path of data.csv, and the caption
    meta_list.append({'id': ids, 'dataPath': dataPath, 'caption': captionText, 'chartType': chartType, 'xAxis': xAxis,
                      'yAxis': yAxis, 'URL': link.url})
    dFrame.to_csv(index=False, path_or_buf=dataPath)
    txtPath = txt_dir + str(ids) + ".txt"
    with open(txtPath, 'w') as f:
      f.write(captionText)

def processMultiColumn(captionText, dFrame):
    dataPath = other_dir + str(multiIds) + ".csv"
    xAxis = dFrame.columns
    columns = []
    for row in xAxis:
        columns.append(row)
    # list of metadata contains item id, path of data.csv, and the caption
    other_meta_list.append({'id': multiIds, 'dataPath': dataPath, 'caption': captionText, 'xAxis': columns, 'URL': link.url})
    dFrame.to_csv(index=False, path_or_buf=dataPath)
    txtPath = other_dir + 'captions/' + str(multiIds) + ".txt"
    with open(txtPath, 'w') as f:
      f.write(captionText)


for link in sr:
    try:
        # open link
        html = urlopen(link.url).read()
        # parse as soup object
        soup = BeautifulSoup(html, 'html.parser')
        if (soup.body.find("article")):
            # find data tables in soup object
            soup = soup.body.find("article")
            tableList = soup.select('.entry-content .chapter div, .pew-chart')
            title = soup.select('.entry-content .chapter div .chart_toggle_content')
            print(title)
            for table in tableList:
                # Convert html table to dataframe. returns list of dataframes, therefore get at [0]
                dfs = pd.read_html(str(table))[0]
                # proceed if line / bar chart
                if (dfs.shape[1] == 2):
                    # take caption appearing before data
                    #title = table.parent.select('#chart-table-subtitle')
                    #print(title)
                    if (table.parent.parent.find_previous_sibling("p")):
                        captionElement = table.parent.parent.find_previous_sibling("p")
                        if (captionElement.get_text() != ""):
                            if (table.find_previous_sibling('p#chart-table-subtitle')):
                                ids += 1
                                title = table.find_previous_sibling('p#chart-table-subtitle')
                                print(title)
                                caption = captionElement.get_text()
                                processData(caption, dfs)
                    # Also take caption appearing after data
                    if (table.parent.parent.find_next_sibling("p")):
                        captionElement = table.parent.parent.find_next_sibling("p")
                        if (captionElement.get_text() != ""):
                            ids += 1
                            caption = captionElement.get_text()
                            processData(caption, dfs)
                # store graphs with over 2 columns for potential future use
                else:
                    # take caption appearing before data
                    if (table.parent.parent.find_previous_sibling("p")):
                        captionElement = table.parent.parent.find_previous_sibling("p")
                        if (captionElement.get_text() != ""):
                            multiIds += 1
                            caption = captionElement.get_text()
                            processMultiColumn(caption, dfs)
                    # Also take caption appearing after data
                    if (table.parent.parent.find_next_sibling("p")):
                        captionElement = table.parent.parent.find_next_sibling("p")
                        if (captionElement.get_text() != ""):
                            multiIds += 1
                            caption = captionElement.get_text()
                            processMultiColumn(caption, dfs)

    except Exception as ex:
        print(ex)

metadata = pd.DataFrame(meta_list)
metadata.to_csv(index=False, path_or_buf=metaPath)

otherMeta = pd.DataFrame(other_meta_list)
otherMeta.to_csv(index=False, path_or_buf=otherMetaPath)

print("complete")
