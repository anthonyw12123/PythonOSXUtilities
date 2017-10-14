# https://stackoverflow.com/a/8329047/8209066
def set_label(filename, color_name):
    from xattr import xattr
    colors = ['none', 'gray', 'green', 'purple', 'blue', 'yellow', 'red', 'orange']
    key = u'com.apple.FinderInfo'
    attrs = xattr(filename)
    current = attrs.copy().get(key, chr(0)*32)
    changed = current[:9] + chr(colors.index(color_name)*2) + current[10:]
    attrs.set(key, changed)

def validatePath(path):
    if os.path.isfile(path) or os.path.isdir(path):
        return path
    else:
        msg = 'Must be a valid file or directory'
        raise argparse.ArgumentTypeError(msg)

def validateFilter(path):
    if os.path.isfile(path) or os.path.isdir(path):
        return path
    else:
        msg = 'Must be a valid file or directory'
        raise argparse.ArgumentTypeError(msg)

if __name__ == '__main__':
    import argparse
    import re
    import os

    arser = argparse.ArgumentParser(description='Label image(s) based on reolution size.')
    parser.add_argument('input',nargs='+', type=validatePath, help='the path to the local image(s)')
    parser.add_argument('-f', type=validateFilter, help='Specify a filter of files to process.', dest='filter')
    parser.add_argument('-v', help='verbose. Turn on debug output.', action='store_true', dest='verbose', default=False)
    parser.add_argument('-ns', help='No saving. This disables actually modifying the filesystem.', action='store_false', dest='save')
    args = parser.parse_args()

set_label('/Users/anthony/Documents/Git/PythonOSXUtilities/ImageSorter/test', 'green')

# def LabelImage(file, color):
#     from xattr import xattr
#     from struct import unpack
#     attrs = xattr(file)
#     try:
#         finder_attrs = attrs[u'com.apple.FinderInfo']
#         flags = unpack(32*'B', finder_attrs)
#         color = flags[9] >> 1 & 7
#     except KeyError:
#         color = 0
