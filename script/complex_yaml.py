import yaml # pip install pyyaml
import os

yamlFile = 'test.yml'
key = '''c#'''

value = '''csharp'''
data1 = {
    key: value
}

f = open(yamlFile, 'w', encoding='utf-8')
yaml.dump(data1, f, allow_unicode=True)

os.system('pause')
os.remove(yamlFile)