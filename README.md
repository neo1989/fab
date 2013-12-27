fab
=======
基于fabric的发布工具

说明：
    
    fab g:yml=xx.yml    #从git获取源代码发布 (yml文件需要commit版本号及files)

    fab l:yml=xx.yml    #从本地开发环境获取源代码发布 (yml文件仅需files)

usage: 

    1.  更新config.py或添加conf_extend.py文件

    2.  更新yml文件或添加xx.py文件
    
    3.  在项目根目录下运行 fab g:yml=xx.yml (或者 fab l:yml=xx.yml) 
