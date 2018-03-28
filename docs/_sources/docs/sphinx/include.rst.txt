===============================================================================
外部ファイルのテキストを埋め込む
===============================================================================
reStructuredTextにテキストファイルを読み込みたいときに


.. code-block:: restructuredtext

    .. include:: ../../../setup.py
        :code: python


結果は以下。

.. include:: ../../../setup.py
    :code: python


参考
=========
* `reStructuredText Directives <http://docutils.sourceforge.net/docs/ref/rst/directives.html#include>`_
