# Class HashDocAttributeSet

**Source:** `java.desktop\javax\print\attribute\HashDocAttributeSet.html`

### Class Description

```java
public class
HashDocAttributeSet

extends
HashAttributeSet

implements
DocAttributeSet
,
Serializable
```

Class

HashDocAttributeSet

provides an attribute set which inherits
its implementation from class

HashAttributeSet

and
enforces the semantic restrictions of interface

DocAttributeSet

.

**All Implemented Interfaces:** Serializable

,

AttributeSet

,

DocAttributeSet

---

### Field Details

*No entries found.*

### Constructor Details

#### public HashDocAttributeSet()

Construct a new, empty hash doc attribute set.

---

#### public HashDocAttributeSet​(
DocAttribute
attribute)

Construct a new hash doc attribute set, initially populated with the
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

#### public HashDocAttributeSet​(
DocAttribute
[] attributes)

Construct a new hash doc attribute set, initially populated with the
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

#### public HashDocAttributeSet​(
DocAttributeSet
attributes)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

DocAttribute

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

DocAttribute

---

### Method Details

*No entries found.*

### Additional Sections

#### Class HashDocAttributeSet

java.lang.Object

- javax.print.attribute.HashAttributeSet
- - javax.print.attribute.HashDocAttributeSet

javax.print.attribute.HashAttributeSet

- javax.print.attribute.HashDocAttributeSet

javax.print.attribute.HashDocAttributeSet

**All Implemented Interfaces:** Serializable

,

AttributeSet

,

DocAttributeSet

```java
public class
HashDocAttributeSet

extends
HashAttributeSet

implements
DocAttributeSet
,
Serializable
```

Class

HashDocAttributeSet

provides an attribute set which inherits
its implementation from class

HashAttributeSet

and
enforces the semantic restrictions of interface

DocAttributeSet

.

**See Also:** Serialized Form

public class

HashDocAttributeSet

extends

HashAttributeSet

implements

DocAttributeSet

,

Serializable

Class

HashDocAttributeSet

provides an attribute set which inherits
its implementation from class

HashAttributeSet

and
enforces the semantic restrictions of interface

DocAttributeSet

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

HashDocAttributeSet

()

Construct a new, empty hash doc attribute set.

HashDocAttributeSet

​(

DocAttribute

attribute)

Construct a new hash doc attribute set, initially populated with the
given value.

HashDocAttributeSet

​(

DocAttribute

[] attributes)

Construct a new hash doc attribute set, initially populated with the
values from the given array.

HashDocAttributeSet

​(

DocAttributeSet

attributes)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

DocAttribute

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

DocAttributeSet

add

,

addAll

Constructor Summary

Constructors

Constructor

Description

HashDocAttributeSet

()

Construct a new, empty hash doc attribute set.

HashDocAttributeSet

​(

DocAttribute

attribute)

Construct a new hash doc attribute set, initially populated with the
given value.

HashDocAttributeSet

​(

DocAttribute

[] attributes)

Construct a new hash doc attribute set, initially populated with the
values from the given array.

HashDocAttributeSet

​(

DocAttributeSet

attributes)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

DocAttribute

interface.

---

#### Constructor Summary

Construct a new, empty hash doc attribute set.

Construct a new hash doc attribute set, initially populated with the
given value.

Construct a new hash doc attribute set, initially populated with the
values from the given array.

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

DocAttribute

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

DocAttributeSet

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

DocAttributeSet

add

,

addAll

---

#### Methods declared in interface javax.print.attribute. DocAttributeSet

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- HashDocAttributeSet

```java
public HashDocAttributeSet()
```

Construct a new, empty hash doc attribute set.

- HashDocAttributeSet

```java
public HashDocAttributeSet​(
DocAttribute
attribute)
```

Construct a new hash doc attribute set, initially populated with the
given value.

**Parameters:** attribute

- attribute value to add to the set
**Throws:** NullPointerException

- if

attribute

is

null

- HashDocAttributeSet

```java
public HashDocAttributeSet​(
DocAttribute
[] attributes)
```

Construct a new hash doc attribute set, initially populated with the
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

- HashDocAttributeSet

```java
public HashDocAttributeSet​(
DocAttributeSet
attributes)
```

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

DocAttribute

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

DocAttribute

Constructor Detail

- HashDocAttributeSet

```java
public HashDocAttributeSet()
```

Construct a new, empty hash doc attribute set.

- HashDocAttributeSet

```java
public HashDocAttributeSet​(
DocAttribute
attribute)
```

Construct a new hash doc attribute set, initially populated with the
given value.

**Parameters:** attribute

- attribute value to add to the set
**Throws:** NullPointerException

- if

attribute

is

null

- HashDocAttributeSet

```java
public HashDocAttributeSet​(
DocAttribute
[] attributes)
```

Construct a new hash doc attribute set, initially populated with the
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

- HashDocAttributeSet

```java
public HashDocAttributeSet​(
DocAttributeSet
attributes)
```

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

DocAttribute

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

DocAttribute

---

#### Constructor Detail

HashDocAttributeSet

```java
public HashDocAttributeSet()
```

Construct a new, empty hash doc attribute set.

---

#### HashDocAttributeSet

public HashDocAttributeSet()

Construct a new, empty hash doc attribute set.

HashDocAttributeSet

```java
public HashDocAttributeSet​(
DocAttribute
attribute)
```

Construct a new hash doc attribute set, initially populated with the
given value.

**Parameters:** attribute

- attribute value to add to the set
**Throws:** NullPointerException

- if

attribute

is

null

---

#### HashDocAttributeSet

public HashDocAttributeSet​(

DocAttribute

attribute)

Construct a new hash doc attribute set, initially populated with the
given value.

HashDocAttributeSet

```java
public HashDocAttributeSet​(
DocAttribute
[] attributes)
```

Construct a new hash doc attribute set, initially populated with the
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

#### HashDocAttributeSet

public HashDocAttributeSet​(

DocAttribute

[] attributes)

Construct a new hash doc attribute set, initially populated with the
values from the given array. The new attribute set is populated by adding
the elements of

attributes

array to the set in sequence, starting
at index 0. Thus, later array elements may replace earlier array elements
if the array contains duplicate attribute values or attribute categories.

HashDocAttributeSet

```java
public HashDocAttributeSet​(
DocAttributeSet
attributes)
```

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

DocAttribute

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

DocAttribute

---

#### HashDocAttributeSet

public HashDocAttributeSet​(

DocAttributeSet

attributes)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the

DocAttribute

interface.

---

