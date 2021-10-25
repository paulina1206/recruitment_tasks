"""
Test 2
-----
Scan all files in any folder
e.g. usr/share/doc recursively and group them by first three letters.
For each 3-letter group sort the filenames in that group by the
actual size of the files in reverse order. Store the resulting structure in
a dictionary called result

Example:
{
'aam': [(42281, 'aamfigs.pdf'), (1219, 'aamfigs.tex')],
'aas': [(113610, 'aassymbols.pdf'), (4753, 'aassymbols.tex.gz')],
...
'zxj': [(132386, 'zxjafont.pdf'), (3182, 'zxjafont.tex.gz'
'zz_': [(654,'zz_translate_test.crm')]
}
"""

import os


def scan_directory(path: str) -> dict:
    """
    Recursive scan of directory to create grouped by first 3-letter dictionary from found files
    :param path: str, directory path
    :return: dictionary with 3-letter key sort the filenames - that group sorted by the actual size
    of the files in reverse order
    """
    result = {}

    for dirpath, dirnames, filenames in os.walk(path):
        # grouping files by first three letters
        for file in filenames:
            try:
                full_file_path = os.path.join(dirpath, file)
                file_size = os.path.getsize(full_file_path)
                result[file[:3]].append((file_size, file))
            except KeyError:
                result[file[:3]] = [(file_size, file)]
    # sorting by the size of the files in reverse order
    for key, value in result.items():
        result[key] = sorted(value, key=lambda x: x[0], reverse=True)
    return result


if __name__ == '__main__':
    dir_path = '/usr/share/doc'
    print(scan_directory(dir_path))