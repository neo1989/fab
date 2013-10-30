fab
=======
基于GIT的自用发布工具

说明：
    
    fab g ：从git获取源代码发布 (yml文件需要commit版本号及files)

    fab l ：从本地开发环境获取源代码发布 (yml文件仅需files)

usage: 

    1.  更新config.py或添加config_extend.py文件

    2.  更新yml文件
    
    3.  在项目根目录下运行 fab g (或者 fab l) 
