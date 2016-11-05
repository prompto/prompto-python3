from xml.dom.minidom import parse
import sys

def readXmlFromFile(file):
    with open(file) as f:
        return parse(file)

def getParentTest(elem):
    parent = elem.parentNode
    return parent.getAttribute("name") + " in " + parent.getAttribute("classname")

def readResultsFromXUnitXml(xml):
    doc = xml.documentElement
    count_t = int(doc.getAttribute("tests"))
    count_e = int(doc.getAttribute("errors"))
    count_f = int(doc.getAttribute("failures"))
    errors = None
    failures = None
    if count_e > 0:
        elems = doc.getElementsByTagName("error")
        errors = [getParentTest(error) for error in elems]
    if count_f > 0:
        elems = doc.getElementsByTagName("failure")
        failures = [getParentTest(error) for error in elems]
    return count_t, count_e, count_f, errors, failures

def readTestResultsFromFiles(files):
    count_t = 0
    count_e = 0
    count_f = 0
    errors = None
    failures = None
    for file in files:
        xml = readXmlFromFile(file)
        t1, e1, f1, errs, fails = readResultsFromXUnitXml(xml)
        count_t += t1
        count_e += e1
        count_f += f1
        if errs is not None:
            if errors is None:
                errors = errs
            else:
                errors.extend(errs)
        if fails is not None:
            if failures is None:
                failures = fails
            else:
                failures.extend(fails)
    return count_t, count_e, count_f, errors, failures

if __name__ == '__main__':
    count_t, count_e, count_f,errors, failures = readTestResultsFromFiles(sys.argv[1:])
    print("Total tests: " + str(count_t))
    if count_e + count_f == 0:
        print("Success!")
    else:
        if errors is not None:
            print(str(count_e) + " test(s) in error:")
            for error in errors:
                print("  " + error)
        if failures is not None:
            print(str(count_f) + " failing test(s):")
            for failure in failures:
                print("  " + failure)
        sys.exit(-1) #raise Exception("Tests in error: " + str(count_e) + ", failing tests: " + str(count_f))
