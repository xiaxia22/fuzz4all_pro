# Class HashPrintRequestAttributeSet

**Source:** `java.desktop\javax\print\attribute\HashPrintRequestAttributeSet.html`

### Class Description

```java
public class
HashPrintRequestAttributeSet

extends
HashAttributeSet

implements
PrintRequestAttributeSet
,
Serializable
```

Class

HashPrintRequestAttributeSet

inherits its implementation from
class

HashAttributeSet

and enforces the semantic
restrictions of interface

PrintRequestAttributeSet

.

**All Implemented Interfaces:** Serializable

,

AttributeSet

,

PrintRequestAttributeSet

---

### Field Details

*No entries found.*

### Constructor Details

#### public HashPrintRequestAttributeSet()

Construct a new, empty print request attribute set.

---

#### public HashPrintRequestAttributeSet​(
PrintRequestAttribute
attribute)

Construct a new print request attribute set, initially populated with the
given value.

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

#### public HashPrintRequestAttributeSet​(
PrintRequestAttribute
[] attributes)

Construct a new print request attribute set, initially populated with the
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

#### public HashPrintRequestAttributeSet​(
PrintRequestAttributeSet
attributes)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

(PrintRequestAttributeSe

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

PrintRequestAttributeSe

---

### Method Details

*No entries found.*

### Additional Sections

#### Class HashPrintRequestAttributeSet

java.lang.Object

- javax.print.attribute.HashAttributeSet
- - javax.print.attribute.HashPrintRequestAttributeSet

javax.print.attribute.HashAttributeSet

- javax.print.attribute.HashPrintRequestAttributeSet

javax.print.attribute.HashPrintRequestAttributeSet

**All Implemented Interfaces:** Serializable

,

AttributeSet

,

PrintRequestAttributeSet

```java
public class
HashPrintRequestAttributeSet

extends
HashAttributeSet

implements
PrintRequestAttributeSet
,
Serializable
```

Class

HashPrintRequestAttributeSet

inherits its implementation from
class

HashAttributeSet

and enforces the semantic
restrictions of interface

PrintRequestAttributeSet

.

**See Also:** Serialized Form

public class

HashPrintRequestAttributeSet

extends

HashAttributeSet

implements

PrintRequestAttributeSet

,

Serializable

Class

HashPrintRequestAttributeSet

inherits its implementation from
class

HashAttributeSet

and enforces the semantic
restrictions of interface

PrintRequestAttributeSet

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

HashPrintRequestAttributeSet

()

Construct a new, empty print request attribute set.

HashPrintRequestAttributeSet

​(

PrintRequestAttribute

attribute)

Construct a new print request attribute set, initially populated with the
given value.

HashPrintRequestAttributeSet

​(

PrintRequestAttribute

[] attributes)

Construct a new print request attribute set, initially populated with the
values from the given array.

HashPrintRequestAttributeSet

​(

PrintRequestAttributeSet

attributes)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

(PrintRequestAttributeSe

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

PrintRequestAttributeSet

add

,

addAll

Constructor Summary

Constructors

Constructor

Description

HashPrintRequestAttributeSet

()

Construct a new, empty print request attribute set.

HashPrintRequestAttributeSet

​(

PrintRequestAttribute

attribute)

Construct a new print request attribute set, initially populated with the
given value.

HashPrintRequestAttributeSet

​(

PrintRequestAttribute

[] attributes)

Construct a new print request attribute set, initially populated with the
values from the given array.

HashPrintRequestAttributeSet

​(

PrintRequestAttributeSet

attributes)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

(PrintRequestAttributeSe

interface.

---

#### Constructor Summary

Construct a new, empty print request attribute set.

Construct a new print request attribute set, initially populated with the
given value.

Construct a new print request attribute set, initially populated with the
values from the given array.

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

(PrintRequestAttributeSe

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

PrintRequestAttributeSet

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

PrintRequestAttributeSet

add

,

addAll

---

#### Methods declared in interface javax.print.attribute. PrintRequestAttributeSet

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- HashPrintRequestAttributeSet

```java
public HashPrintRequestAttributeSet()
```

Construct a new, empty print request attribute set.

- HashPrintRequestAttributeSet

```java
public HashPrintRequestAttributeSet​(
PrintRequestAttribute
attribute)
```

Construct a new print request attribute set, initially populated with the
given value.

**Parameters:** attribute

- attribute value to add to the set
**Throws:** NullPointerException

- if

attribute

is

null

- HashPrintRequestAttributeSet

```java
public HashPrintRequestAttributeSet​(
PrintRequestAttribute
[] attributes)
```

Construct a new print request attribute set, initially populated with the
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

- HashPrintRequestAttributeSet

```java
public HashPrintRequestAttributeSet​(
PrintRequestAttributeSet
attributes)
```

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

(PrintRequestAttributeSe

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

PrintRequestAttributeSe

Constructor Detail

- HashPrintRequestAttributeSet

```java
public HashPrintRequestAttributeSet()
```

Construct a new, empty print request attribute set.

- HashPrintRequestAttributeSet

```java
public HashPrintRequestAttributeSet​(
PrintRequestAttribute
attribute)
```

Construct a new print request attribute set, initially populated with the
given value.

**Parameters:** attribute

- attribute value to add to the set
**Throws:** NullPointerException

- if

attribute

is

null

- HashPrintRequestAttributeSet

```java
public HashPrintRequestAttributeSet​(
PrintRequestAttribute
[] attributes)
```

Construct a new print request attribute set, initially populated with the
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

- HashPrintRequestAttributeSet

```java
public HashPrintRequestAttributeSet​(
PrintRequestAttributeSet
attributes)
```

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

(PrintRequestAttributeSe

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

PrintRequestAttributeSe

---

#### Constructor Detail

HashPrintRequestAttributeSet

```java
public HashPrintRequestAttributeSet()
```

Construct a new, empty print request attribute set.

---

#### HashPrintRequestAttributeSet

public HashPrintRequestAttributeSet()

Construct a new, empty print request attribute set.

HashPrintRequestAttributeSet

```java
public HashPrintRequestAttributeSet​(
PrintRequestAttribute
attribute)
```

Construct a new print request attribute set, initially populated with the
given value.

**Parameters:** attribute

- attribute value to add to the set
**Throws:** NullPointerException

- if

attribute

is

null

---

#### HashPrintRequestAttributeSet

public HashPrintRequestAttributeSet​(

PrintRequestAttribute

attribute)

Construct a new print request attribute set, initially populated with the
given value.

HashPrintRequestAttributeSet

```java
public HashPrintRequestAttributeSet​(
PrintRequestAttribute
[] attributes)
```

Construct a new print request attribute set, initially populated with the
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

#### HashPrintRequestAttributeSet

public HashPrintRequestAttributeSet​(

PrintRequestAttribute

[] attributes)

Construct a new print request attribute set, initially populated with the
values from the given array. The new attribute set is populated by adding
the elements of

attributes

array to the set in sequence, starting
at index 0. Thus, later array elements may replace earlier array elements
if the array contains duplicate attribute values or attribute categories.

HashPrintRequestAttributeSet

```java
public HashPrintRequestAttributeSet​(
PrintRequestAttributeSet
attributes)
```

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

(PrintRequestAttributeSe

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

PrintRequestAttributeSe

---

#### HashPrintRequestAttributeSet

public HashPrintRequestAttributeSet​(

PrintRequestAttributeSet

attributes)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

(PrintRequestAttributeSe

interface.

---

