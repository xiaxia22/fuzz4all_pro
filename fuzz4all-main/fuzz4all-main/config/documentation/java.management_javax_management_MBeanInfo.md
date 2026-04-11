# Class MBeanInfo

**Source:** `java.management\javax\management\MBeanInfo.html`

### Class Description

```java
public class
MBeanInfo

extends
Object

implements
Cloneable
,
Serializable
,
DescriptorRead
```

Describes the management interface exposed by an MBean; that is,
the set of attributes and operations which are available for
management operations. Instances of this class are immutable.
Subclasses may be mutable but this is not recommended.

Usually the

MBeanInfo

for any given MBean does
not change over the lifetime of that MBean. Dynamic MBeans can change their

MBeanInfo

and in that case it is recommended that they emit a

Notification

with a

type

of

"jmx.mbean.info.changed"

and a

userData

that is the new

MBeanInfo

. This is not required, but
provides a conventional way for clients of the MBean to discover the change.
See also the

immutableInfo

and

infoTimeout

fields in the

MBeanInfo

Descriptor

.

The contents of the

MBeanInfo

for a Dynamic MBean
are determined by its

getMBeanInfo()

method. This includes Open MBeans and Model
MBeans, which are kinds of Dynamic MBeans.

The contents of the

MBeanInfo

for a Standard MBean
are determined by the MBean server as follows:

- getClassName()

returns the Java class name of the MBean
object;

getConstructors()

returns the list of all public
constructors in that object;

getAttributes()

returns the list of all attributes
whose existence is deduced from the presence in the MBean interface
of a

get

Name

,

is

Name

, or

set

Name

method that conforms to the conventions
for Standard MBeans;

getOperations()

returns the list of all methods in
the MBean interface that do not represent attributes;

getNotifications()

returns an empty array if the MBean
does not implement the

NotificationBroadcaster

interface,
otherwise the result of calling

NotificationBroadcaster.getNotificationInfo()

on it;

getDescriptor()

returns a descriptor containing the contents
of any descriptor annotations in the MBean interface (see

@DescriptorKey

).

The description returned by

getDescription()

and the
descriptions of the contained attributes and operations are not specified.

The remaining details of the

MBeanInfo

for a
Standard MBean are not specified. This includes the description of
any contained constructors, and notifications; the names
of parameters to constructors and operations; and the descriptions of
constructor parameters.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

---

### Field Details

*No entries found.*

### Constructor Details

#### public MBeanInfo​(
String
className,

String
description,

MBeanAttributeInfo
[] attributes,

MBeanConstructorInfo
[] constructors,

MBeanOperationInfo
[] operations,

MBeanNotificationInfo
[] notifications)
throws
IllegalArgumentException

Constructs an

MBeanInfo

.

**Parameters:**
- className

- The name of the Java class of the MBean described
by this

MBeanInfo

. This value may be any
syntactically legal Java class name. It does not have to be a
Java class known to the MBean server or to the MBean's
ClassLoader. If it is a Java class known to the MBean's
ClassLoader, it is recommended but not required that the
class's public methods include those that would appear in a
Standard MBean implementing the attributes and operations in
this MBeanInfo.
- description

- A human readable description of the MBean (optional).
- attributes

- The list of exposed attributes of the MBean.
This may be null with the same effect as a zero-length array.
- constructors

- The list of public constructors of the
MBean. This may be null with the same effect as a zero-length
array.
- operations

- The list of operations of the MBean. This
may be null with the same effect as a zero-length array.
- notifications

- The list of notifications emitted. This
may be null with the same effect as a zero-length array.

**Throws:**
- IllegalArgumentException

---

#### public MBeanInfo​(
String
className,

String
description,

MBeanAttributeInfo
[] attributes,

MBeanConstructorInfo
[] constructors,

MBeanOperationInfo
[] operations,

MBeanNotificationInfo
[] notifications,

Descriptor
descriptor)
throws
IllegalArgumentException

Constructs an

MBeanInfo

.

**Parameters:**
- className

- The name of the Java class of the MBean described
by this

MBeanInfo

. This value may be any
syntactically legal Java class name. It does not have to be a
Java class known to the MBean server or to the MBean's
ClassLoader. If it is a Java class known to the MBean's
ClassLoader, it is recommended but not required that the
class's public methods include those that would appear in a
Standard MBean implementing the attributes and operations in
this MBeanInfo.
- description

- A human readable description of the MBean (optional).
- attributes

- The list of exposed attributes of the MBean.
This may be null with the same effect as a zero-length array.
- constructors

- The list of public constructors of the
MBean. This may be null with the same effect as a zero-length
array.
- operations

- The list of operations of the MBean. This
may be null with the same effect as a zero-length array.
- notifications

- The list of notifications emitted. This
may be null with the same effect as a zero-length array.
- descriptor

- The descriptor for the MBean. This may be null
which is equivalent to an empty descriptor.

**Throws:**
- IllegalArgumentException

**Since:**
- 1.6

---

### Method Details

#### public
Object
clone()

Returns a shallow clone of this instance.
The clone is obtained by simply calling

super.clone()

,
thus calling the default native shallow cloning mechanism
implemented by

Object.clone()

.
No deeper cloning of any internal field is made.

Since this class is immutable, the clone method is chiefly of
interest to subclasses.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**See Also:**
- Cloneable

---

#### public
String
getClassName()

Returns the name of the Java class of the MBean described by
this

MBeanInfo

.

**Returns:**
- the class name.

---

#### public
String
getDescription()

Returns a human readable description of the MBean.

**Returns:**
- the description.

---

#### public
MBeanAttributeInfo
[] getAttributes()

Returns the list of attributes exposed for management.
Each attribute is described by an

MBeanAttributeInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanAttributeInfo

objects
but that each referenced

MBeanAttributeInfo

object is not copied.

**Returns:**
- An array of

MBeanAttributeInfo

objects.

---

#### public
MBeanOperationInfo
[] getOperations()

Returns the list of operations of the MBean.
Each operation is described by an

MBeanOperationInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanOperationInfo

objects
but that each referenced

MBeanOperationInfo

object is not copied.

**Returns:**
- An array of

MBeanOperationInfo

objects.

---

#### public
MBeanConstructorInfo
[] getConstructors()

Returns the list of the public constructors of the MBean.
Each constructor is described by an

MBeanConstructorInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanConstructorInfo

objects but
that each referenced

MBeanConstructorInfo

object
is not copied.

The returned list is not necessarily exhaustive. That is,
the MBean may have a public constructor that is not in the
list. In this case, the MBean server can construct another
instance of this MBean's class using that constructor, even
though it is not listed here.

**Returns:**
- An array of

MBeanConstructorInfo

objects.

---

#### public
MBeanNotificationInfo
[] getNotifications()

Returns the list of the notifications emitted by the MBean.
Each notification is described by an

MBeanNotificationInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanNotificationInfo

objects
but that each referenced

MBeanNotificationInfo

object is not copied.

**Returns:**
- An array of

MBeanNotificationInfo

objects.

---

#### public
Descriptor
getDescriptor()

Get the descriptor of this MBeanInfo. Changing the returned value
will have no affect on the original descriptor.

**Specified by:**
- getDescriptor

in interface

DescriptorRead

**Returns:**
- a descriptor that is either immutable or a copy of the original.

**Since:**
- 1.6

---

#### public boolean equals​(
Object
o)

Compare this MBeanInfo to another. Two MBeanInfo objects
are equal if and only if they return equal values for

getClassName()

, for

getDescription()

, and for

getDescriptor()

, and the
arrays returned by the two objects for

getAttributes()

,

getOperations()

,

getConstructors()

, and

getNotifications()

are
pairwise equal. Here "equal" means

Object.equals(Object)

, not identity.

If two MBeanInfo objects return the same values in one of
their arrays but in a different order then they are not equal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- the object to compare to.

**Returns:**
- true if and only if

o

is an MBeanInfo that is equal
to this one according to the rules above.

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class MBeanInfo

java.lang.Object

- javax.management.MBeanInfo

javax.management.MBeanInfo

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

**Direct Known Subclasses:** ModelMBeanInfoSupport

,

OpenMBeanInfoSupport

```java
public class
MBeanInfo

extends
Object

implements
Cloneable
,
Serializable
,
DescriptorRead
```

Describes the management interface exposed by an MBean; that is,
the set of attributes and operations which are available for
management operations. Instances of this class are immutable.
Subclasses may be mutable but this is not recommended.

Usually the

MBeanInfo

for any given MBean does
not change over the lifetime of that MBean. Dynamic MBeans can change their

MBeanInfo

and in that case it is recommended that they emit a

Notification

with a

type

of

"jmx.mbean.info.changed"

and a

userData

that is the new

MBeanInfo

. This is not required, but
provides a conventional way for clients of the MBean to discover the change.
See also the

immutableInfo

and

infoTimeout

fields in the

MBeanInfo

Descriptor

.

The contents of the

MBeanInfo

for a Dynamic MBean
are determined by its

getMBeanInfo()

method. This includes Open MBeans and Model
MBeans, which are kinds of Dynamic MBeans.

The contents of the

MBeanInfo

for a Standard MBean
are determined by the MBean server as follows:

- getClassName()

returns the Java class name of the MBean
object;

getConstructors()

returns the list of all public
constructors in that object;

getAttributes()

returns the list of all attributes
whose existence is deduced from the presence in the MBean interface
of a

get

Name

,

is

Name

, or

set

Name

method that conforms to the conventions
for Standard MBeans;

getOperations()

returns the list of all methods in
the MBean interface that do not represent attributes;

getNotifications()

returns an empty array if the MBean
does not implement the

NotificationBroadcaster

interface,
otherwise the result of calling

NotificationBroadcaster.getNotificationInfo()

on it;

getDescriptor()

returns a descriptor containing the contents
of any descriptor annotations in the MBean interface (see

@DescriptorKey

).

The description returned by

getDescription()

and the
descriptions of the contained attributes and operations are not specified.

The remaining details of the

MBeanInfo

for a
Standard MBean are not specified. This includes the description of
any contained constructors, and notifications; the names
of parameters to constructors and operations; and the descriptions of
constructor parameters.

**Since:** 1.5
**See Also:** Serialized Form

public class

MBeanInfo

extends

Object

implements

Cloneable

,

Serializable

,

DescriptorRead

Describes the management interface exposed by an MBean; that is,
the set of attributes and operations which are available for
management operations. Instances of this class are immutable.
Subclasses may be mutable but this is not recommended.

Usually the

MBeanInfo

for any given MBean does
not change over the lifetime of that MBean. Dynamic MBeans can change their

MBeanInfo

and in that case it is recommended that they emit a

Notification

with a

type

of

"jmx.mbean.info.changed"

and a

userData

that is the new

MBeanInfo

. This is not required, but
provides a conventional way for clients of the MBean to discover the change.
See also the

immutableInfo

and

infoTimeout

fields in the

MBeanInfo

Descriptor

.

The contents of the

MBeanInfo

for a Dynamic MBean
are determined by its

getMBeanInfo()

method. This includes Open MBeans and Model
MBeans, which are kinds of Dynamic MBeans.

The contents of the

MBeanInfo

for a Standard MBean
are determined by the MBean server as follows:

- getClassName()

returns the Java class name of the MBean
object;

getConstructors()

returns the list of all public
constructors in that object;

getAttributes()

returns the list of all attributes
whose existence is deduced from the presence in the MBean interface
of a

get

Name

,

is

Name

, or

set

Name

method that conforms to the conventions
for Standard MBeans;

getOperations()

returns the list of all methods in
the MBean interface that do not represent attributes;

getNotifications()

returns an empty array if the MBean
does not implement the

NotificationBroadcaster

interface,
otherwise the result of calling

NotificationBroadcaster.getNotificationInfo()

on it;

getDescriptor()

returns a descriptor containing the contents
of any descriptor annotations in the MBean interface (see

@DescriptorKey

).

The description returned by

getDescription()

and the
descriptions of the contained attributes and operations are not specified.

The remaining details of the

MBeanInfo

for a
Standard MBean are not specified. This includes the description of
any contained constructors, and notifications; the names
of parameters to constructors and operations; and the descriptions of
constructor parameters.

Describes the management interface exposed by an MBean; that is,
the set of attributes and operations which are available for
management operations. Instances of this class are immutable.
Subclasses may be mutable but this is not recommended.

Usually the

MBeanInfo

for any given MBean does
not change over the lifetime of that MBean. Dynamic MBeans can change their

MBeanInfo

and in that case it is recommended that they emit a

Notification

with a

type

of

"jmx.mbean.info.changed"

and a

userData

that is the new

MBeanInfo

. This is not required, but
provides a conventional way for clients of the MBean to discover the change.
See also the

immutableInfo

and

infoTimeout

fields in the

MBeanInfo

Descriptor

.

The contents of the

MBeanInfo

for a Dynamic MBean
are determined by its

getMBeanInfo()

method. This includes Open MBeans and Model
MBeans, which are kinds of Dynamic MBeans.

The contents of the

MBeanInfo

for a Standard MBean
are determined by the MBean server as follows:

getClassName()

returns the Java class name of the MBean
object;

getConstructors()

returns the list of all public
constructors in that object;

getAttributes()

returns the list of all attributes
whose existence is deduced from the presence in the MBean interface
of a

get

Name

,

is

Name

, or

set

Name

method that conforms to the conventions
for Standard MBeans;

getOperations()

returns the list of all methods in
the MBean interface that do not represent attributes;

getNotifications()

returns an empty array if the MBean
does not implement the

NotificationBroadcaster

interface,
otherwise the result of calling

NotificationBroadcaster.getNotificationInfo()

on it;

getDescriptor()

returns a descriptor containing the contents
of any descriptor annotations in the MBean interface (see

@DescriptorKey

).

The description returned by

getDescription()

and the
descriptions of the contained attributes and operations are not specified.

The remaining details of the

MBeanInfo

for a
Standard MBean are not specified. This includes the description of
any contained constructors, and notifications; the names
of parameters to constructors and operations; and the descriptions of
constructor parameters.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MBeanInfo

​(

String

className,

String

description,

MBeanAttributeInfo

[] attributes,

MBeanConstructorInfo

[] constructors,

MBeanOperationInfo

[] operations,

MBeanNotificationInfo

[] notifications)

Constructs an

MBeanInfo

.

MBeanInfo

​(

String

className,

String

description,

MBeanAttributeInfo

[] attributes,

MBeanConstructorInfo

[] constructors,

MBeanOperationInfo

[] operations,

MBeanNotificationInfo

[] notifications,

Descriptor

descriptor)

Constructs an

MBeanInfo

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a shallow clone of this instance.

boolean

equals

​(

Object

o)

Compare this MBeanInfo to another.

MBeanAttributeInfo

[]

getAttributes

()

Returns the list of attributes exposed for management.

String

getClassName

()

Returns the name of the Java class of the MBean described by
this

MBeanInfo

.

MBeanConstructorInfo

[]

getConstructors

()

Returns the list of the public constructors of the MBean.

String

getDescription

()

Returns a human readable description of the MBean.

Descriptor

getDescriptor

()

Get the descriptor of this MBeanInfo.

MBeanNotificationInfo

[]

getNotifications

()

Returns the list of the notifications emitted by the MBean.

MBeanOperationInfo

[]

getOperations

()

Returns the list of operations of the MBean.

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

hashCode

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

Constructor Summary

Constructors

Constructor

Description

MBeanInfo

​(

String

className,

String

description,

MBeanAttributeInfo

[] attributes,

MBeanConstructorInfo

[] constructors,

MBeanOperationInfo

[] operations,

MBeanNotificationInfo

[] notifications)

Constructs an

MBeanInfo

.

MBeanInfo

​(

String

className,

String

description,

MBeanAttributeInfo

[] attributes,

MBeanConstructorInfo

[] constructors,

MBeanOperationInfo

[] operations,

MBeanNotificationInfo

[] notifications,

Descriptor

descriptor)

Constructs an

MBeanInfo

.

---

#### Constructor Summary

Constructs an

MBeanInfo

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a shallow clone of this instance.

boolean

equals

​(

Object

o)

Compare this MBeanInfo to another.

MBeanAttributeInfo

[]

getAttributes

()

Returns the list of attributes exposed for management.

String

getClassName

()

Returns the name of the Java class of the MBean described by
this

MBeanInfo

.

MBeanConstructorInfo

[]

getConstructors

()

Returns the list of the public constructors of the MBean.

String

getDescription

()

Returns a human readable description of the MBean.

Descriptor

getDescriptor

()

Get the descriptor of this MBeanInfo.

MBeanNotificationInfo

[]

getNotifications

()

Returns the list of the notifications emitted by the MBean.

MBeanOperationInfo

[]

getOperations

()

Returns the list of operations of the MBean.

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

hashCode

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

#### Method Summary

Returns a shallow clone of this instance.

Compare this MBeanInfo to another.

Returns the list of attributes exposed for management.

Returns the name of the Java class of the MBean described by
this

MBeanInfo

.

Returns the list of the public constructors of the MBean.

Returns a human readable description of the MBean.

Get the descriptor of this MBeanInfo.

Returns the list of the notifications emitted by the MBean.

Returns the list of operations of the MBean.

Methods declared in class java.lang.

Object

finalize

,

getClass

,

hashCode

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MBeanInfo

```java
public MBeanInfo​(
String
className,

String
description,

MBeanAttributeInfo
[] attributes,

MBeanConstructorInfo
[] constructors,

MBeanOperationInfo
[] operations,

MBeanNotificationInfo
[] notifications)
throws
IllegalArgumentException
```

Constructs an

MBeanInfo

.

**Parameters:** className

- The name of the Java class of the MBean described
by this

MBeanInfo

. This value may be any
syntactically legal Java class name. It does not have to be a
Java class known to the MBean server or to the MBean's
ClassLoader. If it is a Java class known to the MBean's
ClassLoader, it is recommended but not required that the
class's public methods include those that would appear in a
Standard MBean implementing the attributes and operations in
this MBeanInfo.
**Parameters:** description

- A human readable description of the MBean (optional).
**Parameters:** attributes

- The list of exposed attributes of the MBean.
This may be null with the same effect as a zero-length array.
**Parameters:** constructors

- The list of public constructors of the
MBean. This may be null with the same effect as a zero-length
array.
**Parameters:** operations

- The list of operations of the MBean. This
may be null with the same effect as a zero-length array.
**Parameters:** notifications

- The list of notifications emitted. This
may be null with the same effect as a zero-length array.
**Throws:** IllegalArgumentException

- MBeanInfo

```java
public MBeanInfo​(
String
className,

String
description,

MBeanAttributeInfo
[] attributes,

MBeanConstructorInfo
[] constructors,

MBeanOperationInfo
[] operations,

MBeanNotificationInfo
[] notifications,

Descriptor
descriptor)
throws
IllegalArgumentException
```

Constructs an

MBeanInfo

.

**Parameters:** className

- The name of the Java class of the MBean described
by this

MBeanInfo

. This value may be any
syntactically legal Java class name. It does not have to be a
Java class known to the MBean server or to the MBean's
ClassLoader. If it is a Java class known to the MBean's
ClassLoader, it is recommended but not required that the
class's public methods include those that would appear in a
Standard MBean implementing the attributes and operations in
this MBeanInfo.
**Parameters:** description

- A human readable description of the MBean (optional).
**Parameters:** attributes

- The list of exposed attributes of the MBean.
This may be null with the same effect as a zero-length array.
**Parameters:** constructors

- The list of public constructors of the
MBean. This may be null with the same effect as a zero-length
array.
**Parameters:** operations

- The list of operations of the MBean. This
may be null with the same effect as a zero-length array.
**Parameters:** notifications

- The list of notifications emitted. This
may be null with the same effect as a zero-length array.
**Parameters:** descriptor

- The descriptor for the MBean. This may be null
which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException
**Since:** 1.6

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
public
Object
clone()
```

Returns a shallow clone of this instance.
The clone is obtained by simply calling

super.clone()

,
thus calling the default native shallow cloning mechanism
implemented by

Object.clone()

.
No deeper cloning of any internal field is made.

Since this class is immutable, the clone method is chiefly of
interest to subclasses.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

- getClassName

```java
public
String
getClassName()
```

Returns the name of the Java class of the MBean described by
this

MBeanInfo

.

**Returns:** the class name.

- getDescription

```java
public
String
getDescription()
```

Returns a human readable description of the MBean.

**Returns:** the description.

- getAttributes

```java
public
MBeanAttributeInfo
[] getAttributes()
```

Returns the list of attributes exposed for management.
Each attribute is described by an

MBeanAttributeInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanAttributeInfo

objects
but that each referenced

MBeanAttributeInfo

object is not copied.

**Returns:** An array of

MBeanAttributeInfo

objects.

- getOperations

```java
public
MBeanOperationInfo
[] getOperations()
```

Returns the list of operations of the MBean.
Each operation is described by an

MBeanOperationInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanOperationInfo

objects
but that each referenced

MBeanOperationInfo

object is not copied.

**Returns:** An array of

MBeanOperationInfo

objects.

- getConstructors

```java
public
MBeanConstructorInfo
[] getConstructors()
```

Returns the list of the public constructors of the MBean.
Each constructor is described by an

MBeanConstructorInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanConstructorInfo

objects but
that each referenced

MBeanConstructorInfo

object
is not copied.

The returned list is not necessarily exhaustive. That is,
the MBean may have a public constructor that is not in the
list. In this case, the MBean server can construct another
instance of this MBean's class using that constructor, even
though it is not listed here.

**Returns:** An array of

MBeanConstructorInfo

objects.

- getNotifications

```java
public
MBeanNotificationInfo
[] getNotifications()
```

Returns the list of the notifications emitted by the MBean.
Each notification is described by an

MBeanNotificationInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanNotificationInfo

objects
but that each referenced

MBeanNotificationInfo

object is not copied.

**Returns:** An array of

MBeanNotificationInfo

objects.

- getDescriptor

```java
public
Descriptor
getDescriptor()
```

Get the descriptor of this MBeanInfo. Changing the returned value
will have no affect on the original descriptor.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Returns:** a descriptor that is either immutable or a copy of the original.
**Since:** 1.6

- equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanInfo to another. Two MBeanInfo objects
are equal if and only if they return equal values for

getClassName()

, for

getDescription()

, and for

getDescriptor()

, and the
arrays returned by the two objects for

getAttributes()

,

getOperations()

,

getConstructors()

, and

getNotifications()

are
pairwise equal. Here "equal" means

Object.equals(Object)

, not identity.

If two MBeanInfo objects return the same values in one of
their arrays but in a different order then they are not equal.

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanInfo that is equal
to this one according to the rules above.
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- MBeanInfo

```java
public MBeanInfo​(
String
className,

String
description,

MBeanAttributeInfo
[] attributes,

MBeanConstructorInfo
[] constructors,

MBeanOperationInfo
[] operations,

MBeanNotificationInfo
[] notifications)
throws
IllegalArgumentException
```

Constructs an

MBeanInfo

.

**Parameters:** className

- The name of the Java class of the MBean described
by this

MBeanInfo

. This value may be any
syntactically legal Java class name. It does not have to be a
Java class known to the MBean server or to the MBean's
ClassLoader. If it is a Java class known to the MBean's
ClassLoader, it is recommended but not required that the
class's public methods include those that would appear in a
Standard MBean implementing the attributes and operations in
this MBeanInfo.
**Parameters:** description

- A human readable description of the MBean (optional).
**Parameters:** attributes

- The list of exposed attributes of the MBean.
This may be null with the same effect as a zero-length array.
**Parameters:** constructors

- The list of public constructors of the
MBean. This may be null with the same effect as a zero-length
array.
**Parameters:** operations

- The list of operations of the MBean. This
may be null with the same effect as a zero-length array.
**Parameters:** notifications

- The list of notifications emitted. This
may be null with the same effect as a zero-length array.
**Throws:** IllegalArgumentException

- MBeanInfo

```java
public MBeanInfo​(
String
className,

String
description,

MBeanAttributeInfo
[] attributes,

MBeanConstructorInfo
[] constructors,

MBeanOperationInfo
[] operations,

MBeanNotificationInfo
[] notifications,

Descriptor
descriptor)
throws
IllegalArgumentException
```

Constructs an

MBeanInfo

.

**Parameters:** className

- The name of the Java class of the MBean described
by this

MBeanInfo

. This value may be any
syntactically legal Java class name. It does not have to be a
Java class known to the MBean server or to the MBean's
ClassLoader. If it is a Java class known to the MBean's
ClassLoader, it is recommended but not required that the
class's public methods include those that would appear in a
Standard MBean implementing the attributes and operations in
this MBeanInfo.
**Parameters:** description

- A human readable description of the MBean (optional).
**Parameters:** attributes

- The list of exposed attributes of the MBean.
This may be null with the same effect as a zero-length array.
**Parameters:** constructors

- The list of public constructors of the
MBean. This may be null with the same effect as a zero-length
array.
**Parameters:** operations

- The list of operations of the MBean. This
may be null with the same effect as a zero-length array.
**Parameters:** notifications

- The list of notifications emitted. This
may be null with the same effect as a zero-length array.
**Parameters:** descriptor

- The descriptor for the MBean. This may be null
which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException
**Since:** 1.6

---

#### Constructor Detail

MBeanInfo

```java
public MBeanInfo​(
String
className,

String
description,

MBeanAttributeInfo
[] attributes,

MBeanConstructorInfo
[] constructors,

MBeanOperationInfo
[] operations,

MBeanNotificationInfo
[] notifications)
throws
IllegalArgumentException
```

Constructs an

MBeanInfo

.

**Parameters:** className

- The name of the Java class of the MBean described
by this

MBeanInfo

. This value may be any
syntactically legal Java class name. It does not have to be a
Java class known to the MBean server or to the MBean's
ClassLoader. If it is a Java class known to the MBean's
ClassLoader, it is recommended but not required that the
class's public methods include those that would appear in a
Standard MBean implementing the attributes and operations in
this MBeanInfo.
**Parameters:** description

- A human readable description of the MBean (optional).
**Parameters:** attributes

- The list of exposed attributes of the MBean.
This may be null with the same effect as a zero-length array.
**Parameters:** constructors

- The list of public constructors of the
MBean. This may be null with the same effect as a zero-length
array.
**Parameters:** operations

- The list of operations of the MBean. This
may be null with the same effect as a zero-length array.
**Parameters:** notifications

- The list of notifications emitted. This
may be null with the same effect as a zero-length array.
**Throws:** IllegalArgumentException

---

#### MBeanInfo

public MBeanInfo​(

String

className,

String

description,

MBeanAttributeInfo

[] attributes,

MBeanConstructorInfo

[] constructors,

MBeanOperationInfo

[] operations,

MBeanNotificationInfo

[] notifications)
throws

IllegalArgumentException

Constructs an

MBeanInfo

.

MBeanInfo

```java
public MBeanInfo​(
String
className,

String
description,

MBeanAttributeInfo
[] attributes,

MBeanConstructorInfo
[] constructors,

MBeanOperationInfo
[] operations,

MBeanNotificationInfo
[] notifications,

Descriptor
descriptor)
throws
IllegalArgumentException
```

Constructs an

MBeanInfo

.

**Parameters:** className

- The name of the Java class of the MBean described
by this

MBeanInfo

. This value may be any
syntactically legal Java class name. It does not have to be a
Java class known to the MBean server or to the MBean's
ClassLoader. If it is a Java class known to the MBean's
ClassLoader, it is recommended but not required that the
class's public methods include those that would appear in a
Standard MBean implementing the attributes and operations in
this MBeanInfo.
**Parameters:** description

- A human readable description of the MBean (optional).
**Parameters:** attributes

- The list of exposed attributes of the MBean.
This may be null with the same effect as a zero-length array.
**Parameters:** constructors

- The list of public constructors of the
MBean. This may be null with the same effect as a zero-length
array.
**Parameters:** operations

- The list of operations of the MBean. This
may be null with the same effect as a zero-length array.
**Parameters:** notifications

- The list of notifications emitted. This
may be null with the same effect as a zero-length array.
**Parameters:** descriptor

- The descriptor for the MBean. This may be null
which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException
**Since:** 1.6

---

#### MBeanInfo

public MBeanInfo​(

String

className,

String

description,

MBeanAttributeInfo

[] attributes,

MBeanConstructorInfo

[] constructors,

MBeanOperationInfo

[] operations,

MBeanNotificationInfo

[] notifications,

Descriptor

descriptor)
throws

IllegalArgumentException

Constructs an

MBeanInfo

.

Method Detail

- clone

```java
public
Object
clone()
```

Returns a shallow clone of this instance.
The clone is obtained by simply calling

super.clone()

,
thus calling the default native shallow cloning mechanism
implemented by

Object.clone()

.
No deeper cloning of any internal field is made.

Since this class is immutable, the clone method is chiefly of
interest to subclasses.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

- getClassName

```java
public
String
getClassName()
```

Returns the name of the Java class of the MBean described by
this

MBeanInfo

.

**Returns:** the class name.

- getDescription

```java
public
String
getDescription()
```

Returns a human readable description of the MBean.

**Returns:** the description.

- getAttributes

```java
public
MBeanAttributeInfo
[] getAttributes()
```

Returns the list of attributes exposed for management.
Each attribute is described by an

MBeanAttributeInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanAttributeInfo

objects
but that each referenced

MBeanAttributeInfo

object is not copied.

**Returns:** An array of

MBeanAttributeInfo

objects.

- getOperations

```java
public
MBeanOperationInfo
[] getOperations()
```

Returns the list of operations of the MBean.
Each operation is described by an

MBeanOperationInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanOperationInfo

objects
but that each referenced

MBeanOperationInfo

object is not copied.

**Returns:** An array of

MBeanOperationInfo

objects.

- getConstructors

```java
public
MBeanConstructorInfo
[] getConstructors()
```

Returns the list of the public constructors of the MBean.
Each constructor is described by an

MBeanConstructorInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanConstructorInfo

objects but
that each referenced

MBeanConstructorInfo

object
is not copied.

The returned list is not necessarily exhaustive. That is,
the MBean may have a public constructor that is not in the
list. In this case, the MBean server can construct another
instance of this MBean's class using that constructor, even
though it is not listed here.

**Returns:** An array of

MBeanConstructorInfo

objects.

- getNotifications

```java
public
MBeanNotificationInfo
[] getNotifications()
```

Returns the list of the notifications emitted by the MBean.
Each notification is described by an

MBeanNotificationInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanNotificationInfo

objects
but that each referenced

MBeanNotificationInfo

object is not copied.

**Returns:** An array of

MBeanNotificationInfo

objects.

- getDescriptor

```java
public
Descriptor
getDescriptor()
```

Get the descriptor of this MBeanInfo. Changing the returned value
will have no affect on the original descriptor.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Returns:** a descriptor that is either immutable or a copy of the original.
**Since:** 1.6

- equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanInfo to another. Two MBeanInfo objects
are equal if and only if they return equal values for

getClassName()

, for

getDescription()

, and for

getDescriptor()

, and the
arrays returned by the two objects for

getAttributes()

,

getOperations()

,

getConstructors()

, and

getNotifications()

are
pairwise equal. Here "equal" means

Object.equals(Object)

, not identity.

If two MBeanInfo objects return the same values in one of
their arrays but in a different order then they are not equal.

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanInfo that is equal
to this one according to the rules above.
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

clone

```java
public
Object
clone()
```

Returns a shallow clone of this instance.
The clone is obtained by simply calling

super.clone()

,
thus calling the default native shallow cloning mechanism
implemented by

Object.clone()

.
No deeper cloning of any internal field is made.

Since this class is immutable, the clone method is chiefly of
interest to subclasses.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a shallow clone of this instance.
The clone is obtained by simply calling

super.clone()

,
thus calling the default native shallow cloning mechanism
implemented by

Object.clone()

.
No deeper cloning of any internal field is made.

Since this class is immutable, the clone method is chiefly of
interest to subclasses.

Returns a shallow clone of this instance.
The clone is obtained by simply calling

super.clone()

,
thus calling the default native shallow cloning mechanism
implemented by

Object.clone()

.
No deeper cloning of any internal field is made.

Since this class is immutable, the clone method is chiefly of
interest to subclasses.

getClassName

```java
public
String
getClassName()
```

Returns the name of the Java class of the MBean described by
this

MBeanInfo

.

**Returns:** the class name.

---

#### getClassName

public

String

getClassName()

Returns the name of the Java class of the MBean described by
this

MBeanInfo

.

getDescription

```java
public
String
getDescription()
```

Returns a human readable description of the MBean.

**Returns:** the description.

---

#### getDescription

public

String

getDescription()

Returns a human readable description of the MBean.

getAttributes

```java
public
MBeanAttributeInfo
[] getAttributes()
```

Returns the list of attributes exposed for management.
Each attribute is described by an

MBeanAttributeInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanAttributeInfo

objects
but that each referenced

MBeanAttributeInfo

object is not copied.

**Returns:** An array of

MBeanAttributeInfo

objects.

---

#### getAttributes

public

MBeanAttributeInfo

[] getAttributes()

Returns the list of attributes exposed for management.
Each attribute is described by an

MBeanAttributeInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanAttributeInfo

objects
but that each referenced

MBeanAttributeInfo

object is not copied.

getOperations

```java
public
MBeanOperationInfo
[] getOperations()
```

Returns the list of operations of the MBean.
Each operation is described by an

MBeanOperationInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanOperationInfo

objects
but that each referenced

MBeanOperationInfo

object is not copied.

**Returns:** An array of

MBeanOperationInfo

objects.

---

#### getOperations

public

MBeanOperationInfo

[] getOperations()

Returns the list of operations of the MBean.
Each operation is described by an

MBeanOperationInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanOperationInfo

objects
but that each referenced

MBeanOperationInfo

object is not copied.

getConstructors

```java
public
MBeanConstructorInfo
[] getConstructors()
```

Returns the list of the public constructors of the MBean.
Each constructor is described by an

MBeanConstructorInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanConstructorInfo

objects but
that each referenced

MBeanConstructorInfo

object
is not copied.

The returned list is not necessarily exhaustive. That is,
the MBean may have a public constructor that is not in the
list. In this case, the MBean server can construct another
instance of this MBean's class using that constructor, even
though it is not listed here.

**Returns:** An array of

MBeanConstructorInfo

objects.

---

#### getConstructors

public

MBeanConstructorInfo

[] getConstructors()

Returns the list of the public constructors of the MBean.
Each constructor is described by an

MBeanConstructorInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanConstructorInfo

objects but
that each referenced

MBeanConstructorInfo

object
is not copied.

The returned list is not necessarily exhaustive. That is,
the MBean may have a public constructor that is not in the
list. In this case, the MBean server can construct another
instance of this MBean's class using that constructor, even
though it is not listed here.

Returns the list of the public constructors of the MBean.
Each constructor is described by an

MBeanConstructorInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanConstructorInfo

objects but
that each referenced

MBeanConstructorInfo

object
is not copied.

The returned list is not necessarily exhaustive. That is,
the MBean may have a public constructor that is not in the
list. In this case, the MBean server can construct another
instance of this MBean's class using that constructor, even
though it is not listed here.

getNotifications

```java
public
MBeanNotificationInfo
[] getNotifications()
```

Returns the list of the notifications emitted by the MBean.
Each notification is described by an

MBeanNotificationInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanNotificationInfo

objects
but that each referenced

MBeanNotificationInfo

object is not copied.

**Returns:** An array of

MBeanNotificationInfo

objects.

---

#### getNotifications

public

MBeanNotificationInfo

[] getNotifications()

Returns the list of the notifications emitted by the MBean.
Each notification is described by an

MBeanNotificationInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanNotificationInfo

objects
but that each referenced

MBeanNotificationInfo

object is not copied.

getDescriptor

```java
public
Descriptor
getDescriptor()
```

Get the descriptor of this MBeanInfo. Changing the returned value
will have no affect on the original descriptor.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Returns:** a descriptor that is either immutable or a copy of the original.
**Since:** 1.6

---

#### getDescriptor

public

Descriptor

getDescriptor()

Get the descriptor of this MBeanInfo. Changing the returned value
will have no affect on the original descriptor.

equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanInfo to another. Two MBeanInfo objects
are equal if and only if they return equal values for

getClassName()

, for

getDescription()

, and for

getDescriptor()

, and the
arrays returned by the two objects for

getAttributes()

,

getOperations()

,

getConstructors()

, and

getNotifications()

are
pairwise equal. Here "equal" means

Object.equals(Object)

, not identity.

If two MBeanInfo objects return the same values in one of
their arrays but in a different order then they are not equal.

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanInfo that is equal
to this one according to the rules above.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compare this MBeanInfo to another. Two MBeanInfo objects
are equal if and only if they return equal values for

getClassName()

, for

getDescription()

, and for

getDescriptor()

, and the
arrays returned by the two objects for

getAttributes()

,

getOperations()

,

getConstructors()

, and

getNotifications()

are
pairwise equal. Here "equal" means

Object.equals(Object)

, not identity.

If two MBeanInfo objects return the same values in one of
their arrays but in a different order then they are not equal.

Compare this MBeanInfo to another. Two MBeanInfo objects
are equal if and only if they return equal values for

getClassName()

, for

getDescription()

, and for

getDescriptor()

, and the
arrays returned by the two objects for

getAttributes()

,

getOperations()

,

getConstructors()

, and

getNotifications()

are
pairwise equal. Here "equal" means

Object.equals(Object)

, not identity.

If two MBeanInfo objects return the same values in one of
their arrays but in a different order then they are not equal.

---

