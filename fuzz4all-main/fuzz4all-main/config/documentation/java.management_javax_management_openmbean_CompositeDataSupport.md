# Class CompositeDataSupport

**Source:** `java.management\javax\management\openmbean\CompositeDataSupport.html`

### Class Description

```java
public class
CompositeDataSupport

extends
Object

implements
CompositeData
,
Serializable
```

The

CompositeDataSupport

class is the

open data

class which
implements the

CompositeData

interface.

**All Implemented Interfaces:** Serializable

,

CompositeData

---

### Field Details

*No entries found.*

### Constructor Details

#### public CompositeDataSupport​(
CompositeType
compositeType,

String
[] itemNames,

Object
[] itemValues)
throws
OpenDataException

Constructs a

CompositeDataSupport

instance with the specified

compositeType

, whose item values
are specified by

itemValues[]

, in the same order as in

itemNames[]

.
As a

CompositeType

does not specify any order on its items,
the

itemNames[]

parameter is used
to specify the order in which the values are given in

itemValues[]

.
The items contained in this

CompositeDataSupport

instance are
internally stored in a

TreeMap

,
thus sorted in ascending lexicographic order of their names, for faster
retrieval of individual item values.

The constructor checks that all the constraints listed below for each
parameter are satisfied,
and throws the appropriate exception if they are not.

**Parameters:**
- compositeType

- the

composite type

of this

composite
data

instance; must not be null.
- itemNames

-

itemNames

must list, in any order, all the
item names defined in

compositeType

; the order in which the
names are listed, is used to match values in

itemValues[]

; must
not be null or empty.
- itemValues

- the values of the items, listed in the same order as
their respective names in

itemNames

; each item value can be
null, but if it is non-null it must be a valid value for the open type
defined in

compositeType

for the corresponding item; must be of
the same size as

itemNames

; must not be null or empty.

**Throws:**
- IllegalArgumentException

-

compositeType

is null, or

itemNames[]

or

itemValues[]

is null or empty, or one
of the elements in

itemNames[]

is a null or empty string, or

itemNames[]

and

itemValues[]

are not of the same size.
- OpenDataException

-

itemNames[]

or

itemValues[]

's size differs from the number of items defined in

compositeType

, or one of the elements in

itemNames[]

does not exist as an item name defined in

compositeType

, or one
of the elements in

itemValues[]

is not a valid value for the
corresponding item as defined in

compositeType

.

---

#### public CompositeDataSupport​(
CompositeType
compositeType,

Map
<
String
,​?> items)
throws
OpenDataException

Constructs a

CompositeDataSupport

instance with the specified

compositeType

,
whose item names and corresponding values
are given by the mappings in the map

items

.
This constructor converts the keys to a string array and the values to an object array and calls

CompositeDataSupport(javax.management.openmbean.CompositeType, java.lang.String[], java.lang.Object[])

.

**Parameters:**
- compositeType

- the

composite type

of this

composite data

instance;
must not be null.
- items

- the mappings of all the item names to their values;

items

must contain all the item names defined in

compositeType

;
must not be null or empty.

**Throws:**
- IllegalArgumentException

-

compositeType

is null, or

items

is null or empty, or one of the keys in

items

is a null
or empty string.
- OpenDataException

-

items

' size differs from the
number of items defined in

compositeType

, or one of the
keys in

items

does not exist as an item name defined in

compositeType

, or one of the values in

items

is not a valid value for the corresponding item as defined in

compositeType

.
- ArrayStoreException

- one or more keys in

items

is not of
the class

java.lang.String

.

---

### Method Details

#### public
CompositeType
getCompositeType()

Returns the

composite type

of this

composite data

instance.

**Specified by:**
- getCompositeType

in interface

CompositeData

**Returns:**
- the type of this CompositeData.

---

#### public
Object
get​(
String
key)

Returns the value of the item whose name is

key

.

**Specified by:**
- get

in interface

CompositeData

**Parameters:**
- key

- the name of the item.

**Returns:**
- the value associated with this key.

**Throws:**
- IllegalArgumentException

- if

key

is a null or empty String.
- InvalidKeyException

- if

key

is not an existing item name for
this

CompositeData

instance.

---

#### public
Object
[] getAll​(
String
[] keys)

Returns an array of the values of the items whose names are specified by

keys

, in the same order as

keys

.

**Specified by:**
- getAll

in interface

CompositeData

**Parameters:**
- keys

- the names of the items.

**Returns:**
- the values corresponding to the keys.

**Throws:**
- IllegalArgumentException

- if an element in

keys

is a null
or empty String.
- InvalidKeyException

- if an element in

keys

is not an existing
item name for this

CompositeData

instance.

---

#### public boolean containsKey​(
String
key)

Returns

true

if and only if this

CompositeData

instance contains
an item whose name is

key

.
If

key

is a null or empty String, this method simply returns false.

**Specified by:**
- containsKey

in interface

CompositeData

**Parameters:**
- key

- the key to be tested.

**Returns:**
- true if this

CompositeData

contains the key.

---

#### public boolean containsValue​(
Object
value)

Returns

true

if and only if this

CompositeData

instance
contains an item
whose value is

value

.

**Specified by:**
- containsValue

in interface

CompositeData

**Parameters:**
- value

- the value to be tested.

**Returns:**
- true if this

CompositeData

contains the value.

---

#### public
Collection
<?> values()

Returns an unmodifiable Collection view of the item values contained in this

CompositeData

instance.
The returned collection's iterator will return the values in the ascending
lexicographic order of the corresponding
item names.

**Specified by:**
- values

in interface

CompositeData

**Returns:**
- the values.

---

#### public boolean equals​(
Object
obj)

Compares the specified

obj

parameter with this

CompositeDataSupport

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

CompositeData

interface,
- their composite types are equal
- their contents, i.e. (name, value) pairs are equal. If a value contained in
the content is an array, the value comparison is done as if by calling
the

deepEquals

method
for arrays of object reference types or the appropriate overloading of

Arrays.equals(e1,e2)

for arrays of primitive types

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of the

CompositeData

interface, with the restrictions mentioned in the

equals

method of the

java.util.Collection

interface.

**Specified by:**
- equals

in interface

CompositeData

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to be compared for equality with this

CompositeDataSupport

instance.

**Returns:**
- true

if the specified object is equal to this

CompositeDataSupport

instance.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this

CompositeDataSupport

instance.

The hash code of a

CompositeDataSupport

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

composite type

and all the item values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

CompositeDataSupport

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

Each item value's hash code is added to the returned hash code.
If an item value is an array,
its hash code is obtained as if by calling the

deepHashCode

method
for arrays of object reference types or the appropriate overloading
of

Arrays.hashCode(e)

for arrays of primitive types.

**Specified by:**
- hashCode

in interface

CompositeData

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this

CompositeDataSupport

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

CompositeDataSupport

instance.

The string representation consists of the name of this class (ie

javax.management.openmbean.CompositeDataSupport

),
the string representation of the composite type of this instance, and the string representation of the contents
(ie list the itemName=itemValue mappings).

**Specified by:**
- toString

in interface

CompositeData

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

CompositeDataSupport

instance

---

### Additional Sections

#### Class CompositeDataSupport

java.lang.Object

- javax.management.openmbean.CompositeDataSupport

javax.management.openmbean.CompositeDataSupport

**All Implemented Interfaces:** Serializable

,

CompositeData

```java
public class
CompositeDataSupport

extends
Object

implements
CompositeData
,
Serializable
```

The

CompositeDataSupport

class is the

open data

class which
implements the

CompositeData

interface.

**Since:** 1.5
**See Also:** Serialized Form

public class

CompositeDataSupport

extends

Object

implements

CompositeData

,

Serializable

The

CompositeDataSupport

class is the

open data

class which
implements the

CompositeData

interface.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CompositeDataSupport

​(

CompositeType

compositeType,

String

[] itemNames,

Object

[] itemValues)

Constructs a

CompositeDataSupport

instance with the specified

compositeType

, whose item values
are specified by

itemValues[]

, in the same order as in

itemNames[]

.

CompositeDataSupport

​(

CompositeType

compositeType,

Map

<

String

,​?> items)

Constructs a

CompositeDataSupport

instance with the specified

compositeType

,
whose item names and corresponding values
are given by the mappings in the map

items

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

containsKey

​(

String

key)

Returns

true

if and only if this

CompositeData

instance contains
an item whose name is

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

CompositeData

instance
contains an item
whose value is

value

.

boolean

equals

​(

Object

obj)

Compares the specified

obj

parameter with this

CompositeDataSupport

instance for equality.

Object

get

​(

String

key)

Returns the value of the item whose name is

key

.

Object

[]

getAll

​(

String

[] keys)

Returns an array of the values of the items whose names are specified by

keys

, in the same order as

keys

.

CompositeType

getCompositeType

()

Returns the

composite type

of this

composite data

instance.

int

hashCode

()

Returns the hash code value for this

CompositeDataSupport

instance.

String

toString

()

Returns a string representation of this

CompositeDataSupport

instance.

Collection

<?>

values

()

Returns an unmodifiable Collection view of the item values contained in this

CompositeData

instance.

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

CompositeDataSupport

​(

CompositeType

compositeType,

String

[] itemNames,

Object

[] itemValues)

Constructs a

CompositeDataSupport

instance with the specified

compositeType

, whose item values
are specified by

itemValues[]

, in the same order as in

itemNames[]

.

CompositeDataSupport

​(

CompositeType

compositeType,

Map

<

String

,​?> items)

Constructs a

CompositeDataSupport

instance with the specified

compositeType

,
whose item names and corresponding values
are given by the mappings in the map

items

.

---

#### Constructor Summary

Constructs a

CompositeDataSupport

instance with the specified

compositeType

, whose item values
are specified by

itemValues[]

, in the same order as in

itemNames[]

.

Constructs a

CompositeDataSupport

instance with the specified

compositeType

,
whose item names and corresponding values
are given by the mappings in the map

items

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

containsKey

​(

String

key)

Returns

true

if and only if this

CompositeData

instance contains
an item whose name is

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

CompositeData

instance
contains an item
whose value is

value

.

boolean

equals

​(

Object

obj)

Compares the specified

obj

parameter with this

CompositeDataSupport

instance for equality.

Object

get

​(

String

key)

Returns the value of the item whose name is

key

.

Object

[]

getAll

​(

String

[] keys)

Returns an array of the values of the items whose names are specified by

keys

, in the same order as

keys

.

CompositeType

getCompositeType

()

Returns the

composite type

of this

composite data

instance.

int

hashCode

()

Returns the hash code value for this

CompositeDataSupport

instance.

String

toString

()

Returns a string representation of this

CompositeDataSupport

instance.

Collection

<?>

values

()

Returns an unmodifiable Collection view of the item values contained in this

CompositeData

instance.

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

wait

,

wait

,

wait

---

#### Method Summary

Returns

true

if and only if this

CompositeData

instance contains
an item whose name is

key

.

Returns

true

if and only if this

CompositeData

instance
contains an item
whose value is

value

.

Compares the specified

obj

parameter with this

CompositeDataSupport

instance for equality.

Returns the value of the item whose name is

key

.

Returns an array of the values of the items whose names are specified by

keys

, in the same order as

keys

.

Returns the

composite type

of this

composite data

instance.

Returns the hash code value for this

CompositeDataSupport

instance.

Returns a string representation of this

CompositeDataSupport

instance.

Returns an unmodifiable Collection view of the item values contained in this

CompositeData

instance.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CompositeDataSupport

```java
public CompositeDataSupport​(
CompositeType
compositeType,

String
[] itemNames,

Object
[] itemValues)
throws
OpenDataException
```

Constructs a

CompositeDataSupport

instance with the specified

compositeType

, whose item values
are specified by

itemValues[]

, in the same order as in

itemNames[]

.
As a

CompositeType

does not specify any order on its items,
the

itemNames[]

parameter is used
to specify the order in which the values are given in

itemValues[]

.
The items contained in this

CompositeDataSupport

instance are
internally stored in a

TreeMap

,
thus sorted in ascending lexicographic order of their names, for faster
retrieval of individual item values.

The constructor checks that all the constraints listed below for each
parameter are satisfied,
and throws the appropriate exception if they are not.

**Parameters:** compositeType

- the

composite type

of this

composite
data

instance; must not be null.
**Parameters:** itemNames

-

itemNames

must list, in any order, all the
item names defined in

compositeType

; the order in which the
names are listed, is used to match values in

itemValues[]

; must
not be null or empty.
**Parameters:** itemValues

- the values of the items, listed in the same order as
their respective names in

itemNames

; each item value can be
null, but if it is non-null it must be a valid value for the open type
defined in

compositeType

for the corresponding item; must be of
the same size as

itemNames

; must not be null or empty.
**Throws:** IllegalArgumentException

-

compositeType

is null, or

itemNames[]

or

itemValues[]

is null or empty, or one
of the elements in

itemNames[]

is a null or empty string, or

itemNames[]

and

itemValues[]

are not of the same size.
**Throws:** OpenDataException

-

itemNames[]

or

itemValues[]

's size differs from the number of items defined in

compositeType

, or one of the elements in

itemNames[]

does not exist as an item name defined in

compositeType

, or one
of the elements in

itemValues[]

is not a valid value for the
corresponding item as defined in

compositeType

.

- CompositeDataSupport

```java
public CompositeDataSupport​(
CompositeType
compositeType,

Map
<
String
,​?> items)
throws
OpenDataException
```

Constructs a

CompositeDataSupport

instance with the specified

compositeType

,
whose item names and corresponding values
are given by the mappings in the map

items

.
This constructor converts the keys to a string array and the values to an object array and calls

CompositeDataSupport(javax.management.openmbean.CompositeType, java.lang.String[], java.lang.Object[])

.

**Parameters:** compositeType

- the

composite type

of this

composite data

instance;
must not be null.
**Parameters:** items

- the mappings of all the item names to their values;

items

must contain all the item names defined in

compositeType

;
must not be null or empty.
**Throws:** IllegalArgumentException

-

compositeType

is null, or

items

is null or empty, or one of the keys in

items

is a null
or empty string.
**Throws:** OpenDataException

-

items

' size differs from the
number of items defined in

compositeType

, or one of the
keys in

items

does not exist as an item name defined in

compositeType

, or one of the values in

items

is not a valid value for the corresponding item as defined in

compositeType

.
**Throws:** ArrayStoreException

- one or more keys in

items

is not of
the class

java.lang.String

.

============ METHOD DETAIL ==========

- Method Detail

- getCompositeType

```java
public
CompositeType
getCompositeType()
```

Returns the

composite type

of this

composite data

instance.

**Specified by:** getCompositeType

in interface

CompositeData
**Returns:** the type of this CompositeData.

- get

```java
public
Object
get​(
String
key)
```

Returns the value of the item whose name is

key

.

**Specified by:** get

in interface

CompositeData
**Parameters:** key

- the name of the item.
**Returns:** the value associated with this key.
**Throws:** IllegalArgumentException

- if

key

is a null or empty String.
**Throws:** InvalidKeyException

- if

key

is not an existing item name for
this

CompositeData

instance.

- getAll

```java
public
Object
[] getAll​(
String
[] keys)
```

Returns an array of the values of the items whose names are specified by

keys

, in the same order as

keys

.

**Specified by:** getAll

in interface

CompositeData
**Parameters:** keys

- the names of the items.
**Returns:** the values corresponding to the keys.
**Throws:** IllegalArgumentException

- if an element in

keys

is a null
or empty String.
**Throws:** InvalidKeyException

- if an element in

keys

is not an existing
item name for this

CompositeData

instance.

- containsKey

```java
public boolean containsKey​(
String
key)
```

Returns

true

if and only if this

CompositeData

instance contains
an item whose name is

key

.
If

key

is a null or empty String, this method simply returns false.

**Specified by:** containsKey

in interface

CompositeData
**Parameters:** key

- the key to be tested.
**Returns:** true if this

CompositeData

contains the key.

- containsValue

```java
public boolean containsValue​(
Object
value)
```

Returns

true

if and only if this

CompositeData

instance
contains an item
whose value is

value

.

**Specified by:** containsValue

in interface

CompositeData
**Parameters:** value

- the value to be tested.
**Returns:** true if this

CompositeData

contains the value.

- values

```java
public
Collection
<?> values()
```

Returns an unmodifiable Collection view of the item values contained in this

CompositeData

instance.
The returned collection's iterator will return the values in the ascending
lexicographic order of the corresponding
item names.

**Specified by:** values

in interface

CompositeData
**Returns:** the values.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

CompositeDataSupport

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

CompositeData

interface,
- their composite types are equal
- their contents, i.e. (name, value) pairs are equal. If a value contained in
the content is an array, the value comparison is done as if by calling
the

deepEquals

method
for arrays of object reference types or the appropriate overloading of

Arrays.equals(e1,e2)

for arrays of primitive types

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of the

CompositeData

interface, with the restrictions mentioned in the

equals

method of the

java.util.Collection

interface.

**Specified by:** equals

in interface

CompositeData
**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

CompositeDataSupport

instance.
**Returns:** true

if the specified object is equal to this

CompositeDataSupport

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

CompositeDataSupport

instance.

The hash code of a

CompositeDataSupport

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

composite type

and all the item values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

CompositeDataSupport

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

Each item value's hash code is added to the returned hash code.
If an item value is an array,
its hash code is obtained as if by calling the

deepHashCode

method
for arrays of object reference types or the appropriate overloading
of

Arrays.hashCode(e)

for arrays of primitive types.

**Specified by:** hashCode

in interface

CompositeData
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

CompositeDataSupport

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

CompositeDataSupport

instance.

The string representation consists of the name of this class (ie

javax.management.openmbean.CompositeDataSupport

),
the string representation of the composite type of this instance, and the string representation of the contents
(ie list the itemName=itemValue mappings).

**Specified by:** toString

in interface

CompositeData
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

CompositeDataSupport

instance

Constructor Detail

- CompositeDataSupport

```java
public CompositeDataSupport​(
CompositeType
compositeType,

String
[] itemNames,

Object
[] itemValues)
throws
OpenDataException
```

Constructs a

CompositeDataSupport

instance with the specified

compositeType

, whose item values
are specified by

itemValues[]

, in the same order as in

itemNames[]

.
As a

CompositeType

does not specify any order on its items,
the

itemNames[]

parameter is used
to specify the order in which the values are given in

itemValues[]

.
The items contained in this

CompositeDataSupport

instance are
internally stored in a

TreeMap

,
thus sorted in ascending lexicographic order of their names, for faster
retrieval of individual item values.

The constructor checks that all the constraints listed below for each
parameter are satisfied,
and throws the appropriate exception if they are not.

**Parameters:** compositeType

- the

composite type

of this

composite
data

instance; must not be null.
**Parameters:** itemNames

-

itemNames

must list, in any order, all the
item names defined in

compositeType

; the order in which the
names are listed, is used to match values in

itemValues[]

; must
not be null or empty.
**Parameters:** itemValues

- the values of the items, listed in the same order as
their respective names in

itemNames

; each item value can be
null, but if it is non-null it must be a valid value for the open type
defined in

compositeType

for the corresponding item; must be of
the same size as

itemNames

; must not be null or empty.
**Throws:** IllegalArgumentException

-

compositeType

is null, or

itemNames[]

or

itemValues[]

is null or empty, or one
of the elements in

itemNames[]

is a null or empty string, or

itemNames[]

and

itemValues[]

are not of the same size.
**Throws:** OpenDataException

-

itemNames[]

or

itemValues[]

's size differs from the number of items defined in

compositeType

, or one of the elements in

itemNames[]

does not exist as an item name defined in

compositeType

, or one
of the elements in

itemValues[]

is not a valid value for the
corresponding item as defined in

compositeType

.

- CompositeDataSupport

```java
public CompositeDataSupport​(
CompositeType
compositeType,

Map
<
String
,​?> items)
throws
OpenDataException
```

Constructs a

CompositeDataSupport

instance with the specified

compositeType

,
whose item names and corresponding values
are given by the mappings in the map

items

.
This constructor converts the keys to a string array and the values to an object array and calls

CompositeDataSupport(javax.management.openmbean.CompositeType, java.lang.String[], java.lang.Object[])

.

**Parameters:** compositeType

- the

composite type

of this

composite data

instance;
must not be null.
**Parameters:** items

- the mappings of all the item names to their values;

items

must contain all the item names defined in

compositeType

;
must not be null or empty.
**Throws:** IllegalArgumentException

-

compositeType

is null, or

items

is null or empty, or one of the keys in

items

is a null
or empty string.
**Throws:** OpenDataException

-

items

' size differs from the
number of items defined in

compositeType

, or one of the
keys in

items

does not exist as an item name defined in

compositeType

, or one of the values in

items

is not a valid value for the corresponding item as defined in

compositeType

.
**Throws:** ArrayStoreException

- one or more keys in

items

is not of
the class

java.lang.String

.

---

#### Constructor Detail

CompositeDataSupport

```java
public CompositeDataSupport​(
CompositeType
compositeType,

String
[] itemNames,

Object
[] itemValues)
throws
OpenDataException
```

Constructs a

CompositeDataSupport

instance with the specified

compositeType

, whose item values
are specified by

itemValues[]

, in the same order as in

itemNames[]

.
As a

CompositeType

does not specify any order on its items,
the

itemNames[]

parameter is used
to specify the order in which the values are given in

itemValues[]

.
The items contained in this

CompositeDataSupport

instance are
internally stored in a

TreeMap

,
thus sorted in ascending lexicographic order of their names, for faster
retrieval of individual item values.

The constructor checks that all the constraints listed below for each
parameter are satisfied,
and throws the appropriate exception if they are not.

**Parameters:** compositeType

- the

composite type

of this

composite
data

instance; must not be null.
**Parameters:** itemNames

-

itemNames

must list, in any order, all the
item names defined in

compositeType

; the order in which the
names are listed, is used to match values in

itemValues[]

; must
not be null or empty.
**Parameters:** itemValues

- the values of the items, listed in the same order as
their respective names in

itemNames

; each item value can be
null, but if it is non-null it must be a valid value for the open type
defined in

compositeType

for the corresponding item; must be of
the same size as

itemNames

; must not be null or empty.
**Throws:** IllegalArgumentException

-

compositeType

is null, or

itemNames[]

or

itemValues[]

is null or empty, or one
of the elements in

itemNames[]

is a null or empty string, or

itemNames[]

and

itemValues[]

are not of the same size.
**Throws:** OpenDataException

-

itemNames[]

or

itemValues[]

's size differs from the number of items defined in

compositeType

, or one of the elements in

itemNames[]

does not exist as an item name defined in

compositeType

, or one
of the elements in

itemValues[]

is not a valid value for the
corresponding item as defined in

compositeType

.

---

#### CompositeDataSupport

public CompositeDataSupport​(

CompositeType

compositeType,

String

[] itemNames,

Object

[] itemValues)
throws

OpenDataException

Constructs a

CompositeDataSupport

instance with the specified

compositeType

, whose item values
are specified by

itemValues[]

, in the same order as in

itemNames[]

.
As a

CompositeType

does not specify any order on its items,
the

itemNames[]

parameter is used
to specify the order in which the values are given in

itemValues[]

.
The items contained in this

CompositeDataSupport

instance are
internally stored in a

TreeMap

,
thus sorted in ascending lexicographic order of their names, for faster
retrieval of individual item values.

The constructor checks that all the constraints listed below for each
parameter are satisfied,
and throws the appropriate exception if they are not.

Constructs a

CompositeDataSupport

instance with the specified

compositeType

, whose item values
are specified by

itemValues[]

, in the same order as in

itemNames[]

.
As a

CompositeType

does not specify any order on its items,
the

itemNames[]

parameter is used
to specify the order in which the values are given in

itemValues[]

.
The items contained in this

CompositeDataSupport

instance are
internally stored in a

TreeMap

,
thus sorted in ascending lexicographic order of their names, for faster
retrieval of individual item values.

The constructor checks that all the constraints listed below for each
parameter are satisfied,
and throws the appropriate exception if they are not.

CompositeDataSupport

```java
public CompositeDataSupport​(
CompositeType
compositeType,

Map
<
String
,​?> items)
throws
OpenDataException
```

Constructs a

CompositeDataSupport

instance with the specified

compositeType

,
whose item names and corresponding values
are given by the mappings in the map

items

.
This constructor converts the keys to a string array and the values to an object array and calls

CompositeDataSupport(javax.management.openmbean.CompositeType, java.lang.String[], java.lang.Object[])

.

**Parameters:** compositeType

- the

composite type

of this

composite data

instance;
must not be null.
**Parameters:** items

- the mappings of all the item names to their values;

items

must contain all the item names defined in

compositeType

;
must not be null or empty.
**Throws:** IllegalArgumentException

-

compositeType

is null, or

items

is null or empty, or one of the keys in

items

is a null
or empty string.
**Throws:** OpenDataException

-

items

' size differs from the
number of items defined in

compositeType

, or one of the
keys in

items

does not exist as an item name defined in

compositeType

, or one of the values in

items

is not a valid value for the corresponding item as defined in

compositeType

.
**Throws:** ArrayStoreException

- one or more keys in

items

is not of
the class

java.lang.String

.

---

#### CompositeDataSupport

public CompositeDataSupport​(

CompositeType

compositeType,

Map

<

String

,​?> items)
throws

OpenDataException

Constructs a

CompositeDataSupport

instance with the specified

compositeType

,
whose item names and corresponding values
are given by the mappings in the map

items

.
This constructor converts the keys to a string array and the values to an object array and calls

CompositeDataSupport(javax.management.openmbean.CompositeType, java.lang.String[], java.lang.Object[])

.

Method Detail

- getCompositeType

```java
public
CompositeType
getCompositeType()
```

Returns the

composite type

of this

composite data

instance.

**Specified by:** getCompositeType

in interface

CompositeData
**Returns:** the type of this CompositeData.

- get

```java
public
Object
get​(
String
key)
```

Returns the value of the item whose name is

key

.

**Specified by:** get

in interface

CompositeData
**Parameters:** key

- the name of the item.
**Returns:** the value associated with this key.
**Throws:** IllegalArgumentException

- if

key

is a null or empty String.
**Throws:** InvalidKeyException

- if

key

is not an existing item name for
this

CompositeData

instance.

- getAll

```java
public
Object
[] getAll​(
String
[] keys)
```

Returns an array of the values of the items whose names are specified by

keys

, in the same order as

keys

.

**Specified by:** getAll

in interface

CompositeData
**Parameters:** keys

- the names of the items.
**Returns:** the values corresponding to the keys.
**Throws:** IllegalArgumentException

- if an element in

keys

is a null
or empty String.
**Throws:** InvalidKeyException

- if an element in

keys

is not an existing
item name for this

CompositeData

instance.

- containsKey

```java
public boolean containsKey​(
String
key)
```

Returns

true

if and only if this

CompositeData

instance contains
an item whose name is

key

.
If

key

is a null or empty String, this method simply returns false.

**Specified by:** containsKey

in interface

CompositeData
**Parameters:** key

- the key to be tested.
**Returns:** true if this

CompositeData

contains the key.

- containsValue

```java
public boolean containsValue​(
Object
value)
```

Returns

true

if and only if this

CompositeData

instance
contains an item
whose value is

value

.

**Specified by:** containsValue

in interface

CompositeData
**Parameters:** value

- the value to be tested.
**Returns:** true if this

CompositeData

contains the value.

- values

```java
public
Collection
<?> values()
```

Returns an unmodifiable Collection view of the item values contained in this

CompositeData

instance.
The returned collection's iterator will return the values in the ascending
lexicographic order of the corresponding
item names.

**Specified by:** values

in interface

CompositeData
**Returns:** the values.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

CompositeDataSupport

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

CompositeData

interface,
- their composite types are equal
- their contents, i.e. (name, value) pairs are equal. If a value contained in
the content is an array, the value comparison is done as if by calling
the

deepEquals

method
for arrays of object reference types or the appropriate overloading of

Arrays.equals(e1,e2)

for arrays of primitive types

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of the

CompositeData

interface, with the restrictions mentioned in the

equals

method of the

java.util.Collection

interface.

**Specified by:** equals

in interface

CompositeData
**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

CompositeDataSupport

instance.
**Returns:** true

if the specified object is equal to this

CompositeDataSupport

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

CompositeDataSupport

instance.

The hash code of a

CompositeDataSupport

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

composite type

and all the item values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

CompositeDataSupport

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

Each item value's hash code is added to the returned hash code.
If an item value is an array,
its hash code is obtained as if by calling the

deepHashCode

method
for arrays of object reference types or the appropriate overloading
of

Arrays.hashCode(e)

for arrays of primitive types.

**Specified by:** hashCode

in interface

CompositeData
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

CompositeDataSupport

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

CompositeDataSupport

instance.

The string representation consists of the name of this class (ie

javax.management.openmbean.CompositeDataSupport

),
the string representation of the composite type of this instance, and the string representation of the contents
(ie list the itemName=itemValue mappings).

**Specified by:** toString

in interface

CompositeData
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

CompositeDataSupport

instance

---

#### Method Detail

getCompositeType

```java
public
CompositeType
getCompositeType()
```

Returns the

composite type

of this

composite data

instance.

**Specified by:** getCompositeType

in interface

CompositeData
**Returns:** the type of this CompositeData.

---

#### getCompositeType

public

CompositeType

getCompositeType()

Returns the

composite type

of this

composite data

instance.

get

```java
public
Object
get​(
String
key)
```

Returns the value of the item whose name is

key

.

**Specified by:** get

in interface

CompositeData
**Parameters:** key

- the name of the item.
**Returns:** the value associated with this key.
**Throws:** IllegalArgumentException

- if

key

is a null or empty String.
**Throws:** InvalidKeyException

- if

key

is not an existing item name for
this

CompositeData

instance.

---

#### get

public

Object

get​(

String

key)

Returns the value of the item whose name is

key

.

getAll

```java
public
Object
[] getAll​(
String
[] keys)
```

Returns an array of the values of the items whose names are specified by

keys

, in the same order as

keys

.

**Specified by:** getAll

in interface

CompositeData
**Parameters:** keys

- the names of the items.
**Returns:** the values corresponding to the keys.
**Throws:** IllegalArgumentException

- if an element in

keys

is a null
or empty String.
**Throws:** InvalidKeyException

- if an element in

keys

is not an existing
item name for this

CompositeData

instance.

---

#### getAll

public

Object

[] getAll​(

String

[] keys)

Returns an array of the values of the items whose names are specified by

keys

, in the same order as

keys

.

containsKey

```java
public boolean containsKey​(
String
key)
```

Returns

true

if and only if this

CompositeData

instance contains
an item whose name is

key

.
If

key

is a null or empty String, this method simply returns false.

**Specified by:** containsKey

in interface

CompositeData
**Parameters:** key

- the key to be tested.
**Returns:** true if this

CompositeData

contains the key.

---

#### containsKey

public boolean containsKey​(

String

key)

Returns

true

if and only if this

CompositeData

instance contains
an item whose name is

key

.
If

key

is a null or empty String, this method simply returns false.

containsValue

```java
public boolean containsValue​(
Object
value)
```

Returns

true

if and only if this

CompositeData

instance
contains an item
whose value is

value

.

**Specified by:** containsValue

in interface

CompositeData
**Parameters:** value

- the value to be tested.
**Returns:** true if this

CompositeData

contains the value.

---

#### containsValue

public boolean containsValue​(

Object

value)

Returns

true

if and only if this

CompositeData

instance
contains an item
whose value is

value

.

values

```java
public
Collection
<?> values()
```

Returns an unmodifiable Collection view of the item values contained in this

CompositeData

instance.
The returned collection's iterator will return the values in the ascending
lexicographic order of the corresponding
item names.

**Specified by:** values

in interface

CompositeData
**Returns:** the values.

---

#### values

public

Collection

<?> values()

Returns an unmodifiable Collection view of the item values contained in this

CompositeData

instance.
The returned collection's iterator will return the values in the ascending
lexicographic order of the corresponding
item names.

equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

CompositeDataSupport

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

CompositeData

interface,
- their composite types are equal
- their contents, i.e. (name, value) pairs are equal. If a value contained in
the content is an array, the value comparison is done as if by calling
the

deepEquals

method
for arrays of object reference types or the appropriate overloading of

Arrays.equals(e1,e2)

for arrays of primitive types

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of the

CompositeData

interface, with the restrictions mentioned in the

equals

method of the

java.util.Collection

interface.

**Specified by:** equals

in interface

CompositeData
**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

CompositeDataSupport

instance.
**Returns:** true

if the specified object is equal to this

CompositeDataSupport

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

CompositeDataSupport

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

CompositeData

interface,
- their composite types are equal
- their contents, i.e. (name, value) pairs are equal. If a value contained in
the content is an array, the value comparison is done as if by calling
the

deepEquals

method
for arrays of object reference types or the appropriate overloading of

Arrays.equals(e1,e2)

for arrays of primitive types

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of the

CompositeData

interface, with the restrictions mentioned in the

equals

method of the

java.util.Collection

interface.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

CompositeData

interface,
- their composite types are equal
- their contents, i.e. (name, value) pairs are equal. If a value contained in
the content is an array, the value comparison is done as if by calling
the

deepEquals

method
for arrays of object reference types or the appropriate overloading of

Arrays.equals(e1,e2)

for arrays of primitive types

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of the

CompositeData

interface, with the restrictions mentioned in the

equals

method of the

java.util.Collection

interface.

obj

is non null,

obj

also implements the

CompositeData

interface,

their composite types are equal

their contents, i.e. (name, value) pairs are equal. If a value contained in
the content is an array, the value comparison is done as if by calling
the

deepEquals

method
for arrays of object reference types or the appropriate overloading of

Arrays.equals(e1,e2)

for arrays of primitive types

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of the

CompositeData

interface, with the restrictions mentioned in the

equals

method of the

java.util.Collection

interface.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this

CompositeDataSupport

instance.

The hash code of a

CompositeDataSupport

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

composite type

and all the item values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

CompositeDataSupport

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

Each item value's hash code is added to the returned hash code.
If an item value is an array,
its hash code is obtained as if by calling the

deepHashCode

method
for arrays of object reference types or the appropriate overloading
of

Arrays.hashCode(e)

for arrays of primitive types.

**Specified by:** hashCode

in interface

CompositeData
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

CompositeDataSupport

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this

CompositeDataSupport

instance.

The hash code of a

CompositeDataSupport

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

composite type

and all the item values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

CompositeDataSupport

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

Each item value's hash code is added to the returned hash code.
If an item value is an array,
its hash code is obtained as if by calling the

deepHashCode

method
for arrays of object reference types or the appropriate overloading
of

Arrays.hashCode(e)

for arrays of primitive types.

The hash code of a

CompositeDataSupport

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its

composite type

and all the item values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

CompositeDataSupport

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

Each item value's hash code is added to the returned hash code.
If an item value is an array,
its hash code is obtained as if by calling the

deepHashCode

method
for arrays of object reference types or the appropriate overloading
of

Arrays.hashCode(e)

for arrays of primitive types.

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

CompositeDataSupport

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

Each item value's hash code is added to the returned hash code.
If an item value is an array,
its hash code is obtained as if by calling the

deepHashCode

method
for arrays of object reference types or the appropriate overloading
of

Arrays.hashCode(e)

for arrays of primitive types.

Each item value's hash code is added to the returned hash code.
If an item value is an array,
its hash code is obtained as if by calling the

deepHashCode

method
for arrays of object reference types or the appropriate overloading
of

Arrays.hashCode(e)

for arrays of primitive types.

toString

```java
public
String
toString()
```

Returns a string representation of this

CompositeDataSupport

instance.

The string representation consists of the name of this class (ie

javax.management.openmbean.CompositeDataSupport

),
the string representation of the composite type of this instance, and the string representation of the contents
(ie list the itemName=itemValue mappings).

**Specified by:** toString

in interface

CompositeData
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

CompositeDataSupport

instance

---

#### toString

public

String

toString()

Returns a string representation of this

CompositeDataSupport

instance.

The string representation consists of the name of this class (ie

javax.management.openmbean.CompositeDataSupport

),
the string representation of the composite type of this instance, and the string representation of the contents
(ie list the itemName=itemValue mappings).

The string representation consists of the name of this class (ie

javax.management.openmbean.CompositeDataSupport

),
the string representation of the composite type of this instance, and the string representation of the contents
(ie list the itemName=itemValue mappings).

---

