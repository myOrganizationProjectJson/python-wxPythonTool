


http://www.crifan.com/use_pyinstaller_to_package_python_to_single_executable_exe/
http://www.cnblogs.com/chjbbs/archive/2014/01/25/3533187.html
=====================================================================================

安装文件	下载地址
python-2.6.2.msi	http://www.python.org/download/
wxPython2.8-win32-unicode-2.8.10.1-py26.exe
wxPython2.8-win32-docs-demos-2.8.10.1.exe	http://www.wxpython.org/download.php



wxPython2.8-win32-unicode-2.8.10.1-py26.exe 安装后可以 import wx
wxPython2.8-win32-docs-demos-2.8.10.1.exe 中是所有桌面程序demo

http://blog.csdn.net/jia611/article/details/50498094



PyInstaller 打包exe

可以只是生成单独的可执行程序
且支持的版本也多：2.3到2.7都支持。以及x64也支持
也可以自定义图标
所以先去试试PyInstaller。

3.从主页

http://www.pyinstaller.org/

中下载对应的zip包：

https://github.com/downloads/pyinstaller/pyinstaller/pyinstaller-2.0.zip

cd pyinstaller-2.0 setup.py install

结果说需要PyWin32，所以得先去装这个。


去到pyinstaller.py所在目录，去运行：



总结

PyInstaller，的确非常好用啊。感谢作者们。

简单总结其使用方法：

生成单一的exe文件：

pyinstaller.py -F ..\BlogsToWordpress\BlogsToWordpress.py
添加必要的搜索路径：
pyinstaller.py -F -p D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs;D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs\crifan;D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs\crifan\blogModules;D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs\thirdparty;D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs\thirdparty\chardet; ..\BlogsToWordpress\BlogsToWordpress.py
添加必要的搜索路径，且带图标：
pyinstaller.py -F -p D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs;D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs\crifan;D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs\crifan\blogModules;D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs\thirdparty;D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs\thirdparty\chardet; -i ..\BlogsToWordpress\BlogsToWordpress.ico ..\BlogsToWordpress\BlogsToWordpress.py
 

需要注意的是：

1.检查生成的

pyinstaller-2.0\XXX\build\pyi.win32\XXX\warnXXX.txt

(XXX是你的项目名）

中，是否缺少了必要的模块。

如果有缺少的，那么去如上所述，添加必要的搜素路径，使得pyinstaller在运行时，可以找到对应的模块并集成进来。

2.此处我这里没有UPX，暂时没去折腾。

估计是用UPX去压缩，压缩后所生成的exe文件的大小，会小得多。
