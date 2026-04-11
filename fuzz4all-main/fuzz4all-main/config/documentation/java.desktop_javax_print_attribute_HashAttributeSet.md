# Class HashAttributeSet

**Source:** `java.desktop\javax\print\attribute\HashAttributeSet.html`

### Class Description

```java
public class
HashAttributeSet

extends
Object

implements
AttributeSet
,
Serializable
```

Class

HashAttributeSet

provides an

AttributeSet

implementation with characteristics of a hash map.

**All Implemented Interfaces:** Serializable

,

AttributeSet

---

### Field Details

*No entries found.*

### Constructor Details

#### public HashAttributeSet()

Construct a new, empty attribute set.

---

#### public HashAttributeSet​(
Attribute
attribute)

Construct a new attribute set, initially populated with the given
attribute.

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

#### public HashAttributeSet​(
Attribute
[] attributes)

Construct a new attribute set, initially populated with the values from
the given array. The new attribute set is populated by adding the
elements of

attributes

array to the set in sequence, starting at
index 0. Thus, later array elements may replace earlier array elements if
the array contains duplicate attribute values or attribute categories.

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

#### public HashAttributeSet​(
AttributeSet
attributes)

Construct a new attribute set, initially populated with the values from
the given set.

**Parameters:**
- attributes

- set of attributes from which to initialise this set.
If

null

, an empty attribute set is constructed.

---

#### protected HashAttributeSet​(
Class
<?> interfaceName)

Construct a new, empty attribute set, where the members of the attribute
set are restricted to the given interface.

**Parameters:**
- interfaceName

- the interface of which all members of this
attribute set must be an instance. It is assumed to be interface

Attribute

or a subinterface thereof.

**Throws:**
- NullPointerException

- if

interfaceName

is

null

---

#### protected HashAttributeSet​(
Attribute
attribute,

Class
<?> interfaceName)

Construct a new attribute set, initially populated with the given
attribute, where the members of the attribute set are restricted to the
given interface.

**Parameters:**
- attribute

- attribute value to add to the set
- interfaceName

- the interface of which all members of this
attribute set must be an instance. It is assumed to be interface

Attribute

or a subinterface thereof.

**Throws:**
- NullPointerException

- if

attribute

or

interfaceName

are

null
- ClassCastException

- if

attribute

is not an instance of

interfaceName

---

#### protected HashAttributeSet​(
Attribute
[] attributes,

Class
<?> interfaceName)

Construct a new attribute set, where the members of the attribute set are
restricted to the given interface. The new attribute set is populated by
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
- interfaceName

- the interface of which all members of this
attribute set must be an instance. It is assumed to be interface

Attribute

or a subinterface thereof.

**Throws:**
- NullPointerException

- if

interfaceName

is

null

, or
if any element of

attributes

is

null
- ClassCastException

- if any element of

attributes

is not an
instance of

interfaceName

---

#### protected HashAttributeSet​(
AttributeSet
attributes,

Class
<?> interfaceName)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the given interface.

**Parameters:**
- attributes

- set of attribute values to initialise the set. If

null

, an empty attribute set is constructed.
- interfaceName

- The interface of which all members of this
attribute set must be an instance. It is assumed to be interface

Attribute

or a subinterface thereof.

**Throws:**
- ClassCastException

- if any element of

attributes

is not an
instance of

interfaceName

---

### Method Details

#### public
Attribute
get​(
Class
<?> category)

Returns the attribute value which this attribute set contains in the
given attribute category. Returns

null

if this attribute set does
not contain any attribute value in the given attribute category.

**Specified by:**
- get

in interface

AttributeSet

**Parameters:**
- category

- attribute category whose associated attribute value is
to be returned. It must be a

Class

that implements
interface

Attribute

.

**Returns:**
- the attribute value in the given attribute category contained in
this attribute set, or

null

if this attribute set does
not contain any attribute value in the given attribute category

**Throws:**
- NullPointerException

- if the

category

is

null
- ClassCastException

- if the

category

is not a

Class

that implements interface

Attribute

---

#### public boolean add​(
Attribute
attribute)

Adds the specified attribute to this attribute set if it is not already
present, first removing any existing in the same attribute category as
the specified attribute value.

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
- NullPointerException

- if the

attribute

is

null
- UnmodifiableSetException

- if this attribute set does not support
the

add()

operation

---

#### public boolean remove​(
Class
<?> category)

Removes any attribute for this category from this attribute set if
present. If

category

is

null

, then

remove()

does
nothing and returns

false

.

**Specified by:**
- remove

in interface

AttributeSet

**Parameters:**
- category

- attribute category to be removed from this attribute set

**Returns:**
- true

if this attribute set changed as a result of the
call, i.e., the given attribute category had been a member of
this attribute set

**Throws:**
- UnmodifiableSetException

- if this attribute set does not support
the

remove()

operation

---

#### public boolean remove​(
Attribute
attribute)

Removes the specified attribute from this attribute set if present. If

attribute

is

null

, then

remove()

does nothing and
returns

false

.

**Specified by:**
- remove

in interface

AttributeSet

**Parameters:**
- attribute

- attribute value to be removed from this attribute set

**Returns:**
- true

if this attribute set changed as a result of the
call, i.e., the given attribute value had been a member of this
attribute set

**Throws:**
- UnmodifiableSetException

- if this attribute set does not support
the

remove()

operation

---

#### public boolean containsKey​(
Class
<?> category)

Returns

true

if this attribute set contains an attribute for the
specified category.

**Specified by:**
- containsKey

in interface

AttributeSet

**Parameters:**
- category

- whose presence in this attribute set is to be tested

**Returns:**
- true

if this attribute set contains an attribute value
for the specified category

---

#### public boolean containsValue​(
Attribute
attribute)

Returns

true

if this attribute set contains the given attribute.

**Specified by:**
- containsValue

in interface

AttributeSet

**Parameters:**
- attribute

- value whose presence in this attribute set is to be
tested

**Returns:**
- true

if this attribute set contains the given attribute
value

---

#### public boolean addAll​(
AttributeSet
attributes)

Adds all of the elements in the specified set to this attribute. The
outcome is the same as if the

add(Attribute)

operation had been applied to this attribute set successively with each
element from the specified set. The behavior of the

addAll(AttributeSet)

operation is unspecified if the specified
set is modified while the operation is in progress.

If the

addAll(AttributeSet)

operation throws an exception, the
effect on this attribute set's state is implementation dependent;
elements from the specified set before the point of the exception may or
may not have been added to this attribute set.

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

addAll(AttributeSet)

method
- NullPointerException

- if some element in the specified set is

null

, or the set is

null

**See Also:**
- add(Attribute)

---

#### public int size()

Returns the number of attributes in this attribute set. If this attribute
set contains more than

Integer.MAX_VALUE

elements, returns

Integer.MAX_VALUE

.

**Specified by:**
- size

in interface

AttributeSet

**Returns:**
- the number of attributes in this attribute set

---

#### public
Attribute
[] toArray()

Returns an array of the attributes contained in this set.

**Specified by:**
- toArray

in interface

AttributeSet

**Returns:**
- the attributes contained in this set as an array, zero length if
the

AttributeSet

is empty

---

#### public void clear()

Removes all attributes from this attribute set.

**Specified by:**
- clear

in interface

AttributeSet

**Throws:**
- UnmodifiableSetException

- if this attribute set does not support
the

clear()

operation

---

#### public boolean isEmpty()

Returns

true

if this attribute set contains no attributes.

**Specified by:**
- isEmpty

in interface

AttributeSet

**Returns:**
- true

if this attribute set contains no attributes

---

#### public boolean equals​(
Object
object)

Compares the specified object with this attribute set for equality.
Returns

true

if the given object is also an attribute set and the
two attribute sets contain the same attribute category-attribute value
mappings. This ensures that the

equals()

method works properly
across different implementations of the

AttributeSet

interface.

**Specified by:**
- equals

in interface

AttributeSet

**Overrides:**
- equals

in class

Object

**Parameters:**
- object

- to be compared for equality with this attribute set

**Returns:**
- true

if the specified object is equal to this attribute
set

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this attribute set. The hash code of an
attribute set is defined to be the sum of the hash codes of each entry in
the

AttributeSet

. This ensures that

t1.equals(t2)

implies
that

t1.hashCode()==t2.hashCode()

for any two attribute sets

t1

and

t2

, as required by the general contract of

Object.hashCode()

.

**Specified by:**
- hashCode

in interface

AttributeSet

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this attribute set

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class HashAttributeSet

java.lang.Object

- javax.print.attribute.HashAttributeSet

javax.print.attribute.HashAttributeSet

**All Implemented Interfaces:** Serializable

,

AttributeSet

**Direct Known Subclasses:** HashDocAttributeSet

,

HashPrintJobAttributeSet

,

HashPrintRequestAttributeSet

,

HashPrintServiceAttributeSet

```java
public class
HashAttributeSet

extends
Object

implements
AttributeSet
,
Serializable
```

Class

HashAttributeSet

provides an

AttributeSet

implementation with characteristics of a hash map.

**See Also:** Serialized Form

public class

HashAttributeSet

extends

Object

implements

AttributeSet

,

Serializable

Class

HashAttributeSet

provides an

AttributeSet

implementation with characteristics of a hash map.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

HashAttributeSet

()

Construct a new, empty attribute set.

protected

HashAttributeSet

​(

Class

<?> interfaceName)

Construct a new, empty attribute set, where the members of the attribute
set are restricted to the given interface.

HashAttributeSet

​(

Attribute

attribute)

Construct a new attribute set, initially populated with the given
attribute.

HashAttributeSet

​(

Attribute

[] attributes)

Construct a new attribute set, initially populated with the values from
the given array.

protected

HashAttributeSet

​(

Attribute

[] attributes,

Class

<?> interfaceName)

Construct a new attribute set, where the members of the attribute set are
restricted to the given interface.

protected

HashAttributeSet

​(

Attribute

attribute,

Class

<?> interfaceName)

Construct a new attribute set, initially populated with the given
attribute, where the members of the attribute set are restricted to the
given interface.

HashAttributeSet

​(

AttributeSet

attributes)

Construct a new attribute set, initially populated with the values from
the given set.

protected

HashAttributeSet

​(

AttributeSet

attributes,

Class

<?> interfaceName)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the given interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

add

​(

Attribute

attribute)

Adds the specified attribute to this attribute set if it is not already
present, first removing any existing in the same attribute category as
the specified attribute value.

boolean

addAll

​(

AttributeSet

attributes)

Adds all of the elements in the specified set to this attribute.

void

clear

()

Removes all attributes from this attribute set.

boolean

containsKey

​(

Class

<?> category)

Returns

true

if this attribute set contains an attribute for the
specified category.

boolean

containsValue

​(

Attribute

attribute)

Returns

true

if this attribute set contains the given attribute.

boolean

equals

​(

Object

object)

Compares the specified object with this attribute set for equality.

Attribute

get

​(

Class

<?> category)

Returns the attribute value which this attribute set contains in the
given attribute category.

int

hashCode

()

Returns the hash code value for this attribute set.

boolean

isEmpty

()

Returns

true

if this attribute set contains no attributes.

boolean

remove

​(

Class

<?> category)

Removes any attribute for this category from this attribute set if
present.

boolean

remove

​(

Attribute

attribute)

Removes the specified attribute from this attribute set if present.

int

size

()

Returns the number of attributes in this attribute set.

Attribute

[]

toArray

()

Returns an array of the attributes contained in this set.

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

Constructor Summary

Constructors

Modifier

Constructor

Description

HashAttributeSet

()

Construct a new, empty attribute set.

protected

HashAttributeSet

​(

Class

<?> interfaceName)

Construct a new, empty attribute set, where the members of the attribute
set are restricted to the given interface.

HashAttributeSet

​(

Attribute

attribute)

Construct a new attribute set, initially populated with the given
attribute.

HashAttributeSet

​(

Attribute

[] attributes)

Construct a new attribute set, initially populated with the values from
the given array.

protected

HashAttributeSet

​(

Attribute

[] attributes,

Class

<?> interfaceName)

Construct a new attribute set, where the members of the attribute set are
restricted to the given interface.

protected

HashAttributeSet

​(

Attribute

attribute,

Class

<?> interfaceName)

Construct a new attribute set, initially populated with the given
attribute, where the members of the attribute set are restricted to the
given interface.

HashAttributeSet

​(

AttributeSet

attributes)

Construct a new attribute set, initially populated with the values from
the given set.

protected

HashAttributeSet

​(

AttributeSet

attributes,

Class

<?> interfaceName)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the given interface.

---

#### Constructor Summary

Construct a new, empty attribute set.

Construct a new, empty attribute set, where the members of the attribute
set are restricted to the given interface.

Construct a new attribute set, initially populated with the given
attribute.

Construct a new attribute set, initially populated with the values from
the given array.

Construct a new attribute set, where the members of the attribute set are
restricted to the given interface.

Construct a new attribute set, initially populated with the given
attribute, where the members of the attribute set are restricted to the
given interface.

Construct a new attribute set, initially populated with the values from
the given set.

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the given interface.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

add

​(

Attribute

attribute)

Adds the specified attribute to this attribute set if it is not already
present, first removing any existing in the same attribute category as
the specified attribute value.

boolean

addAll

​(

AttributeSet

attributes)

Adds all of the elements in the specified set to this attribute.

void

clear

()

Removes all attributes from this attribute set.

boolean

containsKey

​(

Class

<?> category)

Returns

true

if this attribute set contains an attribute for the
specified category.

boolean

containsValue

​(

Attribute

attribute)

Returns

true

if this attribute set contains the given attribute.

boolean

equals

​(

Object

object)

Compares the specified object with this attribute set for equality.

Attribute

get

​(

Class

<?> category)

Returns the attribute value which this attribute set contains in the
given attribute category.

int

hashCode

()

Returns the hash code value for this attribute set.

boolean

isEmpty

()

Returns

true

if this attribute set contains no attributes.

boolean

remove

​(

Class

<?> category)

Removes any attribute for this category from this attribute set if
present.

boolean

remove

​(

Attribute

attribute)

Removes the specified attribute from this attribute set if present.

int

size

()

Returns the number of attributes in this attribute set.

Attribute

[]

toArray

()

Returns an array of the attributes contained in this set.

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

---

#### Method Summary

Adds the specified attribute to this attribute set if it is not already
present, first removing any existing in the same attribute category as
the specified attribute value.

Adds all of the elements in the specified set to this attribute.

Removes all attributes from this attribute set.

Returns

true

if this attribute set contains an attribute for the
specified category.

Returns

true

if this attribute set contains the given attribute.

Compares the specified object with this attribute set for equality.

Returns the attribute value which this attribute set contains in the
given attribute category.

Returns the hash code value for this attribute set.

Returns

true

if this attribute set contains no attributes.

Removes any attribute for this category from this attribute set if
present.

Removes the specified attribute from this attribute set if present.

Returns the number of attributes in this attribute set.

Returns an array of the attributes contained in this set.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- HashAttributeSet

```java
public HashAttributeSet()
```

Construct a new, empty attribute set.

- HashAttributeSet

```java
public HashAttributeSet​(
Attribute
attribute)
```

Construct a new attribute set, initially populated with the given
attribute.

**Parameters:** attribute

- attribute value to add to the set
**Throws:** NullPointerException

- if

attribute

is

null

- HashAttributeSet

```java
public HashAttributeSet​(
Attribute
[] attributes)
```

Construct a new attribute set, initially populated with the values from
the given array. The new attribute set is populated by adding the
elements of

attributes

array to the set in sequence, starting at
index 0. Thus, later array elements may replace earlier array elements if
the array contains duplicate attribute values or attribute categories.

**Parameters:** attributes

- array of attribute values to add to the set. If

null

, an empty attribute set is constructed.
**Throws:** NullPointerException

- if any element of

attributes

is

null

- HashAttributeSet

```java
public HashAttributeSet​(
AttributeSet
attributes)
```

Construct a new attribute set, initially populated with the values from
the given set.

**Parameters:** attributes

- set of attributes from which to initialise this set.
If

null

, an empty attribute set is constructed.

- HashAttributeSet

```java
protected HashAttributeSet​(
Class
<?> interfaceName)
```

Construct a new, empty attribute set, where the members of the attribute
set are restricted to the given interface.

**Parameters:** interfaceName

- the interface of which all members of this
attribute set must be an instance. It is assumed to be interface

Attribute

or a subinterface thereof.
**Throws:** NullPointerException

- if

interfaceName

is

null

- HashAttributeSet

```java
protected HashAttributeSet​(
Attribute
attribute,

Class
<?> interfaceName)
```

Construct a new attribute set, initially populated with the given
attribute, where the members of the attribute set are restricted to the
given interface.

**Parameters:** attribute

- attribute value to add to the set
**Parameters:** interfaceName

- the interface of which all members of this
attribute set must be an instance. It is assumed to be interface

Attribute

or a subinterface thereof.
**Throws:** NullPointerException

- if

attribute

or

interfaceName

are

null
**Throws:** ClassCastException

- if

attribute

is not an instance of

interfaceName

- HashAttributeSet

```java
protected HashAttributeSet​(
Attribute
[] attributes,

Class
<?> interfaceName)
```

Construct a new attribute set, where the members of the attribute set are
restricted to the given interface. The new attribute set is populated by
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
**Parameters:** interfaceName

- the interface of which all members of this
attribute set must be an instance. It is assumed to be interface

Attribute

or a subinterface thereof.
**Throws:** NullPointerException

- if

interfaceName

is

null

, or
if any element of

attributes

is

null
**Throws:** ClassCastException

- if any element of

attributes

is not an
instance of

interfaceName

- HashAttributeSet

```java
protected HashAttributeSet​(
AttributeSet
attributes,

Class
<?> interfaceName)
```

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the given interface.

**Parameters:** attributes

- set of attribute values to initialise the set. If

null

, an empty attribute set is constructed.
**Parameters:** interfaceName

- The interface of which all members of this
attribute set must be an instance. It is assumed to be interface

Attribute

or a subinterface thereof.
**Throws:** ClassCastException

- if any element of

attributes

is not an
instance of

interfaceName

============ METHOD DETAIL ==========

- Method Detail

- get

```java
public
Attribute
get​(
Class
<?> category)
```

Returns the attribute value which this attribute set contains in the
given attribute category. Returns

null

if this attribute set does
not contain any attribute value in the given attribute category.

**Specified by:** get

in interface

AttributeSet
**Parameters:** category

- attribute category whose associated attribute value is
to be returned. It must be a

Class

that implements
interface

Attribute

.
**Returns:** the attribute value in the given attribute category contained in
this attribute set, or

null

if this attribute set does
not contain any attribute value in the given attribute category
**Throws:** NullPointerException

- if the

category

is

null
**Throws:** ClassCastException

- if the

category

is not a

Class

that implements interface

Attribute

- add

```java
public boolean add​(
Attribute
attribute)
```

Adds the specified attribute to this attribute set if it is not already
present, first removing any existing in the same attribute category as
the specified attribute value.

**Specified by:** add

in interface

AttributeSet
**Parameters:** attribute

- attribute value to be added to this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value was not already a member of
this attribute set
**Throws:** NullPointerException

- if the

attribute

is

null
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

add()

operation

- remove

```java
public boolean remove​(
Class
<?> category)
```

Removes any attribute for this category from this attribute set if
present. If

category

is

null

, then

remove()

does
nothing and returns

false

.

**Specified by:** remove

in interface

AttributeSet
**Parameters:** category

- attribute category to be removed from this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute category had been a member of
this attribute set
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

remove()

operation

- remove

```java
public boolean remove​(
Attribute
attribute)
```

Removes the specified attribute from this attribute set if present. If

attribute

is

null

, then

remove()

does nothing and
returns

false

.

**Specified by:** remove

in interface

AttributeSet
**Parameters:** attribute

- attribute value to be removed from this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value had been a member of this
attribute set
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

remove()

operation

- containsKey

```java
public boolean containsKey​(
Class
<?> category)
```

Returns

true

if this attribute set contains an attribute for the
specified category.

**Specified by:** containsKey

in interface

AttributeSet
**Parameters:** category

- whose presence in this attribute set is to be tested
**Returns:** true

if this attribute set contains an attribute value
for the specified category

- containsValue

```java
public boolean containsValue​(
Attribute
attribute)
```

Returns

true

if this attribute set contains the given attribute.

**Specified by:** containsValue

in interface

AttributeSet
**Parameters:** attribute

- value whose presence in this attribute set is to be
tested
**Returns:** true

if this attribute set contains the given attribute
value

- addAll

```java
public boolean addAll​(
AttributeSet
attributes)
```

Adds all of the elements in the specified set to this attribute. The
outcome is the same as if the

add(Attribute)

operation had been applied to this attribute set successively with each
element from the specified set. The behavior of the

addAll(AttributeSet)

operation is unspecified if the specified
set is modified while the operation is in progress.

If the

addAll(AttributeSet)

operation throws an exception, the
effect on this attribute set's state is implementation dependent;
elements from the specified set before the point of the exception may or
may not have been added to this attribute set.

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

addAll(AttributeSet)

method
**Throws:** NullPointerException

- if some element in the specified set is

null

, or the set is

null
**See Also:** add(Attribute)

- size

```java
public int size()
```

Returns the number of attributes in this attribute set. If this attribute
set contains more than

Integer.MAX_VALUE

elements, returns

Integer.MAX_VALUE

.

**Specified by:** size

in interface

AttributeSet
**Returns:** the number of attributes in this attribute set

- toArray

```java
public
Attribute
[] toArray()
```

Returns an array of the attributes contained in this set.

**Specified by:** toArray

in interface

AttributeSet
**Returns:** the attributes contained in this set as an array, zero length if
the

AttributeSet

is empty

- clear

```java
public void clear()
```

Removes all attributes from this attribute set.

**Specified by:** clear

in interface

AttributeSet
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

clear()

operation

- isEmpty

```java
public boolean isEmpty()
```

Returns

true

if this attribute set contains no attributes.

**Specified by:** isEmpty

in interface

AttributeSet
**Returns:** true

if this attribute set contains no attributes

- equals

```java
public boolean equals​(
Object
object)
```

Compares the specified object with this attribute set for equality.
Returns

true

if the given object is also an attribute set and the
two attribute sets contain the same attribute category-attribute value
mappings. This ensures that the

equals()

method works properly
across different implementations of the

AttributeSet

interface.

**Specified by:** equals

in interface

AttributeSet
**Overrides:** equals

in class

Object
**Parameters:** object

- to be compared for equality with this attribute set
**Returns:** true

if the specified object is equal to this attribute
set
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this attribute set. The hash code of an
attribute set is defined to be the sum of the hash codes of each entry in
the

AttributeSet

. This ensures that

t1.equals(t2)

implies
that

t1.hashCode()==t2.hashCode()

for any two attribute sets

t1

and

t2

, as required by the general contract of

Object.hashCode()

.

**Specified by:** hashCode

in interface

AttributeSet
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this attribute set
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- HashAttributeSet

```java
public HashAttributeSet()
```

Construct a new, empty attribute set.

- HashAttributeSet

```java
public HashAttributeSet​(
Attribute
attribute)
```

Construct a new attribute set, initially populated with the given
attribute.

**Parameters:** attribute

- attribute value to add to the set
**Throws:** NullPointerException

- if

attribute

is

null

- HashAttributeSet

```java
public HashAttributeSet​(
Attribute
[] attributes)
```

Construct a new attribute set, initially populated with the values from
the given array. The new attribute set is populated by adding the
elements of

attributes

array to the set in sequence, starting at
index 0. Thus, later array elements may replace earlier array elements if
the array contains duplicate attribute values or attribute categories.

**Parameters:** attributes

- array of attribute values to add to the set. If

null

, an empty attribute set is constructed.
**Throws:** NullPointerException

- if any element of

attributes

is

null

- HashAttributeSet

```java
public HashAttributeSet​(
AttributeSet
attributes)
```

Construct a new attribute set, initially populated with the values from
the given set.

**Parameters:** attributes

- set of attributes from which to initialise this set.
If

null

, an empty attribute set is constructed.

- HashAttributeSet

```java
protected HashAttributeSet​(
Class
<?> interfaceName)
```

Construct a new, empty attribute set, where the members of the attribute
set are restricted to the given interface.

**Parameters:** interfaceName

- the interface of which all members of this
attribute set must be an instance. It is assumed to be interface

Attribute

or a subinterface thereof.
**Throws:** NullPointerException

- if

interfaceName

is

null

- HashAttributeSet

```java
protected HashAttributeSet​(
Attribute
attribute,

Class
<?> interfaceName)
```

Construct a new attribute set, initially populated with the given
attribute, where the members of the attribute set are restricted to the
given interface.

**Parameters:** attribute

- attribute value to add to the set
**Parameters:** interfaceName

- the interface of which all members of this
attribute set must be an instance. It is assumed to be interface

Attribute

or a subinterface thereof.
**Throws:** NullPointerException

- if

attribute

or

interfaceName

are

null
**Throws:** ClassCastException

- if

attribute

is not an instance of

interfaceName

- HashAttributeSet

```java
protected HashAttributeSet​(
Attribute
[] attributes,

Class
<?> interfaceName)
```

Construct a new attribute set, where the members of the attribute set are
restricted to the given interface. The new attribute set is populated by
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
**Parameters:** interfaceName

- the interface of which all members of this
attribute set must be an instance. It is assumed to be interface

Attribute

or a subinterface thereof.
**Throws:** NullPointerException

- if

interfaceName

is

null

, or
if any element of

attributes

is

null
**Throws:** ClassCastException

- if any element of

attributes

is not an
instance of

interfaceName

- HashAttributeSet

```java
protected HashAttributeSet​(
AttributeSet
attributes,

Class
<?> interfaceName)
```

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the given interface.

**Parameters:** attributes

- set of attribute values to initialise the set. If

null

, an empty attribute set is constructed.
**Parameters:** interfaceName

- The interface of which all members of this
attribute set must be an instance. It is assumed to be interface

Attribute

or a subinterface thereof.
**Throws:** ClassCastException

- if any element of

attributes

is not an
instance of

interfaceName

---

#### Constructor Detail

HashAttributeSet

```java
public HashAttributeSet()
```

Construct a new, empty attribute set.

---

#### HashAttributeSet

public HashAttributeSet()

Construct a new, empty attribute set.

HashAttributeSet

```java
public HashAttributeSet​(
Attribute
attribute)
```

Construct a new attribute set, initially populated with the given
attribute.

**Parameters:** attribute

- attribute value to add to the set
**Throws:** NullPointerException

- if

attribute

is

null

---

#### HashAttributeSet

public HashAttributeSet​(

Attribute

attribute)

Construct a new attribute set, initially populated with the given
attribute.

HashAttributeSet

```java
public HashAttributeSet​(
Attribute
[] attributes)
```

Construct a new attribute set, initially populated with the values from
the given array. The new attribute set is populated by adding the
elements of

attributes

array to the set in sequence, starting at
index 0. Thus, later array elements may replace earlier array elements if
the array contains duplicate attribute values or attribute categories.

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

#### HashAttributeSet

public HashAttributeSet​(

Attribute

[] attributes)

Construct a new attribute set, initially populated with the values from
the given array. The new attribute set is populated by adding the
elements of

attributes

array to the set in sequence, starting at
index 0. Thus, later array elements may replace earlier array elements if
the array contains duplicate attribute values or attribute categories.

HashAttributeSet

```java
public HashAttributeSet​(
AttributeSet
attributes)
```

Construct a new attribute set, initially populated with the values from
the given set.

**Parameters:** attributes

- set of attributes from which to initialise this set.
If

null

, an empty attribute set is constructed.

---

#### HashAttributeSet

public HashAttributeSet​(

AttributeSet

attributes)

Construct a new attribute set, initially populated with the values from
the given set.

HashAttributeSet

```java
protected HashAttributeSet​(
Class
<?> interfaceName)
```

Construct a new, empty attribute set, where the members of the attribute
set are restricted to the given interface.

**Parameters:** interfaceName

- the interface of which all members of this
attribute set must be an instance. It is assumed to be interface

Attribute

or a subinterface thereof.
**Throws:** NullPointerException

- if

interfaceName

is

null

---

#### HashAttributeSet

protected HashAttributeSet​(

Class

<?> interfaceName)

Construct a new, empty attribute set, where the members of the attribute
set are restricted to the given interface.

HashAttributeSet

```java
protected HashAttributeSet​(
Attribute
attribute,

Class
<?> interfaceName)
```

Construct a new attribute set, initially populated with the given
attribute, where the members of the attribute set are restricted to the
given interface.

**Parameters:** attribute

- attribute value to add to the set
**Parameters:** interfaceName

- the interface of which all members of this
attribute set must be an instance. It is assumed to be interface

Attribute

or a subinterface thereof.
**Throws:** NullPointerException

- if

attribute

or

interfaceName

are

null
**Throws:** ClassCastException

- if

attribute

is not an instance of

interfaceName

---

#### HashAttributeSet

protected HashAttributeSet​(

Attribute

attribute,

Class

<?> interfaceName)

Construct a new attribute set, initially populated with the given
attribute, where the members of the attribute set are restricted to the
given interface.

HashAttributeSet

```java
protected HashAttributeSet​(
Attribute
[] attributes,

Class
<?> interfaceName)
```

Construct a new attribute set, where the members of the attribute set are
restricted to the given interface. The new attribute set is populated by
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
**Parameters:** interfaceName

- the interface of which all members of this
attribute set must be an instance. It is assumed to be interface

Attribute

or a subinterface thereof.
**Throws:** NullPointerException

- if

interfaceName

is

null

, or
if any element of

attributes

is

null
**Throws:** ClassCastException

- if any element of

attributes

is not an
instance of

interfaceName

---

#### HashAttributeSet

protected HashAttributeSet​(

Attribute

[] attributes,

Class

<?> interfaceName)

Construct a new attribute set, where the members of the attribute set are
restricted to the given interface. The new attribute set is populated by
adding the elements of

attributes

array to the set in sequence,
starting at index 0. Thus, later array elements may replace earlier array
elements if the array contains duplicate attribute values or attribute
categories.

HashAttributeSet

```java
protected HashAttributeSet​(
AttributeSet
attributes,

Class
<?> interfaceName)
```

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the given interface.

**Parameters:** attributes

- set of attribute values to initialise the set. If

null

, an empty attribute set is constructed.
**Parameters:** interfaceName

- The interface of which all members of this
attribute set must be an instance. It is assumed to be interface

Attribute

or a subinterface thereof.
**Throws:** ClassCastException

- if any element of

attributes

is not an
instance of

interfaceName

---

#### HashAttributeSet

protected HashAttributeSet​(

AttributeSet

attributes,

Class

<?> interfaceName)

Construct a new attribute set, initially populated with the values from
the given set where the members of the attribute set are restricted to
the given interface.

Method Detail

- get

```java
public
Attribute
get​(
Class
<?> category)
```

Returns the attribute value which this attribute set contains in the
given attribute category. Returns

null

if this attribute set does
not contain any attribute value in the given attribute category.

**Specified by:** get

in interface

AttributeSet
**Parameters:** category

- attribute category whose associated attribute value is
to be returned. It must be a

Class

that implements
interface

Attribute

.
**Returns:** the attribute value in the given attribute category contained in
this attribute set, or

null

if this attribute set does
not contain any attribute value in the given attribute category
**Throws:** NullPointerException

- if the

category

is

null
**Throws:** ClassCastException

- if the

category

is not a

Class

that implements interface

Attribute

- add

```java
public boolean add​(
Attribute
attribute)
```

Adds the specified attribute to this attribute set if it is not already
present, first removing any existing in the same attribute category as
the specified attribute value.

**Specified by:** add

in interface

AttributeSet
**Parameters:** attribute

- attribute value to be added to this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value was not already a member of
this attribute set
**Throws:** NullPointerException

- if the

attribute

is

null
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

add()

operation

- remove

```java
public boolean remove​(
Class
<?> category)
```

Removes any attribute for this category from this attribute set if
present. If

category

is

null

, then

remove()

does
nothing and returns

false

.

**Specified by:** remove

in interface

AttributeSet
**Parameters:** category

- attribute category to be removed from this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute category had been a member of
this attribute set
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

remove()

operation

- remove

```java
public boolean remove​(
Attribute
attribute)
```

Removes the specified attribute from this attribute set if present. If

attribute

is

null

, then

remove()

does nothing and
returns

false

.

**Specified by:** remove

in interface

AttributeSet
**Parameters:** attribute

- attribute value to be removed from this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value had been a member of this
attribute set
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

remove()

operation

- containsKey

```java
public boolean containsKey​(
Class
<?> category)
```

Returns

true

if this attribute set contains an attribute for the
specified category.

**Specified by:** containsKey

in interface

AttributeSet
**Parameters:** category

- whose presence in this attribute set is to be tested
**Returns:** true

if this attribute set contains an attribute value
for the specified category

- containsValue

```java
public boolean containsValue​(
Attribute
attribute)
```

Returns

true

if this attribute set contains the given attribute.

**Specified by:** containsValue

in interface

AttributeSet
**Parameters:** attribute

- value whose presence in this attribute set is to be
tested
**Returns:** true

if this attribute set contains the given attribute
value

- addAll

```java
public boolean addAll​(
AttributeSet
attributes)
```

Adds all of the elements in the specified set to this attribute. The
outcome is the same as if the

add(Attribute)

operation had been applied to this attribute set successively with each
element from the specified set. The behavior of the

addAll(AttributeSet)

operation is unspecified if the specified
set is modified while the operation is in progress.

If the

addAll(AttributeSet)

operation throws an exception, the
effect on this attribute set's state is implementation dependent;
elements from the specified set before the point of the exception may or
may not have been added to this attribute set.

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

addAll(AttributeSet)

method
**Throws:** NullPointerException

- if some element in the specified set is

null

, or the set is

null
**See Also:** add(Attribute)

- size

```java
public int size()
```

Returns the number of attributes in this attribute set. If this attribute
set contains more than

Integer.MAX_VALUE

elements, returns

Integer.MAX_VALUE

.

**Specified by:** size

in interface

AttributeSet
**Returns:** the number of attributes in this attribute set

- toArray

```java
public
Attribute
[] toArray()
```

Returns an array of the attributes contained in this set.

**Specified by:** toArray

in interface

AttributeSet
**Returns:** the attributes contained in this set as an array, zero length if
the

AttributeSet

is empty

- clear

```java
public void clear()
```

Removes all attributes from this attribute set.

**Specified by:** clear

in interface

AttributeSet
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

clear()

operation

- isEmpty

```java
public boolean isEmpty()
```

Returns

true

if this attribute set contains no attributes.

**Specified by:** isEmpty

in interface

AttributeSet
**Returns:** true

if this attribute set contains no attributes

- equals

```java
public boolean equals​(
Object
object)
```

Compares the specified object with this attribute set for equality.
Returns

true

if the given object is also an attribute set and the
two attribute sets contain the same attribute category-attribute value
mappings. This ensures that the

equals()

method works properly
across different implementations of the

AttributeSet

interface.

**Specified by:** equals

in interface

AttributeSet
**Overrides:** equals

in class

Object
**Parameters:** object

- to be compared for equality with this attribute set
**Returns:** true

if the specified object is equal to this attribute
set
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this attribute set. The hash code of an
attribute set is defined to be the sum of the hash codes of each entry in
the

AttributeSet

. This ensures that

t1.equals(t2)

implies
that

t1.hashCode()==t2.hashCode()

for any two attribute sets

t1

and

t2

, as required by the general contract of

Object.hashCode()

.

**Specified by:** hashCode

in interface

AttributeSet
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this attribute set
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

get

```java
public
Attribute
get​(
Class
<?> category)
```

Returns the attribute value which this attribute set contains in the
given attribute category. Returns

null

if this attribute set does
not contain any attribute value in the given attribute category.

**Specified by:** get

in interface

AttributeSet
**Parameters:** category

- attribute category whose associated attribute value is
to be returned. It must be a

Class

that implements
interface

Attribute

.
**Returns:** the attribute value in the given attribute category contained in
this attribute set, or

null

if this attribute set does
not contain any attribute value in the given attribute category
**Throws:** NullPointerException

- if the

category

is

null
**Throws:** ClassCastException

- if the

category

is not a

Class

that implements interface

Attribute

---

#### get

public

Attribute

get​(

Class

<?> category)

Returns the attribute value which this attribute set contains in the
given attribute category. Returns

null

if this attribute set does
not contain any attribute value in the given attribute category.

add

```java
public boolean add​(
Attribute
attribute)
```

Adds the specified attribute to this attribute set if it is not already
present, first removing any existing in the same attribute category as
the specified attribute value.

**Specified by:** add

in interface

AttributeSet
**Parameters:** attribute

- attribute value to be added to this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value was not already a member of
this attribute set
**Throws:** NullPointerException

- if the

attribute

is

null
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

add()

operation

---

#### add

public boolean add​(

Attribute

attribute)

Adds the specified attribute to this attribute set if it is not already
present, first removing any existing in the same attribute category as
the specified attribute value.

remove

```java
public boolean remove​(
Class
<?> category)
```

Removes any attribute for this category from this attribute set if
present. If

category

is

null

, then

remove()

does
nothing and returns

false

.

**Specified by:** remove

in interface

AttributeSet
**Parameters:** category

- attribute category to be removed from this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute category had been a member of
this attribute set
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

remove()

operation

---

#### remove

public boolean remove​(

Class

<?> category)

Removes any attribute for this category from this attribute set if
present. If

category

is

null

, then

remove()

does
nothing and returns

false

.

remove

```java
public boolean remove​(
Attribute
attribute)
```

Removes the specified attribute from this attribute set if present. If

attribute

is

null

, then

remove()

does nothing and
returns

false

.

**Specified by:** remove

in interface

AttributeSet
**Parameters:** attribute

- attribute value to be removed from this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value had been a member of this
attribute set
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

remove()

operation

---

#### remove

public boolean remove​(

Attribute

attribute)

Removes the specified attribute from this attribute set if present. If

attribute

is

null

, then

remove()

does nothing and
returns

false

.

containsKey

```java
public boolean containsKey​(
Class
<?> category)
```

Returns

true

if this attribute set contains an attribute for the
specified category.

**Specified by:** containsKey

in interface

AttributeSet
**Parameters:** category

- whose presence in this attribute set is to be tested
**Returns:** true

if this attribute set contains an attribute value
for the specified category

---

#### containsKey

public boolean containsKey​(

Class

<?> category)

Returns

true

if this attribute set contains an attribute for the
specified category.

containsValue

```java
public boolean containsValue​(
Attribute
attribute)
```

Returns

true

if this attribute set contains the given attribute.

**Specified by:** containsValue

in interface

AttributeSet
**Parameters:** attribute

- value whose presence in this attribute set is to be
tested
**Returns:** true

if this attribute set contains the given attribute
value

---

#### containsValue

public boolean containsValue​(

Attribute

attribute)

Returns

true

if this attribute set contains the given attribute.

addAll

```java
public boolean addAll​(
AttributeSet
attributes)
```

Adds all of the elements in the specified set to this attribute. The
outcome is the same as if the

add(Attribute)

operation had been applied to this attribute set successively with each
element from the specified set. The behavior of the

addAll(AttributeSet)

operation is unspecified if the specified
set is modified while the operation is in progress.

If the

addAll(AttributeSet)

operation throws an exception, the
effect on this attribute set's state is implementation dependent;
elements from the specified set before the point of the exception may or
may not have been added to this attribute set.

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

addAll(AttributeSet)

method
**Throws:** NullPointerException

- if some element in the specified set is

null

, or the set is

null
**See Also:** add(Attribute)

---

#### addAll

public boolean addAll​(

AttributeSet

attributes)

Adds all of the elements in the specified set to this attribute. The
outcome is the same as if the

add(Attribute)

operation had been applied to this attribute set successively with each
element from the specified set. The behavior of the

addAll(AttributeSet)

operation is unspecified if the specified
set is modified while the operation is in progress.

If the

addAll(AttributeSet)

operation throws an exception, the
effect on this attribute set's state is implementation dependent;
elements from the specified set before the point of the exception may or
may not have been added to this attribute set.

If the

addAll(AttributeSet)

operation throws an exception, the
effect on this attribute set's state is implementation dependent;
elements from the specified set before the point of the exception may or
may not have been added to this attribute set.

size

```java
public int size()
```

Returns the number of attributes in this attribute set. If this attribute
set contains more than

Integer.MAX_VALUE

elements, returns

Integer.MAX_VALUE

.

**Specified by:** size

in interface

AttributeSet
**Returns:** the number of attributes in this attribute set

---

#### size

public int size()

Returns the number of attributes in this attribute set. If this attribute
set contains more than

Integer.MAX_VALUE

elements, returns

Integer.MAX_VALUE

.

toArray

```java
public
Attribute
[] toArray()
```

Returns an array of the attributes contained in this set.

**Specified by:** toArray

in interface

AttributeSet
**Returns:** the attributes contained in this set as an array, zero length if
the

AttributeSet

is empty

---

#### toArray

public

Attribute

[] toArray()

Returns an array of the attributes contained in this set.

clear

```java
public void clear()
```

Removes all attributes from this attribute set.

**Specified by:** clear

in interface

AttributeSet
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

clear()

operation

---

#### clear

public void clear()

Removes all attributes from this attribute set.

isEmpty

```java
public boolean isEmpty()
```

Returns

true

if this attribute set contains no attributes.

**Specified by:** isEmpty

in interface

AttributeSet
**Returns:** true

if this attribute set contains no attributes

---

#### isEmpty

public boolean isEmpty()

Returns

true

if this attribute set contains no attributes.

equals

```java
public boolean equals​(
Object
object)
```

Compares the specified object with this attribute set for equality.
Returns

true

if the given object is also an attribute set and the
two attribute sets contain the same attribute category-attribute value
mappings. This ensures that the

equals()

method works properly
across different implementations of the

AttributeSet

interface.

**Specified by:** equals

in interface

AttributeSet
**Overrides:** equals

in class

Object
**Parameters:** object

- to be compared for equality with this attribute set
**Returns:** true

if the specified object is equal to this attribute
set
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

object)

Compares the specified object with this attribute set for equality.
Returns

true

if the given object is also an attribute set and the
two attribute sets contain the same attribute category-attribute value
mappings. This ensures that the

equals()

method works properly
across different implementations of the

AttributeSet

interface.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this attribute set. The hash code of an
attribute set is defined to be the sum of the hash codes of each entry in
the

AttributeSet

. This ensures that

t1.equals(t2)

implies
that

t1.hashCode()==t2.hashCode()

for any two attribute sets

t1

and

t2

, as required by the general contract of

Object.hashCode()

.

**Specified by:** hashCode

in interface

AttributeSet
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this attribute set
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this attribute set. The hash code of an
attribute set is defined to be the sum of the hash codes of each entry in
the

AttributeSet

. This ensures that

t1.equals(t2)

implies
that

t1.hashCode()==t2.hashCode()

for any two attribute sets

t1

and

t2

, as required by the general contract of

Object.hashCode()

.

---

