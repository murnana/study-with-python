===============================================================================
===============================================================================
外部ファイルのテキストを埋め込む
===============================================================================
reStructuredTextにテキストファイルを読み込みたいときに


.. code-block:: restructuredtext

    .. include:: ../../../../setup.py
        :code: python


結果は以下。

.. include:: ../../../../../setup.py
    :code: python


オプション
============
.. csv-table::
    :header: 名前, 説明

    ``:start-line:`` , 何行目から始めるか
    ``:end-line:`` , 何行目から終わるか
    ``:start-after:`` , どの文字列の後を引用するか
    ``:end-before:`` , どの文字列の前まで引用するか


.. seealso::

    `reStructuredText Directives <http://docutils.sourceforge.net/docs/ref/rst/directives.html#include>`_
