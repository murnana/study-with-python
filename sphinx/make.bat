@ECHO OFF

pushd %~dp0

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=python -msphinx
)
set SOURCEDIR="./"
set BUILDDIR="../docs"
set PY_SRC="../src"
set PY_RST="./_modules"
set SPHINXPROJ="study_with_python"
set SPHINXOPTS=-d "./_build/doctrees"

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The Sphinx module was not found. Make sure you have Sphinx installed,
	echo.then set the SPHINXBUILD environment variable to point to the full
	echo.path of the 'sphinx-build' executable. Alternatively you may add the
	echo.Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

sphinx-apidoc -M -f -T -o %PY_RST% %PY_SRC%
%SPHINXBUILD% -M html %SPHINXOPTS% %SOURCEDIR% %BUILDDIR%

popd
