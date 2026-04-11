# Class Trees

**Source:** `jdk.compiler\com\sun\source\util\Trees.html`

### Class Description

```java
public abstract class
Trees

extends
Object
```

Bridges JSR 199, JSR 269, and the Tree API.

**Direct Known Subclasses:** DocTrees

---

### Field Details

*No entries found.*

### Constructor Details

#### public Trees()

*No description found.*

---

### Method Details

#### public static
Trees
instance​(
JavaCompiler.CompilationTask
task)

Returns a Trees object for a given CompilationTask.

**Parameters:**
- task

- the compilation task for which to get the Trees object

**Returns:**
- the Trees object

**Throws:**
- IllegalArgumentException

- if the task does not support the Trees API.

---

#### public static
Trees
instance​(
ProcessingEnvironment
env)

Returns a Trees object for a given ProcessingEnvironment.

**Parameters:**
- env

- the processing environment for which to get the Trees object

**Returns:**
- the Trees object

**Throws:**
- IllegalArgumentException

- if the env does not support the Trees API.

---

#### public abstract
SourcePositions
getSourcePositions()

Returns a utility object for obtaining source positions.

**Returns:**
- the utility object for obtaining source positions

---

#### public abstract
Tree
getTree​(
Element
element)

Returns the Tree node for a given Element.
Returns

null

if the node can not be found.

**Parameters:**
- element

- the element

**Returns:**
- the tree node

---

#### public abstract
ClassTree
getTree​(
TypeElement
element)

Returns the ClassTree node for a given TypeElement.
Returns

null

if the node can not be found.

**Parameters:**
- element

- the element

**Returns:**
- the class tree node

---

#### public abstract
MethodTree
getTree​(
ExecutableElement
method)

Returns the MethodTree node for a given ExecutableElement.
Returns

null

if the node can not be found.

**Parameters:**
- method

- the executable element

**Returns:**
- the method tree node

---

#### public abstract
Tree
getTree​(
Element
e,

AnnotationMirror
a)

Returns the Tree node for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

**Parameters:**
- e

- the element
- a

- the annotation mirror

**Returns:**
- the tree node

---

#### public abstract
Tree
getTree​(
Element
e,

AnnotationMirror
a,

AnnotationValue
v)

Returns the Tree node for an AnnotationValue for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

**Parameters:**
- e

- the element
- a

- the annotation mirror
- v

- the annotation value

**Returns:**
- the tree node

---

#### public abstract
TreePath
getPath​(
CompilationUnitTree
unit,

Tree
node)

Returns the path to tree node within the specified compilation unit.

**Parameters:**
- unit

- the compilation unit
- node

- the tree node

**Returns:**
- the tree path

---

#### public abstract
TreePath
getPath​(
Element
e)

Returns the TreePath node for a given Element.
Returns

null

if the node can not be found.

**Parameters:**
- e

- the element

**Returns:**
- the tree path

---

#### public abstract
TreePath
getPath​(
Element
e,

AnnotationMirror
a)

Returns the TreePath node for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

**Parameters:**
- e

- the element
- a

- the annotation mirror

**Returns:**
- the tree path

---

#### public abstract
TreePath
getPath​(
Element
e,

AnnotationMirror
a,

AnnotationValue
v)

Returns the TreePath node for an AnnotationValue for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

**Parameters:**
- e

- the element
- a

- the annotation mirror
- v

- the annotation value

**Returns:**
- the tree path

---

#### public abstract
Element
getElement​(
TreePath
path)

Returns the Element for the Tree node identified by a given TreePath.
Returns

null

if the element is not available.

**Parameters:**
- path

- the tree path

**Returns:**
- the element

**Throws:**
- IllegalArgumentException

- is the TreePath does not identify
a Tree node that might have an associated Element.

---

#### public abstract
TypeMirror
getTypeMirror​(
TreePath
path)

Returns the TypeMirror for the Tree node identified by a given TreePath.
Returns

null

if the TypeMirror is not available.

**Parameters:**
- path

- the tree path

**Returns:**
- the type mirror

**Throws:**
- IllegalArgumentException

- is the TreePath does not identify
a Tree node that might have an associated TypeMirror.

---

#### public abstract
Scope
getScope​(
TreePath
path)

Returns the Scope for the Tree node identified by a given TreePath.
Returns

null

if the Scope is not available.

**Parameters:**
- path

- the tree path

**Returns:**
- the scope

---

#### public abstract
String
getDocComment​(
TreePath
path)

Returns the doc comment, if any, for the Tree node identified by a given TreePath.
Returns

null

if no doc comment was found.

**Parameters:**
- path

- the tree path

**Returns:**
- the doc comment

**See Also:**
- DocTrees.getDocCommentTree(TreePath)

---

#### public abstract boolean isAccessible​(
Scope
scope,

TypeElement
type)

Checks whether a given type is accessible in a given scope.

**Parameters:**
- scope

- the scope to be checked
- type

- the type to be checked

**Returns:**
- true if

type

is accessible

---

#### public abstract boolean isAccessible​(
Scope
scope,

Element
member,

DeclaredType
type)

Checks whether the given element is accessible as a member of the given
type in a given scope.

**Parameters:**
- scope

- the scope to be checked
- member

- the member to be checked
- type

- the type for which to check if the member is accessible

**Returns:**
- true if

member

is accessible in

type

---

#### public abstract
TypeMirror
getOriginalType​(
ErrorType
errorType)

Returns the original type from the ErrorType object.

**Parameters:**
- errorType

- The errorType for which we want to get the original type.

**Returns:**
- javax.lang.model.type.TypeMirror corresponding to the original type, replaced by the ErrorType.

---

#### public abstract void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

Tree
t,

CompilationUnitTree
root)

Prints a message of the specified kind at the location of the
tree within the provided compilation unit

**Parameters:**
- kind

- the kind of message
- msg

- the message, or an empty string if none
- t

- the tree to use as a position hint
- root

- the compilation unit that contains tree

---

#### public abstract
TypeMirror
getLub​(
CatchTree
tree)

Returns the lub of an exception parameter declared in a catch clause.

**Parameters:**
- tree

- the tree for the catch clause

**Returns:**
- The lub of the exception parameter

---

### Additional Sections

#### Class Trees

java.lang.Object

- com.sun.source.util.Trees

com.sun.source.util.Trees

**Direct Known Subclasses:** DocTrees

```java
public abstract class
Trees

extends
Object
```

Bridges JSR 199, JSR 269, and the Tree API.

public abstract class

Trees

extends

Object

Bridges JSR 199, JSR 269, and the Tree API.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Trees

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

String

getDocComment

​(

TreePath

path)

Returns the doc comment, if any, for the Tree node identified by a given TreePath.

abstract

Element

getElement

​(

TreePath

path)

Returns the Element for the Tree node identified by a given TreePath.

abstract

TypeMirror

getLub

​(

CatchTree

tree)

Returns the lub of an exception parameter declared in a catch clause.

abstract

TypeMirror

getOriginalType

​(

ErrorType

errorType)

Returns the original type from the ErrorType object.

abstract

TreePath

getPath

​(

CompilationUnitTree

unit,

Tree

node)

Returns the path to tree node within the specified compilation unit.

abstract

TreePath

getPath

​(

Element

e)

Returns the TreePath node for a given Element.

abstract

TreePath

getPath

​(

Element

e,

AnnotationMirror

a)

Returns the TreePath node for an AnnotationMirror on a given Element.

abstract

TreePath

getPath

​(

Element

e,

AnnotationMirror

a,

AnnotationValue

v)

Returns the TreePath node for an AnnotationValue for an AnnotationMirror on a given Element.

abstract

Scope

getScope

​(

TreePath

path)

Returns the Scope for the Tree node identified by a given TreePath.

abstract

SourcePositions

getSourcePositions

()

Returns a utility object for obtaining source positions.

abstract

Tree

getTree

​(

Element

element)

Returns the Tree node for a given Element.

abstract

Tree

getTree

​(

Element

e,

AnnotationMirror

a)

Returns the Tree node for an AnnotationMirror on a given Element.

abstract

Tree

getTree

​(

Element

e,

AnnotationMirror

a,

AnnotationValue

v)

Returns the Tree node for an AnnotationValue for an AnnotationMirror on a given Element.

abstract

MethodTree

getTree

​(

ExecutableElement

method)

Returns the MethodTree node for a given ExecutableElement.

abstract

ClassTree

getTree

​(

TypeElement

element)

Returns the ClassTree node for a given TypeElement.

abstract

TypeMirror

getTypeMirror

​(

TreePath

path)

Returns the TypeMirror for the Tree node identified by a given TreePath.

static

Trees

instance

​(

ProcessingEnvironment

env)

Returns a Trees object for a given ProcessingEnvironment.

static

Trees

instance

​(

JavaCompiler.CompilationTask

task)

Returns a Trees object for a given CompilationTask.

abstract boolean

isAccessible

​(

Scope

scope,

Element

member,

DeclaredType

type)

Checks whether the given element is accessible as a member of the given
type in a given scope.

abstract boolean

isAccessible

​(

Scope

scope,

TypeElement

type)

Checks whether a given type is accessible in a given scope.

abstract void

printMessage

​(

Diagnostic.Kind

kind,

CharSequence

msg,

Tree

t,

CompilationUnitTree

root)

Prints a message of the specified kind at the location of the
tree within the provided compilation unit

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

Trees

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

String

getDocComment

​(

TreePath

path)

Returns the doc comment, if any, for the Tree node identified by a given TreePath.

abstract

Element

getElement

​(

TreePath

path)

Returns the Element for the Tree node identified by a given TreePath.

abstract

TypeMirror

getLub

​(

CatchTree

tree)

Returns the lub of an exception parameter declared in a catch clause.

abstract

TypeMirror

getOriginalType

​(

ErrorType

errorType)

Returns the original type from the ErrorType object.

abstract

TreePath

getPath

​(

CompilationUnitTree

unit,

Tree

node)

Returns the path to tree node within the specified compilation unit.

abstract

TreePath

getPath

​(

Element

e)

Returns the TreePath node for a given Element.

abstract

TreePath

getPath

​(

Element

e,

AnnotationMirror

a)

Returns the TreePath node for an AnnotationMirror on a given Element.

abstract

TreePath

getPath

​(

Element

e,

AnnotationMirror

a,

AnnotationValue

v)

Returns the TreePath node for an AnnotationValue for an AnnotationMirror on a given Element.

abstract

Scope

getScope

​(

TreePath

path)

Returns the Scope for the Tree node identified by a given TreePath.

abstract

SourcePositions

getSourcePositions

()

Returns a utility object for obtaining source positions.

abstract

Tree

getTree

​(

Element

element)

Returns the Tree node for a given Element.

abstract

Tree

getTree

​(

Element

e,

AnnotationMirror

a)

Returns the Tree node for an AnnotationMirror on a given Element.

abstract

Tree

getTree

​(

Element

e,

AnnotationMirror

a,

AnnotationValue

v)

Returns the Tree node for an AnnotationValue for an AnnotationMirror on a given Element.

abstract

MethodTree

getTree

​(

ExecutableElement

method)

Returns the MethodTree node for a given ExecutableElement.

abstract

ClassTree

getTree

​(

TypeElement

element)

Returns the ClassTree node for a given TypeElement.

abstract

TypeMirror

getTypeMirror

​(

TreePath

path)

Returns the TypeMirror for the Tree node identified by a given TreePath.

static

Trees

instance

​(

ProcessingEnvironment

env)

Returns a Trees object for a given ProcessingEnvironment.

static

Trees

instance

​(

JavaCompiler.CompilationTask

task)

Returns a Trees object for a given CompilationTask.

abstract boolean

isAccessible

​(

Scope

scope,

Element

member,

DeclaredType

type)

Checks whether the given element is accessible as a member of the given
type in a given scope.

abstract boolean

isAccessible

​(

Scope

scope,

TypeElement

type)

Checks whether a given type is accessible in a given scope.

abstract void

printMessage

​(

Diagnostic.Kind

kind,

CharSequence

msg,

Tree

t,

CompilationUnitTree

root)

Prints a message of the specified kind at the location of the
tree within the provided compilation unit

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the doc comment, if any, for the Tree node identified by a given TreePath.

Returns the Element for the Tree node identified by a given TreePath.

Returns the lub of an exception parameter declared in a catch clause.

Returns the original type from the ErrorType object.

Returns the path to tree node within the specified compilation unit.

Returns the TreePath node for a given Element.

Returns the TreePath node for an AnnotationMirror on a given Element.

Returns the TreePath node for an AnnotationValue for an AnnotationMirror on a given Element.

Returns the Scope for the Tree node identified by a given TreePath.

Returns a utility object for obtaining source positions.

Returns the Tree node for a given Element.

Returns the Tree node for an AnnotationMirror on a given Element.

Returns the Tree node for an AnnotationValue for an AnnotationMirror on a given Element.

Returns the MethodTree node for a given ExecutableElement.

Returns the ClassTree node for a given TypeElement.

Returns the TypeMirror for the Tree node identified by a given TreePath.

Returns a Trees object for a given ProcessingEnvironment.

Returns a Trees object for a given CompilationTask.

Checks whether the given element is accessible as a member of the given
type in a given scope.

Checks whether a given type is accessible in a given scope.

Prints a message of the specified kind at the location of the
tree within the provided compilation unit

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Trees

```java
public Trees()
```

============ METHOD DETAIL ==========

- Method Detail

- instance

```java
public static
Trees
instance​(
JavaCompiler.CompilationTask
task)
```

Returns a Trees object for a given CompilationTask.

**Parameters:** task

- the compilation task for which to get the Trees object
**Returns:** the Trees object
**Throws:** IllegalArgumentException

- if the task does not support the Trees API.

- instance

```java
public static
Trees
instance​(
ProcessingEnvironment
env)
```

Returns a Trees object for a given ProcessingEnvironment.

**Parameters:** env

- the processing environment for which to get the Trees object
**Returns:** the Trees object
**Throws:** IllegalArgumentException

- if the env does not support the Trees API.

- getSourcePositions

```java
public abstract
SourcePositions
getSourcePositions()
```

Returns a utility object for obtaining source positions.

**Returns:** the utility object for obtaining source positions

- getTree

```java
public abstract
Tree
getTree​(
Element
element)
```

Returns the Tree node for a given Element.
Returns

null

if the node can not be found.

**Parameters:** element

- the element
**Returns:** the tree node

- getTree

```java
public abstract
ClassTree
getTree​(
TypeElement
element)
```

Returns the ClassTree node for a given TypeElement.
Returns

null

if the node can not be found.

**Parameters:** element

- the element
**Returns:** the class tree node

- getTree

```java
public abstract
MethodTree
getTree​(
ExecutableElement
method)
```

Returns the MethodTree node for a given ExecutableElement.
Returns

null

if the node can not be found.

**Parameters:** method

- the executable element
**Returns:** the method tree node

- getTree

```java
public abstract
Tree
getTree​(
Element
e,

AnnotationMirror
a)
```

Returns the Tree node for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

**Parameters:** e

- the element
**Parameters:** a

- the annotation mirror
**Returns:** the tree node

- getTree

```java
public abstract
Tree
getTree​(
Element
e,

AnnotationMirror
a,

AnnotationValue
v)
```

Returns the Tree node for an AnnotationValue for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

**Parameters:** e

- the element
**Parameters:** a

- the annotation mirror
**Parameters:** v

- the annotation value
**Returns:** the tree node

- getPath

```java
public abstract
TreePath
getPath​(
CompilationUnitTree
unit,

Tree
node)
```

Returns the path to tree node within the specified compilation unit.

**Parameters:** unit

- the compilation unit
**Parameters:** node

- the tree node
**Returns:** the tree path

- getPath

```java
public abstract
TreePath
getPath​(
Element
e)
```

Returns the TreePath node for a given Element.
Returns

null

if the node can not be found.

**Parameters:** e

- the element
**Returns:** the tree path

- getPath

```java
public abstract
TreePath
getPath​(
Element
e,

AnnotationMirror
a)
```

Returns the TreePath node for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

**Parameters:** e

- the element
**Parameters:** a

- the annotation mirror
**Returns:** the tree path

- getPath

```java
public abstract
TreePath
getPath​(
Element
e,

AnnotationMirror
a,

AnnotationValue
v)
```

Returns the TreePath node for an AnnotationValue for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

**Parameters:** e

- the element
**Parameters:** a

- the annotation mirror
**Parameters:** v

- the annotation value
**Returns:** the tree path

- getElement

```java
public abstract
Element
getElement​(
TreePath
path)
```

Returns the Element for the Tree node identified by a given TreePath.
Returns

null

if the element is not available.

**Parameters:** path

- the tree path
**Returns:** the element
**Throws:** IllegalArgumentException

- is the TreePath does not identify
a Tree node that might have an associated Element.

- getTypeMirror

```java
public abstract
TypeMirror
getTypeMirror​(
TreePath
path)
```

Returns the TypeMirror for the Tree node identified by a given TreePath.
Returns

null

if the TypeMirror is not available.

**Parameters:** path

- the tree path
**Returns:** the type mirror
**Throws:** IllegalArgumentException

- is the TreePath does not identify
a Tree node that might have an associated TypeMirror.

- getScope

```java
public abstract
Scope
getScope​(
TreePath
path)
```

Returns the Scope for the Tree node identified by a given TreePath.
Returns

null

if the Scope is not available.

**Parameters:** path

- the tree path
**Returns:** the scope

- getDocComment

```java
public abstract
String
getDocComment​(
TreePath
path)
```

Returns the doc comment, if any, for the Tree node identified by a given TreePath.
Returns

null

if no doc comment was found.

**Parameters:** path

- the tree path
**Returns:** the doc comment
**See Also:** DocTrees.getDocCommentTree(TreePath)

- isAccessible

```java
public abstract boolean isAccessible​(
Scope
scope,

TypeElement
type)
```

Checks whether a given type is accessible in a given scope.

**Parameters:** scope

- the scope to be checked
**Parameters:** type

- the type to be checked
**Returns:** true if

type

is accessible

- isAccessible

```java
public abstract boolean isAccessible​(
Scope
scope,

Element
member,

DeclaredType
type)
```

Checks whether the given element is accessible as a member of the given
type in a given scope.

**Parameters:** scope

- the scope to be checked
**Parameters:** member

- the member to be checked
**Parameters:** type

- the type for which to check if the member is accessible
**Returns:** true if

member

is accessible in

type

- getOriginalType

```java
public abstract
TypeMirror
getOriginalType​(
ErrorType
errorType)
```

Returns the original type from the ErrorType object.

**Parameters:** errorType

- The errorType for which we want to get the original type.
**Returns:** javax.lang.model.type.TypeMirror corresponding to the original type, replaced by the ErrorType.

- printMessage

```java
public abstract void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

Tree
t,

CompilationUnitTree
root)
```

Prints a message of the specified kind at the location of the
tree within the provided compilation unit

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none
**Parameters:** t

- the tree to use as a position hint
**Parameters:** root

- the compilation unit that contains tree

- getLub

```java
public abstract
TypeMirror
getLub​(
CatchTree
tree)
```

Returns the lub of an exception parameter declared in a catch clause.

**Parameters:** tree

- the tree for the catch clause
**Returns:** The lub of the exception parameter

Constructor Detail

- Trees

```java
public Trees()
```

---

#### Constructor Detail

Trees

```java
public Trees()
```

---

#### Trees

public Trees()

Method Detail

- instance

```java
public static
Trees
instance​(
JavaCompiler.CompilationTask
task)
```

Returns a Trees object for a given CompilationTask.

**Parameters:** task

- the compilation task for which to get the Trees object
**Returns:** the Trees object
**Throws:** IllegalArgumentException

- if the task does not support the Trees API.

- instance

```java
public static
Trees
instance​(
ProcessingEnvironment
env)
```

Returns a Trees object for a given ProcessingEnvironment.

**Parameters:** env

- the processing environment for which to get the Trees object
**Returns:** the Trees object
**Throws:** IllegalArgumentException

- if the env does not support the Trees API.

- getSourcePositions

```java
public abstract
SourcePositions
getSourcePositions()
```

Returns a utility object for obtaining source positions.

**Returns:** the utility object for obtaining source positions

- getTree

```java
public abstract
Tree
getTree​(
Element
element)
```

Returns the Tree node for a given Element.
Returns

null

if the node can not be found.

**Parameters:** element

- the element
**Returns:** the tree node

- getTree

```java
public abstract
ClassTree
getTree​(
TypeElement
element)
```

Returns the ClassTree node for a given TypeElement.
Returns

null

if the node can not be found.

**Parameters:** element

- the element
**Returns:** the class tree node

- getTree

```java
public abstract
MethodTree
getTree​(
ExecutableElement
method)
```

Returns the MethodTree node for a given ExecutableElement.
Returns

null

if the node can not be found.

**Parameters:** method

- the executable element
**Returns:** the method tree node

- getTree

```java
public abstract
Tree
getTree​(
Element
e,

AnnotationMirror
a)
```

Returns the Tree node for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

**Parameters:** e

- the element
**Parameters:** a

- the annotation mirror
**Returns:** the tree node

- getTree

```java
public abstract
Tree
getTree​(
Element
e,

AnnotationMirror
a,

AnnotationValue
v)
```

Returns the Tree node for an AnnotationValue for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

**Parameters:** e

- the element
**Parameters:** a

- the annotation mirror
**Parameters:** v

- the annotation value
**Returns:** the tree node

- getPath

```java
public abstract
TreePath
getPath​(
CompilationUnitTree
unit,

Tree
node)
```

Returns the path to tree node within the specified compilation unit.

**Parameters:** unit

- the compilation unit
**Parameters:** node

- the tree node
**Returns:** the tree path

- getPath

```java
public abstract
TreePath
getPath​(
Element
e)
```

Returns the TreePath node for a given Element.
Returns

null

if the node can not be found.

**Parameters:** e

- the element
**Returns:** the tree path

- getPath

```java
public abstract
TreePath
getPath​(
Element
e,

AnnotationMirror
a)
```

Returns the TreePath node for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

**Parameters:** e

- the element
**Parameters:** a

- the annotation mirror
**Returns:** the tree path

- getPath

```java
public abstract
TreePath
getPath​(
Element
e,

AnnotationMirror
a,

AnnotationValue
v)
```

Returns the TreePath node for an AnnotationValue for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

**Parameters:** e

- the element
**Parameters:** a

- the annotation mirror
**Parameters:** v

- the annotation value
**Returns:** the tree path

- getElement

```java
public abstract
Element
getElement​(
TreePath
path)
```

Returns the Element for the Tree node identified by a given TreePath.
Returns

null

if the element is not available.

**Parameters:** path

- the tree path
**Returns:** the element
**Throws:** IllegalArgumentException

- is the TreePath does not identify
a Tree node that might have an associated Element.

- getTypeMirror

```java
public abstract
TypeMirror
getTypeMirror​(
TreePath
path)
```

Returns the TypeMirror for the Tree node identified by a given TreePath.
Returns

null

if the TypeMirror is not available.

**Parameters:** path

- the tree path
**Returns:** the type mirror
**Throws:** IllegalArgumentException

- is the TreePath does not identify
a Tree node that might have an associated TypeMirror.

- getScope

```java
public abstract
Scope
getScope​(
TreePath
path)
```

Returns the Scope for the Tree node identified by a given TreePath.
Returns

null

if the Scope is not available.

**Parameters:** path

- the tree path
**Returns:** the scope

- getDocComment

```java
public abstract
String
getDocComment​(
TreePath
path)
```

Returns the doc comment, if any, for the Tree node identified by a given TreePath.
Returns

null

if no doc comment was found.

**Parameters:** path

- the tree path
**Returns:** the doc comment
**See Also:** DocTrees.getDocCommentTree(TreePath)

- isAccessible

```java
public abstract boolean isAccessible​(
Scope
scope,

TypeElement
type)
```

Checks whether a given type is accessible in a given scope.

**Parameters:** scope

- the scope to be checked
**Parameters:** type

- the type to be checked
**Returns:** true if

type

is accessible

- isAccessible

```java
public abstract boolean isAccessible​(
Scope
scope,

Element
member,

DeclaredType
type)
```

Checks whether the given element is accessible as a member of the given
type in a given scope.

**Parameters:** scope

- the scope to be checked
**Parameters:** member

- the member to be checked
**Parameters:** type

- the type for which to check if the member is accessible
**Returns:** true if

member

is accessible in

type

- getOriginalType

```java
public abstract
TypeMirror
getOriginalType​(
ErrorType
errorType)
```

Returns the original type from the ErrorType object.

**Parameters:** errorType

- The errorType for which we want to get the original type.
**Returns:** javax.lang.model.type.TypeMirror corresponding to the original type, replaced by the ErrorType.

- printMessage

```java
public abstract void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

Tree
t,

CompilationUnitTree
root)
```

Prints a message of the specified kind at the location of the
tree within the provided compilation unit

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none
**Parameters:** t

- the tree to use as a position hint
**Parameters:** root

- the compilation unit that contains tree

- getLub

```java
public abstract
TypeMirror
getLub​(
CatchTree
tree)
```

Returns the lub of an exception parameter declared in a catch clause.

**Parameters:** tree

- the tree for the catch clause
**Returns:** The lub of the exception parameter

---

#### Method Detail

instance

```java
public static
Trees
instance​(
JavaCompiler.CompilationTask
task)
```

Returns a Trees object for a given CompilationTask.

**Parameters:** task

- the compilation task for which to get the Trees object
**Returns:** the Trees object
**Throws:** IllegalArgumentException

- if the task does not support the Trees API.

---

#### instance

public static

Trees

instance​(

JavaCompiler.CompilationTask

task)

Returns a Trees object for a given CompilationTask.

instance

```java
public static
Trees
instance​(
ProcessingEnvironment
env)
```

Returns a Trees object for a given ProcessingEnvironment.

**Parameters:** env

- the processing environment for which to get the Trees object
**Returns:** the Trees object
**Throws:** IllegalArgumentException

- if the env does not support the Trees API.

---

#### instance

public static

Trees

instance​(

ProcessingEnvironment

env)

Returns a Trees object for a given ProcessingEnvironment.

getSourcePositions

```java
public abstract
SourcePositions
getSourcePositions()
```

Returns a utility object for obtaining source positions.

**Returns:** the utility object for obtaining source positions

---

#### getSourcePositions

public abstract

SourcePositions

getSourcePositions()

Returns a utility object for obtaining source positions.

getTree

```java
public abstract
Tree
getTree​(
Element
element)
```

Returns the Tree node for a given Element.
Returns

null

if the node can not be found.

**Parameters:** element

- the element
**Returns:** the tree node

---

#### getTree

public abstract

Tree

getTree​(

Element

element)

Returns the Tree node for a given Element.
Returns

null

if the node can not be found.

getTree

```java
public abstract
ClassTree
getTree​(
TypeElement
element)
```

Returns the ClassTree node for a given TypeElement.
Returns

null

if the node can not be found.

**Parameters:** element

- the element
**Returns:** the class tree node

---

#### getTree

public abstract

ClassTree

getTree​(

TypeElement

element)

Returns the ClassTree node for a given TypeElement.
Returns

null

if the node can not be found.

getTree

```java
public abstract
MethodTree
getTree​(
ExecutableElement
method)
```

Returns the MethodTree node for a given ExecutableElement.
Returns

null

if the node can not be found.

**Parameters:** method

- the executable element
**Returns:** the method tree node

---

#### getTree

public abstract

MethodTree

getTree​(

ExecutableElement

method)

Returns the MethodTree node for a given ExecutableElement.
Returns

null

if the node can not be found.

getTree

```java
public abstract
Tree
getTree​(
Element
e,

AnnotationMirror
a)
```

Returns the Tree node for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

**Parameters:** e

- the element
**Parameters:** a

- the annotation mirror
**Returns:** the tree node

---

#### getTree

public abstract

Tree

getTree​(

Element

e,

AnnotationMirror

a)

Returns the Tree node for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

getTree

```java
public abstract
Tree
getTree​(
Element
e,

AnnotationMirror
a,

AnnotationValue
v)
```

Returns the Tree node for an AnnotationValue for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

**Parameters:** e

- the element
**Parameters:** a

- the annotation mirror
**Parameters:** v

- the annotation value
**Returns:** the tree node

---

#### getTree

public abstract

Tree

getTree​(

Element

e,

AnnotationMirror

a,

AnnotationValue

v)

Returns the Tree node for an AnnotationValue for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

getPath

```java
public abstract
TreePath
getPath​(
CompilationUnitTree
unit,

Tree
node)
```

Returns the path to tree node within the specified compilation unit.

**Parameters:** unit

- the compilation unit
**Parameters:** node

- the tree node
**Returns:** the tree path

---

#### getPath

public abstract

TreePath

getPath​(

CompilationUnitTree

unit,

Tree

node)

Returns the path to tree node within the specified compilation unit.

getPath

```java
public abstract
TreePath
getPath​(
Element
e)
```

Returns the TreePath node for a given Element.
Returns

null

if the node can not be found.

**Parameters:** e

- the element
**Returns:** the tree path

---

#### getPath

public abstract

TreePath

getPath​(

Element

e)

Returns the TreePath node for a given Element.
Returns

null

if the node can not be found.

getPath

```java
public abstract
TreePath
getPath​(
Element
e,

AnnotationMirror
a)
```

Returns the TreePath node for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

**Parameters:** e

- the element
**Parameters:** a

- the annotation mirror
**Returns:** the tree path

---

#### getPath

public abstract

TreePath

getPath​(

Element

e,

AnnotationMirror

a)

Returns the TreePath node for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

getPath

```java
public abstract
TreePath
getPath​(
Element
e,

AnnotationMirror
a,

AnnotationValue
v)
```

Returns the TreePath node for an AnnotationValue for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

**Parameters:** e

- the element
**Parameters:** a

- the annotation mirror
**Parameters:** v

- the annotation value
**Returns:** the tree path

---

#### getPath

public abstract

TreePath

getPath​(

Element

e,

AnnotationMirror

a,

AnnotationValue

v)

Returns the TreePath node for an AnnotationValue for an AnnotationMirror on a given Element.
Returns

null

if the node can not be found.

getElement

```java
public abstract
Element
getElement​(
TreePath
path)
```

Returns the Element for the Tree node identified by a given TreePath.
Returns

null

if the element is not available.

**Parameters:** path

- the tree path
**Returns:** the element
**Throws:** IllegalArgumentException

- is the TreePath does not identify
a Tree node that might have an associated Element.

---

#### getElement

public abstract

Element

getElement​(

TreePath

path)

Returns the Element for the Tree node identified by a given TreePath.
Returns

null

if the element is not available.

getTypeMirror

```java
public abstract
TypeMirror
getTypeMirror​(
TreePath
path)
```

Returns the TypeMirror for the Tree node identified by a given TreePath.
Returns

null

if the TypeMirror is not available.

**Parameters:** path

- the tree path
**Returns:** the type mirror
**Throws:** IllegalArgumentException

- is the TreePath does not identify
a Tree node that might have an associated TypeMirror.

---

#### getTypeMirror

public abstract

TypeMirror

getTypeMirror​(

TreePath

path)

Returns the TypeMirror for the Tree node identified by a given TreePath.
Returns

null

if the TypeMirror is not available.

getScope

```java
public abstract
Scope
getScope​(
TreePath
path)
```

Returns the Scope for the Tree node identified by a given TreePath.
Returns

null

if the Scope is not available.

**Parameters:** path

- the tree path
**Returns:** the scope

---

#### getScope

public abstract

Scope

getScope​(

TreePath

path)

Returns the Scope for the Tree node identified by a given TreePath.
Returns

null

if the Scope is not available.

getDocComment

```java
public abstract
String
getDocComment​(
TreePath
path)
```

Returns the doc comment, if any, for the Tree node identified by a given TreePath.
Returns

null

if no doc comment was found.

**Parameters:** path

- the tree path
**Returns:** the doc comment
**See Also:** DocTrees.getDocCommentTree(TreePath)

---

#### getDocComment

public abstract

String

getDocComment​(

TreePath

path)

Returns the doc comment, if any, for the Tree node identified by a given TreePath.
Returns

null

if no doc comment was found.

isAccessible

```java
public abstract boolean isAccessible​(
Scope
scope,

TypeElement
type)
```

Checks whether a given type is accessible in a given scope.

**Parameters:** scope

- the scope to be checked
**Parameters:** type

- the type to be checked
**Returns:** true if

type

is accessible

---

#### isAccessible

public abstract boolean isAccessible​(

Scope

scope,

TypeElement

type)

Checks whether a given type is accessible in a given scope.

isAccessible

```java
public abstract boolean isAccessible​(
Scope
scope,

Element
member,

DeclaredType
type)
```

Checks whether the given element is accessible as a member of the given
type in a given scope.

**Parameters:** scope

- the scope to be checked
**Parameters:** member

- the member to be checked
**Parameters:** type

- the type for which to check if the member is accessible
**Returns:** true if

member

is accessible in

type

---

#### isAccessible

public abstract boolean isAccessible​(

Scope

scope,

Element

member,

DeclaredType

type)

Checks whether the given element is accessible as a member of the given
type in a given scope.

getOriginalType

```java
public abstract
TypeMirror
getOriginalType​(
ErrorType
errorType)
```

Returns the original type from the ErrorType object.

**Parameters:** errorType

- The errorType for which we want to get the original type.
**Returns:** javax.lang.model.type.TypeMirror corresponding to the original type, replaced by the ErrorType.

---

#### getOriginalType

public abstract

TypeMirror

getOriginalType​(

ErrorType

errorType)

Returns the original type from the ErrorType object.

printMessage

```java
public abstract void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

Tree
t,

CompilationUnitTree
root)
```

Prints a message of the specified kind at the location of the
tree within the provided compilation unit

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none
**Parameters:** t

- the tree to use as a position hint
**Parameters:** root

- the compilation unit that contains tree

---

#### printMessage

public abstract void printMessage​(

Diagnostic.Kind

kind,

CharSequence

msg,

Tree

t,

CompilationUnitTree

root)

Prints a message of the specified kind at the location of the
tree within the provided compilation unit

getLub

```java
public abstract
TypeMirror
getLub​(
CatchTree
tree)
```

Returns the lub of an exception parameter declared in a catch clause.

**Parameters:** tree

- the tree for the catch clause
**Returns:** The lub of the exception parameter

---

#### getLub

public abstract

TypeMirror

getLub​(

CatchTree

tree)

Returns the lub of an exception parameter declared in a catch clause.

---

