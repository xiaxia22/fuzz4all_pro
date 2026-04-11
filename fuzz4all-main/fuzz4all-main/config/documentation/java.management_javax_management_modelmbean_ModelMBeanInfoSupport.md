# Class ModelMBeanInfoSupport

**Source:** `java.management\javax\management\modelmbean\ModelMBeanInfoSupport.html`

### Class Description

```java
public class
ModelMBeanInfoSupport

extends
MBeanInfo

implements
ModelMBeanInfo
```

This class represents the meta data for ModelMBeans. Descriptors have been
added on the meta data objects.

Java resources wishing to be manageable instantiate the ModelMBean using the
MBeanServer's createMBean method. The resource then sets the ModelMBeanInfo
and Descriptors for the ModelMBean instance. The attributes and operations
exposed via the ModelMBeanInfo for the ModelMBean are accessible
from MBeans, connectors/adaptors like other MBeans. Through the Descriptors,
values and methods in the managed application can be defined and mapped to
attributes and operations of the ModelMBean.
This mapping can be defined during development in a file or dynamically and
programmatically at runtime.

Every ModelMBean which is instantiated in the MBeanServer becomes manageable:
its attributes and operations
become remotely accessible through the connectors/adaptors connected to that
MBeanServer.
A Java object cannot be registered in the MBeanServer unless it is a JMX
compliant MBean.
By instantiating a ModelMBean, resources are guaranteed that the MBean is
valid.

MBeanException and RuntimeOperationsException must be thrown on every public
method. This allows for wrapping exceptions from distributed
communications (RMI, EJB, etc.)

The

serialVersionUID

of this class is

-1935722590756516193L

.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

,

ModelMBeanInfo

---

### Field Details

*No entries found.*

### Constructor Details

#### public ModelMBeanInfoSupport​(
ModelMBeanInfo
mbi)

Constructs a ModelMBeanInfoSupport which is a duplicate of the given
ModelMBeanInfo. The returned object is a shallow copy of the given
object. Neither the Descriptor nor the contained arrays
(

ModelMBeanAttributeInfo[]

etc) are cloned. This method is
chiefly of interest to modify the Descriptor of the returned instance
via

setDescriptor

without affecting the
Descriptor of the original object.

**Parameters:**
- mbi

- the ModelMBeanInfo instance from which the ModelMBeanInfo
being created is initialized.

---

#### public ModelMBeanInfoSupport​(
String
className,

String
description,

ModelMBeanAttributeInfo
[] attributes,

ModelMBeanConstructorInfo
[] constructors,

ModelMBeanOperationInfo
[] operations,

ModelMBeanNotificationInfo
[] notifications)

Creates a ModelMBeanInfoSupport with the provided information,
but the descriptor is a default.
The default descriptor is: name=className, descriptorType="mbean",
displayName=className, persistPolicy="never", log="F", visibility="1"

**Parameters:**
- className

- classname of the MBean
- description

- human readable description of the
ModelMBean
- attributes

- array of ModelMBeanAttributeInfo objects
which have descriptors
- constructors

- array of ModelMBeanConstructorInfo
objects which have descriptors
- operations

- array of ModelMBeanOperationInfo objects
which have descriptors
- notifications

- array of ModelMBeanNotificationInfo
objects which have descriptors

---

#### public ModelMBeanInfoSupport​(
String
className,

String
description,

ModelMBeanAttributeInfo
[] attributes,

ModelMBeanConstructorInfo
[] constructors,

ModelMBeanOperationInfo
[] operations,

ModelMBeanNotificationInfo
[] notifications,

Descriptor
mbeandescriptor)

Creates a ModelMBeanInfoSupport with the provided information
and the descriptor given in parameter.

**Parameters:**
- className

- classname of the MBean
- description

- human readable description of the
ModelMBean
- attributes

- array of ModelMBeanAttributeInfo objects
which have descriptors
- constructors

- array of ModelMBeanConstructorInfo
objects which have descriptor
- operations

- array of ModelMBeanOperationInfo objects
which have descriptor
- notifications

- array of ModelMBeanNotificationInfo
objects which have descriptor
- mbeandescriptor

- descriptor to be used as the
MBeanDescriptor containing MBean wide policy. If the
descriptor is null, a default descriptor will be constructed.
The default descriptor is:
name=className, descriptorType="mbean", displayName=className,
persistPolicy="never", log="F", visibility="1". If the descriptor
does not contain all of these fields, the missing ones are
added with these default values.

**Throws:**
- RuntimeOperationsException

- Wraps an
IllegalArgumentException for invalid descriptor passed in
parameter. (see

getMBeanDescriptor

for the definition of a valid MBean
descriptor.)

---

### Method Details

#### public
Object
clone()

Returns a shallow clone of this instance. Neither the Descriptor nor
the contained arrays (

ModelMBeanAttributeInfo[]

etc) are
cloned. This method is chiefly of interest to modify the Descriptor
of the clone via

setDescriptor

without affecting
the Descriptor of the original object.

**Specified by:**
- clone

in interface

ModelMBeanInfo

**Overrides:**
- clone

in class

MBeanInfo

**Returns:**
- a shallow clone of this instance.

**See Also:**
- Cloneable

---

#### public
Descriptor
getDescriptor​(
String
inDescriptorName)
throws
MBeanException
,

RuntimeOperationsException

Returns a Descriptor requested by name.

**Parameters:**
- inDescriptorName

- The name of the descriptor.

**Returns:**
- Descriptor containing a descriptor for the ModelMBean with the
same name. If no descriptor is found, null is returned.

**Throws:**
- MBeanException

- Wraps a distributed communication Exception.
- RuntimeOperationsException

- Wraps an IllegalArgumentException
for null name.

**See Also:**
- ModelMBeanInfo.setDescriptor(javax.management.Descriptor, java.lang.String)

---

#### public
ModelMBeanConstructorInfo
getConstructor​(
String
inName)
throws
MBeanException
,

RuntimeOperationsException

Returns the ModelMBeanConstructorInfo requested by name.
If no ModelMBeanConstructorInfo exists for this name null is returned.

**Parameters:**
- inName

- the name of the constructor.

**Returns:**
- the constructor info for the named constructor, or null
if there is none.

**Throws:**
- MBeanException

- Wraps a distributed communication Exception.
- RuntimeOperationsException

- Wraps an IllegalArgumentException
for a null constructor name.

---

#### public
Descriptor
getDescriptor()

Description copied from class:

MBeanInfo

**Specified by:**
- getDescriptor

in interface

DescriptorRead

**Overrides:**
- getDescriptor

in class

MBeanInfo

**Returns:**
- a descriptor that is either immutable or a copy of the original.

**Since:**
- 1.6

---

### Additional Sections

#### Class ModelMBeanInfoSupport

java.lang.Object

- javax.management.MBeanInfo
- - javax.management.modelmbean.ModelMBeanInfoSupport

javax.management.MBeanInfo

- javax.management.modelmbean.ModelMBeanInfoSupport

javax.management.modelmbean.ModelMBeanInfoSupport

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

,

ModelMBeanInfo

```java
public class
ModelMBeanInfoSupport

extends
MBeanInfo

implements
ModelMBeanInfo
```

This class represents the meta data for ModelMBeans. Descriptors have been
added on the meta data objects.

Java resources wishing to be manageable instantiate the ModelMBean using the
MBeanServer's createMBean method. The resource then sets the ModelMBeanInfo
and Descriptors for the ModelMBean instance. The attributes and operations
exposed via the ModelMBeanInfo for the ModelMBean are accessible
from MBeans, connectors/adaptors like other MBeans. Through the Descriptors,
values and methods in the managed application can be defined and mapped to
attributes and operations of the ModelMBean.
This mapping can be defined during development in a file or dynamically and
programmatically at runtime.

Every ModelMBean which is instantiated in the MBeanServer becomes manageable:
its attributes and operations
become remotely accessible through the connectors/adaptors connected to that
MBeanServer.
A Java object cannot be registered in the MBeanServer unless it is a JMX
compliant MBean.
By instantiating a ModelMBean, resources are guaranteed that the MBean is
valid.

MBeanException and RuntimeOperationsException must be thrown on every public
method. This allows for wrapping exceptions from distributed
communications (RMI, EJB, etc.)

The

serialVersionUID

of this class is

-1935722590756516193L

.

**Since:** 1.5
**See Also:** Serialized Form

public class

ModelMBeanInfoSupport

extends

MBeanInfo

implements

ModelMBeanInfo

This class represents the meta data for ModelMBeans. Descriptors have been
added on the meta data objects.

Java resources wishing to be manageable instantiate the ModelMBean using the
MBeanServer's createMBean method. The resource then sets the ModelMBeanInfo
and Descriptors for the ModelMBean instance. The attributes and operations
exposed via the ModelMBeanInfo for the ModelMBean are accessible
from MBeans, connectors/adaptors like other MBeans. Through the Descriptors,
values and methods in the managed application can be defined and mapped to
attributes and operations of the ModelMBean.
This mapping can be defined during development in a file or dynamically and
programmatically at runtime.

Every ModelMBean which is instantiated in the MBeanServer becomes manageable:
its attributes and operations
become remotely accessible through the connectors/adaptors connected to that
MBeanServer.
A Java object cannot be registered in the MBeanServer unless it is a JMX
compliant MBean.
By instantiating a ModelMBean, resources are guaranteed that the MBean is
valid.

MBeanException and RuntimeOperationsException must be thrown on every public
method. This allows for wrapping exceptions from distributed
communications (RMI, EJB, etc.)

The

serialVersionUID

of this class is

-1935722590756516193L

.

Java resources wishing to be manageable instantiate the ModelMBean using the
MBeanServer's createMBean method. The resource then sets the ModelMBeanInfo
and Descriptors for the ModelMBean instance. The attributes and operations
exposed via the ModelMBeanInfo for the ModelMBean are accessible
from MBeans, connectors/adaptors like other MBeans. Through the Descriptors,
values and methods in the managed application can be defined and mapped to
attributes and operations of the ModelMBean.
This mapping can be defined during development in a file or dynamically and
programmatically at runtime.

Every ModelMBean which is instantiated in the MBeanServer becomes manageable:
its attributes and operations
become remotely accessible through the connectors/adaptors connected to that
MBeanServer.
A Java object cannot be registered in the MBeanServer unless it is a JMX
compliant MBean.
By instantiating a ModelMBean, resources are guaranteed that the MBean is
valid.

MBeanException and RuntimeOperationsException must be thrown on every public
method. This allows for wrapping exceptions from distributed
communications (RMI, EJB, etc.)

The

serialVersionUID

of this class is

-1935722590756516193L

.

Every ModelMBean which is instantiated in the MBeanServer becomes manageable:
its attributes and operations
become remotely accessible through the connectors/adaptors connected to that
MBeanServer.
A Java object cannot be registered in the MBeanServer unless it is a JMX
compliant MBean.
By instantiating a ModelMBean, resources are guaranteed that the MBean is
valid.

MBeanException and RuntimeOperationsException must be thrown on every public
method. This allows for wrapping exceptions from distributed
communications (RMI, EJB, etc.)

The

serialVersionUID

of this class is

-1935722590756516193L

.

The

serialVersionUID

of this class is

-1935722590756516193L

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ModelMBeanInfoSupport

​(

String

className,

String

description,

ModelMBeanAttributeInfo

[] attributes,

ModelMBeanConstructorInfo

[] constructors,

ModelMBeanOperationInfo

[] operations,

ModelMBeanNotificationInfo

[] notifications)

Creates a ModelMBeanInfoSupport with the provided information,
but the descriptor is a default.

ModelMBeanInfoSupport

​(

String

className,

String

description,

ModelMBeanAttributeInfo

[] attributes,

ModelMBeanConstructorInfo

[] constructors,

ModelMBeanOperationInfo

[] operations,

ModelMBeanNotificationInfo

[] notifications,

Descriptor

mbeandescriptor)

Creates a ModelMBeanInfoSupport with the provided information
and the descriptor given in parameter.

ModelMBeanInfoSupport

​(

ModelMBeanInfo

mbi)

Constructs a ModelMBeanInfoSupport which is a duplicate of the given
ModelMBeanInfo.

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

ModelMBeanConstructorInfo

getConstructor

​(

String

inName)

Returns the ModelMBeanConstructorInfo requested by name.

Descriptor

getDescriptor

()

Get the descriptor of this MBeanInfo.

Descriptor

getDescriptor

​(

String

inDescriptorName)

Returns a Descriptor requested by name.

- Methods declared in class javax.management.

MBeanInfo

equals

,

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

- Methods declared in interface javax.management.modelmbean.

ModelMBeanInfo

getAttribute

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

getDescriptors

,

getMBeanDescriptor

,

getNotification

,

getNotifications

,

getOperation

,

getOperations

,

setDescriptor

,

setDescriptors

,

setMBeanDescriptor

Constructor Summary

Constructors

Constructor

Description

ModelMBeanInfoSupport

​(

String

className,

String

description,

ModelMBeanAttributeInfo

[] attributes,

ModelMBeanConstructorInfo

[] constructors,

ModelMBeanOperationInfo

[] operations,

ModelMBeanNotificationInfo

[] notifications)

Creates a ModelMBeanInfoSupport with the provided information,
but the descriptor is a default.

ModelMBeanInfoSupport

​(

String

className,

String

description,

ModelMBeanAttributeInfo

[] attributes,

ModelMBeanConstructorInfo

[] constructors,

ModelMBeanOperationInfo

[] operations,

ModelMBeanNotificationInfo

[] notifications,

Descriptor

mbeandescriptor)

Creates a ModelMBeanInfoSupport with the provided information
and the descriptor given in parameter.

ModelMBeanInfoSupport

​(

ModelMBeanInfo

mbi)

Constructs a ModelMBeanInfoSupport which is a duplicate of the given
ModelMBeanInfo.

---

#### Constructor Summary

Creates a ModelMBeanInfoSupport with the provided information,
but the descriptor is a default.

Creates a ModelMBeanInfoSupport with the provided information
and the descriptor given in parameter.

Constructs a ModelMBeanInfoSupport which is a duplicate of the given
ModelMBeanInfo.

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

ModelMBeanConstructorInfo

getConstructor

​(

String

inName)

Returns the ModelMBeanConstructorInfo requested by name.

Descriptor

getDescriptor

()

Get the descriptor of this MBeanInfo.

Descriptor

getDescriptor

​(

String

inDescriptorName)

Returns a Descriptor requested by name.

- Methods declared in class javax.management.

MBeanInfo

equals

,

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

- Methods declared in interface javax.management.modelmbean.

ModelMBeanInfo

getAttribute

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

getDescriptors

,

getMBeanDescriptor

,

getNotification

,

getNotifications

,

getOperation

,

getOperations

,

setDescriptor

,

setDescriptors

,

setMBeanDescriptor

---

#### Method Summary

Returns a shallow clone of this instance.

Returns the ModelMBeanConstructorInfo requested by name.

Get the descriptor of this MBeanInfo.

Returns a Descriptor requested by name.

Methods declared in class javax.management.

MBeanInfo

equals

,

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

#### Methods declared in class javax.management. MBeanInfo

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

Methods declared in interface javax.management.modelmbean.

ModelMBeanInfo

getAttribute

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

getDescriptors

,

getMBeanDescriptor

,

getNotification

,

getNotifications

,

getOperation

,

getOperations

,

setDescriptor

,

setDescriptors

,

setMBeanDescriptor

---

#### Methods declared in interface javax.management.modelmbean. ModelMBeanInfo

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ModelMBeanInfoSupport

```java
public ModelMBeanInfoSupport​(
ModelMBeanInfo
mbi)
```

Constructs a ModelMBeanInfoSupport which is a duplicate of the given
ModelMBeanInfo. The returned object is a shallow copy of the given
object. Neither the Descriptor nor the contained arrays
(

ModelMBeanAttributeInfo[]

etc) are cloned. This method is
chiefly of interest to modify the Descriptor of the returned instance
via

setDescriptor

without affecting the
Descriptor of the original object.

**Parameters:** mbi

- the ModelMBeanInfo instance from which the ModelMBeanInfo
being created is initialized.

- ModelMBeanInfoSupport

```java
public ModelMBeanInfoSupport​(
String
className,

String
description,

ModelMBeanAttributeInfo
[] attributes,

ModelMBeanConstructorInfo
[] constructors,

ModelMBeanOperationInfo
[] operations,

ModelMBeanNotificationInfo
[] notifications)
```

Creates a ModelMBeanInfoSupport with the provided information,
but the descriptor is a default.
The default descriptor is: name=className, descriptorType="mbean",
displayName=className, persistPolicy="never", log="F", visibility="1"

**Parameters:** className

- classname of the MBean
**Parameters:** description

- human readable description of the
ModelMBean
**Parameters:** attributes

- array of ModelMBeanAttributeInfo objects
which have descriptors
**Parameters:** constructors

- array of ModelMBeanConstructorInfo
objects which have descriptors
**Parameters:** operations

- array of ModelMBeanOperationInfo objects
which have descriptors
**Parameters:** notifications

- array of ModelMBeanNotificationInfo
objects which have descriptors

- ModelMBeanInfoSupport

```java
public ModelMBeanInfoSupport​(
String
className,

String
description,

ModelMBeanAttributeInfo
[] attributes,

ModelMBeanConstructorInfo
[] constructors,

ModelMBeanOperationInfo
[] operations,

ModelMBeanNotificationInfo
[] notifications,

Descriptor
mbeandescriptor)
```

Creates a ModelMBeanInfoSupport with the provided information
and the descriptor given in parameter.

**Parameters:** className

- classname of the MBean
**Parameters:** description

- human readable description of the
ModelMBean
**Parameters:** attributes

- array of ModelMBeanAttributeInfo objects
which have descriptors
**Parameters:** constructors

- array of ModelMBeanConstructorInfo
objects which have descriptor
**Parameters:** operations

- array of ModelMBeanOperationInfo objects
which have descriptor
**Parameters:** notifications

- array of ModelMBeanNotificationInfo
objects which have descriptor
**Parameters:** mbeandescriptor

- descriptor to be used as the
MBeanDescriptor containing MBean wide policy. If the
descriptor is null, a default descriptor will be constructed.
The default descriptor is:
name=className, descriptorType="mbean", displayName=className,
persistPolicy="never", log="F", visibility="1". If the descriptor
does not contain all of these fields, the missing ones are
added with these default values.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException for invalid descriptor passed in
parameter. (see

getMBeanDescriptor

for the definition of a valid MBean
descriptor.)

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
public
Object
clone()
```

Returns a shallow clone of this instance. Neither the Descriptor nor
the contained arrays (

ModelMBeanAttributeInfo[]

etc) are
cloned. This method is chiefly of interest to modify the Descriptor
of the clone via

setDescriptor

without affecting
the Descriptor of the original object.

**Specified by:** clone

in interface

ModelMBeanInfo
**Overrides:** clone

in class

MBeanInfo
**Returns:** a shallow clone of this instance.
**See Also:** Cloneable

- getDescriptor

```java
public
Descriptor
getDescriptor​(
String
inDescriptorName)
throws
MBeanException
,

RuntimeOperationsException
```

Returns a Descriptor requested by name.

**Parameters:** inDescriptorName

- The name of the descriptor.
**Returns:** Descriptor containing a descriptor for the ModelMBean with the
same name. If no descriptor is found, null is returned.
**Throws:** MBeanException

- Wraps a distributed communication Exception.
**Throws:** RuntimeOperationsException

- Wraps an IllegalArgumentException
for null name.
**See Also:** ModelMBeanInfo.setDescriptor(javax.management.Descriptor, java.lang.String)

- getConstructor

```java
public
ModelMBeanConstructorInfo
getConstructor​(
String
inName)
throws
MBeanException
,

RuntimeOperationsException
```

Returns the ModelMBeanConstructorInfo requested by name.
If no ModelMBeanConstructorInfo exists for this name null is returned.

**Parameters:** inName

- the name of the constructor.
**Returns:** the constructor info for the named constructor, or null
if there is none.
**Throws:** MBeanException

- Wraps a distributed communication Exception.
**Throws:** RuntimeOperationsException

- Wraps an IllegalArgumentException
for a null constructor name.

- getDescriptor

```java
public
Descriptor
getDescriptor()
```

Description copied from class:

MBeanInfo

Get the descriptor of this MBeanInfo. Changing the returned value
will have no affect on the original descriptor.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Overrides:** getDescriptor

in class

MBeanInfo
**Returns:** a descriptor that is either immutable or a copy of the original.
**Since:** 1.6

Constructor Detail

- ModelMBeanInfoSupport

```java
public ModelMBeanInfoSupport​(
ModelMBeanInfo
mbi)
```

Constructs a ModelMBeanInfoSupport which is a duplicate of the given
ModelMBeanInfo. The returned object is a shallow copy of the given
object. Neither the Descriptor nor the contained arrays
(

ModelMBeanAttributeInfo[]

etc) are cloned. This method is
chiefly of interest to modify the Descriptor of the returned instance
via

setDescriptor

without affecting the
Descriptor of the original object.

**Parameters:** mbi

- the ModelMBeanInfo instance from which the ModelMBeanInfo
being created is initialized.

- ModelMBeanInfoSupport

```java
public ModelMBeanInfoSupport​(
String
className,

String
description,

ModelMBeanAttributeInfo
[] attributes,

ModelMBeanConstructorInfo
[] constructors,

ModelMBeanOperationInfo
[] operations,

ModelMBeanNotificationInfo
[] notifications)
```

Creates a ModelMBeanInfoSupport with the provided information,
but the descriptor is a default.
The default descriptor is: name=className, descriptorType="mbean",
displayName=className, persistPolicy="never", log="F", visibility="1"

**Parameters:** className

- classname of the MBean
**Parameters:** description

- human readable description of the
ModelMBean
**Parameters:** attributes

- array of ModelMBeanAttributeInfo objects
which have descriptors
**Parameters:** constructors

- array of ModelMBeanConstructorInfo
objects which have descriptors
**Parameters:** operations

- array of ModelMBeanOperationInfo objects
which have descriptors
**Parameters:** notifications

- array of ModelMBeanNotificationInfo
objects which have descriptors

- ModelMBeanInfoSupport

```java
public ModelMBeanInfoSupport​(
String
className,

String
description,

ModelMBeanAttributeInfo
[] attributes,

ModelMBeanConstructorInfo
[] constructors,

ModelMBeanOperationInfo
[] operations,

ModelMBeanNotificationInfo
[] notifications,

Descriptor
mbeandescriptor)
```

Creates a ModelMBeanInfoSupport with the provided information
and the descriptor given in parameter.

**Parameters:** className

- classname of the MBean
**Parameters:** description

- human readable description of the
ModelMBean
**Parameters:** attributes

- array of ModelMBeanAttributeInfo objects
which have descriptors
**Parameters:** constructors

- array of ModelMBeanConstructorInfo
objects which have descriptor
**Parameters:** operations

- array of ModelMBeanOperationInfo objects
which have descriptor
**Parameters:** notifications

- array of ModelMBeanNotificationInfo
objects which have descriptor
**Parameters:** mbeandescriptor

- descriptor to be used as the
MBeanDescriptor containing MBean wide policy. If the
descriptor is null, a default descriptor will be constructed.
The default descriptor is:
name=className, descriptorType="mbean", displayName=className,
persistPolicy="never", log="F", visibility="1". If the descriptor
does not contain all of these fields, the missing ones are
added with these default values.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException for invalid descriptor passed in
parameter. (see

getMBeanDescriptor

for the definition of a valid MBean
descriptor.)

---

#### Constructor Detail

ModelMBeanInfoSupport

```java
public ModelMBeanInfoSupport​(
ModelMBeanInfo
mbi)
```

Constructs a ModelMBeanInfoSupport which is a duplicate of the given
ModelMBeanInfo. The returned object is a shallow copy of the given
object. Neither the Descriptor nor the contained arrays
(

ModelMBeanAttributeInfo[]

etc) are cloned. This method is
chiefly of interest to modify the Descriptor of the returned instance
via

setDescriptor

without affecting the
Descriptor of the original object.

**Parameters:** mbi

- the ModelMBeanInfo instance from which the ModelMBeanInfo
being created is initialized.

---

#### ModelMBeanInfoSupport

public ModelMBeanInfoSupport​(

ModelMBeanInfo

mbi)

Constructs a ModelMBeanInfoSupport which is a duplicate of the given
ModelMBeanInfo. The returned object is a shallow copy of the given
object. Neither the Descriptor nor the contained arrays
(

ModelMBeanAttributeInfo[]

etc) are cloned. This method is
chiefly of interest to modify the Descriptor of the returned instance
via

setDescriptor

without affecting the
Descriptor of the original object.

ModelMBeanInfoSupport

```java
public ModelMBeanInfoSupport​(
String
className,

String
description,

ModelMBeanAttributeInfo
[] attributes,

ModelMBeanConstructorInfo
[] constructors,

ModelMBeanOperationInfo
[] operations,

ModelMBeanNotificationInfo
[] notifications)
```

Creates a ModelMBeanInfoSupport with the provided information,
but the descriptor is a default.
The default descriptor is: name=className, descriptorType="mbean",
displayName=className, persistPolicy="never", log="F", visibility="1"

**Parameters:** className

- classname of the MBean
**Parameters:** description

- human readable description of the
ModelMBean
**Parameters:** attributes

- array of ModelMBeanAttributeInfo objects
which have descriptors
**Parameters:** constructors

- array of ModelMBeanConstructorInfo
objects which have descriptors
**Parameters:** operations

- array of ModelMBeanOperationInfo objects
which have descriptors
**Parameters:** notifications

- array of ModelMBeanNotificationInfo
objects which have descriptors

---

#### ModelMBeanInfoSupport

public ModelMBeanInfoSupport​(

String

className,

String

description,

ModelMBeanAttributeInfo

[] attributes,

ModelMBeanConstructorInfo

[] constructors,

ModelMBeanOperationInfo

[] operations,

ModelMBeanNotificationInfo

[] notifications)

Creates a ModelMBeanInfoSupport with the provided information,
but the descriptor is a default.
The default descriptor is: name=className, descriptorType="mbean",
displayName=className, persistPolicy="never", log="F", visibility="1"

ModelMBeanInfoSupport

```java
public ModelMBeanInfoSupport​(
String
className,

String
description,

ModelMBeanAttributeInfo
[] attributes,

ModelMBeanConstructorInfo
[] constructors,

ModelMBeanOperationInfo
[] operations,

ModelMBeanNotificationInfo
[] notifications,

Descriptor
mbeandescriptor)
```

Creates a ModelMBeanInfoSupport with the provided information
and the descriptor given in parameter.

**Parameters:** className

- classname of the MBean
**Parameters:** description

- human readable description of the
ModelMBean
**Parameters:** attributes

- array of ModelMBeanAttributeInfo objects
which have descriptors
**Parameters:** constructors

- array of ModelMBeanConstructorInfo
objects which have descriptor
**Parameters:** operations

- array of ModelMBeanOperationInfo objects
which have descriptor
**Parameters:** notifications

- array of ModelMBeanNotificationInfo
objects which have descriptor
**Parameters:** mbeandescriptor

- descriptor to be used as the
MBeanDescriptor containing MBean wide policy. If the
descriptor is null, a default descriptor will be constructed.
The default descriptor is:
name=className, descriptorType="mbean", displayName=className,
persistPolicy="never", log="F", visibility="1". If the descriptor
does not contain all of these fields, the missing ones are
added with these default values.
**Throws:** RuntimeOperationsException

- Wraps an
IllegalArgumentException for invalid descriptor passed in
parameter. (see

getMBeanDescriptor

for the definition of a valid MBean
descriptor.)

---

#### ModelMBeanInfoSupport

public ModelMBeanInfoSupport​(

String

className,

String

description,

ModelMBeanAttributeInfo

[] attributes,

ModelMBeanConstructorInfo

[] constructors,

ModelMBeanOperationInfo

[] operations,

ModelMBeanNotificationInfo

[] notifications,

Descriptor

mbeandescriptor)

Creates a ModelMBeanInfoSupport with the provided information
and the descriptor given in parameter.

Method Detail

- clone

```java
public
Object
clone()
```

Returns a shallow clone of this instance. Neither the Descriptor nor
the contained arrays (

ModelMBeanAttributeInfo[]

etc) are
cloned. This method is chiefly of interest to modify the Descriptor
of the clone via

setDescriptor

without affecting
the Descriptor of the original object.

**Specified by:** clone

in interface

ModelMBeanInfo
**Overrides:** clone

in class

MBeanInfo
**Returns:** a shallow clone of this instance.
**See Also:** Cloneable

- getDescriptor

```java
public
Descriptor
getDescriptor​(
String
inDescriptorName)
throws
MBeanException
,

RuntimeOperationsException
```

Returns a Descriptor requested by name.

**Parameters:** inDescriptorName

- The name of the descriptor.
**Returns:** Descriptor containing a descriptor for the ModelMBean with the
same name. If no descriptor is found, null is returned.
**Throws:** MBeanException

- Wraps a distributed communication Exception.
**Throws:** RuntimeOperationsException

- Wraps an IllegalArgumentException
for null name.
**See Also:** ModelMBeanInfo.setDescriptor(javax.management.Descriptor, java.lang.String)

- getConstructor

```java
public
ModelMBeanConstructorInfo
getConstructor​(
String
inName)
throws
MBeanException
,

RuntimeOperationsException
```

Returns the ModelMBeanConstructorInfo requested by name.
If no ModelMBeanConstructorInfo exists for this name null is returned.

**Parameters:** inName

- the name of the constructor.
**Returns:** the constructor info for the named constructor, or null
if there is none.
**Throws:** MBeanException

- Wraps a distributed communication Exception.
**Throws:** RuntimeOperationsException

- Wraps an IllegalArgumentException
for a null constructor name.

- getDescriptor

```java
public
Descriptor
getDescriptor()
```

Description copied from class:

MBeanInfo

Get the descriptor of this MBeanInfo. Changing the returned value
will have no affect on the original descriptor.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Overrides:** getDescriptor

in class

MBeanInfo
**Returns:** a descriptor that is either immutable or a copy of the original.
**Since:** 1.6

---

#### Method Detail

clone

```java
public
Object
clone()
```

Returns a shallow clone of this instance. Neither the Descriptor nor
the contained arrays (

ModelMBeanAttributeInfo[]

etc) are
cloned. This method is chiefly of interest to modify the Descriptor
of the clone via

setDescriptor

without affecting
the Descriptor of the original object.

**Specified by:** clone

in interface

ModelMBeanInfo
**Overrides:** clone

in class

MBeanInfo
**Returns:** a shallow clone of this instance.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a shallow clone of this instance. Neither the Descriptor nor
the contained arrays (

ModelMBeanAttributeInfo[]

etc) are
cloned. This method is chiefly of interest to modify the Descriptor
of the clone via

setDescriptor

without affecting
the Descriptor of the original object.

getDescriptor

```java
public
Descriptor
getDescriptor​(
String
inDescriptorName)
throws
MBeanException
,

RuntimeOperationsException
```

Returns a Descriptor requested by name.

**Parameters:** inDescriptorName

- The name of the descriptor.
**Returns:** Descriptor containing a descriptor for the ModelMBean with the
same name. If no descriptor is found, null is returned.
**Throws:** MBeanException

- Wraps a distributed communication Exception.
**Throws:** RuntimeOperationsException

- Wraps an IllegalArgumentException
for null name.
**See Also:** ModelMBeanInfo.setDescriptor(javax.management.Descriptor, java.lang.String)

---

#### getDescriptor

public

Descriptor

getDescriptor​(

String

inDescriptorName)
throws

MBeanException

,

RuntimeOperationsException

Returns a Descriptor requested by name.

getConstructor

```java
public
ModelMBeanConstructorInfo
getConstructor​(
String
inName)
throws
MBeanException
,

RuntimeOperationsException
```

Returns the ModelMBeanConstructorInfo requested by name.
If no ModelMBeanConstructorInfo exists for this name null is returned.

**Parameters:** inName

- the name of the constructor.
**Returns:** the constructor info for the named constructor, or null
if there is none.
**Throws:** MBeanException

- Wraps a distributed communication Exception.
**Throws:** RuntimeOperationsException

- Wraps an IllegalArgumentException
for a null constructor name.

---

#### getConstructor

public

ModelMBeanConstructorInfo

getConstructor​(

String

inName)
throws

MBeanException

,

RuntimeOperationsException

Returns the ModelMBeanConstructorInfo requested by name.
If no ModelMBeanConstructorInfo exists for this name null is returned.

getDescriptor

```java
public
Descriptor
getDescriptor()
```

Description copied from class:

MBeanInfo

Get the descriptor of this MBeanInfo. Changing the returned value
will have no affect on the original descriptor.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Overrides:** getDescriptor

in class

MBeanInfo
**Returns:** a descriptor that is either immutable or a copy of the original.
**Since:** 1.6

---

#### getDescriptor

public

Descriptor

getDescriptor()

Description copied from class:

MBeanInfo

Get the descriptor of this MBeanInfo. Changing the returned value
will have no affect on the original descriptor.

---

