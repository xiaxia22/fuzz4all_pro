# Class OpenMBeanConstructorInfoSupport

**Source:** `java.management\javax\management\openmbean\OpenMBeanConstructorInfoSupport.html`

### Class Description

```java
public class
OpenMBeanConstructorInfoSupport

extends
MBeanConstructorInfo

implements
OpenMBeanConstructorInfo
```

Describes a constructor of an Open MBean.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

,

OpenMBeanConstructorInfo

---

### Field Details

*No entries found.*

### Constructor Details

#### public OpenMBeanConstructorInfoSupport​(
String
name,

String
description,

OpenMBeanParameterInfo
[] signature)

Constructs an

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

and

signature

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

**Throws:**
- IllegalArgumentException

- if

name

or

description

are null or empty string.
- ArrayStoreException

- If

signature

is not an
array of instances of a subclass of

MBeanParameterInfo

.

---

#### public OpenMBeanConstructorInfoSupport​(
String
name,

String
description,

OpenMBeanParameterInfo
[] signature,

Descriptor
descriptor)

Constructs an

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

,

signature

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
- descriptor

- The descriptor for the constructor. This may
be null which is equivalent to an empty descriptor.

**Throws:**
- IllegalArgumentException

- if

name

or

description

are null or empty string.
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

#### public boolean equals​(
Object
obj)

Compares the specified

obj

parameter with this

OpenMBeanConstructorInfoSupport

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

OpenMBeanConstructorInfo

interface,
- their names are equal
- their signatures are equal.

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanConstructorInfo

interface.

**Specified by:**
- equals

in interface

OpenMBeanConstructorInfo

**Overrides:**
- equals

in class

MBeanConstructorInfo

**Parameters:**
- obj

- the object to be compared for equality with this

OpenMBeanConstructorInfoSupport

instance;

**Returns:**
- true

if the specified object is equal to this

OpenMBeanConstructorInfoSupport

instance.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this

OpenMBeanConstructorInfoSupport

instance.

The hash code of an

OpenMBeanConstructorInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name
and signature, where the signature hashCode is calculated by a
call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanConstructorInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanConstructorInfo

interface may be equal to
this

OpenMBeanConstructorInfoSupport

instance as
defined by

equals(java.lang.Object)

, but may have a
different hash code if it is calculated differently.

As

OpenMBeanConstructorInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

**Specified by:**
- hashCode

in interface

OpenMBeanConstructorInfo

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this

OpenMBeanConstructorInfoSupport

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

OpenMBeanConstructorInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanConstructorInfoSupport

),
the name and signature of the described constructor and the
string representation of its descriptor.

As

OpenMBeanConstructorInfoSupport

instances are
immutable, the string representation for this instance is
calculated once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

**Specified by:**
- toString

in interface

OpenMBeanConstructorInfo

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

OpenMBeanConstructorInfoSupport

instance

---

### Additional Sections

#### Class OpenMBeanConstructorInfoSupport

java.lang.Object

- javax.management.MBeanFeatureInfo
- - javax.management.MBeanConstructorInfo
- - javax.management.openmbean.OpenMBeanConstructorInfoSupport

javax.management.MBeanFeatureInfo

- javax.management.MBeanConstructorInfo
- - javax.management.openmbean.OpenMBeanConstructorInfoSupport

javax.management.MBeanConstructorInfo

- javax.management.openmbean.OpenMBeanConstructorInfoSupport

javax.management.openmbean.OpenMBeanConstructorInfoSupport

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

,

OpenMBeanConstructorInfo

```java
public class
OpenMBeanConstructorInfoSupport

extends
MBeanConstructorInfo

implements
OpenMBeanConstructorInfo
```

Describes a constructor of an Open MBean.

**Since:** 1.5
**See Also:** Serialized Form

public class

OpenMBeanConstructorInfoSupport

extends

MBeanConstructorInfo

implements

OpenMBeanConstructorInfo

Describes a constructor of an Open MBean.

=========== FIELD SUMMARY ===========

- Field Summary

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

OpenMBeanConstructorInfoSupport

​(

String

name,

String

description,

OpenMBeanParameterInfo

[] signature)

Constructs an

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

and

signature

.

OpenMBeanConstructorInfoSupport

​(

String

name,

String

description,

OpenMBeanParameterInfo

[] signature,

Descriptor

descriptor)

Constructs an

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

,

signature

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

OpenMBeanConstructorInfoSupport

instance for
equality.

int

hashCode

()

Returns the hash code value for this

OpenMBeanConstructorInfoSupport

instance.

String

toString

()

Returns a string representation of this

OpenMBeanConstructorInfoSupport

instance.

- Methods declared in class javax.management.

MBeanConstructorInfo

clone

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

OpenMBeanConstructorInfo

getDescription

,

getName

,

getSignature

Field Summary

- Fields declared in class javax.management.

MBeanFeatureInfo

description

,

name

---

#### Field Summary

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

OpenMBeanConstructorInfoSupport

​(

String

name,

String

description,

OpenMBeanParameterInfo

[] signature)

Constructs an

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

and

signature

.

OpenMBeanConstructorInfoSupport

​(

String

name,

String

description,

OpenMBeanParameterInfo

[] signature,

Descriptor

descriptor)

Constructs an

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

,

signature

, and

descriptor

.

---

#### Constructor Summary

Constructs an

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

and

signature

.

Constructs an

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

,

signature

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

OpenMBeanConstructorInfoSupport

instance for
equality.

int

hashCode

()

Returns the hash code value for this

OpenMBeanConstructorInfoSupport

instance.

String

toString

()

Returns a string representation of this

OpenMBeanConstructorInfoSupport

instance.

- Methods declared in class javax.management.

MBeanConstructorInfo

clone

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

OpenMBeanConstructorInfo

getDescription

,

getName

,

getSignature

---

#### Method Summary

Compares the specified

obj

parameter with this

OpenMBeanConstructorInfoSupport

instance for
equality.

Returns the hash code value for this

OpenMBeanConstructorInfoSupport

instance.

Returns a string representation of this

OpenMBeanConstructorInfoSupport

instance.

Methods declared in class javax.management.

MBeanConstructorInfo

clone

,

getSignature

---

#### Methods declared in class javax.management. MBeanConstructorInfo

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

OpenMBeanConstructorInfo

getDescription

,

getName

,

getSignature

---

#### Methods declared in interface javax.management.openmbean. OpenMBeanConstructorInfo

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- OpenMBeanConstructorInfoSupport

```java
public OpenMBeanConstructorInfoSupport​(
String
name,

String
description,

OpenMBeanParameterInfo
[] signature)
```

Constructs an

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

and

signature

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
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string.
**Throws:** ArrayStoreException

- If

signature

is not an
array of instances of a subclass of

MBeanParameterInfo

.

- OpenMBeanConstructorInfoSupport

```java
public OpenMBeanConstructorInfoSupport​(
String
name,

String
description,

OpenMBeanParameterInfo
[] signature,

Descriptor
descriptor)
```

Constructs an

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

,

signature

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
**Parameters:** descriptor

- The descriptor for the constructor. This may
be null which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string.
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

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanConstructorInfoSupport

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

OpenMBeanConstructorInfo

interface,
- their names are equal
- their signatures are equal.

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanConstructorInfo

interface.

**Specified by:** equals

in interface

OpenMBeanConstructorInfo
**Overrides:** equals

in class

MBeanConstructorInfo
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanConstructorInfoSupport

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanConstructorInfoSupport

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

OpenMBeanConstructorInfoSupport

instance.

The hash code of an

OpenMBeanConstructorInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name
and signature, where the signature hashCode is calculated by a
call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanConstructorInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanConstructorInfo

interface may be equal to
this

OpenMBeanConstructorInfoSupport

instance as
defined by

equals(java.lang.Object)

, but may have a
different hash code if it is calculated differently.

As

OpenMBeanConstructorInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

**Specified by:** hashCode

in interface

OpenMBeanConstructorInfo
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanConstructorInfoSupport

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

OpenMBeanConstructorInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanConstructorInfoSupport

),
the name and signature of the described constructor and the
string representation of its descriptor.

As

OpenMBeanConstructorInfoSupport

instances are
immutable, the string representation for this instance is
calculated once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

**Specified by:** toString

in interface

OpenMBeanConstructorInfo
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanConstructorInfoSupport

instance

Constructor Detail

- OpenMBeanConstructorInfoSupport

```java
public OpenMBeanConstructorInfoSupport​(
String
name,

String
description,

OpenMBeanParameterInfo
[] signature)
```

Constructs an

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

and

signature

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
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string.
**Throws:** ArrayStoreException

- If

signature

is not an
array of instances of a subclass of

MBeanParameterInfo

.

- OpenMBeanConstructorInfoSupport

```java
public OpenMBeanConstructorInfoSupport​(
String
name,

String
description,

OpenMBeanParameterInfo
[] signature,

Descriptor
descriptor)
```

Constructs an

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

,

signature

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
**Parameters:** descriptor

- The descriptor for the constructor. This may
be null which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string.
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

OpenMBeanConstructorInfoSupport

```java
public OpenMBeanConstructorInfoSupport​(
String
name,

String
description,

OpenMBeanParameterInfo
[] signature)
```

Constructs an

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

and

signature

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
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string.
**Throws:** ArrayStoreException

- If

signature

is not an
array of instances of a subclass of

MBeanParameterInfo

.

---

#### OpenMBeanConstructorInfoSupport

public OpenMBeanConstructorInfoSupport​(

String

name,

String

description,

OpenMBeanParameterInfo

[] signature)

Constructs an

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

and

signature

.

The

signature

array parameter is internally copied,
so that subsequent changes to the array referenced by

signature

have no effect on this instance.

Constructs an

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

and

signature

.

The

signature

array parameter is internally copied,
so that subsequent changes to the array referenced by

signature

have no effect on this instance.

OpenMBeanConstructorInfoSupport

```java
public OpenMBeanConstructorInfoSupport​(
String
name,

String
description,

OpenMBeanParameterInfo
[] signature,

Descriptor
descriptor)
```

Constructs an

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

,

signature

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
**Parameters:** descriptor

- The descriptor for the constructor. This may
be null which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string.
**Throws:** ArrayStoreException

- If

signature

is not an
array of instances of a subclass of

MBeanParameterInfo

.
**Since:** 1.6

---

#### OpenMBeanConstructorInfoSupport

public OpenMBeanConstructorInfoSupport​(

String

name,

String

description,

OpenMBeanParameterInfo

[] signature,

Descriptor

descriptor)

Constructs an

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

,

signature

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

OpenMBeanConstructorInfoSupport

instance, which describes the constructor of a class of open
MBeans with the specified

name

,

description

,

signature

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

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanConstructorInfoSupport

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

OpenMBeanConstructorInfo

interface,
- their names are equal
- their signatures are equal.

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanConstructorInfo

interface.

**Specified by:** equals

in interface

OpenMBeanConstructorInfo
**Overrides:** equals

in class

MBeanConstructorInfo
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanConstructorInfoSupport

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanConstructorInfoSupport

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

OpenMBeanConstructorInfoSupport

instance.

The hash code of an

OpenMBeanConstructorInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name
and signature, where the signature hashCode is calculated by a
call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanConstructorInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanConstructorInfo

interface may be equal to
this

OpenMBeanConstructorInfoSupport

instance as
defined by

equals(java.lang.Object)

, but may have a
different hash code if it is calculated differently.

As

OpenMBeanConstructorInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

**Specified by:** hashCode

in interface

OpenMBeanConstructorInfo
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanConstructorInfoSupport

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

OpenMBeanConstructorInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanConstructorInfoSupport

),
the name and signature of the described constructor and the
string representation of its descriptor.

As

OpenMBeanConstructorInfoSupport

instances are
immutable, the string representation for this instance is
calculated once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

**Specified by:** toString

in interface

OpenMBeanConstructorInfo
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanConstructorInfoSupport

instance

---

#### Method Detail

equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanConstructorInfoSupport

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

OpenMBeanConstructorInfo

interface,
- their names are equal
- their signatures are equal.

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanConstructorInfo

interface.

**Specified by:** equals

in interface

OpenMBeanConstructorInfo
**Overrides:** equals

in class

MBeanConstructorInfo
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanConstructorInfoSupport

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanConstructorInfoSupport

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

OpenMBeanConstructorInfoSupport

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

OpenMBeanConstructorInfo

interface,
- their names are equal
- their signatures are equal.

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanConstructorInfo

interface.

Compares the specified

obj

parameter with this

OpenMBeanConstructorInfoSupport

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

OpenMBeanConstructorInfo

interface,
- their names are equal
- their signatures are equal.

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanConstructorInfo

interface.

obj

is non null,

obj

also implements the

OpenMBeanConstructorInfo

interface,

their names are equal

their signatures are equal.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this

OpenMBeanConstructorInfoSupport

instance.

The hash code of an

OpenMBeanConstructorInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name
and signature, where the signature hashCode is calculated by a
call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanConstructorInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanConstructorInfo

interface may be equal to
this

OpenMBeanConstructorInfoSupport

instance as
defined by

equals(java.lang.Object)

, but may have a
different hash code if it is calculated differently.

As

OpenMBeanConstructorInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

**Specified by:** hashCode

in interface

OpenMBeanConstructorInfo
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanConstructorInfoSupport

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this

OpenMBeanConstructorInfoSupport

instance.

The hash code of an

OpenMBeanConstructorInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name
and signature, where the signature hashCode is calculated by a
call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanConstructorInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanConstructorInfo

interface may be equal to
this

OpenMBeanConstructorInfoSupport

instance as
defined by

equals(java.lang.Object)

, but may have a
different hash code if it is calculated differently.

As

OpenMBeanConstructorInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

Returns the hash code value for this

OpenMBeanConstructorInfoSupport

instance.

The hash code of an

OpenMBeanConstructorInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name
and signature, where the signature hashCode is calculated by a
call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanConstructorInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanConstructorInfo

interface may be equal to
this

OpenMBeanConstructorInfoSupport

instance as
defined by

equals(java.lang.Object)

, but may have a
different hash code if it is calculated differently.

As

OpenMBeanConstructorInfoSupport

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

OpenMBeanConstructorInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanConstructorInfoSupport

),
the name and signature of the described constructor and the
string representation of its descriptor.

As

OpenMBeanConstructorInfoSupport

instances are
immutable, the string representation for this instance is
calculated once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

**Specified by:** toString

in interface

OpenMBeanConstructorInfo
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanConstructorInfoSupport

instance

---

#### toString

public

String

toString()

Returns a string representation of this

OpenMBeanConstructorInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanConstructorInfoSupport

),
the name and signature of the described constructor and the
string representation of its descriptor.

As

OpenMBeanConstructorInfoSupport

instances are
immutable, the string representation for this instance is
calculated once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

Returns a string representation of this

OpenMBeanConstructorInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanConstructorInfoSupport

),
the name and signature of the described constructor and the
string representation of its descriptor.

As

OpenMBeanConstructorInfoSupport

instances are
immutable, the string representation for this instance is
calculated once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

---

