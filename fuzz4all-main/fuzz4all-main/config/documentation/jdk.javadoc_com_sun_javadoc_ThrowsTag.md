# Interface ThrowsTag

**Source:** `jdk.javadoc\com\sun\javadoc\ThrowsTag.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
ThrowsTag

extends
Tag
```

Represents a @throws or @exception documentation tag.
Parses and holds the exception name and exception comment.
Note: @exception is a backwards compatible synonymy for @throws.

**All Superinterfaces:** Tag

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
exceptionName()

Return the name of the exception
associated with this

ThrowsTag

.

**Returns:**
- name of the exception.

---

#### String
exceptionComment()

Return the exception comment
associated with this

ThrowsTag

.

**Returns:**
- exception comment.

---

#### ClassDoc
exception()

Return a

ClassDoc

that represents the exception.
If the type of the exception is a type variable, return the

ClassDoc

of its erasure.

This method cannot accommodate certain generic type
constructs. The

exceptionType

method
should be used instead.

**Returns:**
- ClassDoc

that represents the exception.

**See Also:**
- exceptionType()

---

#### Type
exceptionType()

Return the type of the exception
associated with this

ThrowsTag

.
This may be a

ClassDoc

or a

TypeVariable

.

**Returns:**
- the type of the exception.

**Since:**
- 1.5

---

### Additional Sections

#### Interface ThrowsTag

**All Superinterfaces:** Tag

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
ThrowsTag

extends
Tag
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Represents a @throws or @exception documentation tag.
Parses and holds the exception name and exception comment.
Note: @exception is a backwards compatible synonymy for @throws.

**See Also:** ExecutableMemberDoc.throwsTags()

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

ThrowsTag

extends

Tag

Represents a @throws or @exception documentation tag.
Parses and holds the exception name and exception comment.
Note: @exception is a backwards compatible synonymy for @throws.

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

exception

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return a

ClassDoc

that represents the exception.

String

exceptionComment

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the exception comment
associated with this

ThrowsTag

.

String

exceptionName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the name of the exception
associated with this

ThrowsTag

.

Type

exceptionType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type of the exception
associated with this

ThrowsTag

.

- Methods declared in interface com.sun.javadoc.

Tag

firstSentenceTags

,

holder

,

inlineTags

,

kind

,

name

,

position

,

text

,

toString

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

ClassDoc

exception

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return a

ClassDoc

that represents the exception.

String

exceptionComment

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the exception comment
associated with this

ThrowsTag

.

String

exceptionName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the name of the exception
associated with this

ThrowsTag

.

Type

exceptionType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type of the exception
associated with this

ThrowsTag

.

- Methods declared in interface com.sun.javadoc.

Tag

firstSentenceTags

,

holder

,

inlineTags

,

kind

,

name

,

position

,

text

,

toString

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Return a

ClassDoc

that represents the exception.

Return the exception comment
associated with this

ThrowsTag

.

Return the name of the exception
associated with this

ThrowsTag

.

Return the type of the exception
associated with this

ThrowsTag

.

Methods declared in interface com.sun.javadoc.

Tag

firstSentenceTags

,

holder

,

inlineTags

,

kind

,

name

,

position

,

text

,

toString

---

#### Methods declared in interface com.sun.javadoc. Tag

============ METHOD DETAIL ==========

- Method Detail

- exceptionName

```java
String
exceptionName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the name of the exception
associated with this

ThrowsTag

.

**Returns:** name of the exception.

- exceptionComment

```java
String
exceptionComment()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the exception comment
associated with this

ThrowsTag

.

**Returns:** exception comment.

- exception

```java
ClassDoc
exception()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return a

ClassDoc

that represents the exception.
If the type of the exception is a type variable, return the

ClassDoc

of its erasure.

This method cannot accommodate certain generic type
constructs. The

exceptionType

method
should be used instead.

**Returns:** ClassDoc

that represents the exception.
**See Also:** exceptionType()

- exceptionType

```java
Type
exceptionType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type of the exception
associated with this

ThrowsTag

.
This may be a

ClassDoc

or a

TypeVariable

.

**Returns:** the type of the exception.
**Since:** 1.5

Method Detail

- exceptionName

```java
String
exceptionName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the name of the exception
associated with this

ThrowsTag

.

**Returns:** name of the exception.

- exceptionComment

```java
String
exceptionComment()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the exception comment
associated with this

ThrowsTag

.

**Returns:** exception comment.

- exception

```java
ClassDoc
exception()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return a

ClassDoc

that represents the exception.
If the type of the exception is a type variable, return the

ClassDoc

of its erasure.

This method cannot accommodate certain generic type
constructs. The

exceptionType

method
should be used instead.

**Returns:** ClassDoc

that represents the exception.
**See Also:** exceptionType()

- exceptionType

```java
Type
exceptionType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type of the exception
associated with this

ThrowsTag

.
This may be a

ClassDoc

or a

TypeVariable

.

**Returns:** the type of the exception.
**Since:** 1.5

---

#### Method Detail

exceptionName

```java
String
exceptionName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the name of the exception
associated with this

ThrowsTag

.

**Returns:** name of the exception.

---

#### exceptionName

String

exceptionName()

Return the name of the exception
associated with this

ThrowsTag

.

exceptionComment

```java
String
exceptionComment()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the exception comment
associated with this

ThrowsTag

.

**Returns:** exception comment.

---

#### exceptionComment

String

exceptionComment()

Return the exception comment
associated with this

ThrowsTag

.

exception

```java
ClassDoc
exception()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return a

ClassDoc

that represents the exception.
If the type of the exception is a type variable, return the

ClassDoc

of its erasure.

This method cannot accommodate certain generic type
constructs. The

exceptionType

method
should be used instead.

**Returns:** ClassDoc

that represents the exception.
**See Also:** exceptionType()

---

#### exception

ClassDoc

exception()

Return a

ClassDoc

that represents the exception.
If the type of the exception is a type variable, return the

ClassDoc

of its erasure.

This method cannot accommodate certain generic type
constructs. The

exceptionType

method
should be used instead.

This method cannot accommodate certain generic type
constructs. The

exceptionType

method
should be used instead.

exceptionType

```java
Type
exceptionType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type of the exception
associated with this

ThrowsTag

.
This may be a

ClassDoc

or a

TypeVariable

.

**Returns:** the type of the exception.
**Since:** 1.5

---

#### exceptionType

Type

exceptionType()

Return the type of the exception
associated with this

ThrowsTag

.
This may be a

ClassDoc

or a

TypeVariable

.

---

