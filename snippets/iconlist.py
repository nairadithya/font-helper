# /// script
# requires-python = ">=3.12"
# dependencies = [
#      "cairosvg",
# ]
# ///

import os
import sys

from cairosvg import svg2png

resolutions = [16, 32, 48, 96, 128]

if len(sys.argv) < 2:
    print(
        """Usage: Use it on an svg to get a list of PNGs in the specified resolution.
        Example: ext_icon file.svg
        """
    )
    sys.exit()

filepath = sys.argv[1]

os.mkdir("./result")


for item in resolutions:
    svg2png(
        url=filepath,
        write_to=f"./result/{item}.png",
        output_width=item,
        output_height=item,
    )

    print(f"Generated png in {item}x{item} resolution")


print(f"Done! You will find your results in {os.path.realpath('./result')}.")
