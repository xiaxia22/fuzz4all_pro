# Interface Name

**Source:** `java.compiler\javax\lang\model\element\Name.html`

### Class Description

```java
public interface
Name

extends
CharSequence
```

An immutable sequence of characters. When created by the same
implementation, objects implementing this interface must obey the
general

equals contract

when compared
with each other. Therefore,

Name

objects from the same
implementation are usable in collections while

Name

s from
different implementations may not work properly in collections.

An empty

Name

has a length of zero.

In the context of

annotation
processing

, the guarantees for "the same" implementation must
include contexts where the

API mediated

side effects of

processors

could be visible
to each other, including successive annotation processing

rounds

.

**All Superinterfaces:** CharSequence

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean equals​(
Object
obj)

Returns

true

if the argument represents the same
name as

this

, and

false

otherwise.

Note that the identity of a

Name

is a function both
of its content in terms of a sequence of characters as well as
the implementation which created it.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to be compared with this element

**Returns:**
- true

if the specified object represents the same
name as this

**See Also:**
- Element.equals(java.lang.Object)

---

#### int hashCode()

Obeys the general contract of

Object.hashCode

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- equals(java.lang.Object)

---

#### boolean contentEquals​(
CharSequence
cs)

Compares this name to the specified

CharSequence

. The result
is

true

if and only if this name represents the same sequence
of

char

values as the specified sequence.

**Parameters:**
- cs

- The sequence to compare this name against

**Returns:**
- true

if this name represents the same sequence
of

char

values as the specified sequence,

false

otherwise

**See Also:**
- String.contentEquals(CharSequence)

---

### Additional Sections

#### Interface Name

**All Superinterfaces:** CharSequence

```java
public interface
Name

extends
CharSequence
```

An immutable sequence of characters. When created by the same
implementation, objects implementing this interface must obey the
general

equals contract

when compared
with each other. Therefore,

Name

objects from the same
implementation are usable in collections while

Name

s from
different implementations may not work properly in collections.

An empty

Name

has a length of zero.

In the context of

annotation
processing

, the guarantees for "the same" implementation must
include contexts where the

API mediated

side effects of

processors

could be visible
to each other, including successive annotation processing

rounds

.

**Since:** 1.6
**See Also:** Elements.getName(java.lang.CharSequence)

public interface

Name

extends

CharSequence

An immutable sequence of characters. When created by the same
implementation, objects implementing this interface must obey the
general

equals contract

when compared
with each other. Therefore,

Name

objects from the same
implementation are usable in collections while

Name

s from
different implementations may not work properly in collections.

An empty

Name

has a length of zero.

In the context of

annotation
processing

, the guarantees for "the same" implementation must
include contexts where the

API mediated

side effects of

processors

could be visible
to each other, including successive annotation processing

rounds

.

An empty

Name

has a length of zero.

In the context of

annotation
processing

, the guarantees for "the same" implementation must
include contexts where the

API mediated

side effects of

processors

could be visible
to each other, including successive annotation processing

rounds

.

In the context of

annotation
processing

, the guarantees for "the same" implementation must
include contexts where the

API mediated

side effects of

processors

could be visible
to each other, including successive annotation processing

rounds

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

contentEquals

​(

CharSequence

cs)

Compares this name to the specified

CharSequence

.

boolean

equals

​(

Object

obj)

Returns

true

if the argument represents the same
name as

this

, and

false

otherwise.

int

hashCode

()

Obeys the general contract of

Object.hashCode

.

- Methods declared in interface java.lang.

CharSequence

charAt

,

chars

,

codePoints

,

length

,

subSequence

,

toString

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

contentEquals

​(

CharSequence

cs)

Compares this name to the specified

CharSequence

.

boolean

equals

​(

Object

obj)

Returns

true

if the argument represents the same
name as

this

, and

false

otherwise.

int

hashCode

()

Obeys the general contract of

Object.hashCode

.

- Methods declared in interface java.lang.

CharSequence

charAt

,

chars

,

codePoints

,

length

,

subSequence

,

toString

---

#### Method Summary

Compares this name to the specified

CharSequence

.

Returns

true

if the argument represents the same
name as

this

, and

false

otherwise.

Obeys the general contract of

Object.hashCode

.

Methods declared in interface java.lang.

CharSequence

charAt

,

chars

,

codePoints

,

length

,

subSequence

,

toString

---

#### Methods declared in interface java.lang. CharSequence

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
boolean equals​(
Object
obj)
```

Returns

true

if the argument represents the same
name as

this

, and

false

otherwise.

Note that the identity of a

Name

is a function both
of its content in terms of a sequence of characters as well as
the implementation which created it.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared with this element
**Returns:** true

if the specified object represents the same
name as this
**See Also:** Element.equals(java.lang.Object)

- hashCode

```java
int hashCode()
```

Obeys the general contract of

Object.hashCode

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** equals(java.lang.Object)

- contentEquals

```java
boolean contentEquals​(
CharSequence
cs)
```

Compares this name to the specified

CharSequence

. The result
is

true

if and only if this name represents the same sequence
of

char

values as the specified sequence.

**Parameters:** cs

- The sequence to compare this name against
**Returns:** true

if this name represents the same sequence
of

char

values as the specified sequence,

false

otherwise
**See Also:** String.contentEquals(CharSequence)

Method Detail

- equals

```java
boolean equals​(
Object
obj)
```

Returns

true

if the argument represents the same
name as

this

, and

false

otherwise.

Note that the identity of a

Name

is a function both
of its content in terms of a sequence of characters as well as
the implementation which created it.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared with this element
**Returns:** true

if the specified object represents the same
name as this
**See Also:** Element.equals(java.lang.Object)

- hashCode

```java
int hashCode()
```

Obeys the general contract of

Object.hashCode

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** equals(java.lang.Object)

- contentEquals

```java
boolean contentEquals​(
CharSequence
cs)
```

Compares this name to the specified

CharSequence

. The result
is

true

if and only if this name represents the same sequence
of

char

values as the specified sequence.

**Parameters:** cs

- The sequence to compare this name against
**Returns:** true

if this name represents the same sequence
of

char

values as the specified sequence,

false

otherwise
**See Also:** String.contentEquals(CharSequence)

---

#### Method Detail

equals

```java
boolean equals​(
Object
obj)
```

Returns

true

if the argument represents the same
name as

this

, and

false

otherwise.

Note that the identity of a

Name

is a function both
of its content in terms of a sequence of characters as well as
the implementation which created it.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared with this element
**Returns:** true

if the specified object represents the same
name as this
**See Also:** Element.equals(java.lang.Object)

---

#### equals

boolean equals​(

Object

obj)

Returns

true

if the argument represents the same
name as

this

, and

false

otherwise.

Note that the identity of a

Name

is a function both
of its content in terms of a sequence of characters as well as
the implementation which created it.

Note that the identity of a

Name

is a function both
of its content in terms of a sequence of characters as well as
the implementation which created it.

hashCode

```java
int hashCode()
```

Obeys the general contract of

Object.hashCode

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** equals(java.lang.Object)

---

#### hashCode

int hashCode()

Obeys the general contract of

Object.hashCode

.

contentEquals

```java
boolean contentEquals​(
CharSequence
cs)
```

Compares this name to the specified

CharSequence

. The result
is

true

if and only if this name represents the same sequence
of

char

values as the specified sequence.

**Parameters:** cs

- The sequence to compare this name against
**Returns:** true

if this name represents the same sequence
of

char

values as the specified sequence,

false

otherwise
**See Also:** String.contentEquals(CharSequence)

---

#### contentEquals

boolean contentEquals​(

CharSequence

cs)

Compares this name to the specified

CharSequence

. The result
is

true

if and only if this name represents the same sequence
of

char

values as the specified sequence.

---

