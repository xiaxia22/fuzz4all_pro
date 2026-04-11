# Class ModelMBeanNotificationInfo

**Source:** `java.management\javax\management\modelmbean\ModelMBeanNotificationInfo.html`

### Class Description

```java
public class
ModelMBeanNotificationInfo

extends
MBeanNotificationInfo

implements
DescriptorAccess
```

The ModelMBeanNotificationInfo object describes a notification emitted
by a ModelMBean.
It is a subclass of MBeanNotificationInfo with the addition of an
associated Descriptor and an implementation of the Descriptor interface.

The fields in the descriptor are defined, but not limited to, the following.
Note that when the Type in this table is Number, a String that is the decimal
representation of a Long can also be used.

ModelMBeanNotificationInfo Fields

Name

Type

Meaning

name

String

Notification name.

descriptorType

String

Must be "notification".

severity

Number

0-6 where 0: unknown; 1: non-recoverable;
2: critical, failure; 3: major, severe;
4: minor, marginal, error; 5: warning;
6: normal, cleared, informative

messageID

String

Unique key for message text (to allow translation, analysis).

messageText

String

Text of notification.

log

String

T - log message, F - do not log message.

logfile

String

fully qualified file name appropriate for operating system.

visibility

Number

1-4 where 1: always visible 4: rarely visible.

presentationString

String

XML formatted string to allow presentation of data.

The default descriptor contains the name, descriptorType,
displayName and severity(=6) fields. The default value of the name
and displayName fields is the name of the Notification class (as
specified by the

name

parameter of the
ModelMBeanNotificationInfo constructor).

The

serialVersionUID

of this class is

-7445681389570207141L

.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorAccess

,

DescriptorRead

---

### Field Details

*No entries found.*

### Constructor Details

#### public ModelMBeanNotificationInfo​(
String
[] notifTypes,

String
name,

String
description)

Constructs a ModelMBeanNotificationInfo object with a default
descriptor.

**Parameters:**
- notifTypes

- The array of strings (in dot notation) containing
the notification types that may be emitted.
- name

- The name of the Notification class.
- description

- A human readable description of the
Notification. Optional.

---

#### public ModelMBeanNotificationInfo​(
String
[] notifTypes,

String
name,

String
description,

Descriptor
descriptor)

Constructs a ModelMBeanNotificationInfo object.

**Parameters:**
- notifTypes

- The array of strings (in dot notation)
containing the notification types that may be emitted.
- name

- The name of the Notification class.
- description

- A human readable description of the Notification.
Optional.
- descriptor

- An instance of Descriptor containing the
appropriate metadata for this instance of the
MBeanNotificationInfo. If it is null a default descriptor
will be created. If the descriptor does not contain the
fields "displayName" or "severity",
the missing ones are added with their default values.

**Throws:**
- RuntimeOperationsException

- Wraps an

IllegalArgumentException

. The descriptor is invalid, or
descriptor field "name" is not equal to parameter name, or
descriptor field "descriptorType" is not equal to "notification".

---

#### public ModelMBeanNotificationInfo​(
ModelMBeanNotificationInfo
inInfo)

Constructs a new ModelMBeanNotificationInfo object from this
ModelMBeanNotfication Object.

**Parameters:**
- inInfo

- the ModelMBeanNotificationInfo to be duplicated

---

### Method Details

#### public
Object
clone()

Creates and returns a new ModelMBeanNotificationInfo which is a
duplicate of this ModelMBeanNotificationInfo.

**Overrides:**
- clone

in class

MBeanNotificationInfo

**Returns:**
- a clone of this instance.

**See Also:**
- Cloneable

---

#### public
Descriptor
getDescriptor()

Returns a copy of the associated Descriptor for the
ModelMBeanNotificationInfo.

**Specified by:**
- getDescriptor

in interface

DescriptorRead

**Overrides:**
- getDescriptor

in class

MBeanFeatureInfo

**Returns:**
- Descriptor associated with the
ModelMBeanNotificationInfo object.

**See Also:**
- setDescriptor(javax.management.Descriptor)

---

#### public void setDescriptor​(
Descriptor
inDescriptor)

Sets associated Descriptor (full replace) for the
ModelMBeanNotificationInfo If the new Descriptor is null,
then the associated Descriptor reverts to a default
descriptor. The Descriptor is validated before it is
assigned. If the new Descriptor is invalid, then a
RuntimeOperationsException wrapping an
IllegalArgumentException is thrown.

**Specified by:**
- setDescriptor

in interface

DescriptorAccess

**Parameters:**
- inDescriptor

- replaces the Descriptor associated with the
ModelMBeanNotification interface

**Throws:**
- RuntimeOperationsException

- Wraps an

IllegalArgumentException

for invalid Descriptor.

**See Also:**
- getDescriptor()

---

#### public
String
toString()

Returns a human readable string containing
ModelMBeanNotificationInfo.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string describing this object.

---

### Additional Sections

#### Class ModelMBeanNotificationInfo

java.lang.Object

- javax.management.MBeanFeatureInfo
- - javax.management.MBeanNotificationInfo
- - javax.management.modelmbean.ModelMBeanNotificationInfo

javax.management.MBeanFeatureInfo

- javax.management.MBeanNotificationInfo
- - javax.management.modelmbean.ModelMBeanNotificationInfo

javax.management.MBeanNotificationInfo

- javax.management.modelmbean.ModelMBeanNotificationInfo

javax.management.modelmbean.ModelMBeanNotificationInfo

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorAccess

,

DescriptorRead

```java
public class
ModelMBeanNotificationInfo

extends
MBeanNotificationInfo

implements
DescriptorAccess
```

The ModelMBeanNotificationInfo object describes a notification emitted
by a ModelMBean.
It is a subclass of MBeanNotificationInfo with the addition of an
associated Descriptor and an implementation of the Descriptor interface.

The fields in the descriptor are defined, but not limited to, the following.
Note that when the Type in this table is Number, a String that is the decimal
representation of a Long can also be used.

ModelMBeanNotificationInfo Fields

Name

Type

Meaning

name

String

Notification name.

descriptorType

String

Must be "notification".

severity

Number

0-6 where 0: unknown; 1: non-recoverable;
2: critical, failure; 3: major, severe;
4: minor, marginal, error; 5: warning;
6: normal, cleared, informative

messageID

String

Unique key for message text (to allow translation, analysis).

messageText

String

Text of notification.

log

String

T - log message, F - do not log message.

logfile

String

fully qualified file name appropriate for operating system.

visibility

Number

1-4 where 1: always visible 4: rarely visible.

presentationString

String

XML formatted string to allow presentation of data.

The default descriptor contains the name, descriptorType,
displayName and severity(=6) fields. The default value of the name
and displayName fields is the name of the Notification class (as
specified by the

name

parameter of the
ModelMBeanNotificationInfo constructor).

The

serialVersionUID

of this class is

-7445681389570207141L

.

**Since:** 1.5
**See Also:** Serialized Form

public class

ModelMBeanNotificationInfo

extends

MBeanNotificationInfo

implements

DescriptorAccess

The ModelMBeanNotificationInfo object describes a notification emitted
by a ModelMBean.
It is a subclass of MBeanNotificationInfo with the addition of an
associated Descriptor and an implementation of the Descriptor interface.

The fields in the descriptor are defined, but not limited to, the following.
Note that when the Type in this table is Number, a String that is the decimal
representation of a Long can also be used.

ModelMBeanNotificationInfo Fields

Name

Type

Meaning

name

String

Notification name.

descriptorType

String

Must be "notification".

severity

Number

0-6 where 0: unknown; 1: non-recoverable;
2: critical, failure; 3: major, severe;
4: minor, marginal, error; 5: warning;
6: normal, cleared, informative

messageID

String

Unique key for message text (to allow translation, analysis).

messageText

String

Text of notification.

log

String

T - log message, F - do not log message.

logfile

String

fully qualified file name appropriate for operating system.

visibility

Number

1-4 where 1: always visible 4: rarely visible.

presentationString

String

XML formatted string to allow presentation of data.

The default descriptor contains the name, descriptorType,
displayName and severity(=6) fields. The default value of the name
and displayName fields is the name of the Notification class (as
specified by the

name

parameter of the
ModelMBeanNotificationInfo constructor).

The

serialVersionUID

of this class is

-7445681389570207141L

.

The ModelMBeanNotificationInfo object describes a notification emitted
by a ModelMBean.
It is a subclass of MBeanNotificationInfo with the addition of an
associated Descriptor and an implementation of the Descriptor interface.

The fields in the descriptor are defined, but not limited to, the following.
Note that when the Type in this table is Number, a String that is the decimal
representation of a Long can also be used.

The default descriptor contains the name, descriptorType,
displayName and severity(=6) fields. The default value of the name
and displayName fields is the name of the Notification class (as
specified by the

name

parameter of the
ModelMBeanNotificationInfo constructor).

The

serialVersionUID

of this class is

-7445681389570207141L

.

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

ModelMBeanNotificationInfo

​(

String

[] notifTypes,

String

name,

String

description)

Constructs a ModelMBeanNotificationInfo object with a default
descriptor.

ModelMBeanNotificationInfo

​(

String

[] notifTypes,

String

name,

String

description,

Descriptor

descriptor)

Constructs a ModelMBeanNotificationInfo object.

ModelMBeanNotificationInfo

​(

ModelMBeanNotificationInfo

inInfo)

Constructs a new ModelMBeanNotificationInfo object from this
ModelMBeanNotfication Object.

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

Creates and returns a new ModelMBeanNotificationInfo which is a
duplicate of this ModelMBeanNotificationInfo.

Descriptor

getDescriptor

()

Returns a copy of the associated Descriptor for the
ModelMBeanNotificationInfo.

void

setDescriptor

​(

Descriptor

inDescriptor)

Sets associated Descriptor (full replace) for the
ModelMBeanNotificationInfo If the new Descriptor is null,
then the associated Descriptor reverts to a default
descriptor.

String

toString

()

Returns a human readable string containing
ModelMBeanNotificationInfo.

- Methods declared in class javax.management.

MBeanNotificationInfo

equals

,

getNotifTypes

- Methods declared in class javax.management.

MBeanFeatureInfo

getDescription

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

ModelMBeanNotificationInfo

​(

String

[] notifTypes,

String

name,

String

description)

Constructs a ModelMBeanNotificationInfo object with a default
descriptor.

ModelMBeanNotificationInfo

​(

String

[] notifTypes,

String

name,

String

description,

Descriptor

descriptor)

Constructs a ModelMBeanNotificationInfo object.

ModelMBeanNotificationInfo

​(

ModelMBeanNotificationInfo

inInfo)

Constructs a new ModelMBeanNotificationInfo object from this
ModelMBeanNotfication Object.

---

#### Constructor Summary

Constructs a ModelMBeanNotificationInfo object with a default
descriptor.

Constructs a ModelMBeanNotificationInfo object.

Constructs a new ModelMBeanNotificationInfo object from this
ModelMBeanNotfication Object.

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

Creates and returns a new ModelMBeanNotificationInfo which is a
duplicate of this ModelMBeanNotificationInfo.

Descriptor

getDescriptor

()

Returns a copy of the associated Descriptor for the
ModelMBeanNotificationInfo.

void

setDescriptor

​(

Descriptor

inDescriptor)

Sets associated Descriptor (full replace) for the
ModelMBeanNotificationInfo If the new Descriptor is null,
then the associated Descriptor reverts to a default
descriptor.

String

toString

()

Returns a human readable string containing
ModelMBeanNotificationInfo.

- Methods declared in class javax.management.

MBeanNotificationInfo

equals

,

getNotifTypes

- Methods declared in class javax.management.

MBeanFeatureInfo

getDescription

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

wait

,

wait

,

wait

---

#### Method Summary

Creates and returns a new ModelMBeanNotificationInfo which is a
duplicate of this ModelMBeanNotificationInfo.

Returns a copy of the associated Descriptor for the
ModelMBeanNotificationInfo.

Sets associated Descriptor (full replace) for the
ModelMBeanNotificationInfo If the new Descriptor is null,
then the associated Descriptor reverts to a default
descriptor.

Returns a human readable string containing
ModelMBeanNotificationInfo.

Methods declared in class javax.management.

MBeanNotificationInfo

equals

,

getNotifTypes

---

#### Methods declared in class javax.management. MBeanNotificationInfo

Methods declared in class javax.management.

MBeanFeatureInfo

getDescription

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ModelMBeanNotificationInfo

```java
public ModelMBeanNotificationInfo​(
String
[] notifTypes,

String
name,

String
description)
```

Constructs a ModelMBeanNotificationInfo object with a default
descriptor.

**Parameters:** notifTypes

- The array of strings (in dot notation) containing
the notification types that may be emitted.
**Parameters:** name

- The name of the Notification class.
**Parameters:** description

- A human readable description of the
Notification. Optional.

- ModelMBeanNotificationInfo

```java
public ModelMBeanNotificationInfo​(
String
[] notifTypes,

String
name,

String
description,

Descriptor
descriptor)
```

Constructs a ModelMBeanNotificationInfo object.

**Parameters:** notifTypes

- The array of strings (in dot notation)
containing the notification types that may be emitted.
**Parameters:** name

- The name of the Notification class.
**Parameters:** description

- A human readable description of the Notification.
Optional.
**Parameters:** descriptor

- An instance of Descriptor containing the
appropriate metadata for this instance of the
MBeanNotificationInfo. If it is null a default descriptor
will be created. If the descriptor does not contain the
fields "displayName" or "severity",
the missing ones are added with their default values.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

. The descriptor is invalid, or
descriptor field "name" is not equal to parameter name, or
descriptor field "descriptorType" is not equal to "notification".

- ModelMBeanNotificationInfo

```java
public ModelMBeanNotificationInfo​(
ModelMBeanNotificationInfo
inInfo)
```

Constructs a new ModelMBeanNotificationInfo object from this
ModelMBeanNotfication Object.

**Parameters:** inInfo

- the ModelMBeanNotificationInfo to be duplicated

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
public
Object
clone()
```

Creates and returns a new ModelMBeanNotificationInfo which is a
duplicate of this ModelMBeanNotificationInfo.

**Overrides:** clone

in class

MBeanNotificationInfo
**Returns:** a clone of this instance.
**See Also:** Cloneable

- getDescriptor

```java
public
Descriptor
getDescriptor()
```

Returns a copy of the associated Descriptor for the
ModelMBeanNotificationInfo.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Overrides:** getDescriptor

in class

MBeanFeatureInfo
**Returns:** Descriptor associated with the
ModelMBeanNotificationInfo object.
**See Also:** setDescriptor(javax.management.Descriptor)

- setDescriptor

```java
public void setDescriptor​(
Descriptor
inDescriptor)
```

Sets associated Descriptor (full replace) for the
ModelMBeanNotificationInfo If the new Descriptor is null,
then the associated Descriptor reverts to a default
descriptor. The Descriptor is validated before it is
assigned. If the new Descriptor is invalid, then a
RuntimeOperationsException wrapping an
IllegalArgumentException is thrown.

**Specified by:** setDescriptor

in interface

DescriptorAccess
**Parameters:** inDescriptor

- replaces the Descriptor associated with the
ModelMBeanNotification interface
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

for invalid Descriptor.
**See Also:** getDescriptor()

- toString

```java
public
String
toString()
```

Returns a human readable string containing
ModelMBeanNotificationInfo.

**Overrides:** toString

in class

Object
**Returns:** a string describing this object.

Constructor Detail

- ModelMBeanNotificationInfo

```java
public ModelMBeanNotificationInfo​(
String
[] notifTypes,

String
name,

String
description)
```

Constructs a ModelMBeanNotificationInfo object with a default
descriptor.

**Parameters:** notifTypes

- The array of strings (in dot notation) containing
the notification types that may be emitted.
**Parameters:** name

- The name of the Notification class.
**Parameters:** description

- A human readable description of the
Notification. Optional.

- ModelMBeanNotificationInfo

```java
public ModelMBeanNotificationInfo​(
String
[] notifTypes,

String
name,

String
description,

Descriptor
descriptor)
```

Constructs a ModelMBeanNotificationInfo object.

**Parameters:** notifTypes

- The array of strings (in dot notation)
containing the notification types that may be emitted.
**Parameters:** name

- The name of the Notification class.
**Parameters:** description

- A human readable description of the Notification.
Optional.
**Parameters:** descriptor

- An instance of Descriptor containing the
appropriate metadata for this instance of the
MBeanNotificationInfo. If it is null a default descriptor
will be created. If the descriptor does not contain the
fields "displayName" or "severity",
the missing ones are added with their default values.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

. The descriptor is invalid, or
descriptor field "name" is not equal to parameter name, or
descriptor field "descriptorType" is not equal to "notification".

- ModelMBeanNotificationInfo

```java
public ModelMBeanNotificationInfo​(
ModelMBeanNotificationInfo
inInfo)
```

Constructs a new ModelMBeanNotificationInfo object from this
ModelMBeanNotfication Object.

**Parameters:** inInfo

- the ModelMBeanNotificationInfo to be duplicated

---

#### Constructor Detail

ModelMBeanNotificationInfo

```java
public ModelMBeanNotificationInfo​(
String
[] notifTypes,

String
name,

String
description)
```

Constructs a ModelMBeanNotificationInfo object with a default
descriptor.

**Parameters:** notifTypes

- The array of strings (in dot notation) containing
the notification types that may be emitted.
**Parameters:** name

- The name of the Notification class.
**Parameters:** description

- A human readable description of the
Notification. Optional.

---

#### ModelMBeanNotificationInfo

public ModelMBeanNotificationInfo​(

String

[] notifTypes,

String

name,

String

description)

Constructs a ModelMBeanNotificationInfo object with a default
descriptor.

ModelMBeanNotificationInfo

```java
public ModelMBeanNotificationInfo​(
String
[] notifTypes,

String
name,

String
description,

Descriptor
descriptor)
```

Constructs a ModelMBeanNotificationInfo object.

**Parameters:** notifTypes

- The array of strings (in dot notation)
containing the notification types that may be emitted.
**Parameters:** name

- The name of the Notification class.
**Parameters:** description

- A human readable description of the Notification.
Optional.
**Parameters:** descriptor

- An instance of Descriptor containing the
appropriate metadata for this instance of the
MBeanNotificationInfo. If it is null a default descriptor
will be created. If the descriptor does not contain the
fields "displayName" or "severity",
the missing ones are added with their default values.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

. The descriptor is invalid, or
descriptor field "name" is not equal to parameter name, or
descriptor field "descriptorType" is not equal to "notification".

---

#### ModelMBeanNotificationInfo

public ModelMBeanNotificationInfo​(

String

[] notifTypes,

String

name,

String

description,

Descriptor

descriptor)

Constructs a ModelMBeanNotificationInfo object.

ModelMBeanNotificationInfo

```java
public ModelMBeanNotificationInfo​(
ModelMBeanNotificationInfo
inInfo)
```

Constructs a new ModelMBeanNotificationInfo object from this
ModelMBeanNotfication Object.

**Parameters:** inInfo

- the ModelMBeanNotificationInfo to be duplicated

---

#### ModelMBeanNotificationInfo

public ModelMBeanNotificationInfo​(

ModelMBeanNotificationInfo

inInfo)

Constructs a new ModelMBeanNotificationInfo object from this
ModelMBeanNotfication Object.

Method Detail

- clone

```java
public
Object
clone()
```

Creates and returns a new ModelMBeanNotificationInfo which is a
duplicate of this ModelMBeanNotificationInfo.

**Overrides:** clone

in class

MBeanNotificationInfo
**Returns:** a clone of this instance.
**See Also:** Cloneable

- getDescriptor

```java
public
Descriptor
getDescriptor()
```

Returns a copy of the associated Descriptor for the
ModelMBeanNotificationInfo.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Overrides:** getDescriptor

in class

MBeanFeatureInfo
**Returns:** Descriptor associated with the
ModelMBeanNotificationInfo object.
**See Also:** setDescriptor(javax.management.Descriptor)

- setDescriptor

```java
public void setDescriptor​(
Descriptor
inDescriptor)
```

Sets associated Descriptor (full replace) for the
ModelMBeanNotificationInfo If the new Descriptor is null,
then the associated Descriptor reverts to a default
descriptor. The Descriptor is validated before it is
assigned. If the new Descriptor is invalid, then a
RuntimeOperationsException wrapping an
IllegalArgumentException is thrown.

**Specified by:** setDescriptor

in interface

DescriptorAccess
**Parameters:** inDescriptor

- replaces the Descriptor associated with the
ModelMBeanNotification interface
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

for invalid Descriptor.
**See Also:** getDescriptor()

- toString

```java
public
String
toString()
```

Returns a human readable string containing
ModelMBeanNotificationInfo.

**Overrides:** toString

in class

Object
**Returns:** a string describing this object.

---

#### Method Detail

clone

```java
public
Object
clone()
```

Creates and returns a new ModelMBeanNotificationInfo which is a
duplicate of this ModelMBeanNotificationInfo.

**Overrides:** clone

in class

MBeanNotificationInfo
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Creates and returns a new ModelMBeanNotificationInfo which is a
duplicate of this ModelMBeanNotificationInfo.

getDescriptor

```java
public
Descriptor
getDescriptor()
```

Returns a copy of the associated Descriptor for the
ModelMBeanNotificationInfo.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Overrides:** getDescriptor

in class

MBeanFeatureInfo
**Returns:** Descriptor associated with the
ModelMBeanNotificationInfo object.
**See Also:** setDescriptor(javax.management.Descriptor)

---

#### getDescriptor

public

Descriptor

getDescriptor()

Returns a copy of the associated Descriptor for the
ModelMBeanNotificationInfo.

setDescriptor

```java
public void setDescriptor​(
Descriptor
inDescriptor)
```

Sets associated Descriptor (full replace) for the
ModelMBeanNotificationInfo If the new Descriptor is null,
then the associated Descriptor reverts to a default
descriptor. The Descriptor is validated before it is
assigned. If the new Descriptor is invalid, then a
RuntimeOperationsException wrapping an
IllegalArgumentException is thrown.

**Specified by:** setDescriptor

in interface

DescriptorAccess
**Parameters:** inDescriptor

- replaces the Descriptor associated with the
ModelMBeanNotification interface
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

for invalid Descriptor.
**See Also:** getDescriptor()

---

#### setDescriptor

public void setDescriptor​(

Descriptor

inDescriptor)

Sets associated Descriptor (full replace) for the
ModelMBeanNotificationInfo If the new Descriptor is null,
then the associated Descriptor reverts to a default
descriptor. The Descriptor is validated before it is
assigned. If the new Descriptor is invalid, then a
RuntimeOperationsException wrapping an
IllegalArgumentException is thrown.

toString

```java
public
String
toString()
```

Returns a human readable string containing
ModelMBeanNotificationInfo.

**Overrides:** toString

in class

Object
**Returns:** a string describing this object.

---

#### toString

public

String

toString()

Returns a human readable string containing
ModelMBeanNotificationInfo.

---

