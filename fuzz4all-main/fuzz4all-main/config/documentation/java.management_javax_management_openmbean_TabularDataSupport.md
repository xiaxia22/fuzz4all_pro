# Class TabularDataSupport

**Source:** `java.management\javax\management\openmbean\TabularDataSupport.html`

### Class Description

```java
public class
TabularDataSupport

extends
Object

implements
TabularData
,
Map
<
Object
,​
Object
>,
Cloneable
,
Serializable
```

The

TabularDataSupport

class is the

open data

class which implements the

TabularData

and the

Map

interfaces, and which is internally based on a hash map data structure.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Map

<

Object

,​

Object

>

,

TabularData

---

### Field Details

*No entries found.*

### Constructor Details

#### public TabularDataSupport​(
TabularType
tabularType)

Creates an empty

TabularDataSupport

instance
whose open-type is

tabularType

,
and whose underlying

HashMap

has a default
initial capacity (101) and default load factor (0.75).

This constructor simply calls

this(tabularType, 101, 0.75f);

**Parameters:**
- tabularType

- the

tabular type

describing this

TabularData

instance; cannot be null.

**Throws:**
- IllegalArgumentException

- if the tabular type is null.

---

#### public TabularDataSupport​(
TabularType
tabularType,
int initialCapacity,
float loadFactor)

Creates an empty

TabularDataSupport

instance whose open-type is

tabularType

,
and whose underlying

HashMap

has the specified initial capacity and load factor.

**Parameters:**
- tabularType

- the

tabular type

describing this

TabularData

instance;
cannot be null.
- initialCapacity

- the initial capacity of the HashMap.
- loadFactor

- the load factor of the HashMap

**Throws:**
- IllegalArgumentException

- if the initial capacity is less than zero,
or the load factor is nonpositive,
or the tabular type is null.

---

### Method Details

#### public
TabularType
getTabularType()

Returns the

tabular type

describing this

TabularData

instance.

**Specified by:**
- getTabularType

in interface

TabularData

**Returns:**
- the tabular type.

---

#### public
Object
[] calculateIndex​(
CompositeData
value)

Calculates the index that would be used in this

TabularData

instance to refer
to the specified composite data

value

parameter if it were added to this instance.
This method checks for the type validity of the specified

value

,
but does not check if the calculated index is already used
to refer to a value in this

TabularData

instance.

**Specified by:**
- calculateIndex

in interface

TabularData

**Parameters:**
- value

- the composite data value whose index in this

TabularData

instance is to be calculated;
must be of the same composite type as this instance's row type;
must not be null.

**Returns:**
- the index that the specified

value

would have in this

TabularData

instance.

**Throws:**
- NullPointerException

- if

value

is

null

.
- InvalidOpenTypeException

- if

value

does not conform to this

TabularData

instance's
row type definition.

---

#### public boolean containsKey​(
Object
key)

Returns

true

if and only if this

TabularData

instance contains a

CompositeData

value
(ie a row) whose index is the specified

key

. If

key

cannot be cast to a one dimension array
of Object instances, this method simply returns

false

; otherwise it returns the result of the call to

this.containsKey((Object[]) key)

.

**Specified by:**
- containsKey

in interface

Map

<

Object

,​

Object

>

**Parameters:**
- key

- the index value whose presence in this

TabularData

instance is to be tested.

**Returns:**
- true

if this

TabularData

indexes a row value with the specified key.

---

#### public boolean containsKey​(
Object
[] key)

Returns

true

if and only if this

TabularData

instance contains a

CompositeData

value
(ie a row) whose index is the specified

key

. If

key

is

null

or does not conform to
this

TabularData

instance's

TabularType

definition, this method simply returns

false

.

**Specified by:**
- containsKey

in interface

TabularData

**Parameters:**
- key

- the index value whose presence in this

TabularData

instance is to be tested.

**Returns:**
- true

if this

TabularData

indexes a row value with the specified key.

---

#### public boolean containsValue​(
CompositeData
value)

Returns

true

if and only if this

TabularData

instance contains the specified

CompositeData

value. If

value

is

null

or does not conform to
this

TabularData

instance's row type definition, this method simply returns

false

.

**Specified by:**
- containsValue

in interface

TabularData

**Parameters:**
- value

- the row value whose presence in this

TabularData

instance is to be tested.

**Returns:**
- true

if this

TabularData

instance contains the specified row value.

---

#### public boolean containsValue​(
Object
value)

Returns

true

if and only if this

TabularData

instance contains the specified
value.

**Specified by:**
- containsValue

in interface

Map

<

Object

,​

Object

>

**Parameters:**
- value

- the row value whose presence in this

TabularData

instance is to be tested.

**Returns:**
- true

if this

TabularData

instance contains the specified row value.

---

#### public
Object
get​(
Object
key)

This method simply calls

get((Object[]) key)

.

**Specified by:**
- get

in interface

Map

<

Object

,​

Object

>

**Parameters:**
- key

- the key whose associated value is to be returned

**Returns:**
- the value to which the specified key is mapped, or

null

if this map contains no mapping for the key

**Throws:**
- NullPointerException

- if the

key

is

null
- ClassCastException

- if the

key

is not of the type

Object[]
- InvalidKeyException

- if the

key

does not conform
to this

TabularData

instance's

TabularType

definition

---

#### public
CompositeData
get​(
Object
[] key)

Returns the

CompositeData

value whose index is

key

, or

null

if there is no value mapping
to

key

, in this

TabularData

instance.

**Specified by:**
- get

in interface

TabularData

**Parameters:**
- key

- the index of the value to get in this

TabularData

instance; must be valid with this

TabularData

instance's row type definition; must not
be null.

**Returns:**
- the value corresponding to

key

.

**Throws:**
- NullPointerException

- if the

key

is

null
- InvalidKeyException

- if the

key

does not conform
to this

TabularData

instance's

TabularType

type definition.

---

#### public
Object
put​(
Object
key,

Object
value)

This method simply calls

put((CompositeData) value)

and
therefore ignores its

key

parameter which can be

null

.

**Specified by:**
- put

in interface

Map

<

Object

,​

Object

>

**Parameters:**
- key

- an ignored parameter.
- value

- the

CompositeData

to put.

**Returns:**
- the value which is put

**Throws:**
- NullPointerException

- if the

value

is

null
- ClassCastException

- if the

value

is not of
the type

CompositeData
- InvalidOpenTypeException

- if the

value

does
not conform to this

TabularData

instance's

TabularType

definition
- KeyAlreadyExistsException

- if the key for the

value

parameter, calculated according to this

TabularData

instance's

TabularType

definition
already maps to an existing value

---

#### public
Object
remove​(
Object
key)

This method simply calls

remove((Object[]) key)

.

**Specified by:**
- remove

in interface

Map

<

Object

,​

Object

>

**Parameters:**
- key

- an

Object[]

representing the key to remove.

**Returns:**
- previous value associated with specified key, or

null

if there was no mapping for key.

**Throws:**
- NullPointerException

- if the

key

is

null
- ClassCastException

- if the

key

is not of the type

Object[]
- InvalidKeyException

- if the

key

does not conform to this

TabularData

instance's

TabularType

definition

---

#### public
CompositeData
remove​(
Object
[] key)

Removes the

CompositeData

value whose index is

key

from this

TabularData

instance,
and returns the removed value, or returns

null

if there is no value whose index is

key

.

**Specified by:**
- remove

in interface

TabularData

**Parameters:**
- key

- the index of the value to get in this

TabularData

instance;
must be valid with this

TabularData

instance's row type definition;
must not be null.

**Returns:**
- previous value associated with specified key, or

null

if there was no mapping for key.

**Throws:**
- NullPointerException

- if the

key

is

null
- InvalidKeyException

- if the

key

does not conform to this

TabularData

instance's

TabularType

definition

---

#### public void putAll​(
Map
<?,​?> t)

Add all the values contained in the specified map

t

to this

TabularData

instance. This method converts
the collection of values contained in this map into an array of

CompositeData

values, if possible, and then call the
method

putAll(CompositeData[])

. Note that the keys
used in the specified map

t

are ignored. This method
allows, for example to add the content of another

TabularData

instance with the same row type (but
possibly different index names) into this instance.

**Specified by:**
- putAll

in interface

Map

<

Object

,​

Object

>

**Parameters:**
- t

- the map whose values are to be added as new rows to
this

TabularData

instance; if

t

is

null

or empty, this method returns without doing
anything.

**Throws:**
- NullPointerException

- if a value in

t

is

null

.
- ClassCastException

- if a value in

t

is not an
instance of

CompositeData

.
- InvalidOpenTypeException

- if a value in

t

does not conform to this

TabularData

instance's row
type definition.
- KeyAlreadyExistsException

- if the index for a value in

t

, calculated according to this

TabularData

instance's

TabularType

definition
already maps to an existing value in this instance, or two
values in

t

have the same index.

---

#### public void putAll​(
CompositeData
[] values)

Add all the elements in

values

to this

TabularData

instance. If any element in

values

does not satisfy the constraints defined in

put

, or if any two
elements in

values

have the same index calculated
according to this

TabularData

instance's

TabularType

definition, then an exception describing
the failure is thrown and no element of

values

is
added, thus leaving this

TabularData

instance
unchanged.

**Specified by:**
- putAll

in interface

TabularData

**Parameters:**
- values

- the array of composite data values to be added as
new rows to this

TabularData

instance; if

values

is

null

or empty, this method
returns without doing anything.

**Throws:**
- NullPointerException

- if an element of

values

is

null
- InvalidOpenTypeException

- if an element of

values

does not conform to this

TabularData

instance's row type definition (ie its

TabularType

definition)
- KeyAlreadyExistsException

- if the index for an element
of

values

, calculated according to this

TabularData

instance's

TabularType

definition
already maps to an existing value in this instance, or two
elements of

values

have the same index

---

#### public void clear()

Removes all rows from this

TabularDataSupport

instance.

**Specified by:**
- clear

in interface

Map

<

Object

,​

Object

>
- clear

in interface

TabularData

---

#### public int size()

Returns the number of rows in this

TabularDataSupport

instance.

**Specified by:**
- size

in interface

Map

<

Object

,​

Object

>
- size

in interface

TabularData

**Returns:**
- the number of rows in this

TabularDataSupport

instance.

---

#### public boolean isEmpty()

Returns

true

if this

TabularDataSupport

instance contains no rows.

**Specified by:**
- isEmpty

in interface

Map

<

Object

,​

Object

>
- isEmpty

in interface

TabularData

**Returns:**
- true

if this

TabularDataSupport

instance contains no rows.

---

#### public
Set
<
Object
> keySet()

Returns a set view of the keys contained in the underlying map of this

TabularDataSupport

instance used to index the rows.
Each key contained in this

Set

is an unmodifiable

List<?>

so the returned set view is a

Set<List<?>>

but is declared as a

Set<Object>

for compatibility reasons.
The set is backed by the underlying map of this

TabularDataSupport

instance, so changes to the

TabularDataSupport

instance are reflected in the
set, and vice-versa.

The set supports element removal, which removes the corresponding
row from this

TabularDataSupport

instance, via the

Iterator.remove()

,

Set.remove(java.lang.Object)

,

Set.removeAll(java.util.Collection<?>)

,

Set.retainAll(java.util.Collection<?>)

, and

Set.clear()

operations. It does
not support the

Set.add(E)

or

Set.addAll(java.util.Collection<? extends E>)

operations.

**Specified by:**
- keySet

in interface

Map

<

Object

,​

Object

>
- keySet

in interface

TabularData

**Returns:**
- a set view (

Set<List<?>>

) of the keys used to index
the rows of this

TabularDataSupport

instance.

---

#### public
Collection
<
Object
> values()

Returns a collection view of the rows contained in this

TabularDataSupport

instance. The returned

Collection

is a

Collection<CompositeData>

but is declared as a

Collection<Object>

for compatibility reasons.
The returned collection can be used to iterate over the values.
The collection is backed by the underlying map, so changes to the

TabularDataSupport

instance are reflected in the collection,
and vice-versa.

The collection supports element removal, which removes the corresponding
index to row mapping from this

TabularDataSupport

instance, via
the

Iterator.remove()

,

Collection.remove(java.lang.Object)

,

Collection.removeAll(java.util.Collection<?>)

,

Collection.retainAll(java.util.Collection<?>)

,
and

Collection.clear()

operations. It does not support
the

Collection.add(E)

or

Collection.addAll(java.util.Collection<? extends E>)

operations.

**Specified by:**
- values

in interface

Map

<

Object

,​

Object

>
- values

in interface

TabularData

**Returns:**
- a collection view (

Collection<CompositeData>

) of
the values contained in this

TabularDataSupport

instance.

---

#### public
Set
<
Map.Entry
<
Object
,​
Object
>> entrySet()

Returns a collection view of the index to row mappings
contained in this

TabularDataSupport

instance.
Each element in the returned collection is
a

Map.Entry<List<?>,CompositeData>

but
is declared as a

Map.Entry<Object,Object>

for compatibility reasons. Each of the map entry
keys is an unmodifiable

List<?>

.
The collection is backed by the underlying map of this

TabularDataSupport

instance, so changes to the

TabularDataSupport

instance are reflected in
the collection, and vice-versa.
The collection supports element removal, which removes
the corresponding mapping from the map, via the

Iterator.remove()

,

Collection.remove(java.lang.Object)

,

Collection.removeAll(java.util.Collection<?>)

,

Collection.retainAll(java.util.Collection<?>)

,
and

Collection.clear()

operations. It does not support
the

Collection.add(E)

or

Collection.addAll(java.util.Collection<? extends E>)

operations.

IMPORTANT NOTICE

: Do not use the

setValue

method of the

Map.Entry

elements contained in the returned collection view.
Doing so would corrupt the index to row mappings contained in this

TabularDataSupport

instance.

**Specified by:**
- entrySet

in interface

Map

<

Object

,​

Object

>

**Returns:**
- a collection view (

Set<Map.Entry<List<?>,CompositeData>>

)
of the mappings contained in this map.

**See Also:**
- Map.Entry

---

#### public
Object
clone()

Returns a clone of this

TabularDataSupport

instance:
the clone is obtained by calling

super.clone()

, and then cloning the underlying map.
Only a shallow clone of the underlying map is made, i.e.
no cloning of the indexes and row values is made as they are immutable.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**See Also:**
- Cloneable

---

#### public boolean equals​(
Object
obj)

Compares the specified

obj

parameter with this

TabularDataSupport

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

TabularData

interface,
- their tabular types are equal
- their contents (ie all CompositeData values) are equal.

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

TabularData

interface.

**Specified by:**
- equals

in interface

Map

<

Object

,​

Object

>
- equals

in interface

TabularData

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to be compared for equality with this

TabularDataSupport

instance;

**Returns:**
- true

if the specified object is equal to this

TabularDataSupport

instance.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this

TabularDataSupport

instance.

The hash code of a

TabularDataSupport

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

tabular type

and its content, where the content is defined as all the CompositeData values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

TabularDataSupport

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing the

TabularData

interface
may be equal to this

TabularDataSupport

instance as defined by

equals(java.lang.Object)

,
but may have a different hash code if it is calculated differently.

**Specified by:**
- hashCode

in interface

Map

<

Object

,​

Object

>
- hashCode

in interface

TabularData

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this

TabularDataSupport

instance

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string representation of this

TabularDataSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.TabularDataSupport

),
the string representation of the tabular type of this instance, and the string representation of the contents
(ie list the key=value mappings as returned by a call to

dataMap.

toString()

).

**Specified by:**
- toString

in interface

TabularData

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

TabularDataSupport

instance

---

### Additional Sections

#### Class TabularDataSupport

java.lang.Object

- javax.management.openmbean.TabularDataSupport

javax.management.openmbean.TabularDataSupport

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Map

<

Object

,​

Object

>

,

TabularData

```java
public class
TabularDataSupport

extends
Object

implements
TabularData
,
Map
<
Object
,​
Object
>,
Cloneable
,
Serializable
```

The

TabularDataSupport

class is the

open data

class which implements the

TabularData

and the

Map

interfaces, and which is internally based on a hash map data structure.

**Since:** 1.5
**See Also:** Serialized Form

public class

TabularDataSupport

extends

Object

implements

TabularData

,

Map

<

Object

,​

Object

>,

Cloneable

,

Serializable

The

TabularDataSupport

class is the

open data

class which implements the

TabularData

and the

Map

interfaces, and which is internally based on a hash map data structure.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface java.util.

Map

Map.Entry

<

K

,​

V

>

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TabularDataSupport

​(

TabularType

tabularType)

Creates an empty

TabularDataSupport

instance
whose open-type is

tabularType

,
and whose underlying

HashMap

has a default
initial capacity (101) and default load factor (0.75).

TabularDataSupport

​(

TabularType

tabularType,
int initialCapacity,
float loadFactor)

Creates an empty

TabularDataSupport

instance whose open-type is

tabularType

,
and whose underlying

HashMap

has the specified initial capacity and load factor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

[]

calculateIndex

​(

CompositeData

value)

Calculates the index that would be used in this

TabularData

instance to refer
to the specified composite data

value

parameter if it were added to this instance.

void

clear

()

Removes all rows from this

TabularDataSupport

instance.

Object

clone

()

Returns a clone of this

TabularDataSupport

instance:
the clone is obtained by calling

super.clone()

, and then cloning the underlying map.

boolean

containsKey

​(

Object

key)

Returns

true

if and only if this

TabularData

instance contains a

CompositeData

value
(ie a row) whose index is the specified

key

.

boolean

containsKey

​(

Object

[] key)

Returns

true

if and only if this

TabularData

instance contains a

CompositeData

value
(ie a row) whose index is the specified

key

.

boolean

containsValue

​(

Object

value)

Returns

true

if and only if this

TabularData

instance contains the specified
value.

boolean

containsValue

​(

CompositeData

value)

Returns

true

if and only if this

TabularData

instance contains the specified

CompositeData

value.

Set

<

Map.Entry

<

Object

,​

Object

>>

entrySet

()

Returns a collection view of the index to row mappings
contained in this

TabularDataSupport

instance.

boolean

equals

​(

Object

obj)

Compares the specified

obj

parameter with this

TabularDataSupport

instance for equality.

Object

get

​(

Object

key)

This method simply calls

get((Object[]) key)

.

CompositeData

get

​(

Object

[] key)

Returns the

CompositeData

value whose index is

key

, or

null

if there is no value mapping
to

key

, in this

TabularData

instance.

TabularType

getTabularType

()

Returns the

tabular type

describing this

TabularData

instance.

int

hashCode

()

Returns the hash code value for this

TabularDataSupport

instance.

boolean

isEmpty

()

Returns

true

if this

TabularDataSupport

instance contains no rows.

Set

<

Object

>

keySet

()

Returns a set view of the keys contained in the underlying map of this

TabularDataSupport

instance used to index the rows.

Object

put

​(

Object

key,

Object

value)

This method simply calls

put((CompositeData) value)

and
therefore ignores its

key

parameter which can be

null

.

void

putAll

​(

Map

<?,​?> t)

Add all the values contained in the specified map

t

to this

TabularData

instance.

void

putAll

​(

CompositeData

[] values)

Add all the elements in

values

to this

TabularData

instance.

Object

remove

​(

Object

key)

This method simply calls

remove((Object[]) key)

.

CompositeData

remove

​(

Object

[] key)

Removes the

CompositeData

value whose index is

key

from this

TabularData

instance,
and returns the removed value, or returns

null

if there is no value whose index is

key

.

int

size

()

Returns the number of rows in this

TabularDataSupport

instance.

String

toString

()

Returns a string representation of this

TabularDataSupport

instance.

Collection

<

Object

>

values

()

Returns a collection view of the rows contained in this

TabularDataSupport

instance.

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

- Methods declared in interface java.util.

Map

compute

,

computeIfAbsent

,

computeIfPresent

,

forEach

,

getOrDefault

,

merge

,

putIfAbsent

,

remove

,

replace

,

replace

,

replaceAll

- Methods declared in interface javax.management.openmbean.

TabularData

put

Nested Class Summary

- Nested classes/interfaces declared in interface java.util.

Map

Map.Entry

<

K

,​

V

>

---

#### Nested Class Summary

Nested classes/interfaces declared in interface java.util.

Map

Map.Entry

<

K

,​

V

>

---

#### Nested classes/interfaces declared in interface java.util. Map

Constructor Summary

Constructors

Constructor

Description

TabularDataSupport

​(

TabularType

tabularType)

Creates an empty

TabularDataSupport

instance
whose open-type is

tabularType

,
and whose underlying

HashMap

has a default
initial capacity (101) and default load factor (0.75).

TabularDataSupport

​(

TabularType

tabularType,
int initialCapacity,
float loadFactor)

Creates an empty

TabularDataSupport

instance whose open-type is

tabularType

,
and whose underlying

HashMap

has the specified initial capacity and load factor.

---

#### Constructor Summary

Creates an empty

TabularDataSupport

instance
whose open-type is

tabularType

,
and whose underlying

HashMap

has a default
initial capacity (101) and default load factor (0.75).

Creates an empty

TabularDataSupport

instance whose open-type is

tabularType

,
and whose underlying

HashMap

has the specified initial capacity and load factor.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

[]

calculateIndex

​(

CompositeData

value)

Calculates the index that would be used in this

TabularData

instance to refer
to the specified composite data

value

parameter if it were added to this instance.

void

clear

()

Removes all rows from this

TabularDataSupport

instance.

Object

clone

()

Returns a clone of this

TabularDataSupport

instance:
the clone is obtained by calling

super.clone()

, and then cloning the underlying map.

boolean

containsKey

​(

Object

key)

Returns

true

if and only if this

TabularData

instance contains a

CompositeData

value
(ie a row) whose index is the specified

key

.

boolean

containsKey

​(

Object

[] key)

Returns

true

if and only if this

TabularData

instance contains a

CompositeData

value
(ie a row) whose index is the specified

key

.

boolean

containsValue

​(

Object

value)

Returns

true

if and only if this

TabularData

instance contains the specified
value.

boolean

containsValue

​(

CompositeData

value)

Returns

true

if and only if this

TabularData

instance contains the specified

CompositeData

value.

Set

<

Map.Entry

<

Object

,​

Object

>>

entrySet

()

Returns a collection view of the index to row mappings
contained in this

TabularDataSupport

instance.

boolean

equals

​(

Object

obj)

Compares the specified

obj

parameter with this

TabularDataSupport

instance for equality.

Object

get

​(

Object

key)

This method simply calls

get((Object[]) key)

.

CompositeData

get

​(

Object

[] key)

Returns the

CompositeData

value whose index is

key

, or

null

if there is no value mapping
to

key

, in this

TabularData

instance.

TabularType

getTabularType

()

Returns the

tabular type

describing this

TabularData

instance.

int

hashCode

()

Returns the hash code value for this

TabularDataSupport

instance.

boolean

isEmpty

()

Returns

true

if this

TabularDataSupport

instance contains no rows.

Set

<

Object

>

keySet

()

Returns a set view of the keys contained in the underlying map of this

TabularDataSupport

instance used to index the rows.

Object

put

​(

Object

key,

Object

value)

This method simply calls

put((CompositeData) value)

and
therefore ignores its

key

parameter which can be

null

.

void

putAll

​(

Map

<?,​?> t)

Add all the values contained in the specified map

t

to this

TabularData

instance.

void

putAll

​(

CompositeData

[] values)

Add all the elements in

values

to this

TabularData

instance.

Object

remove

​(

Object

key)

This method simply calls

remove((Object[]) key)

.

CompositeData

remove

​(

Object

[] key)

Removes the

CompositeData

value whose index is

key

from this

TabularData

instance,
and returns the removed value, or returns

null

if there is no value whose index is

key

.

int

size

()

Returns the number of rows in this

TabularDataSupport

instance.

String

toString

()

Returns a string representation of this

TabularDataSupport

instance.

Collection

<

Object

>

values

()

Returns a collection view of the rows contained in this

TabularDataSupport

instance.

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

- Methods declared in interface java.util.

Map

compute

,

computeIfAbsent

,

computeIfPresent

,

forEach

,

getOrDefault

,

merge

,

putIfAbsent

,

remove

,

replace

,

replace

,

replaceAll

- Methods declared in interface javax.management.openmbean.

TabularData

put

---

#### Method Summary

Calculates the index that would be used in this

TabularData

instance to refer
to the specified composite data

value

parameter if it were added to this instance.

Removes all rows from this

TabularDataSupport

instance.

Returns a clone of this

TabularDataSupport

instance:
the clone is obtained by calling

super.clone()

, and then cloning the underlying map.

Returns

true

if and only if this

TabularData

instance contains a

CompositeData

value
(ie a row) whose index is the specified

key

.

Returns

true

if and only if this

TabularData

instance contains the specified
value.

Returns

true

if and only if this

TabularData

instance contains the specified

CompositeData

value.

Returns a collection view of the index to row mappings
contained in this

TabularDataSupport

instance.

Compares the specified

obj

parameter with this

TabularDataSupport

instance for equality.

This method simply calls

get((Object[]) key)

.

Returns the

CompositeData

value whose index is

key

, or

null

if there is no value mapping
to

key

, in this

TabularData

instance.

Returns the

tabular type

describing this

TabularData

instance.

Returns the hash code value for this

TabularDataSupport

instance.

Returns

true

if this

TabularDataSupport

instance contains no rows.

Returns a set view of the keys contained in the underlying map of this

TabularDataSupport

instance used to index the rows.

This method simply calls

put((CompositeData) value)

and
therefore ignores its

key

parameter which can be

null

.

Add all the values contained in the specified map

t

to this

TabularData

instance.

Add all the elements in

values

to this

TabularData

instance.

This method simply calls

remove((Object[]) key)

.

Removes the

CompositeData

value whose index is

key

from this

TabularData

instance,
and returns the removed value, or returns

null

if there is no value whose index is

key

.

Returns the number of rows in this

TabularDataSupport

instance.

Returns a string representation of this

TabularDataSupport

instance.

Returns a collection view of the rows contained in this

TabularDataSupport

instance.

Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface java.util.

Map

compute

,

computeIfAbsent

,

computeIfPresent

,

forEach

,

getOrDefault

,

merge

,

putIfAbsent

,

remove

,

replace

,

replace

,

replaceAll

---

#### Methods declared in interface java.util. Map

Methods declared in interface javax.management.openmbean.

TabularData

put

---

#### Methods declared in interface javax.management.openmbean. TabularData

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TabularDataSupport

```java
public TabularDataSupport​(
TabularType
tabularType)
```

Creates an empty

TabularDataSupport

instance
whose open-type is

tabularType

,
and whose underlying

HashMap

has a default
initial capacity (101) and default load factor (0.75).

This constructor simply calls

this(tabularType, 101, 0.75f);

**Parameters:** tabularType

- the

tabular type

describing this

TabularData

instance; cannot be null.
**Throws:** IllegalArgumentException

- if the tabular type is null.

- TabularDataSupport

```java
public TabularDataSupport​(
TabularType
tabularType,
int initialCapacity,
float loadFactor)
```

Creates an empty

TabularDataSupport

instance whose open-type is

tabularType

,
and whose underlying

HashMap

has the specified initial capacity and load factor.

**Parameters:** tabularType

- the

tabular type

describing this

TabularData

instance;
cannot be null.
**Parameters:** initialCapacity

- the initial capacity of the HashMap.
**Parameters:** loadFactor

- the load factor of the HashMap
**Throws:** IllegalArgumentException

- if the initial capacity is less than zero,
or the load factor is nonpositive,
or the tabular type is null.

============ METHOD DETAIL ==========

- Method Detail

- getTabularType

```java
public
TabularType
getTabularType()
```

Returns the

tabular type

describing this

TabularData

instance.

**Specified by:** getTabularType

in interface

TabularData
**Returns:** the tabular type.

- calculateIndex

```java
public
Object
[] calculateIndex​(
CompositeData
value)
```

Calculates the index that would be used in this

TabularData

instance to refer
to the specified composite data

value

parameter if it were added to this instance.
This method checks for the type validity of the specified

value

,
but does not check if the calculated index is already used
to refer to a value in this

TabularData

instance.

**Specified by:** calculateIndex

in interface

TabularData
**Parameters:** value

- the composite data value whose index in this

TabularData

instance is to be calculated;
must be of the same composite type as this instance's row type;
must not be null.
**Returns:** the index that the specified

value

would have in this

TabularData

instance.
**Throws:** NullPointerException

- if

value

is

null

.
**Throws:** InvalidOpenTypeException

- if

value

does not conform to this

TabularData

instance's
row type definition.

- containsKey

```java
public boolean containsKey​(
Object
key)
```

Returns

true

if and only if this

TabularData

instance contains a

CompositeData

value
(ie a row) whose index is the specified

key

. If

key

cannot be cast to a one dimension array
of Object instances, this method simply returns

false

; otherwise it returns the result of the call to

this.containsKey((Object[]) key)

.

**Specified by:** containsKey

in interface

Map

<

Object

,​

Object

>
**Parameters:** key

- the index value whose presence in this

TabularData

instance is to be tested.
**Returns:** true

if this

TabularData

indexes a row value with the specified key.

- containsKey

```java
public boolean containsKey​(
Object
[] key)
```

Returns

true

if and only if this

TabularData

instance contains a

CompositeData

value
(ie a row) whose index is the specified

key

. If

key

is

null

or does not conform to
this

TabularData

instance's

TabularType

definition, this method simply returns

false

.

**Specified by:** containsKey

in interface

TabularData
**Parameters:** key

- the index value whose presence in this

TabularData

instance is to be tested.
**Returns:** true

if this

TabularData

indexes a row value with the specified key.

- containsValue

```java
public boolean containsValue​(
CompositeData
value)
```

Returns

true

if and only if this

TabularData

instance contains the specified

CompositeData

value. If

value

is

null

or does not conform to
this

TabularData

instance's row type definition, this method simply returns

false

.

**Specified by:** containsValue

in interface

TabularData
**Parameters:** value

- the row value whose presence in this

TabularData

instance is to be tested.
**Returns:** true

if this

TabularData

instance contains the specified row value.

- containsValue

```java
public boolean containsValue​(
Object
value)
```

Returns

true

if and only if this

TabularData

instance contains the specified
value.

**Specified by:** containsValue

in interface

Map

<

Object

,​

Object

>
**Parameters:** value

- the row value whose presence in this

TabularData

instance is to be tested.
**Returns:** true

if this

TabularData

instance contains the specified row value.

- get

```java
public
Object
get​(
Object
key)
```

This method simply calls

get((Object[]) key)

.

**Specified by:** get

in interface

Map

<

Object

,​

Object

>
**Parameters:** key

- the key whose associated value is to be returned
**Returns:** the value to which the specified key is mapped, or

null

if this map contains no mapping for the key
**Throws:** NullPointerException

- if the

key

is

null
**Throws:** ClassCastException

- if the

key

is not of the type

Object[]
**Throws:** InvalidKeyException

- if the

key

does not conform
to this

TabularData

instance's

TabularType

definition

- get

```java
public
CompositeData
get​(
Object
[] key)
```

Returns the

CompositeData

value whose index is

key

, or

null

if there is no value mapping
to

key

, in this

TabularData

instance.

**Specified by:** get

in interface

TabularData
**Parameters:** key

- the index of the value to get in this

TabularData

instance; must be valid with this

TabularData

instance's row type definition; must not
be null.
**Returns:** the value corresponding to

key

.
**Throws:** NullPointerException

- if the

key

is

null
**Throws:** InvalidKeyException

- if the

key

does not conform
to this

TabularData

instance's

TabularType

type definition.

- put

```java
public
Object
put​(
Object
key,

Object
value)
```

This method simply calls

put((CompositeData) value)

and
therefore ignores its

key

parameter which can be

null

.

**Specified by:** put

in interface

Map

<

Object

,​

Object

>
**Parameters:** key

- an ignored parameter.
**Parameters:** value

- the

CompositeData

to put.
**Returns:** the value which is put
**Throws:** NullPointerException

- if the

value

is

null
**Throws:** ClassCastException

- if the

value

is not of
the type

CompositeData
**Throws:** InvalidOpenTypeException

- if the

value

does
not conform to this

TabularData

instance's

TabularType

definition
**Throws:** KeyAlreadyExistsException

- if the key for the

value

parameter, calculated according to this

TabularData

instance's

TabularType

definition
already maps to an existing value

- remove

```java
public
Object
remove​(
Object
key)
```

This method simply calls

remove((Object[]) key)

.

**Specified by:** remove

in interface

Map

<

Object

,​

Object

>
**Parameters:** key

- an

Object[]

representing the key to remove.
**Returns:** previous value associated with specified key, or

null

if there was no mapping for key.
**Throws:** NullPointerException

- if the

key

is

null
**Throws:** ClassCastException

- if the

key

is not of the type

Object[]
**Throws:** InvalidKeyException

- if the

key

does not conform to this

TabularData

instance's

TabularType

definition

- remove

```java
public
CompositeData
remove​(
Object
[] key)
```

Removes the

CompositeData

value whose index is

key

from this

TabularData

instance,
and returns the removed value, or returns

null

if there is no value whose index is

key

.

**Specified by:** remove

in interface

TabularData
**Parameters:** key

- the index of the value to get in this

TabularData

instance;
must be valid with this

TabularData

instance's row type definition;
must not be null.
**Returns:** previous value associated with specified key, or

null

if there was no mapping for key.
**Throws:** NullPointerException

- if the

key

is

null
**Throws:** InvalidKeyException

- if the

key

does not conform to this

TabularData

instance's

TabularType

definition

- putAll

```java
public void putAll​(
Map
<?,​?> t)
```

Add all the values contained in the specified map

t

to this

TabularData

instance. This method converts
the collection of values contained in this map into an array of

CompositeData

values, if possible, and then call the
method

putAll(CompositeData[])

. Note that the keys
used in the specified map

t

are ignored. This method
allows, for example to add the content of another

TabularData

instance with the same row type (but
possibly different index names) into this instance.

**Specified by:** putAll

in interface

Map

<

Object

,​

Object

>
**Parameters:** t

- the map whose values are to be added as new rows to
this

TabularData

instance; if

t

is

null

or empty, this method returns without doing
anything.
**Throws:** NullPointerException

- if a value in

t

is

null

.
**Throws:** ClassCastException

- if a value in

t

is not an
instance of

CompositeData

.
**Throws:** InvalidOpenTypeException

- if a value in

t

does not conform to this

TabularData

instance's row
type definition.
**Throws:** KeyAlreadyExistsException

- if the index for a value in

t

, calculated according to this

TabularData

instance's

TabularType

definition
already maps to an existing value in this instance, or two
values in

t

have the same index.

- putAll

```java
public void putAll​(
CompositeData
[] values)
```

Add all the elements in

values

to this

TabularData

instance. If any element in

values

does not satisfy the constraints defined in

put

, or if any two
elements in

values

have the same index calculated
according to this

TabularData

instance's

TabularType

definition, then an exception describing
the failure is thrown and no element of

values

is
added, thus leaving this

TabularData

instance
unchanged.

**Specified by:** putAll

in interface

TabularData
**Parameters:** values

- the array of composite data values to be added as
new rows to this

TabularData

instance; if

values

is

null

or empty, this method
returns without doing anything.
**Throws:** NullPointerException

- if an element of

values

is

null
**Throws:** InvalidOpenTypeException

- if an element of

values

does not conform to this

TabularData

instance's row type definition (ie its

TabularType

definition)
**Throws:** KeyAlreadyExistsException

- if the index for an element
of

values

, calculated according to this

TabularData

instance's

TabularType

definition
already maps to an existing value in this instance, or two
elements of

values

have the same index

- clear

```java
public void clear()
```

Removes all rows from this

TabularDataSupport

instance.

**Specified by:** clear

in interface

Map

<

Object

,​

Object

>
**Specified by:** clear

in interface

TabularData

- size

```java
public int size()
```

Returns the number of rows in this

TabularDataSupport

instance.

**Specified by:** size

in interface

Map

<

Object

,​

Object

>
**Specified by:** size

in interface

TabularData
**Returns:** the number of rows in this

TabularDataSupport

instance.

- isEmpty

```java
public boolean isEmpty()
```

Returns

true

if this

TabularDataSupport

instance contains no rows.

**Specified by:** isEmpty

in interface

Map

<

Object

,​

Object

>
**Specified by:** isEmpty

in interface

TabularData
**Returns:** true

if this

TabularDataSupport

instance contains no rows.

- keySet

```java
public
Set
<
Object
> keySet()
```

Returns a set view of the keys contained in the underlying map of this

TabularDataSupport

instance used to index the rows.
Each key contained in this

Set

is an unmodifiable

List<?>

so the returned set view is a

Set<List<?>>

but is declared as a

Set<Object>

for compatibility reasons.
The set is backed by the underlying map of this

TabularDataSupport

instance, so changes to the

TabularDataSupport

instance are reflected in the
set, and vice-versa.

The set supports element removal, which removes the corresponding
row from this

TabularDataSupport

instance, via the

Iterator.remove()

,

Set.remove(java.lang.Object)

,

Set.removeAll(java.util.Collection<?>)

,

Set.retainAll(java.util.Collection<?>)

, and

Set.clear()

operations. It does
not support the

Set.add(E)

or

Set.addAll(java.util.Collection<? extends E>)

operations.

**Specified by:** keySet

in interface

Map

<

Object

,​

Object

>
**Specified by:** keySet

in interface

TabularData
**Returns:** a set view (

Set<List<?>>

) of the keys used to index
the rows of this

TabularDataSupport

instance.

- values

```java
public
Collection
<
Object
> values()
```

Returns a collection view of the rows contained in this

TabularDataSupport

instance. The returned

Collection

is a

Collection<CompositeData>

but is declared as a

Collection<Object>

for compatibility reasons.
The returned collection can be used to iterate over the values.
The collection is backed by the underlying map, so changes to the

TabularDataSupport

instance are reflected in the collection,
and vice-versa.

The collection supports element removal, which removes the corresponding
index to row mapping from this

TabularDataSupport

instance, via
the

Iterator.remove()

,

Collection.remove(java.lang.Object)

,

Collection.removeAll(java.util.Collection<?>)

,

Collection.retainAll(java.util.Collection<?>)

,
and

Collection.clear()

operations. It does not support
the

Collection.add(E)

or

Collection.addAll(java.util.Collection<? extends E>)

operations.

**Specified by:** values

in interface

Map

<

Object

,​

Object

>
**Specified by:** values

in interface

TabularData
**Returns:** a collection view (

Collection<CompositeData>

) of
the values contained in this

TabularDataSupport

instance.

- entrySet

```java
public
Set
<
Map.Entry
<
Object
,​
Object
>> entrySet()
```

Returns a collection view of the index to row mappings
contained in this

TabularDataSupport

instance.
Each element in the returned collection is
a

Map.Entry<List<?>,CompositeData>

but
is declared as a

Map.Entry<Object,Object>

for compatibility reasons. Each of the map entry
keys is an unmodifiable

List<?>

.
The collection is backed by the underlying map of this

TabularDataSupport

instance, so changes to the

TabularDataSupport

instance are reflected in
the collection, and vice-versa.
The collection supports element removal, which removes
the corresponding mapping from the map, via the

Iterator.remove()

,

Collection.remove(java.lang.Object)

,

Collection.removeAll(java.util.Collection<?>)

,

Collection.retainAll(java.util.Collection<?>)

,
and

Collection.clear()

operations. It does not support
the

Collection.add(E)

or

Collection.addAll(java.util.Collection<? extends E>)

operations.

IMPORTANT NOTICE

: Do not use the

setValue

method of the

Map.Entry

elements contained in the returned collection view.
Doing so would corrupt the index to row mappings contained in this

TabularDataSupport

instance.

**Specified by:** entrySet

in interface

Map

<

Object

,​

Object

>
**Returns:** a collection view (

Set<Map.Entry<List<?>,CompositeData>>

)
of the mappings contained in this map.
**See Also:** Map.Entry

- clone

```java
public
Object
clone()
```

Returns a clone of this

TabularDataSupport

instance:
the clone is obtained by calling

super.clone()

, and then cloning the underlying map.
Only a shallow clone of the underlying map is made, i.e.
no cloning of the indexes and row values is made as they are immutable.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

TabularDataSupport

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

TabularData

interface,
- their tabular types are equal
- their contents (ie all CompositeData values) are equal.

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

TabularData

interface.

**Specified by:** equals

in interface

Map

<

Object

,​

Object

>
**Specified by:** equals

in interface

TabularData
**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

TabularDataSupport

instance;
**Returns:** true

if the specified object is equal to this

TabularDataSupport

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

TabularDataSupport

instance.

The hash code of a

TabularDataSupport

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

tabular type

and its content, where the content is defined as all the CompositeData values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

TabularDataSupport

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing the

TabularData

interface
may be equal to this

TabularDataSupport

instance as defined by

equals(java.lang.Object)

,
but may have a different hash code if it is calculated differently.

**Specified by:** hashCode

in interface

Map

<

Object

,​

Object

>
**Specified by:** hashCode

in interface

TabularData
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

TabularDataSupport

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this

TabularDataSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.TabularDataSupport

),
the string representation of the tabular type of this instance, and the string representation of the contents
(ie list the key=value mappings as returned by a call to

dataMap.

toString()

).

**Specified by:** toString

in interface

TabularData
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

TabularDataSupport

instance

Constructor Detail

- TabularDataSupport

```java
public TabularDataSupport​(
TabularType
tabularType)
```

Creates an empty

TabularDataSupport

instance
whose open-type is

tabularType

,
and whose underlying

HashMap

has a default
initial capacity (101) and default load factor (0.75).

This constructor simply calls

this(tabularType, 101, 0.75f);

**Parameters:** tabularType

- the

tabular type

describing this

TabularData

instance; cannot be null.
**Throws:** IllegalArgumentException

- if the tabular type is null.

- TabularDataSupport

```java
public TabularDataSupport​(
TabularType
tabularType,
int initialCapacity,
float loadFactor)
```

Creates an empty

TabularDataSupport

instance whose open-type is

tabularType

,
and whose underlying

HashMap

has the specified initial capacity and load factor.

**Parameters:** tabularType

- the

tabular type

describing this

TabularData

instance;
cannot be null.
**Parameters:** initialCapacity

- the initial capacity of the HashMap.
**Parameters:** loadFactor

- the load factor of the HashMap
**Throws:** IllegalArgumentException

- if the initial capacity is less than zero,
or the load factor is nonpositive,
or the tabular type is null.

---

#### Constructor Detail

TabularDataSupport

```java
public TabularDataSupport​(
TabularType
tabularType)
```

Creates an empty

TabularDataSupport

instance
whose open-type is

tabularType

,
and whose underlying

HashMap

has a default
initial capacity (101) and default load factor (0.75).

This constructor simply calls

this(tabularType, 101, 0.75f);

**Parameters:** tabularType

- the

tabular type

describing this

TabularData

instance; cannot be null.
**Throws:** IllegalArgumentException

- if the tabular type is null.

---

#### TabularDataSupport

public TabularDataSupport​(

TabularType

tabularType)

Creates an empty

TabularDataSupport

instance
whose open-type is

tabularType

,
and whose underlying

HashMap

has a default
initial capacity (101) and default load factor (0.75).

This constructor simply calls

this(tabularType, 101, 0.75f);

This constructor simply calls

this(tabularType, 101, 0.75f);

TabularDataSupport

```java
public TabularDataSupport​(
TabularType
tabularType,
int initialCapacity,
float loadFactor)
```

Creates an empty

TabularDataSupport

instance whose open-type is

tabularType

,
and whose underlying

HashMap

has the specified initial capacity and load factor.

**Parameters:** tabularType

- the

tabular type

describing this

TabularData

instance;
cannot be null.
**Parameters:** initialCapacity

- the initial capacity of the HashMap.
**Parameters:** loadFactor

- the load factor of the HashMap
**Throws:** IllegalArgumentException

- if the initial capacity is less than zero,
or the load factor is nonpositive,
or the tabular type is null.

---

#### TabularDataSupport

public TabularDataSupport​(

TabularType

tabularType,
int initialCapacity,
float loadFactor)

Creates an empty

TabularDataSupport

instance whose open-type is

tabularType

,
and whose underlying

HashMap

has the specified initial capacity and load factor.

Method Detail

- getTabularType

```java
public
TabularType
getTabularType()
```

Returns the

tabular type

describing this

TabularData

instance.

**Specified by:** getTabularType

in interface

TabularData
**Returns:** the tabular type.

- calculateIndex

```java
public
Object
[] calculateIndex​(
CompositeData
value)
```

Calculates the index that would be used in this

TabularData

instance to refer
to the specified composite data

value

parameter if it were added to this instance.
This method checks for the type validity of the specified

value

,
but does not check if the calculated index is already used
to refer to a value in this

TabularData

instance.

**Specified by:** calculateIndex

in interface

TabularData
**Parameters:** value

- the composite data value whose index in this

TabularData

instance is to be calculated;
must be of the same composite type as this instance's row type;
must not be null.
**Returns:** the index that the specified

value

would have in this

TabularData

instance.
**Throws:** NullPointerException

- if

value

is

null

.
**Throws:** InvalidOpenTypeException

- if

value

does not conform to this

TabularData

instance's
row type definition.

- containsKey

```java
public boolean containsKey​(
Object
key)
```

Returns

true

if and only if this

TabularData

instance contains a

CompositeData

value
(ie a row) whose index is the specified

key

. If

key

cannot be cast to a one dimension array
of Object instances, this method simply returns

false

; otherwise it returns the result of the call to

this.containsKey((Object[]) key)

.

**Specified by:** containsKey

in interface

Map

<

Object

,​

Object

>
**Parameters:** key

- the index value whose presence in this

TabularData

instance is to be tested.
**Returns:** true

if this

TabularData

indexes a row value with the specified key.

- containsKey

```java
public boolean containsKey​(
Object
[] key)
```

Returns

true

if and only if this

TabularData

instance contains a

CompositeData

value
(ie a row) whose index is the specified

key

. If

key

is

null

or does not conform to
this

TabularData

instance's

TabularType

definition, this method simply returns

false

.

**Specified by:** containsKey

in interface

TabularData
**Parameters:** key

- the index value whose presence in this

TabularData

instance is to be tested.
**Returns:** true

if this

TabularData

indexes a row value with the specified key.

- containsValue

```java
public boolean containsValue​(
CompositeData
value)
```

Returns

true

if and only if this

TabularData

instance contains the specified

CompositeData

value. If

value

is

null

or does not conform to
this

TabularData

instance's row type definition, this method simply returns

false

.

**Specified by:** containsValue

in interface

TabularData
**Parameters:** value

- the row value whose presence in this

TabularData

instance is to be tested.
**Returns:** true

if this

TabularData

instance contains the specified row value.

- containsValue

```java
public boolean containsValue​(
Object
value)
```

Returns

true

if and only if this

TabularData

instance contains the specified
value.

**Specified by:** containsValue

in interface

Map

<

Object

,​

Object

>
**Parameters:** value

- the row value whose presence in this

TabularData

instance is to be tested.
**Returns:** true

if this

TabularData

instance contains the specified row value.

- get

```java
public
Object
get​(
Object
key)
```

This method simply calls

get((Object[]) key)

.

**Specified by:** get

in interface

Map

<

Object

,​

Object

>
**Parameters:** key

- the key whose associated value is to be returned
**Returns:** the value to which the specified key is mapped, or

null

if this map contains no mapping for the key
**Throws:** NullPointerException

- if the

key

is

null
**Throws:** ClassCastException

- if the

key

is not of the type

Object[]
**Throws:** InvalidKeyException

- if the

key

does not conform
to this

TabularData

instance's

TabularType

definition

- get

```java
public
CompositeData
get​(
Object
[] key)
```

Returns the

CompositeData

value whose index is

key

, or

null

if there is no value mapping
to

key

, in this

TabularData

instance.

**Specified by:** get

in interface

TabularData
**Parameters:** key

- the index of the value to get in this

TabularData

instance; must be valid with this

TabularData

instance's row type definition; must not
be null.
**Returns:** the value corresponding to

key

.
**Throws:** NullPointerException

- if the

key

is

null
**Throws:** InvalidKeyException

- if the

key

does not conform
to this

TabularData

instance's

TabularType

type definition.

- put

```java
public
Object
put​(
Object
key,

Object
value)
```

This method simply calls

put((CompositeData) value)

and
therefore ignores its

key

parameter which can be

null

.

**Specified by:** put

in interface

Map

<

Object

,​

Object

>
**Parameters:** key

- an ignored parameter.
**Parameters:** value

- the

CompositeData

to put.
**Returns:** the value which is put
**Throws:** NullPointerException

- if the

value

is

null
**Throws:** ClassCastException

- if the

value

is not of
the type

CompositeData
**Throws:** InvalidOpenTypeException

- if the

value

does
not conform to this

TabularData

instance's

TabularType

definition
**Throws:** KeyAlreadyExistsException

- if the key for the

value

parameter, calculated according to this

TabularData

instance's

TabularType

definition
already maps to an existing value

- remove

```java
public
Object
remove​(
Object
key)
```

This method simply calls

remove((Object[]) key)

.

**Specified by:** remove

in interface

Map

<

Object

,​

Object

>
**Parameters:** key

- an

Object[]

representing the key to remove.
**Returns:** previous value associated with specified key, or

null

if there was no mapping for key.
**Throws:** NullPointerException

- if the

key

is

null
**Throws:** ClassCastException

- if the

key

is not of the type

Object[]
**Throws:** InvalidKeyException

- if the

key

does not conform to this

TabularData

instance's

TabularType

definition

- remove

```java
public
CompositeData
remove​(
Object
[] key)
```

Removes the

CompositeData

value whose index is

key

from this

TabularData

instance,
and returns the removed value, or returns

null

if there is no value whose index is

key

.

**Specified by:** remove

in interface

TabularData
**Parameters:** key

- the index of the value to get in this

TabularData

instance;
must be valid with this

TabularData

instance's row type definition;
must not be null.
**Returns:** previous value associated with specified key, or

null

if there was no mapping for key.
**Throws:** NullPointerException

- if the

key

is

null
**Throws:** InvalidKeyException

- if the

key

does not conform to this

TabularData

instance's

TabularType

definition

- putAll

```java
public void putAll​(
Map
<?,​?> t)
```

Add all the values contained in the specified map

t

to this

TabularData

instance. This method converts
the collection of values contained in this map into an array of

CompositeData

values, if possible, and then call the
method

putAll(CompositeData[])

. Note that the keys
used in the specified map

t

are ignored. This method
allows, for example to add the content of another

TabularData

instance with the same row type (but
possibly different index names) into this instance.

**Specified by:** putAll

in interface

Map

<

Object

,​

Object

>
**Parameters:** t

- the map whose values are to be added as new rows to
this

TabularData

instance; if

t

is

null

or empty, this method returns without doing
anything.
**Throws:** NullPointerException

- if a value in

t

is

null

.
**Throws:** ClassCastException

- if a value in

t

is not an
instance of

CompositeData

.
**Throws:** InvalidOpenTypeException

- if a value in

t

does not conform to this

TabularData

instance's row
type definition.
**Throws:** KeyAlreadyExistsException

- if the index for a value in

t

, calculated according to this

TabularData

instance's

TabularType

definition
already maps to an existing value in this instance, or two
values in

t

have the same index.

- putAll

```java
public void putAll​(
CompositeData
[] values)
```

Add all the elements in

values

to this

TabularData

instance. If any element in

values

does not satisfy the constraints defined in

put

, or if any two
elements in

values

have the same index calculated
according to this

TabularData

instance's

TabularType

definition, then an exception describing
the failure is thrown and no element of

values

is
added, thus leaving this

TabularData

instance
unchanged.

**Specified by:** putAll

in interface

TabularData
**Parameters:** values

- the array of composite data values to be added as
new rows to this

TabularData

instance; if

values

is

null

or empty, this method
returns without doing anything.
**Throws:** NullPointerException

- if an element of

values

is

null
**Throws:** InvalidOpenTypeException

- if an element of

values

does not conform to this

TabularData

instance's row type definition (ie its

TabularType

definition)
**Throws:** KeyAlreadyExistsException

- if the index for an element
of

values

, calculated according to this

TabularData

instance's

TabularType

definition
already maps to an existing value in this instance, or two
elements of

values

have the same index

- clear

```java
public void clear()
```

Removes all rows from this

TabularDataSupport

instance.

**Specified by:** clear

in interface

Map

<

Object

,​

Object

>
**Specified by:** clear

in interface

TabularData

- size

```java
public int size()
```

Returns the number of rows in this

TabularDataSupport

instance.

**Specified by:** size

in interface

Map

<

Object

,​

Object

>
**Specified by:** size

in interface

TabularData
**Returns:** the number of rows in this

TabularDataSupport

instance.

- isEmpty

```java
public boolean isEmpty()
```

Returns

true

if this

TabularDataSupport

instance contains no rows.

**Specified by:** isEmpty

in interface

Map

<

Object

,​

Object

>
**Specified by:** isEmpty

in interface

TabularData
**Returns:** true

if this

TabularDataSupport

instance contains no rows.

- keySet

```java
public
Set
<
Object
> keySet()
```

Returns a set view of the keys contained in the underlying map of this

TabularDataSupport

instance used to index the rows.
Each key contained in this

Set

is an unmodifiable

List<?>

so the returned set view is a

Set<List<?>>

but is declared as a

Set<Object>

for compatibility reasons.
The set is backed by the underlying map of this

TabularDataSupport

instance, so changes to the

TabularDataSupport

instance are reflected in the
set, and vice-versa.

The set supports element removal, which removes the corresponding
row from this

TabularDataSupport

instance, via the

Iterator.remove()

,

Set.remove(java.lang.Object)

,

Set.removeAll(java.util.Collection<?>)

,

Set.retainAll(java.util.Collection<?>)

, and

Set.clear()

operations. It does
not support the

Set.add(E)

or

Set.addAll(java.util.Collection<? extends E>)

operations.

**Specified by:** keySet

in interface

Map

<

Object

,​

Object

>
**Specified by:** keySet

in interface

TabularData
**Returns:** a set view (

Set<List<?>>

) of the keys used to index
the rows of this

TabularDataSupport

instance.

- values

```java
public
Collection
<
Object
> values()
```

Returns a collection view of the rows contained in this

TabularDataSupport

instance. The returned

Collection

is a

Collection<CompositeData>

but is declared as a

Collection<Object>

for compatibility reasons.
The returned collection can be used to iterate over the values.
The collection is backed by the underlying map, so changes to the

TabularDataSupport

instance are reflected in the collection,
and vice-versa.

The collection supports element removal, which removes the corresponding
index to row mapping from this

TabularDataSupport

instance, via
the

Iterator.remove()

,

Collection.remove(java.lang.Object)

,

Collection.removeAll(java.util.Collection<?>)

,

Collection.retainAll(java.util.Collection<?>)

,
and

Collection.clear()

operations. It does not support
the

Collection.add(E)

or

Collection.addAll(java.util.Collection<? extends E>)

operations.

**Specified by:** values

in interface

Map

<

Object

,​

Object

>
**Specified by:** values

in interface

TabularData
**Returns:** a collection view (

Collection<CompositeData>

) of
the values contained in this

TabularDataSupport

instance.

- entrySet

```java
public
Set
<
Map.Entry
<
Object
,​
Object
>> entrySet()
```

Returns a collection view of the index to row mappings
contained in this

TabularDataSupport

instance.
Each element in the returned collection is
a

Map.Entry<List<?>,CompositeData>

but
is declared as a

Map.Entry<Object,Object>

for compatibility reasons. Each of the map entry
keys is an unmodifiable

List<?>

.
The collection is backed by the underlying map of this

TabularDataSupport

instance, so changes to the

TabularDataSupport

instance are reflected in
the collection, and vice-versa.
The collection supports element removal, which removes
the corresponding mapping from the map, via the

Iterator.remove()

,

Collection.remove(java.lang.Object)

,

Collection.removeAll(java.util.Collection<?>)

,

Collection.retainAll(java.util.Collection<?>)

,
and

Collection.clear()

operations. It does not support
the

Collection.add(E)

or

Collection.addAll(java.util.Collection<? extends E>)

operations.

IMPORTANT NOTICE

: Do not use the

setValue

method of the

Map.Entry

elements contained in the returned collection view.
Doing so would corrupt the index to row mappings contained in this

TabularDataSupport

instance.

**Specified by:** entrySet

in interface

Map

<

Object

,​

Object

>
**Returns:** a collection view (

Set<Map.Entry<List<?>,CompositeData>>

)
of the mappings contained in this map.
**See Also:** Map.Entry

- clone

```java
public
Object
clone()
```

Returns a clone of this

TabularDataSupport

instance:
the clone is obtained by calling

super.clone()

, and then cloning the underlying map.
Only a shallow clone of the underlying map is made, i.e.
no cloning of the indexes and row values is made as they are immutable.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

TabularDataSupport

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

TabularData

interface,
- their tabular types are equal
- their contents (ie all CompositeData values) are equal.

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

TabularData

interface.

**Specified by:** equals

in interface

Map

<

Object

,​

Object

>
**Specified by:** equals

in interface

TabularData
**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

TabularDataSupport

instance;
**Returns:** true

if the specified object is equal to this

TabularDataSupport

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

TabularDataSupport

instance.

The hash code of a

TabularDataSupport

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

tabular type

and its content, where the content is defined as all the CompositeData values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

TabularDataSupport

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing the

TabularData

interface
may be equal to this

TabularDataSupport

instance as defined by

equals(java.lang.Object)

,
but may have a different hash code if it is calculated differently.

**Specified by:** hashCode

in interface

Map

<

Object

,​

Object

>
**Specified by:** hashCode

in interface

TabularData
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

TabularDataSupport

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this

TabularDataSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.TabularDataSupport

),
the string representation of the tabular type of this instance, and the string representation of the contents
(ie list the key=value mappings as returned by a call to

dataMap.

toString()

).

**Specified by:** toString

in interface

TabularData
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

TabularDataSupport

instance

---

#### Method Detail

getTabularType

```java
public
TabularType
getTabularType()
```

Returns the

tabular type

describing this

TabularData

instance.

**Specified by:** getTabularType

in interface

TabularData
**Returns:** the tabular type.

---

#### getTabularType

public

TabularType

getTabularType()

Returns the

tabular type

describing this

TabularData

instance.

calculateIndex

```java
public
Object
[] calculateIndex​(
CompositeData
value)
```

Calculates the index that would be used in this

TabularData

instance to refer
to the specified composite data

value

parameter if it were added to this instance.
This method checks for the type validity of the specified

value

,
but does not check if the calculated index is already used
to refer to a value in this

TabularData

instance.

**Specified by:** calculateIndex

in interface

TabularData
**Parameters:** value

- the composite data value whose index in this

TabularData

instance is to be calculated;
must be of the same composite type as this instance's row type;
must not be null.
**Returns:** the index that the specified

value

would have in this

TabularData

instance.
**Throws:** NullPointerException

- if

value

is

null

.
**Throws:** InvalidOpenTypeException

- if

value

does not conform to this

TabularData

instance's
row type definition.

---

#### calculateIndex

public

Object

[] calculateIndex​(

CompositeData

value)

Calculates the index that would be used in this

TabularData

instance to refer
to the specified composite data

value

parameter if it were added to this instance.
This method checks for the type validity of the specified

value

,
but does not check if the calculated index is already used
to refer to a value in this

TabularData

instance.

containsKey

```java
public boolean containsKey​(
Object
key)
```

Returns

true

if and only if this

TabularData

instance contains a

CompositeData

value
(ie a row) whose index is the specified

key

. If

key

cannot be cast to a one dimension array
of Object instances, this method simply returns

false

; otherwise it returns the result of the call to

this.containsKey((Object[]) key)

.

**Specified by:** containsKey

in interface

Map

<

Object

,​

Object

>
**Parameters:** key

- the index value whose presence in this

TabularData

instance is to be tested.
**Returns:** true

if this

TabularData

indexes a row value with the specified key.

---

#### containsKey

public boolean containsKey​(

Object

key)

Returns

true

if and only if this

TabularData

instance contains a

CompositeData

value
(ie a row) whose index is the specified

key

. If

key

cannot be cast to a one dimension array
of Object instances, this method simply returns

false

; otherwise it returns the result of the call to

this.containsKey((Object[]) key)

.

containsKey

```java
public boolean containsKey​(
Object
[] key)
```

Returns

true

if and only if this

TabularData

instance contains a

CompositeData

value
(ie a row) whose index is the specified

key

. If

key

is

null

or does not conform to
this

TabularData

instance's

TabularType

definition, this method simply returns

false

.

**Specified by:** containsKey

in interface

TabularData
**Parameters:** key

- the index value whose presence in this

TabularData

instance is to be tested.
**Returns:** true

if this

TabularData

indexes a row value with the specified key.

---

#### containsKey

public boolean containsKey​(

Object

[] key)

Returns

true

if and only if this

TabularData

instance contains a

CompositeData

value
(ie a row) whose index is the specified

key

. If

key

is

null

or does not conform to
this

TabularData

instance's

TabularType

definition, this method simply returns

false

.

containsValue

```java
public boolean containsValue​(
CompositeData
value)
```

Returns

true

if and only if this

TabularData

instance contains the specified

CompositeData

value. If

value

is

null

or does not conform to
this

TabularData

instance's row type definition, this method simply returns

false

.

**Specified by:** containsValue

in interface

TabularData
**Parameters:** value

- the row value whose presence in this

TabularData

instance is to be tested.
**Returns:** true

if this

TabularData

instance contains the specified row value.

---

#### containsValue

public boolean containsValue​(

CompositeData

value)

Returns

true

if and only if this

TabularData

instance contains the specified

CompositeData

value. If

value

is

null

or does not conform to
this

TabularData

instance's row type definition, this method simply returns

false

.

containsValue

```java
public boolean containsValue​(
Object
value)
```

Returns

true

if and only if this

TabularData

instance contains the specified
value.

**Specified by:** containsValue

in interface

Map

<

Object

,​

Object

>
**Parameters:** value

- the row value whose presence in this

TabularData

instance is to be tested.
**Returns:** true

if this

TabularData

instance contains the specified row value.

---

#### containsValue

public boolean containsValue​(

Object

value)

Returns

true

if and only if this

TabularData

instance contains the specified
value.

get

```java
public
Object
get​(
Object
key)
```

This method simply calls

get((Object[]) key)

.

**Specified by:** get

in interface

Map

<

Object

,​

Object

>
**Parameters:** key

- the key whose associated value is to be returned
**Returns:** the value to which the specified key is mapped, or

null

if this map contains no mapping for the key
**Throws:** NullPointerException

- if the

key

is

null
**Throws:** ClassCastException

- if the

key

is not of the type

Object[]
**Throws:** InvalidKeyException

- if the

key

does not conform
to this

TabularData

instance's

TabularType

definition

---

#### get

public

Object

get​(

Object

key)

This method simply calls

get((Object[]) key)

.

get

```java
public
CompositeData
get​(
Object
[] key)
```

Returns the

CompositeData

value whose index is

key

, or

null

if there is no value mapping
to

key

, in this

TabularData

instance.

**Specified by:** get

in interface

TabularData
**Parameters:** key

- the index of the value to get in this

TabularData

instance; must be valid with this

TabularData

instance's row type definition; must not
be null.
**Returns:** the value corresponding to

key

.
**Throws:** NullPointerException

- if the

key

is

null
**Throws:** InvalidKeyException

- if the

key

does not conform
to this

TabularData

instance's

TabularType

type definition.

---

#### get

public

CompositeData

get​(

Object

[] key)

Returns the

CompositeData

value whose index is

key

, or

null

if there is no value mapping
to

key

, in this

TabularData

instance.

put

```java
public
Object
put​(
Object
key,

Object
value)
```

This method simply calls

put((CompositeData) value)

and
therefore ignores its

key

parameter which can be

null

.

**Specified by:** put

in interface

Map

<

Object

,​

Object

>
**Parameters:** key

- an ignored parameter.
**Parameters:** value

- the

CompositeData

to put.
**Returns:** the value which is put
**Throws:** NullPointerException

- if the

value

is

null
**Throws:** ClassCastException

- if the

value

is not of
the type

CompositeData
**Throws:** InvalidOpenTypeException

- if the

value

does
not conform to this

TabularData

instance's

TabularType

definition
**Throws:** KeyAlreadyExistsException

- if the key for the

value

parameter, calculated according to this

TabularData

instance's

TabularType

definition
already maps to an existing value

---

#### put

public

Object

put​(

Object

key,

Object

value)

This method simply calls

put((CompositeData) value)

and
therefore ignores its

key

parameter which can be

null

.

remove

```java
public
Object
remove​(
Object
key)
```

This method simply calls

remove((Object[]) key)

.

**Specified by:** remove

in interface

Map

<

Object

,​

Object

>
**Parameters:** key

- an

Object[]

representing the key to remove.
**Returns:** previous value associated with specified key, or

null

if there was no mapping for key.
**Throws:** NullPointerException

- if the

key

is

null
**Throws:** ClassCastException

- if the

key

is not of the type

Object[]
**Throws:** InvalidKeyException

- if the

key

does not conform to this

TabularData

instance's

TabularType

definition

---

#### remove

public

Object

remove​(

Object

key)

This method simply calls

remove((Object[]) key)

.

remove

```java
public
CompositeData
remove​(
Object
[] key)
```

Removes the

CompositeData

value whose index is

key

from this

TabularData

instance,
and returns the removed value, or returns

null

if there is no value whose index is

key

.

**Specified by:** remove

in interface

TabularData
**Parameters:** key

- the index of the value to get in this

TabularData

instance;
must be valid with this

TabularData

instance's row type definition;
must not be null.
**Returns:** previous value associated with specified key, or

null

if there was no mapping for key.
**Throws:** NullPointerException

- if the

key

is

null
**Throws:** InvalidKeyException

- if the

key

does not conform to this

TabularData

instance's

TabularType

definition

---

#### remove

public

CompositeData

remove​(

Object

[] key)

Removes the

CompositeData

value whose index is

key

from this

TabularData

instance,
and returns the removed value, or returns

null

if there is no value whose index is

key

.

putAll

```java
public void putAll​(
Map
<?,​?> t)
```

Add all the values contained in the specified map

t

to this

TabularData

instance. This method converts
the collection of values contained in this map into an array of

CompositeData

values, if possible, and then call the
method

putAll(CompositeData[])

. Note that the keys
used in the specified map

t

are ignored. This method
allows, for example to add the content of another

TabularData

instance with the same row type (but
possibly different index names) into this instance.

**Specified by:** putAll

in interface

Map

<

Object

,​

Object

>
**Parameters:** t

- the map whose values are to be added as new rows to
this

TabularData

instance; if

t

is

null

or empty, this method returns without doing
anything.
**Throws:** NullPointerException

- if a value in

t

is

null

.
**Throws:** ClassCastException

- if a value in

t

is not an
instance of

CompositeData

.
**Throws:** InvalidOpenTypeException

- if a value in

t

does not conform to this

TabularData

instance's row
type definition.
**Throws:** KeyAlreadyExistsException

- if the index for a value in

t

, calculated according to this

TabularData

instance's

TabularType

definition
already maps to an existing value in this instance, or two
values in

t

have the same index.

---

#### putAll

public void putAll​(

Map

<?,​?> t)

Add all the values contained in the specified map

t

to this

TabularData

instance. This method converts
the collection of values contained in this map into an array of

CompositeData

values, if possible, and then call the
method

putAll(CompositeData[])

. Note that the keys
used in the specified map

t

are ignored. This method
allows, for example to add the content of another

TabularData

instance with the same row type (but
possibly different index names) into this instance.

putAll

```java
public void putAll​(
CompositeData
[] values)
```

Add all the elements in

values

to this

TabularData

instance. If any element in

values

does not satisfy the constraints defined in

put

, or if any two
elements in

values

have the same index calculated
according to this

TabularData

instance's

TabularType

definition, then an exception describing
the failure is thrown and no element of

values

is
added, thus leaving this

TabularData

instance
unchanged.

**Specified by:** putAll

in interface

TabularData
**Parameters:** values

- the array of composite data values to be added as
new rows to this

TabularData

instance; if

values

is

null

or empty, this method
returns without doing anything.
**Throws:** NullPointerException

- if an element of

values

is

null
**Throws:** InvalidOpenTypeException

- if an element of

values

does not conform to this

TabularData

instance's row type definition (ie its

TabularType

definition)
**Throws:** KeyAlreadyExistsException

- if the index for an element
of

values

, calculated according to this

TabularData

instance's

TabularType

definition
already maps to an existing value in this instance, or two
elements of

values

have the same index

---

#### putAll

public void putAll​(

CompositeData

[] values)

Add all the elements in

values

to this

TabularData

instance. If any element in

values

does not satisfy the constraints defined in

put

, or if any two
elements in

values

have the same index calculated
according to this

TabularData

instance's

TabularType

definition, then an exception describing
the failure is thrown and no element of

values

is
added, thus leaving this

TabularData

instance
unchanged.

clear

```java
public void clear()
```

Removes all rows from this

TabularDataSupport

instance.

**Specified by:** clear

in interface

Map

<

Object

,​

Object

>
**Specified by:** clear

in interface

TabularData

---

#### clear

public void clear()

Removes all rows from this

TabularDataSupport

instance.

size

```java
public int size()
```

Returns the number of rows in this

TabularDataSupport

instance.

**Specified by:** size

in interface

Map

<

Object

,​

Object

>
**Specified by:** size

in interface

TabularData
**Returns:** the number of rows in this

TabularDataSupport

instance.

---

#### size

public int size()

Returns the number of rows in this

TabularDataSupport

instance.

isEmpty

```java
public boolean isEmpty()
```

Returns

true

if this

TabularDataSupport

instance contains no rows.

**Specified by:** isEmpty

in interface

Map

<

Object

,​

Object

>
**Specified by:** isEmpty

in interface

TabularData
**Returns:** true

if this

TabularDataSupport

instance contains no rows.

---

#### isEmpty

public boolean isEmpty()

Returns

true

if this

TabularDataSupport

instance contains no rows.

keySet

```java
public
Set
<
Object
> keySet()
```

Returns a set view of the keys contained in the underlying map of this

TabularDataSupport

instance used to index the rows.
Each key contained in this

Set

is an unmodifiable

List<?>

so the returned set view is a

Set<List<?>>

but is declared as a

Set<Object>

for compatibility reasons.
The set is backed by the underlying map of this

TabularDataSupport

instance, so changes to the

TabularDataSupport

instance are reflected in the
set, and vice-versa.

The set supports element removal, which removes the corresponding
row from this

TabularDataSupport

instance, via the

Iterator.remove()

,

Set.remove(java.lang.Object)

,

Set.removeAll(java.util.Collection<?>)

,

Set.retainAll(java.util.Collection<?>)

, and

Set.clear()

operations. It does
not support the

Set.add(E)

or

Set.addAll(java.util.Collection<? extends E>)

operations.

**Specified by:** keySet

in interface

Map

<

Object

,​

Object

>
**Specified by:** keySet

in interface

TabularData
**Returns:** a set view (

Set<List<?>>

) of the keys used to index
the rows of this

TabularDataSupport

instance.

---

#### keySet

public

Set

<

Object

> keySet()

Returns a set view of the keys contained in the underlying map of this

TabularDataSupport

instance used to index the rows.
Each key contained in this

Set

is an unmodifiable

List<?>

so the returned set view is a

Set<List<?>>

but is declared as a

Set<Object>

for compatibility reasons.
The set is backed by the underlying map of this

TabularDataSupport

instance, so changes to the

TabularDataSupport

instance are reflected in the
set, and vice-versa.

The set supports element removal, which removes the corresponding
row from this

TabularDataSupport

instance, via the

Iterator.remove()

,

Set.remove(java.lang.Object)

,

Set.removeAll(java.util.Collection<?>)

,

Set.retainAll(java.util.Collection<?>)

, and

Set.clear()

operations. It does
not support the

Set.add(E)

or

Set.addAll(java.util.Collection<? extends E>)

operations.

values

```java
public
Collection
<
Object
> values()
```

Returns a collection view of the rows contained in this

TabularDataSupport

instance. The returned

Collection

is a

Collection<CompositeData>

but is declared as a

Collection<Object>

for compatibility reasons.
The returned collection can be used to iterate over the values.
The collection is backed by the underlying map, so changes to the

TabularDataSupport

instance are reflected in the collection,
and vice-versa.

The collection supports element removal, which removes the corresponding
index to row mapping from this

TabularDataSupport

instance, via
the

Iterator.remove()

,

Collection.remove(java.lang.Object)

,

Collection.removeAll(java.util.Collection<?>)

,

Collection.retainAll(java.util.Collection<?>)

,
and

Collection.clear()

operations. It does not support
the

Collection.add(E)

or

Collection.addAll(java.util.Collection<? extends E>)

operations.

**Specified by:** values

in interface

Map

<

Object

,​

Object

>
**Specified by:** values

in interface

TabularData
**Returns:** a collection view (

Collection<CompositeData>

) of
the values contained in this

TabularDataSupport

instance.

---

#### values

public

Collection

<

Object

> values()

Returns a collection view of the rows contained in this

TabularDataSupport

instance. The returned

Collection

is a

Collection<CompositeData>

but is declared as a

Collection<Object>

for compatibility reasons.
The returned collection can be used to iterate over the values.
The collection is backed by the underlying map, so changes to the

TabularDataSupport

instance are reflected in the collection,
and vice-versa.

The collection supports element removal, which removes the corresponding
index to row mapping from this

TabularDataSupport

instance, via
the

Iterator.remove()

,

Collection.remove(java.lang.Object)

,

Collection.removeAll(java.util.Collection<?>)

,

Collection.retainAll(java.util.Collection<?>)

,
and

Collection.clear()

operations. It does not support
the

Collection.add(E)

or

Collection.addAll(java.util.Collection<? extends E>)

operations.

entrySet

```java
public
Set
<
Map.Entry
<
Object
,​
Object
>> entrySet()
```

Returns a collection view of the index to row mappings
contained in this

TabularDataSupport

instance.
Each element in the returned collection is
a

Map.Entry<List<?>,CompositeData>

but
is declared as a

Map.Entry<Object,Object>

for compatibility reasons. Each of the map entry
keys is an unmodifiable

List<?>

.
The collection is backed by the underlying map of this

TabularDataSupport

instance, so changes to the

TabularDataSupport

instance are reflected in
the collection, and vice-versa.
The collection supports element removal, which removes
the corresponding mapping from the map, via the

Iterator.remove()

,

Collection.remove(java.lang.Object)

,

Collection.removeAll(java.util.Collection<?>)

,

Collection.retainAll(java.util.Collection<?>)

,
and

Collection.clear()

operations. It does not support
the

Collection.add(E)

or

Collection.addAll(java.util.Collection<? extends E>)

operations.

IMPORTANT NOTICE

: Do not use the

setValue

method of the

Map.Entry

elements contained in the returned collection view.
Doing so would corrupt the index to row mappings contained in this

TabularDataSupport

instance.

**Specified by:** entrySet

in interface

Map

<

Object

,​

Object

>
**Returns:** a collection view (

Set<Map.Entry<List<?>,CompositeData>>

)
of the mappings contained in this map.
**See Also:** Map.Entry

---

#### entrySet

public

Set

<

Map.Entry

<

Object

,​

Object

>> entrySet()

Returns a collection view of the index to row mappings
contained in this

TabularDataSupport

instance.
Each element in the returned collection is
a

Map.Entry<List<?>,CompositeData>

but
is declared as a

Map.Entry<Object,Object>

for compatibility reasons. Each of the map entry
keys is an unmodifiable

List<?>

.
The collection is backed by the underlying map of this

TabularDataSupport

instance, so changes to the

TabularDataSupport

instance are reflected in
the collection, and vice-versa.
The collection supports element removal, which removes
the corresponding mapping from the map, via the

Iterator.remove()

,

Collection.remove(java.lang.Object)

,

Collection.removeAll(java.util.Collection<?>)

,

Collection.retainAll(java.util.Collection<?>)

,
and

Collection.clear()

operations. It does not support
the

Collection.add(E)

or

Collection.addAll(java.util.Collection<? extends E>)

operations.

IMPORTANT NOTICE

: Do not use the

setValue

method of the

Map.Entry

elements contained in the returned collection view.
Doing so would corrupt the index to row mappings contained in this

TabularDataSupport

instance.

IMPORTANT NOTICE

: Do not use the

setValue

method of the

Map.Entry

elements contained in the returned collection view.
Doing so would corrupt the index to row mappings contained in this

TabularDataSupport

instance.

clone

```java
public
Object
clone()
```

Returns a clone of this

TabularDataSupport

instance:
the clone is obtained by calling

super.clone()

, and then cloning the underlying map.
Only a shallow clone of the underlying map is made, i.e.
no cloning of the indexes and row values is made as they are immutable.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a clone of this

TabularDataSupport

instance:
the clone is obtained by calling

super.clone()

, and then cloning the underlying map.
Only a shallow clone of the underlying map is made, i.e.
no cloning of the indexes and row values is made as they are immutable.

equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

TabularDataSupport

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

TabularData

interface,
- their tabular types are equal
- their contents (ie all CompositeData values) are equal.

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

TabularData

interface.

**Specified by:** equals

in interface

Map

<

Object

,​

Object

>
**Specified by:** equals

in interface

TabularData
**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

TabularDataSupport

instance;
**Returns:** true

if the specified object is equal to this

TabularDataSupport

instance.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares the specified

obj

parameter with this

TabularDataSupport

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

TabularData

interface,
- their tabular types are equal
- their contents (ie all CompositeData values) are equal.

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

TabularData

interface.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

TabularData

interface,
- their tabular types are equal
- their contents (ie all CompositeData values) are equal.

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

TabularData

interface.

obj

is non null,

obj

also implements the

TabularData

interface,

their tabular types are equal

their contents (ie all CompositeData values) are equal.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this

TabularDataSupport

instance.

The hash code of a

TabularDataSupport

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

tabular type

and its content, where the content is defined as all the CompositeData values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

TabularDataSupport

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing the

TabularData

interface
may be equal to this

TabularDataSupport

instance as defined by

equals(java.lang.Object)

,
but may have a different hash code if it is calculated differently.

**Specified by:** hashCode

in interface

Map

<

Object

,​

Object

>
**Specified by:** hashCode

in interface

TabularData
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

TabularDataSupport

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this

TabularDataSupport

instance.

The hash code of a

TabularDataSupport

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

tabular type

and its content, where the content is defined as all the CompositeData values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

TabularDataSupport

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing the

TabularData

interface
may be equal to this

TabularDataSupport

instance as defined by

equals(java.lang.Object)

,
but may have a different hash code if it is calculated differently.

The hash code of a

TabularDataSupport

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

tabular type

and its content, where the content is defined as all the CompositeData values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

TabularDataSupport

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing the

TabularData

interface
may be equal to this

TabularDataSupport

instance as defined by

equals(java.lang.Object)

,
but may have a different hash code if it is calculated differently.

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

TabularDataSupport

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing the

TabularData

interface
may be equal to this

TabularDataSupport

instance as defined by

equals(java.lang.Object)

,
but may have a different hash code if it is calculated differently.

However, note that another instance of a class implementing the

TabularData

interface
may be equal to this

TabularDataSupport

instance as defined by

equals(java.lang.Object)

,
but may have a different hash code if it is calculated differently.

toString

```java
public
String
toString()
```

Returns a string representation of this

TabularDataSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.TabularDataSupport

),
the string representation of the tabular type of this instance, and the string representation of the contents
(ie list the key=value mappings as returned by a call to

dataMap.

toString()

).

**Specified by:** toString

in interface

TabularData
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

TabularDataSupport

instance

---

#### toString

public

String

toString()

Returns a string representation of this

TabularDataSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.TabularDataSupport

),
the string representation of the tabular type of this instance, and the string representation of the contents
(ie list the key=value mappings as returned by a call to

dataMap.

toString()

).

The string representation consists of the name of this class
(ie

javax.management.openmbean.TabularDataSupport

),
the string representation of the tabular type of this instance, and the string representation of the contents
(ie list the key=value mappings as returned by a call to

dataMap.

toString()

).

---

