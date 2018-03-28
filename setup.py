"""
Pythonプロジェクトのセットアップスクリプト
https://github.com/paver/paver/blob/master/setup.py から持ってきた
"""

# paverがあればimport
# なければminiを入れる
try:
    import paver.tasks
except ImportError:
    from os.path import exists
    if exists("paver-minilib.zip"):
        import sys
        sys.path.insert(0, "paver-minilib.zip")
    import paver.tasks

# paverタスク実行
paver.tasks.main()
