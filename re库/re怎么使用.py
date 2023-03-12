import re
'''
|	    两者任一
^	    匹配字符串的开始
$	    匹配字符串的结束
*	    重复零次或更多次
+	    重复一次或更多次
?	    重复零次或一次
{n}	    重复n次
{n,}	重复n次或更多次
{n,m}	重复n到m次
*?	    重复任意次，但尽可能少重复
+?	    重复1次或更多次，但尽可能少重复
??	    重复0次或1次，但尽可能少重复
{n,m}?	重复n到m次，但尽可能少重复
{n,}?	重复n次以上，但尽可能少重复

\w	    匹配字母或数字或下划线或汉字
\s	    匹配任意的空白符
\d	    匹配数字
\b	    匹配单词的开始或结束
\W	    匹配任意不是字母，数字，下划线，汉字的字符
\S	    匹配任意不是空白符的字符
\D	    匹配任意非数字的字符
\B	    匹配不是单词开头或结束的位置
.	    任何字符（换行符除外）

[^x]	匹配除了x以外的任意字符
[^aeio]	匹配除了aeio这几个字母以外的任意字符

(exp)	        匹配exp,并捕获文本到自动命名的组里
(?<name>exp)	匹配exp,并捕获文本到名称为name的组里，也可以写成(?'name'exp)
(?:exp)	        匹配exp,不捕获匹配的文本，也不给此分组分配组号
(?=exp)	        匹配exp前面的位置
(?<=exp)	    匹配exp后面的位置
(?!exp)	        匹配后面跟的不是exp的位置
(?<!exp)	    匹配前面不是exp的位置
(?#comment)	    这种类型的分组不对正则表达式的处理产生任何影响，用于提供注释让人阅读
'''
string = 'Hello,what is your name? My name is Sam.'
# match:从开始匹配，span索引，group找到的东东
print(re.match('Hello', string).span())
print(re.match('Hello', string).group())
# findall:返回在字符串中找到的所有匹配项的列表
print(re.findall('is', string))
print(re.findall('[a-zA-Z]+', string))
# find:返回在字符串中第一个匹配项
print(string.find('is'))
print(string.find('[a-zA-Z]+'))