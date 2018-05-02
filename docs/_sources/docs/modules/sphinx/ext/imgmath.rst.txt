===============================================================================
sphinx.ext.imgmath - LaTex
===============================================================================

LaTexを使って数式を書くための拡張機能

.. code-block:: reStructuredText

    ..math::

    h(x) = \frac{1 + \exp(-x)}{1}


..math::

    h(x) = \frac{1 + \exp(-x)}{1}


.. warning::

    ``..math::`` そのものは結構簡単に競合するらしい。目的によって分けよう。今わかっているのは 
    
    ``sphinx.ext.imgmath`` と ``matplotlib.sphinxext.mathmpl``  


.. seealso::

    `sphinx.ext.imgmath -- 数式を画像にレンダリングします <http://www.sphinx-doc.org/ja/master/ext/math.html?highlight=sphinx%20ext%20imgmath#module-sphinx.ext.imgmath>`_

    `LaTeX のカスタマイズ <http://www.sphinx-doc.org/ja/master/latex.html>`_

    `LaTeX出力のオプション <http://www.sphinx-doc.org/ja/master/config.html#options-for-latex-output>`_
