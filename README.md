# Graduation Requirements Specification Language (GRADSPEC)

An attempt to describe graduation requirements in a standard format for courses in the National University of Singapore.

## Format
Aimed implementation format: **JSON**

## Basic Syntax & Semantics
This section describes the different types of entities within the overall requirements description. 

### Header
An overall header for the JSON object that is describing a set of graduation requirements.

Fields that **must** be present:
1. **name**: The course that this object is decribing. E.g. "NUS Computer Science Cohort 2015/16 Graduation Requirements"
2. **magic**: A magic number that indicates to any JSON parsers that this is a valid file of this type. Must be exactly **102383781**. The number has no significance.
3. **version**: A SemVer version number for future compatibility. Earliest version is 0.1.0.

### Body (Requirements)
The body section of the JSON object describes the actual course graduation requirements. 

Fields that must be present:
1. **requirements**: A list of **Section** objects

### Syntactical Structure for GRADSPEC in JSON
The header and body together form a basic JSON structure:


```javascript
{
    "name": "NUS Computer Science Cohort 2015/16",
    "magic": 102383781,
    "version": "0.1.0",
    "requirements": ...
}
```


## Requirements Syntax & Semantics

### Sections
A section is a particular subset of graduation requirements. 

Fields that must be present:
1. **title**: The title of the current section, e.g. "Computer Science Breadth and Depth"
2. **mcs**: The total number of modular credits that are fulfilled by this section

One of these two fields must be present:
1. **requirements**: A **Requirements** object that decribes that requirements to fulfil this particular section. 
2. **subsections**: A *non-empty* list of **Section** objects

e.g.

```javascript
{
    "name": "NUS Computer Science Cohort 2015/16",
    "magic": 102383781,
    "version": "0.1.0",
    "requirements": [
        {"title": "University Level Requirements", "requirements": ...},
    ]
}
```

```javascript
{
    "name": "NUS Computer Science Cohort 2015/16",
    "magic": 102383781,
    "version": "0.1.0",
    "requirements": [
        {"title": "University Level Requirements", "subsections": [
            {"title": "English Modules", "requirements": ...}
        ]},
    ]
}
```





### Requirements
This is a collection of **Requirement** objects that are semantically linked with AND/OR/null combinators. It  describes the module requirements to fulfil one subsection/section.

**Requirement** objects can be combined by **AND** combinators or **OR** combinators just like any normal boolean expression. If neither are necessary, the `null` combinator can be used, but the operand list must only have at most 1 requirement.

Combinators are written as such (e.g. assuming some  **Requirement**s r1, r2 and r3 exist):

```javascript
{ 
    "operator": "AND", 
    "operands": [
        {"operator": "OR", "operands": [r1, r2]
    }, r3]
}
```



This describes the requirement: (r1 OR r2) AND r3


### Requirement
This is a particular number/combination of module requirements.

Fields that must be present for all subtypes:
1. **title**: The title of this requirement, e.g. "Computer Systems Team Project"
2. **req-type**: The subtype of requirement this is

There may be other fields depending on **req-type**.

There are many sub-types of Requirement that cater to different kinds of module requirements. Therefore the type "Requirement" is abstract and only concrete implementations below can be used.

#### Requirement Subtype: Take all modules from module list
A simple list of modules that must **all** be completed to satify this requirement.

Fields:
1. **req-type**: "take-all"
2. **modules**: \<list of modules\>

#### Requirement Subtype: Take one module from a list (option)
One module from a given list must be taken to satify this requirement. This is best used to model a situation where you can choose one of a few modules to fulfil a requirement (e.g. an Internship module or FYP)

Fields:
1. **req-type**: "take-one"
2. **modules**: \<list of modules\>

#### Requirement Subtype: Take n modules from module list
Some number of modules from a given list must be taken to satify this requirement

Fields:
1. **req-type**: "take-n"
2. **n**: \<# of modules to take\>
3. **modules**: \<list of modules\>

#### Requirement Subtype: Take n modules over (non-inclusive) Level x from a list
Some number of modules that are over a particular module level (e.g. 5 modules over level-3000) must be taken to satify this requirement

Fields:
1. **req-type**: "take-n-above-level"
2. **n**: \<# of modules to take\>
3. **level**: The module level restriction  (e.g. 2000)
4. **modules**: \<list of modules\>

#### Requirement Subtype: Take n modules below (non-inclusive) Level x from a list
Some number of modules that are below a particular module level (e.g. 5 modules below level-2000) must be taken to satify this requirement

Fields:
1. **req-type**: "take-n-below-level"
2. **n**: \<# of modules to take\>
3. **level**: The module level restriction  (e.g. 2000)
4. **modules**: \<list of modules\>

#### Requirement Subtype: Take n modules matching general regex from a list
Some n modules that match a particular regular expression must be taken to satify this requirement

Fields:
1. **req-type**: "take-n-regex"
2. **mcs**: \<# of modules to take\>
3. **regex**: The regex to check for matches with on each module
4. **modules**: \<list of modules\>



#### Requirement Subtype: Take some number of modules with total MCs > n, modules matching general regex from a list
Some modules that have an MC load that exceeds n  that all match a particular regular expression must be taken to satify this requirement

Fields:
1. **req-type**: "take-mcs-regex"
2. **mcs**: \<# of MCs to minimally reach with this combination\>
3. **regex**: The regex to check for matches with on each module
4. **modules**: \<list of modules\>

#### Requirement Subtype: null requirement 
A null requirement is something that is always satisfied. Can be used as a placeholder.

## Syntax

{

}