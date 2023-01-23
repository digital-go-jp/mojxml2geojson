# coding: utf-8

import argparse
import traceback
import package.xml2geojson


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('FILE_PATH')
    parser.add_argument('-e', '--exclude', help='地番が地図外、別図の筆を除外して出力', action='store_true')
    args = parser.parse_args()

    return args


def main():
    args = get_args()
    srcFile = args.FILE_PATH
    exclude_flag = args.exclude

    try:
        package.xml2geojson.SaveGeoJson(srcFile, exclude_flag)
    except Exception:
        print('Error Source File:', srcFile)
        traceback.print_exc()


if __name__ == '__main__':
    main()
