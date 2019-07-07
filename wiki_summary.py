import os
import argparse

def list_dir(the_dir):
    entries = os.listdir(the_dir)
    return filter(lambda x: x[0] not in ('.', '_'), entries)

def read_files(the_dir):
    contents = {}
    for a_file in list_dir(the_dir):
        path = os.path.join(the_dir, a_file)
        with open(path) as f:
            lines = list(filter(lambda x: x not in ('\n'), f.readlines()))
            for skip in ['_**Note:', 'https://yout', '**_Note:', 'Home']:
                if lines[0].startswith(skip):
                    lines.pop(0)
            contents[a_file.replace('.md', '')] = lines[0]
    return contents

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('dir', metavar='DIR', help='The directory to scan.')
    args = parser.parse_args()
    file_contents = read_files(args.dir)
    for k in sorted(file_contents.keys()):
        print('**{}:** {}'.format(k, file_contents[k]))

if __name__ == '__main__':
    main()
