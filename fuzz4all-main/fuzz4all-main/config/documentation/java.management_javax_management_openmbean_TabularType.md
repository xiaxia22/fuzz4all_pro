# Class TabularType

**Source:** `java.management\javax\management\openmbean\TabularType.html`

### Class Description

```java
public class
TabularType

extends
OpenType
<
TabularData
>
```

The

TabularType

class is the

open type

class
whose instances describe the types of

TabularData

values.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public TabularType​(
String
typeName,

String
description,

CompositeType
rowType,

String
[] indexNames)
throws
OpenDataException

Constructs a

TabularType

instance, checking for the validity of the given parameters.
The validity constraints are described below for each parameter.

The Java class name of tabular data values this tabular type represents
(ie the class name returned by the

getClassName

method)
is set to the string value returned by

TabularData.class.getName()

.

**Parameters:**
- typeName

- The name given to the tabular type this instance represents; cannot be a null or empty string.
- description

- The human readable description of the tabular type this instance represents;
cannot be a null or empty string.
- rowType

- The type of the row elements of tabular data values described by this tabular type instance;
cannot be null.
- indexNames

- The names of the items the values of which are used to uniquely index each row element in the
tabular data values described by this tabular type instance;
cannot be null or empty. Each element should be an item name defined in

rowType

(no null or empty string allowed).
It is important to note that the

order

of the item names in

indexNames

is used by the methods

get

and

remove

of class

TabularData

to match their array of values parameter to items.

**Throws:**
- IllegalArgumentException

- if

rowType

is null,
or

indexNames

is a null or empty array,
or an element in

indexNames

is a null or empty string,
or

typeName

or

description

is a null or empty string.
- OpenDataException

- if an element's value of

indexNames

is not an item name defined in

rowType

.

---

### Method Details

#### public
CompositeType
getRowType()

Returns the type of the row elements of tabular data values
described by this

TabularType

instance.

**Returns:**
- the type of each row.

---

#### public
List
<
String
> getIndexNames()

Returns, in the same order as was given to this instance's
constructor, an unmodifiable List of the names of the items the
values of which are used to uniquely index each row element of
tabular data values described by this

TabularType

instance.

**Returns:**
- a List of String representing the names of the index
items.

---

#### public boolean isValue​(
Object
obj)

Tests whether

obj

is a value which could be
described by this

TabularType

instance.

If

obj

is null or is not an instance of

javax.management.openmbean.TabularData

,

isValue

returns

false

.

If

obj

is an instance of

javax.management.openmbean.TabularData

, say

td

, the result is true if this

TabularType

is

assignable from

td.getTabularType()

, as defined in

CompositeType.isValue

.

**Specified by:**
- isValue

in class

OpenType

<

TabularData

>

**Parameters:**
- obj

- the value whose open type is to be tested for
compatibility with this

TabularType

instance.

**Returns:**
- true

if

obj

is a value for this
tabular type,

false

otherwise.

---

#### public boolean equals​(
Object
obj)

Compares the specified

obj

parameter with this

TabularType

instance for equality.

Two

TabularType

instances are equal if and only if all of the following statements are true:

- their type names are equal
- their row types are equal
- they use the same index names, in the same order

**Specified by:**
- equals

in class

OpenType

<

TabularData

>

**Parameters:**
- obj

- the object to be compared for equality with this

TabularType

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

TabularType

instance.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this

TabularType

instance.

The hash code of a

TabularType

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: name, row type, index names).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

TabularType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

TabularType

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

TabularType

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

TabularType

instance.

The string representation consists of the name of this class (ie

javax.management.openmbean.TabularType

),
the type name for this instance, the row type string representation of this instance,
and the index names of this instance.

As

TabularType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

**Specified by:**
- toString

in class

OpenType

<

TabularData

>

**Returns:**
- a string representation of this

TabularType

instance

---

### Additional Sections

#### Class TabularType

java.lang.Object

- javax.management.openmbean.OpenType

<

TabularData

>
- - javax.management.openmbean.TabularType

javax.management.openmbean.OpenType

<

TabularData

>

- javax.management.openmbean.TabularType

javax.management.openmbean.TabularType

**All Implemented Interfaces:** Serializable

```java
public class
TabularType

extends
OpenType
<
TabularData
>
```

The

TabularType

class is the

open type

class
whose instances describe the types of

TabularData

values.

**Since:** 1.5
**See Also:** Serialized Form

public class

TabularType

extends

OpenType

<

TabularData

>

The

TabularType

class is the

open type

class
whose instances describe the types of

TabularData

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

TabularType

​(

String

typeName,

String

description,

CompositeType

rowType,

String

[] indexNames)

Constructs a

TabularType

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

equals

​(

Object

obj)

Compares the specified

obj

parameter with this

TabularType

instance for equality.

List

<

String

>

getIndexNames

()

Returns, in the same order as was given to this instance's
constructor, an unmodifiable List of the names of the items the
values of which are used to uniquely index each row element of
tabular data values described by this

TabularType

instance.

CompositeType

getRowType

()

Returns the type of the row elements of tabular data values
described by this

TabularType

instance.

int

hashCode

()

Returns the hash code value for this

TabularType

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

TabularType

instance.

String

toString

()

Returns a string representation of this

TabularType

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

TabularType

​(

String

typeName,

String

description,

CompositeType

rowType,

String

[] indexNames)

Constructs a

TabularType

instance, checking for the validity of the given parameters.

---

#### Constructor Summary

Constructs a

TabularType

instance, checking for the validity of the given parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares the specified

obj

parameter with this

TabularType

instance for equality.

List

<

String

>

getIndexNames

()

Returns, in the same order as was given to this instance's
constructor, an unmodifiable List of the names of the items the
values of which are used to uniquely index each row element of
tabular data values described by this

TabularType

instance.

CompositeType

getRowType

()

Returns the type of the row elements of tabular data values
described by this

TabularType

instance.

int

hashCode

()

Returns the hash code value for this

TabularType

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

TabularType

instance.

String

toString

()

Returns a string representation of this

TabularType

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

Compares the specified

obj

parameter with this

TabularType

instance for equality.

Returns, in the same order as was given to this instance's
constructor, an unmodifiable List of the names of the items the
values of which are used to uniquely index each row element of
tabular data values described by this

TabularType

instance.

Returns the type of the row elements of tabular data values
described by this

TabularType

instance.

Returns the hash code value for this

TabularType

instance.

Tests whether

obj

is a value which could be
described by this

TabularType

instance.

Returns a string representation of this

TabularType

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

- TabularType

```java
public TabularType​(
String
typeName,

String
description,

CompositeType
rowType,

String
[] indexNames)
throws
OpenDataException
```

Constructs a

TabularType

instance, checking for the validity of the given parameters.
The validity constraints are described below for each parameter.

The Java class name of tabular data values this tabular type represents
(ie the class name returned by the

getClassName

method)
is set to the string value returned by

TabularData.class.getName()

.

**Parameters:** typeName

- The name given to the tabular type this instance represents; cannot be a null or empty string.
**Parameters:** description

- The human readable description of the tabular type this instance represents;
cannot be a null or empty string.
**Parameters:** rowType

- The type of the row elements of tabular data values described by this tabular type instance;
cannot be null.
**Parameters:** indexNames

- The names of the items the values of which are used to uniquely index each row element in the
tabular data values described by this tabular type instance;
cannot be null or empty. Each element should be an item name defined in

rowType

(no null or empty string allowed).
It is important to note that the

order

of the item names in

indexNames

is used by the methods

get

and

remove

of class

TabularData

to match their array of values parameter to items.
**Throws:** IllegalArgumentException

- if

rowType

is null,
or

indexNames

is a null or empty array,
or an element in

indexNames

is a null or empty string,
or

typeName

or

description

is a null or empty string.
**Throws:** OpenDataException

- if an element's value of

indexNames

is not an item name defined in

rowType

.

============ METHOD DETAIL ==========

- Method Detail

- getRowType

```java
public
CompositeType
getRowType()
```

Returns the type of the row elements of tabular data values
described by this

TabularType

instance.

**Returns:** the type of each row.

- getIndexNames

```java
public
List
<
String
> getIndexNames()
```

Returns, in the same order as was given to this instance's
constructor, an unmodifiable List of the names of the items the
values of which are used to uniquely index each row element of
tabular data values described by this

TabularType

instance.

**Returns:** a List of String representing the names of the index
items.

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

TabularType

instance.

If

obj

is null or is not an instance of

javax.management.openmbean.TabularData

,

isValue

returns

false

.

If

obj

is an instance of

javax.management.openmbean.TabularData

, say

td

, the result is true if this

TabularType

is

assignable from

td.getTabularType()

, as defined in

CompositeType.isValue

.

**Specified by:** isValue

in class

OpenType

<

TabularData

>
**Parameters:** obj

- the value whose open type is to be tested for
compatibility with this

TabularType

instance.
**Returns:** true

if

obj

is a value for this
tabular type,

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

TabularType

instance for equality.

Two

TabularType

instances are equal if and only if all of the following statements are true:

- their type names are equal
- their row types are equal
- they use the same index names, in the same order

**Specified by:** equals

in class

OpenType

<

TabularData

>
**Parameters:** obj

- the object to be compared for equality with this

TabularType

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

TabularType

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

TabularType

instance.

The hash code of a

TabularType

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: name, row type, index names).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

TabularType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

TabularType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

TabularType

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

TabularType

instance.

The string representation consists of the name of this class (ie

javax.management.openmbean.TabularType

),
the type name for this instance, the row type string representation of this instance,
and the index names of this instance.

As

TabularType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

**Specified by:** toString

in class

OpenType

<

TabularData

>
**Returns:** a string representation of this

TabularType

instance

Constructor Detail

- TabularType

```java
public TabularType​(
String
typeName,

String
description,

CompositeType
rowType,

String
[] indexNames)
throws
OpenDataException
```

Constructs a

TabularType

instance, checking for the validity of the given parameters.
The validity constraints are described below for each parameter.

The Java class name of tabular data values this tabular type represents
(ie the class name returned by the

getClassName

method)
is set to the string value returned by

TabularData.class.getName()

.

**Parameters:** typeName

- The name given to the tabular type this instance represents; cannot be a null or empty string.
**Parameters:** description

- The human readable description of the tabular type this instance represents;
cannot be a null or empty string.
**Parameters:** rowType

- The type of the row elements of tabular data values described by this tabular type instance;
cannot be null.
**Parameters:** indexNames

- The names of the items the values of which are used to uniquely index each row element in the
tabular data values described by this tabular type instance;
cannot be null or empty. Each element should be an item name defined in

rowType

(no null or empty string allowed).
It is important to note that the

order

of the item names in

indexNames

is used by the methods

get

and

remove

of class

TabularData

to match their array of values parameter to items.
**Throws:** IllegalArgumentException

- if

rowType

is null,
or

indexNames

is a null or empty array,
or an element in

indexNames

is a null or empty string,
or

typeName

or

description

is a null or empty string.
**Throws:** OpenDataException

- if an element's value of

indexNames

is not an item name defined in

rowType

.

---

#### Constructor Detail

TabularType

```java
public TabularType​(
String
typeName,

String
description,

CompositeType
rowType,

String
[] indexNames)
throws
OpenDataException
```

Constructs a

TabularType

instance, checking for the validity of the given parameters.
The validity constraints are described below for each parameter.

The Java class name of tabular data values this tabular type represents
(ie the class name returned by the

getClassName

method)
is set to the string value returned by

TabularData.class.getName()

.

**Parameters:** typeName

- The name given to the tabular type this instance represents; cannot be a null or empty string.
**Parameters:** description

- The human readable description of the tabular type this instance represents;
cannot be a null or empty string.
**Parameters:** rowType

- The type of the row elements of tabular data values described by this tabular type instance;
cannot be null.
**Parameters:** indexNames

- The names of the items the values of which are used to uniquely index each row element in the
tabular data values described by this tabular type instance;
cannot be null or empty. Each element should be an item name defined in

rowType

(no null or empty string allowed).
It is important to note that the

order

of the item names in

indexNames

is used by the methods

get

and

remove

of class

TabularData

to match their array of values parameter to items.
**Throws:** IllegalArgumentException

- if

rowType

is null,
or

indexNames

is a null or empty array,
or an element in

indexNames

is a null or empty string,
or

typeName

or

description

is a null or empty string.
**Throws:** OpenDataException

- if an element's value of

indexNames

is not an item name defined in

rowType

.

---

#### TabularType

public TabularType​(

String

typeName,

String

description,

CompositeType

rowType,

String

[] indexNames)
throws

OpenDataException

Constructs a

TabularType

instance, checking for the validity of the given parameters.
The validity constraints are described below for each parameter.

The Java class name of tabular data values this tabular type represents
(ie the class name returned by the

getClassName

method)
is set to the string value returned by

TabularData.class.getName()

.

The Java class name of tabular data values this tabular type represents
(ie the class name returned by the

getClassName

method)
is set to the string value returned by

TabularData.class.getName()

.

Method Detail

- getRowType

```java
public
CompositeType
getRowType()
```

Returns the type of the row elements of tabular data values
described by this

TabularType

instance.

**Returns:** the type of each row.

- getIndexNames

```java
public
List
<
String
> getIndexNames()
```

Returns, in the same order as was given to this instance's
constructor, an unmodifiable List of the names of the items the
values of which are used to uniquely index each row element of
tabular data values described by this

TabularType

instance.

**Returns:** a List of String representing the names of the index
items.

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

TabularType

instance.

If

obj

is null or is not an instance of

javax.management.openmbean.TabularData

,

isValue

returns

false

.

If

obj

is an instance of

javax.management.openmbean.TabularData

, say

td

, the result is true if this

TabularType

is

assignable from

td.getTabularType()

, as defined in

CompositeType.isValue

.

**Specified by:** isValue

in class

OpenType

<

TabularData

>
**Parameters:** obj

- the value whose open type is to be tested for
compatibility with this

TabularType

instance.
**Returns:** true

if

obj

is a value for this
tabular type,

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

TabularType

instance for equality.

Two

TabularType

instances are equal if and only if all of the following statements are true:

- their type names are equal
- their row types are equal
- they use the same index names, in the same order

**Specified by:** equals

in class

OpenType

<

TabularData

>
**Parameters:** obj

- the object to be compared for equality with this

TabularType

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

TabularType

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

TabularType

instance.

The hash code of a

TabularType

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: name, row type, index names).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

TabularType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

TabularType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

TabularType

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

TabularType

instance.

The string representation consists of the name of this class (ie

javax.management.openmbean.TabularType

),
the type name for this instance, the row type string representation of this instance,
and the index names of this instance.

As

TabularType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

**Specified by:** toString

in class

OpenType

<

TabularData

>
**Returns:** a string representation of this

TabularType

instance

---

#### Method Detail

getRowType

```java
public
CompositeType
getRowType()
```

Returns the type of the row elements of tabular data values
described by this

TabularType

instance.

**Returns:** the type of each row.

---

#### getRowType

public

CompositeType

getRowType()

Returns the type of the row elements of tabular data values
described by this

TabularType

instance.

getIndexNames

```java
public
List
<
String
> getIndexNames()
```

Returns, in the same order as was given to this instance's
constructor, an unmodifiable List of the names of the items the
values of which are used to uniquely index each row element of
tabular data values described by this

TabularType

instance.

**Returns:** a List of String representing the names of the index
items.

---

#### getIndexNames

public

List

<

String

> getIndexNames()

Returns, in the same order as was given to this instance's
constructor, an unmodifiable List of the names of the items the
values of which are used to uniquely index each row element of
tabular data values described by this

TabularType

instance.

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

TabularType

instance.

If

obj

is null or is not an instance of

javax.management.openmbean.TabularData

,

isValue

returns

false

.

If

obj

is an instance of

javax.management.openmbean.TabularData

, say

td

, the result is true if this

TabularType

is

assignable from

td.getTabularType()

, as defined in

CompositeType.isValue

.

**Specified by:** isValue

in class

OpenType

<

TabularData

>
**Parameters:** obj

- the value whose open type is to be tested for
compatibility with this

TabularType

instance.
**Returns:** true

if

obj

is a value for this
tabular type,

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

TabularType

instance.

If

obj

is null or is not an instance of

javax.management.openmbean.TabularData

,

isValue

returns

false

.

If

obj

is an instance of

javax.management.openmbean.TabularData

, say

td

, the result is true if this

TabularType

is

assignable from

td.getTabularType()

, as defined in

CompositeType.isValue

.

If

obj

is null or is not an instance of

javax.management.openmbean.TabularData

,

isValue

returns

false

.

If

obj

is an instance of

javax.management.openmbean.TabularData

, say

td

, the result is true if this

TabularType

is

assignable from

td.getTabularType()

, as defined in

CompositeType.isValue

.

equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

TabularType

instance for equality.

Two

TabularType

instances are equal if and only if all of the following statements are true:

- their type names are equal
- their row types are equal
- they use the same index names, in the same order

**Specified by:** equals

in class

OpenType

<

TabularData

>
**Parameters:** obj

- the object to be compared for equality with this

TabularType

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

TabularType

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

TabularType

instance for equality.

Two

TabularType

instances are equal if and only if all of the following statements are true:

- their type names are equal
- their row types are equal
- they use the same index names, in the same order

Two

TabularType

instances are equal if and only if all of the following statements are true:

- their type names are equal
- their row types are equal
- they use the same index names, in the same order

their type names are equal

their row types are equal

they use the same index names, in the same order

hashCode

```java
public int hashCode()
```

Returns the hash code value for this

TabularType

instance.

The hash code of a

TabularType

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: name, row type, index names).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

TabularType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

TabularType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

TabularType

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this

TabularType

instance.

The hash code of a

TabularType

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: name, row type, index names).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

TabularType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

TabularType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

The hash code of a

TabularType

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: name, row type, index names).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

TabularType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

TabularType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

As

TabularType

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

TabularType

instance.

The string representation consists of the name of this class (ie

javax.management.openmbean.TabularType

),
the type name for this instance, the row type string representation of this instance,
and the index names of this instance.

As

TabularType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

**Specified by:** toString

in class

OpenType

<

TabularData

>
**Returns:** a string representation of this

TabularType

instance

---

#### toString

public

String

toString()

Returns a string representation of this

TabularType

instance.

The string representation consists of the name of this class (ie

javax.management.openmbean.TabularType

),
the type name for this instance, the row type string representation of this instance,
and the index names of this instance.

As

TabularType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

The string representation consists of the name of this class (ie

javax.management.openmbean.TabularType

),
the type name for this instance, the row type string representation of this instance,
and the index names of this instance.

As

TabularType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

As

TabularType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

---

