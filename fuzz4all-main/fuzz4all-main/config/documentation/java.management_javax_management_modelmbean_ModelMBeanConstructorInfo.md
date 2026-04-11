# Class ModelMBeanConstructorInfo

**Source:** `java.management\javax\management\modelmbean\ModelMBeanConstructorInfo.html`

### Class Description

```java
public class
ModelMBeanConstructorInfo

extends
MBeanConstructorInfo

implements
DescriptorAccess
```

The ModelMBeanConstructorInfo object describes a constructor of the ModelMBean.
It is a subclass of MBeanConstructorInfo with the addition of an associated Descriptor
and an implementation of the DescriptorAccess interface.

The fields in the descriptor are defined, but not limited to, the following.
Note that when the Type in this table is Number, a String that is the decimal
representation of a Long can also be used.

ModelMBeanConstructorInfo Fields

Name

Type

Meaning

name

String

Constructor name.

descriptorType

String

Must be "operation".

role

String

Must be "constructor".

displayName

String

Human readable name of constructor.

visibility

Number

1-4 where 1: always visible 4: rarely visible.

presentationString

String

XML formatted string to describe how to present operation

The

persistPolicy

and

currencyTimeLimit

fields
are meaningless for constructors, but are not considered invalid.

The default descriptor will have the

name

,

descriptorType

,

displayName

and

role

fields.

The

serialVersionUID

of this class is

3862947819818064362L

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

#### public ModelMBeanConstructorInfo​(
String
description,

Constructor
<?> constructorMethod)

Constructs a ModelMBeanConstructorInfo object with a default
descriptor. The

Descriptor

of the constructed
object will include fields contributed by any annotations on
the

Constructor

object that contain the

DescriptorKey

meta-annotation.

**Parameters:**
- description

- A human readable description of the constructor.
- constructorMethod

- The java.lang.reflect.Constructor object
describing the MBean constructor.

---

#### public ModelMBeanConstructorInfo​(
String
description,

Constructor
<?> constructorMethod,

Descriptor
descriptor)

Constructs a ModelMBeanConstructorInfo object. The

Descriptor

of the constructed object will include fields
contributed by any annotations on the

Constructor

object that contain the

DescriptorKey

meta-annotation.

**Parameters:**
- description

- A human readable description of the constructor.
- constructorMethod

- The java.lang.reflect.Constructor object
describing the ModelMBean constructor.
- descriptor

- An instance of Descriptor containing the
appropriate metadata for this instance of the
ModelMBeanConstructorInfo. If it is null, then a default
descriptor will be created. If the descriptor does not
contain the field "displayName" this field is added in the
descriptor with its default value.

**Throws:**
- RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid, or
descriptor field "name" is not equal to name
parameter, or descriptor field "descriptorType" is
not equal to "operation" or descriptor field "role" is
present but not equal to "constructor".

---

#### public ModelMBeanConstructorInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature)

Constructs a ModelMBeanConstructorInfo object with a default descriptor.

**Parameters:**
- name

- The name of the constructor.
- description

- A human readable description of the constructor.
- signature

- MBeanParameterInfo object array describing the parameters(arguments) of the constructor.

---

#### public ModelMBeanConstructorInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

Descriptor
descriptor)

Constructs a ModelMBeanConstructorInfo object.

**Parameters:**
- name

- The name of the constructor.
- description

- A human readable description of the constructor.
- signature

- MBeanParameterInfo objects describing the parameters(arguments) of the constructor.
- descriptor

- An instance of Descriptor containing the appropriate metadata
for this instance of the MBeanConstructorInfo. If it is null then a default descriptor will be created.
If the descriptor does not contain the field "displayName" this field
is added in the descriptor with its default value.

**Throws:**
- RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid, or
descriptor field "name" is not equal to name
parameter, or descriptor field "descriptorType" is
not equal to "operation" or descriptor field "role" is
present but not equal to "constructor".

---

### Method Details

#### public
Object
clone()

Creates and returns a new ModelMBeanConstructorInfo which is a duplicate of this ModelMBeanConstructorInfo.

**Overrides:**
- clone

in class

MBeanConstructorInfo

**Returns:**
- a clone of this instance.

**See Also:**
- Cloneable

---

#### public
Descriptor
getDescriptor()

Returns a copy of the associated Descriptor.

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
ModelMBeanConstructorInfo object.

**See Also:**
- setDescriptor(javax.management.Descriptor)

---

#### public void setDescriptor​(
Descriptor
inDescriptor)

Sets associated Descriptor (full replace) of
ModelMBeanConstructorInfo. If the new Descriptor is null,
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

- replaces the Descriptor associated with
the ModelMBeanConstructor. If the descriptor does not
contain all the following fields, the missing ones are added with
their default values: displayName, name, role, descriptorType.

**Throws:**
- RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid, or
descriptor field "name" is present but not equal to name
parameter, or descriptor field "descriptorType" is present
but not equal to "operation" or descriptor field "role" is
present but not equal to "constructor".

**See Also:**
- getDescriptor()

---

#### public
String
toString()

Returns a string containing the entire contents of the ModelMBeanConstructorInfo in human readable form.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class ModelMBeanConstructorInfo

java.lang.Object

- javax.management.MBeanFeatureInfo
- - javax.management.MBeanConstructorInfo
- - javax.management.modelmbean.ModelMBeanConstructorInfo

javax.management.MBeanFeatureInfo

- javax.management.MBeanConstructorInfo
- - javax.management.modelmbean.ModelMBeanConstructorInfo

javax.management.MBeanConstructorInfo

- javax.management.modelmbean.ModelMBeanConstructorInfo

javax.management.modelmbean.ModelMBeanConstructorInfo

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorAccess

,

DescriptorRead

```java
public class
ModelMBeanConstructorInfo

extends
MBeanConstructorInfo

implements
DescriptorAccess
```

The ModelMBeanConstructorInfo object describes a constructor of the ModelMBean.
It is a subclass of MBeanConstructorInfo with the addition of an associated Descriptor
and an implementation of the DescriptorAccess interface.

The fields in the descriptor are defined, but not limited to, the following.
Note that when the Type in this table is Number, a String that is the decimal
representation of a Long can also be used.

ModelMBeanConstructorInfo Fields

Name

Type

Meaning

name

String

Constructor name.

descriptorType

String

Must be "operation".

role

String

Must be "constructor".

displayName

String

Human readable name of constructor.

visibility

Number

1-4 where 1: always visible 4: rarely visible.

presentationString

String

XML formatted string to describe how to present operation

The

persistPolicy

and

currencyTimeLimit

fields
are meaningless for constructors, but are not considered invalid.

The default descriptor will have the

name

,

descriptorType

,

displayName

and

role

fields.

The

serialVersionUID

of this class is

3862947819818064362L

.

**Since:** 1.5
**See Also:** Serialized Form

public class

ModelMBeanConstructorInfo

extends

MBeanConstructorInfo

implements

DescriptorAccess

The ModelMBeanConstructorInfo object describes a constructor of the ModelMBean.
It is a subclass of MBeanConstructorInfo with the addition of an associated Descriptor
and an implementation of the DescriptorAccess interface.

The fields in the descriptor are defined, but not limited to, the following.
Note that when the Type in this table is Number, a String that is the decimal
representation of a Long can also be used.

ModelMBeanConstructorInfo Fields

Name

Type

Meaning

name

String

Constructor name.

descriptorType

String

Must be "operation".

role

String

Must be "constructor".

displayName

String

Human readable name of constructor.

visibility

Number

1-4 where 1: always visible 4: rarely visible.

presentationString

String

XML formatted string to describe how to present operation

The

persistPolicy

and

currencyTimeLimit

fields
are meaningless for constructors, but are not considered invalid.

The default descriptor will have the

name

,

descriptorType

,

displayName

and

role

fields.

The

serialVersionUID

of this class is

3862947819818064362L

.

The ModelMBeanConstructorInfo object describes a constructor of the ModelMBean.
It is a subclass of MBeanConstructorInfo with the addition of an associated Descriptor
and an implementation of the DescriptorAccess interface.

The fields in the descriptor are defined, but not limited to, the following.
Note that when the Type in this table is Number, a String that is the decimal
representation of a Long can also be used.

The

persistPolicy

and

currencyTimeLimit

fields
are meaningless for constructors, but are not considered invalid.

The default descriptor will have the

name

,

descriptorType

,

displayName

and

role

fields.

The

serialVersionUID

of this class is

3862947819818064362L

.

The

serialVersionUID

of this class is

3862947819818064362L

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

ModelMBeanConstructorInfo

​(

String

description,

Constructor

<?> constructorMethod)

Constructs a ModelMBeanConstructorInfo object with a default
descriptor.

ModelMBeanConstructorInfo

​(

String

description,

Constructor

<?> constructorMethod,

Descriptor

descriptor)

Constructs a ModelMBeanConstructorInfo object.

ModelMBeanConstructorInfo

​(

String

name,

String

description,

MBeanParameterInfo

[] signature)

Constructs a ModelMBeanConstructorInfo object with a default descriptor.

ModelMBeanConstructorInfo

​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

Descriptor

descriptor)

Constructs a ModelMBeanConstructorInfo object.

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

Creates and returns a new ModelMBeanConstructorInfo which is a duplicate of this ModelMBeanConstructorInfo.

Descriptor

getDescriptor

()

Returns a copy of the associated Descriptor.

void

setDescriptor

​(

Descriptor

inDescriptor)

Sets associated Descriptor (full replace) of
ModelMBeanConstructorInfo.

String

toString

()

Returns a string containing the entire contents of the ModelMBeanConstructorInfo in human readable form.

- Methods declared in class javax.management.

MBeanConstructorInfo

equals

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

ModelMBeanConstructorInfo

​(

String

description,

Constructor

<?> constructorMethod)

Constructs a ModelMBeanConstructorInfo object with a default
descriptor.

ModelMBeanConstructorInfo

​(

String

description,

Constructor

<?> constructorMethod,

Descriptor

descriptor)

Constructs a ModelMBeanConstructorInfo object.

ModelMBeanConstructorInfo

​(

String

name,

String

description,

MBeanParameterInfo

[] signature)

Constructs a ModelMBeanConstructorInfo object with a default descriptor.

ModelMBeanConstructorInfo

​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

Descriptor

descriptor)

Constructs a ModelMBeanConstructorInfo object.

---

#### Constructor Summary

Constructs a ModelMBeanConstructorInfo object with a default
descriptor.

Constructs a ModelMBeanConstructorInfo object.

Constructs a ModelMBeanConstructorInfo object with a default descriptor.

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

Creates and returns a new ModelMBeanConstructorInfo which is a duplicate of this ModelMBeanConstructorInfo.

Descriptor

getDescriptor

()

Returns a copy of the associated Descriptor.

void

setDescriptor

​(

Descriptor

inDescriptor)

Sets associated Descriptor (full replace) of
ModelMBeanConstructorInfo.

String

toString

()

Returns a string containing the entire contents of the ModelMBeanConstructorInfo in human readable form.

- Methods declared in class javax.management.

MBeanConstructorInfo

equals

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

Creates and returns a new ModelMBeanConstructorInfo which is a duplicate of this ModelMBeanConstructorInfo.

Returns a copy of the associated Descriptor.

Sets associated Descriptor (full replace) of
ModelMBeanConstructorInfo.

Returns a string containing the entire contents of the ModelMBeanConstructorInfo in human readable form.

Methods declared in class javax.management.

MBeanConstructorInfo

equals

,

getSignature

---

#### Methods declared in class javax.management. MBeanConstructorInfo

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

- ModelMBeanConstructorInfo

```java
public ModelMBeanConstructorInfo​(
String
description,

Constructor
<?> constructorMethod)
```

Constructs a ModelMBeanConstructorInfo object with a default
descriptor. The

Descriptor

of the constructed
object will include fields contributed by any annotations on
the

Constructor

object that contain the

DescriptorKey

meta-annotation.

**Parameters:** description

- A human readable description of the constructor.
**Parameters:** constructorMethod

- The java.lang.reflect.Constructor object
describing the MBean constructor.

- ModelMBeanConstructorInfo

```java
public ModelMBeanConstructorInfo​(
String
description,

Constructor
<?> constructorMethod,

Descriptor
descriptor)
```

Constructs a ModelMBeanConstructorInfo object. The

Descriptor

of the constructed object will include fields
contributed by any annotations on the

Constructor

object that contain the

DescriptorKey

meta-annotation.

**Parameters:** description

- A human readable description of the constructor.
**Parameters:** constructorMethod

- The java.lang.reflect.Constructor object
describing the ModelMBean constructor.
**Parameters:** descriptor

- An instance of Descriptor containing the
appropriate metadata for this instance of the
ModelMBeanConstructorInfo. If it is null, then a default
descriptor will be created. If the descriptor does not
contain the field "displayName" this field is added in the
descriptor with its default value.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid, or
descriptor field "name" is not equal to name
parameter, or descriptor field "descriptorType" is
not equal to "operation" or descriptor field "role" is
present but not equal to "constructor".

- ModelMBeanConstructorInfo

```java
public ModelMBeanConstructorInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature)
```

Constructs a ModelMBeanConstructorInfo object with a default descriptor.

**Parameters:** name

- The name of the constructor.
**Parameters:** description

- A human readable description of the constructor.
**Parameters:** signature

- MBeanParameterInfo object array describing the parameters(arguments) of the constructor.

- ModelMBeanConstructorInfo

```java
public ModelMBeanConstructorInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

Descriptor
descriptor)
```

Constructs a ModelMBeanConstructorInfo object.

**Parameters:** name

- The name of the constructor.
**Parameters:** description

- A human readable description of the constructor.
**Parameters:** signature

- MBeanParameterInfo objects describing the parameters(arguments) of the constructor.
**Parameters:** descriptor

- An instance of Descriptor containing the appropriate metadata
for this instance of the MBeanConstructorInfo. If it is null then a default descriptor will be created.
If the descriptor does not contain the field "displayName" this field
is added in the descriptor with its default value.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid, or
descriptor field "name" is not equal to name
parameter, or descriptor field "descriptorType" is
not equal to "operation" or descriptor field "role" is
present but not equal to "constructor".

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
public
Object
clone()
```

Creates and returns a new ModelMBeanConstructorInfo which is a duplicate of this ModelMBeanConstructorInfo.

**Overrides:** clone

in class

MBeanConstructorInfo
**Returns:** a clone of this instance.
**See Also:** Cloneable

- getDescriptor

```java
public
Descriptor
getDescriptor()
```

Returns a copy of the associated Descriptor.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Overrides:** getDescriptor

in class

MBeanFeatureInfo
**Returns:** Descriptor associated with the
ModelMBeanConstructorInfo object.
**See Also:** setDescriptor(javax.management.Descriptor)

- setDescriptor

```java
public void setDescriptor​(
Descriptor
inDescriptor)
```

Sets associated Descriptor (full replace) of
ModelMBeanConstructorInfo. If the new Descriptor is null,
then the associated Descriptor reverts to a default
descriptor. The Descriptor is validated before it is
assigned. If the new Descriptor is invalid, then a
RuntimeOperationsException wrapping an
IllegalArgumentException is thrown.

**Specified by:** setDescriptor

in interface

DescriptorAccess
**Parameters:** inDescriptor

- replaces the Descriptor associated with
the ModelMBeanConstructor. If the descriptor does not
contain all the following fields, the missing ones are added with
their default values: displayName, name, role, descriptorType.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid, or
descriptor field "name" is present but not equal to name
parameter, or descriptor field "descriptorType" is present
but not equal to "operation" or descriptor field "role" is
present but not equal to "constructor".
**See Also:** getDescriptor()

- toString

```java
public
String
toString()
```

Returns a string containing the entire contents of the ModelMBeanConstructorInfo in human readable form.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- ModelMBeanConstructorInfo

```java
public ModelMBeanConstructorInfo​(
String
description,

Constructor
<?> constructorMethod)
```

Constructs a ModelMBeanConstructorInfo object with a default
descriptor. The

Descriptor

of the constructed
object will include fields contributed by any annotations on
the

Constructor

object that contain the

DescriptorKey

meta-annotation.

**Parameters:** description

- A human readable description of the constructor.
**Parameters:** constructorMethod

- The java.lang.reflect.Constructor object
describing the MBean constructor.

- ModelMBeanConstructorInfo

```java
public ModelMBeanConstructorInfo​(
String
description,

Constructor
<?> constructorMethod,

Descriptor
descriptor)
```

Constructs a ModelMBeanConstructorInfo object. The

Descriptor

of the constructed object will include fields
contributed by any annotations on the

Constructor

object that contain the

DescriptorKey

meta-annotation.

**Parameters:** description

- A human readable description of the constructor.
**Parameters:** constructorMethod

- The java.lang.reflect.Constructor object
describing the ModelMBean constructor.
**Parameters:** descriptor

- An instance of Descriptor containing the
appropriate metadata for this instance of the
ModelMBeanConstructorInfo. If it is null, then a default
descriptor will be created. If the descriptor does not
contain the field "displayName" this field is added in the
descriptor with its default value.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid, or
descriptor field "name" is not equal to name
parameter, or descriptor field "descriptorType" is
not equal to "operation" or descriptor field "role" is
present but not equal to "constructor".

- ModelMBeanConstructorInfo

```java
public ModelMBeanConstructorInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature)
```

Constructs a ModelMBeanConstructorInfo object with a default descriptor.

**Parameters:** name

- The name of the constructor.
**Parameters:** description

- A human readable description of the constructor.
**Parameters:** signature

- MBeanParameterInfo object array describing the parameters(arguments) of the constructor.

- ModelMBeanConstructorInfo

```java
public ModelMBeanConstructorInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

Descriptor
descriptor)
```

Constructs a ModelMBeanConstructorInfo object.

**Parameters:** name

- The name of the constructor.
**Parameters:** description

- A human readable description of the constructor.
**Parameters:** signature

- MBeanParameterInfo objects describing the parameters(arguments) of the constructor.
**Parameters:** descriptor

- An instance of Descriptor containing the appropriate metadata
for this instance of the MBeanConstructorInfo. If it is null then a default descriptor will be created.
If the descriptor does not contain the field "displayName" this field
is added in the descriptor with its default value.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid, or
descriptor field "name" is not equal to name
parameter, or descriptor field "descriptorType" is
not equal to "operation" or descriptor field "role" is
present but not equal to "constructor".

---

#### Constructor Detail

ModelMBeanConstructorInfo

```java
public ModelMBeanConstructorInfo​(
String
description,

Constructor
<?> constructorMethod)
```

Constructs a ModelMBeanConstructorInfo object with a default
descriptor. The

Descriptor

of the constructed
object will include fields contributed by any annotations on
the

Constructor

object that contain the

DescriptorKey

meta-annotation.

**Parameters:** description

- A human readable description of the constructor.
**Parameters:** constructorMethod

- The java.lang.reflect.Constructor object
describing the MBean constructor.

---

#### ModelMBeanConstructorInfo

public ModelMBeanConstructorInfo​(

String

description,

Constructor

<?> constructorMethod)

Constructs a ModelMBeanConstructorInfo object with a default
descriptor. The

Descriptor

of the constructed
object will include fields contributed by any annotations on
the

Constructor

object that contain the

DescriptorKey

meta-annotation.

ModelMBeanConstructorInfo

```java
public ModelMBeanConstructorInfo​(
String
description,

Constructor
<?> constructorMethod,

Descriptor
descriptor)
```

Constructs a ModelMBeanConstructorInfo object. The

Descriptor

of the constructed object will include fields
contributed by any annotations on the

Constructor

object that contain the

DescriptorKey

meta-annotation.

**Parameters:** description

- A human readable description of the constructor.
**Parameters:** constructorMethod

- The java.lang.reflect.Constructor object
describing the ModelMBean constructor.
**Parameters:** descriptor

- An instance of Descriptor containing the
appropriate metadata for this instance of the
ModelMBeanConstructorInfo. If it is null, then a default
descriptor will be created. If the descriptor does not
contain the field "displayName" this field is added in the
descriptor with its default value.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid, or
descriptor field "name" is not equal to name
parameter, or descriptor field "descriptorType" is
not equal to "operation" or descriptor field "role" is
present but not equal to "constructor".

---

#### ModelMBeanConstructorInfo

public ModelMBeanConstructorInfo​(

String

description,

Constructor

<?> constructorMethod,

Descriptor

descriptor)

Constructs a ModelMBeanConstructorInfo object. The

Descriptor

of the constructed object will include fields
contributed by any annotations on the

Constructor

object that contain the

DescriptorKey

meta-annotation.

ModelMBeanConstructorInfo

```java
public ModelMBeanConstructorInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature)
```

Constructs a ModelMBeanConstructorInfo object with a default descriptor.

**Parameters:** name

- The name of the constructor.
**Parameters:** description

- A human readable description of the constructor.
**Parameters:** signature

- MBeanParameterInfo object array describing the parameters(arguments) of the constructor.

---

#### ModelMBeanConstructorInfo

public ModelMBeanConstructorInfo​(

String

name,

String

description,

MBeanParameterInfo

[] signature)

Constructs a ModelMBeanConstructorInfo object with a default descriptor.

ModelMBeanConstructorInfo

```java
public ModelMBeanConstructorInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

Descriptor
descriptor)
```

Constructs a ModelMBeanConstructorInfo object.

**Parameters:** name

- The name of the constructor.
**Parameters:** description

- A human readable description of the constructor.
**Parameters:** signature

- MBeanParameterInfo objects describing the parameters(arguments) of the constructor.
**Parameters:** descriptor

- An instance of Descriptor containing the appropriate metadata
for this instance of the MBeanConstructorInfo. If it is null then a default descriptor will be created.
If the descriptor does not contain the field "displayName" this field
is added in the descriptor with its default value.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid, or
descriptor field "name" is not equal to name
parameter, or descriptor field "descriptorType" is
not equal to "operation" or descriptor field "role" is
present but not equal to "constructor".

---

#### ModelMBeanConstructorInfo

public ModelMBeanConstructorInfo​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

Descriptor

descriptor)

Constructs a ModelMBeanConstructorInfo object.

Method Detail

- clone

```java
public
Object
clone()
```

Creates and returns a new ModelMBeanConstructorInfo which is a duplicate of this ModelMBeanConstructorInfo.

**Overrides:** clone

in class

MBeanConstructorInfo
**Returns:** a clone of this instance.
**See Also:** Cloneable

- getDescriptor

```java
public
Descriptor
getDescriptor()
```

Returns a copy of the associated Descriptor.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Overrides:** getDescriptor

in class

MBeanFeatureInfo
**Returns:** Descriptor associated with the
ModelMBeanConstructorInfo object.
**See Also:** setDescriptor(javax.management.Descriptor)

- setDescriptor

```java
public void setDescriptor​(
Descriptor
inDescriptor)
```

Sets associated Descriptor (full replace) of
ModelMBeanConstructorInfo. If the new Descriptor is null,
then the associated Descriptor reverts to a default
descriptor. The Descriptor is validated before it is
assigned. If the new Descriptor is invalid, then a
RuntimeOperationsException wrapping an
IllegalArgumentException is thrown.

**Specified by:** setDescriptor

in interface

DescriptorAccess
**Parameters:** inDescriptor

- replaces the Descriptor associated with
the ModelMBeanConstructor. If the descriptor does not
contain all the following fields, the missing ones are added with
their default values: displayName, name, role, descriptorType.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid, or
descriptor field "name" is present but not equal to name
parameter, or descriptor field "descriptorType" is present
but not equal to "operation" or descriptor field "role" is
present but not equal to "constructor".
**See Also:** getDescriptor()

- toString

```java
public
String
toString()
```

Returns a string containing the entire contents of the ModelMBeanConstructorInfo in human readable form.

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

Creates and returns a new ModelMBeanConstructorInfo which is a duplicate of this ModelMBeanConstructorInfo.

**Overrides:** clone

in class

MBeanConstructorInfo
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Creates and returns a new ModelMBeanConstructorInfo which is a duplicate of this ModelMBeanConstructorInfo.

getDescriptor

```java
public
Descriptor
getDescriptor()
```

Returns a copy of the associated Descriptor.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Overrides:** getDescriptor

in class

MBeanFeatureInfo
**Returns:** Descriptor associated with the
ModelMBeanConstructorInfo object.
**See Also:** setDescriptor(javax.management.Descriptor)

---

#### getDescriptor

public

Descriptor

getDescriptor()

Returns a copy of the associated Descriptor.

setDescriptor

```java
public void setDescriptor​(
Descriptor
inDescriptor)
```

Sets associated Descriptor (full replace) of
ModelMBeanConstructorInfo. If the new Descriptor is null,
then the associated Descriptor reverts to a default
descriptor. The Descriptor is validated before it is
assigned. If the new Descriptor is invalid, then a
RuntimeOperationsException wrapping an
IllegalArgumentException is thrown.

**Specified by:** setDescriptor

in interface

DescriptorAccess
**Parameters:** inDescriptor

- replaces the Descriptor associated with
the ModelMBeanConstructor. If the descriptor does not
contain all the following fields, the missing ones are added with
their default values: displayName, name, role, descriptorType.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException. The descriptor is invalid, or
descriptor field "name" is present but not equal to name
parameter, or descriptor field "descriptorType" is present
but not equal to "operation" or descriptor field "role" is
present but not equal to "constructor".
**See Also:** getDescriptor()

---

#### setDescriptor

public void setDescriptor​(

Descriptor

inDescriptor)

Sets associated Descriptor (full replace) of
ModelMBeanConstructorInfo. If the new Descriptor is null,
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

Returns a string containing the entire contents of the ModelMBeanConstructorInfo in human readable form.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a string containing the entire contents of the ModelMBeanConstructorInfo in human readable form.

---

