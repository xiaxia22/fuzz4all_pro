# Class OpenMBeanOperationInfoSupport

**Source:** `java.management\javax\management\openmbean\OpenMBeanOperationInfoSupport.html`

### Class Description

```java
public class
OpenMBeanOperationInfoSupport

extends
MBeanOperationInfo

implements
OpenMBeanOperationInfo
```

Describes an operation of an Open MBean.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

,

OpenMBeanOperationInfo

---

### Field Details

*No entries found.*

### Constructor Details

#### public OpenMBeanOperationInfoSupport​(
String
name,

String
description,

OpenMBeanParameterInfo
[] signature,

OpenType
<?> returnOpenType,
int impact)

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

and

impact

.

The

signature

array parameter is internally copied,
so that subsequent changes to the array referenced by

signature

have no effect on this instance.

**Parameters:**
- name

- cannot be a null or empty string.
- description

- cannot be a null or empty string.
- signature

- can be null or empty if there are no
parameters to describe.
- returnOpenType

- cannot be null: use

SimpleType.VOID

for operations that return nothing.
- impact

- must be one of

ACTION

,

ACTION_INFO

,

INFO

, or

UNKNOWN

.

**Throws:**
- IllegalArgumentException

- if

name

or

description

are null or empty string, or

returnOpenType

is null, or

impact

is not one of

ACTION

,

ACTION_INFO

,

INFO

, or

UNKNOWN

.
- ArrayStoreException

- If

signature

is not an
array of instances of a subclass of

MBeanParameterInfo

.

---

#### public OpenMBeanOperationInfoSupport​(
String
name,

String
description,

OpenMBeanParameterInfo
[] signature,

OpenType
<?> returnOpenType,
int impact,

Descriptor
descriptor)

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

,

impact

, and

descriptor

.

The

signature

array parameter is internally copied,
so that subsequent changes to the array referenced by

signature

have no effect on this instance.

**Parameters:**
- name

- cannot be a null or empty string.
- description

- cannot be a null or empty string.
- signature

- can be null or empty if there are no
parameters to describe.
- returnOpenType

- cannot be null: use

SimpleType.VOID

for operations that return nothing.
- impact

- must be one of

ACTION

,

ACTION_INFO

,

INFO

, or

UNKNOWN

.
- descriptor

- The descriptor for the operation. This may
be null, which is equivalent to an empty descriptor.

**Throws:**
- IllegalArgumentException

- if

name

or

description

are null or empty string, or

returnOpenType

is null, or

impact

is not one of

ACTION

,

ACTION_INFO

,

INFO

, or

UNKNOWN

.
- ArrayStoreException

- If

signature

is not an
array of instances of a subclass of

MBeanParameterInfo

.

**Since:**
- 1.6

---

### Method Details

#### public
OpenType
<?> getReturnOpenType()

Returns the

open type

of the values returned by the
operation described by this

OpenMBeanOperationInfo

instance.

**Specified by:**
- getReturnOpenType

in interface

OpenMBeanOperationInfo

**Returns:**
- the return type.

---

#### public boolean equals​(
Object
obj)

Compares the specified

obj

parameter with this

OpenMBeanOperationInfoSupport

instance for
equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanOperationInfo

interface,
- their names are equal
- their signatures are equal
- their return open types are equal
- their impacts are equal

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanOperationInfo

interface.

**Specified by:**
- equals

in interface

OpenMBeanOperationInfo

**Overrides:**
- equals

in class

MBeanOperationInfo

**Parameters:**
- obj

- the object to be compared for equality with this

OpenMBeanOperationInfoSupport

instance;

**Returns:**
- true

if the specified object is equal to this

OpenMBeanOperationInfoSupport

instance.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this

OpenMBeanOperationInfoSupport

instance.

The hash code of an

OpenMBeanOperationInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name,
return open type, impact and signature, where the signature
hashCode is calculated by a call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanOperationInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanOperationInfo

interface may be equal to
this

OpenMBeanOperationInfoSupport

instance as defined
by

equals(java.lang.Object)

, but may have a different
hash code if it is calculated differently.

As

OpenMBeanOperationInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

**Specified by:**
- hashCode

in interface

OpenMBeanOperationInfo

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this

OpenMBeanOperationInfoSupport

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

OpenMBeanOperationInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanOperationInfoSupport

), and
the name, signature, return open type and impact of the
described operation and the string representation of its descriptor.

As

OpenMBeanOperationInfoSupport

instances are
immutable, the string representation for this instance is
calculated once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

**Specified by:**
- toString

in interface

OpenMBeanOperationInfo

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

OpenMBeanOperationInfoSupport

instance

---

### Additional Sections

#### Class OpenMBeanOperationInfoSupport

java.lang.Object

- javax.management.MBeanFeatureInfo
- - javax.management.MBeanOperationInfo
- - javax.management.openmbean.OpenMBeanOperationInfoSupport

javax.management.MBeanFeatureInfo

- javax.management.MBeanOperationInfo
- - javax.management.openmbean.OpenMBeanOperationInfoSupport

javax.management.MBeanOperationInfo

- javax.management.openmbean.OpenMBeanOperationInfoSupport

javax.management.openmbean.OpenMBeanOperationInfoSupport

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

,

OpenMBeanOperationInfo

```java
public class
OpenMBeanOperationInfoSupport

extends
MBeanOperationInfo

implements
OpenMBeanOperationInfo
```

Describes an operation of an Open MBean.

**Since:** 1.5
**See Also:** Serialized Form

public class

OpenMBeanOperationInfoSupport

extends

MBeanOperationInfo

implements

OpenMBeanOperationInfo

Describes an operation of an Open MBean.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.management.

MBeanOperationInfo

ACTION

,

ACTION_INFO

,

INFO

,

UNKNOWN

- Fields declared in class javax.management.

MBeanFeatureInfo

description

,

name

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

OpenMBeanOperationInfoSupport

​(

String

name,

String

description,

OpenMBeanParameterInfo

[] signature,

OpenType

<?> returnOpenType,
int impact)

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

and

impact

.

OpenMBeanOperationInfoSupport

​(

String

name,

String

description,

OpenMBeanParameterInfo

[] signature,

OpenType

<?> returnOpenType,
int impact,

Descriptor

descriptor)

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

,

impact

, and

descriptor

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

equals

​(

Object

obj)

Compares the specified

obj

parameter with this

OpenMBeanOperationInfoSupport

instance for
equality.

OpenType

<?>

getReturnOpenType

()

Returns the

open type

of the values returned by the
operation described by this

OpenMBeanOperationInfo

instance.

int

hashCode

()

Returns the hash code value for this

OpenMBeanOperationInfoSupport

instance.

String

toString

()

Returns a string representation of this

OpenMBeanOperationInfoSupport

instance.

- Methods declared in class javax.management.

MBeanOperationInfo

clone

,

getImpact

,

getReturnType

,

getSignature

- Methods declared in class javax.management.

MBeanFeatureInfo

getDescription

,

getDescriptor

,

getName

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

- Methods declared in interface javax.management.openmbean.

OpenMBeanOperationInfo

getDescription

,

getImpact

,

getName

,

getReturnType

,

getSignature

Field Summary

- Fields declared in class javax.management.

MBeanOperationInfo

ACTION

,

ACTION_INFO

,

INFO

,

UNKNOWN

- Fields declared in class javax.management.

MBeanFeatureInfo

description

,

name

---

#### Field Summary

Fields declared in class javax.management.

MBeanOperationInfo

ACTION

,

ACTION_INFO

,

INFO

,

UNKNOWN

---

#### Fields declared in class javax.management. MBeanOperationInfo

Fields declared in class javax.management.

MBeanFeatureInfo

description

,

name

---

#### Fields declared in class javax.management. MBeanFeatureInfo

Constructor Summary

Constructors

Constructor

Description

OpenMBeanOperationInfoSupport

​(

String

name,

String

description,

OpenMBeanParameterInfo

[] signature,

OpenType

<?> returnOpenType,
int impact)

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

and

impact

.

OpenMBeanOperationInfoSupport

​(

String

name,

String

description,

OpenMBeanParameterInfo

[] signature,

OpenType

<?> returnOpenType,
int impact,

Descriptor

descriptor)

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

,

impact

, and

descriptor

.

---

#### Constructor Summary

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

and

impact

.

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

,

impact

, and

descriptor

.

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

OpenMBeanOperationInfoSupport

instance for
equality.

OpenType

<?>

getReturnOpenType

()

Returns the

open type

of the values returned by the
operation described by this

OpenMBeanOperationInfo

instance.

int

hashCode

()

Returns the hash code value for this

OpenMBeanOperationInfoSupport

instance.

String

toString

()

Returns a string representation of this

OpenMBeanOperationInfoSupport

instance.

- Methods declared in class javax.management.

MBeanOperationInfo

clone

,

getImpact

,

getReturnType

,

getSignature

- Methods declared in class javax.management.

MBeanFeatureInfo

getDescription

,

getDescriptor

,

getName

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

- Methods declared in interface javax.management.openmbean.

OpenMBeanOperationInfo

getDescription

,

getImpact

,

getName

,

getReturnType

,

getSignature

---

#### Method Summary

Compares the specified

obj

parameter with this

OpenMBeanOperationInfoSupport

instance for
equality.

Returns the

open type

of the values returned by the
operation described by this

OpenMBeanOperationInfo

instance.

Returns the hash code value for this

OpenMBeanOperationInfoSupport

instance.

Returns a string representation of this

OpenMBeanOperationInfoSupport

instance.

Methods declared in class javax.management.

MBeanOperationInfo

clone

,

getImpact

,

getReturnType

,

getSignature

---

#### Methods declared in class javax.management. MBeanOperationInfo

Methods declared in class javax.management.

MBeanFeatureInfo

getDescription

,

getDescriptor

,

getName

---

#### Methods declared in class javax.management. MBeanFeatureInfo

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

Methods declared in interface javax.management.openmbean.

OpenMBeanOperationInfo

getDescription

,

getImpact

,

getName

,

getReturnType

,

getSignature

---

#### Methods declared in interface javax.management.openmbean. OpenMBeanOperationInfo

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- OpenMBeanOperationInfoSupport

```java
public OpenMBeanOperationInfoSupport​(
String
name,

String
description,

OpenMBeanParameterInfo
[] signature,

OpenType
<?> returnOpenType,
int impact)
```

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

and

impact

.

The

signature

array parameter is internally copied,
so that subsequent changes to the array referenced by

signature

have no effect on this instance.

**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** signature

- can be null or empty if there are no
parameters to describe.
**Parameters:** returnOpenType

- cannot be null: use

SimpleType.VOID

for operations that return nothing.
**Parameters:** impact

- must be one of

ACTION

,

ACTION_INFO

,

INFO

, or

UNKNOWN

.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

returnOpenType

is null, or

impact

is not one of

ACTION

,

ACTION_INFO

,

INFO

, or

UNKNOWN

.
**Throws:** ArrayStoreException

- If

signature

is not an
array of instances of a subclass of

MBeanParameterInfo

.

- OpenMBeanOperationInfoSupport

```java
public OpenMBeanOperationInfoSupport​(
String
name,

String
description,

OpenMBeanParameterInfo
[] signature,

OpenType
<?> returnOpenType,
int impact,

Descriptor
descriptor)
```

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

,

impact

, and

descriptor

.

The

signature

array parameter is internally copied,
so that subsequent changes to the array referenced by

signature

have no effect on this instance.

**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** signature

- can be null or empty if there are no
parameters to describe.
**Parameters:** returnOpenType

- cannot be null: use

SimpleType.VOID

for operations that return nothing.
**Parameters:** impact

- must be one of

ACTION

,

ACTION_INFO

,

INFO

, or

UNKNOWN

.
**Parameters:** descriptor

- The descriptor for the operation. This may
be null, which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

returnOpenType

is null, or

impact

is not one of

ACTION

,

ACTION_INFO

,

INFO

, or

UNKNOWN

.
**Throws:** ArrayStoreException

- If

signature

is not an
array of instances of a subclass of

MBeanParameterInfo

.
**Since:** 1.6

============ METHOD DETAIL ==========

- Method Detail

- getReturnOpenType

```java
public
OpenType
<?> getReturnOpenType()
```

Returns the

open type

of the values returned by the
operation described by this

OpenMBeanOperationInfo

instance.

**Specified by:** getReturnOpenType

in interface

OpenMBeanOperationInfo
**Returns:** the return type.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanOperationInfoSupport

instance for
equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanOperationInfo

interface,
- their names are equal
- their signatures are equal
- their return open types are equal
- their impacts are equal

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanOperationInfo

interface.

**Specified by:** equals

in interface

OpenMBeanOperationInfo
**Overrides:** equals

in class

MBeanOperationInfo
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanOperationInfoSupport

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanOperationInfoSupport

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

OpenMBeanOperationInfoSupport

instance.

The hash code of an

OpenMBeanOperationInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name,
return open type, impact and signature, where the signature
hashCode is calculated by a call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanOperationInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanOperationInfo

interface may be equal to
this

OpenMBeanOperationInfoSupport

instance as defined
by

equals(java.lang.Object)

, but may have a different
hash code if it is calculated differently.

As

OpenMBeanOperationInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

**Specified by:** hashCode

in interface

OpenMBeanOperationInfo
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanOperationInfoSupport

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

OpenMBeanOperationInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanOperationInfoSupport

), and
the name, signature, return open type and impact of the
described operation and the string representation of its descriptor.

As

OpenMBeanOperationInfoSupport

instances are
immutable, the string representation for this instance is
calculated once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

**Specified by:** toString

in interface

OpenMBeanOperationInfo
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanOperationInfoSupport

instance

Constructor Detail

- OpenMBeanOperationInfoSupport

```java
public OpenMBeanOperationInfoSupport​(
String
name,

String
description,

OpenMBeanParameterInfo
[] signature,

OpenType
<?> returnOpenType,
int impact)
```

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

and

impact

.

The

signature

array parameter is internally copied,
so that subsequent changes to the array referenced by

signature

have no effect on this instance.

**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** signature

- can be null or empty if there are no
parameters to describe.
**Parameters:** returnOpenType

- cannot be null: use

SimpleType.VOID

for operations that return nothing.
**Parameters:** impact

- must be one of

ACTION

,

ACTION_INFO

,

INFO

, or

UNKNOWN

.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

returnOpenType

is null, or

impact

is not one of

ACTION

,

ACTION_INFO

,

INFO

, or

UNKNOWN

.
**Throws:** ArrayStoreException

- If

signature

is not an
array of instances of a subclass of

MBeanParameterInfo

.

- OpenMBeanOperationInfoSupport

```java
public OpenMBeanOperationInfoSupport​(
String
name,

String
description,

OpenMBeanParameterInfo
[] signature,

OpenType
<?> returnOpenType,
int impact,

Descriptor
descriptor)
```

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

,

impact

, and

descriptor

.

The

signature

array parameter is internally copied,
so that subsequent changes to the array referenced by

signature

have no effect on this instance.

**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** signature

- can be null or empty if there are no
parameters to describe.
**Parameters:** returnOpenType

- cannot be null: use

SimpleType.VOID

for operations that return nothing.
**Parameters:** impact

- must be one of

ACTION

,

ACTION_INFO

,

INFO

, or

UNKNOWN

.
**Parameters:** descriptor

- The descriptor for the operation. This may
be null, which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

returnOpenType

is null, or

impact

is not one of

ACTION

,

ACTION_INFO

,

INFO

, or

UNKNOWN

.
**Throws:** ArrayStoreException

- If

signature

is not an
array of instances of a subclass of

MBeanParameterInfo

.
**Since:** 1.6

---

#### Constructor Detail

OpenMBeanOperationInfoSupport

```java
public OpenMBeanOperationInfoSupport​(
String
name,

String
description,

OpenMBeanParameterInfo
[] signature,

OpenType
<?> returnOpenType,
int impact)
```

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

and

impact

.

The

signature

array parameter is internally copied,
so that subsequent changes to the array referenced by

signature

have no effect on this instance.

**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** signature

- can be null or empty if there are no
parameters to describe.
**Parameters:** returnOpenType

- cannot be null: use

SimpleType.VOID

for operations that return nothing.
**Parameters:** impact

- must be one of

ACTION

,

ACTION_INFO

,

INFO

, or

UNKNOWN

.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

returnOpenType

is null, or

impact

is not one of

ACTION

,

ACTION_INFO

,

INFO

, or

UNKNOWN

.
**Throws:** ArrayStoreException

- If

signature

is not an
array of instances of a subclass of

MBeanParameterInfo

.

---

#### OpenMBeanOperationInfoSupport

public OpenMBeanOperationInfoSupport​(

String

name,

String

description,

OpenMBeanParameterInfo

[] signature,

OpenType

<?> returnOpenType,
int impact)

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

and

impact

.

The

signature

array parameter is internally copied,
so that subsequent changes to the array referenced by

signature

have no effect on this instance.

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

and

impact

.

The

signature

array parameter is internally copied,
so that subsequent changes to the array referenced by

signature

have no effect on this instance.

OpenMBeanOperationInfoSupport

```java
public OpenMBeanOperationInfoSupport​(
String
name,

String
description,

OpenMBeanParameterInfo
[] signature,

OpenType
<?> returnOpenType,
int impact,

Descriptor
descriptor)
```

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

,

impact

, and

descriptor

.

The

signature

array parameter is internally copied,
so that subsequent changes to the array referenced by

signature

have no effect on this instance.

**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** signature

- can be null or empty if there are no
parameters to describe.
**Parameters:** returnOpenType

- cannot be null: use

SimpleType.VOID

for operations that return nothing.
**Parameters:** impact

- must be one of

ACTION

,

ACTION_INFO

,

INFO

, or

UNKNOWN

.
**Parameters:** descriptor

- The descriptor for the operation. This may
be null, which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

returnOpenType

is null, or

impact

is not one of

ACTION

,

ACTION_INFO

,

INFO

, or

UNKNOWN

.
**Throws:** ArrayStoreException

- If

signature

is not an
array of instances of a subclass of

MBeanParameterInfo

.
**Since:** 1.6

---

#### OpenMBeanOperationInfoSupport

public OpenMBeanOperationInfoSupport​(

String

name,

String

description,

OpenMBeanParameterInfo

[] signature,

OpenType

<?> returnOpenType,
int impact,

Descriptor

descriptor)

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

,

impact

, and

descriptor

.

The

signature

array parameter is internally copied,
so that subsequent changes to the array referenced by

signature

have no effect on this instance.

Constructs an

OpenMBeanOperationInfoSupport

instance, which describes the operation of a class of open
MBeans, with the specified

name

,

description

,

signature

,

returnOpenType

,

impact

, and

descriptor

.

The

signature

array parameter is internally copied,
so that subsequent changes to the array referenced by

signature

have no effect on this instance.

Method Detail

- getReturnOpenType

```java
public
OpenType
<?> getReturnOpenType()
```

Returns the

open type

of the values returned by the
operation described by this

OpenMBeanOperationInfo

instance.

**Specified by:** getReturnOpenType

in interface

OpenMBeanOperationInfo
**Returns:** the return type.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanOperationInfoSupport

instance for
equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanOperationInfo

interface,
- their names are equal
- their signatures are equal
- their return open types are equal
- their impacts are equal

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanOperationInfo

interface.

**Specified by:** equals

in interface

OpenMBeanOperationInfo
**Overrides:** equals

in class

MBeanOperationInfo
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanOperationInfoSupport

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanOperationInfoSupport

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

OpenMBeanOperationInfoSupport

instance.

The hash code of an

OpenMBeanOperationInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name,
return open type, impact and signature, where the signature
hashCode is calculated by a call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanOperationInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanOperationInfo

interface may be equal to
this

OpenMBeanOperationInfoSupport

instance as defined
by

equals(java.lang.Object)

, but may have a different
hash code if it is calculated differently.

As

OpenMBeanOperationInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

**Specified by:** hashCode

in interface

OpenMBeanOperationInfo
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanOperationInfoSupport

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

OpenMBeanOperationInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanOperationInfoSupport

), and
the name, signature, return open type and impact of the
described operation and the string representation of its descriptor.

As

OpenMBeanOperationInfoSupport

instances are
immutable, the string representation for this instance is
calculated once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

**Specified by:** toString

in interface

OpenMBeanOperationInfo
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanOperationInfoSupport

instance

---

#### Method Detail

getReturnOpenType

```java
public
OpenType
<?> getReturnOpenType()
```

Returns the

open type

of the values returned by the
operation described by this

OpenMBeanOperationInfo

instance.

**Specified by:** getReturnOpenType

in interface

OpenMBeanOperationInfo
**Returns:** the return type.

---

#### getReturnOpenType

public

OpenType

<?> getReturnOpenType()

Returns the

open type

of the values returned by the
operation described by this

OpenMBeanOperationInfo

instance.

equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanOperationInfoSupport

instance for
equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanOperationInfo

interface,
- their names are equal
- their signatures are equal
- their return open types are equal
- their impacts are equal

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanOperationInfo

interface.

**Specified by:** equals

in interface

OpenMBeanOperationInfo
**Overrides:** equals

in class

MBeanOperationInfo
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanOperationInfoSupport

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanOperationInfoSupport

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

OpenMBeanOperationInfoSupport

instance for
equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanOperationInfo

interface,
- their names are equal
- their signatures are equal
- their return open types are equal
- their impacts are equal

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanOperationInfo

interface.

Compares the specified

obj

parameter with this

OpenMBeanOperationInfoSupport

instance for
equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanOperationInfo

interface,
- their names are equal
- their signatures are equal
- their return open types are equal
- their impacts are equal

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanOperationInfo

interface.

obj

is non null,

obj

also implements the

OpenMBeanOperationInfo

interface,

their names are equal

their signatures are equal

their return open types are equal

their impacts are equal

hashCode

```java
public int hashCode()
```

Returns the hash code value for this

OpenMBeanOperationInfoSupport

instance.

The hash code of an

OpenMBeanOperationInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name,
return open type, impact and signature, where the signature
hashCode is calculated by a call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanOperationInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanOperationInfo

interface may be equal to
this

OpenMBeanOperationInfoSupport

instance as defined
by

equals(java.lang.Object)

, but may have a different
hash code if it is calculated differently.

As

OpenMBeanOperationInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

**Specified by:** hashCode

in interface

OpenMBeanOperationInfo
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanOperationInfoSupport

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this

OpenMBeanOperationInfoSupport

instance.

The hash code of an

OpenMBeanOperationInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name,
return open type, impact and signature, where the signature
hashCode is calculated by a call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanOperationInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanOperationInfo

interface may be equal to
this

OpenMBeanOperationInfoSupport

instance as defined
by

equals(java.lang.Object)

, but may have a different
hash code if it is calculated differently.

As

OpenMBeanOperationInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

Returns the hash code value for this

OpenMBeanOperationInfoSupport

instance.

The hash code of an

OpenMBeanOperationInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name,
return open type, impact and signature, where the signature
hashCode is calculated by a call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanOperationInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanOperationInfo

interface may be equal to
this

OpenMBeanOperationInfoSupport

instance as defined
by

equals(java.lang.Object)

, but may have a different
hash code if it is calculated differently.

As

OpenMBeanOperationInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

toString

```java
public
String
toString()
```

Returns a string representation of this

OpenMBeanOperationInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanOperationInfoSupport

), and
the name, signature, return open type and impact of the
described operation and the string representation of its descriptor.

As

OpenMBeanOperationInfoSupport

instances are
immutable, the string representation for this instance is
calculated once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

**Specified by:** toString

in interface

OpenMBeanOperationInfo
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanOperationInfoSupport

instance

---

#### toString

public

String

toString()

Returns a string representation of this

OpenMBeanOperationInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanOperationInfoSupport

), and
the name, signature, return open type and impact of the
described operation and the string representation of its descriptor.

As

OpenMBeanOperationInfoSupport

instances are
immutable, the string representation for this instance is
calculated once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

Returns a string representation of this

OpenMBeanOperationInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanOperationInfoSupport

), and
the name, signature, return open type and impact of the
described operation and the string representation of its descriptor.

As

OpenMBeanOperationInfoSupport

instances are
immutable, the string representation for this instance is
calculated once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

---

