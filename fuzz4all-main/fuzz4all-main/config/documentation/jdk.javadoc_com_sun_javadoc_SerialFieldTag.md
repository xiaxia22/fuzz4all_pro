# Interface SerialFieldTag

**Source:** `jdk.javadoc\com\sun\javadoc\SerialFieldTag.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
SerialFieldTag

extends
Tag
,
Comparable
<
Object
>
```

Documents a Serializable field defined by an ObjectStreamField.

```java
The class parses and stores the three serialField tag parameters:

- field name
- field type name
(fully-qualified or visible from the current import context)
- description of the valid values for the field
```

This tag is only allowed in the javadoc for the special member
serialPersistentFields.

**All Superinterfaces:** Comparable

<

Object

>

,

Tag

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
fieldName()

Return the serializable field name.

**Returns:**
- the serializable field name.

---

#### String
fieldType()

Return the field type string.

**Returns:**
- the field type string.

---

#### ClassDoc
fieldTypeDoc()

Return the ClassDoc for field type.

**Returns:**
- null if no ClassDoc for field type is visible from
containingClass context.

---

#### String
description()

Return the field comment. If there is no serialField comment, return
javadoc comment of corresponding FieldDoc.

**Returns:**
- the field comment. If there is no serialField comment, return
javadoc comment of corresponding FieldDoc.

---

#### int compareTo​(
Object
obj)

Compares this Object with the specified Object for order. Returns a
negative integer, zero, or a positive integer as this Object is less
than, equal to, or greater than the given Object.

Included to make SerialFieldTag items java.lang.Comparable.

**Specified by:**
- compareTo

in interface

Comparable

<

Object

>

**Parameters:**
- obj

- the

Object

to be compared.

**Returns:**
- a negative integer, zero, or a positive integer as this Object
is less than, equal to, or greater than the given Object.

**Throws:**
- ClassCastException

- the specified Object's type prevents it
from being compared to this Object.

**Since:**
- 1.2

---

### Additional Sections

#### Interface SerialFieldTag

**All Superinterfaces:** Comparable

<

Object

>

,

Tag

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
SerialFieldTag

extends
Tag
,
Comparable
<
Object
>
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Documents a Serializable field defined by an ObjectStreamField.

```java
The class parses and stores the three serialField tag parameters:

- field name
- field type name
(fully-qualified or visible from the current import context)
- description of the valid values for the field
```

This tag is only allowed in the javadoc for the special member
serialPersistentFields.

**See Also:** ObjectStreamField

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

SerialFieldTag

extends

Tag

,

Comparable

<

Object

>

Documents a Serializable field defined by an ObjectStreamField.

```java
The class parses and stores the three serialField tag parameters:

- field name
- field type name
(fully-qualified or visible from the current import context)
- description of the valid values for the field
```

This tag is only allowed in the javadoc for the special member
serialPersistentFields.

The class parses and stores the three serialField tag parameters:

- field name
- field type name
(fully-qualified or visible from the current import context)
- description of the valid values for the field

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

int

compareTo

​(

Object

obj)

Deprecated, for removal: This API element is subject to removal in a future version.

Compares this Object with the specified Object for order.

String

description

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the field comment.

String

fieldName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the serializable field name.

String

fieldType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the field type string.

ClassDoc

fieldTypeDoc

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the ClassDoc for field type.

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

int

compareTo

​(

Object

obj)

Deprecated, for removal: This API element is subject to removal in a future version.

Compares this Object with the specified Object for order.

String

description

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the field comment.

String

fieldName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the serializable field name.

String

fieldType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the field type string.

ClassDoc

fieldTypeDoc

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the ClassDoc for field type.

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

Compares this Object with the specified Object for order.

Return the field comment.

Return the serializable field name.

Return the field type string.

Return the ClassDoc for field type.

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

- fieldName

```java
String
fieldName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the serializable field name.

**Returns:** the serializable field name.

- fieldType

```java
String
fieldType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the field type string.

**Returns:** the field type string.

- fieldTypeDoc

```java
ClassDoc
fieldTypeDoc()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the ClassDoc for field type.

**Returns:** null if no ClassDoc for field type is visible from
containingClass context.

- description

```java
String
description()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the field comment. If there is no serialField comment, return
javadoc comment of corresponding FieldDoc.

**Returns:** the field comment. If there is no serialField comment, return
javadoc comment of corresponding FieldDoc.

- compareTo

```java
int compareTo​(
Object
obj)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Compares this Object with the specified Object for order. Returns a
negative integer, zero, or a positive integer as this Object is less
than, equal to, or greater than the given Object.

Included to make SerialFieldTag items java.lang.Comparable.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Parameters:** obj

- the

Object

to be compared.
**Returns:** a negative integer, zero, or a positive integer as this Object
is less than, equal to, or greater than the given Object.
**Throws:** ClassCastException

- the specified Object's type prevents it
from being compared to this Object.
**Since:** 1.2

Method Detail

- fieldName

```java
String
fieldName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the serializable field name.

**Returns:** the serializable field name.

- fieldType

```java
String
fieldType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the field type string.

**Returns:** the field type string.

- fieldTypeDoc

```java
ClassDoc
fieldTypeDoc()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the ClassDoc for field type.

**Returns:** null if no ClassDoc for field type is visible from
containingClass context.

- description

```java
String
description()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the field comment. If there is no serialField comment, return
javadoc comment of corresponding FieldDoc.

**Returns:** the field comment. If there is no serialField comment, return
javadoc comment of corresponding FieldDoc.

- compareTo

```java
int compareTo​(
Object
obj)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Compares this Object with the specified Object for order. Returns a
negative integer, zero, or a positive integer as this Object is less
than, equal to, or greater than the given Object.

Included to make SerialFieldTag items java.lang.Comparable.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Parameters:** obj

- the

Object

to be compared.
**Returns:** a negative integer, zero, or a positive integer as this Object
is less than, equal to, or greater than the given Object.
**Throws:** ClassCastException

- the specified Object's type prevents it
from being compared to this Object.
**Since:** 1.2

---

#### Method Detail

fieldName

```java
String
fieldName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the serializable field name.

**Returns:** the serializable field name.

---

#### fieldName

String

fieldName()

Return the serializable field name.

fieldType

```java
String
fieldType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the field type string.

**Returns:** the field type string.

---

#### fieldType

String

fieldType()

Return the field type string.

fieldTypeDoc

```java
ClassDoc
fieldTypeDoc()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the ClassDoc for field type.

**Returns:** null if no ClassDoc for field type is visible from
containingClass context.

---

#### fieldTypeDoc

ClassDoc

fieldTypeDoc()

Return the ClassDoc for field type.

description

```java
String
description()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the field comment. If there is no serialField comment, return
javadoc comment of corresponding FieldDoc.

**Returns:** the field comment. If there is no serialField comment, return
javadoc comment of corresponding FieldDoc.

---

#### description

String

description()

Return the field comment. If there is no serialField comment, return
javadoc comment of corresponding FieldDoc.

compareTo

```java
int compareTo​(
Object
obj)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Compares this Object with the specified Object for order. Returns a
negative integer, zero, or a positive integer as this Object is less
than, equal to, or greater than the given Object.

Included to make SerialFieldTag items java.lang.Comparable.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Parameters:** obj

- the

Object

to be compared.
**Returns:** a negative integer, zero, or a positive integer as this Object
is less than, equal to, or greater than the given Object.
**Throws:** ClassCastException

- the specified Object's type prevents it
from being compared to this Object.
**Since:** 1.2

---

#### compareTo

int compareTo​(

Object

obj)

Compares this Object with the specified Object for order. Returns a
negative integer, zero, or a positive integer as this Object is less
than, equal to, or greater than the given Object.

Included to make SerialFieldTag items java.lang.Comparable.

Included to make SerialFieldTag items java.lang.Comparable.

---

