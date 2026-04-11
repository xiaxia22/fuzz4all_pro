# Class OpenMBeanInfoSupport

**Source:** `java.management\javax\management\openmbean\OpenMBeanInfoSupport.html`

### Class Description

```java
public class
OpenMBeanInfoSupport

extends
MBeanInfo

implements
OpenMBeanInfo
```

The

OpenMBeanInfoSupport

class describes the management
information of an

open MBean

: it is a subclass of

MBeanInfo

, and it implements the

OpenMBeanInfo

interface. Note that an

open MBean

is
recognized as such if its

getMBeanInfo()

method returns an
instance of a class which implements the OpenMBeanInfo interface,
typically

OpenMBeanInfoSupport

.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

,

OpenMBeanInfo

---

### Field Details

*No entries found.*

### Constructor Details

#### public OpenMBeanInfoSupport​(
String
className,

String
description,

OpenMBeanAttributeInfo
[] openAttributes,

OpenMBeanConstructorInfo
[] openConstructors,

OpenMBeanOperationInfo
[] openOperations,

MBeanNotificationInfo
[] notifications)

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

and

notifications

.

The

openAttributes

,

openConstructors

,

openOperations

and

notifications

array parameters are internally copied, so that subsequent changes
to the arrays referenced by these parameters have no effect on this
instance.

**Parameters:**
- className

- The fully qualified Java class name of the
open MBean described by this

OpenMBeanInfoSupport

instance.
- description

- A human readable description of the open
MBean described by this

OpenMBeanInfoSupport

instance.
- openAttributes

- The list of exposed attributes of the
described open MBean; Must be an array of instances of a
subclass of

MBeanAttributeInfo

, typically

OpenMBeanAttributeInfoSupport

.
- openConstructors

- The list of exposed public constructors
of the described open MBean; Must be an array of instances of a
subclass of

MBeanConstructorInfo

, typically

OpenMBeanConstructorInfoSupport

.
- openOperations

- The list of exposed operations of the
described open MBean. Must be an array of instances of a
subclass of

MBeanOperationInfo

, typically

OpenMBeanOperationInfoSupport

.
- notifications

- The list of notifications emitted by the
described open MBean.

**Throws:**
- ArrayStoreException

- If

openAttributes

,

openConstructors

or

openOperations

is not an array of
instances of a subclass of

MBeanAttributeInfo

,

MBeanConstructorInfo

or

MBeanOperationInfo

respectively.

---

#### public OpenMBeanInfoSupport​(
String
className,

String
description,

OpenMBeanAttributeInfo
[] openAttributes,

OpenMBeanConstructorInfo
[] openConstructors,

OpenMBeanOperationInfo
[] openOperations,

MBeanNotificationInfo
[] notifications,

Descriptor
descriptor)

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

,

notifications

, and

descriptor

.

The

openAttributes

,

openConstructors

,

openOperations

and

notifications

array parameters are
internally copied, so that subsequent changes to the arrays
referenced by these parameters have no effect on this
instance.

**Parameters:**
- className

- The fully qualified Java class name of the
open MBean described by this

OpenMBeanInfoSupport

instance.
- description

- A human readable description of the open
MBean described by this

OpenMBeanInfoSupport

instance.
- openAttributes

- The list of exposed attributes of the
described open MBean; Must be an array of instances of a
subclass of

MBeanAttributeInfo

, typically

OpenMBeanAttributeInfoSupport

.
- openConstructors

- The list of exposed public constructors
of the described open MBean; Must be an array of instances of a
subclass of

MBeanConstructorInfo

, typically

OpenMBeanConstructorInfoSupport

.
- openOperations

- The list of exposed operations of the
described open MBean. Must be an array of instances of a
subclass of

MBeanOperationInfo

, typically

OpenMBeanOperationInfoSupport

.
- notifications

- The list of notifications emitted by the
described open MBean.
- descriptor

- The descriptor for the MBean. This may be null
which is equivalent to an empty descriptor.

**Throws:**
- ArrayStoreException

- If

openAttributes

,

openConstructors

or

openOperations

is not an array of
instances of a subclass of

MBeanAttributeInfo

,

MBeanConstructorInfo

or

MBeanOperationInfo

respectively.

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

OpenMBeanInfoSupport

instance for equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanInfo

interface,
- their class names are equal
- their infos on attributes, constructors, operations and
notifications are equal

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanInfo

interface.

**Specified by:**
- equals

in interface

OpenMBeanInfo

**Overrides:**
- equals

in class

MBeanInfo

**Parameters:**
- obj

- the object to be compared for equality with this

OpenMBeanInfoSupport

instance;

**Returns:**
- true

if the specified object is equal to this

OpenMBeanInfoSupport

instance.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this

OpenMBeanInfoSupport

instance.

The hash code of an

OpenMBeanInfoSupport

instance is
the sum of the hash codes of all elements of information used
in

equals

comparisons (ie: its class name, and its
infos on attributes, constructors, operations and
notifications, where the hashCode of each of these arrays is
calculated by a call to

new
java.util.HashSet(java.util.Arrays.asList(this.getSignature)).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanInfoSupport

instances

t1

and

t2

, as
required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanInfo

interface may be equal to this

OpenMBeanInfoSupport

instance as defined by

equals(java.lang.Object)

, but may have a different hash code
if it is calculated differently.

As

OpenMBeanInfoSupport

instances are immutable, the
hash code for this instance is calculated once, on the first
call to

hashCode

, and then the same value is returned
for subsequent calls.

**Specified by:**
- hashCode

in interface

OpenMBeanInfo

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this

OpenMBeanInfoSupport

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

OpenMBeanInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanInfoSupport

),
the MBean class name, the string representation of infos on
attributes, constructors, operations and notifications of the
described MBean and the string representation of the descriptor.

As

OpenMBeanInfoSupport

instances are immutable, the
string representation for this instance is calculated once, on
the first call to

toString

, and then the same value is
returned for subsequent calls.

**Specified by:**
- toString

in interface

OpenMBeanInfo

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

OpenMBeanInfoSupport

instance

---

### Additional Sections

#### Class OpenMBeanInfoSupport

java.lang.Object

- javax.management.MBeanInfo
- - javax.management.openmbean.OpenMBeanInfoSupport

javax.management.MBeanInfo

- javax.management.openmbean.OpenMBeanInfoSupport

javax.management.openmbean.OpenMBeanInfoSupport

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

,

OpenMBeanInfo

```java
public class
OpenMBeanInfoSupport

extends
MBeanInfo

implements
OpenMBeanInfo
```

The

OpenMBeanInfoSupport

class describes the management
information of an

open MBean

: it is a subclass of

MBeanInfo

, and it implements the

OpenMBeanInfo

interface. Note that an

open MBean

is
recognized as such if its

getMBeanInfo()

method returns an
instance of a class which implements the OpenMBeanInfo interface,
typically

OpenMBeanInfoSupport

.

**Since:** 1.5
**See Also:** Serialized Form

public class

OpenMBeanInfoSupport

extends

MBeanInfo

implements

OpenMBeanInfo

The

OpenMBeanInfoSupport

class describes the management
information of an

open MBean

: it is a subclass of

MBeanInfo

, and it implements the

OpenMBeanInfo

interface. Note that an

open MBean

is
recognized as such if its

getMBeanInfo()

method returns an
instance of a class which implements the OpenMBeanInfo interface,
typically

OpenMBeanInfoSupport

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

OpenMBeanInfoSupport

​(

String

className,

String

description,

OpenMBeanAttributeInfo

[] openAttributes,

OpenMBeanConstructorInfo

[] openConstructors,

OpenMBeanOperationInfo

[] openOperations,

MBeanNotificationInfo

[] notifications)

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

and

notifications

.

OpenMBeanInfoSupport

​(

String

className,

String

description,

OpenMBeanAttributeInfo

[] openAttributes,

OpenMBeanConstructorInfo

[] openConstructors,

OpenMBeanOperationInfo

[] openOperations,

MBeanNotificationInfo

[] notifications,

Descriptor

descriptor)

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

,

notifications

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

OpenMBeanInfoSupport

instance for equality.

int

hashCode

()

Returns the hash code value for this

OpenMBeanInfoSupport

instance.

String

toString

()

Returns a string representation of this

OpenMBeanInfoSupport

instance.

- Methods declared in class javax.management.

MBeanInfo

clone

,

getAttributes

,

getClassName

,

getConstructors

,

getDescription

,

getDescriptor

,

getNotifications

,

getOperations

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

OpenMBeanInfo

getAttributes

,

getClassName

,

getConstructors

,

getDescription

,

getNotifications

,

getOperations

Constructor Summary

Constructors

Constructor

Description

OpenMBeanInfoSupport

​(

String

className,

String

description,

OpenMBeanAttributeInfo

[] openAttributes,

OpenMBeanConstructorInfo

[] openConstructors,

OpenMBeanOperationInfo

[] openOperations,

MBeanNotificationInfo

[] notifications)

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

and

notifications

.

OpenMBeanInfoSupport

​(

String

className,

String

description,

OpenMBeanAttributeInfo

[] openAttributes,

OpenMBeanConstructorInfo

[] openConstructors,

OpenMBeanOperationInfo

[] openOperations,

MBeanNotificationInfo

[] notifications,

Descriptor

descriptor)

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

,

notifications

, and

descriptor

.

---

#### Constructor Summary

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

and

notifications

.

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

,

notifications

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

OpenMBeanInfoSupport

instance for equality.

int

hashCode

()

Returns the hash code value for this

OpenMBeanInfoSupport

instance.

String

toString

()

Returns a string representation of this

OpenMBeanInfoSupport

instance.

- Methods declared in class javax.management.

MBeanInfo

clone

,

getAttributes

,

getClassName

,

getConstructors

,

getDescription

,

getDescriptor

,

getNotifications

,

getOperations

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

OpenMBeanInfo

getAttributes

,

getClassName

,

getConstructors

,

getDescription

,

getNotifications

,

getOperations

---

#### Method Summary

Compares the specified

obj

parameter with this

OpenMBeanInfoSupport

instance for equality.

Returns the hash code value for this

OpenMBeanInfoSupport

instance.

Returns a string representation of this

OpenMBeanInfoSupport

instance.

Methods declared in class javax.management.

MBeanInfo

clone

,

getAttributes

,

getClassName

,

getConstructors

,

getDescription

,

getDescriptor

,

getNotifications

,

getOperations

---

#### Methods declared in class javax.management. MBeanInfo

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

OpenMBeanInfo

getAttributes

,

getClassName

,

getConstructors

,

getDescription

,

getNotifications

,

getOperations

---

#### Methods declared in interface javax.management.openmbean. OpenMBeanInfo

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- OpenMBeanInfoSupport

```java
public OpenMBeanInfoSupport​(
String
className,

String
description,

OpenMBeanAttributeInfo
[] openAttributes,

OpenMBeanConstructorInfo
[] openConstructors,

OpenMBeanOperationInfo
[] openOperations,

MBeanNotificationInfo
[] notifications)
```

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

and

notifications

.

The

openAttributes

,

openConstructors

,

openOperations

and

notifications

array parameters are internally copied, so that subsequent changes
to the arrays referenced by these parameters have no effect on this
instance.

**Parameters:** className

- The fully qualified Java class name of the
open MBean described by this

OpenMBeanInfoSupport

instance.
**Parameters:** description

- A human readable description of the open
MBean described by this

OpenMBeanInfoSupport

instance.
**Parameters:** openAttributes

- The list of exposed attributes of the
described open MBean; Must be an array of instances of a
subclass of

MBeanAttributeInfo

, typically

OpenMBeanAttributeInfoSupport

.
**Parameters:** openConstructors

- The list of exposed public constructors
of the described open MBean; Must be an array of instances of a
subclass of

MBeanConstructorInfo

, typically

OpenMBeanConstructorInfoSupport

.
**Parameters:** openOperations

- The list of exposed operations of the
described open MBean. Must be an array of instances of a
subclass of

MBeanOperationInfo

, typically

OpenMBeanOperationInfoSupport

.
**Parameters:** notifications

- The list of notifications emitted by the
described open MBean.
**Throws:** ArrayStoreException

- If

openAttributes

,

openConstructors

or

openOperations

is not an array of
instances of a subclass of

MBeanAttributeInfo

,

MBeanConstructorInfo

or

MBeanOperationInfo

respectively.

- OpenMBeanInfoSupport

```java
public OpenMBeanInfoSupport​(
String
className,

String
description,

OpenMBeanAttributeInfo
[] openAttributes,

OpenMBeanConstructorInfo
[] openConstructors,

OpenMBeanOperationInfo
[] openOperations,

MBeanNotificationInfo
[] notifications,

Descriptor
descriptor)
```

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

,

notifications

, and

descriptor

.

The

openAttributes

,

openConstructors

,

openOperations

and

notifications

array parameters are
internally copied, so that subsequent changes to the arrays
referenced by these parameters have no effect on this
instance.

**Parameters:** className

- The fully qualified Java class name of the
open MBean described by this

OpenMBeanInfoSupport

instance.
**Parameters:** description

- A human readable description of the open
MBean described by this

OpenMBeanInfoSupport

instance.
**Parameters:** openAttributes

- The list of exposed attributes of the
described open MBean; Must be an array of instances of a
subclass of

MBeanAttributeInfo

, typically

OpenMBeanAttributeInfoSupport

.
**Parameters:** openConstructors

- The list of exposed public constructors
of the described open MBean; Must be an array of instances of a
subclass of

MBeanConstructorInfo

, typically

OpenMBeanConstructorInfoSupport

.
**Parameters:** openOperations

- The list of exposed operations of the
described open MBean. Must be an array of instances of a
subclass of

MBeanOperationInfo

, typically

OpenMBeanOperationInfoSupport

.
**Parameters:** notifications

- The list of notifications emitted by the
described open MBean.
**Parameters:** descriptor

- The descriptor for the MBean. This may be null
which is equivalent to an empty descriptor.
**Throws:** ArrayStoreException

- If

openAttributes

,

openConstructors

or

openOperations

is not an array of
instances of a subclass of

MBeanAttributeInfo

,

MBeanConstructorInfo

or

MBeanOperationInfo

respectively.
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

OpenMBeanInfoSupport

instance for equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanInfo

interface,
- their class names are equal
- their infos on attributes, constructors, operations and
notifications are equal

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanInfo

interface.

**Specified by:** equals

in interface

OpenMBeanInfo
**Overrides:** equals

in class

MBeanInfo
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanInfoSupport

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanInfoSupport

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

OpenMBeanInfoSupport

instance.

The hash code of an

OpenMBeanInfoSupport

instance is
the sum of the hash codes of all elements of information used
in

equals

comparisons (ie: its class name, and its
infos on attributes, constructors, operations and
notifications, where the hashCode of each of these arrays is
calculated by a call to

new
java.util.HashSet(java.util.Arrays.asList(this.getSignature)).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanInfoSupport

instances

t1

and

t2

, as
required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanInfo

interface may be equal to this

OpenMBeanInfoSupport

instance as defined by

equals(java.lang.Object)

, but may have a different hash code
if it is calculated differently.

As

OpenMBeanInfoSupport

instances are immutable, the
hash code for this instance is calculated once, on the first
call to

hashCode

, and then the same value is returned
for subsequent calls.

**Specified by:** hashCode

in interface

OpenMBeanInfo
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanInfoSupport

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

OpenMBeanInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanInfoSupport

),
the MBean class name, the string representation of infos on
attributes, constructors, operations and notifications of the
described MBean and the string representation of the descriptor.

As

OpenMBeanInfoSupport

instances are immutable, the
string representation for this instance is calculated once, on
the first call to

toString

, and then the same value is
returned for subsequent calls.

**Specified by:** toString

in interface

OpenMBeanInfo
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanInfoSupport

instance

Constructor Detail

- OpenMBeanInfoSupport

```java
public OpenMBeanInfoSupport​(
String
className,

String
description,

OpenMBeanAttributeInfo
[] openAttributes,

OpenMBeanConstructorInfo
[] openConstructors,

OpenMBeanOperationInfo
[] openOperations,

MBeanNotificationInfo
[] notifications)
```

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

and

notifications

.

The

openAttributes

,

openConstructors

,

openOperations

and

notifications

array parameters are internally copied, so that subsequent changes
to the arrays referenced by these parameters have no effect on this
instance.

**Parameters:** className

- The fully qualified Java class name of the
open MBean described by this

OpenMBeanInfoSupport

instance.
**Parameters:** description

- A human readable description of the open
MBean described by this

OpenMBeanInfoSupport

instance.
**Parameters:** openAttributes

- The list of exposed attributes of the
described open MBean; Must be an array of instances of a
subclass of

MBeanAttributeInfo

, typically

OpenMBeanAttributeInfoSupport

.
**Parameters:** openConstructors

- The list of exposed public constructors
of the described open MBean; Must be an array of instances of a
subclass of

MBeanConstructorInfo

, typically

OpenMBeanConstructorInfoSupport

.
**Parameters:** openOperations

- The list of exposed operations of the
described open MBean. Must be an array of instances of a
subclass of

MBeanOperationInfo

, typically

OpenMBeanOperationInfoSupport

.
**Parameters:** notifications

- The list of notifications emitted by the
described open MBean.
**Throws:** ArrayStoreException

- If

openAttributes

,

openConstructors

or

openOperations

is not an array of
instances of a subclass of

MBeanAttributeInfo

,

MBeanConstructorInfo

or

MBeanOperationInfo

respectively.

- OpenMBeanInfoSupport

```java
public OpenMBeanInfoSupport​(
String
className,

String
description,

OpenMBeanAttributeInfo
[] openAttributes,

OpenMBeanConstructorInfo
[] openConstructors,

OpenMBeanOperationInfo
[] openOperations,

MBeanNotificationInfo
[] notifications,

Descriptor
descriptor)
```

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

,

notifications

, and

descriptor

.

The

openAttributes

,

openConstructors

,

openOperations

and

notifications

array parameters are
internally copied, so that subsequent changes to the arrays
referenced by these parameters have no effect on this
instance.

**Parameters:** className

- The fully qualified Java class name of the
open MBean described by this

OpenMBeanInfoSupport

instance.
**Parameters:** description

- A human readable description of the open
MBean described by this

OpenMBeanInfoSupport

instance.
**Parameters:** openAttributes

- The list of exposed attributes of the
described open MBean; Must be an array of instances of a
subclass of

MBeanAttributeInfo

, typically

OpenMBeanAttributeInfoSupport

.
**Parameters:** openConstructors

- The list of exposed public constructors
of the described open MBean; Must be an array of instances of a
subclass of

MBeanConstructorInfo

, typically

OpenMBeanConstructorInfoSupport

.
**Parameters:** openOperations

- The list of exposed operations of the
described open MBean. Must be an array of instances of a
subclass of

MBeanOperationInfo

, typically

OpenMBeanOperationInfoSupport

.
**Parameters:** notifications

- The list of notifications emitted by the
described open MBean.
**Parameters:** descriptor

- The descriptor for the MBean. This may be null
which is equivalent to an empty descriptor.
**Throws:** ArrayStoreException

- If

openAttributes

,

openConstructors

or

openOperations

is not an array of
instances of a subclass of

MBeanAttributeInfo

,

MBeanConstructorInfo

or

MBeanOperationInfo

respectively.
**Since:** 1.6

---

#### Constructor Detail

OpenMBeanInfoSupport

```java
public OpenMBeanInfoSupport​(
String
className,

String
description,

OpenMBeanAttributeInfo
[] openAttributes,

OpenMBeanConstructorInfo
[] openConstructors,

OpenMBeanOperationInfo
[] openOperations,

MBeanNotificationInfo
[] notifications)
```

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

and

notifications

.

The

openAttributes

,

openConstructors

,

openOperations

and

notifications

array parameters are internally copied, so that subsequent changes
to the arrays referenced by these parameters have no effect on this
instance.

**Parameters:** className

- The fully qualified Java class name of the
open MBean described by this

OpenMBeanInfoSupport

instance.
**Parameters:** description

- A human readable description of the open
MBean described by this

OpenMBeanInfoSupport

instance.
**Parameters:** openAttributes

- The list of exposed attributes of the
described open MBean; Must be an array of instances of a
subclass of

MBeanAttributeInfo

, typically

OpenMBeanAttributeInfoSupport

.
**Parameters:** openConstructors

- The list of exposed public constructors
of the described open MBean; Must be an array of instances of a
subclass of

MBeanConstructorInfo

, typically

OpenMBeanConstructorInfoSupport

.
**Parameters:** openOperations

- The list of exposed operations of the
described open MBean. Must be an array of instances of a
subclass of

MBeanOperationInfo

, typically

OpenMBeanOperationInfoSupport

.
**Parameters:** notifications

- The list of notifications emitted by the
described open MBean.
**Throws:** ArrayStoreException

- If

openAttributes

,

openConstructors

or

openOperations

is not an array of
instances of a subclass of

MBeanAttributeInfo

,

MBeanConstructorInfo

or

MBeanOperationInfo

respectively.

---

#### OpenMBeanInfoSupport

public OpenMBeanInfoSupport​(

String

className,

String

description,

OpenMBeanAttributeInfo

[] openAttributes,

OpenMBeanConstructorInfo

[] openConstructors,

OpenMBeanOperationInfo

[] openOperations,

MBeanNotificationInfo

[] notifications)

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

and

notifications

.

The

openAttributes

,

openConstructors

,

openOperations

and

notifications

array parameters are internally copied, so that subsequent changes
to the arrays referenced by these parameters have no effect on this
instance.

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

and

notifications

.

The

openAttributes

,

openConstructors

,

openOperations

and

notifications

array parameters are internally copied, so that subsequent changes
to the arrays referenced by these parameters have no effect on this
instance.

OpenMBeanInfoSupport

```java
public OpenMBeanInfoSupport​(
String
className,

String
description,

OpenMBeanAttributeInfo
[] openAttributes,

OpenMBeanConstructorInfo
[] openConstructors,

OpenMBeanOperationInfo
[] openOperations,

MBeanNotificationInfo
[] notifications,

Descriptor
descriptor)
```

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

,

notifications

, and

descriptor

.

The

openAttributes

,

openConstructors

,

openOperations

and

notifications

array parameters are
internally copied, so that subsequent changes to the arrays
referenced by these parameters have no effect on this
instance.

**Parameters:** className

- The fully qualified Java class name of the
open MBean described by this

OpenMBeanInfoSupport

instance.
**Parameters:** description

- A human readable description of the open
MBean described by this

OpenMBeanInfoSupport

instance.
**Parameters:** openAttributes

- The list of exposed attributes of the
described open MBean; Must be an array of instances of a
subclass of

MBeanAttributeInfo

, typically

OpenMBeanAttributeInfoSupport

.
**Parameters:** openConstructors

- The list of exposed public constructors
of the described open MBean; Must be an array of instances of a
subclass of

MBeanConstructorInfo

, typically

OpenMBeanConstructorInfoSupport

.
**Parameters:** openOperations

- The list of exposed operations of the
described open MBean. Must be an array of instances of a
subclass of

MBeanOperationInfo

, typically

OpenMBeanOperationInfoSupport

.
**Parameters:** notifications

- The list of notifications emitted by the
described open MBean.
**Parameters:** descriptor

- The descriptor for the MBean. This may be null
which is equivalent to an empty descriptor.
**Throws:** ArrayStoreException

- If

openAttributes

,

openConstructors

or

openOperations

is not an array of
instances of a subclass of

MBeanAttributeInfo

,

MBeanConstructorInfo

or

MBeanOperationInfo

respectively.
**Since:** 1.6

---

#### OpenMBeanInfoSupport

public OpenMBeanInfoSupport​(

String

className,

String

description,

OpenMBeanAttributeInfo

[] openAttributes,

OpenMBeanConstructorInfo

[] openConstructors,

OpenMBeanOperationInfo

[] openOperations,

MBeanNotificationInfo

[] notifications,

Descriptor

descriptor)

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

,

notifications

, and

descriptor

.

The

openAttributes

,

openConstructors

,

openOperations

and

notifications

array parameters are
internally copied, so that subsequent changes to the arrays
referenced by these parameters have no effect on this
instance.

Constructs an

OpenMBeanInfoSupport

instance, which
describes a class of open MBeans with the specified

className

,

description

,

openAttributes

,

openConstructors

,

openOperations

,

notifications

, and

descriptor

.

The

openAttributes

,

openConstructors

,

openOperations

and

notifications

array parameters are
internally copied, so that subsequent changes to the arrays
referenced by these parameters have no effect on this
instance.

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

OpenMBeanInfoSupport

instance for equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanInfo

interface,
- their class names are equal
- their infos on attributes, constructors, operations and
notifications are equal

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanInfo

interface.

**Specified by:** equals

in interface

OpenMBeanInfo
**Overrides:** equals

in class

MBeanInfo
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanInfoSupport

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanInfoSupport

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

OpenMBeanInfoSupport

instance.

The hash code of an

OpenMBeanInfoSupport

instance is
the sum of the hash codes of all elements of information used
in

equals

comparisons (ie: its class name, and its
infos on attributes, constructors, operations and
notifications, where the hashCode of each of these arrays is
calculated by a call to

new
java.util.HashSet(java.util.Arrays.asList(this.getSignature)).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanInfoSupport

instances

t1

and

t2

, as
required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanInfo

interface may be equal to this

OpenMBeanInfoSupport

instance as defined by

equals(java.lang.Object)

, but may have a different hash code
if it is calculated differently.

As

OpenMBeanInfoSupport

instances are immutable, the
hash code for this instance is calculated once, on the first
call to

hashCode

, and then the same value is returned
for subsequent calls.

**Specified by:** hashCode

in interface

OpenMBeanInfo
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanInfoSupport

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

OpenMBeanInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanInfoSupport

),
the MBean class name, the string representation of infos on
attributes, constructors, operations and notifications of the
described MBean and the string representation of the descriptor.

As

OpenMBeanInfoSupport

instances are immutable, the
string representation for this instance is calculated once, on
the first call to

toString

, and then the same value is
returned for subsequent calls.

**Specified by:** toString

in interface

OpenMBeanInfo
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanInfoSupport

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

OpenMBeanInfoSupport

instance for equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanInfo

interface,
- their class names are equal
- their infos on attributes, constructors, operations and
notifications are equal

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanInfo

interface.

**Specified by:** equals

in interface

OpenMBeanInfo
**Overrides:** equals

in class

MBeanInfo
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanInfoSupport

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanInfoSupport

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

OpenMBeanInfoSupport

instance for equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanInfo

interface,
- their class names are equal
- their infos on attributes, constructors, operations and
notifications are equal

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanInfo

interface.

Compares the specified

obj

parameter with this

OpenMBeanInfoSupport

instance for equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanInfo

interface,
- their class names are equal
- their infos on attributes, constructors, operations and
notifications are equal

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanInfo

interface.

obj

is non null,

obj

also implements the

OpenMBeanInfo

interface,

their class names are equal

their infos on attributes, constructors, operations and
notifications are equal

hashCode

```java
public int hashCode()
```

Returns the hash code value for this

OpenMBeanInfoSupport

instance.

The hash code of an

OpenMBeanInfoSupport

instance is
the sum of the hash codes of all elements of information used
in

equals

comparisons (ie: its class name, and its
infos on attributes, constructors, operations and
notifications, where the hashCode of each of these arrays is
calculated by a call to

new
java.util.HashSet(java.util.Arrays.asList(this.getSignature)).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanInfoSupport

instances

t1

and

t2

, as
required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanInfo

interface may be equal to this

OpenMBeanInfoSupport

instance as defined by

equals(java.lang.Object)

, but may have a different hash code
if it is calculated differently.

As

OpenMBeanInfoSupport

instances are immutable, the
hash code for this instance is calculated once, on the first
call to

hashCode

, and then the same value is returned
for subsequent calls.

**Specified by:** hashCode

in interface

OpenMBeanInfo
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanInfoSupport

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this

OpenMBeanInfoSupport

instance.

The hash code of an

OpenMBeanInfoSupport

instance is
the sum of the hash codes of all elements of information used
in

equals

comparisons (ie: its class name, and its
infos on attributes, constructors, operations and
notifications, where the hashCode of each of these arrays is
calculated by a call to

new
java.util.HashSet(java.util.Arrays.asList(this.getSignature)).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanInfoSupport

instances

t1

and

t2

, as
required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanInfo

interface may be equal to this

OpenMBeanInfoSupport

instance as defined by

equals(java.lang.Object)

, but may have a different hash code
if it is calculated differently.

As

OpenMBeanInfoSupport

instances are immutable, the
hash code for this instance is calculated once, on the first
call to

hashCode

, and then the same value is returned
for subsequent calls.

Returns the hash code value for this

OpenMBeanInfoSupport

instance.

The hash code of an

OpenMBeanInfoSupport

instance is
the sum of the hash codes of all elements of information used
in

equals

comparisons (ie: its class name, and its
infos on attributes, constructors, operations and
notifications, where the hashCode of each of these arrays is
calculated by a call to

new
java.util.HashSet(java.util.Arrays.asList(this.getSignature)).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanInfoSupport

instances

t1

and

t2

, as
required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanInfo

interface may be equal to this

OpenMBeanInfoSupport

instance as defined by

equals(java.lang.Object)

, but may have a different hash code
if it is calculated differently.

As

OpenMBeanInfoSupport

instances are immutable, the
hash code for this instance is calculated once, on the first
call to

hashCode

, and then the same value is returned
for subsequent calls.

toString

```java
public
String
toString()
```

Returns a string representation of this

OpenMBeanInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanInfoSupport

),
the MBean class name, the string representation of infos on
attributes, constructors, operations and notifications of the
described MBean and the string representation of the descriptor.

As

OpenMBeanInfoSupport

instances are immutable, the
string representation for this instance is calculated once, on
the first call to

toString

, and then the same value is
returned for subsequent calls.

**Specified by:** toString

in interface

OpenMBeanInfo
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanInfoSupport

instance

---

#### toString

public

String

toString()

Returns a string representation of this

OpenMBeanInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanInfoSupport

),
the MBean class name, the string representation of infos on
attributes, constructors, operations and notifications of the
described MBean and the string representation of the descriptor.

As

OpenMBeanInfoSupport

instances are immutable, the
string representation for this instance is calculated once, on
the first call to

toString

, and then the same value is
returned for subsequent calls.

Returns a string representation of this

OpenMBeanInfoSupport

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanInfoSupport

),
the MBean class name, the string representation of infos on
attributes, constructors, operations and notifications of the
described MBean and the string representation of the descriptor.

As

OpenMBeanInfoSupport

instances are immutable, the
string representation for this instance is calculated once, on
the first call to

toString

, and then the same value is
returned for subsequent calls.

---

