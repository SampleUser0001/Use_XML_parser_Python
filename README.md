# Use XML parser Python

PythonでXMLをパースする。  
```xml.etree.ElementTree```を使う。

## Files

### sample.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<top name="hoge">
    <sub name="sub1">
        <item>
            item01
        </item>
    </sub>
    <sub name="sub2">
        <value>
            item01
        </value>
    </sub>
</top>
```

### app

- [./app/src/app.py](./app/src/app.py)

``` python
def logging_item(name, item):
    logger.info(
        '{} : {} , {}.tag : {} , {}.attrib : {} , {}.text.strip() : {}'
        .format(
            name, item,
            name, item.tag,
            name, item.attrib,
            name, item.text.strip()))

if __name__ == '__main__':
    logger.info('start')
    # .envの取得
    # setting.ENV_DIC[ImportEnvKeyEnum.importenvに書いた値.value]
    
    # 起動引数の取得
    # args = sys.argv
    # args[0]はpythonのファイル名。
    # 実際の引数はargs[1]から。
    
    root = ET.parse(FILE_PATH).getroot()
    logging_item('root', root)

    logging_name('root[0]', root[0])
    for child in root:
        logging_item('child', child)

        for sub in child:
            logging_item('sub', sub)
            
    logger.info('end')
```

### 実行結果

``` txt
start
root : <Element 'top' at 0x7ff9d2ac04a0> , root.tag : top , root.attrib : {'name': 'hoge'} , root.text.strip() : 
root[0] : <Element 'sub' at 0x7ff9d2ac04f0> , root[0].tag : sub , root[0].attrib : {'name': 'sub1'} , root[0].text.strip() : 
child : <Element 'sub' at 0x7ff9d2ac04f0> , child.tag : sub , child.attrib : {'name': 'sub1'} , child.text.strip() : 
sub : <Element 'item' at 0x7ff9d2ac0540> , sub.tag : item , sub.attrib : {} , sub.text.strip() : item01
child : <Element 'sub' at 0x7ff9d2ac05e0> , child.tag : sub , child.attrib : {'name': 'sub2'} , child.text.strip() : 
sub : <Element 'value' at 0x7ff9d2ac0630> , sub.tag : value , sub.attrib : {} , sub.text.strip() : item01
emd
```

## 実行

``` sh
docker-compose run python --rm
```

## 参考

- [xml.etree.ElementTree --- ElementTree XML API](https://docs.python.org/ja/3/library/xml.etree.elementtree.html)