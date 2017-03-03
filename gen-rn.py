import os
import re
import sys


def genRootIndexFile(projectName):
    indexFileContent = open("template_index")

    targetIndexAndroid = open("./%s/index.android.js" % projectName, "w")

    targetIndexIos = open("./%s/index.ios.js" % projectName, "w")

    for line in indexFileContent:
        # print(line)

        pattern = re.compile('\$\{projectName\}')

        newLine = pattern.sub(projectName, line)

        # print(newLine)

        targetIndexAndroid.write(newLine)

        targetIndexIos.write(newLine)

    targetIndexAndroid.close()
    targetIndexIos.close()


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

    targetFile.close()


def genReactNativeProject(projectName, components):
    ## react-native project name
    # projectName = "wx_sample"

    ## init project
    os.system('react-native init %s' % (projectName))

    ## cd project make directory named src and write default index.js
    os.system("mkdir -p %s/src" % (projectName))

    ## install custom libs provided by developer
    libs = ['fbemitter', 'fzc-emitter']

    for ele in components:
        libs.append(ele)

    print(libs)

    print(components)

    list(map(lambda x:
             os.system("cd %s && npm install --save %s" % (projectName, x)),
             libs))
    genRootIndexFile(projectName)

    genSrcIndexFile(projectName, components)


if __name__ == '__main__':

    components = []
    # for arg in range(sys.argv(1, )):
    #     print(arg)

    for index in range(1, len(sys.argv)):
        arg = sys.argv[index]

        components.append(arg)



    projectName = input("input project name:")
    genReactNativeProject(projectName, components)
