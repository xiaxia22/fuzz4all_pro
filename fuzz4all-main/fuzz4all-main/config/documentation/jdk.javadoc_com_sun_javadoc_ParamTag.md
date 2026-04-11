# Interface ParamTag

**Source:** `jdk.javadoc\com\sun\javadoc\ParamTag.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
ParamTag

extends
Tag
```

Represents an @param documentation tag.
Stores the name and comment parts of the parameter tag.
An @param tag may represent either a method or constructor parameter,
or a type parameter.

**All Superinterfaces:** Tag

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
parameterName()

Return the name of the parameter or type parameter
associated with this

ParamTag

.
The angle brackets delimiting a type parameter are not part of
its name.

**Returns:**
- the parameter name.

---

#### String
parameterComment()

Return the parameter comment
associated with this

ParamTag

.

**Returns:**
- the parameter comment.

---

#### boolean isTypeParameter()

Return true if this

ParamTag

corresponds to a type
parameter. Return false if it corresponds to an ordinary parameter
of a method or constructor.

**Returns:**
- true if this

ParamTag

corresponds to a type
parameter.

**Since:**
- 1.5

---

### Additional Sections

#### Interface ParamTag

**All Superinterfaces:** Tag

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
ParamTag

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

Represents an @param documentation tag.
Stores the name and comment parts of the parameter tag.
An @param tag may represent either a method or constructor parameter,
or a type parameter.

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

ParamTag

extends

Tag

Represents an @param documentation tag.
Stores the name and comment parts of the parameter tag.
An @param tag may represent either a method or constructor parameter,
or a type parameter.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

isTypeParameter

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this

ParamTag

corresponds to a type
parameter.

String

parameterComment

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the parameter comment
associated with this

ParamTag

.

String

parameterName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the name of the parameter or type parameter
associated with this

ParamTag

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

boolean

isTypeParameter

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this

ParamTag

corresponds to a type
parameter.

String

parameterComment

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the parameter comment
associated with this

ParamTag

.

String

parameterName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the name of the parameter or type parameter
associated with this

ParamTag

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

Return true if this

ParamTag

corresponds to a type
parameter.

Return the parameter comment
associated with this

ParamTag

.

Return the name of the parameter or type parameter
associated with this

ParamTag

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

- parameterName

```java
String
parameterName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the name of the parameter or type parameter
associated with this

ParamTag

.
The angle brackets delimiting a type parameter are not part of
its name.

**Returns:** the parameter name.

- parameterComment

```java
String
parameterComment()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the parameter comment
associated with this

ParamTag

.

**Returns:** the parameter comment.

- isTypeParameter

```java
boolean isTypeParameter()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this

ParamTag

corresponds to a type
parameter. Return false if it corresponds to an ordinary parameter
of a method or constructor.

**Returns:** true if this

ParamTag

corresponds to a type
parameter.
**Since:** 1.5

Method Detail

- parameterName

```java
String
parameterName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the name of the parameter or type parameter
associated with this

ParamTag

.
The angle brackets delimiting a type parameter are not part of
its name.

**Returns:** the parameter name.

- parameterComment

```java
String
parameterComment()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the parameter comment
associated with this

ParamTag

.

**Returns:** the parameter comment.

- isTypeParameter

```java
boolean isTypeParameter()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this

ParamTag

corresponds to a type
parameter. Return false if it corresponds to an ordinary parameter
of a method or constructor.

**Returns:** true if this

ParamTag

corresponds to a type
parameter.
**Since:** 1.5

---

#### Method Detail

parameterName

```java
String
parameterName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the name of the parameter or type parameter
associated with this

ParamTag

.
The angle brackets delimiting a type parameter are not part of
its name.

**Returns:** the parameter name.

---

#### parameterName

String

parameterName()

Return the name of the parameter or type parameter
associated with this

ParamTag

.
The angle brackets delimiting a type parameter are not part of
its name.

parameterComment

```java
String
parameterComment()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the parameter comment
associated with this

ParamTag

.

**Returns:** the parameter comment.

---

#### parameterComment

String

parameterComment()

Return the parameter comment
associated with this

ParamTag

.

isTypeParameter

```java
boolean isTypeParameter()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this

ParamTag

corresponds to a type
parameter. Return false if it corresponds to an ordinary parameter
of a method or constructor.

**Returns:** true if this

ParamTag

corresponds to a type
parameter.
**Since:** 1.5

---

#### isTypeParameter

boolean isTypeParameter()

Return true if this

ParamTag

corresponds to a type
parameter. Return false if it corresponds to an ordinary parameter
of a method or constructor.

---

