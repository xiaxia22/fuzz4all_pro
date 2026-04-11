# Class RequiredModelMBean

**Source:** `java.management\javax\management\modelmbean\RequiredModelMBean.html`

### Class Description

```java
public class
RequiredModelMBean

extends
Object

implements
ModelMBean
,
MBeanRegistration
,
NotificationEmitter
```

This class is the implementation of a ModelMBean. An appropriate
implementation of a ModelMBean must be shipped with every JMX Agent
and the class must be named RequiredModelMBean.

Java resources wishing to be manageable instantiate the
RequiredModelMBean using the MBeanServer's createMBean method.
The resource then sets the MBeanInfo and Descriptors for the
RequiredModelMBean instance. The attributes and operations exposed
via the ModelMBeanInfo for the ModelMBean are accessible
from MBeans, connectors/adaptors like other MBeans. Through the
Descriptors, values and methods in the managed application can be
defined and mapped to attributes and operations of the ModelMBean.
This mapping can be defined in an XML formatted file or dynamically and
programmatically at runtime.

Every RequiredModelMBean which is instantiated in the MBeanServer
becomes manageable:

its attributes and operations become remotely accessible through the
connectors/adaptors connected to that MBeanServer.

A Java object cannot be registered in the MBeanServer unless it is a
JMX compliant MBean. By instantiating a RequiredModelMBean, resources
are guaranteed that the MBean is valid.

MBeanException and RuntimeOperationsException must be thrown on every
public method. This allows for wrapping exceptions from distributed
communications (RMI, EJB, etc.)

**All Implemented Interfaces:** DynamicMBean

,

MBeanRegistration

,

ModelMBean

,

ModelMBeanNotificationBroadcaster

,

NotificationBroadcaster

,

NotificationEmitter

,

PersistentMBean

---

### Field Details

*No entries found.*

### Constructor Details

#### public RequiredModelMBean()
throws
MBeanException
,

RuntimeOperationsException

Constructs an

RequiredModelMBean

with an empty
ModelMBeanInfo.

The RequiredModelMBean's MBeanInfo and Descriptors
can be customized using the

setModelMBeanInfo(javax.management.modelmbean.ModelMBeanInfo)

method.
After the RequiredModelMBean's MBeanInfo and Descriptors are
customized, the RequiredModelMBean can be registered with
the MBeanServer.

**Throws:**
- MBeanException

- Wraps a distributed communication Exception.
- RuntimeOperationsException

- Wraps a

RuntimeException

during the construction of the object.

---

#### public RequiredModelMBean​(
ModelMBeanInfo
mbi)
throws
MBeanException
,

RuntimeOperationsException

Constructs a RequiredModelMBean object using ModelMBeanInfo passed in.
As long as the RequiredModelMBean is not registered
with the MBeanServer yet, the RequiredModelMBean's MBeanInfo and
Descriptors can be customized using the

setModelMBeanInfo(javax.management.modelmbean.ModelMBeanInfo)

method.
After the RequiredModelMBean's MBeanInfo and Descriptors are
customized, the RequiredModelMBean can be registered with the
MBeanServer.

**Parameters:**
- mbi

- The ModelMBeanInfo object to be used by the
RequiredModelMBean. The given ModelMBeanInfo is cloned
and modified as specified by

setModelMBeanInfo(javax.management.modelmbean.ModelMBeanInfo)

**Throws:**
- MBeanException

- Wraps a distributed communication Exception.
- RuntimeOperationsException

- Wraps an
{link java.lang.IllegalArgumentException}:
The MBeanInfo passed in parameter is null.

---

### Method Details

#### public void setModelMBeanInfo​(
ModelMBeanInfo
mbi)
throws
MBeanException
,

RuntimeOperationsException

Initializes a ModelMBean object using ModelMBeanInfo passed in.
This method makes it possible to set a customized ModelMBeanInfo on
the ModelMBean as long as it is not registered with the MBeanServer.

Once the ModelMBean's ModelMBeanInfo (with Descriptors) are
customized and set on the ModelMBean, the ModelMBean be
registered with the MBeanServer.

If the ModelMBean is currently registered, this method throws
a

RuntimeOperationsException

wrapping an

IllegalStateException

If the given

inModelMBeanInfo

does not contain any

ModelMBeanNotificationInfo

for the

GENERIC

or

ATTRIBUTE_CHANGE

notifications, then the
RequiredModelMBean will supply its own default

ModelMBeanNotificationInfo

s for
those missing notifications.

**Specified by:**
- setModelMBeanInfo

in interface

ModelMBean

**Parameters:**
- mbi

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

#### public void setManagedResource​(
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

**Specified by:**
- setManagedResource

in interface

ModelMBean

**Parameters:**
- mr

- Object that is the managed resource
- mr_type

- The type of reference for the managed resource.

Can be: "ObjectReference", "Handle", "IOR", "EJBHandle",
or "RMIReference".

In this implementation only "ObjectReference" is supported.

**Throws:**
- MBeanException

- The initializer of the object has
thrown an exception.
- InstanceNotFoundException

- The managed resource
object could not be found
- InvalidTargetObjectTypeException

- The managed
resource type should be "ObjectReference".
- RuntimeOperationsException

- Wraps a

RuntimeException

when setting the resource.

---

#### public void load()
throws
MBeanException
,

RuntimeOperationsException
,

InstanceNotFoundException

Instantiates this MBean instance with the data found for
the MBean in the persistent store. The data loaded could include
attribute and operation values.

This method should be called during construction or
initialization of this instance, and before the MBean is
registered with the MBeanServer.

If the implementation of this class does not support
persistence, an

MBeanException

wrapping a

ServiceNotFoundException

is thrown.

**Specified by:**
- load

in interface

PersistentMBean

**Throws:**
- MBeanException

- Wraps another exception, or
persistence is not supported
- RuntimeOperationsException

- Wraps exceptions from the
persistence mechanism
- InstanceNotFoundException

- Could not find or load
this MBean from persistent storage

---

#### public void store()
throws
MBeanException
,

RuntimeOperationsException
,

InstanceNotFoundException

Captures the current state of this MBean instance and writes
it out to the persistent store. The state stored could include
attribute and operation values.

If the implementation of this class does not support
persistence, an

MBeanException

wrapping a

ServiceNotFoundException

is thrown.

Persistence policy from the MBean and attribute descriptor
is used to guide execution of this method. The MBean should be
stored if 'persistPolicy' field is:

```java
!= "never"
= "always"
= "onTimer" and now > 'lastPersistTime' + 'persistPeriod'
= "NoMoreOftenThan" and now > 'lastPersistTime' + 'persistPeriod'
= "onUnregister"
```

Do not store the MBean if 'persistPolicy' field is:

```java
= "never"
= "onUpdate"
= "onTimer" && now < 'lastPersistTime' + 'persistPeriod'
```

**Specified by:**
- store

in interface

PersistentMBean

**Throws:**
- MBeanException

- Wraps another exception, or
persistence is not supported
- RuntimeOperationsException

- Wraps exceptions from the
persistence mechanism
- InstanceNotFoundException

- Could not find/access the
persistent store

---

#### public
MBeanInfo
getMBeanInfo()

Returns the attributes, operations, constructors and notifications
that this RequiredModelMBean exposes for management.

**Specified by:**
- getMBeanInfo

in interface

DynamicMBean

**Returns:**
- An instance of ModelMBeanInfo allowing retrieval all
attributes, operations, and Notifications of this MBean.

---

#### public
Object
invoke​(
String
opName,

Object
[] opArgs,

String
[] sig)
throws
MBeanException
,

ReflectionException

Invokes a method on or through a RequiredModelMBean and returns
the result of the method execution.

If the given method to be invoked, together with the provided
signature, matches one of RequiredModelMbean
accessible methods, this one will be call. Otherwise the call to
the given method will be tried on the managed resource.

The last value returned by an operation may be cached in
the operation's descriptor which
is in the ModelMBeanOperationInfo's descriptor.
The valid value will be in the 'value' field if there is one.
If the 'currencyTimeLimit' field in the descriptor is:

- <0

Then the value is not cached and is never valid.
The operation method is invoked.
The 'value' and 'lastUpdatedTimeStamp' fields are cleared.
- =0

Then the value is always cached and always valid.
The 'value' field is returned. If there is no 'value' field
then the operation method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields are set to
the operation's return value and the current time stamp.
- >0

Represents the number of seconds that the 'value'
field is valid.
The 'value' field is no longer valid when
'lastUpdatedTimeStamp' + 'currencyTimeLimit' > Now.

- When 'value' is valid, 'value' is returned.
- When 'value' is no longer valid then the operation
method is invoked. The 'lastUpdatedTimeStamp' field
and `value' fields are updated.

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

**Specified by:**
- invoke

in interface

DynamicMBean

**Parameters:**
- opName

- The name of the method to be invoked. The
name can be the fully qualified method name including the
classname, or just the method name if the classname is
defined in the 'class' field of the operation descriptor.
- opArgs

- An array containing the parameters to be set
when the operation is invoked
- sig

- An array containing the signature of the
operation. The class objects will be loaded using the same
class loader as the one used for loading the MBean on which
the operation was invoked.

**Returns:**
- The object returned by the method, which represents the
result of invoking the method on the specified managed resource.

**Throws:**
- MBeanException

- Wraps one of the following Exceptions:

- An Exception thrown by the managed object's invoked method.
- ServiceNotFoundException

: No ModelMBeanOperationInfo or
no descriptor defined for the specified operation or the managed
resource is null.
- InvalidTargetObjectTypeException

: The 'targetType'
field value is not 'objectReference'.
- ReflectionException

- Wraps an

Exception

thrown while trying to invoke the method.
- RuntimeOperationsException

- Wraps an

IllegalArgumentException

Method name is null.

---

#### public
Object
getAttribute​(
String
attrName)
throws
AttributeNotFoundException
,

MBeanException
,

ReflectionException

Returns the value of a specific attribute defined for this
ModelMBean.
The last value returned by an attribute may be cached in the
attribute's descriptor.
The valid value will be in the 'value' field if there is one.
If the 'currencyTimeLimit' field in the descriptor is:

- <0

Then the value is not cached and is never valid.
The getter method is invoked for the attribute.
The 'value' and 'lastUpdatedTimeStamp' fields are cleared.
- =0

Then the value is always cached and always valid.
The 'value' field is returned. If there is no'value' field
then the getter method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields are set
to the attribute's value and the current time stamp.
- >0

Represents the number of seconds that the 'value'
field is valid.
The 'value' field is no longer valid when
'lastUpdatedTimeStamp' + 'currencyTimeLimit' > Now.

- When 'value' is valid, 'value' is returned.
- When 'value' is no longer valid then the getter
method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields
are updated.

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

If the 'getMethod' field contains the name of a valid
operation descriptor, then the method described by the
operation descriptor is executed. The response from the
method is returned as the value of the attribute. If the
operation fails or the returned value is not compatible with
the declared type of the attribute, an exception will be thrown.

If no 'getMethod' field is defined then the default value of the
attribute is returned. If the returned value is not compatible with
the declared type of the attribute, an exception will be thrown.

The declared type of the attribute is the String returned by

MBeanAttributeInfo.getType()

. A value is compatible
with this type if one of the following is true:

- the value is null;
- the declared name is a primitive type name (such as "int")
and the value is an instance of the corresponding wrapper
type (such as java.lang.Integer);
- the name of the value's class is identical to the declared name;
- the declared name can be loaded by the value's class loader and
produces a class to which the value can be assigned.

In this implementation, in every case where the getMethod needs to
be called, because the method is invoked through the standard "invoke"
method and thus needs operationInfo, an operation must be specified
for that getMethod so that the invocation works correctly.

**Specified by:**
- getAttribute

in interface

DynamicMBean

**Parameters:**
- attrName

- A String specifying the name of the
attribute to be retrieved. It must match the name of a
ModelMBeanAttributeInfo.

**Returns:**
- The value of the retrieved attribute from the
descriptor 'value' field or from the invocation of the
operation in the 'getMethod' field of the descriptor.

**Throws:**
- AttributeNotFoundException

- The specified attribute is
not accessible in the MBean.
The following cases may result in an AttributeNotFoundException:

- No ModelMBeanInfo was found for the Model MBean.
- No ModelMBeanAttributeInfo was found for the specified
attribute name.
- The ModelMBeanAttributeInfo isReadable method returns
'false'.
- MBeanException

- Wraps one of the following Exceptions:

- InvalidAttributeValueException

: A wrong value type
was received from the attribute's getter method or
no 'getMethod' field defined in the descriptor for
the attribute and no default value exists.
- ServiceNotFoundException

: No
ModelMBeanOperationInfo defined for the attribute's
getter method or no descriptor associated with the
ModelMBeanOperationInfo or the managed resource is
null.
- InvalidTargetObjectTypeException

The 'targetType'
field value is not 'objectReference'.
- An Exception thrown by the managed object's getter.
- ReflectionException

- Wraps an

Exception

thrown while trying to invoke the getter.
- RuntimeOperationsException

- Wraps an

IllegalArgumentException

: The attribute name in
parameter is null.

**See Also:**
- setAttribute(javax.management.Attribute)

---

#### public
AttributeList
getAttributes​(
String
[] attrNames)

Returns the values of several attributes in the ModelMBean.
Executes a getAttribute for each attribute name in the
attrNames array passed in.

**Specified by:**
- getAttributes

in interface

DynamicMBean

**Parameters:**
- attrNames

- A String array of names of the attributes
to be retrieved.

**Returns:**
- The array of the retrieved attributes.

**Throws:**
- RuntimeOperationsException

- Wraps an

IllegalArgumentException

: The object name in parameter is
null or attributes in parameter is null.

**See Also:**
- setAttributes(javax.management.AttributeList)

---

#### public void setAttribute​(
Attribute
attribute)
throws
AttributeNotFoundException
,

InvalidAttributeValueException
,

MBeanException
,

ReflectionException

Sets the value of a specific attribute of a named ModelMBean.

If the 'setMethod' field of the attribute's descriptor
contains the name of a valid operation descriptor, then the
method described by the operation descriptor is executed.
In this implementation, the operation descriptor must be specified
correctly and assigned to the modelMBeanInfo so that the 'setMethod'
works correctly.
The response from the method is set as the value of the attribute
in the descriptor.

If currencyTimeLimit is > 0, then the new value for the
attribute is cached in the attribute descriptor's
'value' field and the 'lastUpdatedTimeStamp' field is set to
the current time stamp.

If the persist field of the attribute's descriptor is not null
then Persistence policy from the attribute descriptor is used to
guide storing the attribute in a persistent store.

Store the MBean if 'persistPolicy' field is:

- != "never"
- = "always"
- = "onUpdate"
- = "onTimer" and now > 'lastPersistTime' + 'persistPeriod'
- = "NoMoreOftenThan" and now > 'lastPersistTime' +
'persistPeriod'

Do not store the MBean if 'persistPolicy' field is:

- = "never"
- = = "onTimer" && now < 'lastPersistTime' + 'persistPeriod'
- = "onUnregister"
- = = "NoMoreOftenThan" and now < 'lastPersistTime' +
'persistPeriod'

The ModelMBeanInfo of the Model MBean is stored in a file.

**Specified by:**
- setAttribute

in interface

DynamicMBean

**Parameters:**
- attribute

- The Attribute instance containing the name of
the attribute to be set and the value it is to be set to.

**Throws:**
- AttributeNotFoundException

- The specified attribute is
not accessible in the MBean.

The following cases may result in an AttributeNotFoundException:

- No ModelMBeanAttributeInfo is found for the specified
attribute.
- The ModelMBeanAttributeInfo's isWritable method returns
'false'.
- InvalidAttributeValueException

- No descriptor is defined
for the specified attribute.
- MBeanException

- Wraps one of the following Exceptions:

- An Exception thrown by the managed object's setter.
- A

ServiceNotFoundException

if a setMethod field is
defined in the descriptor for the attribute and the managed
resource is null; or if no setMethod field is defined and
caching is not enabled for the attribute.
Note that if there is no getMethod field either, then caching
is automatically enabled.
- InvalidTargetObjectTypeException

The 'targetType'
field value is not 'objectReference'.
- An Exception thrown by the managed object's getter.
- ReflectionException

- Wraps an

Exception

thrown while trying to invoke the setter.
- RuntimeOperationsException

- Wraps an

IllegalArgumentException

: The attribute in parameter is
null.

**See Also:**
- getAttribute(java.lang.String)

---

#### public
AttributeList
setAttributes​(
AttributeList
attributes)

Sets the values of an array of attributes of this ModelMBean.
Executes the setAttribute() method for each attribute in the list.

**Specified by:**
- setAttributes

in interface

DynamicMBean

**Parameters:**
- attributes

- A list of attributes: The identification of the
attributes to be set and the values they are to be set to.

**Returns:**
- The array of attributes that were set, with their new
values in Attribute instances.

**Throws:**
- RuntimeOperationsException

- Wraps an

IllegalArgumentException

: The object name in parameter
is null or attributes in parameter is null.

**See Also:**
- getAttributes(java.lang.String[])

---

#### public void addNotificationListener​(
NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
throws
IllegalArgumentException

Registers an object which implements the NotificationListener
interface as a listener. This
object's 'handleNotification()' method will be invoked when any
notification is issued through or by the ModelMBean. This does
not include attributeChangeNotifications. They must be registered
for independently.

**Specified by:**
- addNotificationListener

in interface

NotificationBroadcaster

**Parameters:**
- listener

- The listener object which will handles
notifications emitted by the registered MBean.
- filter

- The filter object. If null, no filtering will be
performed before handling notifications.
- handback

- The context to be sent to the listener with
the notification when a notification is emitted.

**Throws:**
- IllegalArgumentException

- The listener cannot be null.

**See Also:**
- removeNotificationListener(javax.management.NotificationListener)

---

#### public void removeNotificationListener​(
NotificationListener
listener)
throws
ListenerNotFoundException

Removes a listener for Notifications from the RequiredModelMBean.

**Specified by:**
- removeNotificationListener

in interface

NotificationBroadcaster

**Parameters:**
- listener

- The listener name which was handling notifications
emitted by the registered MBean.
This method will remove all information related to this listener.

**Throws:**
- ListenerNotFoundException

- The listener is not registered
in the MBean or is null.

**See Also:**
- addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

---

#### public
MBeanNotificationInfo
[] getNotificationInfo()

Returns the array of Notifications always generated by the
RequiredModelMBean.

RequiredModelMBean may always send also two additional notifications:

- One with descriptor

"name=GENERIC,descriptorType=notification,log=T,severity=6,displayName=jmx.modelmbean.generic"
- Second is a standard attribute change notification
with descriptor

"name=ATTRIBUTE_CHANGE,descriptorType=notification,log=T,severity=6,displayName=jmx.attribute.change"

Thus these two notifications are always added to those specified
by the application.

**Specified by:**
- getNotificationInfo

in interface

NotificationBroadcaster

**Returns:**
- MBeanNotificationInfo[]

---

#### protected
ClassLoaderRepository
getClassLoaderRepository()

Return the Class Loader Repository used to perform class loading.
Subclasses may wish to redefine this method in order to return
the appropriate

ClassLoaderRepository

that should be used in this object.

**Returns:**
- the Class Loader Repository.

---

#### public
ObjectName
preRegister​(
MBeanServer
server,

ObjectName
name)
throws
Exception

Allows the MBean to perform any operations it needs before
being registered in the MBean server. If the name of the MBean
is not specified, the MBean can provide a name for its
registration. If any exception is raised, the MBean will not be
registered in the MBean server.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.preRegister(server, name)

in its own

preRegister

implementation.

**Specified by:**
- preRegister

in interface

MBeanRegistration

**Parameters:**
- server

- The MBean server in which the MBean will be registered.
- name

- The object name of the MBean. This name is null if
the name parameter to one of the

createMBean

or

registerMBean

methods in the

MBeanServer

interface is null. In that case, this method must return a
non-null ObjectName for the new MBean.

**Returns:**
- The name under which the MBean is to be registered.
This value must not be null. If the

name

parameter is not null, it will usually but not necessarily be
the returned value.

**Throws:**
- Exception

- This exception will be caught by
the MBean server and re-thrown as an

MBeanRegistrationException

.

---

#### public void postRegister​(
Boolean
registrationDone)

Allows the MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.postRegister(registrationDone)

in its own

postRegister

implementation.

**Specified by:**
- postRegister

in interface

MBeanRegistration

**Parameters:**
- registrationDone

- Indicates whether or not the MBean has
been successfully registered in the MBean server. The value
false means that the registration phase has failed.

---

#### public void preDeregister()
throws
Exception

Allows the MBean to perform any operations it needs before
being unregistered by the MBean server.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.preDeregister()

in its own

preDeregister

implementation.

**Specified by:**
- preDeregister

in interface

MBeanRegistration

**Throws:**
- Exception

- This exception will be caught by
the MBean server and re-thrown as an

MBeanRegistrationException

.

---

#### public void postDeregister()

Allows the MBean to perform any operations needed after having been
unregistered in the MBean server.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.postDeregister()

in its own

postDeregister

implementation.

**Specified by:**
- postDeregister

in interface

MBeanRegistration

---

### Additional Sections

#### Class RequiredModelMBean

java.lang.Object

- javax.management.modelmbean.RequiredModelMBean

javax.management.modelmbean.RequiredModelMBean

**All Implemented Interfaces:** DynamicMBean

,

MBeanRegistration

,

ModelMBean

,

ModelMBeanNotificationBroadcaster

,

NotificationBroadcaster

,

NotificationEmitter

,

PersistentMBean

```java
public class
RequiredModelMBean

extends
Object

implements
ModelMBean
,
MBeanRegistration
,
NotificationEmitter
```

This class is the implementation of a ModelMBean. An appropriate
implementation of a ModelMBean must be shipped with every JMX Agent
and the class must be named RequiredModelMBean.

Java resources wishing to be manageable instantiate the
RequiredModelMBean using the MBeanServer's createMBean method.
The resource then sets the MBeanInfo and Descriptors for the
RequiredModelMBean instance. The attributes and operations exposed
via the ModelMBeanInfo for the ModelMBean are accessible
from MBeans, connectors/adaptors like other MBeans. Through the
Descriptors, values and methods in the managed application can be
defined and mapped to attributes and operations of the ModelMBean.
This mapping can be defined in an XML formatted file or dynamically and
programmatically at runtime.

Every RequiredModelMBean which is instantiated in the MBeanServer
becomes manageable:

its attributes and operations become remotely accessible through the
connectors/adaptors connected to that MBeanServer.

A Java object cannot be registered in the MBeanServer unless it is a
JMX compliant MBean. By instantiating a RequiredModelMBean, resources
are guaranteed that the MBean is valid.

MBeanException and RuntimeOperationsException must be thrown on every
public method. This allows for wrapping exceptions from distributed
communications (RMI, EJB, etc.)

**Since:** 1.5

public class

RequiredModelMBean

extends

Object

implements

ModelMBean

,

MBeanRegistration

,

NotificationEmitter

This class is the implementation of a ModelMBean. An appropriate
implementation of a ModelMBean must be shipped with every JMX Agent
and the class must be named RequiredModelMBean.

Java resources wishing to be manageable instantiate the
RequiredModelMBean using the MBeanServer's createMBean method.
The resource then sets the MBeanInfo and Descriptors for the
RequiredModelMBean instance. The attributes and operations exposed
via the ModelMBeanInfo for the ModelMBean are accessible
from MBeans, connectors/adaptors like other MBeans. Through the
Descriptors, values and methods in the managed application can be
defined and mapped to attributes and operations of the ModelMBean.
This mapping can be defined in an XML formatted file or dynamically and
programmatically at runtime.

Every RequiredModelMBean which is instantiated in the MBeanServer
becomes manageable:

its attributes and operations become remotely accessible through the
connectors/adaptors connected to that MBeanServer.

A Java object cannot be registered in the MBeanServer unless it is a
JMX compliant MBean. By instantiating a RequiredModelMBean, resources
are guaranteed that the MBean is valid.

MBeanException and RuntimeOperationsException must be thrown on every
public method. This allows for wrapping exceptions from distributed
communications (RMI, EJB, etc.)

Java resources wishing to be manageable instantiate the
RequiredModelMBean using the MBeanServer's createMBean method.
The resource then sets the MBeanInfo and Descriptors for the
RequiredModelMBean instance. The attributes and operations exposed
via the ModelMBeanInfo for the ModelMBean are accessible
from MBeans, connectors/adaptors like other MBeans. Through the
Descriptors, values and methods in the managed application can be
defined and mapped to attributes and operations of the ModelMBean.
This mapping can be defined in an XML formatted file or dynamically and
programmatically at runtime.

Every RequiredModelMBean which is instantiated in the MBeanServer
becomes manageable:

its attributes and operations become remotely accessible through the
connectors/adaptors connected to that MBeanServer.

A Java object cannot be registered in the MBeanServer unless it is a
JMX compliant MBean. By instantiating a RequiredModelMBean, resources
are guaranteed that the MBean is valid.

MBeanException and RuntimeOperationsException must be thrown on every
public method. This allows for wrapping exceptions from distributed
communications (RMI, EJB, etc.)

Every RequiredModelMBean which is instantiated in the MBeanServer
becomes manageable:

its attributes and operations become remotely accessible through the
connectors/adaptors connected to that MBeanServer.

A Java object cannot be registered in the MBeanServer unless it is a
JMX compliant MBean. By instantiating a RequiredModelMBean, resources
are guaranteed that the MBean is valid.

MBeanException and RuntimeOperationsException must be thrown on every
public method. This allows for wrapping exceptions from distributed
communications (RMI, EJB, etc.)

A Java object cannot be registered in the MBeanServer unless it is a
JMX compliant MBean. By instantiating a RequiredModelMBean, resources
are guaranteed that the MBean is valid.

MBeanException and RuntimeOperationsException must be thrown on every
public method. This allows for wrapping exceptions from distributed
communications (RMI, EJB, etc.)

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RequiredModelMBean

()

Constructs an

RequiredModelMBean

with an empty
ModelMBeanInfo.

RequiredModelMBean

​(

ModelMBeanInfo

mbi)

Constructs a RequiredModelMBean object using ModelMBeanInfo passed in.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addNotificationListener

​(

NotificationListener

listener,

NotificationFilter

filter,

Object

handback)

Registers an object which implements the NotificationListener
interface as a listener.

Object

getAttribute

​(

String

attrName)

Returns the value of a specific attribute defined for this
ModelMBean.

AttributeList

getAttributes

​(

String

[] attrNames)

Returns the values of several attributes in the ModelMBean.

protected

ClassLoaderRepository

getClassLoaderRepository

()

Return the Class Loader Repository used to perform class loading.

MBeanInfo

getMBeanInfo

()

Returns the attributes, operations, constructors and notifications
that this RequiredModelMBean exposes for management.

MBeanNotificationInfo

[]

getNotificationInfo

()

Returns the array of Notifications always generated by the
RequiredModelMBean.

Object

invoke

​(

String

opName,

Object

[] opArgs,

String

[] sig)

Invokes a method on or through a RequiredModelMBean and returns
the result of the method execution.

void

load

()

Instantiates this MBean instance with the data found for
the MBean in the persistent store.

void

postDeregister

()

Allows the MBean to perform any operations needed after having been
unregistered in the MBean server.

void

postRegister

​(

Boolean

registrationDone)

Allows the MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

void

preDeregister

()

Allows the MBean to perform any operations it needs before
being unregistered by the MBean server.

ObjectName

preRegister

​(

MBeanServer

server,

ObjectName

name)

Allows the MBean to perform any operations it needs before
being registered in the MBean server.

void

removeNotificationListener

​(

NotificationListener

listener)

Removes a listener for Notifications from the RequiredModelMBean.

void

setAttribute

​(

Attribute

attribute)

Sets the value of a specific attribute of a named ModelMBean.

AttributeList

setAttributes

​(

AttributeList

attributes)

Sets the values of an array of attributes of this ModelMBean.

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

mbi)

Initializes a ModelMBean object using ModelMBeanInfo passed in.

void

store

()

Captures the current state of this MBean instance and writes
it out to the persistent store.

- Methods declared in class java.lang.

Object

clone

,

equals

,

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

NotificationEmitter

removeNotificationListener

Constructor Summary

Constructors

Constructor

Description

RequiredModelMBean

()

Constructs an

RequiredModelMBean

with an empty
ModelMBeanInfo.

RequiredModelMBean

​(

ModelMBeanInfo

mbi)

Constructs a RequiredModelMBean object using ModelMBeanInfo passed in.

---

#### Constructor Summary

Constructs an

RequiredModelMBean

with an empty
ModelMBeanInfo.

Constructs a RequiredModelMBean object using ModelMBeanInfo passed in.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addNotificationListener

​(

NotificationListener

listener,

NotificationFilter

filter,

Object

handback)

Registers an object which implements the NotificationListener
interface as a listener.

Object

getAttribute

​(

String

attrName)

Returns the value of a specific attribute defined for this
ModelMBean.

AttributeList

getAttributes

​(

String

[] attrNames)

Returns the values of several attributes in the ModelMBean.

protected

ClassLoaderRepository

getClassLoaderRepository

()

Return the Class Loader Repository used to perform class loading.

MBeanInfo

getMBeanInfo

()

Returns the attributes, operations, constructors and notifications
that this RequiredModelMBean exposes for management.

MBeanNotificationInfo

[]

getNotificationInfo

()

Returns the array of Notifications always generated by the
RequiredModelMBean.

Object

invoke

​(

String

opName,

Object

[] opArgs,

String

[] sig)

Invokes a method on or through a RequiredModelMBean and returns
the result of the method execution.

void

load

()

Instantiates this MBean instance with the data found for
the MBean in the persistent store.

void

postDeregister

()

Allows the MBean to perform any operations needed after having been
unregistered in the MBean server.

void

postRegister

​(

Boolean

registrationDone)

Allows the MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

void

preDeregister

()

Allows the MBean to perform any operations it needs before
being unregistered by the MBean server.

ObjectName

preRegister

​(

MBeanServer

server,

ObjectName

name)

Allows the MBean to perform any operations it needs before
being registered in the MBean server.

void

removeNotificationListener

​(

NotificationListener

listener)

Removes a listener for Notifications from the RequiredModelMBean.

void

setAttribute

​(

Attribute

attribute)

Sets the value of a specific attribute of a named ModelMBean.

AttributeList

setAttributes

​(

AttributeList

attributes)

Sets the values of an array of attributes of this ModelMBean.

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

mbi)

Initializes a ModelMBean object using ModelMBeanInfo passed in.

void

store

()

Captures the current state of this MBean instance and writes
it out to the persistent store.

- Methods declared in class java.lang.

Object

clone

,

equals

,

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

NotificationEmitter

removeNotificationListener

---

#### Method Summary

Registers an object which implements the NotificationListener
interface as a listener.

Returns the value of a specific attribute defined for this
ModelMBean.

Returns the values of several attributes in the ModelMBean.

Return the Class Loader Repository used to perform class loading.

Returns the attributes, operations, constructors and notifications
that this RequiredModelMBean exposes for management.

Returns the array of Notifications always generated by the
RequiredModelMBean.

Invokes a method on or through a RequiredModelMBean and returns
the result of the method execution.

Instantiates this MBean instance with the data found for
the MBean in the persistent store.

Allows the MBean to perform any operations needed after having been
unregistered in the MBean server.

Allows the MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

Allows the MBean to perform any operations it needs before
being unregistered by the MBean server.

Allows the MBean to perform any operations it needs before
being registered in the MBean server.

Removes a listener for Notifications from the RequiredModelMBean.

Sets the value of a specific attribute of a named ModelMBean.

Sets the values of an array of attributes of this ModelMBean.

Sets the instance handle of the object against which to
execute all methods in this ModelMBean management interface
(MBeanInfo and Descriptors).

Initializes a ModelMBean object using ModelMBeanInfo passed in.

Captures the current state of this MBean instance and writes
it out to the persistent store.

Methods declared in class java.lang.

Object

clone

,

equals

,

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

NotificationEmitter

removeNotificationListener

---

#### Methods declared in interface javax.management. NotificationEmitter

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RequiredModelMBean

```java
public RequiredModelMBean()
throws
MBeanException
,

RuntimeOperationsException
```

Constructs an

RequiredModelMBean

with an empty
ModelMBeanInfo.

The RequiredModelMBean's MBeanInfo and Descriptors
can be customized using the

setModelMBeanInfo(javax.management.modelmbean.ModelMBeanInfo)

method.
After the RequiredModelMBean's MBeanInfo and Descriptors are
customized, the RequiredModelMBean can be registered with
the MBeanServer.

**Throws:** MBeanException

- Wraps a distributed communication Exception.
**Throws:** RuntimeOperationsException

- Wraps a

RuntimeException

during the construction of the object.

- RequiredModelMBean

```java
public RequiredModelMBean​(
ModelMBeanInfo
mbi)
throws
MBeanException
,

RuntimeOperationsException
```

Constructs a RequiredModelMBean object using ModelMBeanInfo passed in.
As long as the RequiredModelMBean is not registered
with the MBeanServer yet, the RequiredModelMBean's MBeanInfo and
Descriptors can be customized using the

setModelMBeanInfo(javax.management.modelmbean.ModelMBeanInfo)

method.
After the RequiredModelMBean's MBeanInfo and Descriptors are
customized, the RequiredModelMBean can be registered with the
MBeanServer.

**Parameters:** mbi

- The ModelMBeanInfo object to be used by the
RequiredModelMBean. The given ModelMBeanInfo is cloned
and modified as specified by

setModelMBeanInfo(javax.management.modelmbean.ModelMBeanInfo)
**Throws:** MBeanException

- Wraps a distributed communication Exception.
**Throws:** RuntimeOperationsException

- Wraps an
{link java.lang.IllegalArgumentException}:
The MBeanInfo passed in parameter is null.

============ METHOD DETAIL ==========

- Method Detail

- setModelMBeanInfo

```java
public void setModelMBeanInfo​(
ModelMBeanInfo
mbi)
throws
MBeanException
,

RuntimeOperationsException
```

Initializes a ModelMBean object using ModelMBeanInfo passed in.
This method makes it possible to set a customized ModelMBeanInfo on
the ModelMBean as long as it is not registered with the MBeanServer.

Once the ModelMBean's ModelMBeanInfo (with Descriptors) are
customized and set on the ModelMBean, the ModelMBean be
registered with the MBeanServer.

If the ModelMBean is currently registered, this method throws
a

RuntimeOperationsException

wrapping an

IllegalStateException

If the given

inModelMBeanInfo

does not contain any

ModelMBeanNotificationInfo

for the

GENERIC

or

ATTRIBUTE_CHANGE

notifications, then the
RequiredModelMBean will supply its own default

ModelMBeanNotificationInfo

s for
those missing notifications.

**Specified by:** setModelMBeanInfo

in interface

ModelMBean
**Parameters:** mbi

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
public void setManagedResource​(
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

**Specified by:** setManagedResource

in interface

ModelMBean
**Parameters:** mr

- Object that is the managed resource
**Parameters:** mr_type

- The type of reference for the managed resource.

Can be: "ObjectReference", "Handle", "IOR", "EJBHandle",
or "RMIReference".

In this implementation only "ObjectReference" is supported.
**Throws:** MBeanException

- The initializer of the object has
thrown an exception.
**Throws:** InstanceNotFoundException

- The managed resource
object could not be found
**Throws:** InvalidTargetObjectTypeException

- The managed
resource type should be "ObjectReference".
**Throws:** RuntimeOperationsException

- Wraps a

RuntimeException

when setting the resource.

- load

```java
public void load()
throws
MBeanException
,

RuntimeOperationsException
,

InstanceNotFoundException
```

Instantiates this MBean instance with the data found for
the MBean in the persistent store. The data loaded could include
attribute and operation values.

This method should be called during construction or
initialization of this instance, and before the MBean is
registered with the MBeanServer.

If the implementation of this class does not support
persistence, an

MBeanException

wrapping a

ServiceNotFoundException

is thrown.

**Specified by:** load

in interface

PersistentMBean
**Throws:** MBeanException

- Wraps another exception, or
persistence is not supported
**Throws:** RuntimeOperationsException

- Wraps exceptions from the
persistence mechanism
**Throws:** InstanceNotFoundException

- Could not find or load
this MBean from persistent storage

- store

```java
public void store()
throws
MBeanException
,

RuntimeOperationsException
,

InstanceNotFoundException
```

Captures the current state of this MBean instance and writes
it out to the persistent store. The state stored could include
attribute and operation values.

If the implementation of this class does not support
persistence, an

MBeanException

wrapping a

ServiceNotFoundException

is thrown.

Persistence policy from the MBean and attribute descriptor
is used to guide execution of this method. The MBean should be
stored if 'persistPolicy' field is:

```java
!= "never"
= "always"
= "onTimer" and now > 'lastPersistTime' + 'persistPeriod'
= "NoMoreOftenThan" and now > 'lastPersistTime' + 'persistPeriod'
= "onUnregister"
```

Do not store the MBean if 'persistPolicy' field is:

```java
= "never"
= "onUpdate"
= "onTimer" && now < 'lastPersistTime' + 'persistPeriod'
```

**Specified by:** store

in interface

PersistentMBean
**Throws:** MBeanException

- Wraps another exception, or
persistence is not supported
**Throws:** RuntimeOperationsException

- Wraps exceptions from the
persistence mechanism
**Throws:** InstanceNotFoundException

- Could not find/access the
persistent store

- getMBeanInfo

```java
public
MBeanInfo
getMBeanInfo()
```

Returns the attributes, operations, constructors and notifications
that this RequiredModelMBean exposes for management.

**Specified by:** getMBeanInfo

in interface

DynamicMBean
**Returns:** An instance of ModelMBeanInfo allowing retrieval all
attributes, operations, and Notifications of this MBean.

- invoke

```java
public
Object
invoke​(
String
opName,

Object
[] opArgs,

String
[] sig)
throws
MBeanException
,

ReflectionException
```

Invokes a method on or through a RequiredModelMBean and returns
the result of the method execution.

If the given method to be invoked, together with the provided
signature, matches one of RequiredModelMbean
accessible methods, this one will be call. Otherwise the call to
the given method will be tried on the managed resource.

The last value returned by an operation may be cached in
the operation's descriptor which
is in the ModelMBeanOperationInfo's descriptor.
The valid value will be in the 'value' field if there is one.
If the 'currencyTimeLimit' field in the descriptor is:

- <0

Then the value is not cached and is never valid.
The operation method is invoked.
The 'value' and 'lastUpdatedTimeStamp' fields are cleared.
- =0

Then the value is always cached and always valid.
The 'value' field is returned. If there is no 'value' field
then the operation method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields are set to
the operation's return value and the current time stamp.
- >0

Represents the number of seconds that the 'value'
field is valid.
The 'value' field is no longer valid when
'lastUpdatedTimeStamp' + 'currencyTimeLimit' > Now.

- When 'value' is valid, 'value' is returned.
- When 'value' is no longer valid then the operation
method is invoked. The 'lastUpdatedTimeStamp' field
and `value' fields are updated.

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

**Specified by:** invoke

in interface

DynamicMBean
**Parameters:** opName

- The name of the method to be invoked. The
name can be the fully qualified method name including the
classname, or just the method name if the classname is
defined in the 'class' field of the operation descriptor.
**Parameters:** opArgs

- An array containing the parameters to be set
when the operation is invoked
**Parameters:** sig

- An array containing the signature of the
operation. The class objects will be loaded using the same
class loader as the one used for loading the MBean on which
the operation was invoked.
**Returns:** The object returned by the method, which represents the
result of invoking the method on the specified managed resource.
**Throws:** MBeanException

- Wraps one of the following Exceptions:

- An Exception thrown by the managed object's invoked method.
- ServiceNotFoundException

: No ModelMBeanOperationInfo or
no descriptor defined for the specified operation or the managed
resource is null.
- InvalidTargetObjectTypeException

: The 'targetType'
field value is not 'objectReference'.
**Throws:** ReflectionException

- Wraps an

Exception

thrown while trying to invoke the method.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

Method name is null.

- getAttribute

```java
public
Object
getAttribute​(
String
attrName)
throws
AttributeNotFoundException
,

MBeanException
,

ReflectionException
```

Returns the value of a specific attribute defined for this
ModelMBean.
The last value returned by an attribute may be cached in the
attribute's descriptor.
The valid value will be in the 'value' field if there is one.
If the 'currencyTimeLimit' field in the descriptor is:

- <0

Then the value is not cached and is never valid.
The getter method is invoked for the attribute.
The 'value' and 'lastUpdatedTimeStamp' fields are cleared.
- =0

Then the value is always cached and always valid.
The 'value' field is returned. If there is no'value' field
then the getter method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields are set
to the attribute's value and the current time stamp.
- >0

Represents the number of seconds that the 'value'
field is valid.
The 'value' field is no longer valid when
'lastUpdatedTimeStamp' + 'currencyTimeLimit' > Now.

- When 'value' is valid, 'value' is returned.
- When 'value' is no longer valid then the getter
method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields
are updated.

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

If the 'getMethod' field contains the name of a valid
operation descriptor, then the method described by the
operation descriptor is executed. The response from the
method is returned as the value of the attribute. If the
operation fails or the returned value is not compatible with
the declared type of the attribute, an exception will be thrown.

If no 'getMethod' field is defined then the default value of the
attribute is returned. If the returned value is not compatible with
the declared type of the attribute, an exception will be thrown.

The declared type of the attribute is the String returned by

MBeanAttributeInfo.getType()

. A value is compatible
with this type if one of the following is true:

- the value is null;
- the declared name is a primitive type name (such as "int")
and the value is an instance of the corresponding wrapper
type (such as java.lang.Integer);
- the name of the value's class is identical to the declared name;
- the declared name can be loaded by the value's class loader and
produces a class to which the value can be assigned.

In this implementation, in every case where the getMethod needs to
be called, because the method is invoked through the standard "invoke"
method and thus needs operationInfo, an operation must be specified
for that getMethod so that the invocation works correctly.

**Specified by:** getAttribute

in interface

DynamicMBean
**Parameters:** attrName

- A String specifying the name of the
attribute to be retrieved. It must match the name of a
ModelMBeanAttributeInfo.
**Returns:** The value of the retrieved attribute from the
descriptor 'value' field or from the invocation of the
operation in the 'getMethod' field of the descriptor.
**Throws:** AttributeNotFoundException

- The specified attribute is
not accessible in the MBean.
The following cases may result in an AttributeNotFoundException:

- No ModelMBeanInfo was found for the Model MBean.
- No ModelMBeanAttributeInfo was found for the specified
attribute name.
- The ModelMBeanAttributeInfo isReadable method returns
'false'.
**Throws:** MBeanException

- Wraps one of the following Exceptions:

- InvalidAttributeValueException

: A wrong value type
was received from the attribute's getter method or
no 'getMethod' field defined in the descriptor for
the attribute and no default value exists.
- ServiceNotFoundException

: No
ModelMBeanOperationInfo defined for the attribute's
getter method or no descriptor associated with the
ModelMBeanOperationInfo or the managed resource is
null.
- InvalidTargetObjectTypeException

The 'targetType'
field value is not 'objectReference'.
- An Exception thrown by the managed object's getter.
**Throws:** ReflectionException

- Wraps an

Exception

thrown while trying to invoke the getter.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

: The attribute name in
parameter is null.
**See Also:** setAttribute(javax.management.Attribute)

- getAttributes

```java
public
AttributeList
getAttributes​(
String
[] attrNames)
```

Returns the values of several attributes in the ModelMBean.
Executes a getAttribute for each attribute name in the
attrNames array passed in.

**Specified by:** getAttributes

in interface

DynamicMBean
**Parameters:** attrNames

- A String array of names of the attributes
to be retrieved.
**Returns:** The array of the retrieved attributes.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

: The object name in parameter is
null or attributes in parameter is null.
**See Also:** setAttributes(javax.management.AttributeList)

- setAttribute

```java
public void setAttribute​(
Attribute
attribute)
throws
AttributeNotFoundException
,

InvalidAttributeValueException
,

MBeanException
,

ReflectionException
```

Sets the value of a specific attribute of a named ModelMBean.

If the 'setMethod' field of the attribute's descriptor
contains the name of a valid operation descriptor, then the
method described by the operation descriptor is executed.
In this implementation, the operation descriptor must be specified
correctly and assigned to the modelMBeanInfo so that the 'setMethod'
works correctly.
The response from the method is set as the value of the attribute
in the descriptor.

If currencyTimeLimit is > 0, then the new value for the
attribute is cached in the attribute descriptor's
'value' field and the 'lastUpdatedTimeStamp' field is set to
the current time stamp.

If the persist field of the attribute's descriptor is not null
then Persistence policy from the attribute descriptor is used to
guide storing the attribute in a persistent store.

Store the MBean if 'persistPolicy' field is:

- != "never"
- = "always"
- = "onUpdate"
- = "onTimer" and now > 'lastPersistTime' + 'persistPeriod'
- = "NoMoreOftenThan" and now > 'lastPersistTime' +
'persistPeriod'

Do not store the MBean if 'persistPolicy' field is:

- = "never"
- = = "onTimer" && now < 'lastPersistTime' + 'persistPeriod'
- = "onUnregister"
- = = "NoMoreOftenThan" and now < 'lastPersistTime' +
'persistPeriod'

The ModelMBeanInfo of the Model MBean is stored in a file.

**Specified by:** setAttribute

in interface

DynamicMBean
**Parameters:** attribute

- The Attribute instance containing the name of
the attribute to be set and the value it is to be set to.
**Throws:** AttributeNotFoundException

- The specified attribute is
not accessible in the MBean.

The following cases may result in an AttributeNotFoundException:

- No ModelMBeanAttributeInfo is found for the specified
attribute.
- The ModelMBeanAttributeInfo's isWritable method returns
'false'.
**Throws:** InvalidAttributeValueException

- No descriptor is defined
for the specified attribute.
**Throws:** MBeanException

- Wraps one of the following Exceptions:

- An Exception thrown by the managed object's setter.
- A

ServiceNotFoundException

if a setMethod field is
defined in the descriptor for the attribute and the managed
resource is null; or if no setMethod field is defined and
caching is not enabled for the attribute.
Note that if there is no getMethod field either, then caching
is automatically enabled.
- InvalidTargetObjectTypeException

The 'targetType'
field value is not 'objectReference'.
- An Exception thrown by the managed object's getter.
**Throws:** ReflectionException

- Wraps an

Exception

thrown while trying to invoke the setter.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

: The attribute in parameter is
null.
**See Also:** getAttribute(java.lang.String)

- setAttributes

```java
public
AttributeList
setAttributes​(
AttributeList
attributes)
```

Sets the values of an array of attributes of this ModelMBean.
Executes the setAttribute() method for each attribute in the list.

**Specified by:** setAttributes

in interface

DynamicMBean
**Parameters:** attributes

- A list of attributes: The identification of the
attributes to be set and the values they are to be set to.
**Returns:** The array of attributes that were set, with their new
values in Attribute instances.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

: The object name in parameter
is null or attributes in parameter is null.
**See Also:** getAttributes(java.lang.String[])

- addNotificationListener

```java
public void addNotificationListener​(
NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
throws
IllegalArgumentException
```

Registers an object which implements the NotificationListener
interface as a listener. This
object's 'handleNotification()' method will be invoked when any
notification is issued through or by the ModelMBean. This does
not include attributeChangeNotifications. They must be registered
for independently.

**Specified by:** addNotificationListener

in interface

NotificationBroadcaster
**Parameters:** listener

- The listener object which will handles
notifications emitted by the registered MBean.
**Parameters:** filter

- The filter object. If null, no filtering will be
performed before handling notifications.
**Parameters:** handback

- The context to be sent to the listener with
the notification when a notification is emitted.
**Throws:** IllegalArgumentException

- The listener cannot be null.
**See Also:** removeNotificationListener(javax.management.NotificationListener)

- removeNotificationListener

```java
public void removeNotificationListener​(
NotificationListener
listener)
throws
ListenerNotFoundException
```

Removes a listener for Notifications from the RequiredModelMBean.

**Specified by:** removeNotificationListener

in interface

NotificationBroadcaster
**Parameters:** listener

- The listener name which was handling notifications
emitted by the registered MBean.
This method will remove all information related to this listener.
**Throws:** ListenerNotFoundException

- The listener is not registered
in the MBean or is null.
**See Also:** addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

- getNotificationInfo

```java
public
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns the array of Notifications always generated by the
RequiredModelMBean.

RequiredModelMBean may always send also two additional notifications:

- One with descriptor

"name=GENERIC,descriptorType=notification,log=T,severity=6,displayName=jmx.modelmbean.generic"
- Second is a standard attribute change notification
with descriptor

"name=ATTRIBUTE_CHANGE,descriptorType=notification,log=T,severity=6,displayName=jmx.attribute.change"

Thus these two notifications are always added to those specified
by the application.

**Specified by:** getNotificationInfo

in interface

NotificationBroadcaster
**Returns:** MBeanNotificationInfo[]

- getClassLoaderRepository

```java
protected
ClassLoaderRepository
getClassLoaderRepository()
```

Return the Class Loader Repository used to perform class loading.
Subclasses may wish to redefine this method in order to return
the appropriate

ClassLoaderRepository

that should be used in this object.

**Returns:** the Class Loader Repository.

- preRegister

```java
public
ObjectName
preRegister​(
MBeanServer
server,

ObjectName
name)
throws
Exception
```

Allows the MBean to perform any operations it needs before
being registered in the MBean server. If the name of the MBean
is not specified, the MBean can provide a name for its
registration. If any exception is raised, the MBean will not be
registered in the MBean server.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.preRegister(server, name)

in its own

preRegister

implementation.

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** server

- The MBean server in which the MBean will be registered.
**Parameters:** name

- The object name of the MBean. This name is null if
the name parameter to one of the

createMBean

or

registerMBean

methods in the

MBeanServer

interface is null. In that case, this method must return a
non-null ObjectName for the new MBean.
**Returns:** The name under which the MBean is to be registered.
This value must not be null. If the

name

parameter is not null, it will usually but not necessarily be
the returned value.
**Throws:** Exception

- This exception will be caught by
the MBean server and re-thrown as an

MBeanRegistrationException

.

- postRegister

```java
public void postRegister​(
Boolean
registrationDone)
```

Allows the MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.postRegister(registrationDone)

in its own

postRegister

implementation.

**Specified by:** postRegister

in interface

MBeanRegistration
**Parameters:** registrationDone

- Indicates whether or not the MBean has
been successfully registered in the MBean server. The value
false means that the registration phase has failed.

- preDeregister

```java
public void preDeregister()
throws
Exception
```

Allows the MBean to perform any operations it needs before
being unregistered by the MBean server.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.preDeregister()

in its own

preDeregister

implementation.

**Specified by:** preDeregister

in interface

MBeanRegistration
**Throws:** Exception

- This exception will be caught by
the MBean server and re-thrown as an

MBeanRegistrationException

.

- postDeregister

```java
public void postDeregister()
```

Allows the MBean to perform any operations needed after having been
unregistered in the MBean server.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.postDeregister()

in its own

postDeregister

implementation.

**Specified by:** postDeregister

in interface

MBeanRegistration

Constructor Detail

- RequiredModelMBean

```java
public RequiredModelMBean()
throws
MBeanException
,

RuntimeOperationsException
```

Constructs an

RequiredModelMBean

with an empty
ModelMBeanInfo.

The RequiredModelMBean's MBeanInfo and Descriptors
can be customized using the

setModelMBeanInfo(javax.management.modelmbean.ModelMBeanInfo)

method.
After the RequiredModelMBean's MBeanInfo and Descriptors are
customized, the RequiredModelMBean can be registered with
the MBeanServer.

**Throws:** MBeanException

- Wraps a distributed communication Exception.
**Throws:** RuntimeOperationsException

- Wraps a

RuntimeException

during the construction of the object.

- RequiredModelMBean

```java
public RequiredModelMBean​(
ModelMBeanInfo
mbi)
throws
MBeanException
,

RuntimeOperationsException
```

Constructs a RequiredModelMBean object using ModelMBeanInfo passed in.
As long as the RequiredModelMBean is not registered
with the MBeanServer yet, the RequiredModelMBean's MBeanInfo and
Descriptors can be customized using the

setModelMBeanInfo(javax.management.modelmbean.ModelMBeanInfo)

method.
After the RequiredModelMBean's MBeanInfo and Descriptors are
customized, the RequiredModelMBean can be registered with the
MBeanServer.

**Parameters:** mbi

- The ModelMBeanInfo object to be used by the
RequiredModelMBean. The given ModelMBeanInfo is cloned
and modified as specified by

setModelMBeanInfo(javax.management.modelmbean.ModelMBeanInfo)
**Throws:** MBeanException

- Wraps a distributed communication Exception.
**Throws:** RuntimeOperationsException

- Wraps an
{link java.lang.IllegalArgumentException}:
The MBeanInfo passed in parameter is null.

---

#### Constructor Detail

RequiredModelMBean

```java
public RequiredModelMBean()
throws
MBeanException
,

RuntimeOperationsException
```

Constructs an

RequiredModelMBean

with an empty
ModelMBeanInfo.

The RequiredModelMBean's MBeanInfo and Descriptors
can be customized using the

setModelMBeanInfo(javax.management.modelmbean.ModelMBeanInfo)

method.
After the RequiredModelMBean's MBeanInfo and Descriptors are
customized, the RequiredModelMBean can be registered with
the MBeanServer.

**Throws:** MBeanException

- Wraps a distributed communication Exception.
**Throws:** RuntimeOperationsException

- Wraps a

RuntimeException

during the construction of the object.

---

#### RequiredModelMBean

public RequiredModelMBean()
throws

MBeanException

,

RuntimeOperationsException

Constructs an

RequiredModelMBean

with an empty
ModelMBeanInfo.

The RequiredModelMBean's MBeanInfo and Descriptors
can be customized using the

setModelMBeanInfo(javax.management.modelmbean.ModelMBeanInfo)

method.
After the RequiredModelMBean's MBeanInfo and Descriptors are
customized, the RequiredModelMBean can be registered with
the MBeanServer.

The RequiredModelMBean's MBeanInfo and Descriptors
can be customized using the

setModelMBeanInfo(javax.management.modelmbean.ModelMBeanInfo)

method.
After the RequiredModelMBean's MBeanInfo and Descriptors are
customized, the RequiredModelMBean can be registered with
the MBeanServer.

RequiredModelMBean

```java
public RequiredModelMBean​(
ModelMBeanInfo
mbi)
throws
MBeanException
,

RuntimeOperationsException
```

Constructs a RequiredModelMBean object using ModelMBeanInfo passed in.
As long as the RequiredModelMBean is not registered
with the MBeanServer yet, the RequiredModelMBean's MBeanInfo and
Descriptors can be customized using the

setModelMBeanInfo(javax.management.modelmbean.ModelMBeanInfo)

method.
After the RequiredModelMBean's MBeanInfo and Descriptors are
customized, the RequiredModelMBean can be registered with the
MBeanServer.

**Parameters:** mbi

- The ModelMBeanInfo object to be used by the
RequiredModelMBean. The given ModelMBeanInfo is cloned
and modified as specified by

setModelMBeanInfo(javax.management.modelmbean.ModelMBeanInfo)
**Throws:** MBeanException

- Wraps a distributed communication Exception.
**Throws:** RuntimeOperationsException

- Wraps an
{link java.lang.IllegalArgumentException}:
The MBeanInfo passed in parameter is null.

---

#### RequiredModelMBean

public RequiredModelMBean​(

ModelMBeanInfo

mbi)
throws

MBeanException

,

RuntimeOperationsException

Constructs a RequiredModelMBean object using ModelMBeanInfo passed in.
As long as the RequiredModelMBean is not registered
with the MBeanServer yet, the RequiredModelMBean's MBeanInfo and
Descriptors can be customized using the

setModelMBeanInfo(javax.management.modelmbean.ModelMBeanInfo)

method.
After the RequiredModelMBean's MBeanInfo and Descriptors are
customized, the RequiredModelMBean can be registered with the
MBeanServer.

Method Detail

- setModelMBeanInfo

```java
public void setModelMBeanInfo​(
ModelMBeanInfo
mbi)
throws
MBeanException
,

RuntimeOperationsException
```

Initializes a ModelMBean object using ModelMBeanInfo passed in.
This method makes it possible to set a customized ModelMBeanInfo on
the ModelMBean as long as it is not registered with the MBeanServer.

Once the ModelMBean's ModelMBeanInfo (with Descriptors) are
customized and set on the ModelMBean, the ModelMBean be
registered with the MBeanServer.

If the ModelMBean is currently registered, this method throws
a

RuntimeOperationsException

wrapping an

IllegalStateException

If the given

inModelMBeanInfo

does not contain any

ModelMBeanNotificationInfo

for the

GENERIC

or

ATTRIBUTE_CHANGE

notifications, then the
RequiredModelMBean will supply its own default

ModelMBeanNotificationInfo

s for
those missing notifications.

**Specified by:** setModelMBeanInfo

in interface

ModelMBean
**Parameters:** mbi

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
public void setManagedResource​(
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

**Specified by:** setManagedResource

in interface

ModelMBean
**Parameters:** mr

- Object that is the managed resource
**Parameters:** mr_type

- The type of reference for the managed resource.

Can be: "ObjectReference", "Handle", "IOR", "EJBHandle",
or "RMIReference".

In this implementation only "ObjectReference" is supported.
**Throws:** MBeanException

- The initializer of the object has
thrown an exception.
**Throws:** InstanceNotFoundException

- The managed resource
object could not be found
**Throws:** InvalidTargetObjectTypeException

- The managed
resource type should be "ObjectReference".
**Throws:** RuntimeOperationsException

- Wraps a

RuntimeException

when setting the resource.

- load

```java
public void load()
throws
MBeanException
,

RuntimeOperationsException
,

InstanceNotFoundException
```

Instantiates this MBean instance with the data found for
the MBean in the persistent store. The data loaded could include
attribute and operation values.

This method should be called during construction or
initialization of this instance, and before the MBean is
registered with the MBeanServer.

If the implementation of this class does not support
persistence, an

MBeanException

wrapping a

ServiceNotFoundException

is thrown.

**Specified by:** load

in interface

PersistentMBean
**Throws:** MBeanException

- Wraps another exception, or
persistence is not supported
**Throws:** RuntimeOperationsException

- Wraps exceptions from the
persistence mechanism
**Throws:** InstanceNotFoundException

- Could not find or load
this MBean from persistent storage

- store

```java
public void store()
throws
MBeanException
,

RuntimeOperationsException
,

InstanceNotFoundException
```

Captures the current state of this MBean instance and writes
it out to the persistent store. The state stored could include
attribute and operation values.

If the implementation of this class does not support
persistence, an

MBeanException

wrapping a

ServiceNotFoundException

is thrown.

Persistence policy from the MBean and attribute descriptor
is used to guide execution of this method. The MBean should be
stored if 'persistPolicy' field is:

```java
!= "never"
= "always"
= "onTimer" and now > 'lastPersistTime' + 'persistPeriod'
= "NoMoreOftenThan" and now > 'lastPersistTime' + 'persistPeriod'
= "onUnregister"
```

Do not store the MBean if 'persistPolicy' field is:

```java
= "never"
= "onUpdate"
= "onTimer" && now < 'lastPersistTime' + 'persistPeriod'
```

**Specified by:** store

in interface

PersistentMBean
**Throws:** MBeanException

- Wraps another exception, or
persistence is not supported
**Throws:** RuntimeOperationsException

- Wraps exceptions from the
persistence mechanism
**Throws:** InstanceNotFoundException

- Could not find/access the
persistent store

- getMBeanInfo

```java
public
MBeanInfo
getMBeanInfo()
```

Returns the attributes, operations, constructors and notifications
that this RequiredModelMBean exposes for management.

**Specified by:** getMBeanInfo

in interface

DynamicMBean
**Returns:** An instance of ModelMBeanInfo allowing retrieval all
attributes, operations, and Notifications of this MBean.

- invoke

```java
public
Object
invoke​(
String
opName,

Object
[] opArgs,

String
[] sig)
throws
MBeanException
,

ReflectionException
```

Invokes a method on or through a RequiredModelMBean and returns
the result of the method execution.

If the given method to be invoked, together with the provided
signature, matches one of RequiredModelMbean
accessible methods, this one will be call. Otherwise the call to
the given method will be tried on the managed resource.

The last value returned by an operation may be cached in
the operation's descriptor which
is in the ModelMBeanOperationInfo's descriptor.
The valid value will be in the 'value' field if there is one.
If the 'currencyTimeLimit' field in the descriptor is:

- <0

Then the value is not cached and is never valid.
The operation method is invoked.
The 'value' and 'lastUpdatedTimeStamp' fields are cleared.
- =0

Then the value is always cached and always valid.
The 'value' field is returned. If there is no 'value' field
then the operation method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields are set to
the operation's return value and the current time stamp.
- >0

Represents the number of seconds that the 'value'
field is valid.
The 'value' field is no longer valid when
'lastUpdatedTimeStamp' + 'currencyTimeLimit' > Now.

- When 'value' is valid, 'value' is returned.
- When 'value' is no longer valid then the operation
method is invoked. The 'lastUpdatedTimeStamp' field
and `value' fields are updated.

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

**Specified by:** invoke

in interface

DynamicMBean
**Parameters:** opName

- The name of the method to be invoked. The
name can be the fully qualified method name including the
classname, or just the method name if the classname is
defined in the 'class' field of the operation descriptor.
**Parameters:** opArgs

- An array containing the parameters to be set
when the operation is invoked
**Parameters:** sig

- An array containing the signature of the
operation. The class objects will be loaded using the same
class loader as the one used for loading the MBean on which
the operation was invoked.
**Returns:** The object returned by the method, which represents the
result of invoking the method on the specified managed resource.
**Throws:** MBeanException

- Wraps one of the following Exceptions:

- An Exception thrown by the managed object's invoked method.
- ServiceNotFoundException

: No ModelMBeanOperationInfo or
no descriptor defined for the specified operation or the managed
resource is null.
- InvalidTargetObjectTypeException

: The 'targetType'
field value is not 'objectReference'.
**Throws:** ReflectionException

- Wraps an

Exception

thrown while trying to invoke the method.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

Method name is null.

- getAttribute

```java
public
Object
getAttribute​(
String
attrName)
throws
AttributeNotFoundException
,

MBeanException
,

ReflectionException
```

Returns the value of a specific attribute defined for this
ModelMBean.
The last value returned by an attribute may be cached in the
attribute's descriptor.
The valid value will be in the 'value' field if there is one.
If the 'currencyTimeLimit' field in the descriptor is:

- <0

Then the value is not cached and is never valid.
The getter method is invoked for the attribute.
The 'value' and 'lastUpdatedTimeStamp' fields are cleared.
- =0

Then the value is always cached and always valid.
The 'value' field is returned. If there is no'value' field
then the getter method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields are set
to the attribute's value and the current time stamp.
- >0

Represents the number of seconds that the 'value'
field is valid.
The 'value' field is no longer valid when
'lastUpdatedTimeStamp' + 'currencyTimeLimit' > Now.

- When 'value' is valid, 'value' is returned.
- When 'value' is no longer valid then the getter
method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields
are updated.

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

If the 'getMethod' field contains the name of a valid
operation descriptor, then the method described by the
operation descriptor is executed. The response from the
method is returned as the value of the attribute. If the
operation fails or the returned value is not compatible with
the declared type of the attribute, an exception will be thrown.

If no 'getMethod' field is defined then the default value of the
attribute is returned. If the returned value is not compatible with
the declared type of the attribute, an exception will be thrown.

The declared type of the attribute is the String returned by

MBeanAttributeInfo.getType()

. A value is compatible
with this type if one of the following is true:

- the value is null;
- the declared name is a primitive type name (such as "int")
and the value is an instance of the corresponding wrapper
type (such as java.lang.Integer);
- the name of the value's class is identical to the declared name;
- the declared name can be loaded by the value's class loader and
produces a class to which the value can be assigned.

In this implementation, in every case where the getMethod needs to
be called, because the method is invoked through the standard "invoke"
method and thus needs operationInfo, an operation must be specified
for that getMethod so that the invocation works correctly.

**Specified by:** getAttribute

in interface

DynamicMBean
**Parameters:** attrName

- A String specifying the name of the
attribute to be retrieved. It must match the name of a
ModelMBeanAttributeInfo.
**Returns:** The value of the retrieved attribute from the
descriptor 'value' field or from the invocation of the
operation in the 'getMethod' field of the descriptor.
**Throws:** AttributeNotFoundException

- The specified attribute is
not accessible in the MBean.
The following cases may result in an AttributeNotFoundException:

- No ModelMBeanInfo was found for the Model MBean.
- No ModelMBeanAttributeInfo was found for the specified
attribute name.
- The ModelMBeanAttributeInfo isReadable method returns
'false'.
**Throws:** MBeanException

- Wraps one of the following Exceptions:

- InvalidAttributeValueException

: A wrong value type
was received from the attribute's getter method or
no 'getMethod' field defined in the descriptor for
the attribute and no default value exists.
- ServiceNotFoundException

: No
ModelMBeanOperationInfo defined for the attribute's
getter method or no descriptor associated with the
ModelMBeanOperationInfo or the managed resource is
null.
- InvalidTargetObjectTypeException

The 'targetType'
field value is not 'objectReference'.
- An Exception thrown by the managed object's getter.
**Throws:** ReflectionException

- Wraps an

Exception

thrown while trying to invoke the getter.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

: The attribute name in
parameter is null.
**See Also:** setAttribute(javax.management.Attribute)

- getAttributes

```java
public
AttributeList
getAttributes​(
String
[] attrNames)
```

Returns the values of several attributes in the ModelMBean.
Executes a getAttribute for each attribute name in the
attrNames array passed in.

**Specified by:** getAttributes

in interface

DynamicMBean
**Parameters:** attrNames

- A String array of names of the attributes
to be retrieved.
**Returns:** The array of the retrieved attributes.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

: The object name in parameter is
null or attributes in parameter is null.
**See Also:** setAttributes(javax.management.AttributeList)

- setAttribute

```java
public void setAttribute​(
Attribute
attribute)
throws
AttributeNotFoundException
,

InvalidAttributeValueException
,

MBeanException
,

ReflectionException
```

Sets the value of a specific attribute of a named ModelMBean.

If the 'setMethod' field of the attribute's descriptor
contains the name of a valid operation descriptor, then the
method described by the operation descriptor is executed.
In this implementation, the operation descriptor must be specified
correctly and assigned to the modelMBeanInfo so that the 'setMethod'
works correctly.
The response from the method is set as the value of the attribute
in the descriptor.

If currencyTimeLimit is > 0, then the new value for the
attribute is cached in the attribute descriptor's
'value' field and the 'lastUpdatedTimeStamp' field is set to
the current time stamp.

If the persist field of the attribute's descriptor is not null
then Persistence policy from the attribute descriptor is used to
guide storing the attribute in a persistent store.

Store the MBean if 'persistPolicy' field is:

- != "never"
- = "always"
- = "onUpdate"
- = "onTimer" and now > 'lastPersistTime' + 'persistPeriod'
- = "NoMoreOftenThan" and now > 'lastPersistTime' +
'persistPeriod'

Do not store the MBean if 'persistPolicy' field is:

- = "never"
- = = "onTimer" && now < 'lastPersistTime' + 'persistPeriod'
- = "onUnregister"
- = = "NoMoreOftenThan" and now < 'lastPersistTime' +
'persistPeriod'

The ModelMBeanInfo of the Model MBean is stored in a file.

**Specified by:** setAttribute

in interface

DynamicMBean
**Parameters:** attribute

- The Attribute instance containing the name of
the attribute to be set and the value it is to be set to.
**Throws:** AttributeNotFoundException

- The specified attribute is
not accessible in the MBean.

The following cases may result in an AttributeNotFoundException:

- No ModelMBeanAttributeInfo is found for the specified
attribute.
- The ModelMBeanAttributeInfo's isWritable method returns
'false'.
**Throws:** InvalidAttributeValueException

- No descriptor is defined
for the specified attribute.
**Throws:** MBeanException

- Wraps one of the following Exceptions:

- An Exception thrown by the managed object's setter.
- A

ServiceNotFoundException

if a setMethod field is
defined in the descriptor for the attribute and the managed
resource is null; or if no setMethod field is defined and
caching is not enabled for the attribute.
Note that if there is no getMethod field either, then caching
is automatically enabled.
- InvalidTargetObjectTypeException

The 'targetType'
field value is not 'objectReference'.
- An Exception thrown by the managed object's getter.
**Throws:** ReflectionException

- Wraps an

Exception

thrown while trying to invoke the setter.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

: The attribute in parameter is
null.
**See Also:** getAttribute(java.lang.String)

- setAttributes

```java
public
AttributeList
setAttributes​(
AttributeList
attributes)
```

Sets the values of an array of attributes of this ModelMBean.
Executes the setAttribute() method for each attribute in the list.

**Specified by:** setAttributes

in interface

DynamicMBean
**Parameters:** attributes

- A list of attributes: The identification of the
attributes to be set and the values they are to be set to.
**Returns:** The array of attributes that were set, with their new
values in Attribute instances.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

: The object name in parameter
is null or attributes in parameter is null.
**See Also:** getAttributes(java.lang.String[])

- addNotificationListener

```java
public void addNotificationListener​(
NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
throws
IllegalArgumentException
```

Registers an object which implements the NotificationListener
interface as a listener. This
object's 'handleNotification()' method will be invoked when any
notification is issued through or by the ModelMBean. This does
not include attributeChangeNotifications. They must be registered
for independently.

**Specified by:** addNotificationListener

in interface

NotificationBroadcaster
**Parameters:** listener

- The listener object which will handles
notifications emitted by the registered MBean.
**Parameters:** filter

- The filter object. If null, no filtering will be
performed before handling notifications.
**Parameters:** handback

- The context to be sent to the listener with
the notification when a notification is emitted.
**Throws:** IllegalArgumentException

- The listener cannot be null.
**See Also:** removeNotificationListener(javax.management.NotificationListener)

- removeNotificationListener

```java
public void removeNotificationListener​(
NotificationListener
listener)
throws
ListenerNotFoundException
```

Removes a listener for Notifications from the RequiredModelMBean.

**Specified by:** removeNotificationListener

in interface

NotificationBroadcaster
**Parameters:** listener

- The listener name which was handling notifications
emitted by the registered MBean.
This method will remove all information related to this listener.
**Throws:** ListenerNotFoundException

- The listener is not registered
in the MBean or is null.
**See Also:** addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

- getNotificationInfo

```java
public
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns the array of Notifications always generated by the
RequiredModelMBean.

RequiredModelMBean may always send also two additional notifications:

- One with descriptor

"name=GENERIC,descriptorType=notification,log=T,severity=6,displayName=jmx.modelmbean.generic"
- Second is a standard attribute change notification
with descriptor

"name=ATTRIBUTE_CHANGE,descriptorType=notification,log=T,severity=6,displayName=jmx.attribute.change"

Thus these two notifications are always added to those specified
by the application.

**Specified by:** getNotificationInfo

in interface

NotificationBroadcaster
**Returns:** MBeanNotificationInfo[]

- getClassLoaderRepository

```java
protected
ClassLoaderRepository
getClassLoaderRepository()
```

Return the Class Loader Repository used to perform class loading.
Subclasses may wish to redefine this method in order to return
the appropriate

ClassLoaderRepository

that should be used in this object.

**Returns:** the Class Loader Repository.

- preRegister

```java
public
ObjectName
preRegister​(
MBeanServer
server,

ObjectName
name)
throws
Exception
```

Allows the MBean to perform any operations it needs before
being registered in the MBean server. If the name of the MBean
is not specified, the MBean can provide a name for its
registration. If any exception is raised, the MBean will not be
registered in the MBean server.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.preRegister(server, name)

in its own

preRegister

implementation.

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** server

- The MBean server in which the MBean will be registered.
**Parameters:** name

- The object name of the MBean. This name is null if
the name parameter to one of the

createMBean

or

registerMBean

methods in the

MBeanServer

interface is null. In that case, this method must return a
non-null ObjectName for the new MBean.
**Returns:** The name under which the MBean is to be registered.
This value must not be null. If the

name

parameter is not null, it will usually but not necessarily be
the returned value.
**Throws:** Exception

- This exception will be caught by
the MBean server and re-thrown as an

MBeanRegistrationException

.

- postRegister

```java
public void postRegister​(
Boolean
registrationDone)
```

Allows the MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.postRegister(registrationDone)

in its own

postRegister

implementation.

**Specified by:** postRegister

in interface

MBeanRegistration
**Parameters:** registrationDone

- Indicates whether or not the MBean has
been successfully registered in the MBean server. The value
false means that the registration phase has failed.

- preDeregister

```java
public void preDeregister()
throws
Exception
```

Allows the MBean to perform any operations it needs before
being unregistered by the MBean server.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.preDeregister()

in its own

preDeregister

implementation.

**Specified by:** preDeregister

in interface

MBeanRegistration
**Throws:** Exception

- This exception will be caught by
the MBean server and re-thrown as an

MBeanRegistrationException

.

- postDeregister

```java
public void postDeregister()
```

Allows the MBean to perform any operations needed after having been
unregistered in the MBean server.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.postDeregister()

in its own

postDeregister

implementation.

**Specified by:** postDeregister

in interface

MBeanRegistration

---

#### Method Detail

setModelMBeanInfo

```java
public void setModelMBeanInfo​(
ModelMBeanInfo
mbi)
throws
MBeanException
,

RuntimeOperationsException
```

Initializes a ModelMBean object using ModelMBeanInfo passed in.
This method makes it possible to set a customized ModelMBeanInfo on
the ModelMBean as long as it is not registered with the MBeanServer.

Once the ModelMBean's ModelMBeanInfo (with Descriptors) are
customized and set on the ModelMBean, the ModelMBean be
registered with the MBeanServer.

If the ModelMBean is currently registered, this method throws
a

RuntimeOperationsException

wrapping an

IllegalStateException

If the given

inModelMBeanInfo

does not contain any

ModelMBeanNotificationInfo

for the

GENERIC

or

ATTRIBUTE_CHANGE

notifications, then the
RequiredModelMBean will supply its own default

ModelMBeanNotificationInfo

s for
those missing notifications.

**Specified by:** setModelMBeanInfo

in interface

ModelMBean
**Parameters:** mbi

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

public void setModelMBeanInfo​(

ModelMBeanInfo

mbi)
throws

MBeanException

,

RuntimeOperationsException

Initializes a ModelMBean object using ModelMBeanInfo passed in.
This method makes it possible to set a customized ModelMBeanInfo on
the ModelMBean as long as it is not registered with the MBeanServer.

Once the ModelMBean's ModelMBeanInfo (with Descriptors) are
customized and set on the ModelMBean, the ModelMBean be
registered with the MBeanServer.

If the ModelMBean is currently registered, this method throws
a

RuntimeOperationsException

wrapping an

IllegalStateException

If the given

inModelMBeanInfo

does not contain any

ModelMBeanNotificationInfo

for the

GENERIC

or

ATTRIBUTE_CHANGE

notifications, then the
RequiredModelMBean will supply its own default

ModelMBeanNotificationInfo

s for
those missing notifications.

If the ModelMBean is currently registered, this method throws
a

RuntimeOperationsException

wrapping an

IllegalStateException

If the given

inModelMBeanInfo

does not contain any

ModelMBeanNotificationInfo

for the

GENERIC

or

ATTRIBUTE_CHANGE

notifications, then the
RequiredModelMBean will supply its own default

ModelMBeanNotificationInfo

s for
those missing notifications.

If the given

inModelMBeanInfo

does not contain any

ModelMBeanNotificationInfo

for the

GENERIC

or

ATTRIBUTE_CHANGE

notifications, then the
RequiredModelMBean will supply its own default

ModelMBeanNotificationInfo

s for
those missing notifications.

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
public void setManagedResource​(
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

**Specified by:** setManagedResource

in interface

ModelMBean
**Parameters:** mr

- Object that is the managed resource
**Parameters:** mr_type

- The type of reference for the managed resource.

Can be: "ObjectReference", "Handle", "IOR", "EJBHandle",
or "RMIReference".

In this implementation only "ObjectReference" is supported.
**Throws:** MBeanException

- The initializer of the object has
thrown an exception.
**Throws:** InstanceNotFoundException

- The managed resource
object could not be found
**Throws:** InvalidTargetObjectTypeException

- The managed
resource type should be "ObjectReference".
**Throws:** RuntimeOperationsException

- Wraps a

RuntimeException

when setting the resource.

---

#### setManagedResource

public void setManagedResource​(

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

load

```java
public void load()
throws
MBeanException
,

RuntimeOperationsException
,

InstanceNotFoundException
```

Instantiates this MBean instance with the data found for
the MBean in the persistent store. The data loaded could include
attribute and operation values.

This method should be called during construction or
initialization of this instance, and before the MBean is
registered with the MBeanServer.

If the implementation of this class does not support
persistence, an

MBeanException

wrapping a

ServiceNotFoundException

is thrown.

**Specified by:** load

in interface

PersistentMBean
**Throws:** MBeanException

- Wraps another exception, or
persistence is not supported
**Throws:** RuntimeOperationsException

- Wraps exceptions from the
persistence mechanism
**Throws:** InstanceNotFoundException

- Could not find or load
this MBean from persistent storage

---

#### load

public void load()
throws

MBeanException

,

RuntimeOperationsException

,

InstanceNotFoundException

Instantiates this MBean instance with the data found for
the MBean in the persistent store. The data loaded could include
attribute and operation values.

This method should be called during construction or
initialization of this instance, and before the MBean is
registered with the MBeanServer.

If the implementation of this class does not support
persistence, an

MBeanException

wrapping a

ServiceNotFoundException

is thrown.

Instantiates this MBean instance with the data found for
the MBean in the persistent store. The data loaded could include
attribute and operation values.

This method should be called during construction or
initialization of this instance, and before the MBean is
registered with the MBeanServer.

If the implementation of this class does not support
persistence, an

MBeanException

wrapping a

ServiceNotFoundException

is thrown.

store

```java
public void store()
throws
MBeanException
,

RuntimeOperationsException
,

InstanceNotFoundException
```

Captures the current state of this MBean instance and writes
it out to the persistent store. The state stored could include
attribute and operation values.

If the implementation of this class does not support
persistence, an

MBeanException

wrapping a

ServiceNotFoundException

is thrown.

Persistence policy from the MBean and attribute descriptor
is used to guide execution of this method. The MBean should be
stored if 'persistPolicy' field is:

```java
!= "never"
= "always"
= "onTimer" and now > 'lastPersistTime' + 'persistPeriod'
= "NoMoreOftenThan" and now > 'lastPersistTime' + 'persistPeriod'
= "onUnregister"
```

Do not store the MBean if 'persistPolicy' field is:

```java
= "never"
= "onUpdate"
= "onTimer" && now < 'lastPersistTime' + 'persistPeriod'
```

**Specified by:** store

in interface

PersistentMBean
**Throws:** MBeanException

- Wraps another exception, or
persistence is not supported
**Throws:** RuntimeOperationsException

- Wraps exceptions from the
persistence mechanism
**Throws:** InstanceNotFoundException

- Could not find/access the
persistent store

---

#### store

public void store()
throws

MBeanException

,

RuntimeOperationsException

,

InstanceNotFoundException

Captures the current state of this MBean instance and writes
it out to the persistent store. The state stored could include
attribute and operation values.

If the implementation of this class does not support
persistence, an

MBeanException

wrapping a

ServiceNotFoundException

is thrown.

Persistence policy from the MBean and attribute descriptor
is used to guide execution of this method. The MBean should be
stored if 'persistPolicy' field is:

```java
!= "never"
= "always"
= "onTimer" and now > 'lastPersistTime' + 'persistPeriod'
= "NoMoreOftenThan" and now > 'lastPersistTime' + 'persistPeriod'
= "onUnregister"
```

Do not store the MBean if 'persistPolicy' field is:

```java
= "never"
= "onUpdate"
= "onTimer" && now < 'lastPersistTime' + 'persistPeriod'
```

Captures the current state of this MBean instance and writes
it out to the persistent store. The state stored could include
attribute and operation values.

If the implementation of this class does not support
persistence, an

MBeanException

wrapping a

ServiceNotFoundException

is thrown.

Persistence policy from the MBean and attribute descriptor
is used to guide execution of this method. The MBean should be
stored if 'persistPolicy' field is:

!= "never"
= "always"
= "onTimer" and now > 'lastPersistTime' + 'persistPeriod'
= "NoMoreOftenThan" and now > 'lastPersistTime' + 'persistPeriod'
= "onUnregister"

Do not store the MBean if 'persistPolicy' field is:

= "never"
= "onUpdate"
= "onTimer" && now < 'lastPersistTime' + 'persistPeriod'

getMBeanInfo

```java
public
MBeanInfo
getMBeanInfo()
```

Returns the attributes, operations, constructors and notifications
that this RequiredModelMBean exposes for management.

**Specified by:** getMBeanInfo

in interface

DynamicMBean
**Returns:** An instance of ModelMBeanInfo allowing retrieval all
attributes, operations, and Notifications of this MBean.

---

#### getMBeanInfo

public

MBeanInfo

getMBeanInfo()

Returns the attributes, operations, constructors and notifications
that this RequiredModelMBean exposes for management.

invoke

```java
public
Object
invoke​(
String
opName,

Object
[] opArgs,

String
[] sig)
throws
MBeanException
,

ReflectionException
```

Invokes a method on or through a RequiredModelMBean and returns
the result of the method execution.

If the given method to be invoked, together with the provided
signature, matches one of RequiredModelMbean
accessible methods, this one will be call. Otherwise the call to
the given method will be tried on the managed resource.

The last value returned by an operation may be cached in
the operation's descriptor which
is in the ModelMBeanOperationInfo's descriptor.
The valid value will be in the 'value' field if there is one.
If the 'currencyTimeLimit' field in the descriptor is:

- <0

Then the value is not cached and is never valid.
The operation method is invoked.
The 'value' and 'lastUpdatedTimeStamp' fields are cleared.
- =0

Then the value is always cached and always valid.
The 'value' field is returned. If there is no 'value' field
then the operation method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields are set to
the operation's return value and the current time stamp.
- >0

Represents the number of seconds that the 'value'
field is valid.
The 'value' field is no longer valid when
'lastUpdatedTimeStamp' + 'currencyTimeLimit' > Now.

- When 'value' is valid, 'value' is returned.
- When 'value' is no longer valid then the operation
method is invoked. The 'lastUpdatedTimeStamp' field
and `value' fields are updated.

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

**Specified by:** invoke

in interface

DynamicMBean
**Parameters:** opName

- The name of the method to be invoked. The
name can be the fully qualified method name including the
classname, or just the method name if the classname is
defined in the 'class' field of the operation descriptor.
**Parameters:** opArgs

- An array containing the parameters to be set
when the operation is invoked
**Parameters:** sig

- An array containing the signature of the
operation. The class objects will be loaded using the same
class loader as the one used for loading the MBean on which
the operation was invoked.
**Returns:** The object returned by the method, which represents the
result of invoking the method on the specified managed resource.
**Throws:** MBeanException

- Wraps one of the following Exceptions:

- An Exception thrown by the managed object's invoked method.
- ServiceNotFoundException

: No ModelMBeanOperationInfo or
no descriptor defined for the specified operation or the managed
resource is null.
- InvalidTargetObjectTypeException

: The 'targetType'
field value is not 'objectReference'.
**Throws:** ReflectionException

- Wraps an

Exception

thrown while trying to invoke the method.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

Method name is null.

---

#### invoke

public

Object

invoke​(

String

opName,

Object

[] opArgs,

String

[] sig)
throws

MBeanException

,

ReflectionException

Invokes a method on or through a RequiredModelMBean and returns
the result of the method execution.

If the given method to be invoked, together with the provided
signature, matches one of RequiredModelMbean
accessible methods, this one will be call. Otherwise the call to
the given method will be tried on the managed resource.

The last value returned by an operation may be cached in
the operation's descriptor which
is in the ModelMBeanOperationInfo's descriptor.
The valid value will be in the 'value' field if there is one.
If the 'currencyTimeLimit' field in the descriptor is:

- <0

Then the value is not cached and is never valid.
The operation method is invoked.
The 'value' and 'lastUpdatedTimeStamp' fields are cleared.
- =0

Then the value is always cached and always valid.
The 'value' field is returned. If there is no 'value' field
then the operation method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields are set to
the operation's return value and the current time stamp.
- >0

Represents the number of seconds that the 'value'
field is valid.
The 'value' field is no longer valid when
'lastUpdatedTimeStamp' + 'currencyTimeLimit' > Now.

- When 'value' is valid, 'value' is returned.
- When 'value' is no longer valid then the operation
method is invoked. The 'lastUpdatedTimeStamp' field
and `value' fields are updated.

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

If the given method to be invoked, together with the provided
signature, matches one of RequiredModelMbean
accessible methods, this one will be call. Otherwise the call to
the given method will be tried on the managed resource.

The last value returned by an operation may be cached in
the operation's descriptor which
is in the ModelMBeanOperationInfo's descriptor.
The valid value will be in the 'value' field if there is one.
If the 'currencyTimeLimit' field in the descriptor is:

- <0

Then the value is not cached and is never valid.
The operation method is invoked.
The 'value' and 'lastUpdatedTimeStamp' fields are cleared.
- =0

Then the value is always cached and always valid.
The 'value' field is returned. If there is no 'value' field
then the operation method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields are set to
the operation's return value and the current time stamp.
- >0

Represents the number of seconds that the 'value'
field is valid.
The 'value' field is no longer valid when
'lastUpdatedTimeStamp' + 'currencyTimeLimit' > Now.

- When 'value' is valid, 'value' is returned.
- When 'value' is no longer valid then the operation
method is invoked. The 'lastUpdatedTimeStamp' field
and `value' fields are updated.

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

The last value returned by an operation may be cached in
the operation's descriptor which
is in the ModelMBeanOperationInfo's descriptor.
The valid value will be in the 'value' field if there is one.
If the 'currencyTimeLimit' field in the descriptor is:

- <0

Then the value is not cached and is never valid.
The operation method is invoked.
The 'value' and 'lastUpdatedTimeStamp' fields are cleared.
- =0

Then the value is always cached and always valid.
The 'value' field is returned. If there is no 'value' field
then the operation method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields are set to
the operation's return value and the current time stamp.
- >0

Represents the number of seconds that the 'value'
field is valid.
The 'value' field is no longer valid when
'lastUpdatedTimeStamp' + 'currencyTimeLimit' > Now.

- When 'value' is valid, 'value' is returned.
- When 'value' is no longer valid then the operation
method is invoked. The 'lastUpdatedTimeStamp' field
and `value' fields are updated.

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

<0

Then the value is not cached and is never valid.
The operation method is invoked.
The 'value' and 'lastUpdatedTimeStamp' fields are cleared.

=0

Then the value is always cached and always valid.
The 'value' field is returned. If there is no 'value' field
then the operation method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields are set to
the operation's return value and the current time stamp.

>0

Represents the number of seconds that the 'value'
field is valid.
The 'value' field is no longer valid when
'lastUpdatedTimeStamp' + 'currencyTimeLimit' > Now.

- When 'value' is valid, 'value' is returned.
- When 'value' is no longer valid then the operation
method is invoked. The 'lastUpdatedTimeStamp' field
and `value' fields are updated.

When 'value' is valid, 'value' is returned.

When 'value' is no longer valid then the operation
method is invoked. The 'lastUpdatedTimeStamp' field
and `value' fields are updated.

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

An Exception thrown by the managed object's invoked method.

ServiceNotFoundException

: No ModelMBeanOperationInfo or
no descriptor defined for the specified operation or the managed
resource is null.

InvalidTargetObjectTypeException

: The 'targetType'
field value is not 'objectReference'.

getAttribute

```java
public
Object
getAttribute​(
String
attrName)
throws
AttributeNotFoundException
,

MBeanException
,

ReflectionException
```

Returns the value of a specific attribute defined for this
ModelMBean.
The last value returned by an attribute may be cached in the
attribute's descriptor.
The valid value will be in the 'value' field if there is one.
If the 'currencyTimeLimit' field in the descriptor is:

- <0

Then the value is not cached and is never valid.
The getter method is invoked for the attribute.
The 'value' and 'lastUpdatedTimeStamp' fields are cleared.
- =0

Then the value is always cached and always valid.
The 'value' field is returned. If there is no'value' field
then the getter method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields are set
to the attribute's value and the current time stamp.
- >0

Represents the number of seconds that the 'value'
field is valid.
The 'value' field is no longer valid when
'lastUpdatedTimeStamp' + 'currencyTimeLimit' > Now.

- When 'value' is valid, 'value' is returned.
- When 'value' is no longer valid then the getter
method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields
are updated.

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

If the 'getMethod' field contains the name of a valid
operation descriptor, then the method described by the
operation descriptor is executed. The response from the
method is returned as the value of the attribute. If the
operation fails or the returned value is not compatible with
the declared type of the attribute, an exception will be thrown.

If no 'getMethod' field is defined then the default value of the
attribute is returned. If the returned value is not compatible with
the declared type of the attribute, an exception will be thrown.

The declared type of the attribute is the String returned by

MBeanAttributeInfo.getType()

. A value is compatible
with this type if one of the following is true:

- the value is null;
- the declared name is a primitive type name (such as "int")
and the value is an instance of the corresponding wrapper
type (such as java.lang.Integer);
- the name of the value's class is identical to the declared name;
- the declared name can be loaded by the value's class loader and
produces a class to which the value can be assigned.

In this implementation, in every case where the getMethod needs to
be called, because the method is invoked through the standard "invoke"
method and thus needs operationInfo, an operation must be specified
for that getMethod so that the invocation works correctly.

**Specified by:** getAttribute

in interface

DynamicMBean
**Parameters:** attrName

- A String specifying the name of the
attribute to be retrieved. It must match the name of a
ModelMBeanAttributeInfo.
**Returns:** The value of the retrieved attribute from the
descriptor 'value' field or from the invocation of the
operation in the 'getMethod' field of the descriptor.
**Throws:** AttributeNotFoundException

- The specified attribute is
not accessible in the MBean.
The following cases may result in an AttributeNotFoundException:

- No ModelMBeanInfo was found for the Model MBean.
- No ModelMBeanAttributeInfo was found for the specified
attribute name.
- The ModelMBeanAttributeInfo isReadable method returns
'false'.
**Throws:** MBeanException

- Wraps one of the following Exceptions:

- InvalidAttributeValueException

: A wrong value type
was received from the attribute's getter method or
no 'getMethod' field defined in the descriptor for
the attribute and no default value exists.
- ServiceNotFoundException

: No
ModelMBeanOperationInfo defined for the attribute's
getter method or no descriptor associated with the
ModelMBeanOperationInfo or the managed resource is
null.
- InvalidTargetObjectTypeException

The 'targetType'
field value is not 'objectReference'.
- An Exception thrown by the managed object's getter.
**Throws:** ReflectionException

- Wraps an

Exception

thrown while trying to invoke the getter.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

: The attribute name in
parameter is null.
**See Also:** setAttribute(javax.management.Attribute)

---

#### getAttribute

public

Object

getAttribute​(

String

attrName)
throws

AttributeNotFoundException

,

MBeanException

,

ReflectionException

Returns the value of a specific attribute defined for this
ModelMBean.
The last value returned by an attribute may be cached in the
attribute's descriptor.
The valid value will be in the 'value' field if there is one.
If the 'currencyTimeLimit' field in the descriptor is:

- <0

Then the value is not cached and is never valid.
The getter method is invoked for the attribute.
The 'value' and 'lastUpdatedTimeStamp' fields are cleared.
- =0

Then the value is always cached and always valid.
The 'value' field is returned. If there is no'value' field
then the getter method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields are set
to the attribute's value and the current time stamp.
- >0

Represents the number of seconds that the 'value'
field is valid.
The 'value' field is no longer valid when
'lastUpdatedTimeStamp' + 'currencyTimeLimit' > Now.

- When 'value' is valid, 'value' is returned.
- When 'value' is no longer valid then the getter
method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields
are updated.

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

If the 'getMethod' field contains the name of a valid
operation descriptor, then the method described by the
operation descriptor is executed. The response from the
method is returned as the value of the attribute. If the
operation fails or the returned value is not compatible with
the declared type of the attribute, an exception will be thrown.

If no 'getMethod' field is defined then the default value of the
attribute is returned. If the returned value is not compatible with
the declared type of the attribute, an exception will be thrown.

The declared type of the attribute is the String returned by

MBeanAttributeInfo.getType()

. A value is compatible
with this type if one of the following is true:

- the value is null;
- the declared name is a primitive type name (such as "int")
and the value is an instance of the corresponding wrapper
type (such as java.lang.Integer);
- the name of the value's class is identical to the declared name;
- the declared name can be loaded by the value's class loader and
produces a class to which the value can be assigned.

In this implementation, in every case where the getMethod needs to
be called, because the method is invoked through the standard "invoke"
method and thus needs operationInfo, an operation must be specified
for that getMethod so that the invocation works correctly.

<0

Then the value is not cached and is never valid.
The getter method is invoked for the attribute.
The 'value' and 'lastUpdatedTimeStamp' fields are cleared.

=0

Then the value is always cached and always valid.
The 'value' field is returned. If there is no'value' field
then the getter method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields are set
to the attribute's value and the current time stamp.

>0

Represents the number of seconds that the 'value'
field is valid.
The 'value' field is no longer valid when
'lastUpdatedTimeStamp' + 'currencyTimeLimit' > Now.

- When 'value' is valid, 'value' is returned.
- When 'value' is no longer valid then the getter
method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields
are updated.

When 'value' is valid, 'value' is returned.

When 'value' is no longer valid then the getter
method is invoked for the attribute.
The 'lastUpdatedTimeStamp' field and `value' fields
are updated.

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

If the 'getMethod' field contains the name of a valid
operation descriptor, then the method described by the
operation descriptor is executed. The response from the
method is returned as the value of the attribute. If the
operation fails or the returned value is not compatible with
the declared type of the attribute, an exception will be thrown.

If no 'getMethod' field is defined then the default value of the
attribute is returned. If the returned value is not compatible with
the declared type of the attribute, an exception will be thrown.

The declared type of the attribute is the String returned by

MBeanAttributeInfo.getType()

. A value is compatible
with this type if one of the following is true:

- the value is null;
- the declared name is a primitive type name (such as "int")
and the value is an instance of the corresponding wrapper
type (such as java.lang.Integer);
- the name of the value's class is identical to the declared name;
- the declared name can be loaded by the value's class loader and
produces a class to which the value can be assigned.

In this implementation, in every case where the getMethod needs to
be called, because the method is invoked through the standard "invoke"
method and thus needs operationInfo, an operation must be specified
for that getMethod so that the invocation works correctly.

the value is null;

the declared name is a primitive type name (such as "int")
and the value is an instance of the corresponding wrapper
type (such as java.lang.Integer);

the name of the value's class is identical to the declared name;

the declared name can be loaded by the value's class loader and
produces a class to which the value can be assigned.

In this implementation, in every case where the getMethod needs to
be called, because the method is invoked through the standard "invoke"
method and thus needs operationInfo, an operation must be specified
for that getMethod so that the invocation works correctly.

No ModelMBeanInfo was found for the Model MBean.

No ModelMBeanAttributeInfo was found for the specified
attribute name.

The ModelMBeanAttributeInfo isReadable method returns
'false'.

InvalidAttributeValueException

: A wrong value type
was received from the attribute's getter method or
no 'getMethod' field defined in the descriptor for
the attribute and no default value exists.

ServiceNotFoundException

: No
ModelMBeanOperationInfo defined for the attribute's
getter method or no descriptor associated with the
ModelMBeanOperationInfo or the managed resource is
null.

InvalidTargetObjectTypeException

The 'targetType'
field value is not 'objectReference'.

An Exception thrown by the managed object's getter.

getAttributes

```java
public
AttributeList
getAttributes​(
String
[] attrNames)
```

Returns the values of several attributes in the ModelMBean.
Executes a getAttribute for each attribute name in the
attrNames array passed in.

**Specified by:** getAttributes

in interface

DynamicMBean
**Parameters:** attrNames

- A String array of names of the attributes
to be retrieved.
**Returns:** The array of the retrieved attributes.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

: The object name in parameter is
null or attributes in parameter is null.
**See Also:** setAttributes(javax.management.AttributeList)

---

#### getAttributes

public

AttributeList

getAttributes​(

String

[] attrNames)

Returns the values of several attributes in the ModelMBean.
Executes a getAttribute for each attribute name in the
attrNames array passed in.

setAttribute

```java
public void setAttribute​(
Attribute
attribute)
throws
AttributeNotFoundException
,

InvalidAttributeValueException
,

MBeanException
,

ReflectionException
```

Sets the value of a specific attribute of a named ModelMBean.

If the 'setMethod' field of the attribute's descriptor
contains the name of a valid operation descriptor, then the
method described by the operation descriptor is executed.
In this implementation, the operation descriptor must be specified
correctly and assigned to the modelMBeanInfo so that the 'setMethod'
works correctly.
The response from the method is set as the value of the attribute
in the descriptor.

If currencyTimeLimit is > 0, then the new value for the
attribute is cached in the attribute descriptor's
'value' field and the 'lastUpdatedTimeStamp' field is set to
the current time stamp.

If the persist field of the attribute's descriptor is not null
then Persistence policy from the attribute descriptor is used to
guide storing the attribute in a persistent store.

Store the MBean if 'persistPolicy' field is:

- != "never"
- = "always"
- = "onUpdate"
- = "onTimer" and now > 'lastPersistTime' + 'persistPeriod'
- = "NoMoreOftenThan" and now > 'lastPersistTime' +
'persistPeriod'

Do not store the MBean if 'persistPolicy' field is:

- = "never"
- = = "onTimer" && now < 'lastPersistTime' + 'persistPeriod'
- = "onUnregister"
- = = "NoMoreOftenThan" and now < 'lastPersistTime' +
'persistPeriod'

The ModelMBeanInfo of the Model MBean is stored in a file.

**Specified by:** setAttribute

in interface

DynamicMBean
**Parameters:** attribute

- The Attribute instance containing the name of
the attribute to be set and the value it is to be set to.
**Throws:** AttributeNotFoundException

- The specified attribute is
not accessible in the MBean.

The following cases may result in an AttributeNotFoundException:

- No ModelMBeanAttributeInfo is found for the specified
attribute.
- The ModelMBeanAttributeInfo's isWritable method returns
'false'.
**Throws:** InvalidAttributeValueException

- No descriptor is defined
for the specified attribute.
**Throws:** MBeanException

- Wraps one of the following Exceptions:

- An Exception thrown by the managed object's setter.
- A

ServiceNotFoundException

if a setMethod field is
defined in the descriptor for the attribute and the managed
resource is null; or if no setMethod field is defined and
caching is not enabled for the attribute.
Note that if there is no getMethod field either, then caching
is automatically enabled.
- InvalidTargetObjectTypeException

The 'targetType'
field value is not 'objectReference'.
- An Exception thrown by the managed object's getter.
**Throws:** ReflectionException

- Wraps an

Exception

thrown while trying to invoke the setter.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

: The attribute in parameter is
null.
**See Also:** getAttribute(java.lang.String)

---

#### setAttribute

public void setAttribute​(

Attribute

attribute)
throws

AttributeNotFoundException

,

InvalidAttributeValueException

,

MBeanException

,

ReflectionException

Sets the value of a specific attribute of a named ModelMBean.

If the 'setMethod' field of the attribute's descriptor
contains the name of a valid operation descriptor, then the
method described by the operation descriptor is executed.
In this implementation, the operation descriptor must be specified
correctly and assigned to the modelMBeanInfo so that the 'setMethod'
works correctly.
The response from the method is set as the value of the attribute
in the descriptor.

If currencyTimeLimit is > 0, then the new value for the
attribute is cached in the attribute descriptor's
'value' field and the 'lastUpdatedTimeStamp' field is set to
the current time stamp.

If the persist field of the attribute's descriptor is not null
then Persistence policy from the attribute descriptor is used to
guide storing the attribute in a persistent store.

Store the MBean if 'persistPolicy' field is:

- != "never"
- = "always"
- = "onUpdate"
- = "onTimer" and now > 'lastPersistTime' + 'persistPeriod'
- = "NoMoreOftenThan" and now > 'lastPersistTime' +
'persistPeriod'

Do not store the MBean if 'persistPolicy' field is:

- = "never"
- = = "onTimer" && now < 'lastPersistTime' + 'persistPeriod'
- = "onUnregister"
- = = "NoMoreOftenThan" and now < 'lastPersistTime' +
'persistPeriod'

The ModelMBeanInfo of the Model MBean is stored in a file.

If currencyTimeLimit is > 0, then the new value for the
attribute is cached in the attribute descriptor's
'value' field and the 'lastUpdatedTimeStamp' field is set to
the current time stamp.

If the persist field of the attribute's descriptor is not null
then Persistence policy from the attribute descriptor is used to
guide storing the attribute in a persistent store.

Store the MBean if 'persistPolicy' field is:

- != "never"
- = "always"
- = "onUpdate"
- = "onTimer" and now > 'lastPersistTime' + 'persistPeriod'
- = "NoMoreOftenThan" and now > 'lastPersistTime' +
'persistPeriod'

Do not store the MBean if 'persistPolicy' field is:

- = "never"
- = = "onTimer" && now < 'lastPersistTime' + 'persistPeriod'
- = "onUnregister"
- = = "NoMoreOftenThan" and now < 'lastPersistTime' +
'persistPeriod'

The ModelMBeanInfo of the Model MBean is stored in a file.

If the persist field of the attribute's descriptor is not null
then Persistence policy from the attribute descriptor is used to
guide storing the attribute in a persistent store.

Store the MBean if 'persistPolicy' field is:

- != "never"
- = "always"
- = "onUpdate"
- = "onTimer" and now > 'lastPersistTime' + 'persistPeriod'
- = "NoMoreOftenThan" and now > 'lastPersistTime' +
'persistPeriod'

Do not store the MBean if 'persistPolicy' field is:

- = "never"
- = = "onTimer" && now < 'lastPersistTime' + 'persistPeriod'
- = "onUnregister"
- = = "NoMoreOftenThan" and now < 'lastPersistTime' +
'persistPeriod'

The ModelMBeanInfo of the Model MBean is stored in a file.

!= "never"

= "always"

= "onUpdate"

= "onTimer" and now > 'lastPersistTime' + 'persistPeriod'

= "NoMoreOftenThan" and now > 'lastPersistTime' +
'persistPeriod'

= "never"

= = "onTimer" && now < 'lastPersistTime' + 'persistPeriod'

= "onUnregister"

= = "NoMoreOftenThan" and now < 'lastPersistTime' +
'persistPeriod'

The ModelMBeanInfo of the Model MBean is stored in a file.

No ModelMBeanAttributeInfo is found for the specified
attribute.

The ModelMBeanAttributeInfo's isWritable method returns
'false'.

An Exception thrown by the managed object's setter.

A

ServiceNotFoundException

if a setMethod field is
defined in the descriptor for the attribute and the managed
resource is null; or if no setMethod field is defined and
caching is not enabled for the attribute.
Note that if there is no getMethod field either, then caching
is automatically enabled.

InvalidTargetObjectTypeException

The 'targetType'
field value is not 'objectReference'.

An Exception thrown by the managed object's getter.

setAttributes

```java
public
AttributeList
setAttributes​(
AttributeList
attributes)
```

Sets the values of an array of attributes of this ModelMBean.
Executes the setAttribute() method for each attribute in the list.

**Specified by:** setAttributes

in interface

DynamicMBean
**Parameters:** attributes

- A list of attributes: The identification of the
attributes to be set and the values they are to be set to.
**Returns:** The array of attributes that were set, with their new
values in Attribute instances.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

: The object name in parameter
is null or attributes in parameter is null.
**See Also:** getAttributes(java.lang.String[])

---

#### setAttributes

public

AttributeList

setAttributes​(

AttributeList

attributes)

Sets the values of an array of attributes of this ModelMBean.
Executes the setAttribute() method for each attribute in the list.

addNotificationListener

```java
public void addNotificationListener​(
NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
throws
IllegalArgumentException
```

Registers an object which implements the NotificationListener
interface as a listener. This
object's 'handleNotification()' method will be invoked when any
notification is issued through or by the ModelMBean. This does
not include attributeChangeNotifications. They must be registered
for independently.

**Specified by:** addNotificationListener

in interface

NotificationBroadcaster
**Parameters:** listener

- The listener object which will handles
notifications emitted by the registered MBean.
**Parameters:** filter

- The filter object. If null, no filtering will be
performed before handling notifications.
**Parameters:** handback

- The context to be sent to the listener with
the notification when a notification is emitted.
**Throws:** IllegalArgumentException

- The listener cannot be null.
**See Also:** removeNotificationListener(javax.management.NotificationListener)

---

#### addNotificationListener

public void addNotificationListener​(

NotificationListener

listener,

NotificationFilter

filter,

Object

handback)
throws

IllegalArgumentException

Registers an object which implements the NotificationListener
interface as a listener. This
object's 'handleNotification()' method will be invoked when any
notification is issued through or by the ModelMBean. This does
not include attributeChangeNotifications. They must be registered
for independently.

removeNotificationListener

```java
public void removeNotificationListener​(
NotificationListener
listener)
throws
ListenerNotFoundException
```

Removes a listener for Notifications from the RequiredModelMBean.

**Specified by:** removeNotificationListener

in interface

NotificationBroadcaster
**Parameters:** listener

- The listener name which was handling notifications
emitted by the registered MBean.
This method will remove all information related to this listener.
**Throws:** ListenerNotFoundException

- The listener is not registered
in the MBean or is null.
**See Also:** addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

---

#### removeNotificationListener

public void removeNotificationListener​(

NotificationListener

listener)
throws

ListenerNotFoundException

Removes a listener for Notifications from the RequiredModelMBean.

getNotificationInfo

```java
public
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns the array of Notifications always generated by the
RequiredModelMBean.

RequiredModelMBean may always send also two additional notifications:

- One with descriptor

"name=GENERIC,descriptorType=notification,log=T,severity=6,displayName=jmx.modelmbean.generic"
- Second is a standard attribute change notification
with descriptor

"name=ATTRIBUTE_CHANGE,descriptorType=notification,log=T,severity=6,displayName=jmx.attribute.change"

Thus these two notifications are always added to those specified
by the application.

**Specified by:** getNotificationInfo

in interface

NotificationBroadcaster
**Returns:** MBeanNotificationInfo[]

---

#### getNotificationInfo

public

MBeanNotificationInfo

[] getNotificationInfo()

Returns the array of Notifications always generated by the
RequiredModelMBean.

RequiredModelMBean may always send also two additional notifications:

- One with descriptor

"name=GENERIC,descriptorType=notification,log=T,severity=6,displayName=jmx.modelmbean.generic"
- Second is a standard attribute change notification
with descriptor

"name=ATTRIBUTE_CHANGE,descriptorType=notification,log=T,severity=6,displayName=jmx.attribute.change"

Thus these two notifications are always added to those specified
by the application.

RequiredModelMBean may always send also two additional notifications:

- One with descriptor

"name=GENERIC,descriptorType=notification,log=T,severity=6,displayName=jmx.modelmbean.generic"
- Second is a standard attribute change notification
with descriptor

"name=ATTRIBUTE_CHANGE,descriptorType=notification,log=T,severity=6,displayName=jmx.attribute.change"

Thus these two notifications are always added to those specified
by the application.

One with descriptor

"name=GENERIC,descriptorType=notification,log=T,severity=6,displayName=jmx.modelmbean.generic"

Second is a standard attribute change notification
with descriptor

"name=ATTRIBUTE_CHANGE,descriptorType=notification,log=T,severity=6,displayName=jmx.attribute.change"

getClassLoaderRepository

```java
protected
ClassLoaderRepository
getClassLoaderRepository()
```

Return the Class Loader Repository used to perform class loading.
Subclasses may wish to redefine this method in order to return
the appropriate

ClassLoaderRepository

that should be used in this object.

**Returns:** the Class Loader Repository.

---

#### getClassLoaderRepository

protected

ClassLoaderRepository

getClassLoaderRepository()

Return the Class Loader Repository used to perform class loading.
Subclasses may wish to redefine this method in order to return
the appropriate

ClassLoaderRepository

that should be used in this object.

preRegister

```java
public
ObjectName
preRegister​(
MBeanServer
server,

ObjectName
name)
throws
Exception
```

Allows the MBean to perform any operations it needs before
being registered in the MBean server. If the name of the MBean
is not specified, the MBean can provide a name for its
registration. If any exception is raised, the MBean will not be
registered in the MBean server.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.preRegister(server, name)

in its own

preRegister

implementation.

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** server

- The MBean server in which the MBean will be registered.
**Parameters:** name

- The object name of the MBean. This name is null if
the name parameter to one of the

createMBean

or

registerMBean

methods in the

MBeanServer

interface is null. In that case, this method must return a
non-null ObjectName for the new MBean.
**Returns:** The name under which the MBean is to be registered.
This value must not be null. If the

name

parameter is not null, it will usually but not necessarily be
the returned value.
**Throws:** Exception

- This exception will be caught by
the MBean server and re-thrown as an

MBeanRegistrationException

.

---

#### preRegister

public

ObjectName

preRegister​(

MBeanServer

server,

ObjectName

name)
throws

Exception

Allows the MBean to perform any operations it needs before
being registered in the MBean server. If the name of the MBean
is not specified, the MBean can provide a name for its
registration. If any exception is raised, the MBean will not be
registered in the MBean server.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.preRegister(server, name)

in its own

preRegister

implementation.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.preRegister(server, name)

in its own

preRegister

implementation.

postRegister

```java
public void postRegister​(
Boolean
registrationDone)
```

Allows the MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.postRegister(registrationDone)

in its own

postRegister

implementation.

**Specified by:** postRegister

in interface

MBeanRegistration
**Parameters:** registrationDone

- Indicates whether or not the MBean has
been successfully registered in the MBean server. The value
false means that the registration phase has failed.

---

#### postRegister

public void postRegister​(

Boolean

registrationDone)

Allows the MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.postRegister(registrationDone)

in its own

postRegister

implementation.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.postRegister(registrationDone)

in its own

postRegister

implementation.

preDeregister

```java
public void preDeregister()
throws
Exception
```

Allows the MBean to perform any operations it needs before
being unregistered by the MBean server.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.preDeregister()

in its own

preDeregister

implementation.

**Specified by:** preDeregister

in interface

MBeanRegistration
**Throws:** Exception

- This exception will be caught by
the MBean server and re-thrown as an

MBeanRegistrationException

.

---

#### preDeregister

public void preDeregister()
throws

Exception

Allows the MBean to perform any operations it needs before
being unregistered by the MBean server.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.preDeregister()

in its own

preDeregister

implementation.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.preDeregister()

in its own

preDeregister

implementation.

postDeregister

```java
public void postDeregister()
```

Allows the MBean to perform any operations needed after having been
unregistered in the MBean server.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.postDeregister()

in its own

postDeregister

implementation.

**Specified by:** postDeregister

in interface

MBeanRegistration

---

#### postDeregister

public void postDeregister()

Allows the MBean to perform any operations needed after having been
unregistered in the MBean server.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.postDeregister()

in its own

postDeregister

implementation.

In order to ensure proper run-time semantics of RequireModelMBean,
Any subclass of RequiredModelMBean overloading or overriding this
method should call

super.postDeregister()

in its own

postDeregister

implementation.

---

