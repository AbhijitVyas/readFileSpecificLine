# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# this method will read given specific file and only select those lines with given keyword
# e.g. fileName= "kitchenClash0.urdf" and keyword="<child link="
# it will write those line from urdf file into out_processed.txt file
def readFileSpecificLine(fileName, keyword):
    with open(fileName) as f:
        lines = f.readlines()
        lines = [l for l in lines if keyword in l]
        with open("out_processed.txt", "w") as f1:
            f1.writelines(lines)

def readFileLinesAndWriteThemToArray(fileName):
    testsite_array = []
    with open(fileName) as my_file:
        for line in my_file:
            testsite_array.append(line.rstrip("\n"))
    return testsite_array

def writeOwlFileWithGivenListOfKeywords(fileName, arrayWithKeywords):
    outF = open(fileName, "w")
    for line in arrayWithKeywords:
        # write line to output file
        lineComment = "\t<!-- http://knowrob.org/kb/Kitchen-clash.owl#" + line + "-->"
        outF.write(lineComment)
        # outF.write(line)
        outF.write("\n")
        outF.write("\n")
        lineNamedIndividualStart = '\t\t<owl:NamedIndividual rdf:about="http://knowrob.org/kb/Kitchen-clash.owl#' + line + '">'
        outF.write(lineNamedIndividualStart)
        outF.write("\n")
        lineNamedIndividualSecondLine = '\t\t\t<rdf:type rdf:resource="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#PhysicalObject"/>'
        outF.write(lineNamedIndividualSecondLine)
        outF.write("\n")
        lineNamedIndividualThirdLine = '\t\t\t<urdf:hasBaseLinkName rdf:datatype="http://www.w3.org/2001/XMLSchema#string">' + line + '</urdf:hasBaseLinkName>'
        outF.write(lineNamedIndividualThirdLine)
        outF.write("\n")
        lineNamedIndividualFinalLine = '\t\t</owl:NamedIndividual>'
        outF.write(lineNamedIndividualFinalLine)
        outF.write("\n")

    outF.close()

def writeOwlFileWithGivenListOfKeywordsEndLinkNames(fileName, arrayWithKeywords):
    outF = open(fileName, "w")
    for line in arrayWithKeywords:
        # write line to output file
        theOnlyline = '\t<urdf:hasEndLinkName rdf:datatype="http://www.w3.org/2001/XMLSchema#string">' + line + '</urdf:hasEndLinkName>'
        outF.write(theOnlyline)

        outF.write("\n")

    outF.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('start reading')
    # at first read kitchenclash urdf file and search for child links, copy all links in out_processed.txt
    readFileSpecificLine('kitchenClash0.urdf', '<child link=')
    keywordsArray = readFileLinesAndWriteThemToArray('out_processed.txt')
    # remove all unncessasory words from out_processed such as <child link=, tabs, manually so that all rows contains only keywords
    # After that create a owl file with named individuals along with proper formatting
    writeOwlFileWithGivenListOfKeywords('write_all_named_individuals.txt', keywordsArray)
    # create has endlink names for all keywords in array
    writeOwlFileWithGivenListOfKeywordsEndLinkNames('write_all_hasEndLinkName.txt',
                                        keywordsArray)
    print_hi('Finished!')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
