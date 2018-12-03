import re
a = re.match('^[\u4e00-\u9fa5|，。；？]+\?$', '你好哈人日你，妈我。我？；们我為啥說在張志這?')
a.groups()

