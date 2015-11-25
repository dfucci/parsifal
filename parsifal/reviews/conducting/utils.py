# coding: utf-8


def fix_bibtex_file(bibtex_file):
    new_bibtex_file = list()
    entry = list()
    for line in bibtex_file:
        new_line = None
        if '\r\n' in line: 
            line = line.split('\r\n')[0]

        if '=' in line:
            arr = line.split('=', 1)
            if arr[1][-1:] != ',':
                arr[1] = arr[1] + ','
            comma_index = arr[1].rfind(',')
            value = arr[1][:comma_index].strip()
            new_line_content = arr[0].strip() + '={' + value + '},'
            new_line = new_line_content
        else:
            new_line = line
        if len(new_line) > 0 and new_line[0] == '@':
            if entry:
                new_bibtex_file.append(entry)
            entry = list()
        entry.append(new_line)
    new_bibtex_file.append(entry)
    return _merge_dup_keywords(new_bibtex_file)

def _merge_dup_keywords(bibtex_file_list):
    new_bibtex_file_list = list()
    for bibtex_file in bibtex_file_list:
        keywords_lines = filter(lambda x: 'keywords=' in x, bibtex_file)
        keywords = map(lambda x: x.split("=")[1].replace('"','').strip(), keywords_lines)
        keywords_str = '; '.join(keywords).replace('{', '').replace('},','')
        keywords_line = 'keywords={' + keywords_str.strip() + '},'
        bibtex_withouth_keywords = [line for line in bibtex_file if "keywords={" not in line]
        bibtex_withouth_keywords.insert(len(bibtex_withouth_keywords)-1, keywords_line)
        new_bibtex_file_list.append(bibtex_withouth_keywords)
    return new_bibtex_file_list
