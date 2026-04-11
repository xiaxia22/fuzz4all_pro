# Class ModelMBeanOperationInfo

**Source:** `java.management\javax\management\modelmbean\ModelMBeanOperationInfo.html`

### Class Description

```java
public class
ModelMBeanOperationInfo

extends
MBeanOperationInfo

implements
DescriptorAccess
```

The ModelMBeanOperationInfo object describes a management operation of
the ModelMBean. It is a subclass of MBeanOperationInfo with the addition
of an associated Descriptor and an implementation of the DescriptorAccess
interface.

The fields in the descriptor are defined, but not limited to, the following.
Note that when the Type in this table is Number, a String that is the decimal
representation of a Long can also be used.

ModelMBeanOperationInfo Fields

Name

Type

Meaning

name

String

Operation name.

descriptorType

String

Must be "operation".

class

String

Class where method is defined (fully qualified).

role

String

Must be "operation", "getter", or "setter".

targetObject

Object

Object on which to execute this method.

targetType

String

type of object reference for targetObject. Can be:
ObjectReference | Handle | EJBHandle | IOR | RMIReference.

value

Object

Cached value for operation.

displayName

String

Human readable display name of the operation.

currencyTimeLimit

Number

How long cached value is valid.

lastUpdatedTimeStamp

Number

When cached value was set.

visibility

Number

1-4 where 1: always visible 4: rarely visible.

presentationString

String

XML formatted string to describe how to present operation

The default descriptor will have name, descriptorType, displayName and
role fields set. The default value of the name and displayName fields is
the operation name.

Note:

because of inconsistencies in previous versions of
this specification, it is recommended not to use negative or zero
values for

currencyTimeLimit

. To indicate that a
cached value is never valid, omit the

currencyTimeLimit

field. To indicate that it is
always valid, use a very large number for this field.

The

serialVersionUID

of this class is

6532732096650090465L

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

#### public ModelMBeanOperationInfo​(
String
description,

Method
operationMethod)

Constructs a ModelMBeanOperationInfo object with a default
descriptor. The

Descriptor

of the constructed
object will include fields contributed by any annotations
on the

Method

object that contain the

DescriptorKey

meta-annotation.

**Parameters:**
- operationMethod

- The java.lang.reflect.Method object
describing the MBean operation.
- description

- A human readable description of the operation.

---

#### public ModelMBeanOperationInfo​(
String
description,

Method
operationMethod,

Descriptor
descriptor)

Constructs a ModelMBeanOperationInfo object. The

Descriptor

of the constructed object will include fields
contributed by any annotations on the

Method

object
that contain the

DescriptorKey

meta-annotation.

**Parameters:**
- operationMethod

- The java.lang.reflect.Method object
describing the MBean operation.
- description

- A human readable description of the
operation.
- descriptor

- An instance of Descriptor containing the
appropriate metadata for this instance of the
ModelMBeanOperationInfo. If it is null a default
descriptor will be created. If the descriptor does not
contain the fields
"displayName" or "role", the missing ones are added with
their default values.

**Throws:**
- RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid; or
descriptor field "name" is not equal to
operation name; or descriptor field "DescriptorType" is
not equal to "operation"; or descriptor
optional field "role" is present but not equal to "operation",
"getter", or "setter".

---

#### public ModelMBeanOperationInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

String
type,
int impact)

Constructs a ModelMBeanOperationInfo object with a default descriptor.

**Parameters:**
- name

- The name of the method.
- description

- A human readable description of the operation.
- signature

- MBeanParameterInfo objects describing the
parameters(arguments) of the method.
- type

- The type of the method's return value.
- impact

- The impact of the method, one of INFO, ACTION,
ACTION_INFO, UNKNOWN.

---

#### public ModelMBeanOperationInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

String
type,
int impact,

Descriptor
descriptor)

Constructs a ModelMBeanOperationInfo object.

**Parameters:**
- name

- The name of the method.
- description

- A human readable description of the operation.
- signature

- MBeanParameterInfo objects describing the
parameters(arguments) of the method.
- type

- The type of the method's return value.
- impact

- The impact of the method, one of INFO, ACTION,
ACTION_INFO, UNKNOWN.
- descriptor

- An instance of Descriptor containing the
appropriate metadata for this instance of the
MBeanOperationInfo. If it is null then a default descriptor
will be created. If the descriptor does not contain
fields "displayName" or "role",
the missing ones are added with their default values.

**Throws:**
- RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid; or
descriptor field "name" is not equal to
operation name; or descriptor field "DescriptorType" is
not equal to "operation"; or descriptor optional
field "role" is present but not equal to "operation", "getter", or
"setter".

---

#### public ModelMBeanOperationInfo​(
ModelMBeanOperationInfo
inInfo)

Constructs a new ModelMBeanOperationInfo object from this
ModelMBeanOperation Object.

**Parameters:**
- inInfo

- the ModelMBeanOperationInfo to be duplicated

---

### Method Details

#### public
Object
clone()

Creates and returns a new ModelMBeanOperationInfo which is a
duplicate of this ModelMBeanOperationInfo.

**Overrides:**
- clone

in class

MBeanOperationInfo

**Returns:**
- a clone of this instance.

**See Also:**
- Cloneable

---

#### public
Descriptor
getDescriptor()

Returns a copy of the associated Descriptor of the
ModelMBeanOperationInfo.

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
ModelMBeanOperationInfo object.

**See Also:**
- setDescriptor(javax.management.Descriptor)

---

#### public void setDescriptor​(
Descriptor
inDescriptor)

Sets associated Descriptor (full replace) for the
ModelMBeanOperationInfo If the new Descriptor is null, then
the associated Descriptor reverts to a default descriptor.
The Descriptor is validated before it is assigned. If the
new Descriptor is invalid, then a
RuntimeOperationsException wrapping an
IllegalArgumentException is thrown.

**Specified by:**
- setDescriptor

in interface

DescriptorAccess

**Parameters:**
- inDescriptor

- replaces the Descriptor associated with the
ModelMBeanOperation.

**Throws:**
- RuntimeOperationsException

- Wraps an
IllegalArgumentException for invalid Descriptor.

**See Also:**
- getDescriptor()

---

#### public
String
toString()

Returns a string containing the entire contents of the
ModelMBeanOperationInfo in human readable form.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class ModelMBeanOperationInfo

java.lang.Object

- javax.management.MBeanFeatureInfo
- - javax.management.MBeanOperationInfo
- - javax.management.modelmbean.ModelMBeanOperationInfo

javax.management.MBeanFeatureInfo

- javax.management.MBeanOperationInfo
- - javax.management.modelmbean.ModelMBeanOperationInfo

javax.management.MBeanOperationInfo

- javax.management.modelmbean.ModelMBeanOperationInfo

javax.management.modelmbean.ModelMBeanOperationInfo

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorAccess

,

DescriptorRead

```java
public class
ModelMBeanOperationInfo

extends
MBeanOperationInfo

implements
DescriptorAccess
```

The ModelMBeanOperationInfo object describes a management operation of
the ModelMBean. It is a subclass of MBeanOperationInfo with the addition
of an associated Descriptor and an implementation of the DescriptorAccess
interface.

The fields in the descriptor are defined, but not limited to, the following.
Note that when the Type in this table is Number, a String that is the decimal
representation of a Long can also be used.

ModelMBeanOperationInfo Fields

Name

Type

Meaning

name

String

Operation name.

descriptorType

String

Must be "operation".

class

String

Class where method is defined (fully qualified).

role

String

Must be "operation", "getter", or "setter".

targetObject

Object

Object on which to execute this method.

targetType

String

type of object reference for targetObject. Can be:
ObjectReference | Handle | EJBHandle | IOR | RMIReference.

value

Object

Cached value for operation.

displayName

String

Human readable display name of the operation.

currencyTimeLimit

Number

How long cached value is valid.

lastUpdatedTimeStamp

Number

When cached value was set.

visibility

Number

1-4 where 1: always visible 4: rarely visible.

presentationString

String

XML formatted string to describe how to present operation

The default descriptor will have name, descriptorType, displayName and
role fields set. The default value of the name and displayName fields is
the operation name.

Note:

because of inconsistencies in previous versions of
this specification, it is recommended not to use negative or zero
values for

currencyTimeLimit

. To indicate that a
cached value is never valid, omit the

currencyTimeLimit

field. To indicate that it is
always valid, use a very large number for this field.

The

serialVersionUID

of this class is

6532732096650090465L

.

**Since:** 1.5
**See Also:** Serialized Form

public class

ModelMBeanOperationInfo

extends

MBeanOperationInfo

implements

DescriptorAccess

The ModelMBeanOperationInfo object describes a management operation of
the ModelMBean. It is a subclass of MBeanOperationInfo with the addition
of an associated Descriptor and an implementation of the DescriptorAccess
interface.

The fields in the descriptor are defined, but not limited to, the following.
Note that when the Type in this table is Number, a String that is the decimal
representation of a Long can also be used.

ModelMBeanOperationInfo Fields

Name

Type

Meaning

name

String

Operation name.

descriptorType

String

Must be "operation".

class

String

Class where method is defined (fully qualified).

role

String

Must be "operation", "getter", or "setter".

targetObject

Object

Object on which to execute this method.

targetType

String

type of object reference for targetObject. Can be:
ObjectReference | Handle | EJBHandle | IOR | RMIReference.

value

Object

Cached value for operation.

displayName

String

Human readable display name of the operation.

currencyTimeLimit

Number

How long cached value is valid.

lastUpdatedTimeStamp

Number

When cached value was set.

visibility

Number

1-4 where 1: always visible 4: rarely visible.

presentationString

String

XML formatted string to describe how to present operation

The default descriptor will have name, descriptorType, displayName and
role fields set. The default value of the name and displayName fields is
the operation name.

Note:

because of inconsistencies in previous versions of
this specification, it is recommended not to use negative or zero
values for

currencyTimeLimit

. To indicate that a
cached value is never valid, omit the

currencyTimeLimit

field. To indicate that it is
always valid, use a very large number for this field.

The

serialVersionUID

of this class is

6532732096650090465L

.

The ModelMBeanOperationInfo object describes a management operation of
the ModelMBean. It is a subclass of MBeanOperationInfo with the addition
of an associated Descriptor and an implementation of the DescriptorAccess
interface.

The fields in the descriptor are defined, but not limited to, the following.
Note that when the Type in this table is Number, a String that is the decimal
representation of a Long can also be used.

The default descriptor will have name, descriptorType, displayName and
role fields set. The default value of the name and displayName fields is
the operation name.

Note:

because of inconsistencies in previous versions of
this specification, it is recommended not to use negative or zero
values for

currencyTimeLimit

. To indicate that a
cached value is never valid, omit the

currencyTimeLimit

field. To indicate that it is
always valid, use a very large number for this field.

The

serialVersionUID

of this class is

6532732096650090465L

.

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

ModelMBeanOperationInfo

​(

String

description,

Method

operationMethod)

Constructs a ModelMBeanOperationInfo object with a default
descriptor.

ModelMBeanOperationInfo

​(

String

description,

Method

operationMethod,

Descriptor

descriptor)

Constructs a ModelMBeanOperationInfo object.

ModelMBeanOperationInfo

​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

String

type,
int impact)

Constructs a ModelMBeanOperationInfo object with a default descriptor.

ModelMBeanOperationInfo

​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

String

type,
int impact,

Descriptor

descriptor)

Constructs a ModelMBeanOperationInfo object.

ModelMBeanOperationInfo

​(

ModelMBeanOperationInfo

inInfo)

Constructs a new ModelMBeanOperationInfo object from this
ModelMBeanOperation Object.

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

Creates and returns a new ModelMBeanOperationInfo which is a
duplicate of this ModelMBeanOperationInfo.

Descriptor

getDescriptor

()

Returns a copy of the associated Descriptor of the
ModelMBeanOperationInfo.

void

setDescriptor

​(

Descriptor

inDescriptor)

Sets associated Descriptor (full replace) for the
ModelMBeanOperationInfo If the new Descriptor is null, then
the associated Descriptor reverts to a default descriptor.

String

toString

()

Returns a string containing the entire contents of the
ModelMBeanOperationInfo in human readable form.

- Methods declared in class javax.management.

MBeanOperationInfo

equals

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

ModelMBeanOperationInfo

​(

String

description,

Method

operationMethod)

Constructs a ModelMBeanOperationInfo object with a default
descriptor.

ModelMBeanOperationInfo

​(

String

description,

Method

operationMethod,

Descriptor

descriptor)

Constructs a ModelMBeanOperationInfo object.

ModelMBeanOperationInfo

​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

String

type,
int impact)

Constructs a ModelMBeanOperationInfo object with a default descriptor.

ModelMBeanOperationInfo

​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

String

type,
int impact,

Descriptor

descriptor)

Constructs a ModelMBeanOperationInfo object.

ModelMBeanOperationInfo

​(

ModelMBeanOperationInfo

inInfo)

Constructs a new ModelMBeanOperationInfo object from this
ModelMBeanOperation Object.

---

#### Constructor Summary

Constructs a ModelMBeanOperationInfo object with a default
descriptor.

Constructs a ModelMBeanOperationInfo object.

Constructs a ModelMBeanOperationInfo object with a default descriptor.

Constructs a new ModelMBeanOperationInfo object from this
ModelMBeanOperation Object.

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

Creates and returns a new ModelMBeanOperationInfo which is a
duplicate of this ModelMBeanOperationInfo.

Descriptor

getDescriptor

()

Returns a copy of the associated Descriptor of the
ModelMBeanOperationInfo.

void

setDescriptor

​(

Descriptor

inDescriptor)

Sets associated Descriptor (full replace) for the
ModelMBeanOperationInfo If the new Descriptor is null, then
the associated Descriptor reverts to a default descriptor.

String

toString

()

Returns a string containing the entire contents of the
ModelMBeanOperationInfo in human readable form.

- Methods declared in class javax.management.

MBeanOperationInfo

equals

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

Creates and returns a new ModelMBeanOperationInfo which is a
duplicate of this ModelMBeanOperationInfo.

Returns a copy of the associated Descriptor of the
ModelMBeanOperationInfo.

Sets associated Descriptor (full replace) for the
ModelMBeanOperationInfo If the new Descriptor is null, then
the associated Descriptor reverts to a default descriptor.

Returns a string containing the entire contents of the
ModelMBeanOperationInfo in human readable form.

Methods declared in class javax.management.

MBeanOperationInfo

equals

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

- ModelMBeanOperationInfo

```java
public ModelMBeanOperationInfo​(
String
description,

Method
operationMethod)
```

Constructs a ModelMBeanOperationInfo object with a default
descriptor. The

Descriptor

of the constructed
object will include fields contributed by any annotations
on the

Method

object that contain the

DescriptorKey

meta-annotation.

**Parameters:** operationMethod

- The java.lang.reflect.Method object
describing the MBean operation.
**Parameters:** description

- A human readable description of the operation.

- ModelMBeanOperationInfo

```java
public ModelMBeanOperationInfo​(
String
description,

Method
operationMethod,

Descriptor
descriptor)
```

Constructs a ModelMBeanOperationInfo object. The

Descriptor

of the constructed object will include fields
contributed by any annotations on the

Method

object
that contain the

DescriptorKey

meta-annotation.

**Parameters:** operationMethod

- The java.lang.reflect.Method object
describing the MBean operation.
**Parameters:** description

- A human readable description of the
operation.
**Parameters:** descriptor

- An instance of Descriptor containing the
appropriate metadata for this instance of the
ModelMBeanOperationInfo. If it is null a default
descriptor will be created. If the descriptor does not
contain the fields
"displayName" or "role", the missing ones are added with
their default values.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid; or
descriptor field "name" is not equal to
operation name; or descriptor field "DescriptorType" is
not equal to "operation"; or descriptor
optional field "role" is present but not equal to "operation",
"getter", or "setter".

- ModelMBeanOperationInfo

```java
public ModelMBeanOperationInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

String
type,
int impact)
```

Constructs a ModelMBeanOperationInfo object with a default descriptor.

**Parameters:** name

- The name of the method.
**Parameters:** description

- A human readable description of the operation.
**Parameters:** signature

- MBeanParameterInfo objects describing the
parameters(arguments) of the method.
**Parameters:** type

- The type of the method's return value.
**Parameters:** impact

- The impact of the method, one of INFO, ACTION,
ACTION_INFO, UNKNOWN.

- ModelMBeanOperationInfo

```java
public ModelMBeanOperationInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

String
type,
int impact,

Descriptor
descriptor)
```

Constructs a ModelMBeanOperationInfo object.

**Parameters:** name

- The name of the method.
**Parameters:** description

- A human readable description of the operation.
**Parameters:** signature

- MBeanParameterInfo objects describing the
parameters(arguments) of the method.
**Parameters:** type

- The type of the method's return value.
**Parameters:** impact

- The impact of the method, one of INFO, ACTION,
ACTION_INFO, UNKNOWN.
**Parameters:** descriptor

- An instance of Descriptor containing the
appropriate metadata for this instance of the
MBeanOperationInfo. If it is null then a default descriptor
will be created. If the descriptor does not contain
fields "displayName" or "role",
the missing ones are added with their default values.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid; or
descriptor field "name" is not equal to
operation name; or descriptor field "DescriptorType" is
not equal to "operation"; or descriptor optional
field "role" is present but not equal to "operation", "getter", or
"setter".

- ModelMBeanOperationInfo

```java
public ModelMBeanOperationInfo​(
ModelMBeanOperationInfo
inInfo)
```

Constructs a new ModelMBeanOperationInfo object from this
ModelMBeanOperation Object.

**Parameters:** inInfo

- the ModelMBeanOperationInfo to be duplicated

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
public
Object
clone()
```

Creates and returns a new ModelMBeanOperationInfo which is a
duplicate of this ModelMBeanOperationInfo.

**Overrides:** clone

in class

MBeanOperationInfo
**Returns:** a clone of this instance.
**See Also:** Cloneable

- getDescriptor

```java
public
Descriptor
getDescriptor()
```

Returns a copy of the associated Descriptor of the
ModelMBeanOperationInfo.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Overrides:** getDescriptor

in class

MBeanFeatureInfo
**Returns:** Descriptor associated with the
ModelMBeanOperationInfo object.
**See Also:** setDescriptor(javax.management.Descriptor)

- setDescriptor

```java
public void setDescriptor​(
Descriptor
inDescriptor)
```

Sets associated Descriptor (full replace) for the
ModelMBeanOperationInfo If the new Descriptor is null, then
the associated Descriptor reverts to a default descriptor.
The Descriptor is validated before it is assigned. If the
new Descriptor is invalid, then a
RuntimeOperationsException wrapping an
IllegalArgumentException is thrown.

**Specified by:** setDescriptor

in interface

DescriptorAccess
**Parameters:** inDescriptor

- replaces the Descriptor associated with the
ModelMBeanOperation.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException for invalid Descriptor.
**See Also:** getDescriptor()

- toString

```java
public
String
toString()
```

Returns a string containing the entire contents of the
ModelMBeanOperationInfo in human readable form.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- ModelMBeanOperationInfo

```java
public ModelMBeanOperationInfo​(
String
description,

Method
operationMethod)
```

Constructs a ModelMBeanOperationInfo object with a default
descriptor. The

Descriptor

of the constructed
object will include fields contributed by any annotations
on the

Method

object that contain the

DescriptorKey

meta-annotation.

**Parameters:** operationMethod

- The java.lang.reflect.Method object
describing the MBean operation.
**Parameters:** description

- A human readable description of the operation.

- ModelMBeanOperationInfo

```java
public ModelMBeanOperationInfo​(
String
description,

Method
operationMethod,

Descriptor
descriptor)
```

Constructs a ModelMBeanOperationInfo object. The

Descriptor

of the constructed object will include fields
contributed by any annotations on the

Method

object
that contain the

DescriptorKey

meta-annotation.

**Parameters:** operationMethod

- The java.lang.reflect.Method object
describing the MBean operation.
**Parameters:** description

- A human readable description of the
operation.
**Parameters:** descriptor

- An instance of Descriptor containing the
appropriate metadata for this instance of the
ModelMBeanOperationInfo. If it is null a default
descriptor will be created. If the descriptor does not
contain the fields
"displayName" or "role", the missing ones are added with
their default values.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid; or
descriptor field "name" is not equal to
operation name; or descriptor field "DescriptorType" is
not equal to "operation"; or descriptor
optional field "role" is present but not equal to "operation",
"getter", or "setter".

- ModelMBeanOperationInfo

```java
public ModelMBeanOperationInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

String
type,
int impact)
```

Constructs a ModelMBeanOperationInfo object with a default descriptor.

**Parameters:** name

- The name of the method.
**Parameters:** description

- A human readable description of the operation.
**Parameters:** signature

- MBeanParameterInfo objects describing the
parameters(arguments) of the method.
**Parameters:** type

- The type of the method's return value.
**Parameters:** impact

- The impact of the method, one of INFO, ACTION,
ACTION_INFO, UNKNOWN.

- ModelMBeanOperationInfo

```java
public ModelMBeanOperationInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

String
type,
int impact,

Descriptor
descriptor)
```

Constructs a ModelMBeanOperationInfo object.

**Parameters:** name

- The name of the method.
**Parameters:** description

- A human readable description of the operation.
**Parameters:** signature

- MBeanParameterInfo objects describing the
parameters(arguments) of the method.
**Parameters:** type

- The type of the method's return value.
**Parameters:** impact

- The impact of the method, one of INFO, ACTION,
ACTION_INFO, UNKNOWN.
**Parameters:** descriptor

- An instance of Descriptor containing the
appropriate metadata for this instance of the
MBeanOperationInfo. If it is null then a default descriptor
will be created. If the descriptor does not contain
fields "displayName" or "role",
the missing ones are added with their default values.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid; or
descriptor field "name" is not equal to
operation name; or descriptor field "DescriptorType" is
not equal to "operation"; or descriptor optional
field "role" is present but not equal to "operation", "getter", or
"setter".

- ModelMBeanOperationInfo

```java
public ModelMBeanOperationInfo​(
ModelMBeanOperationInfo
inInfo)
```

Constructs a new ModelMBeanOperationInfo object from this
ModelMBeanOperation Object.

**Parameters:** inInfo

- the ModelMBeanOperationInfo to be duplicated

---

#### Constructor Detail

ModelMBeanOperationInfo

```java
public ModelMBeanOperationInfo​(
String
description,

Method
operationMethod)
```

Constructs a ModelMBeanOperationInfo object with a default
descriptor. The

Descriptor

of the constructed
object will include fields contributed by any annotations
on the

Method

object that contain the

DescriptorKey

meta-annotation.

**Parameters:** operationMethod

- The java.lang.reflect.Method object
describing the MBean operation.
**Parameters:** description

- A human readable description of the operation.

---

#### ModelMBeanOperationInfo

public ModelMBeanOperationInfo​(

String

description,

Method

operationMethod)

Constructs a ModelMBeanOperationInfo object with a default
descriptor. The

Descriptor

of the constructed
object will include fields contributed by any annotations
on the

Method

object that contain the

DescriptorKey

meta-annotation.

ModelMBeanOperationInfo

```java
public ModelMBeanOperationInfo​(
String
description,

Method
operationMethod,

Descriptor
descriptor)
```

Constructs a ModelMBeanOperationInfo object. The

Descriptor

of the constructed object will include fields
contributed by any annotations on the

Method

object
that contain the

DescriptorKey

meta-annotation.

**Parameters:** operationMethod

- The java.lang.reflect.Method object
describing the MBean operation.
**Parameters:** description

- A human readable description of the
operation.
**Parameters:** descriptor

- An instance of Descriptor containing the
appropriate metadata for this instance of the
ModelMBeanOperationInfo. If it is null a default
descriptor will be created. If the descriptor does not
contain the fields
"displayName" or "role", the missing ones are added with
their default values.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid; or
descriptor field "name" is not equal to
operation name; or descriptor field "DescriptorType" is
not equal to "operation"; or descriptor
optional field "role" is present but not equal to "operation",
"getter", or "setter".

---

#### ModelMBeanOperationInfo

public ModelMBeanOperationInfo​(

String

description,

Method

operationMethod,

Descriptor

descriptor)

Constructs a ModelMBeanOperationInfo object. The

Descriptor

of the constructed object will include fields
contributed by any annotations on the

Method

object
that contain the

DescriptorKey

meta-annotation.

ModelMBeanOperationInfo

```java
public ModelMBeanOperationInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

String
type,
int impact)
```

Constructs a ModelMBeanOperationInfo object with a default descriptor.

**Parameters:** name

- The name of the method.
**Parameters:** description

- A human readable description of the operation.
**Parameters:** signature

- MBeanParameterInfo objects describing the
parameters(arguments) of the method.
**Parameters:** type

- The type of the method's return value.
**Parameters:** impact

- The impact of the method, one of INFO, ACTION,
ACTION_INFO, UNKNOWN.

---

#### ModelMBeanOperationInfo

public ModelMBeanOperationInfo​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

String

type,
int impact)

Constructs a ModelMBeanOperationInfo object with a default descriptor.

ModelMBeanOperationInfo

```java
public ModelMBeanOperationInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

String
type,
int impact,

Descriptor
descriptor)
```

Constructs a ModelMBeanOperationInfo object.

**Parameters:** name

- The name of the method.
**Parameters:** description

- A human readable description of the operation.
**Parameters:** signature

- MBeanParameterInfo objects describing the
parameters(arguments) of the method.
**Parameters:** type

- The type of the method's return value.
**Parameters:** impact

- The impact of the method, one of INFO, ACTION,
ACTION_INFO, UNKNOWN.
**Parameters:** descriptor

- An instance of Descriptor containing the
appropriate metadata for this instance of the
MBeanOperationInfo. If it is null then a default descriptor
will be created. If the descriptor does not contain
fields "displayName" or "role",
the missing ones are added with their default values.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid; or
descriptor field "name" is not equal to
operation name; or descriptor field "DescriptorType" is
not equal to "operation"; or descriptor optional
field "role" is present but not equal to "operation", "getter", or
"setter".

---

#### ModelMBeanOperationInfo

public ModelMBeanOperationInfo​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

String

type,
int impact,

Descriptor

descriptor)

Constructs a ModelMBeanOperationInfo object.

ModelMBeanOperationInfo

```java
public ModelMBeanOperationInfo​(
ModelMBeanOperationInfo
inInfo)
```

Constructs a new ModelMBeanOperationInfo object from this
ModelMBeanOperation Object.

**Parameters:** inInfo

- the ModelMBeanOperationInfo to be duplicated

---

#### ModelMBeanOperationInfo

public ModelMBeanOperationInfo​(

ModelMBeanOperationInfo

inInfo)

Constructs a new ModelMBeanOperationInfo object from this
ModelMBeanOperation Object.

Method Detail

- clone

```java
public
Object
clone()
```

Creates and returns a new ModelMBeanOperationInfo which is a
duplicate of this ModelMBeanOperationInfo.

**Overrides:** clone

in class

MBeanOperationInfo
**Returns:** a clone of this instance.
**See Also:** Cloneable

- getDescriptor

```java
public
Descriptor
getDescriptor()
```

Returns a copy of the associated Descriptor of the
ModelMBeanOperationInfo.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Overrides:** getDescriptor

in class

MBeanFeatureInfo
**Returns:** Descriptor associated with the
ModelMBeanOperationInfo object.
**See Also:** setDescriptor(javax.management.Descriptor)

- setDescriptor

```java
public void setDescriptor​(
Descriptor
inDescriptor)
```

Sets associated Descriptor (full replace) for the
ModelMBeanOperationInfo If the new Descriptor is null, then
the associated Descriptor reverts to a default descriptor.
The Descriptor is validated before it is assigned. If the
new Descriptor is invalid, then a
RuntimeOperationsException wrapping an
IllegalArgumentException is thrown.

**Specified by:** setDescriptor

in interface

DescriptorAccess
**Parameters:** inDescriptor

- replaces the Descriptor associated with the
ModelMBeanOperation.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException for invalid Descriptor.
**See Also:** getDescriptor()

- toString

```java
public
String
toString()
```

Returns a string containing the entire contents of the
ModelMBeanOperationInfo in human readable form.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

clone

```java
public
Object
clone()
```

Creates and returns a new ModelMBeanOperationInfo which is a
duplicate of this ModelMBeanOperationInfo.

**Overrides:** clone

in class

MBeanOperationInfo
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Creates and returns a new ModelMBeanOperationInfo which is a
duplicate of this ModelMBeanOperationInfo.

getDescriptor

```java
public
Descriptor
getDescriptor()
```

Returns a copy of the associated Descriptor of the
ModelMBeanOperationInfo.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Overrides:** getDescriptor

in class

MBeanFeatureInfo
**Returns:** Descriptor associated with the
ModelMBeanOperationInfo object.
**See Also:** setDescriptor(javax.management.Descriptor)

---

#### getDescriptor

public

Descriptor

getDescriptor()

Returns a copy of the associated Descriptor of the
ModelMBeanOperationInfo.

setDescriptor

```java
public void setDescriptor​(
Descriptor
inDescriptor)
```

Sets associated Descriptor (full replace) for the
ModelMBeanOperationInfo If the new Descriptor is null, then
the associated Descriptor reverts to a default descriptor.
The Descriptor is validated before it is assigned. If the
new Descriptor is invalid, then a
RuntimeOperationsException wrapping an
IllegalArgumentException is thrown.

**Specified by:** setDescriptor

in interface

DescriptorAccess
**Parameters:** inDescriptor

- replaces the Descriptor associated with the
ModelMBeanOperation.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException for invalid Descriptor.
**See Also:** getDescriptor()

---

#### setDescriptor

public void setDescriptor​(

Descriptor

inDescriptor)

Sets associated Descriptor (full replace) for the
ModelMBeanOperationInfo If the new Descriptor is null, then
the associated Descriptor reverts to a default descriptor.
The Descriptor is validated before it is assigned. If the
new Descriptor is invalid, then a
RuntimeOperationsException wrapping an
IllegalArgumentException is thrown.

toString

```java
public
String
toString()
```

Returns a string containing the entire contents of the
ModelMBeanOperationInfo in human readable form.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a string containing the entire contents of the
ModelMBeanOperationInfo in human readable form.

---

