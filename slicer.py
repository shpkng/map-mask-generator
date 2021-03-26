from PIL import Image


def slice_path(path, tw, th, export):
    source = Image.open(path)
    slice_image(source, tw, th, export)


def slice_image(source, tw, th, export):
    sw, sh = source.size
    cw, ch = sw // tw, sh // th
    for i in range(0, cw):
        for j in range(0, ch):
            box = (i * tw, j * th, i * tw + tw, j * th + th)
            temp = source.crop(box)
            temp.save("%s%sx%s%s.%s" % (export, cw, ch, "_%s_%s" % (i, ch - 1 - j), "png"), "png")
