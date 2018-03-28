===============================================================================
Pavement.pyの中身
===============================================================================

このファイルは？
==================
タスクを読み込むエントリポイントのようなもの。
ファイル名、位置はルートディレクトリに置く。

※マルチバイトのコメントを打つと怒りだします
　なぜだ…



このプロジェクトでの中身
=========================
.. include:: ../../../pavement.py
    :code: python



タスクの基本
=========================
定義するには ``@task`` を使用します

.. code-block:: python

    from paver.easy import task

    @task
    def sample_task(): 
        print('さんぷる')


この場合は、 ``sample_task`` という名前のタスクになります



依存タスク
=============
自分より前に実行されなければならないタスクがある場合は ``@needs`` を使います

.. code-block:: python

    from paver.easy import task, needs

    @task
    @needs(['sample_prev_task'])
    def sample_task(): 
        print('さんぷる')



実行方法
=============
コマンドラインもしくはターミナルに

.. code-block:: bat

    paver sample_prev_task

と書くだけ



参考
=========

* `徹底的に pavement.py — Paver v1.0.1 documentation <https://paver.github.io/paver-docs-jp/pavement.html>`_
