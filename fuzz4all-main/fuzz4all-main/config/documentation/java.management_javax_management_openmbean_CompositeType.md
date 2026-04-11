# Class CompositeType

**Source:** `java.management\javax\management\openmbean\CompositeType.html`

### Class Description

```java
public class
CompositeType

extends
OpenType
<
CompositeData
>
```

The

CompositeType

class is the

open type

class
whose instances describe the types of

CompositeData

values.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CompositeType​(
String
typeName,

String
description,

String
[] itemNames,

String
[] itemDescriptions,

OpenType
<?>[] itemTypes)
throws
OpenDataException

Constructs a

CompositeType

instance, checking for the validity of the given parameters.
The validity constraints are described below for each parameter.

Note that the contents of the three array parameters

itemNames

,

itemDescriptions

and

itemTypes

are internally copied so that any subsequent modification of these arrays by the caller of this constructor
has no impact on the constructed

CompositeType

instance.

The Java class name of composite data values this composite type represents
(ie the class name returned by the

getClassName

method)
is set to the string value returned by

CompositeData.class.getName()

.

**Parameters:**
- typeName

- The name given to the composite type this instance represents; cannot be a null or empty string.
- description

- The human readable description of the composite type this instance represents;
cannot be a null or empty string.
- itemNames

- The names of the items contained in the
composite data values described by this

CompositeType

instance;
cannot be null and should contain at least one element; no element can be a null or empty string.
Note that the order in which the item names are given is not important to differentiate a

CompositeType

instance from another;
the item names are internally stored sorted in ascending alphanumeric order.
- itemDescriptions

- The descriptions, in the same order as

itemNames

, of the items contained in the
composite data values described by this

CompositeType

instance;
should be of the same size as

itemNames

;
no element can be null or an empty string.
- itemTypes

- The open type instances, in the same order as

itemNames

, describing the items contained
in the composite data values described by this

CompositeType

instance;
should be of the same size as

itemNames

;
no element can be null.

**Throws:**
- IllegalArgumentException

- If

typeName

or

description

is a null or empty string,
or

itemNames

or

itemDescriptions

or

itemTypes

is null,
or any element of

itemNames

or

itemDescriptions

is a null or empty string,
or any element of

itemTypes

is null,
or

itemNames

or

itemDescriptions

or

itemTypes

are not of the same size.
- OpenDataException

- If

itemNames

contains duplicate item names
(case sensitive, but leading and trailing whitespaces removed).

---

### Method Details

#### public boolean containsKey​(
String
itemName)

Returns

true

if this

CompositeType

instance defines an item
whose name is

itemName

.

**Parameters:**
- itemName

- the name of the item.

**Returns:**
- true if an item of this name is present.

---

#### public
String
getDescription​(
String
itemName)

Returns the description of the item whose name is

itemName

,
or

null

if this

CompositeType

instance does not define any item
whose name is

itemName

.

**Parameters:**
- itemName

- the name of the item.

**Returns:**
- the description.

---

#### public
OpenType
<?> getType​(
String
itemName)

Returns the

open type

of the item whose name is

itemName

,
or

null

if this

CompositeType

instance does not define any item
whose name is

itemName

.

**Parameters:**
- itemName

- the name of the time.

**Returns:**
- the type.

---

#### public
Set
<
String
> keySet()

Returns an unmodifiable Set view of all the item names defined by this

CompositeType

instance.
The set's iterator will return the item names in ascending order.

**Returns:**
- a

Set

of

String

.

---

#### public boolean isValue​(
Object
obj)

Tests whether

obj

is a value which could be
described by this

CompositeType

instance.

If

obj

is null or is not an instance of

javax.management.openmbean.CompositeData

,

isValue

returns

false

.

If

obj

is an instance of

javax.management.openmbean.CompositeData

, then let

ct

be its

CompositeType

as returned by

CompositeData.getCompositeType()

. The result is true if

this

is

assignable from

ct

. This
means that:

- this.getTypeName()

equals

ct.getTypeName()

, and

there are no item names present in

this

that are
not also present in

ct

, and

for every item in

this

, its type is assignable from
the type of the corresponding item in

ct

.

A

TabularType

is assignable from another

TabularType

if they have the same

typeName

and

index name list

, and the

row type

of the first is
assignable from the row type of the second.

An

ArrayType

is assignable from another

ArrayType

if they have the same

dimension

; and both are

primitive arrays

or neither is;
and the

element
type

of the first is assignable from the element type of the
second.

In every other case, an

OpenType

is assignable from
another

OpenType

only if they are equal.

These rules mean that extra items can be added to a

CompositeData

without making it invalid for a

CompositeType

that does not have those items.

**Specified by:**
- isValue

in class

OpenType

<

CompositeData

>

**Parameters:**
- obj

- the value whose open type is to be tested for compatibility
with this

CompositeType

instance.

**Returns:**
- true

if

obj

is a value for this
composite type,

false

otherwise.

---

#### public boolean equals​(
Object
obj)

Compares the specified

obj

parameter with this

CompositeType

instance for equality.

Two

CompositeType

instances are equal if and only if all of the following statements are true:

- their type names are equal
- their items' names and types are equal

**Specified by:**
- equals

in class

OpenType

<

CompositeData

>

**Parameters:**
- obj

- the object to be compared for equality with this

CompositeType

instance;
if

obj

is

null

,

equals

returns

false

.

**Returns:**
- true

if the specified object is equal to this

CompositeType

instance.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this

CompositeType

instance.

The hash code of a

CompositeType

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: name, items names, items types).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

CompositeType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

CompositeType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this

CompositeType

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

CompositeType

instance.

The string representation consists of
the name of this class (ie

javax.management.openmbean.CompositeType

), the type name for this instance,
and the list of the items names and types string representation of this instance.

As

CompositeType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

**Specified by:**
- toString

in class

OpenType

<

CompositeData

>

**Returns:**
- a string representation of this

CompositeType

instance

---

### Additional Sections

#### Class CompositeType

java.lang.Object

- javax.management.openmbean.OpenType

<

CompositeData

>
- - javax.management.openmbean.CompositeType

javax.management.openmbean.OpenType

<

CompositeData

>

- javax.management.openmbean.CompositeType

javax.management.openmbean.CompositeType

**All Implemented Interfaces:** Serializable

```java
public class
CompositeType

extends
OpenType
<
CompositeData
>
```

The

CompositeType

class is the

open type

class
whose instances describe the types of

CompositeData

values.

**Since:** 1.5
**See Also:** Serialized Form

public class

CompositeType

extends

OpenType

<

CompositeData

>

The

CompositeType

class is the

open type

class
whose instances describe the types of

CompositeData

values.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.management.openmbean.

OpenType

ALLOWED_CLASSNAMES

,

ALLOWED_CLASSNAMES_LIST

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CompositeType

​(

String

typeName,

String

description,

String

[] itemNames,

String

[] itemDescriptions,

OpenType

<?>[] itemTypes)

Constructs a

CompositeType

instance, checking for the validity of the given parameters.

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

itemName)

Returns

true

if this

CompositeType

instance defines an item
whose name is

itemName

.

boolean

equals

​(

Object

obj)

Compares the specified

obj

parameter with this

CompositeType

instance for equality.

String

getDescription

​(

String

itemName)

Returns the description of the item whose name is

itemName

,
or

null

if this

CompositeType

instance does not define any item
whose name is

itemName

.

OpenType

<?>

getType

​(

String

itemName)

Returns the

open type

of the item whose name is

itemName

,
or

null

if this

CompositeType

instance does not define any item
whose name is

itemName

.

int

hashCode

()

Returns the hash code value for this

CompositeType

instance.

boolean

isValue

​(

Object

obj)

Tests whether

obj

is a value which could be
described by this

CompositeType

instance.

Set

<

String

>

keySet

()

Returns an unmodifiable Set view of all the item names defined by this

CompositeType

instance.

String

toString

()

Returns a string representation of this

CompositeType

instance.

- Methods declared in class javax.management.openmbean.

OpenType

getClassName

,

getDescription

,

getTypeName

,

isArray

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

Field Summary

- Fields declared in class javax.management.openmbean.

OpenType

ALLOWED_CLASSNAMES

,

ALLOWED_CLASSNAMES_LIST

---

#### Field Summary

Fields declared in class javax.management.openmbean.

OpenType

ALLOWED_CLASSNAMES

,

ALLOWED_CLASSNAMES_LIST

---

#### Fields declared in class javax.management.openmbean. OpenType

Constructor Summary

Constructors

Constructor

Description

CompositeType

​(

String

typeName,

String

description,

String

[] itemNames,

String

[] itemDescriptions,

OpenType

<?>[] itemTypes)

Constructs a

CompositeType

instance, checking for the validity of the given parameters.

---

#### Constructor Summary

Constructs a

CompositeType

instance, checking for the validity of the given parameters.

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

itemName)

Returns

true

if this

CompositeType

instance defines an item
whose name is

itemName

.

boolean

equals

​(

Object

obj)

Compares the specified

obj

parameter with this

CompositeType

instance for equality.

String

getDescription

​(

String

itemName)

Returns the description of the item whose name is

itemName

,
or

null

if this

CompositeType

instance does not define any item
whose name is

itemName

.

OpenType

<?>

getType

​(

String

itemName)

Returns the

open type

of the item whose name is

itemName

,
or

null

if this

CompositeType

instance does not define any item
whose name is

itemName

.

int

hashCode

()

Returns the hash code value for this

CompositeType

instance.

boolean

isValue

​(

Object

obj)

Tests whether

obj

is a value which could be
described by this

CompositeType

instance.

Set

<

String

>

keySet

()

Returns an unmodifiable Set view of all the item names defined by this

CompositeType

instance.

String

toString

()

Returns a string representation of this

CompositeType

instance.

- Methods declared in class javax.management.openmbean.

OpenType

getClassName

,

getDescription

,

getTypeName

,

isArray

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

if this

CompositeType

instance defines an item
whose name is

itemName

.

Compares the specified

obj

parameter with this

CompositeType

instance for equality.

Returns the description of the item whose name is

itemName

,
or

null

if this

CompositeType

instance does not define any item
whose name is

itemName

.

Returns the

open type

of the item whose name is

itemName

,
or

null

if this

CompositeType

instance does not define any item
whose name is

itemName

.

Returns the hash code value for this

CompositeType

instance.

Tests whether

obj

is a value which could be
described by this

CompositeType

instance.

Returns an unmodifiable Set view of all the item names defined by this

CompositeType

instance.

Returns a string representation of this

CompositeType

instance.

Methods declared in class javax.management.openmbean.

OpenType

getClassName

,

getDescription

,

getTypeName

,

isArray

---

#### Methods declared in class javax.management.openmbean. OpenType

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

- CompositeType

```java
public CompositeType​(
String
typeName,

String
description,

String
[] itemNames,

String
[] itemDescriptions,

OpenType
<?>[] itemTypes)
throws
OpenDataException
```

Constructs a

CompositeType

instance, checking for the validity of the given parameters.
The validity constraints are described below for each parameter.

Note that the contents of the three array parameters

itemNames

,

itemDescriptions

and

itemTypes

are internally copied so that any subsequent modification of these arrays by the caller of this constructor
has no impact on the constructed

CompositeType

instance.

The Java class name of composite data values this composite type represents
(ie the class name returned by the

getClassName

method)
is set to the string value returned by

CompositeData.class.getName()

.

**Parameters:** typeName

- The name given to the composite type this instance represents; cannot be a null or empty string.
**Parameters:** description

- The human readable description of the composite type this instance represents;
cannot be a null or empty string.
**Parameters:** itemNames

- The names of the items contained in the
composite data values described by this

CompositeType

instance;
cannot be null and should contain at least one element; no element can be a null or empty string.
Note that the order in which the item names are given is not important to differentiate a

CompositeType

instance from another;
the item names are internally stored sorted in ascending alphanumeric order.
**Parameters:** itemDescriptions

- The descriptions, in the same order as

itemNames

, of the items contained in the
composite data values described by this

CompositeType

instance;
should be of the same size as

itemNames

;
no element can be null or an empty string.
**Parameters:** itemTypes

- The open type instances, in the same order as

itemNames

, describing the items contained
in the composite data values described by this

CompositeType

instance;
should be of the same size as

itemNames

;
no element can be null.
**Throws:** IllegalArgumentException

- If

typeName

or

description

is a null or empty string,
or

itemNames

or

itemDescriptions

or

itemTypes

is null,
or any element of

itemNames

or

itemDescriptions

is a null or empty string,
or any element of

itemTypes

is null,
or

itemNames

or

itemDescriptions

or

itemTypes

are not of the same size.
**Throws:** OpenDataException

- If

itemNames

contains duplicate item names
(case sensitive, but leading and trailing whitespaces removed).

============ METHOD DETAIL ==========

- Method Detail

- containsKey

```java
public boolean containsKey​(
String
itemName)
```

Returns

true

if this

CompositeType

instance defines an item
whose name is

itemName

.

**Parameters:** itemName

- the name of the item.
**Returns:** true if an item of this name is present.

- getDescription

```java
public
String
getDescription​(
String
itemName)
```

Returns the description of the item whose name is

itemName

,
or

null

if this

CompositeType

instance does not define any item
whose name is

itemName

.

**Parameters:** itemName

- the name of the item.
**Returns:** the description.

- getType

```java
public
OpenType
<?> getType​(
String
itemName)
```

Returns the

open type

of the item whose name is

itemName

,
or

null

if this

CompositeType

instance does not define any item
whose name is

itemName

.

**Parameters:** itemName

- the name of the time.
**Returns:** the type.

- keySet

```java
public
Set
<
String
> keySet()
```

Returns an unmodifiable Set view of all the item names defined by this

CompositeType

instance.
The set's iterator will return the item names in ascending order.

**Returns:** a

Set

of

String

.

- isValue

```java
public boolean isValue​(
Object
obj)
```

Tests whether

obj

is a value which could be
described by this

CompositeType

instance.

If

obj

is null or is not an instance of

javax.management.openmbean.CompositeData

,

isValue

returns

false

.

If

obj

is an instance of

javax.management.openmbean.CompositeData

, then let

ct

be its

CompositeType

as returned by

CompositeData.getCompositeType()

. The result is true if

this

is

assignable from

ct

. This
means that:

- this.getTypeName()

equals

ct.getTypeName()

, and

there are no item names present in

this

that are
not also present in

ct

, and

for every item in

this

, its type is assignable from
the type of the corresponding item in

ct

.

A

TabularType

is assignable from another

TabularType

if they have the same

typeName

and

index name list

, and the

row type

of the first is
assignable from the row type of the second.

An

ArrayType

is assignable from another

ArrayType

if they have the same

dimension

; and both are

primitive arrays

or neither is;
and the

element
type

of the first is assignable from the element type of the
second.

In every other case, an

OpenType

is assignable from
another

OpenType

only if they are equal.

These rules mean that extra items can be added to a

CompositeData

without making it invalid for a

CompositeType

that does not have those items.

**Specified by:** isValue

in class

OpenType

<

CompositeData

>
**Parameters:** obj

- the value whose open type is to be tested for compatibility
with this

CompositeType

instance.
**Returns:** true

if

obj

is a value for this
composite type,

false

otherwise.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

CompositeType

instance for equality.

Two

CompositeType

instances are equal if and only if all of the following statements are true:

- their type names are equal
- their items' names and types are equal

**Specified by:** equals

in class

OpenType

<

CompositeData

>
**Parameters:** obj

- the object to be compared for equality with this

CompositeType

instance;
if

obj

is

null

,

equals

returns

false

.
**Returns:** true

if the specified object is equal to this

CompositeType

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

CompositeType

instance.

The hash code of a

CompositeType

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: name, items names, items types).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

CompositeType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

CompositeType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

CompositeType

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

CompositeType

instance.

The string representation consists of
the name of this class (ie

javax.management.openmbean.CompositeType

), the type name for this instance,
and the list of the items names and types string representation of this instance.

As

CompositeType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

**Specified by:** toString

in class

OpenType

<

CompositeData

>
**Returns:** a string representation of this

CompositeType

instance

Constructor Detail

- CompositeType

```java
public CompositeType​(
String
typeName,

String
description,

String
[] itemNames,

String
[] itemDescriptions,

OpenType
<?>[] itemTypes)
throws
OpenDataException
```

Constructs a

CompositeType

instance, checking for the validity of the given parameters.
The validity constraints are described below for each parameter.

Note that the contents of the three array parameters

itemNames

,

itemDescriptions

and

itemTypes

are internally copied so that any subsequent modification of these arrays by the caller of this constructor
has no impact on the constructed

CompositeType

instance.

The Java class name of composite data values this composite type represents
(ie the class name returned by the

getClassName

method)
is set to the string value returned by

CompositeData.class.getName()

.

**Parameters:** typeName

- The name given to the composite type this instance represents; cannot be a null or empty string.
**Parameters:** description

- The human readable description of the composite type this instance represents;
cannot be a null or empty string.
**Parameters:** itemNames

- The names of the items contained in the
composite data values described by this

CompositeType

instance;
cannot be null and should contain at least one element; no element can be a null or empty string.
Note that the order in which the item names are given is not important to differentiate a

CompositeType

instance from another;
the item names are internally stored sorted in ascending alphanumeric order.
**Parameters:** itemDescriptions

- The descriptions, in the same order as

itemNames

, of the items contained in the
composite data values described by this

CompositeType

instance;
should be of the same size as

itemNames

;
no element can be null or an empty string.
**Parameters:** itemTypes

- The open type instances, in the same order as

itemNames

, describing the items contained
in the composite data values described by this

CompositeType

instance;
should be of the same size as

itemNames

;
no element can be null.
**Throws:** IllegalArgumentException

- If

typeName

or

description

is a null or empty string,
or

itemNames

or

itemDescriptions

or

itemTypes

is null,
or any element of

itemNames

or

itemDescriptions

is a null or empty string,
or any element of

itemTypes

is null,
or

itemNames

or

itemDescriptions

or

itemTypes

are not of the same size.
**Throws:** OpenDataException

- If

itemNames

contains duplicate item names
(case sensitive, but leading and trailing whitespaces removed).

---

#### Constructor Detail

CompositeType

```java
public CompositeType​(
String
typeName,

String
description,

String
[] itemNames,

String
[] itemDescriptions,

OpenType
<?>[] itemTypes)
throws
OpenDataException
```

Constructs a

CompositeType

instance, checking for the validity of the given parameters.
The validity constraints are described below for each parameter.

Note that the contents of the three array parameters

itemNames

,

itemDescriptions

and

itemTypes

are internally copied so that any subsequent modification of these arrays by the caller of this constructor
has no impact on the constructed

CompositeType

instance.

The Java class name of composite data values this composite type represents
(ie the class name returned by the

getClassName

method)
is set to the string value returned by

CompositeData.class.getName()

.

**Parameters:** typeName

- The name given to the composite type this instance represents; cannot be a null or empty string.
**Parameters:** description

- The human readable description of the composite type this instance represents;
cannot be a null or empty string.
**Parameters:** itemNames

- The names of the items contained in the
composite data values described by this

CompositeType

instance;
cannot be null and should contain at least one element; no element can be a null or empty string.
Note that the order in which the item names are given is not important to differentiate a

CompositeType

instance from another;
the item names are internally stored sorted in ascending alphanumeric order.
**Parameters:** itemDescriptions

- The descriptions, in the same order as

itemNames

, of the items contained in the
composite data values described by this

CompositeType

instance;
should be of the same size as

itemNames

;
no element can be null or an empty string.
**Parameters:** itemTypes

- The open type instances, in the same order as

itemNames

, describing the items contained
in the composite data values described by this

CompositeType

instance;
should be of the same size as

itemNames

;
no element can be null.
**Throws:** IllegalArgumentException

- If

typeName

or

description

is a null or empty string,
or

itemNames

or

itemDescriptions

or

itemTypes

is null,
or any element of

itemNames

or

itemDescriptions

is a null or empty string,
or any element of

itemTypes

is null,
or

itemNames

or

itemDescriptions

or

itemTypes

are not of the same size.
**Throws:** OpenDataException

- If

itemNames

contains duplicate item names
(case sensitive, but leading and trailing whitespaces removed).

---

#### CompositeType

public CompositeType​(

String

typeName,

String

description,

String

[] itemNames,

String

[] itemDescriptions,

OpenType

<?>[] itemTypes)
throws

OpenDataException

Constructs a

CompositeType

instance, checking for the validity of the given parameters.
The validity constraints are described below for each parameter.

Note that the contents of the three array parameters

itemNames

,

itemDescriptions

and

itemTypes

are internally copied so that any subsequent modification of these arrays by the caller of this constructor
has no impact on the constructed

CompositeType

instance.

The Java class name of composite data values this composite type represents
(ie the class name returned by the

getClassName

method)
is set to the string value returned by

CompositeData.class.getName()

.

Note that the contents of the three array parameters

itemNames

,

itemDescriptions

and

itemTypes

are internally copied so that any subsequent modification of these arrays by the caller of this constructor
has no impact on the constructed

CompositeType

instance.

The Java class name of composite data values this composite type represents
(ie the class name returned by the

getClassName

method)
is set to the string value returned by

CompositeData.class.getName()

.

The Java class name of composite data values this composite type represents
(ie the class name returned by the

getClassName

method)
is set to the string value returned by

CompositeData.class.getName()

.

Method Detail

- containsKey

```java
public boolean containsKey​(
String
itemName)
```

Returns

true

if this

CompositeType

instance defines an item
whose name is

itemName

.

**Parameters:** itemName

- the name of the item.
**Returns:** true if an item of this name is present.

- getDescription

```java
public
String
getDescription​(
String
itemName)
```

Returns the description of the item whose name is

itemName

,
or

null

if this

CompositeType

instance does not define any item
whose name is

itemName

.

**Parameters:** itemName

- the name of the item.
**Returns:** the description.

- getType

```java
public
OpenType
<?> getType​(
String
itemName)
```

Returns the

open type

of the item whose name is

itemName

,
or

null

if this

CompositeType

instance does not define any item
whose name is

itemName

.

**Parameters:** itemName

- the name of the time.
**Returns:** the type.

- keySet

```java
public
Set
<
String
> keySet()
```

Returns an unmodifiable Set view of all the item names defined by this

CompositeType

instance.
The set's iterator will return the item names in ascending order.

**Returns:** a

Set

of

String

.

- isValue

```java
public boolean isValue​(
Object
obj)
```

Tests whether

obj

is a value which could be
described by this

CompositeType

instance.

If

obj

is null or is not an instance of

javax.management.openmbean.CompositeData

,

isValue

returns

false

.

If

obj

is an instance of

javax.management.openmbean.CompositeData

, then let

ct

be its

CompositeType

as returned by

CompositeData.getCompositeType()

. The result is true if

this

is

assignable from

ct

. This
means that:

- this.getTypeName()

equals

ct.getTypeName()

, and

there are no item names present in

this

that are
not also present in

ct

, and

for every item in

this

, its type is assignable from
the type of the corresponding item in

ct

.

A

TabularType

is assignable from another

TabularType

if they have the same

typeName

and

index name list

, and the

row type

of the first is
assignable from the row type of the second.

An

ArrayType

is assignable from another

ArrayType

if they have the same

dimension

; and both are

primitive arrays

or neither is;
and the

element
type

of the first is assignable from the element type of the
second.

In every other case, an

OpenType

is assignable from
another

OpenType

only if they are equal.

These rules mean that extra items can be added to a

CompositeData

without making it invalid for a

CompositeType

that does not have those items.

**Specified by:** isValue

in class

OpenType

<

CompositeData

>
**Parameters:** obj

- the value whose open type is to be tested for compatibility
with this

CompositeType

instance.
**Returns:** true

if

obj

is a value for this
composite type,

false

otherwise.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

CompositeType

instance for equality.

Two

CompositeType

instances are equal if and only if all of the following statements are true:

- their type names are equal
- their items' names and types are equal

**Specified by:** equals

in class

OpenType

<

CompositeData

>
**Parameters:** obj

- the object to be compared for equality with this

CompositeType

instance;
if

obj

is

null

,

equals

returns

false

.
**Returns:** true

if the specified object is equal to this

CompositeType

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

CompositeType

instance.

The hash code of a

CompositeType

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: name, items names, items types).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

CompositeType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

CompositeType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

CompositeType

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

CompositeType

instance.

The string representation consists of
the name of this class (ie

javax.management.openmbean.CompositeType

), the type name for this instance,
and the list of the items names and types string representation of this instance.

As

CompositeType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

**Specified by:** toString

in class

OpenType

<

CompositeData

>
**Returns:** a string representation of this

CompositeType

instance

---

#### Method Detail

containsKey

```java
public boolean containsKey​(
String
itemName)
```

Returns

true

if this

CompositeType

instance defines an item
whose name is

itemName

.

**Parameters:** itemName

- the name of the item.
**Returns:** true if an item of this name is present.

---

#### containsKey

public boolean containsKey​(

String

itemName)

Returns

true

if this

CompositeType

instance defines an item
whose name is

itemName

.

getDescription

```java
public
String
getDescription​(
String
itemName)
```

Returns the description of the item whose name is

itemName

,
or

null

if this

CompositeType

instance does not define any item
whose name is

itemName

.

**Parameters:** itemName

- the name of the item.
**Returns:** the description.

---

#### getDescription

public

String

getDescription​(

String

itemName)

Returns the description of the item whose name is

itemName

,
or

null

if this

CompositeType

instance does not define any item
whose name is

itemName

.

getType

```java
public
OpenType
<?> getType​(
String
itemName)
```

Returns the

open type

of the item whose name is

itemName

,
or

null

if this

CompositeType

instance does not define any item
whose name is

itemName

.

**Parameters:** itemName

- the name of the time.
**Returns:** the type.

---

#### getType

public

OpenType

<?> getType​(

String

itemName)

Returns the

open type

of the item whose name is

itemName

,
or

null

if this

CompositeType

instance does not define any item
whose name is

itemName

.

keySet

```java
public
Set
<
String
> keySet()
```

Returns an unmodifiable Set view of all the item names defined by this

CompositeType

instance.
The set's iterator will return the item names in ascending order.

**Returns:** a

Set

of

String

.

---

#### keySet

public

Set

<

String

> keySet()

Returns an unmodifiable Set view of all the item names defined by this

CompositeType

instance.
The set's iterator will return the item names in ascending order.

isValue

```java
public boolean isValue​(
Object
obj)
```

Tests whether

obj

is a value which could be
described by this

CompositeType

instance.

If

obj

is null or is not an instance of

javax.management.openmbean.CompositeData

,

isValue

returns

false

.

If

obj

is an instance of

javax.management.openmbean.CompositeData

, then let

ct

be its

CompositeType

as returned by

CompositeData.getCompositeType()

. The result is true if

this

is

assignable from

ct

. This
means that:

- this.getTypeName()

equals

ct.getTypeName()

, and

there are no item names present in

this

that are
not also present in

ct

, and

for every item in

this

, its type is assignable from
the type of the corresponding item in

ct

.

A

TabularType

is assignable from another

TabularType

if they have the same

typeName

and

index name list

, and the

row type

of the first is
assignable from the row type of the second.

An

ArrayType

is assignable from another

ArrayType

if they have the same

dimension

; and both are

primitive arrays

or neither is;
and the

element
type

of the first is assignable from the element type of the
second.

In every other case, an

OpenType

is assignable from
another

OpenType

only if they are equal.

These rules mean that extra items can be added to a

CompositeData

without making it invalid for a

CompositeType

that does not have those items.

**Specified by:** isValue

in class

OpenType

<

CompositeData

>
**Parameters:** obj

- the value whose open type is to be tested for compatibility
with this

CompositeType

instance.
**Returns:** true

if

obj

is a value for this
composite type,

false

otherwise.

---

#### isValue

public boolean isValue​(

Object

obj)

Tests whether

obj

is a value which could be
described by this

CompositeType

instance.

If

obj

is null or is not an instance of

javax.management.openmbean.CompositeData

,

isValue

returns

false

.

If

obj

is an instance of

javax.management.openmbean.CompositeData

, then let

ct

be its

CompositeType

as returned by

CompositeData.getCompositeType()

. The result is true if

this

is

assignable from

ct

. This
means that:

- this.getTypeName()

equals

ct.getTypeName()

, and

there are no item names present in

this

that are
not also present in

ct

, and

for every item in

this

, its type is assignable from
the type of the corresponding item in

ct

.

A

TabularType

is assignable from another

TabularType

if they have the same

typeName

and

index name list

, and the

row type

of the first is
assignable from the row type of the second.

An

ArrayType

is assignable from another

ArrayType

if they have the same

dimension

; and both are

primitive arrays

or neither is;
and the

element
type

of the first is assignable from the element type of the
second.

In every other case, an

OpenType

is assignable from
another

OpenType

only if they are equal.

These rules mean that extra items can be added to a

CompositeData

without making it invalid for a

CompositeType

that does not have those items.

If

obj

is null or is not an instance of

javax.management.openmbean.CompositeData

,

isValue

returns

false

.

If

obj

is an instance of

javax.management.openmbean.CompositeData

, then let

ct

be its

CompositeType

as returned by

CompositeData.getCompositeType()

. The result is true if

this

is

assignable from

ct

. This
means that:

this.getTypeName()

equals

ct.getTypeName()

, and

there are no item names present in

this

that are
not also present in

ct

, and

for every item in

this

, its type is assignable from
the type of the corresponding item in

ct

.

A

TabularType

is assignable from another

TabularType

if they have the same

typeName

and

index name list

, and the

row type

of the first is
assignable from the row type of the second.

An

ArrayType

is assignable from another

ArrayType

if they have the same

dimension

; and both are

primitive arrays

or neither is;
and the

element
type

of the first is assignable from the element type of the
second.

In every other case, an

OpenType

is assignable from
another

OpenType

only if they are equal.

These rules mean that extra items can be added to a

CompositeData

without making it invalid for a

CompositeType

that does not have those items.

An

ArrayType

is assignable from another

ArrayType

if they have the same

dimension

; and both are

primitive arrays

or neither is;
and the

element
type

of the first is assignable from the element type of the
second.

In every other case, an

OpenType

is assignable from
another

OpenType

only if they are equal.

These rules mean that extra items can be added to a

CompositeData

without making it invalid for a

CompositeType

that does not have those items.

In every other case, an

OpenType

is assignable from
another

OpenType

only if they are equal.

These rules mean that extra items can be added to a

CompositeData

without making it invalid for a

CompositeType

that does not have those items.

equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

CompositeType

instance for equality.

Two

CompositeType

instances are equal if and only if all of the following statements are true:

- their type names are equal
- their items' names and types are equal

**Specified by:** equals

in class

OpenType

<

CompositeData

>
**Parameters:** obj

- the object to be compared for equality with this

CompositeType

instance;
if

obj

is

null

,

equals

returns

false

.
**Returns:** true

if the specified object is equal to this

CompositeType

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

CompositeType

instance for equality.

Two

CompositeType

instances are equal if and only if all of the following statements are true:

- their type names are equal
- their items' names and types are equal

Two

CompositeType

instances are equal if and only if all of the following statements are true:

- their type names are equal
- their items' names and types are equal

their type names are equal

their items' names and types are equal

hashCode

```java
public int hashCode()
```

Returns the hash code value for this

CompositeType

instance.

The hash code of a

CompositeType

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: name, items names, items types).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

CompositeType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

CompositeType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

CompositeType

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this

CompositeType

instance.

The hash code of a

CompositeType

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: name, items names, items types).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

CompositeType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

CompositeType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

The hash code of a

CompositeType

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: name, items names, items types).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

CompositeType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

CompositeType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

As

CompositeType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

toString

```java
public
String
toString()
```

Returns a string representation of this

CompositeType

instance.

The string representation consists of
the name of this class (ie

javax.management.openmbean.CompositeType

), the type name for this instance,
and the list of the items names and types string representation of this instance.

As

CompositeType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

**Specified by:** toString

in class

OpenType

<

CompositeData

>
**Returns:** a string representation of this

CompositeType

instance

---

#### toString

public

String

toString()

Returns a string representation of this

CompositeType

instance.

The string representation consists of
the name of this class (ie

javax.management.openmbean.CompositeType

), the type name for this instance,
and the list of the items names and types string representation of this instance.

As

CompositeType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

The string representation consists of
the name of this class (ie

javax.management.openmbean.CompositeType

), the type name for this instance,
and the list of the items names and types string representation of this instance.

As

CompositeType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

As

CompositeType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

---

