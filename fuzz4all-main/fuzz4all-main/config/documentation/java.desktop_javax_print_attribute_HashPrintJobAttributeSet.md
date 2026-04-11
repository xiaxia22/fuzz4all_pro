# Class HashPrintJobAttributeSet

**Source:** `java.desktop\javax\print\attribute\HashPrintJobAttributeSet.html`

### Class Description

```java
public class
HashPrintJobAttributeSet

extends
HashAttributeSet

implements
PrintJobAttributeSet
,
Serializable
```

Class

HashPrintJobAttributeSet

provides an attribute set which
inherits its implementation from class

HashAttributeSet

and enforces the semantic
restrictions of interface

PrintJobAttributeSet

.

**All Implemented Interfaces:** Serializable

,

AttributeSet

,

PrintJobAttributeSet

---

### Field Details

*No entries found.*

### Constructor Details

#### public HashPrintJobAttributeSet()

Construct a new, empty hash print job attribute set.

---

#### public HashPrintJobAttributeSet​(
PrintJobAttribute
attribute)

Construct a new hash print job attribute set, initially populated with
the given value.

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

#### public HashPrintJobAttributeSet​(
PrintJobAttribute
[] attributes)

Construct a new hash print job attribute set, initially populated with
the values from the given array. The new attribute set is populated by
adding the elements of

attributes

array to the set in sequence,
starting at index 0. Thus, later array elements may replace earlier array
elements if the array contains duplicate attribute values or attribute
categories.

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

#### public HashPrintJobAttributeSet​(
PrintJobAttributeSet
attributes)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

PrintJobAttribute

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

PrintJobAttribute

---

### Method Details

*No entries found.*

### Additional Sections

#### Class HashPrintJobAttributeSet

java.lang.Object

- javax.print.attribute.HashAttributeSet
- - javax.print.attribute.HashPrintJobAttributeSet

javax.print.attribute.HashAttributeSet

- javax.print.attribute.HashPrintJobAttributeSet

javax.print.attribute.HashPrintJobAttributeSet

**All Implemented Interfaces:** Serializable

,

AttributeSet

,

PrintJobAttributeSet

```java
public class
HashPrintJobAttributeSet

extends
HashAttributeSet

implements
PrintJobAttributeSet
,
Serializable
```

Class

HashPrintJobAttributeSet

provides an attribute set which
inherits its implementation from class

HashAttributeSet

and enforces the semantic
restrictions of interface

PrintJobAttributeSet

.

**See Also:** Serialized Form

public class

HashPrintJobAttributeSet

extends

HashAttributeSet

implements

PrintJobAttributeSet

,

Serializable

Class

HashPrintJobAttributeSet

provides an attribute set which
inherits its implementation from class

HashAttributeSet

and enforces the semantic
restrictions of interface

PrintJobAttributeSet

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

HashPrintJobAttributeSet

()

Construct a new, empty hash print job attribute set.

HashPrintJobAttributeSet

​(

PrintJobAttribute

attribute)

Construct a new hash print job attribute set, initially populated with
the given value.

HashPrintJobAttributeSet

​(

PrintJobAttribute

[] attributes)

Construct a new hash print job attribute set, initially populated with
the values from the given array.

HashPrintJobAttributeSet

​(

PrintJobAttributeSet

attributes)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

PrintJobAttribute

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

PrintJobAttributeSet

add

,

addAll

Constructor Summary

Constructors

Constructor

Description

HashPrintJobAttributeSet

()

Construct a new, empty hash print job attribute set.

HashPrintJobAttributeSet

​(

PrintJobAttribute

attribute)

Construct a new hash print job attribute set, initially populated with
the given value.

HashPrintJobAttributeSet

​(

PrintJobAttribute

[] attributes)

Construct a new hash print job attribute set, initially populated with
the values from the given array.

HashPrintJobAttributeSet

​(

PrintJobAttributeSet

attributes)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

PrintJobAttribute

interface.

---

#### Constructor Summary

Construct a new, empty hash print job attribute set.

Construct a new hash print job attribute set, initially populated with
the given value.

Construct a new hash print job attribute set, initially populated with
the values from the given array.

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

PrintJobAttribute

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

PrintJobAttributeSet

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

PrintJobAttributeSet

add

,

addAll

---

#### Methods declared in interface javax.print.attribute. PrintJobAttributeSet

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- HashPrintJobAttributeSet

```java
public HashPrintJobAttributeSet()
```

Construct a new, empty hash print job attribute set.

- HashPrintJobAttributeSet

```java
public HashPrintJobAttributeSet​(
PrintJobAttribute
attribute)
```

Construct a new hash print job attribute set, initially populated with
the given value.

**Parameters:** attribute

- attribute value to add to the set
**Throws:** NullPointerException

- if

attribute

is

null

- HashPrintJobAttributeSet

```java
public HashPrintJobAttributeSet​(
PrintJobAttribute
[] attributes)
```

Construct a new hash print job attribute set, initially populated with
the values from the given array. The new attribute set is populated by
adding the elements of

attributes

array to the set in sequence,
starting at index 0. Thus, later array elements may replace earlier array
elements if the array contains duplicate attribute values or attribute
categories.

**Parameters:** attributes

- array of attribute values to add to the set. If

null

, an empty attribute set is constructed.
**Throws:** NullPointerException

- if any element of

attributes

is

null

- HashPrintJobAttributeSet

```java
public HashPrintJobAttributeSet​(
PrintJobAttributeSet
attributes)
```

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

PrintJobAttribute

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

PrintJobAttribute

Constructor Detail

- HashPrintJobAttributeSet

```java
public HashPrintJobAttributeSet()
```

Construct a new, empty hash print job attribute set.

- HashPrintJobAttributeSet

```java
public HashPrintJobAttributeSet​(
PrintJobAttribute
attribute)
```

Construct a new hash print job attribute set, initially populated with
the given value.

**Parameters:** attribute

- attribute value to add to the set
**Throws:** NullPointerException

- if

attribute

is

null

- HashPrintJobAttributeSet

```java
public HashPrintJobAttributeSet​(
PrintJobAttribute
[] attributes)
```

Construct a new hash print job attribute set, initially populated with
the values from the given array. The new attribute set is populated by
adding the elements of

attributes

array to the set in sequence,
starting at index 0. Thus, later array elements may replace earlier array
elements if the array contains duplicate attribute values or attribute
categories.

**Parameters:** attributes

- array of attribute values to add to the set. If

null

, an empty attribute set is constructed.
**Throws:** NullPointerException

- if any element of

attributes

is

null

- HashPrintJobAttributeSet

```java
public HashPrintJobAttributeSet​(
PrintJobAttributeSet
attributes)
```

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

PrintJobAttribute

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

PrintJobAttribute

---

#### Constructor Detail

HashPrintJobAttributeSet

```java
public HashPrintJobAttributeSet()
```

Construct a new, empty hash print job attribute set.

---

#### HashPrintJobAttributeSet

public HashPrintJobAttributeSet()

Construct a new, empty hash print job attribute set.

HashPrintJobAttributeSet

```java
public HashPrintJobAttributeSet​(
PrintJobAttribute
attribute)
```

Construct a new hash print job attribute set, initially populated with
the given value.

**Parameters:** attribute

- attribute value to add to the set
**Throws:** NullPointerException

- if

attribute

is

null

---

#### HashPrintJobAttributeSet

public HashPrintJobAttributeSet​(

PrintJobAttribute

attribute)

Construct a new hash print job attribute set, initially populated with
the given value.

HashPrintJobAttributeSet

```java
public HashPrintJobAttributeSet​(
PrintJobAttribute
[] attributes)
```

Construct a new hash print job attribute set, initially populated with
the values from the given array. The new attribute set is populated by
adding the elements of

attributes

array to the set in sequence,
starting at index 0. Thus, later array elements may replace earlier array
elements if the array contains duplicate attribute values or attribute
categories.

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

#### HashPrintJobAttributeSet

public HashPrintJobAttributeSet​(

PrintJobAttribute

[] attributes)

Construct a new hash print job attribute set, initially populated with
the values from the given array. The new attribute set is populated by
adding the elements of

attributes

array to the set in sequence,
starting at index 0. Thus, later array elements may replace earlier array
elements if the array contains duplicate attribute values or attribute
categories.

HashPrintJobAttributeSet

```java
public HashPrintJobAttributeSet​(
PrintJobAttributeSet
attributes)
```

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

PrintJobAttribute

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

PrintJobAttribute

---

#### HashPrintJobAttributeSet

public HashPrintJobAttributeSet​(

PrintJobAttributeSet

attributes)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

PrintJobAttribute

interface.

---

