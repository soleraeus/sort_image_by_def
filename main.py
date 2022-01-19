import os
import shutil

try:
    import Image
except ImportError:
    from PIL import Image


def main():
    source_path = input("Please enter source path\n")
    while not os.path.exists(source_path):
        source_path = input('Wrong path name for source folder, please enter a valid folder name\n')
    destination_path = input("Please enter destination path\n")
    if not os.path.exists(destination_path):
        answer = 'b'
        while not (answer == 'y' or answer == 'n'):
            answer = input(
                'Destination path ' + destination_path + ' does not exist, do you wish to create it? (y/n)\n')
            if answer == 'n':
                print('Goodbye\n')
            elif answer == 'y':
                print('Creating path ' + destination_path + '\n')
                os.mkdir(destination_path)
            else:
                pass
    hd_path = destination_path + '/' + 'HD'
    md_path = destination_path + '/' + 'MD'
    bd_path = destination_path + '/' + 'BD'
    if not os.path.exists(hd_path):
        os.mkdir(hd_path)
    if not os.path.exists(md_path):
        os.mkdir(md_path)
    if not os.path.exists(bd_path):
        os.mkdir(bd_path)
    for root, directory_names, file_names in os.walk(source_path):
        for files in file_names:
            path_to_file = os.path.join(root, files)
            try:
                image = Image.open(path_to_file)
            except (IOError, Image.DecompressionBombError):
                continue
            width, height = image.size
            if width >= height:
                length = width
            else:
                length = height
            if length > 3000:
                shutil.move(path_to_file, hd_path)
            elif length < 1200:
                shutil.move(path_to_file, bd_path)
            else:
                shutil.move(path_to_file, md_path)
            image.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
