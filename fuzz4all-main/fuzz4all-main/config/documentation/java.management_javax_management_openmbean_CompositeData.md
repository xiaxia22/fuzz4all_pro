# Interface CompositeData

**Source:** `java.management\javax\management\openmbean\CompositeData.html`

### Class Description

```java
public interface
CompositeData
```

The

CompositeData

interface specifies
the behavior of a specific type of complex

open data

objects
which represent

composite data

structures.

**All Known Implementing Classes:** CompositeDataSupport

,

GcInfo

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### CompositeType
getCompositeType()

Returns the

composite type

of this

composite data

instance.

**Returns:**
- the type of this CompositeData.

---

#### Object
get​(
String
key)

Returns the value of the item whose name is

key

.

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

is not an
existing item name for this

CompositeData

instance.

---

#### Object
[] getAll​(
String
[] keys)

Returns an array of the values of the items whose names
are specified by

keys

, in the same order as

keys

.

**Parameters:**
- keys

- the names of the items.

**Returns:**
- the values corresponding to the keys.

**Throws:**
- IllegalArgumentException

- if an element in

keys

is a null or empty String.
- InvalidKeyException

- if an element in

keys

is not an existing item name for this

CompositeData

instance.

---

#### boolean containsKey​(
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

**Parameters:**
- key

- the key to be tested.

**Returns:**
- true if this

CompositeData

contains the key.

---

#### boolean containsValue​(
Object
value)

Returns

true

if and only if this

CompositeData

instance contains an item
whose value is

value

.

**Parameters:**
- value

- the value to be tested.

**Returns:**
- true if this

CompositeData

contains the value.

---

#### Collection
<?> values()

Returns an unmodifiable Collection view of the item values
contained in this

CompositeData

instance.
The returned collection's iterator will return the values
in the ascending lexicographic order of the corresponding
item names.

**Returns:**
- the values.

---

#### boolean equals​(
Object
obj)

Compares the specified

obj

parameter with this

CompositeData

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

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to be compared for equality with this

CompositeData

instance.

**Returns:**
- true

if the specified object is equal to this

CompositeData

instance.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this

CompositeData

instance.

The hash code of a

CompositeData

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

CompositeData

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

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this

CompositeData

instance

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### String
toString()

Returns a string representation of this

CompositeData

instance.

The string representation consists of the name of the implementing class,
the string representation of the composite type of this instance,
and the string representation of the contents
(ie list the itemName=itemValue mappings).

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

CompositeData

instance

---

### Additional Sections

#### Interface CompositeData

**All Known Implementing Classes:** CompositeDataSupport

,

GcInfo

```java
public interface
CompositeData
```

The

CompositeData

interface specifies
the behavior of a specific type of complex

open data

objects
which represent

composite data

structures.

**Since:** 1.5

public interface

CompositeData

The

CompositeData

interface specifies
the behavior of a specific type of complex

open data

objects
which represent

composite data

structures.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

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

instance contains an item
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

CompositeData

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

Returns an array of the values of the items whose names
are specified by

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

CompositeData

instance.

String

toString

()

Returns a string representation of this

CompositeData

instance.

Collection

<?>

values

()

Returns an unmodifiable Collection view of the item values
contained in this

CompositeData

instance.

Method Summary

All Methods

Instance Methods

Abstract Methods

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

instance contains an item
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

CompositeData

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

Returns an array of the values of the items whose names
are specified by

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

CompositeData

instance.

String

toString

()

Returns a string representation of this

CompositeData

instance.

Collection

<?>

values

()

Returns an unmodifiable Collection view of the item values
contained in this

CompositeData

instance.

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

instance contains an item
whose value is

value

.

Compares the specified

obj

parameter with this

CompositeData

instance for equality.

Returns the value of the item whose name is

key

.

Returns an array of the values of the items whose names
are specified by

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

CompositeData

instance.

Returns a string representation of this

CompositeData

instance.

Returns an unmodifiable Collection view of the item values
contained in this

CompositeData

instance.

============ METHOD DETAIL ==========

- Method Detail

- getCompositeType

```java
CompositeType
getCompositeType()
```

Returns the

composite type

of this

composite data

instance.

**Returns:** the type of this CompositeData.

- get

```java
Object
get​(
String
key)
```

Returns the value of the item whose name is

key

.

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

is not an
existing item name for this

CompositeData

instance.

- getAll

```java
Object
[] getAll​(
String
[] keys)
```

Returns an array of the values of the items whose names
are specified by

keys

, in the same order as

keys

.

**Parameters:** keys

- the names of the items.
**Returns:** the values corresponding to the keys.
**Throws:** IllegalArgumentException

- if an element in

keys

is a null or empty String.
**Throws:** InvalidKeyException

- if an element in

keys

is not an existing item name for this

CompositeData

instance.

- containsKey

```java
boolean containsKey​(
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

**Parameters:** key

- the key to be tested.
**Returns:** true if this

CompositeData

contains the key.

- containsValue

```java
boolean containsValue​(
Object
value)
```

Returns

true

if and only if this

CompositeData

instance contains an item
whose value is

value

.

**Parameters:** value

- the value to be tested.
**Returns:** true if this

CompositeData

contains the value.

- values

```java
Collection
<?> values()
```

Returns an unmodifiable Collection view of the item values
contained in this

CompositeData

instance.
The returned collection's iterator will return the values
in the ascending lexicographic order of the corresponding
item names.

**Returns:** the values.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

CompositeData

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

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

CompositeData

instance.
**Returns:** true

if the specified object is equal to this

CompositeData

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this

CompositeData

instance.

The hash code of a

CompositeData

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

CompositeData

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

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

CompositeData

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

CompositeData

instance.

The string representation consists of the name of the implementing class,
the string representation of the composite type of this instance,
and the string representation of the contents
(ie list the itemName=itemValue mappings).

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

CompositeData

instance

Method Detail

- getCompositeType

```java
CompositeType
getCompositeType()
```

Returns the

composite type

of this

composite data

instance.

**Returns:** the type of this CompositeData.

- get

```java
Object
get​(
String
key)
```

Returns the value of the item whose name is

key

.

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

is not an
existing item name for this

CompositeData

instance.

- getAll

```java
Object
[] getAll​(
String
[] keys)
```

Returns an array of the values of the items whose names
are specified by

keys

, in the same order as

keys

.

**Parameters:** keys

- the names of the items.
**Returns:** the values corresponding to the keys.
**Throws:** IllegalArgumentException

- if an element in

keys

is a null or empty String.
**Throws:** InvalidKeyException

- if an element in

keys

is not an existing item name for this

CompositeData

instance.

- containsKey

```java
boolean containsKey​(
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

**Parameters:** key

- the key to be tested.
**Returns:** true if this

CompositeData

contains the key.

- containsValue

```java
boolean containsValue​(
Object
value)
```

Returns

true

if and only if this

CompositeData

instance contains an item
whose value is

value

.

**Parameters:** value

- the value to be tested.
**Returns:** true if this

CompositeData

contains the value.

- values

```java
Collection
<?> values()
```

Returns an unmodifiable Collection view of the item values
contained in this

CompositeData

instance.
The returned collection's iterator will return the values
in the ascending lexicographic order of the corresponding
item names.

**Returns:** the values.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

CompositeData

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

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

CompositeData

instance.
**Returns:** true

if the specified object is equal to this

CompositeData

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this

CompositeData

instance.

The hash code of a

CompositeData

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

CompositeData

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

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

CompositeData

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

CompositeData

instance.

The string representation consists of the name of the implementing class,
the string representation of the composite type of this instance,
and the string representation of the contents
(ie list the itemName=itemValue mappings).

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

CompositeData

instance

---

#### Method Detail

getCompositeType

```java
CompositeType
getCompositeType()
```

Returns the

composite type

of this

composite data

instance.

**Returns:** the type of this CompositeData.

---

#### getCompositeType

CompositeType

getCompositeType()

Returns the

composite type

of this

composite data

instance.

get

```java
Object
get​(
String
key)
```

Returns the value of the item whose name is

key

.

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

is not an
existing item name for this

CompositeData

instance.

---

#### get

Object

get​(

String

key)

Returns the value of the item whose name is

key

.

getAll

```java
Object
[] getAll​(
String
[] keys)
```

Returns an array of the values of the items whose names
are specified by

keys

, in the same order as

keys

.

**Parameters:** keys

- the names of the items.
**Returns:** the values corresponding to the keys.
**Throws:** IllegalArgumentException

- if an element in

keys

is a null or empty String.
**Throws:** InvalidKeyException

- if an element in

keys

is not an existing item name for this

CompositeData

instance.

---

#### getAll

Object

[] getAll​(

String

[] keys)

Returns an array of the values of the items whose names
are specified by

keys

, in the same order as

keys

.

containsKey

```java
boolean containsKey​(
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

**Parameters:** key

- the key to be tested.
**Returns:** true if this

CompositeData

contains the key.

---

#### containsKey

boolean containsKey​(

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
boolean containsValue​(
Object
value)
```

Returns

true

if and only if this

CompositeData

instance contains an item
whose value is

value

.

**Parameters:** value

- the value to be tested.
**Returns:** true if this

CompositeData

contains the value.

---

#### containsValue

boolean containsValue​(

Object

value)

Returns

true

if and only if this

CompositeData

instance contains an item
whose value is

value

.

values

```java
Collection
<?> values()
```

Returns an unmodifiable Collection view of the item values
contained in this

CompositeData

instance.
The returned collection's iterator will return the values
in the ascending lexicographic order of the corresponding
item names.

**Returns:** the values.

---

#### values

Collection

<?> values()

Returns an unmodifiable Collection view of the item values
contained in this

CompositeData

instance.
The returned collection's iterator will return the values
in the ascending lexicographic order of the corresponding
item names.

equals

```java
boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

CompositeData

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

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

CompositeData

instance.
**Returns:** true

if the specified object is equal to this

CompositeData

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

CompositeData

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
int hashCode()
```

Returns the hash code value for this

CompositeData

instance.

The hash code of a

CompositeData

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

CompositeData

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

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

CompositeData

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

int hashCode()

Returns the hash code value for this

CompositeData

instance.

The hash code of a

CompositeData

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

CompositeData

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

CompositeData

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

CompositeData

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

CompositeData

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
String
toString()
```

Returns a string representation of this

CompositeData

instance.

The string representation consists of the name of the implementing class,
the string representation of the composite type of this instance,
and the string representation of the contents
(ie list the itemName=itemValue mappings).

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

CompositeData

instance

---

#### toString

String

toString()

Returns a string representation of this

CompositeData

instance.

The string representation consists of the name of the implementing class,
the string representation of the composite type of this instance,
and the string representation of the contents
(ie list the itemName=itemValue mappings).

The string representation consists of the name of the implementing class,
the string representation of the composite type of this instance,
and the string representation of the contents
(ie list the itemName=itemValue mappings).

---

