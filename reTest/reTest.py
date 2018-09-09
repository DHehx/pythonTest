import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My num is 415-555-4242')
print(mo.group())

#括号分组
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My num is 415-555-4242')
print(mo.group(2))

#匹配特殊字符
phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My num is (415)-555-4242')
print(mo.group(1))
print(mo.group(2))

#用管道匹配多个分组
phoneNumRegex = re.compile(r'Batman|Tina Fey')
mo = phoneNumRegex.search('Batman and Tina Fey.')
print(mo.group())

mo2 = phoneNumRegex.search('Tina Fey and Batman.')
print(mo2.group())

batRegex = re.compile(r'Bat(man|Tina Fey|mobile|bat)')
mo = batRegex.search('Batmobile lost a wheel.')
print(mo.group())
print(mo.group(1))

#选择匹配
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman.')
print(mo.group())

mo = batRegex.search('The Adventures of Batwoman.')
print(mo.group())

#匹配零次或多次
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman.')
print(mo.group())

mo = batRegex.search('The Adventures of Batwoman.')
print(mo.group())

mo = batRegex.search('The Adventures of Batwowowowoman.')
print(mo.group())
print(mo==None)

#匹配特定次数
batRegex = re.compile(r'(Ha){3}')
mo = batRegex.search('HaHaHa')
print(mo.group())

mo = batRegex.search('Ha')
print(mo==None)

#贪心匹配和非贪心匹配
batRegex = re.compile(r'(Ha){3,5}')
mo = batRegex.search('HaHaHaHaHa')
print(mo.group())

batRegex = re.compile(r'(Ha){3,5}?')
mo = batRegex.search('HaHaHaHaHa')
print(mo.group())

#findall()
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('Cell: 415-555-4242 Work:212-555-0000')
print(mo)

#匹配必须发生在被查找文本开始处
begins = re.compile(r'^Hello')
mo = begins.search('Hello world!')
print(mo)
mo = begins.search('Say Hello world!')
print(mo)

#匹配必须发生在被查找文本结束处
begins = re.compile(r'\d$')
mo = begins.search('It\'s 42')
print(mo)
mo = begins.search('Say 42!')
print(mo)

#匹配从开始到结束都是数字的字符串
begins = re.compile(r'^\d+$')
mo = begins.search('It\'s 42')
print(mo)
mo = begins.search('4782572493065743242')
print(mo)
mo = begins.search('478257249yy3065743242')
print(mo)

#通配符
begins = re.compile(r'.')
mo = begins.search('It\'s 42')
print(mo)
mo = begins.search('4782572493065743242')
print(mo)
mo = begins.findall('4782yy1')
print(mo)

#匹配所有字符
begins = re.compile(r'First Name: (.*) LastName: (.*)')
mo = begins.search('First Name: My Last Name: Name')
print("1")
print(mo.group(1))
print(mo.group(2))
