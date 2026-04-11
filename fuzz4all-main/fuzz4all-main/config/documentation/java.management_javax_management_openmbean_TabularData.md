# Interface TabularData

**Source:** `java.management\javax\management\openmbean\TabularData.html`

### Class Description

```java
public interface
TabularData
```

The

TabularData

interface specifies the behavior of a specific type of complex

open data

objects
which represent

tabular data

structures.

**All Known Implementing Classes:** TabularDataSupport

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### TabularType
getTabularType()

Returns the

tabular type

describing this

TabularData

instance.

**Returns:**
- the tabular type.

---

#### Object
[] calculateIndex​(
CompositeData
value)

Calculates the index that would be used in this

TabularData

instance to refer to the specified
composite data

value

parameter if it were added to this instance.
This method checks for the type validity of the specified

value

,
but does not check if the calculated index is already used to refer to a value in this

TabularData

instance.

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
- InvalidOpenTypeException

- if

value

does not conform to this

TabularData

instance's
row type definition.

---

#### int size()

Returns the number of

CompositeData

values (ie the
number of rows) contained in this

TabularData

instance.

**Returns:**
- the number of values contained.

---

#### boolean isEmpty()

Returns

true

if the number of

CompositeData

values (ie the number of rows) contained in this

TabularData

instance is zero.

**Returns:**
- true if this

TabularData

is empty.

---

#### boolean containsKey​(
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

#### boolean containsValue​(
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

#### CompositeData
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

**Parameters:**
- key

- the key of the row to return.

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

does not
conform to this

TabularData

instance's *

TabularType

definition

---

#### void put​(
CompositeData
value)

Adds

value

to this

TabularData

instance.
The composite type of

value

must be the same as this
instance's row type (ie the composite type returned by

this.getTabularType().

getRowType()

), and there must not already be an existing
value in this

TabularData

instance whose index is the
same as the one calculated for the

value

to be
added. The index for

value

is calculated according
to this

TabularData

instance's

TabularType

definition (see

TabularType.

getIndexNames()

).

**Parameters:**
- value

- the composite data value to be added as a new row to this

TabularData

instance;
must be of the same composite type as this instance's row type;
must not be null.

**Throws:**
- NullPointerException

- if

value

is

null
- InvalidOpenTypeException

- if

value

does not conform to this

TabularData

instance's
row type definition.
- KeyAlreadyExistsException

- if the index for

value

, calculated according to
this

TabularData

instance's

TabularType

definition
already maps to an existing value in the underlying HashMap.

---

#### CompositeData
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

#### void putAll​(
CompositeData
[] values)

Add all the elements in

values

to this

TabularData

instance.
If any element in

values

does not satisfy the constraints defined in

put

,
or if any two elements in

values

have the same index calculated according to this

TabularData

instance's

TabularType

definition, then an exception describing the failure is thrown
and no element of

values

is added, thus leaving this

TabularData

instance unchanged.

**Parameters:**
- values

- the array of composite data values to be added as new rows to this

TabularData

instance;
if

values

is

null

or empty, this method returns without doing anything.

**Throws:**
- NullPointerException

- if an element of

values

is

null
- InvalidOpenTypeException

- if an element of

values

does not conform to
this

TabularData

instance's row type definition
- KeyAlreadyExistsException

- if the index for an element of

values

, calculated according to
this

TabularData

instance's

TabularType

definition
already maps to an existing value in this instance,
or two elements of

values

have the same index.

---

#### void clear()

Removes all

CompositeData

values (ie rows) from this

TabularData

instance.

---

#### Set
<?> keySet()

Returns a set view of the keys (ie the index values) of the

CompositeData

values (ie the rows) contained in this

TabularData

instance. The returned

Set

is a

Set<List<?>>

but is declared as a

Set<?>

for
compatibility reasons. The returned set can be used to iterate
over the keys.

**Returns:**
- a set view (

Set<List<?>>

) of the index values
used in this

TabularData

instance.

---

#### Collection
<?> values()

Returns a collection view of the

CompositeData

values
(ie the rows) contained in this

TabularData

instance.
The returned

Collection

is a

Collection<CompositeData>

but is declared as a

Collection<?>

for compatibility reasons.
The returned collection can be used to iterate over the values.

**Returns:**
- a collection view (

Collection<CompositeData>

)
of the rows contained in this

TabularData

instance.

---

#### boolean equals​(
Object
obj)

Compares the specified

obj

parameter with this

TabularData

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
- their row types are equal
- their contents (ie index to value mappings) are equal

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

TabularData

interface.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to be compared for equality with this

TabularData

instance;

**Returns:**
- true

if the specified object is equal to this

TabularData

instance.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this

TabularData

instance.

The hash code of a

TabularData

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

tabular type

and its content, where the content is defined as all the index to value mappings).

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

#### String
toString()

Returns a string representation of this

TabularData

instance.

The string representation consists of the name of the implementing class,
and the tabular type of this instance.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

TabularData

instance

---

### Additional Sections

#### Interface TabularData

**All Known Implementing Classes:** TabularDataSupport

```java
public interface
TabularData
```

The

TabularData

interface specifies the behavior of a specific type of complex

open data

objects
which represent

tabular data

structures.

**Since:** 1.5

public interface

TabularData

The

TabularData

interface specifies the behavior of a specific type of complex

open data

objects
which represent

tabular data

structures.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

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

instance to refer to the specified
composite data

value

parameter if it were added to this instance.

void

clear

()

Removes all

CompositeData

values (ie rows) from this

TabularData

instance.

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

CompositeData

value)

Returns

true

if and only if this

TabularData

instance contains the specified

CompositeData

value.

boolean

equals

​(

Object

obj)

Compares the specified

obj

parameter with this

TabularData

instance for equality.

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

TabularData

instance.

boolean

isEmpty

()

Returns

true

if the number of

CompositeData

values (ie the number of rows) contained in this

TabularData

instance is zero.

Set

<?>

keySet

()

Returns a set view of the keys (ie the index values) of the

CompositeData

values (ie the rows) contained in this

TabularData

instance.

void

put

​(

CompositeData

value)

Adds

value

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

Returns the number of

CompositeData

values (ie the
number of rows) contained in this

TabularData

instance.

String

toString

()

Returns a string representation of this

TabularData

instance.

Collection

<?>

values

()

Returns a collection view of the

CompositeData

values
(ie the rows) contained in this

TabularData

instance.

Method Summary

All Methods

Instance Methods

Abstract Methods

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

instance to refer to the specified
composite data

value

parameter if it were added to this instance.

void

clear

()

Removes all

CompositeData

values (ie rows) from this

TabularData

instance.

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

CompositeData

value)

Returns

true

if and only if this

TabularData

instance contains the specified

CompositeData

value.

boolean

equals

​(

Object

obj)

Compares the specified

obj

parameter with this

TabularData

instance for equality.

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

TabularData

instance.

boolean

isEmpty

()

Returns

true

if the number of

CompositeData

values (ie the number of rows) contained in this

TabularData

instance is zero.

Set

<?>

keySet

()

Returns a set view of the keys (ie the index values) of the

CompositeData

values (ie the rows) contained in this

TabularData

instance.

void

put

​(

CompositeData

value)

Adds

value

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

Returns the number of

CompositeData

values (ie the
number of rows) contained in this

TabularData

instance.

String

toString

()

Returns a string representation of this

TabularData

instance.

Collection

<?>

values

()

Returns a collection view of the

CompositeData

values
(ie the rows) contained in this

TabularData

instance.

---

#### Method Summary

Calculates the index that would be used in this

TabularData

instance to refer to the specified
composite data

value

parameter if it were added to this instance.

Removes all

CompositeData

values (ie rows) from this

TabularData

instance.

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

CompositeData

value.

Compares the specified

obj

parameter with this

TabularData

instance for equality.

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

TabularData

instance.

Returns

true

if the number of

CompositeData

values (ie the number of rows) contained in this

TabularData

instance is zero.

Returns a set view of the keys (ie the index values) of the

CompositeData

values (ie the rows) contained in this

TabularData

instance.

Adds

value

to this

TabularData

instance.

Add all the elements in

values

to this

TabularData

instance.

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

Returns the number of

CompositeData

values (ie the
number of rows) contained in this

TabularData

instance.

Returns a string representation of this

TabularData

instance.

Returns a collection view of the

CompositeData

values
(ie the rows) contained in this

TabularData

instance.

============ METHOD DETAIL ==========

- Method Detail

- getTabularType

```java
TabularType
getTabularType()
```

Returns the

tabular type

describing this

TabularData

instance.

**Returns:** the tabular type.

- calculateIndex

```java
Object
[] calculateIndex​(
CompositeData
value)
```

Calculates the index that would be used in this

TabularData

instance to refer to the specified
composite data

value

parameter if it were added to this instance.
This method checks for the type validity of the specified

value

,
but does not check if the calculated index is already used to refer to a value in this

TabularData

instance.

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
**Throws:** InvalidOpenTypeException

- if

value

does not conform to this

TabularData

instance's
row type definition.

- size

```java
int size()
```

Returns the number of

CompositeData

values (ie the
number of rows) contained in this

TabularData

instance.

**Returns:** the number of values contained.

- isEmpty

```java
boolean isEmpty()
```

Returns

true

if the number of

CompositeData

values (ie the number of rows) contained in this

TabularData

instance is zero.

**Returns:** true if this

TabularData

is empty.

- containsKey

```java
boolean containsKey​(
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
boolean containsValue​(
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

**Parameters:** key

- the key of the row to return.
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

does not
conform to this

TabularData

instance's *

TabularType

definition

- put

```java
void put​(
CompositeData
value)
```

Adds

value

to this

TabularData

instance.
The composite type of

value

must be the same as this
instance's row type (ie the composite type returned by

this.getTabularType().

getRowType()

), and there must not already be an existing
value in this

TabularData

instance whose index is the
same as the one calculated for the

value

to be
added. The index for

value

is calculated according
to this

TabularData

instance's

TabularType

definition (see

TabularType.

getIndexNames()

).

**Parameters:** value

- the composite data value to be added as a new row to this

TabularData

instance;
must be of the same composite type as this instance's row type;
must not be null.
**Throws:** NullPointerException

- if

value

is

null
**Throws:** InvalidOpenTypeException

- if

value

does not conform to this

TabularData

instance's
row type definition.
**Throws:** KeyAlreadyExistsException

- if the index for

value

, calculated according to
this

TabularData

instance's

TabularType

definition
already maps to an existing value in the underlying HashMap.

- remove

```java
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
void putAll​(
CompositeData
[] values)
```

Add all the elements in

values

to this

TabularData

instance.
If any element in

values

does not satisfy the constraints defined in

put

,
or if any two elements in

values

have the same index calculated according to this

TabularData

instance's

TabularType

definition, then an exception describing the failure is thrown
and no element of

values

is added, thus leaving this

TabularData

instance unchanged.

**Parameters:** values

- the array of composite data values to be added as new rows to this

TabularData

instance;
if

values

is

null

or empty, this method returns without doing anything.
**Throws:** NullPointerException

- if an element of

values

is

null
**Throws:** InvalidOpenTypeException

- if an element of

values

does not conform to
this

TabularData

instance's row type definition
**Throws:** KeyAlreadyExistsException

- if the index for an element of

values

, calculated according to
this

TabularData

instance's

TabularType

definition
already maps to an existing value in this instance,
or two elements of

values

have the same index.

- clear

```java
void clear()
```

Removes all

CompositeData

values (ie rows) from this

TabularData

instance.

- keySet

```java
Set
<?> keySet()
```

Returns a set view of the keys (ie the index values) of the

CompositeData

values (ie the rows) contained in this

TabularData

instance. The returned

Set

is a

Set<List<?>>

but is declared as a

Set<?>

for
compatibility reasons. The returned set can be used to iterate
over the keys.

**Returns:** a set view (

Set<List<?>>

) of the index values
used in this

TabularData

instance.

- values

```java
Collection
<?> values()
```

Returns a collection view of the

CompositeData

values
(ie the rows) contained in this

TabularData

instance.
The returned

Collection

is a

Collection<CompositeData>

but is declared as a

Collection<?>

for compatibility reasons.
The returned collection can be used to iterate over the values.

**Returns:** a collection view (

Collection<CompositeData>

)
of the rows contained in this

TabularData

instance.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

TabularData

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
- their row types are equal
- their contents (ie index to value mappings) are equal

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

TabularData

interface.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

TabularData

instance;
**Returns:** true

if the specified object is equal to this

TabularData

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this

TabularData

instance.

The hash code of a

TabularData

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

tabular type

and its content, where the content is defined as all the index to value mappings).

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
String
toString()
```

Returns a string representation of this

TabularData

instance.

The string representation consists of the name of the implementing class,
and the tabular type of this instance.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

TabularData

instance

Method Detail

- getTabularType

```java
TabularType
getTabularType()
```

Returns the

tabular type

describing this

TabularData

instance.

**Returns:** the tabular type.

- calculateIndex

```java
Object
[] calculateIndex​(
CompositeData
value)
```

Calculates the index that would be used in this

TabularData

instance to refer to the specified
composite data

value

parameter if it were added to this instance.
This method checks for the type validity of the specified

value

,
but does not check if the calculated index is already used to refer to a value in this

TabularData

instance.

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
**Throws:** InvalidOpenTypeException

- if

value

does not conform to this

TabularData

instance's
row type definition.

- size

```java
int size()
```

Returns the number of

CompositeData

values (ie the
number of rows) contained in this

TabularData

instance.

**Returns:** the number of values contained.

- isEmpty

```java
boolean isEmpty()
```

Returns

true

if the number of

CompositeData

values (ie the number of rows) contained in this

TabularData

instance is zero.

**Returns:** true if this

TabularData

is empty.

- containsKey

```java
boolean containsKey​(
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
boolean containsValue​(
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

**Parameters:** key

- the key of the row to return.
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

does not
conform to this

TabularData

instance's *

TabularType

definition

- put

```java
void put​(
CompositeData
value)
```

Adds

value

to this

TabularData

instance.
The composite type of

value

must be the same as this
instance's row type (ie the composite type returned by

this.getTabularType().

getRowType()

), and there must not already be an existing
value in this

TabularData

instance whose index is the
same as the one calculated for the

value

to be
added. The index for

value

is calculated according
to this

TabularData

instance's

TabularType

definition (see

TabularType.

getIndexNames()

).

**Parameters:** value

- the composite data value to be added as a new row to this

TabularData

instance;
must be of the same composite type as this instance's row type;
must not be null.
**Throws:** NullPointerException

- if

value

is

null
**Throws:** InvalidOpenTypeException

- if

value

does not conform to this

TabularData

instance's
row type definition.
**Throws:** KeyAlreadyExistsException

- if the index for

value

, calculated according to
this

TabularData

instance's

TabularType

definition
already maps to an existing value in the underlying HashMap.

- remove

```java
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
void putAll​(
CompositeData
[] values)
```

Add all the elements in

values

to this

TabularData

instance.
If any element in

values

does not satisfy the constraints defined in

put

,
or if any two elements in

values

have the same index calculated according to this

TabularData

instance's

TabularType

definition, then an exception describing the failure is thrown
and no element of

values

is added, thus leaving this

TabularData

instance unchanged.

**Parameters:** values

- the array of composite data values to be added as new rows to this

TabularData

instance;
if

values

is

null

or empty, this method returns without doing anything.
**Throws:** NullPointerException

- if an element of

values

is

null
**Throws:** InvalidOpenTypeException

- if an element of

values

does not conform to
this

TabularData

instance's row type definition
**Throws:** KeyAlreadyExistsException

- if the index for an element of

values

, calculated according to
this

TabularData

instance's

TabularType

definition
already maps to an existing value in this instance,
or two elements of

values

have the same index.

- clear

```java
void clear()
```

Removes all

CompositeData

values (ie rows) from this

TabularData

instance.

- keySet

```java
Set
<?> keySet()
```

Returns a set view of the keys (ie the index values) of the

CompositeData

values (ie the rows) contained in this

TabularData

instance. The returned

Set

is a

Set<List<?>>

but is declared as a

Set<?>

for
compatibility reasons. The returned set can be used to iterate
over the keys.

**Returns:** a set view (

Set<List<?>>

) of the index values
used in this

TabularData

instance.

- values

```java
Collection
<?> values()
```

Returns a collection view of the

CompositeData

values
(ie the rows) contained in this

TabularData

instance.
The returned

Collection

is a

Collection<CompositeData>

but is declared as a

Collection<?>

for compatibility reasons.
The returned collection can be used to iterate over the values.

**Returns:** a collection view (

Collection<CompositeData>

)
of the rows contained in this

TabularData

instance.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

TabularData

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
- their row types are equal
- their contents (ie index to value mappings) are equal

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

TabularData

interface.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

TabularData

instance;
**Returns:** true

if the specified object is equal to this

TabularData

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this

TabularData

instance.

The hash code of a

TabularData

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

tabular type

and its content, where the content is defined as all the index to value mappings).

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
String
toString()
```

Returns a string representation of this

TabularData

instance.

The string representation consists of the name of the implementing class,
and the tabular type of this instance.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

TabularData

instance

---

#### Method Detail

getTabularType

```java
TabularType
getTabularType()
```

Returns the

tabular type

describing this

TabularData

instance.

**Returns:** the tabular type.

---

#### getTabularType

TabularType

getTabularType()

Returns the

tabular type

describing this

TabularData

instance.

calculateIndex

```java
Object
[] calculateIndex​(
CompositeData
value)
```

Calculates the index that would be used in this

TabularData

instance to refer to the specified
composite data

value

parameter if it were added to this instance.
This method checks for the type validity of the specified

value

,
but does not check if the calculated index is already used to refer to a value in this

TabularData

instance.

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
**Throws:** InvalidOpenTypeException

- if

value

does not conform to this

TabularData

instance's
row type definition.

---

#### calculateIndex

Object

[] calculateIndex​(

CompositeData

value)

Calculates the index that would be used in this

TabularData

instance to refer to the specified
composite data

value

parameter if it were added to this instance.
This method checks for the type validity of the specified

value

,
but does not check if the calculated index is already used to refer to a value in this

TabularData

instance.

size

```java
int size()
```

Returns the number of

CompositeData

values (ie the
number of rows) contained in this

TabularData

instance.

**Returns:** the number of values contained.

---

#### size

int size()

Returns the number of

CompositeData

values (ie the
number of rows) contained in this

TabularData

instance.

isEmpty

```java
boolean isEmpty()
```

Returns

true

if the number of

CompositeData

values (ie the number of rows) contained in this

TabularData

instance is zero.

**Returns:** true if this

TabularData

is empty.

---

#### isEmpty

boolean isEmpty()

Returns

true

if the number of

CompositeData

values (ie the number of rows) contained in this

TabularData

instance is zero.

containsKey

```java
boolean containsKey​(
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

boolean containsKey​(

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
boolean containsValue​(
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

boolean containsValue​(

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

get

```java
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

**Parameters:** key

- the key of the row to return.
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

does not
conform to this

TabularData

instance's *

TabularType

definition

---

#### get

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
void put​(
CompositeData
value)
```

Adds

value

to this

TabularData

instance.
The composite type of

value

must be the same as this
instance's row type (ie the composite type returned by

this.getTabularType().

getRowType()

), and there must not already be an existing
value in this

TabularData

instance whose index is the
same as the one calculated for the

value

to be
added. The index for

value

is calculated according
to this

TabularData

instance's

TabularType

definition (see

TabularType.

getIndexNames()

).

**Parameters:** value

- the composite data value to be added as a new row to this

TabularData

instance;
must be of the same composite type as this instance's row type;
must not be null.
**Throws:** NullPointerException

- if

value

is

null
**Throws:** InvalidOpenTypeException

- if

value

does not conform to this

TabularData

instance's
row type definition.
**Throws:** KeyAlreadyExistsException

- if the index for

value

, calculated according to
this

TabularData

instance's

TabularType

definition
already maps to an existing value in the underlying HashMap.

---

#### put

void put​(

CompositeData

value)

Adds

value

to this

TabularData

instance.
The composite type of

value

must be the same as this
instance's row type (ie the composite type returned by

this.getTabularType().

getRowType()

), and there must not already be an existing
value in this

TabularData

instance whose index is the
same as the one calculated for the

value

to be
added. The index for

value

is calculated according
to this

TabularData

instance's

TabularType

definition (see

TabularType.

getIndexNames()

).

remove

```java
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
void putAll​(
CompositeData
[] values)
```

Add all the elements in

values

to this

TabularData

instance.
If any element in

values

does not satisfy the constraints defined in

put

,
or if any two elements in

values

have the same index calculated according to this

TabularData

instance's

TabularType

definition, then an exception describing the failure is thrown
and no element of

values

is added, thus leaving this

TabularData

instance unchanged.

**Parameters:** values

- the array of composite data values to be added as new rows to this

TabularData

instance;
if

values

is

null

or empty, this method returns without doing anything.
**Throws:** NullPointerException

- if an element of

values

is

null
**Throws:** InvalidOpenTypeException

- if an element of

values

does not conform to
this

TabularData

instance's row type definition
**Throws:** KeyAlreadyExistsException

- if the index for an element of

values

, calculated according to
this

TabularData

instance's

TabularType

definition
already maps to an existing value in this instance,
or two elements of

values

have the same index.

---

#### putAll

void putAll​(

CompositeData

[] values)

Add all the elements in

values

to this

TabularData

instance.
If any element in

values

does not satisfy the constraints defined in

put

,
or if any two elements in

values

have the same index calculated according to this

TabularData

instance's

TabularType

definition, then an exception describing the failure is thrown
and no element of

values

is added, thus leaving this

TabularData

instance unchanged.

clear

```java
void clear()
```

Removes all

CompositeData

values (ie rows) from this

TabularData

instance.

---

#### clear

void clear()

Removes all

CompositeData

values (ie rows) from this

TabularData

instance.

keySet

```java
Set
<?> keySet()
```

Returns a set view of the keys (ie the index values) of the

CompositeData

values (ie the rows) contained in this

TabularData

instance. The returned

Set

is a

Set<List<?>>

but is declared as a

Set<?>

for
compatibility reasons. The returned set can be used to iterate
over the keys.

**Returns:** a set view (

Set<List<?>>

) of the index values
used in this

TabularData

instance.

---

#### keySet

Set

<?> keySet()

Returns a set view of the keys (ie the index values) of the

CompositeData

values (ie the rows) contained in this

TabularData

instance. The returned

Set

is a

Set<List<?>>

but is declared as a

Set<?>

for
compatibility reasons. The returned set can be used to iterate
over the keys.

values

```java
Collection
<?> values()
```

Returns a collection view of the

CompositeData

values
(ie the rows) contained in this

TabularData

instance.
The returned

Collection

is a

Collection<CompositeData>

but is declared as a

Collection<?>

for compatibility reasons.
The returned collection can be used to iterate over the values.

**Returns:** a collection view (

Collection<CompositeData>

)
of the rows contained in this

TabularData

instance.

---

#### values

Collection

<?> values()

Returns a collection view of the

CompositeData

values
(ie the rows) contained in this

TabularData

instance.
The returned

Collection

is a

Collection<CompositeData>

but is declared as a

Collection<?>

for compatibility reasons.
The returned collection can be used to iterate over the values.

equals

```java
boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

TabularData

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
- their row types are equal
- their contents (ie index to value mappings) are equal

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

TabularData

interface.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

TabularData

instance;
**Returns:** true

if the specified object is equal to this

TabularData

instance.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

boolean equals​(

Object

obj)

Compares the specified

obj

parameter with this

TabularData

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
- their row types are equal
- their contents (ie index to value mappings) are equal

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
- their row types are equal
- their contents (ie index to value mappings) are equal

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

their row types are equal

their contents (ie index to value mappings) are equal

hashCode

```java
int hashCode()
```

Returns the hash code value for this

TabularData

instance.

The hash code of a

TabularData

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

tabular type

and its content, where the content is defined as all the index to value mappings).

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

int hashCode()

Returns the hash code value for this

TabularData

instance.

The hash code of a

TabularData

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

tabular type

and its content, where the content is defined as all the index to value mappings).

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

The hash code of a

TabularData

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

tabular type

and its content, where the content is defined as all the index to value mappings).

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

toString

```java
String
toString()
```

Returns a string representation of this

TabularData

instance.

The string representation consists of the name of the implementing class,
and the tabular type of this instance.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

TabularData

instance

---

#### toString

String

toString()

Returns a string representation of this

TabularData

instance.

The string representation consists of the name of the implementing class,
and the tabular type of this instance.

The string representation consists of the name of the implementing class,
and the tabular type of this instance.

---

