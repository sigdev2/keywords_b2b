Keywords CSV generator for context advertising
===================================

Generate keywords csv file for context advertising by input file in next format:

.. code-block::

  Заголовок::<headline>
  Текст::<Announcement text>
  Слова::<keyword=alias1=alias2=...>[::...]
  
  Категория::<Category name>::<Category link>::<link title>
    Слова::<keyword=alias1=alias2=...>[::...]
    <Key phrase 1>
    <Key phrase 2>
    [...]
    
  [...]

Usage in console:

    usage: keywords_b2b [-h] [--encoding ENCODING] input

    Generate keywords combinations

    positional arguments:
      input                 Keywords file

    optional arguments:
      -h, --help            show this help message and exit
      --encoding ENCODING, -c ENCODING
                            Work files encoding

    Version 0.1.0a0, Copyright 2018, SigDev
