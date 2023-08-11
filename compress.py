import datetime

class NodeTree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


class Huffman:
    CODE_BEGIN_FILE = 1
    CODE_NAME_FILE = 2
    CODE_ICON_FILE = 3
    CODE_DATE_FILE = 4
    CODE_CONTENT_FILE = 5
    CODE_CRC_FILE = 6
    CODE_END_FILE = 7
    CODE_SHOW_TABLE = 25
    ENCODING = 'utf-8'

    def huffman_code_tree(self, node, left=True, binstring=''):
        if type(node) is bytes:
            return {node: binstring}
        
        (l, r) = node.children()
        d = dict()
        d.update(self.huffman_code_tree(l, True, binstring + '0'))
        d.update(self.huffman_code_tree(r, False, binstring + '1'))
        return d

    def binary(self, s):
        a = 0
        for i in range(len(s)):
            a += int(s[len(s) - 1 - i]) * (2 ** i)
        return bytes([a])

    def decimal(self, s, digits = None):
        a = bin(s)
        a = a[2:]
        if digits:
            a = '0' * (digits - len(a)) + a
        return a

    def __init__(self, string = None):
        if string:
            self.data = string

    def set_files(self, desc = b'', files = {}, crcs = {}, icons = {}, dates = {}):
        self.files = files

        self.data = desc if isinstance(desc, bytes) else desc.encode(self.ENCODING) if isinstance(desc, str) else ''
        for name, content in self.files.items():
            self.data += bytes([self.CODE_BEGIN_FILE, self.CODE_NAME_FILE])
            self.data += name if isinstance(name, bytes) else name.encode(self.ENCODING)
            self.data += bytes([self.CODE_CONTENT_FILE])
            self.data += content if isinstance(content, bytes) else content.encode(self.ENCODING)
            self.data += bytes([self.CODE_ICON_FILE])
            self.data += icons[name] if isinstance(icons[name], bytes) else icons[name].encode(self.ENCODING)
            self.data += bytes([self.CODE_DATE_FILE])
            self.data += dates[name] if isinstance(dates[name], bytes) else dates[name].encode(self.ENCODING)
            self.data += bytes([self.CODE_CRC_FILE])
            self.data += crcs[name] if isinstance(crcs[name], bytes) else crcs[name].encode(self.ENCODING)
            self.data += bytes([self.CODE_END_FILE])

    def start(self):
        freq = {}
        for c in self.data:
            if bytes([c]) in freq:
                freq[bytes([c])] += 1
            else:
                freq[bytes([c])] = 1
        
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        nodes = freq
        
        while len(nodes) > 1:
            (key1, c1) = nodes[-1]
            (key2, c2) = nodes[-2]
            nodes = nodes[:-2]
            node = NodeTree(key1, key2)
            nodes.append((node, c1 + c2))
        
            nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
        
        huffmanCode = self.huffman_code_tree(nodes[0][0])
        
        self.table = {}
        for (char, frequency) in freq:
            self.table[char] = huffmanCode[char]

        #print('Table originale :', self.table)

    def compress(self):
        self.binaire = ''
        self.output = b''
        for item in self.data:
            it = bytes([item])
            code = self.table[it]
            for i in list(code):
                self.binaire += i
                if len(self.binaire) == 8:
                    bit = self.binary(self.binaire)
                    self.output += bit
                    self.binaire = ''

        if self.binaire != '':
            for i in range(len(self.binaire), 8):
                self.binaire += '0'
            self.output += self.binary(self.binaire)
            self.binaire = ''

        self.add_table()
        return self.output

    def add_table(self):
        self.output += bytes([self.CODE_SHOW_TABLE])
        a = b''
        for char, code in self.table.items():
            octet4 = b''
            octet1 = char
            octet2 = bytes([len(code)])
            if len(code) <= 8:
                cde = ('0' * (8 - len(code))) + code
                octet3 = self.binary(cde)
            elif len(code) <= 16:
                cde = ('0' * (16 - len(code))) + code
                octet3 = self.binary(cde[:8])
                octet4 = self.binary(cde[8:])

            self.output += octet1
            self.output += octet2
            self.output += octet3

            a += octet1
            a += octet2
            a += octet3
            if octet4:
                a += octet4
        print(a)

    def uncompress(self, data, table_sec = {}):
        self.compressed = data
        t = b''
        l = len(self.compressed) - 1
        print(self.CODE_SHOW_TABLE, self.compressed[l], bytes([self.compressed[l]]))
        while self.compressed[l] != self.CODE_SHOW_TABLE:
            t += bytes([self.compressed[l]])
            l -= 1
            print(self.CODE_SHOW_TABLE, self.compressed[l], bytes([self.compressed[l]]))
        print(t)

        table = [None for i in range(len(t))]
        for i in range(len(t)):
            table[len(t) - 1 - i] = t[i]

        table = bytes(table)
        i = 0
        self.table = {}
        maxi = 0
        while True:
            try:
                #print(bytes([table[i]]), table[i + 1], table[i + 2])
                octet1 = bytes([table[i]])
                i += 1
                octet2 = table[i]
                i += 1
                octet3 = self.decimal(table[i], 8)
                i += 1
                if octet2 > 8:
                    octet4 = self.decimal(table[i], 8)
                    i += 1
                else:
                    octet4 = ''

                if octet2 > maxi:
                    maxi = octet2

                code = str(octet3 + octet4)
                code = code[-octet2:]
                for j in range(len(code), octet2):
                    code = '0' + code
                self.table[octet1] = code
            except IndexError:
                break

        if table_sec:
            if self.table == table_sec:
                print("Tables are correct !")
            else:
                print("Tables are incorrect ->")
                print('Table lue       :', self.table)
                print('Table correcte  :', table_sec)
                return b'', {}, {}, {}, {}

        self.compressed = self.compressed[:l]
        octet_to_read = 0
        while maxi > 0:
            maxi -= 8
            octet_to_read += 1

        self.content = []
        self.binaire = ''
        c = 0
        while True:
            try:
                e = False
                while not e:
                    for char, code in self.table.items():
                        if self.binaire[:len(code)] == code:
                            self.content.append(char)
                            self.binaire = self.binaire[len(code):]
                            e = True
                            break
                    if e:
                        break
                    else:
                        c += 1
                        b = self.decimal(self.compressed[0])
                        self.compressed = self.compressed[1:]
                        self.binaire += '0' * (8 - len(b)) + b
            except IndexError:
                break

        if table_sec:
            i = -1
            a = b''
            b = ''
            while True:
                try:
                    i += 1
                    a += self.content[i]
                    try:
                        print(a.decode(self.ENCODING), end='')
                        a = b''
                    except UnicodeDecodeError:
                        pass
                except IndexError:
                    break
        
        n = -1
        mode = 'desc'
        desc = b''
        files = {}
        file = b''
        crcs = {}
        icons = {}
        dates = {}
        while True:
            try:
                n += 1
                item = self.content[n]
                if item == bytes([self.CODE_BEGIN_FILE]):
                    mode = ''
                    file = b''
                    continue

                elif item == bytes([self.CODE_NAME_FILE]):
                    mode = 'name'
                    file = b''
                    continue

                elif item == bytes([self.CODE_ICON_FILE]):
                    mode = 'icon'
                    continue

                elif item == bytes([self.CODE_DATE_FILE]):
                    mode = 'date'
                    continue

                elif item == bytes([self.CODE_CONTENT_FILE]):
                    mode = 'data'
                    files[file] = b''
                    crcs[file] = b''
                    dates[file] = b''
                    icons[file] = b''
                    continue

                elif item == bytes([self.CODE_CRC_FILE]):
                    mode = 'crc'
                    continue

                elif item == bytes([self.CODE_END_FILE]):
                    mode = ''
                    file = b''
                    continue

                if mode == 'desc':
                    desc += item
                elif mode == 'name':
                    file += item
                elif mode == 'data':
                    files[file] += item
                elif mode == 'icon':
                    icons[file] += item
                elif mode == 'date':
                    dates[file] += item
                elif mode == 'crc':
                    crcs[file] += item

            except IndexError:
                break

        return desc, files, dates, icons, crcs

    def infos(self):
        l_o = len(self.data)
        l_r = len(self.output)
        compress = int(((l_o - l_r) * 100) / l_o)
        rslt = ''
        rslt += 'Nombre de données en entrée : ' + str(l_o) + '\n'
        rslt += 'Nombre de données en sortie : ' + str(l_r) + '\n'
        rslt += 'Ratio de compression : ' + str(compress) + ' %'
        return rslt


class CmpdFile:
    def __init__(self, file, mode = 'r', table = {}):
        assert mode in ('r', 'w', 'a')

        self.file = file
        self.mode = mode
        self.files = {}
        self.desc = ''

        self.h = Huffman()
        if self.mode in ('r', 'a'):
            f = open(self.file, mode = 'rb')
            self.data = f.read()
            f.close()
            self.desc, fls, dates, icons, crcs = self.h.uncompress(self.data, table_sec = table)
            self.desc = self.decode(self.desc)
            self.files = {}
            for f, d in fls.items():
                self.files[self.decode(f)] = {'content': d, 'icon': icons[f], 'date': dates[f], 'crc': crcs[f]}

        elif self.mode == 'w':
            f = open(self.file, mode = 'w')
            f.close()

    def decode(self, data):
        return data.decode(self.h.ENCODING)

    def read(self, file, string = False):
        assert self.mode == 'r'
        try:
            if string:
                return self.decode(self.files[file]['content'])
            else:
                return self.files[file]
        except KeyError:
            raise FileNotFoundError(file)

    def write(self, file, data):
        assert self.mode in ('w', 'a')
        date = datetime.datetime.now()
        now = str(date.day) + '/' + str(date.month) + '/' + str(date.year) + ' ' + str(date.hour) + ':' + str(date.minute) + ':' + str(date.second)
        self.files[file] = {'content': data, 'icon': b'', 'date': now, 'crc': b''}

    def close(self):
        if self.mode in ('w', 'a'):
            files_only = {}
            self.crcs = {}
            self.dates = {}
            self.icons = {}
            for n, data in self.files.items():
                files_only[n] = data['content']
                self.crcs[n] = data['crc']
                self.icons[n] = data['icon']
                self.dates[n] = data['date']

            self.h.set_files(desc = self.desc, files = files_only, icons = self.icons, dates = self.dates, crcs = self.crcs)
            self.h.start()
            f = open(self.file, mode = 'wb')
            r = self.h.compress()
            f.write(r)
            f.close()
            return self.h.infos()

    def namelist(self):
        return list(self.files.keys())


if __name__ == '__main__':
    f = CmpdFile('testn1.form', mode = 'w')
    f.write('Benoit.txt', "Bonjour, je voudrais savoir en premier comment vous vous portez... Comme vous aurez pu le constater, mon algorithme de huffman n'est pas génial dans le sens ou la sortie est plus grande que l'entrée.")
    f.write('Yanis.txt', "Bonjour, je voudrais déjà, avant toute chose connaitre si vous connaissez les LGBTQAI+ car je fait moi même parti de cette grande communauté")
    f.desc = 'Coucou maman, comment vas tu ? Je voudrais te demander ton avis pour une petite chose sans importance... :)'
    f.close()
    #f = CmpdFile('testn1.form', mode = 'r')
    #print(f.read('Benoit.txt', True))
    #f.close()
    #f = CmpdFile('testn1.form', mode = 'a')
    #f.write('Gaëtan.txt', "Bonjour Gaëtan, on sait tous très bien que tu aimes Nolwen :) :) :)")
    #f.close()
    t = f.h.table####################
    f = CmpdFile('testn1.form', mode = 'r', table = t)
    print(f.namelist())
    #print(f.read('Gaëtan.txt', True))
    #print(f.read('Yanis.txt'))
    #print(f.namelist())
    f.close()
