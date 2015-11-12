# coding: utf-8


def fix_bibtex_file(bibtex_file):
    new_bibtex_file = list()
    for line in bibtex_file:
        if '\r\n' in line: 
            line = line.split('\r\n')[0]

        if '=' in line:
            arr = line.split('=', 1)
            if arr[1][-1:] != ',':
                arr[1] = arr[1] + ','
            comma_index = arr[1].rfind(',')
            value = arr[1][:comma_index].strip()
            new_line_content = arr[0].strip() + '={' + value + '},'
            new_bibtex_file.append(new_line_content)
        else:
            new_bibtex_file.append(line)
    return new_bibtex_file
