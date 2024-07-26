from utils import GoogleMapDownloader, dms_to_decimal
import os
from tqdm.auto import tqdm
import pandas as pd
import numpy as np

def main(lat,lon,zoom=20,img_name='high_resolution_image',dir='images'):
    # Create a new instance of GoogleMap Downloader
    gmd = GoogleMapDownloader(lat, lon, zoom)

    print(f'The tile coorindates are {gmd.getXY()}')

    try:
        # Get the high resolution image
        img = gmd.generateImage()
    except IOError:
        print("Could not generate the image - try adjusting the zoom level and checking your coordinates")
    else:
        #Save the image to disk
        os.makedirs(dir, exist_ok=True)
        img.save(f'{dir}/{img_name}_{zoom}.png')
        print("The map has successfully been created")


if __name__ == '__main__':
    df = pd.read_csv('csv/australian_basins.csv')
    df['Latitude'] = np.round(df['Latitude'].apply(dms_to_decimal),5)
    df['Longitude'] = np.round(df['Longitude'].apply(dms_to_decimal),5)
    # main(23.25215,11.933, 19, '0',dir='data')
    # main(dms_to_decimal("22°12'"),dms_to_decimal("85°21'"), 20, 'singhbum_zoom',dir='data')
    main(dms_to_decimal("24°08'14.09"),dms_to_decimal("15°41'31.63"), 19, 'namibia',dir='data')
    for i in tqdm(df.index,total=len(df)):
        # if i==1:
        #     break
        print(df.loc[i,'Latitude'], df.loc[i,'Longitude'])
        main(df.loc[i,'Latitude'], df.loc[i,'Longitude'], 13, f'{i}',dir='data')
