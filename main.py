import region_reader as rr
import slicer

from PIL import Image, ImageDraw

Image.MAX_IMAGE_PIXELS = 933120000
image_name_prefix = "map_mask"
image_size = 16384
image_size_real = 2048


def show():
    pass


def create():
    global im, dw
    im = Image.new("L", (image_size_real, image_size_real))


def draw(regions):
    dw = ImageDraw.Draw(im)
    for index in regions:
        arrs = regions[index]
        tuples = []
        for i in range(len(arrs)):
            arr = arrs[i]
            tuples.append(((arr[0] + 8192) / 8, (-arr[1] + 8192) / 8))
        print(int(index))
        dw.polygon(tuples, fill=int(index), outline=0)


def slice_image(image: Image, tw: int, th: int, export: str) -> None:
    slicer.slice_image(image, tw, th, export)


if __name__ == '__main__':
    create()
    regions = rr.get_regions("area.json")
    if regions is not None:
        pass
    draw(regions)
    slicer.slice_image(im,2048,2048,"mask")
    slicer.slice_image(im, 256, 256, "mask")
    slicer.slice_image(im, 1024, 1024, "mask")
