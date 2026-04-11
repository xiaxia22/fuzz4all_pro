# Class MBeanNotificationInfo

**Source:** `java.management\javax\management\MBeanNotificationInfo.html`

### Class Description

```java
public class
MBeanNotificationInfo

extends
MBeanFeatureInfo

implements
Cloneable
```

The

MBeanNotificationInfo

class is used to describe the
characteristics of the different notification instances
emitted by an MBean, for a given Java class of notification.
If an MBean emits notifications that can be instances of different Java classes,
then the metadata for that MBean should provide an

MBeanNotificationInfo

object for each of these notification Java classes.

Instances of this class are immutable. Subclasses may be
mutable but this is not recommended.

This class extends

javax.management.MBeanFeatureInfo

and thus provides

name

and

description

fields.
The

name

field should be the fully qualified Java class name of
the notification objects described by this class.

The

getNotifTypes

method returns an array of
strings containing the notification types that the MBean may
emit. The notification type is a dot-notation string which
describes what the emitted notification is about, not the Java
class of the notification. A single generic notification class can
be used to send notifications of several types. All of these types
are returned in the string array result of the

getNotifTypes

method.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

---

### Field Details

*No entries found.*

### Constructor Details

#### public MBeanNotificationInfo​(
String
[] notifTypes,

String
name,

String
description)

Constructs an

MBeanNotificationInfo

object.

**Parameters:**
- notifTypes

- The array of strings (in dot notation)
containing the notification types that the MBean may emit.
This may be null with the same effect as a zero-length array.
- name

- The fully qualified Java class name of the
described notifications.
- description

- A human readable description of the data.

---

#### public MBeanNotificationInfo​(
String
[] notifTypes,

String
name,

String
description,

Descriptor
descriptor)

Constructs an

MBeanNotificationInfo

object.

**Parameters:**
- notifTypes

- The array of strings (in dot notation)
containing the notification types that the MBean may emit.
This may be null with the same effect as a zero-length array.
- name

- The fully qualified Java class name of the
described notifications.
- description

- A human readable description of the data.
- descriptor

- The descriptor for the notifications. This may be null
which is equivalent to an empty descriptor.

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
[] getNotifTypes()

Returns the array of strings (in dot notation) containing the
notification types that the MBean may emit.

**Returns:**
- the array of strings. Changing the returned array has no
effect on this MBeanNotificationInfo.

---

#### public boolean equals​(
Object
o)

Compare this MBeanNotificationInfo to another.

**Overrides:**
- equals

in class

MBeanFeatureInfo

**Parameters:**
- o

- the object to compare to.

**Returns:**
- true if and only if

o

is an MBeanNotificationInfo
such that its

MBeanFeatureInfo.getName()

,

MBeanFeatureInfo.getDescription()

,

MBeanFeatureInfo.getDescriptor()

,
and

getNotifTypes()

values are equal (not necessarily
identical) to those of this MBeanNotificationInfo. Two
notification type arrays are equal if their corresponding
elements are equal. They are not equal if they have the same
elements but in a different order.

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class MBeanNotificationInfo

java.lang.Object

- javax.management.MBeanFeatureInfo
- - javax.management.MBeanNotificationInfo

javax.management.MBeanFeatureInfo

- javax.management.MBeanNotificationInfo

javax.management.MBeanNotificationInfo

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

**Direct Known Subclasses:** ModelMBeanNotificationInfo

```java
public class
MBeanNotificationInfo

extends
MBeanFeatureInfo

implements
Cloneable
```

The

MBeanNotificationInfo

class is used to describe the
characteristics of the different notification instances
emitted by an MBean, for a given Java class of notification.
If an MBean emits notifications that can be instances of different Java classes,
then the metadata for that MBean should provide an

MBeanNotificationInfo

object for each of these notification Java classes.

Instances of this class are immutable. Subclasses may be
mutable but this is not recommended.

This class extends

javax.management.MBeanFeatureInfo

and thus provides

name

and

description

fields.
The

name

field should be the fully qualified Java class name of
the notification objects described by this class.

The

getNotifTypes

method returns an array of
strings containing the notification types that the MBean may
emit. The notification type is a dot-notation string which
describes what the emitted notification is about, not the Java
class of the notification. A single generic notification class can
be used to send notifications of several types. All of these types
are returned in the string array result of the

getNotifTypes

method.

**Since:** 1.5
**See Also:** Serialized Form

public class

MBeanNotificationInfo

extends

MBeanFeatureInfo

implements

Cloneable

The

MBeanNotificationInfo

class is used to describe the
characteristics of the different notification instances
emitted by an MBean, for a given Java class of notification.
If an MBean emits notifications that can be instances of different Java classes,
then the metadata for that MBean should provide an

MBeanNotificationInfo

object for each of these notification Java classes.

Instances of this class are immutable. Subclasses may be
mutable but this is not recommended.

This class extends

javax.management.MBeanFeatureInfo

and thus provides

name

and

description

fields.
The

name

field should be the fully qualified Java class name of
the notification objects described by this class.

The

getNotifTypes

method returns an array of
strings containing the notification types that the MBean may
emit. The notification type is a dot-notation string which
describes what the emitted notification is about, not the Java
class of the notification. A single generic notification class can
be used to send notifications of several types. All of these types
are returned in the string array result of the

getNotifTypes

method.

The

MBeanNotificationInfo

class is used to describe the
characteristics of the different notification instances
emitted by an MBean, for a given Java class of notification.
If an MBean emits notifications that can be instances of different Java classes,
then the metadata for that MBean should provide an

MBeanNotificationInfo

object for each of these notification Java classes.

Instances of this class are immutable. Subclasses may be
mutable but this is not recommended.

This class extends

javax.management.MBeanFeatureInfo

and thus provides

name

and

description

fields.
The

name

field should be the fully qualified Java class name of
the notification objects described by this class.

The

getNotifTypes

method returns an array of
strings containing the notification types that the MBean may
emit. The notification type is a dot-notation string which
describes what the emitted notification is about, not the Java
class of the notification. A single generic notification class can
be used to send notifications of several types. All of these types
are returned in the string array result of the

getNotifTypes

method.

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

MBeanNotificationInfo

​(

String

[] notifTypes,

String

name,

String

description)

Constructs an

MBeanNotificationInfo

object.

MBeanNotificationInfo

​(

String

[] notifTypes,

String

name,

String

description,

Descriptor

descriptor)

Constructs an

MBeanNotificationInfo

object.

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

Compare this MBeanNotificationInfo to another.

String

[]

getNotifTypes

()

Returns the array of strings (in dot notation) containing the
notification types that the MBean may emit.

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

MBeanNotificationInfo

​(

String

[] notifTypes,

String

name,

String

description)

Constructs an

MBeanNotificationInfo

object.

MBeanNotificationInfo

​(

String

[] notifTypes,

String

name,

String

description,

Descriptor

descriptor)

Constructs an

MBeanNotificationInfo

object.

---

#### Constructor Summary

Constructs an

MBeanNotificationInfo

object.

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

Compare this MBeanNotificationInfo to another.

String

[]

getNotifTypes

()

Returns the array of strings (in dot notation) containing the
notification types that the MBean may emit.

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

Compare this MBeanNotificationInfo to another.

Returns the array of strings (in dot notation) containing the
notification types that the MBean may emit.

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

- MBeanNotificationInfo

```java
public MBeanNotificationInfo​(
String
[] notifTypes,

String
name,

String
description)
```

Constructs an

MBeanNotificationInfo

object.

**Parameters:** notifTypes

- The array of strings (in dot notation)
containing the notification types that the MBean may emit.
This may be null with the same effect as a zero-length array.
**Parameters:** name

- The fully qualified Java class name of the
described notifications.
**Parameters:** description

- A human readable description of the data.

- MBeanNotificationInfo

```java
public MBeanNotificationInfo​(
String
[] notifTypes,

String
name,

String
description,

Descriptor
descriptor)
```

Constructs an

MBeanNotificationInfo

object.

**Parameters:** notifTypes

- The array of strings (in dot notation)
containing the notification types that the MBean may emit.
This may be null with the same effect as a zero-length array.
**Parameters:** name

- The fully qualified Java class name of the
described notifications.
**Parameters:** description

- A human readable description of the data.
**Parameters:** descriptor

- The descriptor for the notifications. This may be null
which is equivalent to an empty descriptor.
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

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

- getNotifTypes

```java
public
String
[] getNotifTypes()
```

Returns the array of strings (in dot notation) containing the
notification types that the MBean may emit.

**Returns:** the array of strings. Changing the returned array has no
effect on this MBeanNotificationInfo.

- equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanNotificationInfo to another.

**Overrides:** equals

in class

MBeanFeatureInfo
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanNotificationInfo
such that its

MBeanFeatureInfo.getName()

,

MBeanFeatureInfo.getDescription()

,

MBeanFeatureInfo.getDescriptor()

,
and

getNotifTypes()

values are equal (not necessarily
identical) to those of this MBeanNotificationInfo. Two
notification type arrays are equal if their corresponding
elements are equal. They are not equal if they have the same
elements but in a different order.
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- MBeanNotificationInfo

```java
public MBeanNotificationInfo​(
String
[] notifTypes,

String
name,

String
description)
```

Constructs an

MBeanNotificationInfo

object.

**Parameters:** notifTypes

- The array of strings (in dot notation)
containing the notification types that the MBean may emit.
This may be null with the same effect as a zero-length array.
**Parameters:** name

- The fully qualified Java class name of the
described notifications.
**Parameters:** description

- A human readable description of the data.

- MBeanNotificationInfo

```java
public MBeanNotificationInfo​(
String
[] notifTypes,

String
name,

String
description,

Descriptor
descriptor)
```

Constructs an

MBeanNotificationInfo

object.

**Parameters:** notifTypes

- The array of strings (in dot notation)
containing the notification types that the MBean may emit.
This may be null with the same effect as a zero-length array.
**Parameters:** name

- The fully qualified Java class name of the
described notifications.
**Parameters:** description

- A human readable description of the data.
**Parameters:** descriptor

- The descriptor for the notifications. This may be null
which is equivalent to an empty descriptor.
**Since:** 1.6

---

#### Constructor Detail

MBeanNotificationInfo

```java
public MBeanNotificationInfo​(
String
[] notifTypes,

String
name,

String
description)
```

Constructs an

MBeanNotificationInfo

object.

**Parameters:** notifTypes

- The array of strings (in dot notation)
containing the notification types that the MBean may emit.
This may be null with the same effect as a zero-length array.
**Parameters:** name

- The fully qualified Java class name of the
described notifications.
**Parameters:** description

- A human readable description of the data.

---

#### MBeanNotificationInfo

public MBeanNotificationInfo​(

String

[] notifTypes,

String

name,

String

description)

Constructs an

MBeanNotificationInfo

object.

MBeanNotificationInfo

```java
public MBeanNotificationInfo​(
String
[] notifTypes,

String
name,

String
description,

Descriptor
descriptor)
```

Constructs an

MBeanNotificationInfo

object.

**Parameters:** notifTypes

- The array of strings (in dot notation)
containing the notification types that the MBean may emit.
This may be null with the same effect as a zero-length array.
**Parameters:** name

- The fully qualified Java class name of the
described notifications.
**Parameters:** description

- A human readable description of the data.
**Parameters:** descriptor

- The descriptor for the notifications. This may be null
which is equivalent to an empty descriptor.
**Since:** 1.6

---

#### MBeanNotificationInfo

public MBeanNotificationInfo​(

String

[] notifTypes,

String

name,

String

description,

Descriptor

descriptor)

Constructs an

MBeanNotificationInfo

object.

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

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

- getNotifTypes

```java
public
String
[] getNotifTypes()
```

Returns the array of strings (in dot notation) containing the
notification types that the MBean may emit.

**Returns:** the array of strings. Changing the returned array has no
effect on this MBeanNotificationInfo.

- equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanNotificationInfo to another.

**Overrides:** equals

in class

MBeanFeatureInfo
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanNotificationInfo
such that its

MBeanFeatureInfo.getName()

,

MBeanFeatureInfo.getDescription()

,

MBeanFeatureInfo.getDescriptor()

,
and

getNotifTypes()

values are equal (not necessarily
identical) to those of this MBeanNotificationInfo. Two
notification type arrays are equal if their corresponding
elements are equal. They are not equal if they have the same
elements but in a different order.
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

getNotifTypes

```java
public
String
[] getNotifTypes()
```

Returns the array of strings (in dot notation) containing the
notification types that the MBean may emit.

**Returns:** the array of strings. Changing the returned array has no
effect on this MBeanNotificationInfo.

---

#### getNotifTypes

public

String

[] getNotifTypes()

Returns the array of strings (in dot notation) containing the
notification types that the MBean may emit.

equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanNotificationInfo to another.

**Overrides:** equals

in class

MBeanFeatureInfo
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanNotificationInfo
such that its

MBeanFeatureInfo.getName()

,

MBeanFeatureInfo.getDescription()

,

MBeanFeatureInfo.getDescriptor()

,
and

getNotifTypes()

values are equal (not necessarily
identical) to those of this MBeanNotificationInfo. Two
notification type arrays are equal if their corresponding
elements are equal. They are not equal if they have the same
elements but in a different order.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compare this MBeanNotificationInfo to another.

---

