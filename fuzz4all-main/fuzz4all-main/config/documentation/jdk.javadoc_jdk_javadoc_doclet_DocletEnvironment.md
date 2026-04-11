# Interface DocletEnvironment

**Source:** `jdk.javadoc\jdk\javadoc\doclet\DocletEnvironment.html`

### Class Description

```java
public interface
DocletEnvironment
```

Represents the operating environment of a single invocation
of the doclet. This object can be used to access the program
structures, various utilities and the user specified elements
on the command line.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Set
<? extends
Element
> getSpecifiedElements()

Returns the elements

specified

when the tool is invoked.

**Returns:**
- the set of specified elements

---

#### Set
<? extends
Element
> getIncludedElements()

Returns the module, package and type elements that should be

included

in the
documentation.

**Returns:**
- the set of included elements

---

#### DocTrees
getDocTrees()

Returns an instance of the

DocTrees

utility class.
This class provides methods to access

TreePath

s,

DocCommentTree

s
and so on.

**Returns:**
- a utility class to operate on doc trees

---

#### Elements
getElementUtils()

Returns an instance of the

Elements

utility class.
This class provides methods for operating on

elements

.

**Returns:**
- a utility class to operate on elements

---

#### Types
getTypeUtils()

Returns an instance of the

Types

utility class.
This class provides methods for operating on

type mirrors

.

**Returns:**
- a utility class to operate on type mirrors

---

#### boolean isIncluded​(
Element
e)

Returns true if an element should be

included

in the
documentation.

**Parameters:**
- e

- the element

**Returns:**
- true if included, false otherwise

---

#### boolean isSelected​(
Element
e)

Returns true if the element is

selected

.

**Parameters:**
- e

- the element

**Returns:**
- true if selected, false otherwise

---

#### JavaFileManager
getJavaFileManager()

Returns the file manager used to read and write files.

**Returns:**
- the file manager used to read and write files

---

#### SourceVersion
getSourceVersion()

Returns the source version of the source files that were read.

**Returns:**
- the source version

---

#### DocletEnvironment.ModuleMode
getModuleMode()

Returns the required level of module documentation.

**Returns:**
- the required level of module documentation

---

#### JavaFileObject.Kind
getFileKind​(
TypeElement
type)

Returns the file kind of a type element.

**Parameters:**
- type

- the type element

**Returns:**
- the file kind

---

### Additional Sections

#### Interface DocletEnvironment

```java
public interface
DocletEnvironment
```

Represents the operating environment of a single invocation
of the doclet. This object can be used to access the program
structures, various utilities and the user specified elements
on the command line.

**Since:** 9

public interface

DocletEnvironment

Represents the operating environment of a single invocation
of the doclet. This object can be used to access the program
structures, various utilities and the user specified elements
on the command line.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

DocletEnvironment.ModuleMode

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

DocTrees

getDocTrees

()

Returns an instance of the

DocTrees

utility class.

Elements

getElementUtils

()

Returns an instance of the

Elements

utility class.

JavaFileObject.Kind

getFileKind

​(

TypeElement

type)

Returns the file kind of a type element.

Set

<? extends

Element

>

getIncludedElements

()

Returns the module, package and type elements that should be

included

in the
documentation.

JavaFileManager

getJavaFileManager

()

Returns the file manager used to read and write files.

DocletEnvironment.ModuleMode

getModuleMode

()

Returns the required level of module documentation.

SourceVersion

getSourceVersion

()

Returns the source version of the source files that were read.

Set

<? extends

Element

>

getSpecifiedElements

()

Returns the elements

specified

when the tool is invoked.

Types

getTypeUtils

()

Returns an instance of the

Types

utility class.

boolean

isIncluded

​(

Element

e)

Returns true if an element should be

included

in the
documentation.

boolean

isSelected

​(

Element

e)

Returns true if the element is

selected

.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

DocletEnvironment.ModuleMode

---

#### Nested Class Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

DocTrees

getDocTrees

()

Returns an instance of the

DocTrees

utility class.

Elements

getElementUtils

()

Returns an instance of the

Elements

utility class.

JavaFileObject.Kind

getFileKind

​(

TypeElement

type)

Returns the file kind of a type element.

Set

<? extends

Element

>

getIncludedElements

()

Returns the module, package and type elements that should be

included

in the
documentation.

JavaFileManager

getJavaFileManager

()

Returns the file manager used to read and write files.

DocletEnvironment.ModuleMode

getModuleMode

()

Returns the required level of module documentation.

SourceVersion

getSourceVersion

()

Returns the source version of the source files that were read.

Set

<? extends

Element

>

getSpecifiedElements

()

Returns the elements

specified

when the tool is invoked.

Types

getTypeUtils

()

Returns an instance of the

Types

utility class.

boolean

isIncluded

​(

Element

e)

Returns true if an element should be

included

in the
documentation.

boolean

isSelected

​(

Element

e)

Returns true if the element is

selected

.

---

#### Method Summary

Returns an instance of the

DocTrees

utility class.

Returns an instance of the

Elements

utility class.

Returns the file kind of a type element.

Returns the module, package and type elements that should be

included

in the
documentation.

Returns the file manager used to read and write files.

Returns the required level of module documentation.

Returns the source version of the source files that were read.

Returns the elements

specified

when the tool is invoked.

Returns an instance of the

Types

utility class.

Returns true if an element should be

included

in the
documentation.

Returns true if the element is

selected

.

============ METHOD DETAIL ==========

- Method Detail

- getSpecifiedElements

```java
Set
<? extends
Element
> getSpecifiedElements()
```

Returns the elements

specified

when the tool is invoked.

**Returns:** the set of specified elements

- getIncludedElements

```java
Set
<? extends
Element
> getIncludedElements()
```

Returns the module, package and type elements that should be

included

in the
documentation.

**Returns:** the set of included elements

- getDocTrees

```java
DocTrees
getDocTrees()
```

Returns an instance of the

DocTrees

utility class.
This class provides methods to access

TreePath

s,

DocCommentTree

s
and so on.

**Returns:** a utility class to operate on doc trees

- getElementUtils

```java
Elements
getElementUtils()
```

Returns an instance of the

Elements

utility class.
This class provides methods for operating on

elements

.

**Returns:** a utility class to operate on elements

- getTypeUtils

```java
Types
getTypeUtils()
```

Returns an instance of the

Types

utility class.
This class provides methods for operating on

type mirrors

.

**Returns:** a utility class to operate on type mirrors

- isIncluded

```java
boolean isIncluded​(
Element
e)
```

Returns true if an element should be

included

in the
documentation.

**Parameters:** e

- the element
**Returns:** true if included, false otherwise

- isSelected

```java
boolean isSelected​(
Element
e)
```

Returns true if the element is

selected

.

**Parameters:** e

- the element
**Returns:** true if selected, false otherwise

- getJavaFileManager

```java
JavaFileManager
getJavaFileManager()
```

Returns the file manager used to read and write files.

**Returns:** the file manager used to read and write files

- getSourceVersion

```java
SourceVersion
getSourceVersion()
```

Returns the source version of the source files that were read.

**Returns:** the source version

- getModuleMode

```java
DocletEnvironment.ModuleMode
getModuleMode()
```

Returns the required level of module documentation.

**Returns:** the required level of module documentation

- getFileKind

```java
JavaFileObject.Kind
getFileKind​(
TypeElement
type)
```

Returns the file kind of a type element.

**Parameters:** type

- the type element
**Returns:** the file kind

Method Detail

- getSpecifiedElements

```java
Set
<? extends
Element
> getSpecifiedElements()
```

Returns the elements

specified

when the tool is invoked.

**Returns:** the set of specified elements

- getIncludedElements

```java
Set
<? extends
Element
> getIncludedElements()
```

Returns the module, package and type elements that should be

included

in the
documentation.

**Returns:** the set of included elements

- getDocTrees

```java
DocTrees
getDocTrees()
```

Returns an instance of the

DocTrees

utility class.
This class provides methods to access

TreePath

s,

DocCommentTree

s
and so on.

**Returns:** a utility class to operate on doc trees

- getElementUtils

```java
Elements
getElementUtils()
```

Returns an instance of the

Elements

utility class.
This class provides methods for operating on

elements

.

**Returns:** a utility class to operate on elements

- getTypeUtils

```java
Types
getTypeUtils()
```

Returns an instance of the

Types

utility class.
This class provides methods for operating on

type mirrors

.

**Returns:** a utility class to operate on type mirrors

- isIncluded

```java
boolean isIncluded​(
Element
e)
```

Returns true if an element should be

included

in the
documentation.

**Parameters:** e

- the element
**Returns:** true if included, false otherwise

- isSelected

```java
boolean isSelected​(
Element
e)
```

Returns true if the element is

selected

.

**Parameters:** e

- the element
**Returns:** true if selected, false otherwise

- getJavaFileManager

```java
JavaFileManager
getJavaFileManager()
```

Returns the file manager used to read and write files.

**Returns:** the file manager used to read and write files

- getSourceVersion

```java
SourceVersion
getSourceVersion()
```

Returns the source version of the source files that were read.

**Returns:** the source version

- getModuleMode

```java
DocletEnvironment.ModuleMode
getModuleMode()
```

Returns the required level of module documentation.

**Returns:** the required level of module documentation

- getFileKind

```java
JavaFileObject.Kind
getFileKind​(
TypeElement
type)
```

Returns the file kind of a type element.

**Parameters:** type

- the type element
**Returns:** the file kind

---

#### Method Detail

getSpecifiedElements

```java
Set
<? extends
Element
> getSpecifiedElements()
```

Returns the elements

specified

when the tool is invoked.

**Returns:** the set of specified elements

---

#### getSpecifiedElements

Set

<? extends

Element

> getSpecifiedElements()

Returns the elements

specified

when the tool is invoked.

getIncludedElements

```java
Set
<? extends
Element
> getIncludedElements()
```

Returns the module, package and type elements that should be

included

in the
documentation.

**Returns:** the set of included elements

---

#### getIncludedElements

Set

<? extends

Element

> getIncludedElements()

Returns the module, package and type elements that should be

included

in the
documentation.

getDocTrees

```java
DocTrees
getDocTrees()
```

Returns an instance of the

DocTrees

utility class.
This class provides methods to access

TreePath

s,

DocCommentTree

s
and so on.

**Returns:** a utility class to operate on doc trees

---

#### getDocTrees

DocTrees

getDocTrees()

Returns an instance of the

DocTrees

utility class.
This class provides methods to access

TreePath

s,

DocCommentTree

s
and so on.

getElementUtils

```java
Elements
getElementUtils()
```

Returns an instance of the

Elements

utility class.
This class provides methods for operating on

elements

.

**Returns:** a utility class to operate on elements

---

#### getElementUtils

Elements

getElementUtils()

Returns an instance of the

Elements

utility class.
This class provides methods for operating on

elements

.

getTypeUtils

```java
Types
getTypeUtils()
```

Returns an instance of the

Types

utility class.
This class provides methods for operating on

type mirrors

.

**Returns:** a utility class to operate on type mirrors

---

#### getTypeUtils

Types

getTypeUtils()

Returns an instance of the

Types

utility class.
This class provides methods for operating on

type mirrors

.

isIncluded

```java
boolean isIncluded​(
Element
e)
```

Returns true if an element should be

included

in the
documentation.

**Parameters:** e

- the element
**Returns:** true if included, false otherwise

---

#### isIncluded

boolean isIncluded​(

Element

e)

Returns true if an element should be

included

in the
documentation.

isSelected

```java
boolean isSelected​(
Element
e)
```

Returns true if the element is

selected

.

**Parameters:** e

- the element
**Returns:** true if selected, false otherwise

---

#### isSelected

boolean isSelected​(

Element

e)

Returns true if the element is

selected

.

getJavaFileManager

```java
JavaFileManager
getJavaFileManager()
```

Returns the file manager used to read and write files.

**Returns:** the file manager used to read and write files

---

#### getJavaFileManager

JavaFileManager

getJavaFileManager()

Returns the file manager used to read and write files.

getSourceVersion

```java
SourceVersion
getSourceVersion()
```

Returns the source version of the source files that were read.

**Returns:** the source version

---

#### getSourceVersion

SourceVersion

getSourceVersion()

Returns the source version of the source files that were read.

getModuleMode

```java
DocletEnvironment.ModuleMode
getModuleMode()
```

Returns the required level of module documentation.

**Returns:** the required level of module documentation

---

#### getModuleMode

DocletEnvironment.ModuleMode

getModuleMode()

Returns the required level of module documentation.

getFileKind

```java
JavaFileObject.Kind
getFileKind​(
TypeElement
type)
```

Returns the file kind of a type element.

**Parameters:** type

- the type element
**Returns:** the file kind

---

#### getFileKind

JavaFileObject.Kind

getFileKind​(

TypeElement

type)

Returns the file kind of a type element.

---

