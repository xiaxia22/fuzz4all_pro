# Interface OpenMBeanConstructorInfo

**Source:** `java.management\javax\management\openmbean\OpenMBeanConstructorInfo.html`

### Class Description

```java
public interface
OpenMBeanConstructorInfo
```

Describes a constructor of an Open MBean.

This interface declares the same methods as the class

MBeanConstructorInfo

. A class implementing this
interface (typically

OpenMBeanConstructorInfoSupport

)
should extend

MBeanConstructorInfo

.

The

getSignature()

method should return at runtime an
array of instances of a subclass of

MBeanParameterInfo

which implements the

OpenMBeanParameterInfo

interface
(typically

OpenMBeanParameterInfoSupport

).

**All Known Implementing Classes:** OpenMBeanConstructorInfoSupport

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getDescription()

Returns a human readable description of the constructor
described by this

OpenMBeanConstructorInfo

instance.

**Returns:**
- the description.

---

#### String
getName()

Returns the name of the constructor
described by this

OpenMBeanConstructorInfo

instance.

**Returns:**
- the name.

---

#### MBeanParameterInfo
[] getSignature()

Returns an array of

OpenMBeanParameterInfo

instances
describing each parameter in the signature of the constructor
described by this

OpenMBeanConstructorInfo

instance.

**Returns:**
- the signature.

---

#### boolean equals​(
Object
obj)

Compares the specified

obj

parameter with this

OpenMBeanConstructorInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

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

parameters which are
different implementations of the

OpenMBeanConstructorInfo

interface.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to be compared for equality with this

OpenMBeanConstructorInfo

instance;

**Returns:**
- true

if the specified object is equal to this

OpenMBeanConstructorInfo

instance.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this

OpenMBeanConstructorInfo

instance.

The hash code of an

OpenMBeanConstructorInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name and signature, where the signature hashCode is calculated by a call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanConstructorInfo

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

OpenMBeanConstructorInfo

instance

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### String
toString()

Returns a string representation of this

OpenMBeanConstructorInfo

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanConstructorInfo

),
and the name and signature of the described constructor.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

OpenMBeanConstructorInfo

instance

---

### Additional Sections

#### Interface OpenMBeanConstructorInfo

**All Known Implementing Classes:** OpenMBeanConstructorInfoSupport

```java
public interface
OpenMBeanConstructorInfo
```

Describes a constructor of an Open MBean.

This interface declares the same methods as the class

MBeanConstructorInfo

. A class implementing this
interface (typically

OpenMBeanConstructorInfoSupport

)
should extend

MBeanConstructorInfo

.

The

getSignature()

method should return at runtime an
array of instances of a subclass of

MBeanParameterInfo

which implements the

OpenMBeanParameterInfo

interface
(typically

OpenMBeanParameterInfoSupport

).

**Since:** 1.5

public interface

OpenMBeanConstructorInfo

Describes a constructor of an Open MBean.

This interface declares the same methods as the class

MBeanConstructorInfo

. A class implementing this
interface (typically

OpenMBeanConstructorInfoSupport

)
should extend

MBeanConstructorInfo

.

The

getSignature()

method should return at runtime an
array of instances of a subclass of

MBeanParameterInfo

which implements the

OpenMBeanParameterInfo

interface
(typically

OpenMBeanParameterInfoSupport

).

Describes a constructor of an Open MBean.

This interface declares the same methods as the class

MBeanConstructorInfo

. A class implementing this
interface (typically

OpenMBeanConstructorInfoSupport

)
should extend

MBeanConstructorInfo

.

The

getSignature()

method should return at runtime an
array of instances of a subclass of

MBeanParameterInfo

which implements the

OpenMBeanParameterInfo

interface
(typically

OpenMBeanParameterInfoSupport

).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

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

OpenMBeanConstructorInfo

instance for equality.

String

getDescription

()

Returns a human readable description of the constructor
described by this

OpenMBeanConstructorInfo

instance.

String

getName

()

Returns the name of the constructor
described by this

OpenMBeanConstructorInfo

instance.

MBeanParameterInfo

[]

getSignature

()

Returns an array of

OpenMBeanParameterInfo

instances
describing each parameter in the signature of the constructor
described by this

OpenMBeanConstructorInfo

instance.

int

hashCode

()

Returns the hash code value for this

OpenMBeanConstructorInfo

instance.

String

toString

()

Returns a string representation of this

OpenMBeanConstructorInfo

instance.

Method Summary

All Methods

Instance Methods

Abstract Methods

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

OpenMBeanConstructorInfo

instance for equality.

String

getDescription

()

Returns a human readable description of the constructor
described by this

OpenMBeanConstructorInfo

instance.

String

getName

()

Returns the name of the constructor
described by this

OpenMBeanConstructorInfo

instance.

MBeanParameterInfo

[]

getSignature

()

Returns an array of

OpenMBeanParameterInfo

instances
describing each parameter in the signature of the constructor
described by this

OpenMBeanConstructorInfo

instance.

int

hashCode

()

Returns the hash code value for this

OpenMBeanConstructorInfo

instance.

String

toString

()

Returns a string representation of this

OpenMBeanConstructorInfo

instance.

---

#### Method Summary

Compares the specified

obj

parameter with this

OpenMBeanConstructorInfo

instance for equality.

Returns a human readable description of the constructor
described by this

OpenMBeanConstructorInfo

instance.

Returns the name of the constructor
described by this

OpenMBeanConstructorInfo

instance.

Returns an array of

OpenMBeanParameterInfo

instances
describing each parameter in the signature of the constructor
described by this

OpenMBeanConstructorInfo

instance.

Returns the hash code value for this

OpenMBeanConstructorInfo

instance.

Returns a string representation of this

OpenMBeanConstructorInfo

instance.

============ METHOD DETAIL ==========

- Method Detail

- getDescription

```java
String
getDescription()
```

Returns a human readable description of the constructor
described by this

OpenMBeanConstructorInfo

instance.

**Returns:** the description.

- getName

```java
String
getName()
```

Returns the name of the constructor
described by this

OpenMBeanConstructorInfo

instance.

**Returns:** the name.

- getSignature

```java
MBeanParameterInfo
[] getSignature()
```

Returns an array of

OpenMBeanParameterInfo

instances
describing each parameter in the signature of the constructor
described by this

OpenMBeanConstructorInfo

instance.

**Returns:** the signature.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanConstructorInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

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

parameters which are
different implementations of the

OpenMBeanConstructorInfo

interface.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanConstructorInfo

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanConstructorInfo

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this

OpenMBeanConstructorInfo

instance.

The hash code of an

OpenMBeanConstructorInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name and signature, where the signature hashCode is calculated by a call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanConstructorInfo

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

OpenMBeanConstructorInfo

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

OpenMBeanConstructorInfo

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanConstructorInfo

),
and the name and signature of the described constructor.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanConstructorInfo

instance

Method Detail

- getDescription

```java
String
getDescription()
```

Returns a human readable description of the constructor
described by this

OpenMBeanConstructorInfo

instance.

**Returns:** the description.

- getName

```java
String
getName()
```

Returns the name of the constructor
described by this

OpenMBeanConstructorInfo

instance.

**Returns:** the name.

- getSignature

```java
MBeanParameterInfo
[] getSignature()
```

Returns an array of

OpenMBeanParameterInfo

instances
describing each parameter in the signature of the constructor
described by this

OpenMBeanConstructorInfo

instance.

**Returns:** the signature.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanConstructorInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

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

parameters which are
different implementations of the

OpenMBeanConstructorInfo

interface.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanConstructorInfo

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanConstructorInfo

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this

OpenMBeanConstructorInfo

instance.

The hash code of an

OpenMBeanConstructorInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name and signature, where the signature hashCode is calculated by a call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanConstructorInfo

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

OpenMBeanConstructorInfo

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

OpenMBeanConstructorInfo

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanConstructorInfo

),
and the name and signature of the described constructor.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanConstructorInfo

instance

---

#### Method Detail

getDescription

```java
String
getDescription()
```

Returns a human readable description of the constructor
described by this

OpenMBeanConstructorInfo

instance.

**Returns:** the description.

---

#### getDescription

String

getDescription()

Returns a human readable description of the constructor
described by this

OpenMBeanConstructorInfo

instance.

getName

```java
String
getName()
```

Returns the name of the constructor
described by this

OpenMBeanConstructorInfo

instance.

**Returns:** the name.

---

#### getName

String

getName()

Returns the name of the constructor
described by this

OpenMBeanConstructorInfo

instance.

getSignature

```java
MBeanParameterInfo
[] getSignature()
```

Returns an array of

OpenMBeanParameterInfo

instances
describing each parameter in the signature of the constructor
described by this

OpenMBeanConstructorInfo

instance.

**Returns:** the signature.

---

#### getSignature

MBeanParameterInfo

[] getSignature()

Returns an array of

OpenMBeanParameterInfo

instances
describing each parameter in the signature of the constructor
described by this

OpenMBeanConstructorInfo

instance.

equals

```java
boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanConstructorInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

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

parameters which are
different implementations of the

OpenMBeanConstructorInfo

interface.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanConstructorInfo

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanConstructorInfo

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

OpenMBeanConstructorInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

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

parameters which are
different implementations of the

OpenMBeanConstructorInfo

interface.

Returns

true

if and only if all of the following statements are true:

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

parameters which are
different implementations of the

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
int hashCode()
```

Returns the hash code value for this

OpenMBeanConstructorInfo

instance.

The hash code of an

OpenMBeanConstructorInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name and signature, where the signature hashCode is calculated by a call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanConstructorInfo

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

OpenMBeanConstructorInfo

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

int hashCode()

Returns the hash code value for this

OpenMBeanConstructorInfo

instance.

The hash code of an

OpenMBeanConstructorInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name and signature, where the signature hashCode is calculated by a call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanConstructorInfo

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

The hash code of an

OpenMBeanConstructorInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name and signature, where the signature hashCode is calculated by a call to

java.util.Arrays.asList(this.getSignature).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanConstructorInfo

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

OpenMBeanConstructorInfo

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

OpenMBeanConstructorInfo

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanConstructorInfo

),
and the name and signature of the described constructor.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanConstructorInfo

instance

---

#### toString

String

toString()

Returns a string representation of this

OpenMBeanConstructorInfo

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanConstructorInfo

),
and the name and signature of the described constructor.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanConstructorInfo

),
and the name and signature of the described constructor.

---

