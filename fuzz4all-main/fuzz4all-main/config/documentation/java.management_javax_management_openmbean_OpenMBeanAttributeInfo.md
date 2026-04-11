# Interface OpenMBeanAttributeInfo

**Source:** `java.management\javax\management\openmbean\OpenMBeanAttributeInfo.html`

### Class Description

```java
public interface
OpenMBeanAttributeInfo

extends
OpenMBeanParameterInfo
```

Describes an attribute of an open MBean.

This interface declares the same methods as the class

MBeanAttributeInfo

. A class implementing this
interface (typically

OpenMBeanAttributeInfoSupport

) should
extend

MBeanAttributeInfo

.

**All Superinterfaces:** OpenMBeanParameterInfo

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isReadable()

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance is readable,

false

otherwise.

**Returns:**
- true if the attribute is readable.

---

#### boolean isWritable()

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance is writable,

false

otherwise.

**Returns:**
- true if the attribute is writable.

---

#### boolean isIs()

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance
is accessed through a

is

XXX

getter
(applies only to

boolean

and

Boolean

values),

false

otherwise.

**Returns:**
- true if the attribute is accessed through

is

XXX

.

---

#### boolean equals​(
Object
obj)

Compares the specified

obj

parameter with this

OpenMBeanAttributeInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanAttributeInfo

interface,
- their names are equal
- their open types are equal
- their access properties (isReadable, isWritable and isIs) are equal
- their default, min, max and legal values are equal.

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

OpenMBeanAttributeInfo

interface.

**Specified by:**
- equals

in interface

OpenMBeanParameterInfo

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to be compared for equality with this

OpenMBeanAttributeInfo

instance;

**Returns:**
- true

if the specified object is equal to this

OpenMBeanAttributeInfo

instance.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this

OpenMBeanAttributeInfo

instance.

The hash code of an

OpenMBeanAttributeInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name, its

open type

, and its default, min, max and legal values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanAttributeInfo

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

**Specified by:**
- hashCode

in interface

OpenMBeanParameterInfo

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this

OpenMBeanAttributeInfo

instance

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### String
toString()

Returns a string representation of this

OpenMBeanAttributeInfo

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanAttributeInfo

),
the string representation of the name and open type of the described attribute,
and the string representation of its default, min, max and legal values.

**Specified by:**
- toString

in interface

OpenMBeanParameterInfo

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

OpenMBeanAttributeInfo

instance

---

### Additional Sections

#### Interface OpenMBeanAttributeInfo

**All Superinterfaces:** OpenMBeanParameterInfo

**All Known Implementing Classes:** OpenMBeanAttributeInfoSupport

```java
public interface
OpenMBeanAttributeInfo

extends
OpenMBeanParameterInfo
```

Describes an attribute of an open MBean.

This interface declares the same methods as the class

MBeanAttributeInfo

. A class implementing this
interface (typically

OpenMBeanAttributeInfoSupport

) should
extend

MBeanAttributeInfo

.

**Since:** 1.5

public interface

OpenMBeanAttributeInfo

extends

OpenMBeanParameterInfo

Describes an attribute of an open MBean.

This interface declares the same methods as the class

MBeanAttributeInfo

. A class implementing this
interface (typically

OpenMBeanAttributeInfoSupport

) should
extend

MBeanAttributeInfo

.

Describes an attribute of an open MBean.

This interface declares the same methods as the class

MBeanAttributeInfo

. A class implementing this
interface (typically

OpenMBeanAttributeInfoSupport

) should
extend

MBeanAttributeInfo

.

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

OpenMBeanAttributeInfo

instance for equality.

int

hashCode

()

Returns the hash code value for this

OpenMBeanAttributeInfo

instance.

boolean

isIs

()

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance
is accessed through a

is

XXX

getter
(applies only to

boolean

and

Boolean

values),

false

otherwise.

boolean

isReadable

()

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance is readable,

false

otherwise.

boolean

isWritable

()

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance is writable,

false

otherwise.

String

toString

()

Returns a string representation of this

OpenMBeanAttributeInfo

instance.

- Methods declared in interface javax.management.openmbean.

OpenMBeanParameterInfo

getDefaultValue

,

getDescription

,

getLegalValues

,

getMaxValue

,

getMinValue

,

getName

,

getOpenType

,

hasDefaultValue

,

hasLegalValues

,

hasMaxValue

,

hasMinValue

,

isValue

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

OpenMBeanAttributeInfo

instance for equality.

int

hashCode

()

Returns the hash code value for this

OpenMBeanAttributeInfo

instance.

boolean

isIs

()

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance
is accessed through a

is

XXX

getter
(applies only to

boolean

and

Boolean

values),

false

otherwise.

boolean

isReadable

()

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance is readable,

false

otherwise.

boolean

isWritable

()

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance is writable,

false

otherwise.

String

toString

()

Returns a string representation of this

OpenMBeanAttributeInfo

instance.

- Methods declared in interface javax.management.openmbean.

OpenMBeanParameterInfo

getDefaultValue

,

getDescription

,

getLegalValues

,

getMaxValue

,

getMinValue

,

getName

,

getOpenType

,

hasDefaultValue

,

hasLegalValues

,

hasMaxValue

,

hasMinValue

,

isValue

---

#### Method Summary

Compares the specified

obj

parameter with this

OpenMBeanAttributeInfo

instance for equality.

Returns the hash code value for this

OpenMBeanAttributeInfo

instance.

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance
is accessed through a

is

XXX

getter
(applies only to

boolean

and

Boolean

values),

false

otherwise.

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance is readable,

false

otherwise.

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance is writable,

false

otherwise.

Returns a string representation of this

OpenMBeanAttributeInfo

instance.

Methods declared in interface javax.management.openmbean.

OpenMBeanParameterInfo

getDefaultValue

,

getDescription

,

getLegalValues

,

getMaxValue

,

getMinValue

,

getName

,

getOpenType

,

hasDefaultValue

,

hasLegalValues

,

hasMaxValue

,

hasMinValue

,

isValue

---

#### Methods declared in interface javax.management.openmbean. OpenMBeanParameterInfo

============ METHOD DETAIL ==========

- Method Detail

- isReadable

```java
boolean isReadable()
```

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance is readable,

false

otherwise.

**Returns:** true if the attribute is readable.

- isWritable

```java
boolean isWritable()
```

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance is writable,

false

otherwise.

**Returns:** true if the attribute is writable.

- isIs

```java
boolean isIs()
```

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance
is accessed through a

is

XXX

getter
(applies only to

boolean

and

Boolean

values),

false

otherwise.

**Returns:** true if the attribute is accessed through

is

XXX

.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanAttributeInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanAttributeInfo

interface,
- their names are equal
- their open types are equal
- their access properties (isReadable, isWritable and isIs) are equal
- their default, min, max and legal values are equal.

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

OpenMBeanAttributeInfo

interface.

**Specified by:** equals

in interface

OpenMBeanParameterInfo
**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanAttributeInfo

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanAttributeInfo

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this

OpenMBeanAttributeInfo

instance.

The hash code of an

OpenMBeanAttributeInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name, its

open type

, and its default, min, max and legal values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanAttributeInfo

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

**Specified by:** hashCode

in interface

OpenMBeanParameterInfo
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanAttributeInfo

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

OpenMBeanAttributeInfo

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanAttributeInfo

),
the string representation of the name and open type of the described attribute,
and the string representation of its default, min, max and legal values.

**Specified by:** toString

in interface

OpenMBeanParameterInfo
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanAttributeInfo

instance

Method Detail

- isReadable

```java
boolean isReadable()
```

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance is readable,

false

otherwise.

**Returns:** true if the attribute is readable.

- isWritable

```java
boolean isWritable()
```

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance is writable,

false

otherwise.

**Returns:** true if the attribute is writable.

- isIs

```java
boolean isIs()
```

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance
is accessed through a

is

XXX

getter
(applies only to

boolean

and

Boolean

values),

false

otherwise.

**Returns:** true if the attribute is accessed through

is

XXX

.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanAttributeInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanAttributeInfo

interface,
- their names are equal
- their open types are equal
- their access properties (isReadable, isWritable and isIs) are equal
- their default, min, max and legal values are equal.

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

OpenMBeanAttributeInfo

interface.

**Specified by:** equals

in interface

OpenMBeanParameterInfo
**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanAttributeInfo

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanAttributeInfo

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this

OpenMBeanAttributeInfo

instance.

The hash code of an

OpenMBeanAttributeInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name, its

open type

, and its default, min, max and legal values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanAttributeInfo

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

**Specified by:** hashCode

in interface

OpenMBeanParameterInfo
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanAttributeInfo

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

OpenMBeanAttributeInfo

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanAttributeInfo

),
the string representation of the name and open type of the described attribute,
and the string representation of its default, min, max and legal values.

**Specified by:** toString

in interface

OpenMBeanParameterInfo
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanAttributeInfo

instance

---

#### Method Detail

isReadable

```java
boolean isReadable()
```

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance is readable,

false

otherwise.

**Returns:** true if the attribute is readable.

---

#### isReadable

boolean isReadable()

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance is readable,

false

otherwise.

isWritable

```java
boolean isWritable()
```

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance is writable,

false

otherwise.

**Returns:** true if the attribute is writable.

---

#### isWritable

boolean isWritable()

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance is writable,

false

otherwise.

isIs

```java
boolean isIs()
```

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance
is accessed through a

is

XXX

getter
(applies only to

boolean

and

Boolean

values),

false

otherwise.

**Returns:** true if the attribute is accessed through

is

XXX

.

---

#### isIs

boolean isIs()

Returns

true

if the attribute described by this

OpenMBeanAttributeInfo

instance
is accessed through a

is

XXX

getter
(applies only to

boolean

and

Boolean

values),

false

otherwise.

equals

```java
boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanAttributeInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanAttributeInfo

interface,
- their names are equal
- their open types are equal
- their access properties (isReadable, isWritable and isIs) are equal
- their default, min, max and legal values are equal.

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

OpenMBeanAttributeInfo

interface.

**Specified by:** equals

in interface

OpenMBeanParameterInfo
**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanAttributeInfo

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanAttributeInfo

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

OpenMBeanAttributeInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanAttributeInfo

interface,
- their names are equal
- their open types are equal
- their access properties (isReadable, isWritable and isIs) are equal
- their default, min, max and legal values are equal.

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

OpenMBeanAttributeInfo

interface.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanAttributeInfo

interface,
- their names are equal
- their open types are equal
- their access properties (isReadable, isWritable and isIs) are equal
- their default, min, max and legal values are equal.

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

OpenMBeanAttributeInfo

interface.

obj

is non null,

obj

also implements the

OpenMBeanAttributeInfo

interface,

their names are equal

their open types are equal

their access properties (isReadable, isWritable and isIs) are equal

their default, min, max and legal values are equal.

hashCode

```java
int hashCode()
```

Returns the hash code value for this

OpenMBeanAttributeInfo

instance.

The hash code of an

OpenMBeanAttributeInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name, its

open type

, and its default, min, max and legal values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanAttributeInfo

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

**Specified by:** hashCode

in interface

OpenMBeanParameterInfo
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanAttributeInfo

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

int hashCode()

Returns the hash code value for this

OpenMBeanAttributeInfo

instance.

The hash code of an

OpenMBeanAttributeInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name, its

open type

, and its default, min, max and legal values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanAttributeInfo

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

The hash code of an

OpenMBeanAttributeInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name, its

open type

, and its default, min, max and legal values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanAttributeInfo

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

OpenMBeanAttributeInfo

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

OpenMBeanAttributeInfo

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanAttributeInfo

),
the string representation of the name and open type of the described attribute,
and the string representation of its default, min, max and legal values.

**Specified by:** toString

in interface

OpenMBeanParameterInfo
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanAttributeInfo

instance

---

#### toString

String

toString()

Returns a string representation of this

OpenMBeanAttributeInfo

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanAttributeInfo

),
the string representation of the name and open type of the described attribute,
and the string representation of its default, min, max and legal values.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanAttributeInfo

),
the string representation of the name and open type of the described attribute,
and the string representation of its default, min, max and legal values.

---

