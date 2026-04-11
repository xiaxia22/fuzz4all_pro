# Interface ModelMBean

**Source:** `java.management\javax\management\modelmbean\ModelMBean.html`

### Class Description

```java
public interface
ModelMBean

extends
DynamicMBean
,
PersistentMBean
,
ModelMBeanNotificationBroadcaster
```

This interface must be implemented by the ModelMBeans. An implementation of this interface
must be shipped with every JMX Agent.

Java resources wishing to be manageable instantiate the ModelMBean using the MBeanServer's
createMBean method. The resource then sets the ModelMBeanInfo (with Descriptors) for the ModelMBean
instance. The attributes and operations exposed via the ModelMBeanInfo for the ModelMBean are accessible
from MBeans, connectors/adaptors like other MBeans. Through the ModelMBeanInfo Descriptors, values and methods in
the managed application can be defined and mapped to attributes and operations of the ModelMBean.
This mapping can be defined during development in an XML formatted file or dynamically and
programmatically at runtime.

Every ModelMBean which is instantiated in the MBeanServer becomes manageable:
its attributes and operations
become remotely accessible through the connectors/adaptors connected to that MBeanServer.
A Java object cannot be registered in the MBeanServer unless it is a JMX compliant MBean.
By instantiating a ModelMBean, resources are guaranteed that the MBean is valid.

MBeanException and RuntimeOperationsException must be thrown on every public method. This allows
for wrapping exceptions from distributed communications (RMI, EJB, etc.). These exceptions do
not have to be thrown by the implementation except in the scenarios described in the specification
and javadoc.

**All Superinterfaces:** DynamicMBean

,

ModelMBeanNotificationBroadcaster

,

NotificationBroadcaster

,

PersistentMBean

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void setModelMBeanInfo​(
ModelMBeanInfo
inModelMBeanInfo)
throws
MBeanException
,

RuntimeOperationsException

Initializes a ModelMBean object using ModelMBeanInfo passed in.
This method makes it possible to set a customized ModelMBeanInfo on
the ModelMBean as long as it is not registered with the MBeanServer.

Once the ModelMBean's ModelMBeanInfo (with Descriptors) are
customized and set on the ModelMBean, the ModelMBean can be
registered with the MBeanServer.

If the ModelMBean is currently registered, this method throws
a

RuntimeOperationsException

wrapping an

IllegalStateException

**Parameters:**
- inModelMBeanInfo

- The ModelMBeanInfo object to be used
by the ModelMBean.

**Throws:**
- MBeanException

- Wraps a distributed communication
Exception.
- RuntimeOperationsException

-

- Wraps an

IllegalArgumentException

if
the MBeanInfo passed in parameter is null.
- Wraps an

IllegalStateException

if the ModelMBean
is currently registered in the MBeanServer.

---

#### void setManagedResource​(
Object
mr,

String
mr_type)
throws
MBeanException
,

RuntimeOperationsException
,

InstanceNotFoundException
,

InvalidTargetObjectTypeException

Sets the instance handle of the object against which to
execute all methods in this ModelMBean management interface
(MBeanInfo and Descriptors).

**Parameters:**
- mr

- Object that is the managed resource
- mr_type

- The type of reference for the managed resource. Can be: ObjectReference,
Handle, IOR, EJBHandle, RMIReference.
If the MBeanServer cannot process the mr_type passed in, an InvalidTargetTypeException
will be thrown.

**Throws:**
- MBeanException

- The initializer of the object has thrown an exception.
- RuntimeOperationsException

- Wraps an IllegalArgumentException:
The managed resource type passed in parameter is null.
- InstanceNotFoundException

- The managed resource object could not be found
- InvalidTargetObjectTypeException

- The managed resource type cannot be processed by the
ModelMBean or JMX Agent.

---

### Additional Sections

#### Interface ModelMBean

**All Superinterfaces:** DynamicMBean

,

ModelMBeanNotificationBroadcaster

,

NotificationBroadcaster

,

PersistentMBean

**All Known Implementing Classes:** RequiredModelMBean

```java
public interface
ModelMBean

extends
DynamicMBean
,
PersistentMBean
,
ModelMBeanNotificationBroadcaster
```

This interface must be implemented by the ModelMBeans. An implementation of this interface
must be shipped with every JMX Agent.

Java resources wishing to be manageable instantiate the ModelMBean using the MBeanServer's
createMBean method. The resource then sets the ModelMBeanInfo (with Descriptors) for the ModelMBean
instance. The attributes and operations exposed via the ModelMBeanInfo for the ModelMBean are accessible
from MBeans, connectors/adaptors like other MBeans. Through the ModelMBeanInfo Descriptors, values and methods in
the managed application can be defined and mapped to attributes and operations of the ModelMBean.
This mapping can be defined during development in an XML formatted file or dynamically and
programmatically at runtime.

Every ModelMBean which is instantiated in the MBeanServer becomes manageable:
its attributes and operations
become remotely accessible through the connectors/adaptors connected to that MBeanServer.
A Java object cannot be registered in the MBeanServer unless it is a JMX compliant MBean.
By instantiating a ModelMBean, resources are guaranteed that the MBean is valid.

MBeanException and RuntimeOperationsException must be thrown on every public method. This allows
for wrapping exceptions from distributed communications (RMI, EJB, etc.). These exceptions do
not have to be thrown by the implementation except in the scenarios described in the specification
and javadoc.

**Since:** 1.5

public interface

ModelMBean

extends

DynamicMBean

,

PersistentMBean

,

ModelMBeanNotificationBroadcaster

This interface must be implemented by the ModelMBeans. An implementation of this interface
must be shipped with every JMX Agent.

Java resources wishing to be manageable instantiate the ModelMBean using the MBeanServer's
createMBean method. The resource then sets the ModelMBeanInfo (with Descriptors) for the ModelMBean
instance. The attributes and operations exposed via the ModelMBeanInfo for the ModelMBean are accessible
from MBeans, connectors/adaptors like other MBeans. Through the ModelMBeanInfo Descriptors, values and methods in
the managed application can be defined and mapped to attributes and operations of the ModelMBean.
This mapping can be defined during development in an XML formatted file or dynamically and
programmatically at runtime.

Every ModelMBean which is instantiated in the MBeanServer becomes manageable:
its attributes and operations
become remotely accessible through the connectors/adaptors connected to that MBeanServer.
A Java object cannot be registered in the MBeanServer unless it is a JMX compliant MBean.
By instantiating a ModelMBean, resources are guaranteed that the MBean is valid.

MBeanException and RuntimeOperationsException must be thrown on every public method. This allows
for wrapping exceptions from distributed communications (RMI, EJB, etc.). These exceptions do
not have to be thrown by the implementation except in the scenarios described in the specification
and javadoc.

Java resources wishing to be manageable instantiate the ModelMBean using the MBeanServer's
createMBean method. The resource then sets the ModelMBeanInfo (with Descriptors) for the ModelMBean
instance. The attributes and operations exposed via the ModelMBeanInfo for the ModelMBean are accessible
from MBeans, connectors/adaptors like other MBeans. Through the ModelMBeanInfo Descriptors, values and methods in
the managed application can be defined and mapped to attributes and operations of the ModelMBean.
This mapping can be defined during development in an XML formatted file or dynamically and
programmatically at runtime.

Every ModelMBean which is instantiated in the MBeanServer becomes manageable:
its attributes and operations
become remotely accessible through the connectors/adaptors connected to that MBeanServer.
A Java object cannot be registered in the MBeanServer unless it is a JMX compliant MBean.
By instantiating a ModelMBean, resources are guaranteed that the MBean is valid.

MBeanException and RuntimeOperationsException must be thrown on every public method. This allows
for wrapping exceptions from distributed communications (RMI, EJB, etc.). These exceptions do
not have to be thrown by the implementation except in the scenarios described in the specification
and javadoc.

Every ModelMBean which is instantiated in the MBeanServer becomes manageable:
its attributes and operations
become remotely accessible through the connectors/adaptors connected to that MBeanServer.
A Java object cannot be registered in the MBeanServer unless it is a JMX compliant MBean.
By instantiating a ModelMBean, resources are guaranteed that the MBean is valid.

MBeanException and RuntimeOperationsException must be thrown on every public method. This allows
for wrapping exceptions from distributed communications (RMI, EJB, etc.). These exceptions do
not have to be thrown by the implementation except in the scenarios described in the specification
and javadoc.

MBeanException and RuntimeOperationsException must be thrown on every public method. This allows
for wrapping exceptions from distributed communications (RMI, EJB, etc.). These exceptions do
not have to be thrown by the implementation except in the scenarios described in the specification
and javadoc.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

setManagedResource

​(

Object

mr,

String

mr_type)

Sets the instance handle of the object against which to
execute all methods in this ModelMBean management interface
(MBeanInfo and Descriptors).

void

setModelMBeanInfo

​(

ModelMBeanInfo

inModelMBeanInfo)

Initializes a ModelMBean object using ModelMBeanInfo passed in.

- Methods declared in interface javax.management.

DynamicMBean

getAttribute

,

getAttributes

,

getMBeanInfo

,

invoke

,

setAttribute

,

setAttributes

- Methods declared in interface javax.management.modelmbean.

ModelMBeanNotificationBroadcaster

addAttributeChangeNotificationListener

,

removeAttributeChangeNotificationListener

,

sendAttributeChangeNotification

,

sendAttributeChangeNotification

,

sendNotification

,

sendNotification

- Methods declared in interface javax.management.

NotificationBroadcaster

addNotificationListener

,

getNotificationInfo

,

removeNotificationListener

- Methods declared in interface javax.management.

PersistentMBean

load

,

store

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

setManagedResource

​(

Object

mr,

String

mr_type)

Sets the instance handle of the object against which to
execute all methods in this ModelMBean management interface
(MBeanInfo and Descriptors).

void

setModelMBeanInfo

​(

ModelMBeanInfo

inModelMBeanInfo)

Initializes a ModelMBean object using ModelMBeanInfo passed in.

- Methods declared in interface javax.management.

DynamicMBean

getAttribute

,

getAttributes

,

getMBeanInfo

,

invoke

,

setAttribute

,

setAttributes

- Methods declared in interface javax.management.modelmbean.

ModelMBeanNotificationBroadcaster

addAttributeChangeNotificationListener

,

removeAttributeChangeNotificationListener

,

sendAttributeChangeNotification

,

sendAttributeChangeNotification

,

sendNotification

,

sendNotification

- Methods declared in interface javax.management.

NotificationBroadcaster

addNotificationListener

,

getNotificationInfo

,

removeNotificationListener

- Methods declared in interface javax.management.

PersistentMBean

load

,

store

---

#### Method Summary

Sets the instance handle of the object against which to
execute all methods in this ModelMBean management interface
(MBeanInfo and Descriptors).

Initializes a ModelMBean object using ModelMBeanInfo passed in.

Methods declared in interface javax.management.

DynamicMBean

getAttribute

,

getAttributes

,

getMBeanInfo

,

invoke

,

setAttribute

,

setAttributes

---

#### Methods declared in interface javax.management. DynamicMBean

Methods declared in interface javax.management.modelmbean.

ModelMBeanNotificationBroadcaster

addAttributeChangeNotificationListener

,

removeAttributeChangeNotificationListener

,

sendAttributeChangeNotification

,

sendAttributeChangeNotification

,

sendNotification

,

sendNotification

---

#### Methods declared in interface javax.management.modelmbean. ModelMBeanNotificationBroadcaster

Methods declared in interface javax.management.

NotificationBroadcaster

addNotificationListener

,

getNotificationInfo

,

removeNotificationListener

---

#### Methods declared in interface javax.management. NotificationBroadcaster

Methods declared in interface javax.management.

PersistentMBean

load

,

store

---

#### Methods declared in interface javax.management. PersistentMBean

============ METHOD DETAIL ==========

- Method Detail

- setModelMBeanInfo

```java
void setModelMBeanInfo​(
ModelMBeanInfo
inModelMBeanInfo)
throws
MBeanException
,

RuntimeOperationsException
```

Initializes a ModelMBean object using ModelMBeanInfo passed in.
This method makes it possible to set a customized ModelMBeanInfo on
the ModelMBean as long as it is not registered with the MBeanServer.

Once the ModelMBean's ModelMBeanInfo (with Descriptors) are
customized and set on the ModelMBean, the ModelMBean can be
registered with the MBeanServer.

If the ModelMBean is currently registered, this method throws
a

RuntimeOperationsException

wrapping an

IllegalStateException

**Parameters:** inModelMBeanInfo

- The ModelMBeanInfo object to be used
by the ModelMBean.
**Throws:** MBeanException

- Wraps a distributed communication
Exception.
**Throws:** RuntimeOperationsException

-

- Wraps an

IllegalArgumentException

if
the MBeanInfo passed in parameter is null.
- Wraps an

IllegalStateException

if the ModelMBean
is currently registered in the MBeanServer.

- setManagedResource

```java
void setManagedResource​(
Object
mr,

String
mr_type)
throws
MBeanException
,

RuntimeOperationsException
,

InstanceNotFoundException
,

InvalidTargetObjectTypeException
```

Sets the instance handle of the object against which to
execute all methods in this ModelMBean management interface
(MBeanInfo and Descriptors).

**Parameters:** mr

- Object that is the managed resource
**Parameters:** mr_type

- The type of reference for the managed resource. Can be: ObjectReference,
Handle, IOR, EJBHandle, RMIReference.
If the MBeanServer cannot process the mr_type passed in, an InvalidTargetTypeException
will be thrown.
**Throws:** MBeanException

- The initializer of the object has thrown an exception.
**Throws:** RuntimeOperationsException

- Wraps an IllegalArgumentException:
The managed resource type passed in parameter is null.
**Throws:** InstanceNotFoundException

- The managed resource object could not be found
**Throws:** InvalidTargetObjectTypeException

- The managed resource type cannot be processed by the
ModelMBean or JMX Agent.

Method Detail

- setModelMBeanInfo

```java
void setModelMBeanInfo​(
ModelMBeanInfo
inModelMBeanInfo)
throws
MBeanException
,

RuntimeOperationsException
```

Initializes a ModelMBean object using ModelMBeanInfo passed in.
This method makes it possible to set a customized ModelMBeanInfo on
the ModelMBean as long as it is not registered with the MBeanServer.

Once the ModelMBean's ModelMBeanInfo (with Descriptors) are
customized and set on the ModelMBean, the ModelMBean can be
registered with the MBeanServer.

If the ModelMBean is currently registered, this method throws
a

RuntimeOperationsException

wrapping an

IllegalStateException

**Parameters:** inModelMBeanInfo

- The ModelMBeanInfo object to be used
by the ModelMBean.
**Throws:** MBeanException

- Wraps a distributed communication
Exception.
**Throws:** RuntimeOperationsException

-

- Wraps an

IllegalArgumentException

if
the MBeanInfo passed in parameter is null.
- Wraps an

IllegalStateException

if the ModelMBean
is currently registered in the MBeanServer.

- setManagedResource

```java
void setManagedResource​(
Object
mr,

String
mr_type)
throws
MBeanException
,

RuntimeOperationsException
,

InstanceNotFoundException
,

InvalidTargetObjectTypeException
```

Sets the instance handle of the object against which to
execute all methods in this ModelMBean management interface
(MBeanInfo and Descriptors).

**Parameters:** mr

- Object that is the managed resource
**Parameters:** mr_type

- The type of reference for the managed resource. Can be: ObjectReference,
Handle, IOR, EJBHandle, RMIReference.
If the MBeanServer cannot process the mr_type passed in, an InvalidTargetTypeException
will be thrown.
**Throws:** MBeanException

- The initializer of the object has thrown an exception.
**Throws:** RuntimeOperationsException

- Wraps an IllegalArgumentException:
The managed resource type passed in parameter is null.
**Throws:** InstanceNotFoundException

- The managed resource object could not be found
**Throws:** InvalidTargetObjectTypeException

- The managed resource type cannot be processed by the
ModelMBean or JMX Agent.

---

#### Method Detail

setModelMBeanInfo

```java
void setModelMBeanInfo​(
ModelMBeanInfo
inModelMBeanInfo)
throws
MBeanException
,

RuntimeOperationsException
```

Initializes a ModelMBean object using ModelMBeanInfo passed in.
This method makes it possible to set a customized ModelMBeanInfo on
the ModelMBean as long as it is not registered with the MBeanServer.

Once the ModelMBean's ModelMBeanInfo (with Descriptors) are
customized and set on the ModelMBean, the ModelMBean can be
registered with the MBeanServer.

If the ModelMBean is currently registered, this method throws
a

RuntimeOperationsException

wrapping an

IllegalStateException

**Parameters:** inModelMBeanInfo

- The ModelMBeanInfo object to be used
by the ModelMBean.
**Throws:** MBeanException

- Wraps a distributed communication
Exception.
**Throws:** RuntimeOperationsException

-

- Wraps an

IllegalArgumentException

if
the MBeanInfo passed in parameter is null.
- Wraps an

IllegalStateException

if the ModelMBean
is currently registered in the MBeanServer.

---

#### setModelMBeanInfo

void setModelMBeanInfo​(

ModelMBeanInfo

inModelMBeanInfo)
throws

MBeanException

,

RuntimeOperationsException

Initializes a ModelMBean object using ModelMBeanInfo passed in.
This method makes it possible to set a customized ModelMBeanInfo on
the ModelMBean as long as it is not registered with the MBeanServer.

Once the ModelMBean's ModelMBeanInfo (with Descriptors) are
customized and set on the ModelMBean, the ModelMBean can be
registered with the MBeanServer.

If the ModelMBean is currently registered, this method throws
a

RuntimeOperationsException

wrapping an

IllegalStateException

If the ModelMBean is currently registered, this method throws
a

RuntimeOperationsException

wrapping an

IllegalStateException

Wraps an

IllegalArgumentException

if
the MBeanInfo passed in parameter is null.

Wraps an

IllegalStateException

if the ModelMBean
is currently registered in the MBeanServer.

setManagedResource

```java
void setManagedResource​(
Object
mr,

String
mr_type)
throws
MBeanException
,

RuntimeOperationsException
,

InstanceNotFoundException
,

InvalidTargetObjectTypeException
```

Sets the instance handle of the object against which to
execute all methods in this ModelMBean management interface
(MBeanInfo and Descriptors).

**Parameters:** mr

- Object that is the managed resource
**Parameters:** mr_type

- The type of reference for the managed resource. Can be: ObjectReference,
Handle, IOR, EJBHandle, RMIReference.
If the MBeanServer cannot process the mr_type passed in, an InvalidTargetTypeException
will be thrown.
**Throws:** MBeanException

- The initializer of the object has thrown an exception.
**Throws:** RuntimeOperationsException

- Wraps an IllegalArgumentException:
The managed resource type passed in parameter is null.
**Throws:** InstanceNotFoundException

- The managed resource object could not be found
**Throws:** InvalidTargetObjectTypeException

- The managed resource type cannot be processed by the
ModelMBean or JMX Agent.

---

#### setManagedResource

void setManagedResource​(

Object

mr,

String

mr_type)
throws

MBeanException

,

RuntimeOperationsException

,

InstanceNotFoundException

,

InvalidTargetObjectTypeException

Sets the instance handle of the object against which to
execute all methods in this ModelMBean management interface
(MBeanInfo and Descriptors).

---

