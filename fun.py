import argparse

parser = argparse.ArgumentParser(description='just for fun')
"""
    class argparse.ArgumentParser(
                                prog=None,
                                usage=None,
                                description=None,
                                epilog=None,
                                parents=[],
                                formatter_class=argparse.HelpFormatter,
                                prefix_chars='_',
                                fromfile_prefix_chars=None,
                                argument_default=None,
                                conflict_handler='error',
                                add_help=True,
                                allow_abbrev=True,
                                exit_on_error=True)

prog - 程序的名称（默认：sys.argv[0]）
usage - 描述程序用途的字符串（默认值：从添加到解析器的参数生成）
description - 在参数帮助文档之前显示的文本（默认值：无）
epilog - 在参数帮助文档之后显示的文本（默认值：无）
parents - 一个 ArgumentParser 对象的列表，它们的参数也应包含在内
formatter_class - 用于自定义帮助文档输出格式的类
prefix_chars - 可选参数的前缀字符集合（默认值：'-'）
fromfile_prefix_chars - 当需要从文件中读取其他参数时，用于标识文件名的前缀字符集合（默认值：None）
argument_default - 参数的全局默认值（默认值： None）
conflict_handler - 解决冲突选项的策略（通常是不必要的）
add_help - 为解析器添加一个 -h/--help 选项（默认值： True）
allow_abbrev - 如果缩写是无歧义的，则允许缩写长选项 （默认值：True）
exit_on_error - 决定当错误发生时是否让 ArgumentParser 附带错误信息退出。 (默认值: True)
"""
parser.add_argument('-r','--reason',action='store_false',help='the reason y you create this file')
"""
ArgumentParser.add_argument(name or flags...,
                            action='',store store_const store_teue store_false：保存值，保存const true false值 append：将统一参数不同值保存在一个list中
                            count：统计参数出现次数 extend：存储一个列表，将参数的不同值加入列表是，注意加narg"
                            nargs,默认情况下 ArgumentParser对象将参数与action一一关联，通过指定nargs可以将多个参数与一个action相关联。支持的值有：
                            N,将参数的N个值保存在一个list[]中; '?'：如果存在该参数且给出了参数值，则为该参数复制；如果存在该参数但未给出参数值，赋const关键字的值；不存在该参数赋默认值。
                            '*'：将参数的多个值保存在一个list中
                            const,
                            default,用于指定未赋值时参数的默认值。default默认值为None。如果目标命名空间已经有一个属性集，则default动作不会覆盖它：args = parser.parse_args([], namespace=argparse.Namespace(foo=101))
                            
                            type,
                            choices,将命令行参数的值限定在指定范围内，超出范围则报错
                            required,由'-'和'--'为前缀的参数是可选参数（required=False），只有当加入required=True时参数才是必需的。
                            help,包含参数简短描述的字符串
                            metavar,
                            dest
                            允许自定义ArgumentParser的参数属性名称。)
name or flags... 可选参数会以'-' '--'前缀识别 否则作为位置参数
- 代表短选项，在命令行输入- 和 -- 效果相同。但如果想通过解析后的参数取出该值，必须使用带--的名称
可选参数需要指定名称才能进行赋值，位置参数不需要。
'-'和'--'同时出现 默认'--'为可选参数 


action='',
"""
args = parser.parse_args()#i解析参数
print(args.reason)
