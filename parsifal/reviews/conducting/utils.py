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

def merge_dup_keywords(bibtex_file_ref):
    with open(bibtex_file_ref, 'rt') as f:
        whole_file = f.read()
    #sanitize
    whole_file = whole_file.replace('\n', '')
    whole_file = whole_file.replace('\r', '')

    entries = whole_file.split('}@')
    #need to add the last } back
    sanitized_entries = list()
    for e in entries:
        if e[len(e)-1] != '}':
            e = e + '}'
            sanitized_entries.append(e)

    entry_list = list()
    for se in sanitized_entries:
        _fix_keywords(se)



def _fix_keywords(entry):
    lines = entry.split(',')
    keywords_lines = filter(lambda x: 'keywords=' in x, lines)
    keywords = map(lambda x: x.split("=")[1], keywords_lines)
    keywords_line = 'keywords=' + '; '.join(keywords) + ','
    lines_no_keywords = [line for line in lines if "keywords=" not in lines]
    lines.insert(len(lines)-1, keywords_line)
    # add commas at EOL ?
    return lines 
