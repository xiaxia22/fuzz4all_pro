# Interface OpenMBeanInfo

**Source:** `java.management\javax\management\openmbean\OpenMBeanInfo.html`

### Class Description

```java
public interface
OpenMBeanInfo
```

Describes an Open MBean: an Open MBean is recognized as such if
its

getMBeanInfo()

method returns an instance of a class which
implements the

OpenMBeanInfo

interface, typically

OpenMBeanInfoSupport

.

This interface declares the same methods as the class

MBeanInfo

. A class implementing this interface
(typically

OpenMBeanInfoSupport

) should extend

MBeanInfo

.

The

getAttributes()

,

getOperations()

and

getConstructors()

methods of the implementing class should
return at runtime an array of instances of a subclass of

MBeanAttributeInfo

,

MBeanOperationInfo

or

MBeanConstructorInfo

respectively which implement the

OpenMBeanAttributeInfo

,

OpenMBeanOperationInfo

or

OpenMBeanConstructorInfo

interface respectively.

**All Known Implementing Classes:** OpenMBeanInfoSupport

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getClassName()

Returns the fully qualified Java class name of the open MBean
instances this

OpenMBeanInfo

describes.

**Returns:**
- the class name.

---

#### String
getDescription()

Returns a human readable description of the type of open MBean
instances this

OpenMBeanInfo

describes.

**Returns:**
- the description.

---

#### MBeanAttributeInfo
[] getAttributes()

Returns an array of

OpenMBeanAttributeInfo

instances
describing each attribute in the open MBean described by this

OpenMBeanInfo

instance. Each instance in the returned
array should actually be a subclass of

MBeanAttributeInfo

which implements the

OpenMBeanAttributeInfo

interface (typically

OpenMBeanAttributeInfoSupport

).

**Returns:**
- the attribute array.

---

#### MBeanOperationInfo
[] getOperations()

Returns an array of

OpenMBeanOperationInfo

instances
describing each operation in the open MBean described by this

OpenMBeanInfo

instance. Each instance in the returned
array should actually be a subclass of

MBeanOperationInfo

which implements the

OpenMBeanOperationInfo

interface (typically

OpenMBeanOperationInfoSupport

).

**Returns:**
- the operation array.

---

#### MBeanConstructorInfo
[] getConstructors()

Returns an array of

OpenMBeanConstructorInfo

instances
describing each constructor in the open MBean described by this

OpenMBeanInfo

instance. Each instance in the returned
array should actually be a subclass of

MBeanConstructorInfo

which implements the

OpenMBeanConstructorInfo

interface (typically

OpenMBeanConstructorInfoSupport

).

**Returns:**
- the constructor array.

---

#### MBeanNotificationInfo
[] getNotifications()

Returns an array of

MBeanNotificationInfo

instances
describing each notification emitted by the open MBean
described by this

OpenMBeanInfo

instance.

**Returns:**
- the notification array.

---

#### boolean equals​(
Object
obj)

Compares the specified

obj

parameter with this

OpenMBeanInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanInfo

interface,
- their class names are equal
- their infos on attributes, constructors, operations and notifications are equal

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

OpenMBeanInfo

interface.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to be compared for equality with this

OpenMBeanInfo

instance;

**Returns:**
- true

if the specified object is equal to this

OpenMBeanInfo

instance.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this

OpenMBeanInfo

instance.

The hash code of an

OpenMBeanInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its class name, and its infos on attributes, constructors, operations and notifications,
where the hashCode of each of these arrays is calculated by a call to

new java.util.HashSet(java.util.Arrays.asList(this.getSignature)).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanInfo

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

OpenMBeanInfo

instance

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### String
toString()

Returns a string representation of this

OpenMBeanInfo

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanInfo

), the MBean class name,
and the string representation of infos on attributes, constructors,
operations and notifications of the described MBean.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

OpenMBeanInfo

instance

---

### Additional Sections

#### Interface OpenMBeanInfo

**All Known Implementing Classes:** OpenMBeanInfoSupport

```java
public interface
OpenMBeanInfo
```

Describes an Open MBean: an Open MBean is recognized as such if
its

getMBeanInfo()

method returns an instance of a class which
implements the

OpenMBeanInfo

interface, typically

OpenMBeanInfoSupport

.

This interface declares the same methods as the class

MBeanInfo

. A class implementing this interface
(typically

OpenMBeanInfoSupport

) should extend

MBeanInfo

.

The

getAttributes()

,

getOperations()

and

getConstructors()

methods of the implementing class should
return at runtime an array of instances of a subclass of

MBeanAttributeInfo

,

MBeanOperationInfo

or

MBeanConstructorInfo

respectively which implement the

OpenMBeanAttributeInfo

,

OpenMBeanOperationInfo

or

OpenMBeanConstructorInfo

interface respectively.

**Since:** 1.5

public interface

OpenMBeanInfo

Describes an Open MBean: an Open MBean is recognized as such if
its

getMBeanInfo()

method returns an instance of a class which
implements the

OpenMBeanInfo

interface, typically

OpenMBeanInfoSupport

.

This interface declares the same methods as the class

MBeanInfo

. A class implementing this interface
(typically

OpenMBeanInfoSupport

) should extend

MBeanInfo

.

The

getAttributes()

,

getOperations()

and

getConstructors()

methods of the implementing class should
return at runtime an array of instances of a subclass of

MBeanAttributeInfo

,

MBeanOperationInfo

or

MBeanConstructorInfo

respectively which implement the

OpenMBeanAttributeInfo

,

OpenMBeanOperationInfo

or

OpenMBeanConstructorInfo

interface respectively.

Describes an Open MBean: an Open MBean is recognized as such if
its

getMBeanInfo()

method returns an instance of a class which
implements the

OpenMBeanInfo

interface, typically

OpenMBeanInfoSupport

.

This interface declares the same methods as the class

MBeanInfo

. A class implementing this interface
(typically

OpenMBeanInfoSupport

) should extend

MBeanInfo

.

The

getAttributes()

,

getOperations()

and

getConstructors()

methods of the implementing class should
return at runtime an array of instances of a subclass of

MBeanAttributeInfo

,

MBeanOperationInfo

or

MBeanConstructorInfo

respectively which implement the

OpenMBeanAttributeInfo

,

OpenMBeanOperationInfo

or

OpenMBeanConstructorInfo

interface respectively.

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

OpenMBeanInfo

instance for equality.

MBeanAttributeInfo

[]

getAttributes

()

Returns an array of

OpenMBeanAttributeInfo

instances
describing each attribute in the open MBean described by this

OpenMBeanInfo

instance.

String

getClassName

()

Returns the fully qualified Java class name of the open MBean
instances this

OpenMBeanInfo

describes.

MBeanConstructorInfo

[]

getConstructors

()

Returns an array of

OpenMBeanConstructorInfo

instances
describing each constructor in the open MBean described by this

OpenMBeanInfo

instance.

String

getDescription

()

Returns a human readable description of the type of open MBean
instances this

OpenMBeanInfo

describes.

MBeanNotificationInfo

[]

getNotifications

()

Returns an array of

MBeanNotificationInfo

instances
describing each notification emitted by the open MBean
described by this

OpenMBeanInfo

instance.

MBeanOperationInfo

[]

getOperations

()

Returns an array of

OpenMBeanOperationInfo

instances
describing each operation in the open MBean described by this

OpenMBeanInfo

instance.

int

hashCode

()

Returns the hash code value for this

OpenMBeanInfo

instance.

String

toString

()

Returns a string representation of this

OpenMBeanInfo

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

OpenMBeanInfo

instance for equality.

MBeanAttributeInfo

[]

getAttributes

()

Returns an array of

OpenMBeanAttributeInfo

instances
describing each attribute in the open MBean described by this

OpenMBeanInfo

instance.

String

getClassName

()

Returns the fully qualified Java class name of the open MBean
instances this

OpenMBeanInfo

describes.

MBeanConstructorInfo

[]

getConstructors

()

Returns an array of

OpenMBeanConstructorInfo

instances
describing each constructor in the open MBean described by this

OpenMBeanInfo

instance.

String

getDescription

()

Returns a human readable description of the type of open MBean
instances this

OpenMBeanInfo

describes.

MBeanNotificationInfo

[]

getNotifications

()

Returns an array of

MBeanNotificationInfo

instances
describing each notification emitted by the open MBean
described by this

OpenMBeanInfo

instance.

MBeanOperationInfo

[]

getOperations

()

Returns an array of

OpenMBeanOperationInfo

instances
describing each operation in the open MBean described by this

OpenMBeanInfo

instance.

int

hashCode

()

Returns the hash code value for this

OpenMBeanInfo

instance.

String

toString

()

Returns a string representation of this

OpenMBeanInfo

instance.

---

#### Method Summary

Compares the specified

obj

parameter with this

OpenMBeanInfo

instance for equality.

Returns an array of

OpenMBeanAttributeInfo

instances
describing each attribute in the open MBean described by this

OpenMBeanInfo

instance.

Returns the fully qualified Java class name of the open MBean
instances this

OpenMBeanInfo

describes.

Returns an array of

OpenMBeanConstructorInfo

instances
describing each constructor in the open MBean described by this

OpenMBeanInfo

instance.

Returns a human readable description of the type of open MBean
instances this

OpenMBeanInfo

describes.

Returns an array of

MBeanNotificationInfo

instances
describing each notification emitted by the open MBean
described by this

OpenMBeanInfo

instance.

Returns an array of

OpenMBeanOperationInfo

instances
describing each operation in the open MBean described by this

OpenMBeanInfo

instance.

Returns the hash code value for this

OpenMBeanInfo

instance.

Returns a string representation of this

OpenMBeanInfo

instance.

============ METHOD DETAIL ==========

- Method Detail

- getClassName

```java
String
getClassName()
```

Returns the fully qualified Java class name of the open MBean
instances this

OpenMBeanInfo

describes.

**Returns:** the class name.

- getDescription

```java
String
getDescription()
```

Returns a human readable description of the type of open MBean
instances this

OpenMBeanInfo

describes.

**Returns:** the description.

- getAttributes

```java
MBeanAttributeInfo
[] getAttributes()
```

Returns an array of

OpenMBeanAttributeInfo

instances
describing each attribute in the open MBean described by this

OpenMBeanInfo

instance. Each instance in the returned
array should actually be a subclass of

MBeanAttributeInfo

which implements the

OpenMBeanAttributeInfo

interface (typically

OpenMBeanAttributeInfoSupport

).

**Returns:** the attribute array.

- getOperations

```java
MBeanOperationInfo
[] getOperations()
```

Returns an array of

OpenMBeanOperationInfo

instances
describing each operation in the open MBean described by this

OpenMBeanInfo

instance. Each instance in the returned
array should actually be a subclass of

MBeanOperationInfo

which implements the

OpenMBeanOperationInfo

interface (typically

OpenMBeanOperationInfoSupport

).

**Returns:** the operation array.

- getConstructors

```java
MBeanConstructorInfo
[] getConstructors()
```

Returns an array of

OpenMBeanConstructorInfo

instances
describing each constructor in the open MBean described by this

OpenMBeanInfo

instance. Each instance in the returned
array should actually be a subclass of

MBeanConstructorInfo

which implements the

OpenMBeanConstructorInfo

interface (typically

OpenMBeanConstructorInfoSupport

).

**Returns:** the constructor array.

- getNotifications

```java
MBeanNotificationInfo
[] getNotifications()
```

Returns an array of

MBeanNotificationInfo

instances
describing each notification emitted by the open MBean
described by this

OpenMBeanInfo

instance.

**Returns:** the notification array.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanInfo

interface,
- their class names are equal
- their infos on attributes, constructors, operations and notifications are equal

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

OpenMBeanInfo

interface.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanInfo

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanInfo

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this

OpenMBeanInfo

instance.

The hash code of an

OpenMBeanInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its class name, and its infos on attributes, constructors, operations and notifications,
where the hashCode of each of these arrays is calculated by a call to

new java.util.HashSet(java.util.Arrays.asList(this.getSignature)).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanInfo

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

OpenMBeanInfo

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

OpenMBeanInfo

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanInfo

), the MBean class name,
and the string representation of infos on attributes, constructors,
operations and notifications of the described MBean.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanInfo

instance

Method Detail

- getClassName

```java
String
getClassName()
```

Returns the fully qualified Java class name of the open MBean
instances this

OpenMBeanInfo

describes.

**Returns:** the class name.

- getDescription

```java
String
getDescription()
```

Returns a human readable description of the type of open MBean
instances this

OpenMBeanInfo

describes.

**Returns:** the description.

- getAttributes

```java
MBeanAttributeInfo
[] getAttributes()
```

Returns an array of

OpenMBeanAttributeInfo

instances
describing each attribute in the open MBean described by this

OpenMBeanInfo

instance. Each instance in the returned
array should actually be a subclass of

MBeanAttributeInfo

which implements the

OpenMBeanAttributeInfo

interface (typically

OpenMBeanAttributeInfoSupport

).

**Returns:** the attribute array.

- getOperations

```java
MBeanOperationInfo
[] getOperations()
```

Returns an array of

OpenMBeanOperationInfo

instances
describing each operation in the open MBean described by this

OpenMBeanInfo

instance. Each instance in the returned
array should actually be a subclass of

MBeanOperationInfo

which implements the

OpenMBeanOperationInfo

interface (typically

OpenMBeanOperationInfoSupport

).

**Returns:** the operation array.

- getConstructors

```java
MBeanConstructorInfo
[] getConstructors()
```

Returns an array of

OpenMBeanConstructorInfo

instances
describing each constructor in the open MBean described by this

OpenMBeanInfo

instance. Each instance in the returned
array should actually be a subclass of

MBeanConstructorInfo

which implements the

OpenMBeanConstructorInfo

interface (typically

OpenMBeanConstructorInfoSupport

).

**Returns:** the constructor array.

- getNotifications

```java
MBeanNotificationInfo
[] getNotifications()
```

Returns an array of

MBeanNotificationInfo

instances
describing each notification emitted by the open MBean
described by this

OpenMBeanInfo

instance.

**Returns:** the notification array.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanInfo

interface,
- their class names are equal
- their infos on attributes, constructors, operations and notifications are equal

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

OpenMBeanInfo

interface.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanInfo

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanInfo

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this

OpenMBeanInfo

instance.

The hash code of an

OpenMBeanInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its class name, and its infos on attributes, constructors, operations and notifications,
where the hashCode of each of these arrays is calculated by a call to

new java.util.HashSet(java.util.Arrays.asList(this.getSignature)).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanInfo

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

OpenMBeanInfo

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

OpenMBeanInfo

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanInfo

), the MBean class name,
and the string representation of infos on attributes, constructors,
operations and notifications of the described MBean.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanInfo

instance

---

#### Method Detail

getClassName

```java
String
getClassName()
```

Returns the fully qualified Java class name of the open MBean
instances this

OpenMBeanInfo

describes.

**Returns:** the class name.

---

#### getClassName

String

getClassName()

Returns the fully qualified Java class name of the open MBean
instances this

OpenMBeanInfo

describes.

getDescription

```java
String
getDescription()
```

Returns a human readable description of the type of open MBean
instances this

OpenMBeanInfo

describes.

**Returns:** the description.

---

#### getDescription

String

getDescription()

Returns a human readable description of the type of open MBean
instances this

OpenMBeanInfo

describes.

getAttributes

```java
MBeanAttributeInfo
[] getAttributes()
```

Returns an array of

OpenMBeanAttributeInfo

instances
describing each attribute in the open MBean described by this

OpenMBeanInfo

instance. Each instance in the returned
array should actually be a subclass of

MBeanAttributeInfo

which implements the

OpenMBeanAttributeInfo

interface (typically

OpenMBeanAttributeInfoSupport

).

**Returns:** the attribute array.

---

#### getAttributes

MBeanAttributeInfo

[] getAttributes()

Returns an array of

OpenMBeanAttributeInfo

instances
describing each attribute in the open MBean described by this

OpenMBeanInfo

instance. Each instance in the returned
array should actually be a subclass of

MBeanAttributeInfo

which implements the

OpenMBeanAttributeInfo

interface (typically

OpenMBeanAttributeInfoSupport

).

getOperations

```java
MBeanOperationInfo
[] getOperations()
```

Returns an array of

OpenMBeanOperationInfo

instances
describing each operation in the open MBean described by this

OpenMBeanInfo

instance. Each instance in the returned
array should actually be a subclass of

MBeanOperationInfo

which implements the

OpenMBeanOperationInfo

interface (typically

OpenMBeanOperationInfoSupport

).

**Returns:** the operation array.

---

#### getOperations

MBeanOperationInfo

[] getOperations()

Returns an array of

OpenMBeanOperationInfo

instances
describing each operation in the open MBean described by this

OpenMBeanInfo

instance. Each instance in the returned
array should actually be a subclass of

MBeanOperationInfo

which implements the

OpenMBeanOperationInfo

interface (typically

OpenMBeanOperationInfoSupport

).

getConstructors

```java
MBeanConstructorInfo
[] getConstructors()
```

Returns an array of

OpenMBeanConstructorInfo

instances
describing each constructor in the open MBean described by this

OpenMBeanInfo

instance. Each instance in the returned
array should actually be a subclass of

MBeanConstructorInfo

which implements the

OpenMBeanConstructorInfo

interface (typically

OpenMBeanConstructorInfoSupport

).

**Returns:** the constructor array.

---

#### getConstructors

MBeanConstructorInfo

[] getConstructors()

Returns an array of

OpenMBeanConstructorInfo

instances
describing each constructor in the open MBean described by this

OpenMBeanInfo

instance. Each instance in the returned
array should actually be a subclass of

MBeanConstructorInfo

which implements the

OpenMBeanConstructorInfo

interface (typically

OpenMBeanConstructorInfoSupport

).

getNotifications

```java
MBeanNotificationInfo
[] getNotifications()
```

Returns an array of

MBeanNotificationInfo

instances
describing each notification emitted by the open MBean
described by this

OpenMBeanInfo

instance.

**Returns:** the notification array.

---

#### getNotifications

MBeanNotificationInfo

[] getNotifications()

Returns an array of

MBeanNotificationInfo

instances
describing each notification emitted by the open MBean
described by this

OpenMBeanInfo

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

OpenMBeanInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanInfo

interface,
- their class names are equal
- their infos on attributes, constructors, operations and notifications are equal

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

OpenMBeanInfo

interface.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanInfo

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanInfo

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

OpenMBeanInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanInfo

interface,
- their class names are equal
- their infos on attributes, constructors, operations and notifications are equal

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

OpenMBeanInfo

interface.

Returns

true

if and only if all of the following statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanInfo

interface,
- their class names are equal
- their infos on attributes, constructors, operations and notifications are equal

This ensures that this

equals

method works properly for

obj

parameters which are
different implementations of the

OpenMBeanInfo

interface.

obj

is non null,

obj

also implements the

OpenMBeanInfo

interface,

their class names are equal

their infos on attributes, constructors, operations and notifications are equal

hashCode

```java
int hashCode()
```

Returns the hash code value for this

OpenMBeanInfo

instance.

The hash code of an

OpenMBeanInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its class name, and its infos on attributes, constructors, operations and notifications,
where the hashCode of each of these arrays is calculated by a call to

new java.util.HashSet(java.util.Arrays.asList(this.getSignature)).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanInfo

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

OpenMBeanInfo

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

int hashCode()

Returns the hash code value for this

OpenMBeanInfo

instance.

The hash code of an

OpenMBeanInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its class name, and its infos on attributes, constructors, operations and notifications,
where the hashCode of each of these arrays is calculated by a call to

new java.util.HashSet(java.util.Arrays.asList(this.getSignature)).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanInfo

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

The hash code of an

OpenMBeanInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its class name, and its infos on attributes, constructors, operations and notifications,
where the hashCode of each of these arrays is calculated by a call to

new java.util.HashSet(java.util.Arrays.asList(this.getSignature)).hashCode()

).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanInfo

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

OpenMBeanInfo

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

OpenMBeanInfo

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanInfo

), the MBean class name,
and the string representation of infos on attributes, constructors,
operations and notifications of the described MBean.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanInfo

instance

---

#### toString

String

toString()

Returns a string representation of this

OpenMBeanInfo

instance.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanInfo

), the MBean class name,
and the string representation of infos on attributes, constructors,
operations and notifications of the described MBean.

The string representation consists of the name of this class
(ie

javax.management.openmbean.OpenMBeanInfo

), the MBean class name,
and the string representation of infos on attributes, constructors,
operations and notifications of the described MBean.

---

