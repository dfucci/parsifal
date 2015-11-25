# coding: utf-8
class BibitexSanitizer(object):
    def __init__(self, bibtex_file):
        self.bibtex_file = bibtex_file

    def sanitize(self):
        tokenized_bibtex = self._tokenize_bibtex()
        no_keywords_bibtex = self._merge_dup_keywords(tokenized_bibtex)
        sanitized_bibtex = self._to_string(no_keywords_bibtex)
        return sanitized_bibtex

    def _tokenize_bibtex(self):
        new_bibtex_file = list()
        entry = list()
        for line in self.bibtex_file.readlines():
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
        return new_bibtex_file

    def _merge_dup_keywords(self, bibtex_file_list):
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

    def _to_string(self, bibtex_file_list):
        list_bibtex_file = map(lambda x: '\r\n'.join(x), bibtex_file_list)
        str_bibtex_file = '\r\n'.join(list_bibtex_file)
        return str_bibtex_file
