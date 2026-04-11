# Interface PackageDoc

**Source:** `jdk.javadoc\com\sun\javadoc\PackageDoc.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
PackageDoc

extends
Doc
```

Represents a java package. Provides access to information
about the package, the package's comment and tags, and the
classes in the package.

Each method whose return type is an array will return an empty
array (never null) when there are no objects in the result.

**All Superinterfaces:** Comparable

<

Object

>

,

Doc

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ClassDoc
[] allClasses​(boolean filter)

Get all classes and interfaces in the package, filtered to the specified

access
modifier option

.

**Parameters:**
- filter

- Specifying true filters according to the specified access
modifier option.
Specifying false includes all classes and interfaces
regardless of access modifier option.

**Returns:**
- filtered classes and interfaces in this package

**Since:**
- 1.4

---

#### ClassDoc
[] allClasses()

Get all

included

classes and interfaces in the package. Same as allClasses(true).

**Returns:**
- all included classes and interfaces in this package.

---

#### ClassDoc
[] ordinaryClasses()

Get included

ordinary

classes (that is, exclude exceptions, errors, enums, interfaces, and
annotation types)
in this package.

**Returns:**
- included ordinary classes in this package.

---

#### ClassDoc
[] exceptions()

Get included Exception classes in this package.

**Returns:**
- included Exceptions in this package.

---

#### ClassDoc
[] errors()

Get included Error classes in this package.

**Returns:**
- included Errors in this package.

---

#### ClassDoc
[] enums()

Get included enum types in this package.

**Returns:**
- included enum types in this package.

**Since:**
- 1.5

---

#### ClassDoc
[] interfaces()

Get included interfaces in this package, omitting annotation types.

**Returns:**
- included interfaces in this package.

---

#### AnnotationTypeDoc
[] annotationTypes()

Get included annotation types in this package.

**Returns:**
- included annotation types in this package.

**Since:**
- 1.5

---

#### AnnotationDesc
[] annotations()

Get the annotations of this package.
Return an empty array if there are none.

**Returns:**
- the annotations of this package.

**Since:**
- 1.5

---

#### ClassDoc
findClass​(
String
className)

Lookup a class or interface within this package.

**Parameters:**
- className

- A String containing the name of the class to look up.

**Returns:**
- ClassDoc of found class or interface,
or null if not found.

---

### Additional Sections

#### Interface PackageDoc

**All Superinterfaces:** Comparable

<

Object

>

,

Doc

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
PackageDoc

extends
Doc
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Represents a java package. Provides access to information
about the package, the package's comment and tags, and the
classes in the package.

Each method whose return type is an array will return an empty
array (never null) when there are no objects in the result.

**Since:** 1.2

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

PackageDoc

extends

Doc

Represents a java package. Provides access to information
about the package, the package's comment and tags, and the
classes in the package.

Each method whose return type is an array will return an empty
array (never null) when there are no objects in the result.

Each method whose return type is an array will return an empty
array (never null) when there are no objects in the result.

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

allClasses

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get all

included

classes and interfaces in the package.

ClassDoc

[]

allClasses

​(boolean filter)

Deprecated, for removal: This API element is subject to removal in a future version.

Get all classes and interfaces in the package, filtered to the specified

access
modifier option

.

AnnotationDesc

[]

annotations

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this package.

AnnotationTypeDoc

[]

annotationTypes

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get included annotation types in this package.

ClassDoc

[]

enums

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get included enum types in this package.

ClassDoc

[]

errors

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get included Error classes in this package.

ClassDoc

[]

exceptions

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get included Exception classes in this package.

ClassDoc

findClass

​(

String

className)

Deprecated, for removal: This API element is subject to removal in a future version.

Lookup a class or interface within this package.

ClassDoc

[]

interfaces

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get included interfaces in this package, omitting annotation types.

ClassDoc

[]

ordinaryClasses

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get included

ordinary

classes (that is, exclude exceptions, errors, enums, interfaces, and
annotation types)
in this package.

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

allClasses

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get all

included

classes and interfaces in the package.

ClassDoc

[]

allClasses

​(boolean filter)

Deprecated, for removal: This API element is subject to removal in a future version.

Get all classes and interfaces in the package, filtered to the specified

access
modifier option

.

AnnotationDesc

[]

annotations

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this package.

AnnotationTypeDoc

[]

annotationTypes

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get included annotation types in this package.

ClassDoc

[]

enums

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get included enum types in this package.

ClassDoc

[]

errors

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get included Error classes in this package.

ClassDoc

[]

exceptions

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get included Exception classes in this package.

ClassDoc

findClass

​(

String

className)

Deprecated, for removal: This API element is subject to removal in a future version.

Lookup a class or interface within this package.

ClassDoc

[]

interfaces

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get included interfaces in this package, omitting annotation types.

ClassDoc

[]

ordinaryClasses

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get included

ordinary

classes (that is, exclude exceptions, errors, enums, interfaces, and
annotation types)
in this package.

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

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Get all

included

classes and interfaces in the package.

Get all classes and interfaces in the package, filtered to the specified

access
modifier option

.

Get the annotations of this package.

Get included annotation types in this package.

Get included enum types in this package.

Get included Error classes in this package.

Get included Exception classes in this package.

Lookup a class or interface within this package.

Get included interfaces in this package, omitting annotation types.

Get included

ordinary

classes (that is, exclude exceptions, errors, enums, interfaces, and
annotation types)
in this package.

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

============ METHOD DETAIL ==========

- Method Detail

- allClasses

```java
ClassDoc
[] allClasses​(boolean filter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get all classes and interfaces in the package, filtered to the specified

access
modifier option

.

**Parameters:** filter

- Specifying true filters according to the specified access
modifier option.
Specifying false includes all classes and interfaces
regardless of access modifier option.
**Returns:** filtered classes and interfaces in this package
**Since:** 1.4

- allClasses

```java
ClassDoc
[] allClasses()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get all

included

classes and interfaces in the package. Same as allClasses(true).

**Returns:** all included classes and interfaces in this package.

- ordinaryClasses

```java
ClassDoc
[] ordinaryClasses()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included

ordinary

classes (that is, exclude exceptions, errors, enums, interfaces, and
annotation types)
in this package.

**Returns:** included ordinary classes in this package.

- exceptions

```java
ClassDoc
[] exceptions()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included Exception classes in this package.

**Returns:** included Exceptions in this package.

- errors

```java
ClassDoc
[] errors()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included Error classes in this package.

**Returns:** included Errors in this package.

- enums

```java
ClassDoc
[] enums()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included enum types in this package.

**Returns:** included enum types in this package.
**Since:** 1.5

- interfaces

```java
ClassDoc
[] interfaces()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included interfaces in this package, omitting annotation types.

**Returns:** included interfaces in this package.

- annotationTypes

```java
AnnotationTypeDoc
[] annotationTypes()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included annotation types in this package.

**Returns:** included annotation types in this package.
**Since:** 1.5

- annotations

```java
AnnotationDesc
[] annotations()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this package.
Return an empty array if there are none.

**Returns:** the annotations of this package.
**Since:** 1.5

- findClass

```java
ClassDoc
findClass​(
String
className)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Lookup a class or interface within this package.

**Parameters:** className

- A String containing the name of the class to look up.
**Returns:** ClassDoc of found class or interface,
or null if not found.

Method Detail

- allClasses

```java
ClassDoc
[] allClasses​(boolean filter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get all classes and interfaces in the package, filtered to the specified

access
modifier option

.

**Parameters:** filter

- Specifying true filters according to the specified access
modifier option.
Specifying false includes all classes and interfaces
regardless of access modifier option.
**Returns:** filtered classes and interfaces in this package
**Since:** 1.4

- allClasses

```java
ClassDoc
[] allClasses()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get all

included

classes and interfaces in the package. Same as allClasses(true).

**Returns:** all included classes and interfaces in this package.

- ordinaryClasses

```java
ClassDoc
[] ordinaryClasses()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included

ordinary

classes (that is, exclude exceptions, errors, enums, interfaces, and
annotation types)
in this package.

**Returns:** included ordinary classes in this package.

- exceptions

```java
ClassDoc
[] exceptions()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included Exception classes in this package.

**Returns:** included Exceptions in this package.

- errors

```java
ClassDoc
[] errors()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included Error classes in this package.

**Returns:** included Errors in this package.

- enums

```java
ClassDoc
[] enums()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included enum types in this package.

**Returns:** included enum types in this package.
**Since:** 1.5

- interfaces

```java
ClassDoc
[] interfaces()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included interfaces in this package, omitting annotation types.

**Returns:** included interfaces in this package.

- annotationTypes

```java
AnnotationTypeDoc
[] annotationTypes()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included annotation types in this package.

**Returns:** included annotation types in this package.
**Since:** 1.5

- annotations

```java
AnnotationDesc
[] annotations()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this package.
Return an empty array if there are none.

**Returns:** the annotations of this package.
**Since:** 1.5

- findClass

```java
ClassDoc
findClass​(
String
className)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Lookup a class or interface within this package.

**Parameters:** className

- A String containing the name of the class to look up.
**Returns:** ClassDoc of found class or interface,
or null if not found.

---

#### Method Detail

allClasses

```java
ClassDoc
[] allClasses​(boolean filter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get all classes and interfaces in the package, filtered to the specified

access
modifier option

.

**Parameters:** filter

- Specifying true filters according to the specified access
modifier option.
Specifying false includes all classes and interfaces
regardless of access modifier option.
**Returns:** filtered classes and interfaces in this package
**Since:** 1.4

---

#### allClasses

ClassDoc

[] allClasses​(boolean filter)

Get all classes and interfaces in the package, filtered to the specified

access
modifier option

.

allClasses

```java
ClassDoc
[] allClasses()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get all

included

classes and interfaces in the package. Same as allClasses(true).

**Returns:** all included classes and interfaces in this package.

---

#### allClasses

ClassDoc

[] allClasses()

Get all

included

classes and interfaces in the package. Same as allClasses(true).

ordinaryClasses

```java
ClassDoc
[] ordinaryClasses()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included

ordinary

classes (that is, exclude exceptions, errors, enums, interfaces, and
annotation types)
in this package.

**Returns:** included ordinary classes in this package.

---

#### ordinaryClasses

ClassDoc

[] ordinaryClasses()

Get included

ordinary

classes (that is, exclude exceptions, errors, enums, interfaces, and
annotation types)
in this package.

exceptions

```java
ClassDoc
[] exceptions()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included Exception classes in this package.

**Returns:** included Exceptions in this package.

---

#### exceptions

ClassDoc

[] exceptions()

Get included Exception classes in this package.

errors

```java
ClassDoc
[] errors()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included Error classes in this package.

**Returns:** included Errors in this package.

---

#### errors

ClassDoc

[] errors()

Get included Error classes in this package.

enums

```java
ClassDoc
[] enums()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included enum types in this package.

**Returns:** included enum types in this package.
**Since:** 1.5

---

#### enums

ClassDoc

[] enums()

Get included enum types in this package.

interfaces

```java
ClassDoc
[] interfaces()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included interfaces in this package, omitting annotation types.

**Returns:** included interfaces in this package.

---

#### interfaces

ClassDoc

[] interfaces()

Get included interfaces in this package, omitting annotation types.

annotationTypes

```java
AnnotationTypeDoc
[] annotationTypes()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get included annotation types in this package.

**Returns:** included annotation types in this package.
**Since:** 1.5

---

#### annotationTypes

AnnotationTypeDoc

[] annotationTypes()

Get included annotation types in this package.

annotations

```java
AnnotationDesc
[] annotations()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this package.
Return an empty array if there are none.

**Returns:** the annotations of this package.
**Since:** 1.5

---

#### annotations

AnnotationDesc

[] annotations()

Get the annotations of this package.
Return an empty array if there are none.

findClass

```java
ClassDoc
findClass​(
String
className)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Lookup a class or interface within this package.

**Parameters:** className

- A String containing the name of the class to look up.
**Returns:** ClassDoc of found class or interface,
or null if not found.

---

#### findClass

ClassDoc

findClass​(

String

className)

Lookup a class or interface within this package.

---

