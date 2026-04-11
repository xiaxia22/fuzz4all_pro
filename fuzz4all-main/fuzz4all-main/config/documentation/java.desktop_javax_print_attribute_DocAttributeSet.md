# Interface DocAttributeSet

**Source:** `java.desktop\javax\print\attribute\DocAttributeSet.html`

### Class Description

```java
public interface
DocAttributeSet

extends
AttributeSet
```

Interface

DocAttributeSet

specifies the interface for a set of doc
attributes, i.e. printing attributes that implement interface

DocAttribute

. In the Print Service API, the client uses
a

DocAttributeSet

to specify the characteristics of an individual doc
and the print job settings to be applied to an individual doc.

A

DocAttributeSet

is just an

AttributeSet

whose
constructors and mutating operations guarantee an additional invariant,
namely that all attribute values in the

DocAttributeSet

must be
instances of interface

DocAttribute

. The

add(Attribute)

, and

addAll(AttributeSet)

operations are respecified
below to guarantee this additional invariant.

**All Superinterfaces:** AttributeSet

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean add​(
Attribute
attribute)

Adds the specified attribute value to this attribute set if it is not
already present, first removing any existing value in the same attribute
category as the specified attribute value (optional operation).

**Specified by:**
- add

in interface

AttributeSet

**Parameters:**
- attribute

- attribute value to be added to this attribute set

**Returns:**
- true

if this attribute set changed as a result of the
call, i.e., the given attribute value was not already a member of
this attribute set

**Throws:**
- UnmodifiableSetException

- if this attribute set does not support
the

add()

operation
- ClassCastException

- if the

attribute

is not an instance of
interface

DocAttribute
- NullPointerException

- if the

attribute

is

null

---

#### boolean addAll​(
AttributeSet
attributes)

Adds all of the elements in the specified set to this attribute. The
outcome is the same as if the

add(Attribute)

operation had been applied to this attribute set successively with each
element from the specified set. If none of the categories in the
specified set are the same as any categories in this attribute set, the

addAll()

operation effectively modifies this attribute set so
that its value is the

union

of the two sets.

The behavior of the

addAll()

operation is unspecified if the
specified set is modified while the operation is in progress.

If the

addAll()

operation throws an exception, the effect on this
attribute set's state is implementation dependent; elements from the
specified set before the point of the exception may or may not have been
added to this attribute set.

**Specified by:**
- addAll

in interface

AttributeSet

**Parameters:**
- attributes

- whose elements are to be added to this attribute set

**Returns:**
- true

if this attribute set changed as a result of the
call

**Throws:**
- UnmodifiableSetException

- if this attribute set does not support
the

addAll()

method
- ClassCastException

- if some element in the specified set is not an
instance of interface

DocAttribute
- NullPointerException

- if the specified set is

null

**See Also:**
- add(Attribute)

---

### Additional Sections

#### Interface DocAttributeSet

**All Superinterfaces:** AttributeSet

**All Known Implementing Classes:** HashDocAttributeSet

```java
public interface
DocAttributeSet

extends
AttributeSet
```

Interface

DocAttributeSet

specifies the interface for a set of doc
attributes, i.e. printing attributes that implement interface

DocAttribute

. In the Print Service API, the client uses
a

DocAttributeSet

to specify the characteristics of an individual doc
and the print job settings to be applied to an individual doc.

A

DocAttributeSet

is just an

AttributeSet

whose
constructors and mutating operations guarantee an additional invariant,
namely that all attribute values in the

DocAttributeSet

must be
instances of interface

DocAttribute

. The

add(Attribute)

, and

addAll(AttributeSet)

operations are respecified
below to guarantee this additional invariant.

public interface

DocAttributeSet

extends

AttributeSet

Interface

DocAttributeSet

specifies the interface for a set of doc
attributes, i.e. printing attributes that implement interface

DocAttribute

. In the Print Service API, the client uses
a

DocAttributeSet

to specify the characteristics of an individual doc
and the print job settings to be applied to an individual doc.

A

DocAttributeSet

is just an

AttributeSet

whose
constructors and mutating operations guarantee an additional invariant,
namely that all attribute values in the

DocAttributeSet

must be
instances of interface

DocAttribute

. The

add(Attribute)

, and

addAll(AttributeSet)

operations are respecified
below to guarantee this additional invariant.

A

DocAttributeSet

is just an

AttributeSet

whose
constructors and mutating operations guarantee an additional invariant,
namely that all attribute values in the

DocAttributeSet

must be
instances of interface

DocAttribute

. The

add(Attribute)

, and

addAll(AttributeSet)

operations are respecified
below to guarantee this additional invariant.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

add

​(

Attribute

attribute)

Adds the specified attribute value to this attribute set if it is not
already present, first removing any existing value in the same attribute
category as the specified attribute value (optional operation).

boolean

addAll

​(

AttributeSet

attributes)

Adds all of the elements in the specified set to this attribute.

- Methods declared in interface javax.print.attribute.

AttributeSet

clear

,

containsKey

,

containsValue

,

equals

,

get

,

hashCode

,

isEmpty

,

remove

,

remove

,

size

,

toArray

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

add

​(

Attribute

attribute)

Adds the specified attribute value to this attribute set if it is not
already present, first removing any existing value in the same attribute
category as the specified attribute value (optional operation).

boolean

addAll

​(

AttributeSet

attributes)

Adds all of the elements in the specified set to this attribute.

- Methods declared in interface javax.print.attribute.

AttributeSet

clear

,

containsKey

,

containsValue

,

equals

,

get

,

hashCode

,

isEmpty

,

remove

,

remove

,

size

,

toArray

---

#### Method Summary

Adds the specified attribute value to this attribute set if it is not
already present, first removing any existing value in the same attribute
category as the specified attribute value (optional operation).

Adds all of the elements in the specified set to this attribute.

Methods declared in interface javax.print.attribute.

AttributeSet

clear

,

containsKey

,

containsValue

,

equals

,

get

,

hashCode

,

isEmpty

,

remove

,

remove

,

size

,

toArray

---

#### Methods declared in interface javax.print.attribute. AttributeSet

============ METHOD DETAIL ==========

- Method Detail

- add

```java
boolean add​(
Attribute
attribute)
```

Adds the specified attribute value to this attribute set if it is not
already present, first removing any existing value in the same attribute
category as the specified attribute value (optional operation).

**Specified by:** add

in interface

AttributeSet
**Parameters:** attribute

- attribute value to be added to this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value was not already a member of
this attribute set
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

add()

operation
**Throws:** ClassCastException

- if the

attribute

is not an instance of
interface

DocAttribute
**Throws:** NullPointerException

- if the

attribute

is

null

- addAll

```java
boolean addAll​(
AttributeSet
attributes)
```

Adds all of the elements in the specified set to this attribute. The
outcome is the same as if the

add(Attribute)

operation had been applied to this attribute set successively with each
element from the specified set. If none of the categories in the
specified set are the same as any categories in this attribute set, the

addAll()

operation effectively modifies this attribute set so
that its value is the

union

of the two sets.

The behavior of the

addAll()

operation is unspecified if the
specified set is modified while the operation is in progress.

If the

addAll()

operation throws an exception, the effect on this
attribute set's state is implementation dependent; elements from the
specified set before the point of the exception may or may not have been
added to this attribute set.

**Specified by:** addAll

in interface

AttributeSet
**Parameters:** attributes

- whose elements are to be added to this attribute set
**Returns:** true

if this attribute set changed as a result of the
call
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

addAll()

method
**Throws:** ClassCastException

- if some element in the specified set is not an
instance of interface

DocAttribute
**Throws:** NullPointerException

- if the specified set is

null
**See Also:** add(Attribute)

Method Detail

- add

```java
boolean add​(
Attribute
attribute)
```

Adds the specified attribute value to this attribute set if it is not
already present, first removing any existing value in the same attribute
category as the specified attribute value (optional operation).

**Specified by:** add

in interface

AttributeSet
**Parameters:** attribute

- attribute value to be added to this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value was not already a member of
this attribute set
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

add()

operation
**Throws:** ClassCastException

- if the

attribute

is not an instance of
interface

DocAttribute
**Throws:** NullPointerException

- if the

attribute

is

null

- addAll

```java
boolean addAll​(
AttributeSet
attributes)
```

Adds all of the elements in the specified set to this attribute. The
outcome is the same as if the

add(Attribute)

operation had been applied to this attribute set successively with each
element from the specified set. If none of the categories in the
specified set are the same as any categories in this attribute set, the

addAll()

operation effectively modifies this attribute set so
that its value is the

union

of the two sets.

The behavior of the

addAll()

operation is unspecified if the
specified set is modified while the operation is in progress.

If the

addAll()

operation throws an exception, the effect on this
attribute set's state is implementation dependent; elements from the
specified set before the point of the exception may or may not have been
added to this attribute set.

**Specified by:** addAll

in interface

AttributeSet
**Parameters:** attributes

- whose elements are to be added to this attribute set
**Returns:** true

if this attribute set changed as a result of the
call
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

addAll()

method
**Throws:** ClassCastException

- if some element in the specified set is not an
instance of interface

DocAttribute
**Throws:** NullPointerException

- if the specified set is

null
**See Also:** add(Attribute)

---

#### Method Detail

add

```java
boolean add​(
Attribute
attribute)
```

Adds the specified attribute value to this attribute set if it is not
already present, first removing any existing value in the same attribute
category as the specified attribute value (optional operation).

**Specified by:** add

in interface

AttributeSet
**Parameters:** attribute

- attribute value to be added to this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value was not already a member of
this attribute set
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

add()

operation
**Throws:** ClassCastException

- if the

attribute

is not an instance of
interface

DocAttribute
**Throws:** NullPointerException

- if the

attribute

is

null

---

#### add

boolean add​(

Attribute

attribute)

Adds the specified attribute value to this attribute set if it is not
already present, first removing any existing value in the same attribute
category as the specified attribute value (optional operation).

addAll

```java
boolean addAll​(
AttributeSet
attributes)
```

Adds all of the elements in the specified set to this attribute. The
outcome is the same as if the

add(Attribute)

operation had been applied to this attribute set successively with each
element from the specified set. If none of the categories in the
specified set are the same as any categories in this attribute set, the

addAll()

operation effectively modifies this attribute set so
that its value is the

union

of the two sets.

The behavior of the

addAll()

operation is unspecified if the
specified set is modified while the operation is in progress.

If the

addAll()

operation throws an exception, the effect on this
attribute set's state is implementation dependent; elements from the
specified set before the point of the exception may or may not have been
added to this attribute set.

**Specified by:** addAll

in interface

AttributeSet
**Parameters:** attributes

- whose elements are to be added to this attribute set
**Returns:** true

if this attribute set changed as a result of the
call
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

addAll()

method
**Throws:** ClassCastException

- if some element in the specified set is not an
instance of interface

DocAttribute
**Throws:** NullPointerException

- if the specified set is

null
**See Also:** add(Attribute)

---

#### addAll

boolean addAll​(

AttributeSet

attributes)

Adds all of the elements in the specified set to this attribute. The
outcome is the same as if the

add(Attribute)

operation had been applied to this attribute set successively with each
element from the specified set. If none of the categories in the
specified set are the same as any categories in this attribute set, the

addAll()

operation effectively modifies this attribute set so
that its value is the

union

of the two sets.

The behavior of the

addAll()

operation is unspecified if the
specified set is modified while the operation is in progress.

If the

addAll()

operation throws an exception, the effect on this
attribute set's state is implementation dependent; elements from the
specified set before the point of the exception may or may not have been
added to this attribute set.

The behavior of the

addAll()

operation is unspecified if the
specified set is modified while the operation is in progress.

If the

addAll()

operation throws an exception, the effect on this
attribute set's state is implementation dependent; elements from the
specified set before the point of the exception may or may not have been
added to this attribute set.

If the

addAll()

operation throws an exception, the effect on this
attribute set's state is implementation dependent; elements from the
specified set before the point of the exception may or may not have been
added to this attribute set.

---

