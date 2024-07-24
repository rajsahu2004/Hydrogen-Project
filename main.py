from googleMapDownloader import GoogleMapDownloader
import os

def main(lat,lon,zoom=20,img_name='high_resolution_image.png',dir='images'):
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
        img.save(f'{dir}/{img_name}')
        print("The map has successfully been created")


if __name__ == '__main__':
    main(23.81765, 86.44040, 19, 'jasper_hostel_medium.png')