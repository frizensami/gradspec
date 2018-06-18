import json
import pprint
import sys 

# Code for printing w/o unicode u prefix
def my_safe_repr(object, context, maxlevels, level):
    typ = pprint._type(object)
    if typ is unicode:
        object = str(object)
    return pprint._safe_repr(object, context, maxlevels, level)
printer = pprint.PrettyPrinter()
printer.format = my_safe_repr

def print_requirement(requirement, level):
    print (" " * (level + 2) * 4) + "Requirement Name: %s, Type: %s, Modules: %s" % (requirement["title"], requirement["req-type"], str(requirement["modules"]))


def print_requirements(requirements, level):
    if not requirements:
        print (" " * (level + 1) * 4) + "No requirements for this section"
    else:
        for idx, operand in enumerate(requirements["operands"]):
            if "operator" not in operand:
                print_requirement(operand, level)
                if idx < len(requirements["operands"]) - 1:
                    print (" " * (level + 2) * 4) + requirements["operator"]
            else:
                #print (" " * (level + 2) * 4) + "<<This is a nested requirement>>"
                print_requirements(operand, level+1)
                print (" " * (level + 2) * 4) + requirements["operator"]

        


def print_sections_recursive(spec, level=-1):
    # If we see a "sections" or "subsections" field, recurse
    if "sections" in spec:
        for section in spec["sections"]:
            print_sections_recursive(section, level+1)
            print ""
    elif "subsections" in spec:
        print  (" " * level * 4) + "Section: " + spec["title"]
        for section in spec["subsections"]:
            print_sections_recursive(section, level+1)
    else:
        # This must be a section
        print  (" " * level * 4) + "Section: " + spec["title"]
        print_requirements(spec["requirements"], level)



if __name__ == "__main__":

    specfile = sys.argv[1] if len(sys.argv) > 1 else None
    if not specfile:
        print "No specification file to parse (pass as first command line argument)! Exiting."
        sys.exit(1)

    json_data = open(specfile).read()
    spec = json.loads(json_data)

    print "Printing Specification:"
    printer.pprint(spec)

    print "\n\n----------- SPEC PRINTER v0.1.0 -----------"
    print "----------- HEADER -----------"
    print "Requirements name: %s" % spec["name"]
    print "Version: %s" % spec["version"]
    print "Magic: %s" % spec["magic"]
    print "----------- BODY SECTIONS -----------"

    print_sections_recursive(spec)
    #for toplevel_section in spec["sections"]:
    #    print "Toplevel section name: %s" % toplevel_section["title"]
