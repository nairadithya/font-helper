import os
import pathlib
import subprocess
import sys
import zipfile

font_dir = os.path.expanduser("~/.local/share/fonts/")


def main() -> None:
    if len(sys.argv) < 2:
        print("""Usage: Operates on a zip file and moves the files to the fonts dir.
        Example: font-helper Roboto.zip
        """)
        sys.exit()
    else:
        with zipfile.ZipFile(sys.argv[1]) as font_zip:
            cur_path = pathlib.Path(sys.argv[1])
            dir_name = os.path.basename(cur_path.resolve()).split(".")[0]
            new_dir_name = os.path.join(os.path.dirname(cur_path), dir_name)
            os.mkdir(new_dir_name)

            font_info = font_zip.infolist()
            print("Installing The Following Fonts:")
            for item in font_info:
                print(item.filename)

            print("Extracting the file...")
            font_zip.extractall(path=new_dir_name)
            dest_dir = os.path.join(font_dir, dir_name)
            print(new_dir_name, dest_dir)

            print(f"Done extracting, now moving to {dest_dir}")
            os.rename(new_dir_name, dest_dir)

            print("Refreshing font cache")
            subprocess.Popen("fc-cache", shell=True)

            print("Font Successfully Added")


if __name__ == "__main__":
    main()
