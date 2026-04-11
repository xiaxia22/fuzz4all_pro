# Interface FieldDoc

**Source:** `jdk.javadoc\com\sun\javadoc\FieldDoc.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
FieldDoc

extends
MemberDoc
```

Represents a field in a java class.

**All Superinterfaces:** Comparable

<

Object

>

,

Doc

,

MemberDoc

,

ProgramElementDoc

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Type
type()

Get type of this field.

**Returns:**
- the type of this field.

---

#### boolean isTransient()

Return true if this field is transient

**Returns:**
- true if this field is transient

---

#### boolean isVolatile()

Return true if this field is volatile

**Returns:**
- true if this field is volatile

---

#### SerialFieldTag
[] serialFieldTags()

Return the serialField tags in this FieldDoc item.

**Returns:**
- an array of

SerialFieldTag

objects containing
all

@serialField

tags.

---

#### Object
constantValue()

Get the value of a constant field.

**Returns:**
- the value of a constant field. The value is
automatically wrapped in an object if it has a primitive type.
If the field is not constant, returns null.

---

#### String
constantValueExpression()

Get the value of a constant field.

**Returns:**
- the text of a Java language expression whose value
is the value of the constant. The expression uses no identifiers
other than primitive literals. If the field is
not constant, returns null.

---

### Additional Sections

#### Interface FieldDoc

**All Superinterfaces:** Comparable

<

Object

>

,

Doc

,

MemberDoc

,

ProgramElementDoc

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
FieldDoc

extends
MemberDoc
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Represents a field in a java class.

**Since:** 1.2
**See Also:** MemberDoc

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

FieldDoc

extends

MemberDoc

Represents a field in a java class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

Object

constantValue

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the value of a constant field.

String

constantValueExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the value of a constant field.

boolean

isTransient

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this field is transient

boolean

isVolatile

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this field is volatile

SerialFieldTag

[]

serialFieldTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the serialField tags in this FieldDoc item.

Type

type

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get type of this field.

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

MemberDoc

isSynthetic

- Methods declared in interface com.sun.javadoc.

ProgramElementDoc

annotations

,

containingClass

,

containingPackage

,

isFinal

,

isPackagePrivate

,

isPrivate

,

isProtected

,

isPublic

,

isStatic

,

modifiers

,

modifierSpecifier

,

qualifiedName

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

Object

constantValue

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the value of a constant field.

String

constantValueExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the value of a constant field.

boolean

isTransient

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this field is transient

boolean

isVolatile

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this field is volatile

SerialFieldTag

[]

serialFieldTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the serialField tags in this FieldDoc item.

Type

type

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get type of this field.

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

MemberDoc

isSynthetic

- Methods declared in interface com.sun.javadoc.

ProgramElementDoc

annotations

,

containingClass

,

containingPackage

,

isFinal

,

isPackagePrivate

,

isPrivate

,

isProtected

,

isPublic

,

isStatic

,

modifiers

,

modifierSpecifier

,

qualifiedName

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Get the value of a constant field.

Return true if this field is transient

Return true if this field is volatile

Return the serialField tags in this FieldDoc item.

Get type of this field.

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

MemberDoc

isSynthetic

---

#### Methods declared in interface com.sun.javadoc. MemberDoc

Methods declared in interface com.sun.javadoc.

ProgramElementDoc

annotations

,

containingClass

,

containingPackage

,

isFinal

,

isPackagePrivate

,

isPrivate

,

isProtected

,

isPublic

,

isStatic

,

modifiers

,

modifierSpecifier

,

qualifiedName

---

#### Methods declared in interface com.sun.javadoc. ProgramElementDoc

============ METHOD DETAIL ==========

- Method Detail

- type

```java
Type
type()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get type of this field.

**Returns:** the type of this field.

- isTransient

```java
boolean isTransient()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this field is transient

**Returns:** true if this field is transient

- isVolatile

```java
boolean isVolatile()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this field is volatile

**Returns:** true if this field is volatile

- serialFieldTags

```java
SerialFieldTag
[] serialFieldTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the serialField tags in this FieldDoc item.

**Returns:** an array of

SerialFieldTag

objects containing
all

@serialField

tags.

- constantValue

```java
Object
constantValue()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the value of a constant field.

**Returns:** the value of a constant field. The value is
automatically wrapped in an object if it has a primitive type.
If the field is not constant, returns null.

- constantValueExpression

```java
String
constantValueExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the value of a constant field.

**Returns:** the text of a Java language expression whose value
is the value of the constant. The expression uses no identifiers
other than primitive literals. If the field is
not constant, returns null.

Method Detail

- type

```java
Type
type()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get type of this field.

**Returns:** the type of this field.

- isTransient

```java
boolean isTransient()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this field is transient

**Returns:** true if this field is transient

- isVolatile

```java
boolean isVolatile()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this field is volatile

**Returns:** true if this field is volatile

- serialFieldTags

```java
SerialFieldTag
[] serialFieldTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the serialField tags in this FieldDoc item.

**Returns:** an array of

SerialFieldTag

objects containing
all

@serialField

tags.

- constantValue

```java
Object
constantValue()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the value of a constant field.

**Returns:** the value of a constant field. The value is
automatically wrapped in an object if it has a primitive type.
If the field is not constant, returns null.

- constantValueExpression

```java
String
constantValueExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the value of a constant field.

**Returns:** the text of a Java language expression whose value
is the value of the constant. The expression uses no identifiers
other than primitive literals. If the field is
not constant, returns null.

---

#### Method Detail

type

```java
Type
type()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get type of this field.

**Returns:** the type of this field.

---

#### type

Type

type()

Get type of this field.

isTransient

```java
boolean isTransient()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this field is transient

**Returns:** true if this field is transient

---

#### isTransient

boolean isTransient()

Return true if this field is transient

isVolatile

```java
boolean isVolatile()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this field is volatile

**Returns:** true if this field is volatile

---

#### isVolatile

boolean isVolatile()

Return true if this field is volatile

serialFieldTags

```java
SerialFieldTag
[] serialFieldTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the serialField tags in this FieldDoc item.

**Returns:** an array of

SerialFieldTag

objects containing
all

@serialField

tags.

---

#### serialFieldTags

SerialFieldTag

[] serialFieldTags()

Return the serialField tags in this FieldDoc item.

constantValue

```java
Object
constantValue()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the value of a constant field.

**Returns:** the value of a constant field. The value is
automatically wrapped in an object if it has a primitive type.
If the field is not constant, returns null.

---

#### constantValue

Object

constantValue()

Get the value of a constant field.

constantValueExpression

```java
String
constantValueExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the value of a constant field.

**Returns:** the text of a Java language expression whose value
is the value of the constant. The expression uses no identifiers
other than primitive literals. If the field is
not constant, returns null.

---

#### constantValueExpression

String

constantValueExpression()

Get the value of a constant field.

---

