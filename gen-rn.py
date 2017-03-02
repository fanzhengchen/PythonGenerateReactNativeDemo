import os
import re


def genRootIndexFile(projectName):
    indexFileContent = open("template_index")

    targetIndexAndroid = open("./%s/index.android.js" % projectName, "w")

    targetIndexIos = open("./%s/index.ios.js" % projectName, "w")

    for line in indexFileContent:
        # print(line)

        pattern = re.compile('\$\{projectName\}')

        newLine = pattern.sub(projectName, line)

        print(newLine)

        targetIndexAndroid.write(newLine)

        targetIndexIos.write(newLine)


def genSrcIndexFile(projectName, libs):
    indexFileContent = open("template_for_src_index")
    targetFile = open("./%s/src/index.js" % (projectName), "w")

    importFilePattern = re.compile('\$\{importFiles\}')
    importComponentsPattern = re.compile('\$\{importComponents\}')

    for line in indexFileContent:

        if importFilePattern.search(line) != None:
            importLine = ""
            for libName in libs:
                name = re.sub('[\W]', '', libName)
                name = 'N' + name
                importLine += "import %s from '%s';\n" % (name, libName)
            targetFile.write(importLine)
        elif importComponentsPattern.search(line) != None:

            print("fuck")
            importLine = ""
            for libName in libs:
                name = re.sub('[\W]', '', libName)
                name = 'N' + name
                importLine += "\t\t\t\t<%s/>\n" % (name)
            targetFile.write(importLine)
        else:
            targetFile.write(line)


## react-native project name
projectName = "wx_sample"

## init project
os.system('react-native init %s' % (projectName))

## cd prject make directory named src and write default index.js
os.system("mkdir -p %s/src" % (projectName))

## install custom libs provided by developer
libs = ['fbemitter', 'fzc-emitter', 'fzc-sku', 'fzc-price']

components = ['fzc-sku', 'fzc-price']
list(map(lambda x:
         os.system("cd %s && npm install --save %s" % (projectName, x)),
         libs))
#
genRootIndexFile(projectName)

genSrcIndexFile(projectName, ['fzc-sku', 'fzc-price'])
