


http://www.crifan.com/use_pyinstaller_to_package_python_to_single_executable_exe/
http://www.cnblogs.com/chjbbs/archive/2014/01/25/3533187.html
=====================================================================================

��װ�ļ�	���ص�ַ
python-2.6.2.msi	http://www.python.org/download/
wxPython2.8-win32-unicode-2.8.10.1-py26.exe
wxPython2.8-win32-docs-demos-2.8.10.1.exe	http://www.wxpython.org/download.php



wxPython2.8-win32-unicode-2.8.10.1-py26.exe ��װ����� import wx
wxPython2.8-win32-docs-demos-2.8.10.1.exe ���������������demo

http://blog.csdn.net/jia611/article/details/50498094



PyInstaller ���exe

����ֻ�����ɵ����Ŀ�ִ�г���
��֧�ֵİ汾Ҳ�ࣺ2.3��2.7��֧�֡��Լ�x64Ҳ֧��
Ҳ�����Զ���ͼ��
������ȥ����PyInstaller��

3.����ҳ

http://www.pyinstaller.org/

�����ض�Ӧ��zip����

https://github.com/downloads/pyinstaller/pyinstaller/pyinstaller-2.0.zip

cd pyinstaller-2.0 setup.py install

���˵��ҪPyWin32�����Ե���ȥװ�����


ȥ��pyinstaller.py����Ŀ¼��ȥ���У�



�ܽ�

PyInstaller����ȷ�ǳ����ð�����л�����ǡ�

���ܽ���ʹ�÷�����

���ɵ�һ��exe�ļ���

pyinstaller.py -F ..\BlogsToWordpress\BlogsToWordpress.py
��ӱ�Ҫ������·����
pyinstaller.py -F -p D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs;D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs\crifan;D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs\crifan\blogModules;D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs\thirdparty;D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs\thirdparty\chardet; ..\BlogsToWordpress\BlogsToWordpress.py
��ӱ�Ҫ������·�����Ҵ�ͼ�꣺
pyinstaller.py -F -p D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs;D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs\crifan;D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs\crifan\blogModules;D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs\thirdparty;D:\tmp\tmp_dev_root\python\tutorial_summary\make_exe\BlogsToWordpress\libs\thirdparty\chardet; -i ..\BlogsToWordpress\BlogsToWordpress.ico ..\BlogsToWordpress\BlogsToWordpress.py
 

��Ҫע����ǣ�

1.������ɵ�

pyinstaller-2.0\XXX\build\pyi.win32\XXX\warnXXX.txt

(XXX�������Ŀ����

�У��Ƿ�ȱ���˱�Ҫ��ģ�顣

�����ȱ�ٵģ���ôȥ������������ӱ�Ҫ������·����ʹ��pyinstaller������ʱ�������ҵ���Ӧ��ģ�鲢���ɽ�����

2.�˴�������û��UPX����ʱûȥ���ڡ�

��������UPXȥѹ����ѹ���������ɵ�exe�ļ��Ĵ�С����С�öࡣ
