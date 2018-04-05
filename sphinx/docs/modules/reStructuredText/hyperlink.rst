===============================================================================
ハイパーリンク
===============================================================================

.. サンプル用の設定

.. _`google`: https://www.google.co.jp/
.. _`ぐーぐる`: `google`_




ハイパーリンクターゲットの種類
===========================================================

.. csv-table::
    :header: 種類, 説明

    内部, 同じページ内に飛ぶ
    外部, ページ外に飛ぶ
    間接, 同じところに飛ぶが別名


間接ハイパーリンクターゲット(indirect hyperlink targets)
--------------------------------------------------------

.. code-block:: restructuredtext

    .. _`google`: https://www.google.co.jp/
    .. _`ぐーぐる`: `google`_

    `google`_ も `ぐーぐる`_ も同じになります


`google`_ も `ぐーぐる`_ も同じになります



明示的ハイパーリンクターゲット(explicit hyperlink targets)
===========================================================

この名前にはこのリンクを使いたい、というときに使用できます。

.. code-block:: restructuredtext

    .. 何処でもいいので、リンクにしたい名前を入れる

    .. _`google`: https://www.google.co.jp/

    .. あとは文をいれるだけ

    ぐーぐるさん `google`_

結果は以下の通り

ぐーぐるさん `google`_




暗黙的ハイパーリンクターゲット(implicit hyperlink targets)
===========================================================

セクションタイトル、脚注および引用によって生成されるハイパーリンクターゲットです。

.. code-block:: restructuredtext

    このページでは `明示的ハイパーリンクターゲット(explicit hyperlink targets)`_ のように使えます

このページでは `明示的ハイパーリンクターゲット(explicit hyperlink targets)`_ のように使えます



.. seealso::
    `reStructuredText Markup Specification <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#hyperlink-targets>`_
        本家リファレンス

    `reStructuredText Markup Specification <http://docutils.sphinx-users.jp/docutils/docs/ref/rst/restructuredtext.html#hyperlink-targets>`_
        日本語訳
