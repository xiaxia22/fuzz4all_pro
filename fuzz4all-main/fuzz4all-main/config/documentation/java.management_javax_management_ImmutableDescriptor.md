# Class ImmutableDescriptor

**Source:** `java.management\javax\management\ImmutableDescriptor.html`

### Class Description

```java
public class
ImmutableDescriptor

extends
Object

implements
Descriptor
```

An immutable descriptor.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Descriptor

---

### Field Details

#### public static final
ImmutableDescriptor
EMPTY_DESCRIPTOR

An empty descriptor.

---

### Constructor Details

#### public ImmutableDescriptor​(
String
[] fieldNames,

Object
[] fieldValues)

Construct a descriptor containing the given fields and values.

**Parameters:**
- fieldNames

- the field names
- fieldValues

- the field values

**Throws:**
- IllegalArgumentException

- if either array is null, or
if the arrays have different sizes, or
if a field name is null or empty, or if the same field name
appears more than once.

---

#### public ImmutableDescriptor​(
String
... fields)

Construct a descriptor containing the given fields. Each String
must be of the form

fieldName=fieldValue

. The field name
ends at the first

=

character; for example if the String
is

a=b=c

then the field name is

a

and its value
is

b=c

.

**Parameters:**
- fields

- the field names

**Throws:**
- IllegalArgumentException

- if the parameter is null, or
if a field name is empty, or if the same field name appears
more than once, or if one of the strings does not contain
an

=

character.

---

#### public ImmutableDescriptor​(
Map
<
String
,​?> fields)

Construct a descriptor where the names and values of the fields
are the keys and values of the given Map.

**Parameters:**
- fields

- the field names and values

**Throws:**
- IllegalArgumentException

- if the parameter is null, or
if a field name is null or empty, or if the same field name appears
more than once (which can happen because field names are not case
sensitive).

---

### Method Details

#### public static
ImmutableDescriptor
union​(
Descriptor
... descriptors)

Return an

ImmutableDescriptor

whose contents are the union of
the given descriptors. Every field name that appears in any of
the descriptors will appear in the result with the
value that it has when the method is called. Subsequent changes
to any of the descriptors do not affect the ImmutableDescriptor
returned here.

In the simplest case, there is only one descriptor and the
returned

ImmutableDescriptor

is a copy of its fields at the
time this method is called:

```java
Descriptor d = something();
ImmutableDescriptor copy = ImmutableDescriptor.union(d);
```

**Parameters:**
- descriptors

- the descriptors to be combined. Any of the
descriptors can be null, in which case it is skipped.

**Returns:**
- an

ImmutableDescriptor

that is the union of the given
descriptors. The returned object may be identical to one of the
input descriptors if it is an ImmutableDescriptor that contains all of
the required fields.

**Throws:**
- IllegalArgumentException

- if two Descriptors contain the
same field name with different associated values. Primitive array
values are considered the same if they are of the same type with
the same elements. Object array values are considered the same if

Arrays.deepEquals(Object[],Object[])

returns true.

---

#### public boolean equals​(
Object
o)

Compares this descriptor to the given object. The objects are equal if
the given object is also a Descriptor, and if the two Descriptors have
the same field names (possibly differing in case) and the same
associated values. The respective values for a field in the two
Descriptors are equal if the following conditions hold:

- If one value is null then the other must be too.
- If one value is a primitive array then the other must be a primitive
array of the same type with the same elements.
- If one value is an object array then the other must be too and

Arrays.deepEquals(Object[],Object[])

must return true.
- Otherwise

Object.equals(Object)

must return true.

**Specified by:**
- equals

in interface

Descriptor

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- the object to compare with.

**Returns:**
- true

if the objects are the same;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this descriptor. The hash
code is computed as the sum of the hash codes for each field in
the descriptor. The hash code of a field with name

n

and value

v

is

n.toLowerCase().hashCode() ^ h

.
Here

h

is the hash code of

v

, computed as
follows:

- If

v

is null then

h

is 0.
- If

v

is a primitive array then

h

is computed using
the appropriate overloading of

java.util.Arrays.hashCode

.
- If

v

is an object array then

h

is computed using

Arrays.deepHashCode(Object[])

.
- Otherwise

h

is

v.hashCode()

.

**Specified by:**
- hashCode

in interface

Descriptor

**Overrides:**
- hashCode

in class

Object

**Returns:**
- A hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean isValid()

Returns true if all of the fields have legal values given their
names. This method always returns true, but a subclass can
override it to return false when appropriate.

**Specified by:**
- isValid

in interface

Descriptor

**Returns:**
- true if the values are legal.

**Throws:**
- RuntimeOperationsException

- if the validity checking fails.
The method returns false if the descriptor is not valid, but throws
this exception if the attempt to determine validity fails.

---

#### public
Descriptor
clone()

Returns a descriptor which is equal to this descriptor.
Changes to the returned descriptor will have no effect on this
descriptor, and vice versa.

This method returns the object on which it is called.
A subclass can override it
to return another object provided the contract is respected.

**Specified by:**
- clone

in interface

Descriptor

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**Throws:**
- RuntimeOperationsException

- for illegal value for field Names
or field Values.
If the descriptor construction fails for any reason, this exception will
be thrown.

**See Also:**
- Cloneable

---

#### public final void setFields​(
String
[] fieldNames,

Object
[] fieldValues)
throws
RuntimeOperationsException

This operation is unsupported since this class is immutable. If
this call would change a mutable descriptor with the same contents,
then a

RuntimeOperationsException

wrapping an

UnsupportedOperationException

is thrown. Otherwise,
the behavior is the same as it would be for a mutable descriptor:
either an exception is thrown because of illegal parameters, or
there is no effect.

**Specified by:**
- setFields

in interface

Descriptor

**Parameters:**
- fieldNames

- String array of field names. The array and array
elements cannot be null.
- fieldValues

- Object array of the corresponding field values.
The array cannot be null. Elements of the array can be null.

**Throws:**
- RuntimeOperationsException

- if the change fails for any reason.
Wrapped exception is

IllegalArgumentException

if

fieldNames

or

fieldValues

is null, or if
the arrays are of different lengths, or if there is an
illegal value in one of them.
Wrapped exception is

UnsupportedOperationException

if the descriptor is immutable, and the call would change
its contents.

**See Also:**
- Descriptor.getFields()

---

#### public final void setField​(
String
fieldName,

Object
fieldValue)
throws
RuntimeOperationsException

This operation is unsupported since this class is immutable. If
this call would change a mutable descriptor with the same contents,
then a

RuntimeOperationsException

wrapping an

UnsupportedOperationException

is thrown. Otherwise,
the behavior is the same as it would be for a mutable descriptor:
either an exception is thrown because of illegal parameters, or
there is no effect.

**Specified by:**
- setField

in interface

Descriptor

**Parameters:**
- fieldName

- The field name to be set. Cannot be null or empty.
- fieldValue

- The field value to be set for the field
name. Can be null if that is a valid value for the field.

**Throws:**
- RuntimeOperationsException

- if the field name or field value
is illegal (wrapped exception is

IllegalArgumentException

); or
if the descriptor is immutable (wrapped exception is

UnsupportedOperationException

).

---

#### public final void removeField​(
String
fieldName)

Removes a field from the descriptor.

**Specified by:**
- removeField

in interface

Descriptor

**Parameters:**
- fieldName

- String name of the field to be removed.
If the field name is illegal or the field is not found,
no exception is thrown.

**Throws:**
- RuntimeOperationsException

- if a field of the given name
exists and the descriptor is immutable. The wrapped exception will
be an

UnsupportedOperationException

.

---

### Additional Sections

#### Class ImmutableDescriptor

java.lang.Object

- javax.management.ImmutableDescriptor

javax.management.ImmutableDescriptor

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Descriptor

```java
public class
ImmutableDescriptor

extends
Object

implements
Descriptor
```

An immutable descriptor.

**Since:** 1.6
**See Also:** Serialized Form

public class

ImmutableDescriptor

extends

Object

implements

Descriptor

An immutable descriptor.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

ImmutableDescriptor

EMPTY_DESCRIPTOR

An empty descriptor.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ImmutableDescriptor

​(

String

... fields)

Construct a descriptor containing the given fields.

ImmutableDescriptor

​(

String

[] fieldNames,

Object

[] fieldValues)

Construct a descriptor containing the given fields and values.

ImmutableDescriptor

​(

Map

<

String

,​?> fields)

Construct a descriptor where the names and values of the fields
are the keys and values of the given Map.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Descriptor

clone

()

Returns a descriptor which is equal to this descriptor.

boolean

equals

​(

Object

o)

Compares this descriptor to the given object.

int

hashCode

()

Returns the hash code value for this descriptor.

boolean

isValid

()

Returns true if all of the fields have legal values given their
names.

void

removeField

​(

String

fieldName)

Removes a field from the descriptor.

void

setField

​(

String

fieldName,

Object

fieldValue)

This operation is unsupported since this class is immutable.

void

setFields

​(

String

[] fieldNames,

Object

[] fieldValues)

This operation is unsupported since this class is immutable.

static

ImmutableDescriptor

union

​(

Descriptor

... descriptors)

Return an

ImmutableDescriptor

whose contents are the union of
the given descriptors.

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

toString

,

wait

,

wait

,

wait

- Methods declared in interface javax.management.

Descriptor

getFieldNames

,

getFields

,

getFieldValue

,

getFieldValues

Field Summary

Fields

Modifier and Type

Field

Description

static

ImmutableDescriptor

EMPTY_DESCRIPTOR

An empty descriptor.

---

#### Field Summary

An empty descriptor.

Constructor Summary

Constructors

Constructor

Description

ImmutableDescriptor

​(

String

... fields)

Construct a descriptor containing the given fields.

ImmutableDescriptor

​(

String

[] fieldNames,

Object

[] fieldValues)

Construct a descriptor containing the given fields and values.

ImmutableDescriptor

​(

Map

<

String

,​?> fields)

Construct a descriptor where the names and values of the fields
are the keys and values of the given Map.

---

#### Constructor Summary

Construct a descriptor containing the given fields.

Construct a descriptor containing the given fields and values.

Construct a descriptor where the names and values of the fields
are the keys and values of the given Map.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Descriptor

clone

()

Returns a descriptor which is equal to this descriptor.

boolean

equals

​(

Object

o)

Compares this descriptor to the given object.

int

hashCode

()

Returns the hash code value for this descriptor.

boolean

isValid

()

Returns true if all of the fields have legal values given their
names.

void

removeField

​(

String

fieldName)

Removes a field from the descriptor.

void

setField

​(

String

fieldName,

Object

fieldValue)

This operation is unsupported since this class is immutable.

void

setFields

​(

String

[] fieldNames,

Object

[] fieldValues)

This operation is unsupported since this class is immutable.

static

ImmutableDescriptor

union

​(

Descriptor

... descriptors)

Return an

ImmutableDescriptor

whose contents are the union of
the given descriptors.

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

toString

,

wait

,

wait

,

wait

- Methods declared in interface javax.management.

Descriptor

getFieldNames

,

getFields

,

getFieldValue

,

getFieldValues

---

#### Method Summary

Returns a descriptor which is equal to this descriptor.

Compares this descriptor to the given object.

Returns the hash code value for this descriptor.

Returns true if all of the fields have legal values given their
names.

Removes a field from the descriptor.

This operation is unsupported since this class is immutable.

Return an

ImmutableDescriptor

whose contents are the union of
the given descriptors.

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

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface javax.management.

Descriptor

getFieldNames

,

getFields

,

getFieldValue

,

getFieldValues

---

#### Methods declared in interface javax.management. Descriptor

============ FIELD DETAIL ===========

- Field Detail

- EMPTY_DESCRIPTOR

```java
public static final
ImmutableDescriptor
EMPTY_DESCRIPTOR
```

An empty descriptor.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ImmutableDescriptor

```java
public ImmutableDescriptor​(
String
[] fieldNames,

Object
[] fieldValues)
```

Construct a descriptor containing the given fields and values.

**Parameters:** fieldNames

- the field names
**Parameters:** fieldValues

- the field values
**Throws:** IllegalArgumentException

- if either array is null, or
if the arrays have different sizes, or
if a field name is null or empty, or if the same field name
appears more than once.

- ImmutableDescriptor

```java
public ImmutableDescriptor​(
String
... fields)
```

Construct a descriptor containing the given fields. Each String
must be of the form

fieldName=fieldValue

. The field name
ends at the first

=

character; for example if the String
is

a=b=c

then the field name is

a

and its value
is

b=c

.

**Parameters:** fields

- the field names
**Throws:** IllegalArgumentException

- if the parameter is null, or
if a field name is empty, or if the same field name appears
more than once, or if one of the strings does not contain
an

=

character.

- ImmutableDescriptor

```java
public ImmutableDescriptor​(
Map
<
String
,​?> fields)
```

Construct a descriptor where the names and values of the fields
are the keys and values of the given Map.

**Parameters:** fields

- the field names and values
**Throws:** IllegalArgumentException

- if the parameter is null, or
if a field name is null or empty, or if the same field name appears
more than once (which can happen because field names are not case
sensitive).

============ METHOD DETAIL ==========

- Method Detail

- union

```java
public static
ImmutableDescriptor
union​(
Descriptor
... descriptors)
```

Return an

ImmutableDescriptor

whose contents are the union of
the given descriptors. Every field name that appears in any of
the descriptors will appear in the result with the
value that it has when the method is called. Subsequent changes
to any of the descriptors do not affect the ImmutableDescriptor
returned here.

In the simplest case, there is only one descriptor and the
returned

ImmutableDescriptor

is a copy of its fields at the
time this method is called:

```java
Descriptor d = something();
ImmutableDescriptor copy = ImmutableDescriptor.union(d);
```

**Parameters:** descriptors

- the descriptors to be combined. Any of the
descriptors can be null, in which case it is skipped.
**Returns:** an

ImmutableDescriptor

that is the union of the given
descriptors. The returned object may be identical to one of the
input descriptors if it is an ImmutableDescriptor that contains all of
the required fields.
**Throws:** IllegalArgumentException

- if two Descriptors contain the
same field name with different associated values. Primitive array
values are considered the same if they are of the same type with
the same elements. Object array values are considered the same if

Arrays.deepEquals(Object[],Object[])

returns true.

- equals

```java
public boolean equals​(
Object
o)
```

Compares this descriptor to the given object. The objects are equal if
the given object is also a Descriptor, and if the two Descriptors have
the same field names (possibly differing in case) and the same
associated values. The respective values for a field in the two
Descriptors are equal if the following conditions hold:

- If one value is null then the other must be too.
- If one value is a primitive array then the other must be a primitive
array of the same type with the same elements.
- If one value is an object array then the other must be too and

Arrays.deepEquals(Object[],Object[])

must return true.
- Otherwise

Object.equals(Object)

must return true.

**Specified by:** equals

in interface

Descriptor
**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare with.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this descriptor. The hash
code is computed as the sum of the hash codes for each field in
the descriptor. The hash code of a field with name

n

and value

v

is

n.toLowerCase().hashCode() ^ h

.
Here

h

is the hash code of

v

, computed as
follows:

- If

v

is null then

h

is 0.
- If

v

is a primitive array then

h

is computed using
the appropriate overloading of

java.util.Arrays.hashCode

.
- If

v

is an object array then

h

is computed using

Arrays.deepHashCode(Object[])

.
- Otherwise

h

is

v.hashCode()

.

**Specified by:** hashCode

in interface

Descriptor
**Overrides:** hashCode

in class

Object
**Returns:** A hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- isValid

```java
public boolean isValid()
```

Returns true if all of the fields have legal values given their
names. This method always returns true, but a subclass can
override it to return false when appropriate.

**Specified by:** isValid

in interface

Descriptor
**Returns:** true if the values are legal.
**Throws:** RuntimeOperationsException

- if the validity checking fails.
The method returns false if the descriptor is not valid, but throws
this exception if the attempt to determine validity fails.

- clone

```java
public
Descriptor
clone()
```

Returns a descriptor which is equal to this descriptor.
Changes to the returned descriptor will have no effect on this
descriptor, and vice versa.

This method returns the object on which it is called.
A subclass can override it
to return another object provided the contract is respected.

**Specified by:** clone

in interface

Descriptor
**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** RuntimeOperationsException

- for illegal value for field Names
or field Values.
If the descriptor construction fails for any reason, this exception will
be thrown.
**See Also:** Cloneable

- setFields

```java
public final void setFields​(
String
[] fieldNames,

Object
[] fieldValues)
throws
RuntimeOperationsException
```

This operation is unsupported since this class is immutable. If
this call would change a mutable descriptor with the same contents,
then a

RuntimeOperationsException

wrapping an

UnsupportedOperationException

is thrown. Otherwise,
the behavior is the same as it would be for a mutable descriptor:
either an exception is thrown because of illegal parameters, or
there is no effect.

**Specified by:** setFields

in interface

Descriptor
**Parameters:** fieldNames

- String array of field names. The array and array
elements cannot be null.
**Parameters:** fieldValues

- Object array of the corresponding field values.
The array cannot be null. Elements of the array can be null.
**Throws:** RuntimeOperationsException

- if the change fails for any reason.
Wrapped exception is

IllegalArgumentException

if

fieldNames

or

fieldValues

is null, or if
the arrays are of different lengths, or if there is an
illegal value in one of them.
Wrapped exception is

UnsupportedOperationException

if the descriptor is immutable, and the call would change
its contents.
**See Also:** Descriptor.getFields()

- setField

```java
public final void setField​(
String
fieldName,

Object
fieldValue)
throws
RuntimeOperationsException
```

This operation is unsupported since this class is immutable. If
this call would change a mutable descriptor with the same contents,
then a

RuntimeOperationsException

wrapping an

UnsupportedOperationException

is thrown. Otherwise,
the behavior is the same as it would be for a mutable descriptor:
either an exception is thrown because of illegal parameters, or
there is no effect.

**Specified by:** setField

in interface

Descriptor
**Parameters:** fieldName

- The field name to be set. Cannot be null or empty.
**Parameters:** fieldValue

- The field value to be set for the field
name. Can be null if that is a valid value for the field.
**Throws:** RuntimeOperationsException

- if the field name or field value
is illegal (wrapped exception is

IllegalArgumentException

); or
if the descriptor is immutable (wrapped exception is

UnsupportedOperationException

).

- removeField

```java
public final void removeField​(
String
fieldName)
```

Removes a field from the descriptor.

**Specified by:** removeField

in interface

Descriptor
**Parameters:** fieldName

- String name of the field to be removed.
If the field name is illegal or the field is not found,
no exception is thrown.
**Throws:** RuntimeOperationsException

- if a field of the given name
exists and the descriptor is immutable. The wrapped exception will
be an

UnsupportedOperationException

.

Field Detail

- EMPTY_DESCRIPTOR

```java
public static final
ImmutableDescriptor
EMPTY_DESCRIPTOR
```

An empty descriptor.

---

#### Field Detail

EMPTY_DESCRIPTOR

```java
public static final
ImmutableDescriptor
EMPTY_DESCRIPTOR
```

An empty descriptor.

---

#### EMPTY_DESCRIPTOR

public static final

ImmutableDescriptor

EMPTY_DESCRIPTOR

An empty descriptor.

Constructor Detail

- ImmutableDescriptor

```java
public ImmutableDescriptor​(
String
[] fieldNames,

Object
[] fieldValues)
```

Construct a descriptor containing the given fields and values.

**Parameters:** fieldNames

- the field names
**Parameters:** fieldValues

- the field values
**Throws:** IllegalArgumentException

- if either array is null, or
if the arrays have different sizes, or
if a field name is null or empty, or if the same field name
appears more than once.

- ImmutableDescriptor

```java
public ImmutableDescriptor​(
String
... fields)
```

Construct a descriptor containing the given fields. Each String
must be of the form

fieldName=fieldValue

. The field name
ends at the first

=

character; for example if the String
is

a=b=c

then the field name is

a

and its value
is

b=c

.

**Parameters:** fields

- the field names
**Throws:** IllegalArgumentException

- if the parameter is null, or
if a field name is empty, or if the same field name appears
more than once, or if one of the strings does not contain
an

=

character.

- ImmutableDescriptor

```java
public ImmutableDescriptor​(
Map
<
String
,​?> fields)
```

Construct a descriptor where the names and values of the fields
are the keys and values of the given Map.

**Parameters:** fields

- the field names and values
**Throws:** IllegalArgumentException

- if the parameter is null, or
if a field name is null or empty, or if the same field name appears
more than once (which can happen because field names are not case
sensitive).

---

#### Constructor Detail

ImmutableDescriptor

```java
public ImmutableDescriptor​(
String
[] fieldNames,

Object
[] fieldValues)
```

Construct a descriptor containing the given fields and values.

**Parameters:** fieldNames

- the field names
**Parameters:** fieldValues

- the field values
**Throws:** IllegalArgumentException

- if either array is null, or
if the arrays have different sizes, or
if a field name is null or empty, or if the same field name
appears more than once.

---

#### ImmutableDescriptor

public ImmutableDescriptor​(

String

[] fieldNames,

Object

[] fieldValues)

Construct a descriptor containing the given fields and values.

ImmutableDescriptor

```java
public ImmutableDescriptor​(
String
... fields)
```

Construct a descriptor containing the given fields. Each String
must be of the form

fieldName=fieldValue

. The field name
ends at the first

=

character; for example if the String
is

a=b=c

then the field name is

a

and its value
is

b=c

.

**Parameters:** fields

- the field names
**Throws:** IllegalArgumentException

- if the parameter is null, or
if a field name is empty, or if the same field name appears
more than once, or if one of the strings does not contain
an

=

character.

---

#### ImmutableDescriptor

public ImmutableDescriptor​(

String

... fields)

Construct a descriptor containing the given fields. Each String
must be of the form

fieldName=fieldValue

. The field name
ends at the first

=

character; for example if the String
is

a=b=c

then the field name is

a

and its value
is

b=c

.

ImmutableDescriptor

```java
public ImmutableDescriptor​(
Map
<
String
,​?> fields)
```

Construct a descriptor where the names and values of the fields
are the keys and values of the given Map.

**Parameters:** fields

- the field names and values
**Throws:** IllegalArgumentException

- if the parameter is null, or
if a field name is null or empty, or if the same field name appears
more than once (which can happen because field names are not case
sensitive).

---

#### ImmutableDescriptor

public ImmutableDescriptor​(

Map

<

String

,​?> fields)

Construct a descriptor where the names and values of the fields
are the keys and values of the given Map.

Method Detail

- union

```java
public static
ImmutableDescriptor
union​(
Descriptor
... descriptors)
```

Return an

ImmutableDescriptor

whose contents are the union of
the given descriptors. Every field name that appears in any of
the descriptors will appear in the result with the
value that it has when the method is called. Subsequent changes
to any of the descriptors do not affect the ImmutableDescriptor
returned here.

In the simplest case, there is only one descriptor and the
returned

ImmutableDescriptor

is a copy of its fields at the
time this method is called:

```java
Descriptor d = something();
ImmutableDescriptor copy = ImmutableDescriptor.union(d);
```

**Parameters:** descriptors

- the descriptors to be combined. Any of the
descriptors can be null, in which case it is skipped.
**Returns:** an

ImmutableDescriptor

that is the union of the given
descriptors. The returned object may be identical to one of the
input descriptors if it is an ImmutableDescriptor that contains all of
the required fields.
**Throws:** IllegalArgumentException

- if two Descriptors contain the
same field name with different associated values. Primitive array
values are considered the same if they are of the same type with
the same elements. Object array values are considered the same if

Arrays.deepEquals(Object[],Object[])

returns true.

- equals

```java
public boolean equals​(
Object
o)
```

Compares this descriptor to the given object. The objects are equal if
the given object is also a Descriptor, and if the two Descriptors have
the same field names (possibly differing in case) and the same
associated values. The respective values for a field in the two
Descriptors are equal if the following conditions hold:

- If one value is null then the other must be too.
- If one value is a primitive array then the other must be a primitive
array of the same type with the same elements.
- If one value is an object array then the other must be too and

Arrays.deepEquals(Object[],Object[])

must return true.
- Otherwise

Object.equals(Object)

must return true.

**Specified by:** equals

in interface

Descriptor
**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare with.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this descriptor. The hash
code is computed as the sum of the hash codes for each field in
the descriptor. The hash code of a field with name

n

and value

v

is

n.toLowerCase().hashCode() ^ h

.
Here

h

is the hash code of

v

, computed as
follows:

- If

v

is null then

h

is 0.
- If

v

is a primitive array then

h

is computed using
the appropriate overloading of

java.util.Arrays.hashCode

.
- If

v

is an object array then

h

is computed using

Arrays.deepHashCode(Object[])

.
- Otherwise

h

is

v.hashCode()

.

**Specified by:** hashCode

in interface

Descriptor
**Overrides:** hashCode

in class

Object
**Returns:** A hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- isValid

```java
public boolean isValid()
```

Returns true if all of the fields have legal values given their
names. This method always returns true, but a subclass can
override it to return false when appropriate.

**Specified by:** isValid

in interface

Descriptor
**Returns:** true if the values are legal.
**Throws:** RuntimeOperationsException

- if the validity checking fails.
The method returns false if the descriptor is not valid, but throws
this exception if the attempt to determine validity fails.

- clone

```java
public
Descriptor
clone()
```

Returns a descriptor which is equal to this descriptor.
Changes to the returned descriptor will have no effect on this
descriptor, and vice versa.

This method returns the object on which it is called.
A subclass can override it
to return another object provided the contract is respected.

**Specified by:** clone

in interface

Descriptor
**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** RuntimeOperationsException

- for illegal value for field Names
or field Values.
If the descriptor construction fails for any reason, this exception will
be thrown.
**See Also:** Cloneable

- setFields

```java
public final void setFields​(
String
[] fieldNames,

Object
[] fieldValues)
throws
RuntimeOperationsException
```

This operation is unsupported since this class is immutable. If
this call would change a mutable descriptor with the same contents,
then a

RuntimeOperationsException

wrapping an

UnsupportedOperationException

is thrown. Otherwise,
the behavior is the same as it would be for a mutable descriptor:
either an exception is thrown because of illegal parameters, or
there is no effect.

**Specified by:** setFields

in interface

Descriptor
**Parameters:** fieldNames

- String array of field names. The array and array
elements cannot be null.
**Parameters:** fieldValues

- Object array of the corresponding field values.
The array cannot be null. Elements of the array can be null.
**Throws:** RuntimeOperationsException

- if the change fails for any reason.
Wrapped exception is

IllegalArgumentException

if

fieldNames

or

fieldValues

is null, or if
the arrays are of different lengths, or if there is an
illegal value in one of them.
Wrapped exception is

UnsupportedOperationException

if the descriptor is immutable, and the call would change
its contents.
**See Also:** Descriptor.getFields()

- setField

```java
public final void setField​(
String
fieldName,

Object
fieldValue)
throws
RuntimeOperationsException
```

This operation is unsupported since this class is immutable. If
this call would change a mutable descriptor with the same contents,
then a

RuntimeOperationsException

wrapping an

UnsupportedOperationException

is thrown. Otherwise,
the behavior is the same as it would be for a mutable descriptor:
either an exception is thrown because of illegal parameters, or
there is no effect.

**Specified by:** setField

in interface

Descriptor
**Parameters:** fieldName

- The field name to be set. Cannot be null or empty.
**Parameters:** fieldValue

- The field value to be set for the field
name. Can be null if that is a valid value for the field.
**Throws:** RuntimeOperationsException

- if the field name or field value
is illegal (wrapped exception is

IllegalArgumentException

); or
if the descriptor is immutable (wrapped exception is

UnsupportedOperationException

).

- removeField

```java
public final void removeField​(
String
fieldName)
```

Removes a field from the descriptor.

**Specified by:** removeField

in interface

Descriptor
**Parameters:** fieldName

- String name of the field to be removed.
If the field name is illegal or the field is not found,
no exception is thrown.
**Throws:** RuntimeOperationsException

- if a field of the given name
exists and the descriptor is immutable. The wrapped exception will
be an

UnsupportedOperationException

.

---

#### Method Detail

union

```java
public static
ImmutableDescriptor
union​(
Descriptor
... descriptors)
```

Return an

ImmutableDescriptor

whose contents are the union of
the given descriptors. Every field name that appears in any of
the descriptors will appear in the result with the
value that it has when the method is called. Subsequent changes
to any of the descriptors do not affect the ImmutableDescriptor
returned here.

In the simplest case, there is only one descriptor and the
returned

ImmutableDescriptor

is a copy of its fields at the
time this method is called:

```java
Descriptor d = something();
ImmutableDescriptor copy = ImmutableDescriptor.union(d);
```

**Parameters:** descriptors

- the descriptors to be combined. Any of the
descriptors can be null, in which case it is skipped.
**Returns:** an

ImmutableDescriptor

that is the union of the given
descriptors. The returned object may be identical to one of the
input descriptors if it is an ImmutableDescriptor that contains all of
the required fields.
**Throws:** IllegalArgumentException

- if two Descriptors contain the
same field name with different associated values. Primitive array
values are considered the same if they are of the same type with
the same elements. Object array values are considered the same if

Arrays.deepEquals(Object[],Object[])

returns true.

---

#### union

public static

ImmutableDescriptor

union​(

Descriptor

... descriptors)

Return an

ImmutableDescriptor

whose contents are the union of
the given descriptors. Every field name that appears in any of
the descriptors will appear in the result with the
value that it has when the method is called. Subsequent changes
to any of the descriptors do not affect the ImmutableDescriptor
returned here.

In the simplest case, there is only one descriptor and the
returned

ImmutableDescriptor

is a copy of its fields at the
time this method is called:

```java
Descriptor d = something();
ImmutableDescriptor copy = ImmutableDescriptor.union(d);
```

Return an

ImmutableDescriptor

whose contents are the union of
the given descriptors. Every field name that appears in any of
the descriptors will appear in the result with the
value that it has when the method is called. Subsequent changes
to any of the descriptors do not affect the ImmutableDescriptor
returned here.

In the simplest case, there is only one descriptor and the
returned

ImmutableDescriptor

is a copy of its fields at the
time this method is called:

Descriptor d = something();
ImmutableDescriptor copy = ImmutableDescriptor.union(d);

equals

```java
public boolean equals​(
Object
o)
```

Compares this descriptor to the given object. The objects are equal if
the given object is also a Descriptor, and if the two Descriptors have
the same field names (possibly differing in case) and the same
associated values. The respective values for a field in the two
Descriptors are equal if the following conditions hold:

- If one value is null then the other must be too.
- If one value is a primitive array then the other must be a primitive
array of the same type with the same elements.
- If one value is an object array then the other must be too and

Arrays.deepEquals(Object[],Object[])

must return true.
- Otherwise

Object.equals(Object)

must return true.

**Specified by:** equals

in interface

Descriptor
**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare with.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compares this descriptor to the given object. The objects are equal if
the given object is also a Descriptor, and if the two Descriptors have
the same field names (possibly differing in case) and the same
associated values. The respective values for a field in the two
Descriptors are equal if the following conditions hold:

- If one value is null then the other must be too.
- If one value is a primitive array then the other must be a primitive
array of the same type with the same elements.
- If one value is an object array then the other must be too and

Arrays.deepEquals(Object[],Object[])

must return true.
- Otherwise

Object.equals(Object)

must return true.

If one value is null then the other must be too.

If one value is a primitive array then the other must be a primitive
array of the same type with the same elements.

If one value is an object array then the other must be too and

Arrays.deepEquals(Object[],Object[])

must return true.

Otherwise

Object.equals(Object)

must return true.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this descriptor. The hash
code is computed as the sum of the hash codes for each field in
the descriptor. The hash code of a field with name

n

and value

v

is

n.toLowerCase().hashCode() ^ h

.
Here

h

is the hash code of

v

, computed as
follows:

- If

v

is null then

h

is 0.
- If

v

is a primitive array then

h

is computed using
the appropriate overloading of

java.util.Arrays.hashCode

.
- If

v

is an object array then

h

is computed using

Arrays.deepHashCode(Object[])

.
- Otherwise

h

is

v.hashCode()

.

**Specified by:** hashCode

in interface

Descriptor
**Overrides:** hashCode

in class

Object
**Returns:** A hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this descriptor. The hash
code is computed as the sum of the hash codes for each field in
the descriptor. The hash code of a field with name

n

and value

v

is

n.toLowerCase().hashCode() ^ h

.
Here

h

is the hash code of

v

, computed as
follows:

- If

v

is null then

h

is 0.
- If

v

is a primitive array then

h

is computed using
the appropriate overloading of

java.util.Arrays.hashCode

.
- If

v

is an object array then

h

is computed using

Arrays.deepHashCode(Object[])

.
- Otherwise

h

is

v.hashCode()

.

Returns the hash code value for this descriptor. The hash
code is computed as the sum of the hash codes for each field in
the descriptor. The hash code of a field with name

n

and value

v

is

n.toLowerCase().hashCode() ^ h

.
Here

h

is the hash code of

v

, computed as
follows:

If

v

is null then

h

is 0.

If

v

is a primitive array then

h

is computed using
the appropriate overloading of

java.util.Arrays.hashCode

.

If

v

is an object array then

h

is computed using

Arrays.deepHashCode(Object[])

.

Otherwise

h

is

v.hashCode()

.

isValid

```java
public boolean isValid()
```

Returns true if all of the fields have legal values given their
names. This method always returns true, but a subclass can
override it to return false when appropriate.

**Specified by:** isValid

in interface

Descriptor
**Returns:** true if the values are legal.
**Throws:** RuntimeOperationsException

- if the validity checking fails.
The method returns false if the descriptor is not valid, but throws
this exception if the attempt to determine validity fails.

---

#### isValid

public boolean isValid()

Returns true if all of the fields have legal values given their
names. This method always returns true, but a subclass can
override it to return false when appropriate.

clone

```java
public
Descriptor
clone()
```

Returns a descriptor which is equal to this descriptor.
Changes to the returned descriptor will have no effect on this
descriptor, and vice versa.

This method returns the object on which it is called.
A subclass can override it
to return another object provided the contract is respected.

**Specified by:** clone

in interface

Descriptor
**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** RuntimeOperationsException

- for illegal value for field Names
or field Values.
If the descriptor construction fails for any reason, this exception will
be thrown.
**See Also:** Cloneable

---

#### clone

public

Descriptor

clone()

Returns a descriptor which is equal to this descriptor.
Changes to the returned descriptor will have no effect on this
descriptor, and vice versa.

This method returns the object on which it is called.
A subclass can override it
to return another object provided the contract is respected.

Returns a descriptor which is equal to this descriptor.
Changes to the returned descriptor will have no effect on this
descriptor, and vice versa.

This method returns the object on which it is called.
A subclass can override it
to return another object provided the contract is respected.

setFields

```java
public final void setFields​(
String
[] fieldNames,

Object
[] fieldValues)
throws
RuntimeOperationsException
```

This operation is unsupported since this class is immutable. If
this call would change a mutable descriptor with the same contents,
then a

RuntimeOperationsException

wrapping an

UnsupportedOperationException

is thrown. Otherwise,
the behavior is the same as it would be for a mutable descriptor:
either an exception is thrown because of illegal parameters, or
there is no effect.

**Specified by:** setFields

in interface

Descriptor
**Parameters:** fieldNames

- String array of field names. The array and array
elements cannot be null.
**Parameters:** fieldValues

- Object array of the corresponding field values.
The array cannot be null. Elements of the array can be null.
**Throws:** RuntimeOperationsException

- if the change fails for any reason.
Wrapped exception is

IllegalArgumentException

if

fieldNames

or

fieldValues

is null, or if
the arrays are of different lengths, or if there is an
illegal value in one of them.
Wrapped exception is

UnsupportedOperationException

if the descriptor is immutable, and the call would change
its contents.
**See Also:** Descriptor.getFields()

---

#### setFields

public final void setFields​(

String

[] fieldNames,

Object

[] fieldValues)
throws

RuntimeOperationsException

This operation is unsupported since this class is immutable. If
this call would change a mutable descriptor with the same contents,
then a

RuntimeOperationsException

wrapping an

UnsupportedOperationException

is thrown. Otherwise,
the behavior is the same as it would be for a mutable descriptor:
either an exception is thrown because of illegal parameters, or
there is no effect.

setField

```java
public final void setField​(
String
fieldName,

Object
fieldValue)
throws
RuntimeOperationsException
```

This operation is unsupported since this class is immutable. If
this call would change a mutable descriptor with the same contents,
then a

RuntimeOperationsException

wrapping an

UnsupportedOperationException

is thrown. Otherwise,
the behavior is the same as it would be for a mutable descriptor:
either an exception is thrown because of illegal parameters, or
there is no effect.

**Specified by:** setField

in interface

Descriptor
**Parameters:** fieldName

- The field name to be set. Cannot be null or empty.
**Parameters:** fieldValue

- The field value to be set for the field
name. Can be null if that is a valid value for the field.
**Throws:** RuntimeOperationsException

- if the field name or field value
is illegal (wrapped exception is

IllegalArgumentException

); or
if the descriptor is immutable (wrapped exception is

UnsupportedOperationException

).

---

#### setField

public final void setField​(

String

fieldName,

Object

fieldValue)
throws

RuntimeOperationsException

This operation is unsupported since this class is immutable. If
this call would change a mutable descriptor with the same contents,
then a

RuntimeOperationsException

wrapping an

UnsupportedOperationException

is thrown. Otherwise,
the behavior is the same as it would be for a mutable descriptor:
either an exception is thrown because of illegal parameters, or
there is no effect.

removeField

```java
public final void removeField​(
String
fieldName)
```

Removes a field from the descriptor.

**Specified by:** removeField

in interface

Descriptor
**Parameters:** fieldName

- String name of the field to be removed.
If the field name is illegal or the field is not found,
no exception is thrown.
**Throws:** RuntimeOperationsException

- if a field of the given name
exists and the descriptor is immutable. The wrapped exception will
be an

UnsupportedOperationException

.

---

#### removeField

public final void removeField​(

String

fieldName)

Removes a field from the descriptor.

---

