# Class HashPrintServiceAttributeSet

**Source:** `java.desktop\javax\print\attribute\HashPrintServiceAttributeSet.html`

### Class Description

```java
public class
HashPrintServiceAttributeSet

extends
HashAttributeSet

implements
PrintServiceAttributeSet
,
Serializable
```

Class

HashPrintServiceAttributeSet

provides an attribute set which
inherits its implementation from class

HashAttributeSet

and enforces the semantic
restrictions of interface

PrintServiceAttributeSet

.

**All Implemented Interfaces:** Serializable

,

AttributeSet

,

PrintServiceAttributeSet

---

### Field Details

*No entries found.*

### Constructor Details

#### public HashPrintServiceAttributeSet()

Construct a new, empty hash print service attribute set.

---

#### public HashPrintServiceAttributeSet​(
PrintServiceAttribute
attribute)

Construct a new hash print service attribute set, initially populated
with the given value.

**Parameters:**
- attribute

- attribute value to add to the set

**Throws:**
- NullPointerException

- if

attribute

is

null

---

#### public HashPrintServiceAttributeSet​(
PrintServiceAttribute
[] attributes)

Construct a new print service attribute set, initially populated with the
values from the given array. The new attribute set is populated by adding
the elements of

attributes

array to the set in sequence, starting
at index 0. Thus, later array elements may replace earlier array elements
if the array contains duplicate attribute values or attribute categories.

**Parameters:**
- attributes

- array of attribute values to add to the set. If

null

, an empty attribute set is constructed.

**Throws:**
- NullPointerException

- if any element of

attributes

is

null

---

#### public HashPrintServiceAttributeSet​(
PrintServiceAttributeSet
attributes)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

PrintServiceAttribute

interface.

**Parameters:**
- attributes

- set of attribute values to initialise the set. If

null

, an empty attribute set is constructed.

**Throws:**
- ClassCastException

- if any element of

attributes

is not an
instance of

PrintServiceAttribute

---

### Method Details

*No entries found.*

### Additional Sections

#### Class HashPrintServiceAttributeSet

java.lang.Object

- javax.print.attribute.HashAttributeSet
- - javax.print.attribute.HashPrintServiceAttributeSet

javax.print.attribute.HashAttributeSet

- javax.print.attribute.HashPrintServiceAttributeSet

javax.print.attribute.HashPrintServiceAttributeSet

**All Implemented Interfaces:** Serializable

,

AttributeSet

,

PrintServiceAttributeSet

```java
public class
HashPrintServiceAttributeSet

extends
HashAttributeSet

implements
PrintServiceAttributeSet
,
Serializable
```

Class

HashPrintServiceAttributeSet

provides an attribute set which
inherits its implementation from class

HashAttributeSet

and enforces the semantic
restrictions of interface

PrintServiceAttributeSet

.

**See Also:** Serialized Form

public class

HashPrintServiceAttributeSet

extends

HashAttributeSet

implements

PrintServiceAttributeSet

,

Serializable

Class

HashPrintServiceAttributeSet

provides an attribute set which
inherits its implementation from class

HashAttributeSet

and enforces the semantic
restrictions of interface

PrintServiceAttributeSet

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

HashPrintServiceAttributeSet

()

Construct a new, empty hash print service attribute set.

HashPrintServiceAttributeSet

​(

PrintServiceAttribute

attribute)

Construct a new hash print service attribute set, initially populated
with the given value.

HashPrintServiceAttributeSet

​(

PrintServiceAttribute

[] attributes)

Construct a new print service attribute set, initially populated with the
values from the given array.

HashPrintServiceAttributeSet

​(

PrintServiceAttributeSet

attributes)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

PrintServiceAttribute

interface.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.print.attribute.

HashAttributeSet

add

,

addAll

,

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

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- Methods declared in interface javax.print.attribute.

PrintServiceAttributeSet

add

,

addAll

Constructor Summary

Constructors

Constructor

Description

HashPrintServiceAttributeSet

()

Construct a new, empty hash print service attribute set.

HashPrintServiceAttributeSet

​(

PrintServiceAttribute

attribute)

Construct a new hash print service attribute set, initially populated
with the given value.

HashPrintServiceAttributeSet

​(

PrintServiceAttribute

[] attributes)

Construct a new print service attribute set, initially populated with the
values from the given array.

HashPrintServiceAttributeSet

​(

PrintServiceAttributeSet

attributes)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

PrintServiceAttribute

interface.

---

#### Constructor Summary

Construct a new, empty hash print service attribute set.

Construct a new hash print service attribute set, initially populated
with the given value.

Construct a new print service attribute set, initially populated with the
values from the given array.

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

PrintServiceAttribute

interface.

Method Summary

- Methods declared in class javax.print.attribute.

HashAttributeSet

add

,

addAll

,

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

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- Methods declared in interface javax.print.attribute.

PrintServiceAttributeSet

add

,

addAll

---

#### Method Summary

Methods declared in class javax.print.attribute.

HashAttributeSet

add

,

addAll

,

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

#### Methods declared in class javax.print.attribute. HashAttributeSet

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Methods declared in interface javax.print.attribute.

PrintServiceAttributeSet

add

,

addAll

---

#### Methods declared in interface javax.print.attribute. PrintServiceAttributeSet

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- HashPrintServiceAttributeSet

```java
public HashPrintServiceAttributeSet()
```

Construct a new, empty hash print service attribute set.

- HashPrintServiceAttributeSet

```java
public HashPrintServiceAttributeSet​(
PrintServiceAttribute
attribute)
```

Construct a new hash print service attribute set, initially populated
with the given value.

**Parameters:** attribute

- attribute value to add to the set
**Throws:** NullPointerException

- if

attribute

is

null

- HashPrintServiceAttributeSet

```java
public HashPrintServiceAttributeSet​(
PrintServiceAttribute
[] attributes)
```

Construct a new print service attribute set, initially populated with the
values from the given array. The new attribute set is populated by adding
the elements of

attributes

array to the set in sequence, starting
at index 0. Thus, later array elements may replace earlier array elements
if the array contains duplicate attribute values or attribute categories.

**Parameters:** attributes

- array of attribute values to add to the set. If

null

, an empty attribute set is constructed.
**Throws:** NullPointerException

- if any element of

attributes

is

null

- HashPrintServiceAttributeSet

```java
public HashPrintServiceAttributeSet​(
PrintServiceAttributeSet
attributes)
```

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

PrintServiceAttribute

interface.

**Parameters:** attributes

- set of attribute values to initialise the set. If

null

, an empty attribute set is constructed.
**Throws:** ClassCastException

- if any element of

attributes

is not an
instance of

PrintServiceAttribute

Constructor Detail

- HashPrintServiceAttributeSet

```java
public HashPrintServiceAttributeSet()
```

Construct a new, empty hash print service attribute set.

- HashPrintServiceAttributeSet

```java
public HashPrintServiceAttributeSet​(
PrintServiceAttribute
attribute)
```

Construct a new hash print service attribute set, initially populated
with the given value.

**Parameters:** attribute

- attribute value to add to the set
**Throws:** NullPointerException

- if

attribute

is

null

- HashPrintServiceAttributeSet

```java
public HashPrintServiceAttributeSet​(
PrintServiceAttribute
[] attributes)
```

Construct a new print service attribute set, initially populated with the
values from the given array. The new attribute set is populated by adding
the elements of

attributes

array to the set in sequence, starting
at index 0. Thus, later array elements may replace earlier array elements
if the array contains duplicate attribute values or attribute categories.

**Parameters:** attributes

- array of attribute values to add to the set. If

null

, an empty attribute set is constructed.
**Throws:** NullPointerException

- if any element of

attributes

is

null

- HashPrintServiceAttributeSet

```java
public HashPrintServiceAttributeSet​(
PrintServiceAttributeSet
attributes)
```

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

PrintServiceAttribute

interface.

**Parameters:** attributes

- set of attribute values to initialise the set. If

null

, an empty attribute set is constructed.
**Throws:** ClassCastException

- if any element of

attributes

is not an
instance of

PrintServiceAttribute

---

#### Constructor Detail

HashPrintServiceAttributeSet

```java
public HashPrintServiceAttributeSet()
```

Construct a new, empty hash print service attribute set.

---

#### HashPrintServiceAttributeSet

public HashPrintServiceAttributeSet()

Construct a new, empty hash print service attribute set.

HashPrintServiceAttributeSet

```java
public HashPrintServiceAttributeSet​(
PrintServiceAttribute
attribute)
```

Construct a new hash print service attribute set, initially populated
with the given value.

**Parameters:** attribute

- attribute value to add to the set
**Throws:** NullPointerException

- if

attribute

is

null

---

#### HashPrintServiceAttributeSet

public HashPrintServiceAttributeSet​(

PrintServiceAttribute

attribute)

Construct a new hash print service attribute set, initially populated
with the given value.

HashPrintServiceAttributeSet

```java
public HashPrintServiceAttributeSet​(
PrintServiceAttribute
[] attributes)
```

Construct a new print service attribute set, initially populated with the
values from the given array. The new attribute set is populated by adding
the elements of

attributes

array to the set in sequence, starting
at index 0. Thus, later array elements may replace earlier array elements
if the array contains duplicate attribute values or attribute categories.

**Parameters:** attributes

- array of attribute values to add to the set. If

null

, an empty attribute set is constructed.
**Throws:** NullPointerException

- if any element of

attributes

is

null

---

#### HashPrintServiceAttributeSet

public HashPrintServiceAttributeSet​(

PrintServiceAttribute

[] attributes)

Construct a new print service attribute set, initially populated with the
values from the given array. The new attribute set is populated by adding
the elements of

attributes

array to the set in sequence, starting
at index 0. Thus, later array elements may replace earlier array elements
if the array contains duplicate attribute values or attribute categories.

HashPrintServiceAttributeSet

```java
public HashPrintServiceAttributeSet​(
PrintServiceAttributeSet
attributes)
```

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

PrintServiceAttribute

interface.

**Parameters:** attributes

- set of attribute values to initialise the set. If

null

, an empty attribute set is constructed.
**Throws:** ClassCastException

- if any element of

attributes

is not an
instance of

PrintServiceAttribute

---

#### HashPrintServiceAttributeSet

public HashPrintServiceAttributeSet​(

PrintServiceAttributeSet

attributes)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

PrintServiceAttribute

interface.

---

