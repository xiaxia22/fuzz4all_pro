# Interface RootDoc

**Source:** `jdk.javadoc\com\sun\javadoc\RootDoc.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
RootDoc

extends
Doc
,
DocErrorReporter
```

Represents the root of the program structure information
for one run of javadoc. From this root all other program
structure information can be extracted.
Also represents the command line information -- the
packages, classes and options specified by the user.

**All Superinterfaces:** Comparable

<

Object

>

,

Doc

,

DocErrorReporter

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
[][] options()

Command line options.

For example, given:

```java
javadoc -foo this that -bar other ...
```

this method will return:

```java
options()[0][0] = "-foo"
options()[0][1] = "this"
options()[0][2] = "that"
options()[1][0] = "-bar"
options()[1][1] = "other"
```

**Returns:**
- an array of arrays of String.

---

#### PackageDoc
[] specifiedPackages()

Return the packages

specified

on the command line.
If

-subpackages

and

-exclude

options
are used, return all the non-excluded packages.

**Returns:**
- packages specified on the command line.

---

#### ClassDoc
[] specifiedClasses()

Return the classes and interfaces

specified

as source file names on the command line.

**Returns:**
- classes and interfaces specified on the command line.

---

#### ClassDoc
[] classes()

Return the

included

classes and interfaces in all packages.

**Returns:**
- included classes and interfaces in all packages.

---

#### PackageDoc
packageNamed​(
String
name)

Return a PackageDoc for the specified package name.

**Parameters:**
- name

- package name

**Returns:**
- a PackageDoc holding the specified package, null if
this package is not referenced.

---

#### ClassDoc
classNamed​(
String
qualifiedName)

Return a ClassDoc for the specified class or interface name.

**Parameters:**
- qualifiedName

-

qualified

class or package name

**Returns:**
- a ClassDoc holding the specified class, null if
this class is not referenced.

---

### Additional Sections

#### Interface RootDoc

**All Superinterfaces:** Comparable

<

Object

>

,

Doc

,

DocErrorReporter

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
RootDoc

extends
Doc
,
DocErrorReporter
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Represents the root of the program structure information
for one run of javadoc. From this root all other program
structure information can be extracted.
Also represents the command line information -- the
packages, classes and options specified by the user.

**Since:** 1.2

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

RootDoc

extends

Doc

,

DocErrorReporter

Represents the root of the program structure information
for one run of javadoc. From this root all other program
structure information can be extracted.
Also represents the command line information -- the
packages, classes and options specified by the user.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

ClassDoc

[]

classes

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the

included

classes and interfaces in all packages.

ClassDoc

classNamed

​(

String

qualifiedName)

Deprecated, for removal: This API element is subject to removal in a future version.

Return a ClassDoc for the specified class or interface name.

String

[][]

options

()

Deprecated, for removal: This API element is subject to removal in a future version.

Command line options.

PackageDoc

packageNamed

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Return a PackageDoc for the specified package name.

ClassDoc

[]

specifiedClasses

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the classes and interfaces

specified

as source file names on the command line.

PackageDoc

[]

specifiedPackages

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the packages

specified

on the command line.

- Methods declared in interface com.sun.javadoc.

Doc

commentText

,

compareTo

,

firstSentenceTags

,

getRawCommentText

,

inlineTags

,

isAnnotationType

,

isAnnotationTypeElement

,

isClass

,

isConstructor

,

isEnum

,

isEnumConstant

,

isError

,

isException

,

isField

,

isIncluded

,

isInterface

,

isMethod

,

isOrdinaryClass

,

name

,

position

,

seeTags

,

setRawCommentText

,

tags

,

tags

- Methods declared in interface com.sun.javadoc.

DocErrorReporter

printError

,

printError

,

printNotice

,

printNotice

,

printWarning

,

printWarning

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

ClassDoc

[]

classes

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the

included

classes and interfaces in all packages.

ClassDoc

classNamed

​(

String

qualifiedName)

Deprecated, for removal: This API element is subject to removal in a future version.

Return a ClassDoc for the specified class or interface name.

String

[][]

options

()

Deprecated, for removal: This API element is subject to removal in a future version.

Command line options.

PackageDoc

packageNamed

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Return a PackageDoc for the specified package name.

ClassDoc

[]

specifiedClasses

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the classes and interfaces

specified

as source file names on the command line.

PackageDoc

[]

specifiedPackages

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the packages

specified

on the command line.

- Methods declared in interface com.sun.javadoc.

Doc

commentText

,

compareTo

,

firstSentenceTags

,

getRawCommentText

,

inlineTags

,

isAnnotationType

,

isAnnotationTypeElement

,

isClass

,

isConstructor

,

isEnum

,

isEnumConstant

,

isError

,

isException

,

isField

,

isIncluded

,

isInterface

,

isMethod

,

isOrdinaryClass

,

name

,

position

,

seeTags

,

setRawCommentText

,

tags

,

tags

- Methods declared in interface com.sun.javadoc.

DocErrorReporter

printError

,

printError

,

printNotice

,

printNotice

,

printWarning

,

printWarning

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Return the

included

classes and interfaces in all packages.

Return a ClassDoc for the specified class or interface name.

Command line options.

Return a PackageDoc for the specified package name.

Return the classes and interfaces

specified

as source file names on the command line.

Return the packages

specified

on the command line.

Methods declared in interface com.sun.javadoc.

Doc

commentText

,

compareTo

,

firstSentenceTags

,

getRawCommentText

,

inlineTags

,

isAnnotationType

,

isAnnotationTypeElement

,

isClass

,

isConstructor

,

isEnum

,

isEnumConstant

,

isError

,

isException

,

isField

,

isIncluded

,

isInterface

,

isMethod

,

isOrdinaryClass

,

name

,

position

,

seeTags

,

setRawCommentText

,

tags

,

tags

---

#### Methods declared in interface com.sun.javadoc. Doc

Methods declared in interface com.sun.javadoc.

DocErrorReporter

printError

,

printError

,

printNotice

,

printNotice

,

printWarning

,

printWarning

---

#### Methods declared in interface com.sun.javadoc. DocErrorReporter

============ METHOD DETAIL ==========

- Method Detail

- options

```java
String
[][] options()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Command line options.

For example, given:

```java
javadoc -foo this that -bar other ...
```

this method will return:

```java
options()[0][0] = "-foo"
options()[0][1] = "this"
options()[0][2] = "that"
options()[1][0] = "-bar"
options()[1][1] = "other"
```

**Returns:** an array of arrays of String.

- specifiedPackages

```java
PackageDoc
[] specifiedPackages()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the packages

specified

on the command line.
If

-subpackages

and

-exclude

options
are used, return all the non-excluded packages.

**Returns:** packages specified on the command line.

- specifiedClasses

```java
ClassDoc
[] specifiedClasses()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the classes and interfaces

specified

as source file names on the command line.

**Returns:** classes and interfaces specified on the command line.

- classes

```java
ClassDoc
[] classes()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the

included

classes and interfaces in all packages.

**Returns:** included classes and interfaces in all packages.

- packageNamed

```java
PackageDoc
packageNamed​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return a PackageDoc for the specified package name.

**Parameters:** name

- package name
**Returns:** a PackageDoc holding the specified package, null if
this package is not referenced.

- classNamed

```java
ClassDoc
classNamed​(
String
qualifiedName)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return a ClassDoc for the specified class or interface name.

**Parameters:** qualifiedName

-

qualified

class or package name
**Returns:** a ClassDoc holding the specified class, null if
this class is not referenced.

Method Detail

- options

```java
String
[][] options()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Command line options.

For example, given:

```java
javadoc -foo this that -bar other ...
```

this method will return:

```java
options()[0][0] = "-foo"
options()[0][1] = "this"
options()[0][2] = "that"
options()[1][0] = "-bar"
options()[1][1] = "other"
```

**Returns:** an array of arrays of String.

- specifiedPackages

```java
PackageDoc
[] specifiedPackages()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the packages

specified

on the command line.
If

-subpackages

and

-exclude

options
are used, return all the non-excluded packages.

**Returns:** packages specified on the command line.

- specifiedClasses

```java
ClassDoc
[] specifiedClasses()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the classes and interfaces

specified

as source file names on the command line.

**Returns:** classes and interfaces specified on the command line.

- classes

```java
ClassDoc
[] classes()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the

included

classes and interfaces in all packages.

**Returns:** included classes and interfaces in all packages.

- packageNamed

```java
PackageDoc
packageNamed​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return a PackageDoc for the specified package name.

**Parameters:** name

- package name
**Returns:** a PackageDoc holding the specified package, null if
this package is not referenced.

- classNamed

```java
ClassDoc
classNamed​(
String
qualifiedName)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return a ClassDoc for the specified class or interface name.

**Parameters:** qualifiedName

-

qualified

class or package name
**Returns:** a ClassDoc holding the specified class, null if
this class is not referenced.

---

#### Method Detail

options

```java
String
[][] options()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Command line options.

For example, given:

```java
javadoc -foo this that -bar other ...
```

this method will return:

```java
options()[0][0] = "-foo"
options()[0][1] = "this"
options()[0][2] = "that"
options()[1][0] = "-bar"
options()[1][1] = "other"
```

**Returns:** an array of arrays of String.

---

#### options

String

[][] options()

Command line options.

For example, given:

```java
javadoc -foo this that -bar other ...
```

this method will return:

```java
options()[0][0] = "-foo"
options()[0][1] = "this"
options()[0][2] = "that"
options()[1][0] = "-bar"
options()[1][1] = "other"
```

For example, given:

```java
javadoc -foo this that -bar other ...
```

this method will return:

```java
options()[0][0] = "-foo"
options()[0][1] = "this"
options()[0][2] = "that"
options()[1][0] = "-bar"
options()[1][1] = "other"
```

javadoc -foo this that -bar other ...

options()[0][0] = "-foo"
options()[0][1] = "this"
options()[0][2] = "that"
options()[1][0] = "-bar"
options()[1][1] = "other"

specifiedPackages

```java
PackageDoc
[] specifiedPackages()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the packages

specified

on the command line.
If

-subpackages

and

-exclude

options
are used, return all the non-excluded packages.

**Returns:** packages specified on the command line.

---

#### specifiedPackages

PackageDoc

[] specifiedPackages()

Return the packages

specified

on the command line.
If

-subpackages

and

-exclude

options
are used, return all the non-excluded packages.

specifiedClasses

```java
ClassDoc
[] specifiedClasses()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the classes and interfaces

specified

as source file names on the command line.

**Returns:** classes and interfaces specified on the command line.

---

#### specifiedClasses

ClassDoc

[] specifiedClasses()

Return the classes and interfaces

specified

as source file names on the command line.

classes

```java
ClassDoc
[] classes()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the

included

classes and interfaces in all packages.

**Returns:** included classes and interfaces in all packages.

---

#### classes

ClassDoc

[] classes()

Return the

included

classes and interfaces in all packages.

packageNamed

```java
PackageDoc
packageNamed​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return a PackageDoc for the specified package name.

**Parameters:** name

- package name
**Returns:** a PackageDoc holding the specified package, null if
this package is not referenced.

---

#### packageNamed

PackageDoc

packageNamed​(

String

name)

Return a PackageDoc for the specified package name.

classNamed

```java
ClassDoc
classNamed​(
String
qualifiedName)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return a ClassDoc for the specified class or interface name.

**Parameters:** qualifiedName

-

qualified

class or package name
**Returns:** a ClassDoc holding the specified class, null if
this class is not referenced.

---

#### classNamed

ClassDoc

classNamed​(

String

qualifiedName)

Return a ClassDoc for the specified class or interface name.

---

