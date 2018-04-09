"""
Sphinxドキュメントを生成するタスク
通常、Paverのdoctoolsを使うのだが、このプロジェクトの構造に合わせたいので作成
"""

import os, shutil, sphinx.cmd.build, sphinx.ext.apidoc
from paver.easy import dry, task, needs

_sphinx_path = 'sphinx'
_doctree_path = 'sphinx/__doctree__'
_api_reSt_path = 'sphinx/api'
_module_path = 'src'
_docs_path = 'docs'

def create_apidoc(option):
    """
    APIドキュメントの作成

        :param list[str] option: sphinx-apidocオプション

    """
    sphinx.ext.apidoc.main(option)



def build(option):
    """
    reStructuredTextからSphinxによるビルド

        :param list[str] option: sphinx-buildオプション

    """
    sphinx.cmd.build.main(option)



def clear(dir):
    """
    ディレクトリごと削除
        :param str dir:ディレクトリ
    """
    if(os.path.exists(dir)):
        print('%s is delete...' % dir)
        shutil.rmtree(dir)
        print('%s is done delete!' % dir)



@task
def cleanup_docs():
    clear(_api_reSt_path)
    clear(_doctree_path)
    clear(_docs_path)


@task
def create_docs():
    """
    ドキュメント生成

        :param list[str] option: sphinx-buildオプション

    """
    create_apidoc(['-f', '-o', _api_reSt_path, _module_path])
    build(['-b', 'html', '-d', _doctree_path, _sphinx_path, _docs_path])

@task
def recreate_docs():
    cleanup_docs()
    create_docs()
