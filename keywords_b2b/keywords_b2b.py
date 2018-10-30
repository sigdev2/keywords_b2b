#!/usr/bin/env python
# -*- coding: utf-8 -*-

r''' Copyright 2018, SigDev

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License. '''

from itertools import combinations
from itertools import product

def comb(n, k):
    d = list(range(0, k))
    yield d

    while True:
        i = k - 1
        while i >= 0 and d[i] + k - i + 1 > n:
            i -= 1
        if i < 0:
            return

        d[i] += 1
        for j in range(i + 1, k):
            d[j] = d[j - 1] + 1

        yield d

def comb_sets(sets, m):
    for ci in comb(len(sets), m):
        for cj in product(*(sets[i] for i in ci)):
            yield cj

def keys_replace(strings, keys):
    if len(keys) <= 0:
        return strings
    
    index = {}
    for lk in keys:
        for k in lk:
            index[k] = lk[0]

    l = len(keys)

    ret = []
    for s in strings:
        for r in comb_sets(keys, l):
            new_s = s
            for k in r:
                if len(k) > 0:
                    new_s = new_s.replace(index[k], k)
            if new_s != s and not new_s in strings and not new_s in ret:
                ret.append(new_s)
    return strings + ret        

def keys_combinations(arr):
    words = []
    items = []
    repls = []
    for x in arr:
        if isinstance(x, list):
            repls.append(x)
            items.append(x[0].strip())
        else:
            items.append(x.strip())

    for i in range(len(items)):
        for item in combinations(items, i + 1):
            words.append(item)
    
    return words, repls

def rec_combinate(phrases, keys, rootkeys):
    phrases = keys_replace(phrases, keys)

    ret = []
    for p in phrases:
        words, repls = keys_combinations(rootkeys)
        for item in words:
            all_items = keys_replace([r' '.join(item)], repls)
            for full_item in all_items:
                new_p = p + r' ' + full_item
                if not new_p in phrases and not new_p in ret:
                    ret.append(new_p)

    if len(ret) <= 0:
        return phrases

    ret = keys_replace(ret, keys)
    phrases += ret
    
    return phrases

def parse(text):
    lines = text.split('\n')
    header = r''
    text = r''
    cats = {r'root' : {r'keys' : [], r'phrase' : [], r'link': r'', r'name': r''}}
    last = r'root'
    for l in lines:
        l = l.strip()
        if len(l) <= 0:
            continue
        choises = l.split(r'::')
        first = choises[0].strip()
        if first == u'Заголовок':
            header += choises[1]
        elif first == u'Текст':
            text += choises[1]
        elif first == u'Категория':
            if not choises[1] in cats:
                cats[choises[1]] = {r'keys' : [], r'phrase' : [], r'link': choises[2], r'name': choises[3] }
            last = choises[1]
        elif first == u'Замены' or first == u'Слова' :
            keys = choises[1:]
            for k in keys:
                cats[last][r'keys'].append(k.split(r'='))
        else:
            cats[last][r'phrase'].append(choises)
    
    out = r''
    rootkeys = cats[r'root'][r'keys']
    n = 1

    for cat in cats.keys():
        if cat == r'root':
            continue
        keys = cats[cat][r'keys']
        phrases = cats[cat][r'phrase']
        all_phrases = []
        for p in phrases:
            for _p in p:
                _p = _p.strip()
                all_phrases.append(_p)

        all_phrases = rec_combinate(all_phrases, keys, rootkeys)

        for p in all_phrases:
            out += str(n) + r';' + p + r';' + cat + r';' + header + r';' + text + r';' + cats[cat][r'link'] + r';' + cats[cat][r'name'] + '\n'
        n += 1

    return out
   
if __name__ == r'__main__':
    pass