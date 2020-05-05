import argparse
import files_list
import filter_processor

if __name__ == '__main__':
    parser = argparse.ArgumentParser('find file utility')
    parser.add_argument('-e', help='file extenstion to search')
    parser.add_argument('-n', help='file name to search')
    parser.add_argument('-s', help='file size greater than size')
    parser.add_argument('-t', help='file modified post this date in format YY-MM-DD')
    parser.add_argument('path', help='absolute path of directory to search files')
    #TODO add support for recursive search

    args = parser.parse_args()
    file_object = files_list.FilesFromDirectory(args.path)

    for arg in vars(args):
        if arg == 'path':
            continue

        filter = getattr(args, arg)
        if filter:
            cls = filter_processor.FILTER_COMMAND_MAPPING[arg]
            filtered_files = cls(filter, file_object).get_matching_files()
            file_object.update_filtered_files(filtered_files)

    print 'matching files are --->'
    for file in file_object.get_filtered_files():
        print file

