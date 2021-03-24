def make_bbox(bounds, crs = "EPSG:3006", buffer = 0): 
    # Function to create dataframe with bounding box polygon to make spatial join with bground layer
    xmin, ymin, xmax, ymax = bounds
    if buffer != 0:
        xmin -= buffer
        ymin -= buffer 
        xmax += buffer 
        ymax += buffer
        
    bbox = gpd.GeoDataFrame(gpd.GeoSeries(Polygon([[xmin, ymin], [xmin, ymax], [xmax, ymax], [xmax, ymin]])), columns = ["geometry"]).set_crs(crs)
    return bbox

def adjust_bounds(ax, bounds):
    xmin, ymin, xmax, ymax = bounds
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    return ax


def get_middle(bounds): 
    xmin,ymin,xmax,ymax = bounds
    xmid = xmin + (xmax-xmin)/2
    ymid = ymin + (ymax-ymin)/2
    return (xmid, ymid)

def filter(df, col, values, filter_type = "equal"):
    
    if not isinstance(values, list): 
        values = [values]
        
    Bool = False   
    
    for val in values: 
        if filter_type == "equal":
            Bool = Bool | (df[col] == val) 
        
        elif filter_type == "contain":
            Bool = Bool | (df[col].str.contains(val))
            
    return Bool