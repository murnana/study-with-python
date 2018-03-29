===============================================================================
module(もしくはpackage)
===============================================================================

他のファイルから関数やクラスなどを使用する際の、「他のファイル」のことをモジュール(module)といいます。
モジュールは、importされた際に実行文があると、実行されます。

一方、パッケージ(package)という言葉も使われますが、これは「複数のモジュール + `__init__.py`」が入ったディレクトリで構成されているものです。  
C++でのnamespace(名前空間)のようなもの、と思ってください(厳密には、モジュールも名前空間だったりする)


項目
======
.. toctree::
    :glob:
    :titlesonly:

    **/index



参考
=========
* `6. モジュール (module) - Python 3.6.4 ドキュメント <https://docs.python.jp/3/tutorial/modules.html>`_
* `Python基礎講座(14 モジュールとパッケージ) - Qiita <https://qiita.com/Usek/items/86edfa0835292c80fff5>`_
* `Community Blog - Python の名前空間とスコープ <https://www.oreilly.co.jp/community/blog/2011/11/namespace-and-scope-in-python.html>`_ - オライリー
