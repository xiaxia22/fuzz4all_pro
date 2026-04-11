# Interface RMIConnection

**Source:** `java.management.rmi\javax\management\remote\rmi\RMIConnection.html`

### Class Description

```java
public interface
RMIConnection

extends
Closeable
,
Remote
```

RMI object used to forward an MBeanServer request from a client
to its MBeanServer implementation on the server side. There is one
Remote object implementing this interface for each remote client
connected to an RMI connector.

User code does not usually refer to this interface. It is
specified as part of the public API so that different
implementations of that API will interoperate.

To ensure that client parameters will be deserialized at the
server side with the correct classloader, client parameters such as
parameters used to invoke a method are wrapped in a

MarshalledObject

. An implementation of this interface must first
get the appropriate class loader for the operation and its target,
then deserialize the marshalled parameters with this classloader.
Except as noted, a parameter that is a

MarshalledObject

or

MarshalledObject[]

must not be null; the behavior is unspecified if it is.

Class loading aspects are detailed in the

JMX Specification, version 1.4

Most methods in this interface parallel methods in the

MBeanServerConnection

interface. Where an aspect of the behavior
of a method is not specified here, it is the same as in the
corresponding

MBeanServerConnection

method.

**All Superinterfaces:** AutoCloseable

,

Closeable

,

Remote

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getConnectionId()
throws
IOException

Returns the connection ID. This string is different for
every open connection to a given RMI connector server.

**Returns:**
- the connection ID

**Throws:**
- IOException

- if a general communication exception occurred.

**See Also:**
- RMIConnector.connect

---

#### void close()
throws
IOException

Closes this connection. On return from this method, the RMI
object implementing this interface is unexported, so further
remote calls to it will fail.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable

**Throws:**
- IOException

- if the connection could not be closed,
or the Remote object could not be unexported, or there was a
communication failure when transmitting the remote close
request.

---

#### ObjectInstance
createMBean​(
String
className,

ObjectName
name,

Subject
delegationSubject)
throws
ReflectionException
,

InstanceAlreadyExistsException
,

MBeanRegistrationException
,

MBeanException
,

NotCompliantMBeanException
,

IOException

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName)

.

**Parameters:**
- className

- The class name of the MBean to be instantiated.
- name

- The object name of the MBean. May be null.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Returns:**
- An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
instantiated MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.

**Throws:**
- ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or a

java.lang.Exception

that occurred
when trying to invoke the MBean's constructor.
- InstanceAlreadyExistsException

- The MBean is already
under the control of the MBean server.
- MBeanRegistrationException

- The

preRegister

(

MBeanRegistration

interface) method of the MBean has thrown an exception. The
MBean will not be registered.
- MBeanException

- The constructor of the MBean has
thrown an exception.
- NotCompliantMBeanException

- This class is not a JMX
compliant MBean.
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null, the

ObjectName

passed
in parameter contains a pattern or no

ObjectName

is specified for the MBean.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.

---

#### ObjectInstance
createMBean​(
String
className,

ObjectName
name,

ObjectName
loaderName,

Subject
delegationSubject)
throws
ReflectionException
,

InstanceAlreadyExistsException
,

MBeanRegistrationException
,

MBeanException
,

NotCompliantMBeanException
,

InstanceNotFoundException
,

IOException

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, ObjectName)

.

**Parameters:**
- className

- The class name of the MBean to be instantiated.
- name

- The object name of the MBean. May be null.
- loaderName

- The object name of the class loader to be used.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Returns:**
- An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
instantiated MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.

**Throws:**
- ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or a

java.lang.Exception

that occurred when trying to
invoke the MBean's constructor.
- InstanceAlreadyExistsException

- The MBean is already
under the control of the MBean server.
- MBeanRegistrationException

- The

preRegister

(

MBeanRegistration

interface) method of the MBean has thrown an exception. The
MBean will not be registered.
- MBeanException

- The constructor of the MBean has
thrown an exception.
- NotCompliantMBeanException

- This class is not a JMX
compliant MBean.
- InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null, the

ObjectName

passed
in parameter contains a pattern or no

ObjectName

is specified for the MBean.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.

---

#### ObjectInstance
createMBean​(
String
className,

ObjectName
name,

MarshalledObject
params,

String
[] signature,

Subject
delegationSubject)
throws
ReflectionException
,

InstanceAlreadyExistsException
,

MBeanRegistrationException
,

MBeanException
,

NotCompliantMBeanException
,

IOException

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, Object[], String[])

. The

Object[]

parameter is wrapped in a

MarshalledObject

.

**Parameters:**
- className

- The class name of the MBean to be instantiated.
- name

- The object name of the MBean. May be null.
- params

- An array containing the parameters of the
constructor to be invoked, encapsulated into a

MarshalledObject

. The encapsulated array can be
null, equivalent to an empty array.
- signature

- An array containing the signature of the
constructor to be invoked. Can be null, equivalent to an empty
array.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Returns:**
- An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
instantiated MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.

**Throws:**
- ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or a

java.lang.Exception

that occurred when trying to
invoke the MBean's constructor.
- InstanceAlreadyExistsException

- The MBean is already
under the control of the MBean server.
- MBeanRegistrationException

- The

preRegister

(

MBeanRegistration

interface) method of the MBean has thrown an exception. The
MBean will not be registered.
- MBeanException

- The constructor of the MBean has
thrown an exception.
- NotCompliantMBeanException

- This class is not a JMX
compliant MBean.
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null, the

ObjectName

passed
in parameter contains a pattern, or no

ObjectName

is specified for the MBean.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.

---

#### ObjectInstance
createMBean​(
String
className,

ObjectName
name,

ObjectName
loaderName,

MarshalledObject
params,

String
[] signature,

Subject
delegationSubject)
throws
ReflectionException
,

InstanceAlreadyExistsException
,

MBeanRegistrationException
,

MBeanException
,

NotCompliantMBeanException
,

InstanceNotFoundException
,

IOException

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, ObjectName, Object[], String[])

. The

Object[]

parameter is wrapped in a

MarshalledObject

.

**Parameters:**
- className

- The class name of the MBean to be instantiated.
- name

- The object name of the MBean. May be null.
- loaderName

- The object name of the class loader to be used.
- params

- An array containing the parameters of the
constructor to be invoked, encapsulated into a

MarshalledObject

. The encapsulated array can be
null, equivalent to an empty array.
- signature

- An array containing the signature of the
constructor to be invoked. Can be null, equivalent to an empty
array.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Returns:**
- An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
instantiated MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.

**Throws:**
- ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or a

java.lang.Exception

that occurred when trying to
invoke the MBean's constructor.
- InstanceAlreadyExistsException

- The MBean is already
under the control of the MBean server.
- MBeanRegistrationException

- The

preRegister

(

MBeanRegistration

interface) method of the MBean has thrown an exception. The
MBean will not be registered.
- MBeanException

- The constructor of the MBean has
thrown an exception.
- NotCompliantMBeanException

- This class is not a JMX
compliant MBean.
- InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null, the

ObjectName

passed
in parameter contains a pattern, or no

ObjectName

is specified for the MBean.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.

---

#### void unregisterMBean​(
ObjectName
name,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

MBeanRegistrationException
,

IOException

Handles the method

MBeanServerConnection.unregisterMBean(ObjectName)

.

**Parameters:**
- name

- The object name of the MBean to be unregistered.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Throws:**
- InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
- MBeanRegistrationException

- The preDeregister
((

MBeanRegistration

interface) method of the MBean
has thrown an exception.
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the MBean you are when trying to
unregister is the

MBeanServerDelegate

MBean.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.

---

#### ObjectInstance
getObjectInstance​(
ObjectName
name,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

IOException

Handles the method

MBeanServerConnection.getObjectInstance(ObjectName)

.

**Parameters:**
- name

- The object name of the MBean.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Returns:**
- The

ObjectInstance

associated with the MBean
specified by

name

. The contained

ObjectName

is

name

and the contained class name is

getMBeanInfo(name)

.getClassName()

.

**Throws:**
- InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.

---

#### Set
<
ObjectInstance
> queryMBeans​(
ObjectName
name,

MarshalledObject
query,

Subject
delegationSubject)
throws
IOException

Handles the method

MBeanServerConnection.queryMBeans(ObjectName,
QueryExp)

. The

QueryExp

is wrapped in a

MarshalledObject

.

**Parameters:**
- name

- The object name pattern identifying the MBeans to
be retrieved. If null or no domain and key properties are
specified, all the MBeans registered will be retrieved.
- query

- The query expression to be applied for selecting
MBeans, encapsulated into a

MarshalledObject

. If
the

MarshalledObject

encapsulates a null value no
query expression will be applied for selecting MBeans.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Returns:**
- A set containing the

ObjectInstance

objects for the selected MBeans. If no MBean satisfies the
query an empty list is returned.

**Throws:**
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.

---

#### Set
<
ObjectName
> queryNames​(
ObjectName
name,

MarshalledObject
query,

Subject
delegationSubject)
throws
IOException

Handles the method

MBeanServerConnection.queryNames(ObjectName,
QueryExp)

. The

QueryExp

is wrapped in a

MarshalledObject

.

**Parameters:**
- name

- The object name pattern identifying the MBean names
to be retrieved. If null or no domain and key properties are
specified, the name of all registered MBeans will be retrieved.
- query

- The query expression to be applied for selecting
MBeans, encapsulated into a

MarshalledObject

. If
the

MarshalledObject

encapsulates a null value no
query expression will be applied for selecting MBeans.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Returns:**
- A set containing the ObjectNames for the MBeans
selected. If no MBean satisfies the query, an empty list is
returned.

**Throws:**
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.

---

#### boolean isRegistered​(
ObjectName
name,

Subject
delegationSubject)
throws
IOException

Handles the method

MBeanServerConnection.isRegistered(ObjectName)

.

**Parameters:**
- name

- The object name of the MBean to be checked.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Returns:**
- True if the MBean is already registered in the MBean
server, false otherwise.

**Throws:**
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.

---

#### Integer
getMBeanCount​(
Subject
delegationSubject)
throws
IOException

Handles the method

MBeanServerConnection.getMBeanCount()

.

**Parameters:**
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Returns:**
- the number of MBeans registered.

**Throws:**
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.

---

#### Object
getAttribute​(
ObjectName
name,

String
attribute,

Subject
delegationSubject)
throws
MBeanException
,

AttributeNotFoundException
,

InstanceNotFoundException
,

ReflectionException
,

IOException

Handles the method

MBeanServerConnection.getAttribute(ObjectName,
String)

.

**Parameters:**
- name

- The object name of the MBean from which the
attribute is to be retrieved.
- attribute

- A String specifying the name of the attribute
to be retrieved.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Returns:**
- The value of the retrieved attribute.

**Throws:**
- AttributeNotFoundException

- The attribute specified
is not accessible in the MBean.
- MBeanException

- Wraps an exception thrown by the
MBean's getter.
- InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
- ReflectionException

- Wraps a

java.lang.Exception

thrown when trying to invoke
the getter.
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the attribute in parameter is
null.
- RuntimeMBeanException

- Wraps a runtime exception thrown
by the MBean's getter.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.

**See Also:**
- setAttribute(javax.management.ObjectName, java.rmi.MarshalledObject, javax.security.auth.Subject)

---

#### AttributeList
getAttributes​(
ObjectName
name,

String
[] attributes,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ReflectionException
,

IOException

Handles the method

MBeanServerConnection.getAttributes(ObjectName,
String[])

.

**Parameters:**
- name

- The object name of the MBean from which the
attributes are retrieved.
- attributes

- A list of the attributes to be retrieved.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Returns:**
- The list of the retrieved attributes.

**Throws:**
- InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
- ReflectionException

- An exception occurred when
trying to invoke the getAttributes method of a Dynamic MBean.
- RuntimeOperationsException

- Wrap a

java.lang.IllegalArgumentException

: The object
name in parameter is null or attributes in parameter is null.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.

**See Also:**
- setAttributes(javax.management.ObjectName, java.rmi.MarshalledObject, javax.security.auth.Subject)

---

#### void setAttribute​(
ObjectName
name,

MarshalledObject
attribute,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

AttributeNotFoundException
,

InvalidAttributeValueException
,

MBeanException
,

ReflectionException
,

IOException

Handles the method

MBeanServerConnection.setAttribute(ObjectName,
Attribute)

. The

Attribute

parameter is wrapped
in a

MarshalledObject

.

**Parameters:**
- name

- The name of the MBean within which the attribute is
to be set.
- attribute

- The identification of the attribute to be set
and the value it is to be set to, encapsulated into a

MarshalledObject

.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Throws:**
- InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
- AttributeNotFoundException

- The attribute specified
is not accessible in the MBean.
- InvalidAttributeValueException

- The value specified
for the attribute is not valid.
- MBeanException

- Wraps an exception thrown by the
MBean's setter.
- ReflectionException

- Wraps a

java.lang.Exception

thrown when trying to invoke
the setter.
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the attribute in parameter is
null.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.

**See Also:**
- getAttribute(javax.management.ObjectName, java.lang.String, javax.security.auth.Subject)

---

#### AttributeList
setAttributes​(
ObjectName
name,

MarshalledObject
attributes,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ReflectionException
,

IOException

Handles the method

MBeanServerConnection.setAttributes(ObjectName,
AttributeList)

. The

AttributeList

parameter is
wrapped in a

MarshalledObject

.

**Parameters:**
- name

- The object name of the MBean within which the
attributes are to be set.
- attributes

- A list of attributes: The identification of
the attributes to be set and the values they are to be set to,
encapsulated into a

MarshalledObject

.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Returns:**
- The list of attributes that were set, with their new
values.

**Throws:**
- InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
- ReflectionException

- An exception occurred when
trying to invoke the getAttributes method of a Dynamic MBean.
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or attributes in parameter is null.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.

**See Also:**
- getAttributes(javax.management.ObjectName, java.lang.String[], javax.security.auth.Subject)

---

#### Object
invoke​(
ObjectName
name,

String
operationName,

MarshalledObject
params,

String
[] signature,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

MBeanException
,

ReflectionException
,

IOException

Handles the method

MBeanServerConnection.invoke(ObjectName,
String, Object[], String[])

. The

Object[]

parameter is wrapped in a

MarshalledObject

.

**Parameters:**
- name

- The object name of the MBean on which the method is
to be invoked.
- operationName

- The name of the operation to be invoked.
- params

- An array containing the parameters to be set when
the operation is invoked, encapsulated into a

MarshalledObject

. The encapsulated array can be
null, equivalent to an empty array.
- signature

- An array containing the signature of the
operation. The class objects will be loaded using the same
class loader as the one used for loading the MBean on which the
operation was invoked. Can be null, equivalent to an empty
array.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Returns:**
- The object returned by the operation, which represents
the result of invoking the operation on the MBean specified.

**Throws:**
- InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
- MBeanException

- Wraps an exception thrown by the
MBean's invoked method.
- ReflectionException

- Wraps a

java.lang.Exception

thrown while trying to invoke
the method.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.
- RuntimeOperationsException

- Wraps an

IllegalArgumentException

when

name

or

operationName

is null.

---

#### String
getDefaultDomain​(
Subject
delegationSubject)
throws
IOException

Handles the method

MBeanServerConnection.getDefaultDomain()

.

**Parameters:**
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Returns:**
- the default domain.

**Throws:**
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.

---

#### String
[] getDomains​(
Subject
delegationSubject)
throws
IOException

Handles the method

MBeanServerConnection.getDomains()

.

**Parameters:**
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Returns:**
- the list of domains.

**Throws:**
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.

---

#### MBeanInfo
getMBeanInfo​(
ObjectName
name,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

IntrospectionException
,

ReflectionException
,

IOException

Handles the method

MBeanServerConnection.getMBeanInfo(ObjectName)

.

**Parameters:**
- name

- The name of the MBean to analyze
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Returns:**
- An instance of

MBeanInfo

allowing the
retrieval of all attributes and operations of this MBean.

**Throws:**
- IntrospectionException

- An exception occurred during
introspection.
- InstanceNotFoundException

- The MBean specified was
not found.
- ReflectionException

- An exception occurred when
trying to invoke the getMBeanInfo of a Dynamic MBean.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.

---

#### boolean isInstanceOf​(
ObjectName
name,

String
className,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

IOException

Handles the method

MBeanServerConnection.isInstanceOf(ObjectName,
String)

.

**Parameters:**
- name

- The

ObjectName

of the MBean.
- className

- The name of the class.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Returns:**
- true if the MBean specified is an instance of the
specified class according to the rules above, false otherwise.

**Throws:**
- InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.

---

#### void addNotificationListener​(
ObjectName
name,

ObjectName
listener,

MarshalledObject
filter,

MarshalledObject
handback,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

IOException

Handles the method

MBeanServerConnection.addNotificationListener(ObjectName,
ObjectName, NotificationFilter, Object)

. The

NotificationFilter

parameter is wrapped in a

MarshalledObject

. The

Object

(handback) parameter is also wrapped in a

MarshalledObject

.

**Parameters:**
- name

- The name of the MBean on which the listener should
be added.
- listener

- The object name of the listener which will
handle the notifications emitted by the registered MBean.
- filter

- The filter object, encapsulated into a

MarshalledObject

. If filter encapsulated in the

MarshalledObject

has a null value, no filtering
will be performed before handling notifications.
- handback

- The context to be sent to the listener when a
notification is emitted, encapsulated into a

MarshalledObject

.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Throws:**
- InstanceNotFoundException

- The MBean name of the
notification listener or of the notification broadcaster does
not match any of the registered MBeans.
- RuntimeOperationsException

- Wraps an

IllegalArgumentException

. The MBean named by

listener

exists but does not implement the

NotificationListener

interface,
or

name

or

listener

is null.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.

**See Also:**
- removeNotificationListener(ObjectName, ObjectName, Subject)

,

removeNotificationListener(ObjectName, ObjectName,
MarshalledObject, MarshalledObject, Subject)

---

#### void removeNotificationListener​(
ObjectName
name,

ObjectName
listener,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ListenerNotFoundException
,

IOException

Handles the method

MBeanServerConnection.removeNotificationListener(ObjectName,
ObjectName)

.

**Parameters:**
- name

- The name of the MBean on which the listener should
be removed.
- listener

- The object name of the listener to be removed.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Throws:**
- InstanceNotFoundException

- The MBean name provided
does not match any of the registered MBeans.
- ListenerNotFoundException

- The listener is not
registered in the MBean.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.
- RuntimeOperationsException

- Wraps an

IllegalArgumentException

when

name

or

listener

is null.

**See Also:**
- addNotificationListener(javax.management.ObjectName, javax.management.ObjectName, java.rmi.MarshalledObject, java.rmi.MarshalledObject, javax.security.auth.Subject)

---

#### void removeNotificationListener​(
ObjectName
name,

ObjectName
listener,

MarshalledObject
filter,

MarshalledObject
handback,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ListenerNotFoundException
,

IOException

Handles the method

MBeanServerConnection.removeNotificationListener(ObjectName,
ObjectName, NotificationFilter, Object)

. The

NotificationFilter

parameter is wrapped in a

MarshalledObject

. The

Object

parameter is also wrapped in a

MarshalledObject

.

**Parameters:**
- name

- The name of the MBean on which the listener should
be removed.
- listener

- A listener that was previously added to this
MBean.
- filter

- The filter that was specified when the listener
was added, encapsulated into a

MarshalledObject

.
- handback

- The handback that was specified when the
listener was added, encapsulated into a

MarshalledObject

.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Throws:**
- InstanceNotFoundException

- The MBean name provided
does not match any of the registered MBeans.
- ListenerNotFoundException

- The listener is not
registered in the MBean, or it is not registered with the given
filter and handback.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
- IOException

- if a general communication exception occurred.
- RuntimeOperationsException

- Wraps an

IllegalArgumentException

when

name

or

listener

is null.

**See Also:**
- addNotificationListener(javax.management.ObjectName, javax.management.ObjectName, java.rmi.MarshalledObject, java.rmi.MarshalledObject, javax.security.auth.Subject)

---

#### Integer
[] addNotificationListeners​(
ObjectName
[] names,

MarshalledObject
[] filters,

Subject
[] delegationSubjects)
throws
InstanceNotFoundException
,

IOException

Handles the method

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

.

Register for notifications from the given MBeans that match
the given filters. The remote client can subsequently retrieve
the notifications using the

fetchNotifications

method.

For each listener, the original

NotificationListener

and

handback

are
kept on the client side; in order for the client to be able to
identify them, the server generates and returns a unique

listenerID

. This

listenerID

is
forwarded with the

Notifications

to the remote
client.

If any one of the given (name, filter) pairs cannot be
registered, then the operation fails with an exception, and no
names or filters are registered.

**Parameters:**
- names

- the

ObjectNames

identifying the
MBeans emitting the Notifications.
- filters

- an array of marshalled representations of the

NotificationFilters

. Elements of this array can
be null.
- delegationSubjects

- the

Subjects

on behalf
of which the listeners are being added. Elements of this array
can be null. Also, the

delegationSubjects

parameter itself can be null, which is equivalent to an array
of null values with the same size as the

names

and

filters

arrays.

**Returns:**
- an array of

listenerIDs

identifying the
local listeners. This array has the same number of elements as
the parameters.

**Throws:**
- IllegalArgumentException

- if

names

or

filters

is null, or if

names

contains
a null element, or if the three arrays do not all have the same
size.
- ClassCastException

- if one of the elements of

filters

unmarshalls as a non-null object that is
not a

NotificationFilter

.
- InstanceNotFoundException

- if one of the

names

does not correspond to any registered MBean.
- SecurityException

- if, for one of the MBeans, the
client, or the delegated Subject if any, does not have
permission to add a listener.
- IOException

- if a general communication exception occurred.

---

#### void removeNotificationListeners​(
ObjectName
name,

Integer
[] listenerIDs,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ListenerNotFoundException
,

IOException

Handles the

removeNotificationListener(ObjectName, NotificationListener)

and

removeNotificationListener(ObjectName, NotificationListener, NotificationFilter, Object)

methods.

This method removes one or more

NotificationListener

s from a given MBean in the
MBean server.

The

NotificationListeners

are identified by the
IDs which were returned by the

addNotificationListeners(ObjectName[], MarshalledObject[],
Subject[])

method.

**Parameters:**
- name

- the

ObjectName

identifying the MBean
emitting the Notifications.
- listenerIDs

- the list of the IDs corresponding to the
listeners to remove.
- delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.

**Throws:**
- InstanceNotFoundException

- if the given

name

does not correspond to any registered MBean.
- ListenerNotFoundException

- if one of the listeners was
not found on the server side. This exception can happen if the
MBean discarded a listener for some reason other than a call to

MBeanServer.removeNotificationListener

.
- SecurityException

- if the client, or the delegated Subject
if any, does not have permission to remove the listeners.
- IOException

- if a general communication exception occurred.
- IllegalArgumentException

- if

ObjectName

or

listenerIds

is null or if

listenerIds

contains a null element.

---

#### NotificationResult
fetchNotifications​(long clientSequenceNumber,
int maxNotifications,
long timeout)
throws
IOException

Retrieves notifications from the connector server. This
method can block until there is at least one notification or
until the specified timeout is reached. The method can also
return at any time with zero notifications.

A notification can be included in the result if its sequence
number is no less than

clientSequenceNumber

and
this client has registered at least one listener for the MBean
generating the notification, with a filter that accepts the
notification. Each listener that is interested in the
notification is identified by an Integer ID that was returned
by

addNotificationListeners(ObjectName[],
MarshalledObject[], Subject[])

.

**Parameters:**
- clientSequenceNumber

- the first sequence number that the
client is interested in. If negative, it is interpreted as
meaning the sequence number that the next notification will
have.
- maxNotifications

- the maximum number of different
notifications to return. The

TargetedNotification

array in the returned

NotificationResult

can have
more elements than this if the same notification appears more
than once. The behavior is unspecified if this parameter is
negative.
- timeout

- the maximum time in milliseconds to wait for a
notification to arrive. This can be 0 to indicate that the
method should not wait if there are no notifications, but
should return at once. It can be

Long.MAX_VALUE

to indicate that there is no timeout. The behavior is
unspecified if this parameter is negative.

**Returns:**
- A

NotificationResult

.

**Throws:**
- IOException

- if a general communication exception occurred.

---

### Additional Sections

#### Interface RMIConnection

**All Superinterfaces:** AutoCloseable

,

Closeable

,

Remote

**All Known Implementing Classes:** RMIConnectionImpl

,

RMIConnectionImpl_Stub

```java
public interface
RMIConnection

extends
Closeable
,
Remote
```

RMI object used to forward an MBeanServer request from a client
to its MBeanServer implementation on the server side. There is one
Remote object implementing this interface for each remote client
connected to an RMI connector.

User code does not usually refer to this interface. It is
specified as part of the public API so that different
implementations of that API will interoperate.

To ensure that client parameters will be deserialized at the
server side with the correct classloader, client parameters such as
parameters used to invoke a method are wrapped in a

MarshalledObject

. An implementation of this interface must first
get the appropriate class loader for the operation and its target,
then deserialize the marshalled parameters with this classloader.
Except as noted, a parameter that is a

MarshalledObject

or

MarshalledObject[]

must not be null; the behavior is unspecified if it is.

Class loading aspects are detailed in the

JMX Specification, version 1.4

Most methods in this interface parallel methods in the

MBeanServerConnection

interface. Where an aspect of the behavior
of a method is not specified here, it is the same as in the
corresponding

MBeanServerConnection

method.

**Since:** 1.5

public interface

RMIConnection

extends

Closeable

,

Remote

RMI object used to forward an MBeanServer request from a client
to its MBeanServer implementation on the server side. There is one
Remote object implementing this interface for each remote client
connected to an RMI connector.

User code does not usually refer to this interface. It is
specified as part of the public API so that different
implementations of that API will interoperate.

To ensure that client parameters will be deserialized at the
server side with the correct classloader, client parameters such as
parameters used to invoke a method are wrapped in a

MarshalledObject

. An implementation of this interface must first
get the appropriate class loader for the operation and its target,
then deserialize the marshalled parameters with this classloader.
Except as noted, a parameter that is a

MarshalledObject

or

MarshalledObject[]

must not be null; the behavior is unspecified if it is.

Class loading aspects are detailed in the

JMX Specification, version 1.4

Most methods in this interface parallel methods in the

MBeanServerConnection

interface. Where an aspect of the behavior
of a method is not specified here, it is the same as in the
corresponding

MBeanServerConnection

method.

RMI object used to forward an MBeanServer request from a client
to its MBeanServer implementation on the server side. There is one
Remote object implementing this interface for each remote client
connected to an RMI connector.

User code does not usually refer to this interface. It is
specified as part of the public API so that different
implementations of that API will interoperate.

To ensure that client parameters will be deserialized at the
server side with the correct classloader, client parameters such as
parameters used to invoke a method are wrapped in a

MarshalledObject

. An implementation of this interface must first
get the appropriate class loader for the operation and its target,
then deserialize the marshalled parameters with this classloader.
Except as noted, a parameter that is a

MarshalledObject

or

MarshalledObject[]

must not be null; the behavior is unspecified if it is.

Class loading aspects are detailed in the

JMX Specification, version 1.4

Most methods in this interface parallel methods in the

MBeanServerConnection

interface. Where an aspect of the behavior
of a method is not specified here, it is the same as in the
corresponding

MBeanServerConnection

method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addNotificationListener

​(

ObjectName

name,

ObjectName

listener,

MarshalledObject

filter,

MarshalledObject

handback,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.addNotificationListener(ObjectName,
ObjectName, NotificationFilter, Object)

.

Integer

[]

addNotificationListeners

​(

ObjectName

[] names,

MarshalledObject

[] filters,

Subject

[] delegationSubjects)

Handles the method

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

.

void

close

()

Closes this connection.

ObjectInstance

createMBean

​(

String

className,

ObjectName

name,

MarshalledObject

params,

String

[] signature,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, Object[], String[])

.

ObjectInstance

createMBean

​(

String

className,

ObjectName

name,

ObjectName

loaderName,

MarshalledObject

params,

String

[] signature,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, ObjectName, Object[], String[])

.

ObjectInstance

createMBean

​(

String

className,

ObjectName

name,

ObjectName

loaderName,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, ObjectName)

.

ObjectInstance

createMBean

​(

String

className,

ObjectName

name,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName)

.

NotificationResult

fetchNotifications

​(long clientSequenceNumber,
int maxNotifications,
long timeout)

Retrieves notifications from the connector server.

Object

getAttribute

​(

ObjectName

name,

String

attribute,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.getAttribute(ObjectName,
String)

.

AttributeList

getAttributes

​(

ObjectName

name,

String

[] attributes,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.getAttributes(ObjectName,
String[])

.

String

getConnectionId

()

Returns the connection ID.

String

getDefaultDomain

​(

Subject

delegationSubject)

Handles the method

MBeanServerConnection.getDefaultDomain()

.

String

[]

getDomains

​(

Subject

delegationSubject)

Handles the method

MBeanServerConnection.getDomains()

.

Integer

getMBeanCount

​(

Subject

delegationSubject)

Handles the method

MBeanServerConnection.getMBeanCount()

.

MBeanInfo

getMBeanInfo

​(

ObjectName

name,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.getMBeanInfo(ObjectName)

.

ObjectInstance

getObjectInstance

​(

ObjectName

name,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.getObjectInstance(ObjectName)

.

Object

invoke

​(

ObjectName

name,

String

operationName,

MarshalledObject

params,

String

[] signature,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.invoke(ObjectName,
String, Object[], String[])

.

boolean

isInstanceOf

​(

ObjectName

name,

String

className,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.isInstanceOf(ObjectName,
String)

.

boolean

isRegistered

​(

ObjectName

name,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.isRegistered(ObjectName)

.

Set

<

ObjectInstance

>

queryMBeans

​(

ObjectName

name,

MarshalledObject

query,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.queryMBeans(ObjectName,
QueryExp)

.

Set

<

ObjectName

>

queryNames

​(

ObjectName

name,

MarshalledObject

query,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.queryNames(ObjectName,
QueryExp)

.

void

removeNotificationListener

​(

ObjectName

name,

ObjectName

listener,

MarshalledObject

filter,

MarshalledObject

handback,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.removeNotificationListener(ObjectName,
ObjectName, NotificationFilter, Object)

.

void

removeNotificationListener

​(

ObjectName

name,

ObjectName

listener,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.removeNotificationListener(ObjectName,
ObjectName)

.

void

removeNotificationListeners

​(

ObjectName

name,

Integer

[] listenerIDs,

Subject

delegationSubject)

Handles the

removeNotificationListener(ObjectName, NotificationListener)

and

removeNotificationListener(ObjectName, NotificationListener, NotificationFilter, Object)

methods.

void

setAttribute

​(

ObjectName

name,

MarshalledObject

attribute,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.setAttribute(ObjectName,
Attribute)

.

AttributeList

setAttributes

​(

ObjectName

name,

MarshalledObject

attributes,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.setAttributes(ObjectName,
AttributeList)

.

void

unregisterMBean

​(

ObjectName

name,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.unregisterMBean(ObjectName)

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addNotificationListener

​(

ObjectName

name,

ObjectName

listener,

MarshalledObject

filter,

MarshalledObject

handback,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.addNotificationListener(ObjectName,
ObjectName, NotificationFilter, Object)

.

Integer

[]

addNotificationListeners

​(

ObjectName

[] names,

MarshalledObject

[] filters,

Subject

[] delegationSubjects)

Handles the method

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

.

void

close

()

Closes this connection.

ObjectInstance

createMBean

​(

String

className,

ObjectName

name,

MarshalledObject

params,

String

[] signature,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, Object[], String[])

.

ObjectInstance

createMBean

​(

String

className,

ObjectName

name,

ObjectName

loaderName,

MarshalledObject

params,

String

[] signature,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, ObjectName, Object[], String[])

.

ObjectInstance

createMBean

​(

String

className,

ObjectName

name,

ObjectName

loaderName,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, ObjectName)

.

ObjectInstance

createMBean

​(

String

className,

ObjectName

name,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName)

.

NotificationResult

fetchNotifications

​(long clientSequenceNumber,
int maxNotifications,
long timeout)

Retrieves notifications from the connector server.

Object

getAttribute

​(

ObjectName

name,

String

attribute,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.getAttribute(ObjectName,
String)

.

AttributeList

getAttributes

​(

ObjectName

name,

String

[] attributes,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.getAttributes(ObjectName,
String[])

.

String

getConnectionId

()

Returns the connection ID.

String

getDefaultDomain

​(

Subject

delegationSubject)

Handles the method

MBeanServerConnection.getDefaultDomain()

.

String

[]

getDomains

​(

Subject

delegationSubject)

Handles the method

MBeanServerConnection.getDomains()

.

Integer

getMBeanCount

​(

Subject

delegationSubject)

Handles the method

MBeanServerConnection.getMBeanCount()

.

MBeanInfo

getMBeanInfo

​(

ObjectName

name,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.getMBeanInfo(ObjectName)

.

ObjectInstance

getObjectInstance

​(

ObjectName

name,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.getObjectInstance(ObjectName)

.

Object

invoke

​(

ObjectName

name,

String

operationName,

MarshalledObject

params,

String

[] signature,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.invoke(ObjectName,
String, Object[], String[])

.

boolean

isInstanceOf

​(

ObjectName

name,

String

className,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.isInstanceOf(ObjectName,
String)

.

boolean

isRegistered

​(

ObjectName

name,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.isRegistered(ObjectName)

.

Set

<

ObjectInstance

>

queryMBeans

​(

ObjectName

name,

MarshalledObject

query,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.queryMBeans(ObjectName,
QueryExp)

.

Set

<

ObjectName

>

queryNames

​(

ObjectName

name,

MarshalledObject

query,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.queryNames(ObjectName,
QueryExp)

.

void

removeNotificationListener

​(

ObjectName

name,

ObjectName

listener,

MarshalledObject

filter,

MarshalledObject

handback,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.removeNotificationListener(ObjectName,
ObjectName, NotificationFilter, Object)

.

void

removeNotificationListener

​(

ObjectName

name,

ObjectName

listener,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.removeNotificationListener(ObjectName,
ObjectName)

.

void

removeNotificationListeners

​(

ObjectName

name,

Integer

[] listenerIDs,

Subject

delegationSubject)

Handles the

removeNotificationListener(ObjectName, NotificationListener)

and

removeNotificationListener(ObjectName, NotificationListener, NotificationFilter, Object)

methods.

void

setAttribute

​(

ObjectName

name,

MarshalledObject

attribute,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.setAttribute(ObjectName,
Attribute)

.

AttributeList

setAttributes

​(

ObjectName

name,

MarshalledObject

attributes,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.setAttributes(ObjectName,
AttributeList)

.

void

unregisterMBean

​(

ObjectName

name,

Subject

delegationSubject)

Handles the method

MBeanServerConnection.unregisterMBean(ObjectName)

.

---

#### Method Summary

Handles the method

MBeanServerConnection.addNotificationListener(ObjectName,
ObjectName, NotificationFilter, Object)

.

Handles the method

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

.

Closes this connection.

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, Object[], String[])

.

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, ObjectName, Object[], String[])

.

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, ObjectName)

.

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName)

.

Retrieves notifications from the connector server.

Handles the method

MBeanServerConnection.getAttribute(ObjectName,
String)

.

Handles the method

MBeanServerConnection.getAttributes(ObjectName,
String[])

.

Returns the connection ID.

Handles the method

MBeanServerConnection.getDefaultDomain()

.

Handles the method

MBeanServerConnection.getDomains()

.

Handles the method

MBeanServerConnection.getMBeanCount()

.

Handles the method

MBeanServerConnection.getMBeanInfo(ObjectName)

.

Handles the method

MBeanServerConnection.getObjectInstance(ObjectName)

.

Handles the method

MBeanServerConnection.invoke(ObjectName,
String, Object[], String[])

.

Handles the method

MBeanServerConnection.isInstanceOf(ObjectName,
String)

.

Handles the method

MBeanServerConnection.isRegistered(ObjectName)

.

Handles the method

MBeanServerConnection.queryMBeans(ObjectName,
QueryExp)

.

Handles the method

MBeanServerConnection.queryNames(ObjectName,
QueryExp)

.

Handles the method

MBeanServerConnection.removeNotificationListener(ObjectName,
ObjectName, NotificationFilter, Object)

.

Handles the method

MBeanServerConnection.removeNotificationListener(ObjectName,
ObjectName)

.

Handles the

removeNotificationListener(ObjectName, NotificationListener)

and

removeNotificationListener(ObjectName, NotificationListener, NotificationFilter, Object)

methods.

Handles the method

MBeanServerConnection.setAttribute(ObjectName,
Attribute)

.

Handles the method

MBeanServerConnection.setAttributes(ObjectName,
AttributeList)

.

Handles the method

MBeanServerConnection.unregisterMBean(ObjectName)

.

============ METHOD DETAIL ==========

- Method Detail

- getConnectionId

```java
String
getConnectionId()
throws
IOException
```

Returns the connection ID. This string is different for
every open connection to a given RMI connector server.

**Returns:** the connection ID
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** RMIConnector.connect

- close

```java
void close()
throws
IOException
```

Closes this connection. On return from this method, the RMI
object implementing this interface is unexported, so further
remote calls to it will fail.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if the connection could not be closed,
or the Remote object could not be unexported, or there was a
communication failure when transmitting the remote close
request.

- createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name,

Subject
delegationSubject)
throws
ReflectionException
,

InstanceAlreadyExistsException
,

MBeanRegistrationException
,

MBeanException
,

NotCompliantMBeanException
,

IOException
```

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName)

.

**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
instantiated MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or a

java.lang.Exception

that occurred
when trying to invoke the MBean's constructor.
**Throws:** InstanceAlreadyExistsException

- The MBean is already
under the control of the MBean server.
**Throws:** MBeanRegistrationException

- The

preRegister

(

MBeanRegistration

interface) method of the MBean has thrown an exception. The
MBean will not be registered.
**Throws:** MBeanException

- The constructor of the MBean has
thrown an exception.
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null, the

ObjectName

passed
in parameter contains a pattern or no

ObjectName

is specified for the MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name,

ObjectName
loaderName,

Subject
delegationSubject)
throws
ReflectionException
,

InstanceAlreadyExistsException
,

MBeanRegistrationException
,

MBeanException
,

NotCompliantMBeanException
,

InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, ObjectName)

.

**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** loaderName

- The object name of the class loader to be used.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
instantiated MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or a

java.lang.Exception

that occurred when trying to
invoke the MBean's constructor.
**Throws:** InstanceAlreadyExistsException

- The MBean is already
under the control of the MBean server.
**Throws:** MBeanRegistrationException

- The

preRegister

(

MBeanRegistration

interface) method of the MBean has thrown an exception. The
MBean will not be registered.
**Throws:** MBeanException

- The constructor of the MBean has
thrown an exception.
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean.
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null, the

ObjectName

passed
in parameter contains a pattern or no

ObjectName

is specified for the MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name,

MarshalledObject
params,

String
[] signature,

Subject
delegationSubject)
throws
ReflectionException
,

InstanceAlreadyExistsException
,

MBeanRegistrationException
,

MBeanException
,

NotCompliantMBeanException
,

IOException
```

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, Object[], String[])

. The

Object[]

parameter is wrapped in a

MarshalledObject

.

**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked, encapsulated into a

MarshalledObject

. The encapsulated array can be
null, equivalent to an empty array.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked. Can be null, equivalent to an empty
array.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
instantiated MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or a

java.lang.Exception

that occurred when trying to
invoke the MBean's constructor.
**Throws:** InstanceAlreadyExistsException

- The MBean is already
under the control of the MBean server.
**Throws:** MBeanRegistrationException

- The

preRegister

(

MBeanRegistration

interface) method of the MBean has thrown an exception. The
MBean will not be registered.
**Throws:** MBeanException

- The constructor of the MBean has
thrown an exception.
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null, the

ObjectName

passed
in parameter contains a pattern, or no

ObjectName

is specified for the MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name,

ObjectName
loaderName,

MarshalledObject
params,

String
[] signature,

Subject
delegationSubject)
throws
ReflectionException
,

InstanceAlreadyExistsException
,

MBeanRegistrationException
,

MBeanException
,

NotCompliantMBeanException
,

InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, ObjectName, Object[], String[])

. The

Object[]

parameter is wrapped in a

MarshalledObject

.

**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** loaderName

- The object name of the class loader to be used.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked, encapsulated into a

MarshalledObject

. The encapsulated array can be
null, equivalent to an empty array.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked. Can be null, equivalent to an empty
array.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
instantiated MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or a

java.lang.Exception

that occurred when trying to
invoke the MBean's constructor.
**Throws:** InstanceAlreadyExistsException

- The MBean is already
under the control of the MBean server.
**Throws:** MBeanRegistrationException

- The

preRegister

(

MBeanRegistration

interface) method of the MBean has thrown an exception. The
MBean will not be registered.
**Throws:** MBeanException

- The constructor of the MBean has
thrown an exception.
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean.
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null, the

ObjectName

passed
in parameter contains a pattern, or no

ObjectName

is specified for the MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- unregisterMBean

```java
void unregisterMBean​(
ObjectName
name,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

MBeanRegistrationException
,

IOException
```

Handles the method

MBeanServerConnection.unregisterMBean(ObjectName)

.

**Parameters:** name

- The object name of the MBean to be unregistered.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** MBeanRegistrationException

- The preDeregister
((

MBeanRegistration

interface) method of the MBean
has thrown an exception.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the MBean you are when trying to
unregister is the

MBeanServerDelegate

MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- getObjectInstance

```java
ObjectInstance
getObjectInstance​(
ObjectName
name,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.getObjectInstance(ObjectName)

.

**Parameters:** name

- The object name of the MBean.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** The

ObjectInstance

associated with the MBean
specified by

name

. The contained

ObjectName

is

name

and the contained class name is

getMBeanInfo(name)

.getClassName()

.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- queryMBeans

```java
Set
<
ObjectInstance
> queryMBeans​(
ObjectName
name,

MarshalledObject
query,

Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.queryMBeans(ObjectName,
QueryExp)

. The

QueryExp

is wrapped in a

MarshalledObject

.

**Parameters:** name

- The object name pattern identifying the MBeans to
be retrieved. If null or no domain and key properties are
specified, all the MBeans registered will be retrieved.
**Parameters:** query

- The query expression to be applied for selecting
MBeans, encapsulated into a

MarshalledObject

. If
the

MarshalledObject

encapsulates a null value no
query expression will be applied for selecting MBeans.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** A set containing the

ObjectInstance

objects for the selected MBeans. If no MBean satisfies the
query an empty list is returned.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- queryNames

```java
Set
<
ObjectName
> queryNames​(
ObjectName
name,

MarshalledObject
query,

Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.queryNames(ObjectName,
QueryExp)

. The

QueryExp

is wrapped in a

MarshalledObject

.

**Parameters:** name

- The object name pattern identifying the MBean names
to be retrieved. If null or no domain and key properties are
specified, the name of all registered MBeans will be retrieved.
**Parameters:** query

- The query expression to be applied for selecting
MBeans, encapsulated into a

MarshalledObject

. If
the

MarshalledObject

encapsulates a null value no
query expression will be applied for selecting MBeans.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** A set containing the ObjectNames for the MBeans
selected. If no MBean satisfies the query, an empty list is
returned.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- isRegistered

```java
boolean isRegistered​(
ObjectName
name,

Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.isRegistered(ObjectName)

.

**Parameters:** name

- The object name of the MBean to be checked.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** True if the MBean is already registered in the MBean
server, false otherwise.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- getMBeanCount

```java
Integer
getMBeanCount​(
Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.getMBeanCount()

.

**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** the number of MBeans registered.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- getAttribute

```java
Object
getAttribute​(
ObjectName
name,

String
attribute,

Subject
delegationSubject)
throws
MBeanException
,

AttributeNotFoundException
,

InstanceNotFoundException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.getAttribute(ObjectName,
String)

.

**Parameters:** name

- The object name of the MBean from which the
attribute is to be retrieved.
**Parameters:** attribute

- A String specifying the name of the attribute
to be retrieved.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** The value of the retrieved attribute.
**Throws:** AttributeNotFoundException

- The attribute specified
is not accessible in the MBean.
**Throws:** MBeanException

- Wraps an exception thrown by the
MBean's getter.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown when trying to invoke
the getter.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the attribute in parameter is
null.
**Throws:** RuntimeMBeanException

- Wraps a runtime exception thrown
by the MBean's getter.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** setAttribute(javax.management.ObjectName, java.rmi.MarshalledObject, javax.security.auth.Subject)

- getAttributes

```java
AttributeList
getAttributes​(
ObjectName
name,

String
[] attributes,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.getAttributes(ObjectName,
String[])

.

**Parameters:** name

- The object name of the MBean from which the
attributes are retrieved.
**Parameters:** attributes

- A list of the attributes to be retrieved.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** The list of the retrieved attributes.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- An exception occurred when
trying to invoke the getAttributes method of a Dynamic MBean.
**Throws:** RuntimeOperationsException

- Wrap a

java.lang.IllegalArgumentException

: The object
name in parameter is null or attributes in parameter is null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** setAttributes(javax.management.ObjectName, java.rmi.MarshalledObject, javax.security.auth.Subject)

- setAttribute

```java
void setAttribute​(
ObjectName
name,

MarshalledObject
attribute,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

AttributeNotFoundException
,

InvalidAttributeValueException
,

MBeanException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.setAttribute(ObjectName,
Attribute)

. The

Attribute

parameter is wrapped
in a

MarshalledObject

.

**Parameters:** name

- The name of the MBean within which the attribute is
to be set.
**Parameters:** attribute

- The identification of the attribute to be set
and the value it is to be set to, encapsulated into a

MarshalledObject

.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** AttributeNotFoundException

- The attribute specified
is not accessible in the MBean.
**Throws:** InvalidAttributeValueException

- The value specified
for the attribute is not valid.
**Throws:** MBeanException

- Wraps an exception thrown by the
MBean's setter.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown when trying to invoke
the setter.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the attribute in parameter is
null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** getAttribute(javax.management.ObjectName, java.lang.String, javax.security.auth.Subject)

- setAttributes

```java
AttributeList
setAttributes​(
ObjectName
name,

MarshalledObject
attributes,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.setAttributes(ObjectName,
AttributeList)

. The

AttributeList

parameter is
wrapped in a

MarshalledObject

.

**Parameters:** name

- The object name of the MBean within which the
attributes are to be set.
**Parameters:** attributes

- A list of attributes: The identification of
the attributes to be set and the values they are to be set to,
encapsulated into a

MarshalledObject

.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** The list of attributes that were set, with their new
values.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- An exception occurred when
trying to invoke the getAttributes method of a Dynamic MBean.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or attributes in parameter is null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** getAttributes(javax.management.ObjectName, java.lang.String[], javax.security.auth.Subject)

- invoke

```java
Object
invoke​(
ObjectName
name,

String
operationName,

MarshalledObject
params,

String
[] signature,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

MBeanException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.invoke(ObjectName,
String, Object[], String[])

. The

Object[]

parameter is wrapped in a

MarshalledObject

.

**Parameters:** name

- The object name of the MBean on which the method is
to be invoked.
**Parameters:** operationName

- The name of the operation to be invoked.
**Parameters:** params

- An array containing the parameters to be set when
the operation is invoked, encapsulated into a

MarshalledObject

. The encapsulated array can be
null, equivalent to an empty array.
**Parameters:** signature

- An array containing the signature of the
operation. The class objects will be loaded using the same
class loader as the one used for loading the MBean on which the
operation was invoked. Can be null, equivalent to an empty
array.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** The object returned by the operation, which represents
the result of invoking the operation on the MBean specified.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** MBeanException

- Wraps an exception thrown by the
MBean's invoked method.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown while trying to invoke
the method.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

when

name

or

operationName

is null.

- getDefaultDomain

```java
String
getDefaultDomain​(
Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.getDefaultDomain()

.

**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** the default domain.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- getDomains

```java
String
[] getDomains​(
Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.getDomains()

.

**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** the list of domains.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- getMBeanInfo

```java
MBeanInfo
getMBeanInfo​(
ObjectName
name,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

IntrospectionException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.getMBeanInfo(ObjectName)

.

**Parameters:** name

- The name of the MBean to analyze
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** An instance of

MBeanInfo

allowing the
retrieval of all attributes and operations of this MBean.
**Throws:** IntrospectionException

- An exception occurred during
introspection.
**Throws:** InstanceNotFoundException

- The MBean specified was
not found.
**Throws:** ReflectionException

- An exception occurred when
trying to invoke the getMBeanInfo of a Dynamic MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.

- isInstanceOf

```java
boolean isInstanceOf​(
ObjectName
name,

String
className,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.isInstanceOf(ObjectName,
String)

.

**Parameters:** name

- The

ObjectName

of the MBean.
**Parameters:** className

- The name of the class.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** true if the MBean specified is an instance of the
specified class according to the rules above, false otherwise.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.

- addNotificationListener

```java
void addNotificationListener​(
ObjectName
name,

ObjectName
listener,

MarshalledObject
filter,

MarshalledObject
handback,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.addNotificationListener(ObjectName,
ObjectName, NotificationFilter, Object)

. The

NotificationFilter

parameter is wrapped in a

MarshalledObject

. The

Object

(handback) parameter is also wrapped in a

MarshalledObject

.

**Parameters:** name

- The name of the MBean on which the listener should
be added.
**Parameters:** listener

- The object name of the listener which will
handle the notifications emitted by the registered MBean.
**Parameters:** filter

- The filter object, encapsulated into a

MarshalledObject

. If filter encapsulated in the

MarshalledObject

has a null value, no filtering
will be performed before handling notifications.
**Parameters:** handback

- The context to be sent to the listener when a
notification is emitted, encapsulated into a

MarshalledObject

.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- The MBean name of the
notification listener or of the notification broadcaster does
not match any of the registered MBeans.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

. The MBean named by

listener

exists but does not implement the

NotificationListener

interface,
or

name

or

listener

is null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** removeNotificationListener(ObjectName, ObjectName, Subject)

,

removeNotificationListener(ObjectName, ObjectName,
MarshalledObject, MarshalledObject, Subject)

- removeNotificationListener

```java
void removeNotificationListener​(
ObjectName
name,

ObjectName
listener,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ListenerNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.removeNotificationListener(ObjectName,
ObjectName)

.

**Parameters:** name

- The name of the MBean on which the listener should
be removed.
**Parameters:** listener

- The object name of the listener to be removed.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- The MBean name provided
does not match any of the registered MBeans.
**Throws:** ListenerNotFoundException

- The listener is not
registered in the MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

when

name

or

listener

is null.
**See Also:** addNotificationListener(javax.management.ObjectName, javax.management.ObjectName, java.rmi.MarshalledObject, java.rmi.MarshalledObject, javax.security.auth.Subject)

- removeNotificationListener

```java
void removeNotificationListener​(
ObjectName
name,

ObjectName
listener,

MarshalledObject
filter,

MarshalledObject
handback,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ListenerNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.removeNotificationListener(ObjectName,
ObjectName, NotificationFilter, Object)

. The

NotificationFilter

parameter is wrapped in a

MarshalledObject

. The

Object

parameter is also wrapped in a

MarshalledObject

.

**Parameters:** name

- The name of the MBean on which the listener should
be removed.
**Parameters:** listener

- A listener that was previously added to this
MBean.
**Parameters:** filter

- The filter that was specified when the listener
was added, encapsulated into a

MarshalledObject

.
**Parameters:** handback

- The handback that was specified when the
listener was added, encapsulated into a

MarshalledObject

.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- The MBean name provided
does not match any of the registered MBeans.
**Throws:** ListenerNotFoundException

- The listener is not
registered in the MBean, or it is not registered with the given
filter and handback.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

when

name

or

listener

is null.
**See Also:** addNotificationListener(javax.management.ObjectName, javax.management.ObjectName, java.rmi.MarshalledObject, java.rmi.MarshalledObject, javax.security.auth.Subject)

- addNotificationListeners

```java
Integer
[] addNotificationListeners​(
ObjectName
[] names,

MarshalledObject
[] filters,

Subject
[] delegationSubjects)
throws
InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

.

Register for notifications from the given MBeans that match
the given filters. The remote client can subsequently retrieve
the notifications using the

fetchNotifications

method.

For each listener, the original

NotificationListener

and

handback

are
kept on the client side; in order for the client to be able to
identify them, the server generates and returns a unique

listenerID

. This

listenerID

is
forwarded with the

Notifications

to the remote
client.

If any one of the given (name, filter) pairs cannot be
registered, then the operation fails with an exception, and no
names or filters are registered.

**Parameters:** names

- the

ObjectNames

identifying the
MBeans emitting the Notifications.
**Parameters:** filters

- an array of marshalled representations of the

NotificationFilters

. Elements of this array can
be null.
**Parameters:** delegationSubjects

- the

Subjects

on behalf
of which the listeners are being added. Elements of this array
can be null. Also, the

delegationSubjects

parameter itself can be null, which is equivalent to an array
of null values with the same size as the

names

and

filters

arrays.
**Returns:** an array of

listenerIDs

identifying the
local listeners. This array has the same number of elements as
the parameters.
**Throws:** IllegalArgumentException

- if

names

or

filters

is null, or if

names

contains
a null element, or if the three arrays do not all have the same
size.
**Throws:** ClassCastException

- if one of the elements of

filters

unmarshalls as a non-null object that is
not a

NotificationFilter

.
**Throws:** InstanceNotFoundException

- if one of the

names

does not correspond to any registered MBean.
**Throws:** SecurityException

- if, for one of the MBeans, the
client, or the delegated Subject if any, does not have
permission to add a listener.
**Throws:** IOException

- if a general communication exception occurred.

- removeNotificationListeners

```java
void removeNotificationListeners​(
ObjectName
name,

Integer
[] listenerIDs,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ListenerNotFoundException
,

IOException
```

Handles the

removeNotificationListener(ObjectName, NotificationListener)

and

removeNotificationListener(ObjectName, NotificationListener, NotificationFilter, Object)

methods.

This method removes one or more

NotificationListener

s from a given MBean in the
MBean server.

The

NotificationListeners

are identified by the
IDs which were returned by the

addNotificationListeners(ObjectName[], MarshalledObject[],
Subject[])

method.

**Parameters:** name

- the

ObjectName

identifying the MBean
emitting the Notifications.
**Parameters:** listenerIDs

- the list of the IDs corresponding to the
listeners to remove.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- if the given

name

does not correspond to any registered MBean.
**Throws:** ListenerNotFoundException

- if one of the listeners was
not found on the server side. This exception can happen if the
MBean discarded a listener for some reason other than a call to

MBeanServer.removeNotificationListener

.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to remove the listeners.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** IllegalArgumentException

- if

ObjectName

or

listenerIds

is null or if

listenerIds

contains a null element.

- fetchNotifications

```java
NotificationResult
fetchNotifications​(long clientSequenceNumber,
int maxNotifications,
long timeout)
throws
IOException
```

Retrieves notifications from the connector server. This
method can block until there is at least one notification or
until the specified timeout is reached. The method can also
return at any time with zero notifications.

A notification can be included in the result if its sequence
number is no less than

clientSequenceNumber

and
this client has registered at least one listener for the MBean
generating the notification, with a filter that accepts the
notification. Each listener that is interested in the
notification is identified by an Integer ID that was returned
by

addNotificationListeners(ObjectName[],
MarshalledObject[], Subject[])

.

**Parameters:** clientSequenceNumber

- the first sequence number that the
client is interested in. If negative, it is interpreted as
meaning the sequence number that the next notification will
have.
**Parameters:** maxNotifications

- the maximum number of different
notifications to return. The

TargetedNotification

array in the returned

NotificationResult

can have
more elements than this if the same notification appears more
than once. The behavior is unspecified if this parameter is
negative.
**Parameters:** timeout

- the maximum time in milliseconds to wait for a
notification to arrive. This can be 0 to indicate that the
method should not wait if there are no notifications, but
should return at once. It can be

Long.MAX_VALUE

to indicate that there is no timeout. The behavior is
unspecified if this parameter is negative.
**Returns:** A

NotificationResult

.
**Throws:** IOException

- if a general communication exception occurred.

Method Detail

- getConnectionId

```java
String
getConnectionId()
throws
IOException
```

Returns the connection ID. This string is different for
every open connection to a given RMI connector server.

**Returns:** the connection ID
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** RMIConnector.connect

- close

```java
void close()
throws
IOException
```

Closes this connection. On return from this method, the RMI
object implementing this interface is unexported, so further
remote calls to it will fail.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if the connection could not be closed,
or the Remote object could not be unexported, or there was a
communication failure when transmitting the remote close
request.

- createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name,

Subject
delegationSubject)
throws
ReflectionException
,

InstanceAlreadyExistsException
,

MBeanRegistrationException
,

MBeanException
,

NotCompliantMBeanException
,

IOException
```

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName)

.

**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
instantiated MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or a

java.lang.Exception

that occurred
when trying to invoke the MBean's constructor.
**Throws:** InstanceAlreadyExistsException

- The MBean is already
under the control of the MBean server.
**Throws:** MBeanRegistrationException

- The

preRegister

(

MBeanRegistration

interface) method of the MBean has thrown an exception. The
MBean will not be registered.
**Throws:** MBeanException

- The constructor of the MBean has
thrown an exception.
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null, the

ObjectName

passed
in parameter contains a pattern or no

ObjectName

is specified for the MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name,

ObjectName
loaderName,

Subject
delegationSubject)
throws
ReflectionException
,

InstanceAlreadyExistsException
,

MBeanRegistrationException
,

MBeanException
,

NotCompliantMBeanException
,

InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, ObjectName)

.

**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** loaderName

- The object name of the class loader to be used.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
instantiated MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or a

java.lang.Exception

that occurred when trying to
invoke the MBean's constructor.
**Throws:** InstanceAlreadyExistsException

- The MBean is already
under the control of the MBean server.
**Throws:** MBeanRegistrationException

- The

preRegister

(

MBeanRegistration

interface) method of the MBean has thrown an exception. The
MBean will not be registered.
**Throws:** MBeanException

- The constructor of the MBean has
thrown an exception.
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean.
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null, the

ObjectName

passed
in parameter contains a pattern or no

ObjectName

is specified for the MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name,

MarshalledObject
params,

String
[] signature,

Subject
delegationSubject)
throws
ReflectionException
,

InstanceAlreadyExistsException
,

MBeanRegistrationException
,

MBeanException
,

NotCompliantMBeanException
,

IOException
```

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, Object[], String[])

. The

Object[]

parameter is wrapped in a

MarshalledObject

.

**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked, encapsulated into a

MarshalledObject

. The encapsulated array can be
null, equivalent to an empty array.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked. Can be null, equivalent to an empty
array.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
instantiated MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or a

java.lang.Exception

that occurred when trying to
invoke the MBean's constructor.
**Throws:** InstanceAlreadyExistsException

- The MBean is already
under the control of the MBean server.
**Throws:** MBeanRegistrationException

- The

preRegister

(

MBeanRegistration

interface) method of the MBean has thrown an exception. The
MBean will not be registered.
**Throws:** MBeanException

- The constructor of the MBean has
thrown an exception.
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null, the

ObjectName

passed
in parameter contains a pattern, or no

ObjectName

is specified for the MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name,

ObjectName
loaderName,

MarshalledObject
params,

String
[] signature,

Subject
delegationSubject)
throws
ReflectionException
,

InstanceAlreadyExistsException
,

MBeanRegistrationException
,

MBeanException
,

NotCompliantMBeanException
,

InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, ObjectName, Object[], String[])

. The

Object[]

parameter is wrapped in a

MarshalledObject

.

**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** loaderName

- The object name of the class loader to be used.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked, encapsulated into a

MarshalledObject

. The encapsulated array can be
null, equivalent to an empty array.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked. Can be null, equivalent to an empty
array.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
instantiated MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or a

java.lang.Exception

that occurred when trying to
invoke the MBean's constructor.
**Throws:** InstanceAlreadyExistsException

- The MBean is already
under the control of the MBean server.
**Throws:** MBeanRegistrationException

- The

preRegister

(

MBeanRegistration

interface) method of the MBean has thrown an exception. The
MBean will not be registered.
**Throws:** MBeanException

- The constructor of the MBean has
thrown an exception.
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean.
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null, the

ObjectName

passed
in parameter contains a pattern, or no

ObjectName

is specified for the MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- unregisterMBean

```java
void unregisterMBean​(
ObjectName
name,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

MBeanRegistrationException
,

IOException
```

Handles the method

MBeanServerConnection.unregisterMBean(ObjectName)

.

**Parameters:** name

- The object name of the MBean to be unregistered.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** MBeanRegistrationException

- The preDeregister
((

MBeanRegistration

interface) method of the MBean
has thrown an exception.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the MBean you are when trying to
unregister is the

MBeanServerDelegate

MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- getObjectInstance

```java
ObjectInstance
getObjectInstance​(
ObjectName
name,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.getObjectInstance(ObjectName)

.

**Parameters:** name

- The object name of the MBean.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** The

ObjectInstance

associated with the MBean
specified by

name

. The contained

ObjectName

is

name

and the contained class name is

getMBeanInfo(name)

.getClassName()

.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- queryMBeans

```java
Set
<
ObjectInstance
> queryMBeans​(
ObjectName
name,

MarshalledObject
query,

Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.queryMBeans(ObjectName,
QueryExp)

. The

QueryExp

is wrapped in a

MarshalledObject

.

**Parameters:** name

- The object name pattern identifying the MBeans to
be retrieved. If null or no domain and key properties are
specified, all the MBeans registered will be retrieved.
**Parameters:** query

- The query expression to be applied for selecting
MBeans, encapsulated into a

MarshalledObject

. If
the

MarshalledObject

encapsulates a null value no
query expression will be applied for selecting MBeans.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** A set containing the

ObjectInstance

objects for the selected MBeans. If no MBean satisfies the
query an empty list is returned.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- queryNames

```java
Set
<
ObjectName
> queryNames​(
ObjectName
name,

MarshalledObject
query,

Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.queryNames(ObjectName,
QueryExp)

. The

QueryExp

is wrapped in a

MarshalledObject

.

**Parameters:** name

- The object name pattern identifying the MBean names
to be retrieved. If null or no domain and key properties are
specified, the name of all registered MBeans will be retrieved.
**Parameters:** query

- The query expression to be applied for selecting
MBeans, encapsulated into a

MarshalledObject

. If
the

MarshalledObject

encapsulates a null value no
query expression will be applied for selecting MBeans.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** A set containing the ObjectNames for the MBeans
selected. If no MBean satisfies the query, an empty list is
returned.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- isRegistered

```java
boolean isRegistered​(
ObjectName
name,

Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.isRegistered(ObjectName)

.

**Parameters:** name

- The object name of the MBean to be checked.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** True if the MBean is already registered in the MBean
server, false otherwise.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- getMBeanCount

```java
Integer
getMBeanCount​(
Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.getMBeanCount()

.

**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** the number of MBeans registered.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- getAttribute

```java
Object
getAttribute​(
ObjectName
name,

String
attribute,

Subject
delegationSubject)
throws
MBeanException
,

AttributeNotFoundException
,

InstanceNotFoundException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.getAttribute(ObjectName,
String)

.

**Parameters:** name

- The object name of the MBean from which the
attribute is to be retrieved.
**Parameters:** attribute

- A String specifying the name of the attribute
to be retrieved.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** The value of the retrieved attribute.
**Throws:** AttributeNotFoundException

- The attribute specified
is not accessible in the MBean.
**Throws:** MBeanException

- Wraps an exception thrown by the
MBean's getter.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown when trying to invoke
the getter.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the attribute in parameter is
null.
**Throws:** RuntimeMBeanException

- Wraps a runtime exception thrown
by the MBean's getter.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** setAttribute(javax.management.ObjectName, java.rmi.MarshalledObject, javax.security.auth.Subject)

- getAttributes

```java
AttributeList
getAttributes​(
ObjectName
name,

String
[] attributes,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.getAttributes(ObjectName,
String[])

.

**Parameters:** name

- The object name of the MBean from which the
attributes are retrieved.
**Parameters:** attributes

- A list of the attributes to be retrieved.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** The list of the retrieved attributes.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- An exception occurred when
trying to invoke the getAttributes method of a Dynamic MBean.
**Throws:** RuntimeOperationsException

- Wrap a

java.lang.IllegalArgumentException

: The object
name in parameter is null or attributes in parameter is null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** setAttributes(javax.management.ObjectName, java.rmi.MarshalledObject, javax.security.auth.Subject)

- setAttribute

```java
void setAttribute​(
ObjectName
name,

MarshalledObject
attribute,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

AttributeNotFoundException
,

InvalidAttributeValueException
,

MBeanException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.setAttribute(ObjectName,
Attribute)

. The

Attribute

parameter is wrapped
in a

MarshalledObject

.

**Parameters:** name

- The name of the MBean within which the attribute is
to be set.
**Parameters:** attribute

- The identification of the attribute to be set
and the value it is to be set to, encapsulated into a

MarshalledObject

.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** AttributeNotFoundException

- The attribute specified
is not accessible in the MBean.
**Throws:** InvalidAttributeValueException

- The value specified
for the attribute is not valid.
**Throws:** MBeanException

- Wraps an exception thrown by the
MBean's setter.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown when trying to invoke
the setter.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the attribute in parameter is
null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** getAttribute(javax.management.ObjectName, java.lang.String, javax.security.auth.Subject)

- setAttributes

```java
AttributeList
setAttributes​(
ObjectName
name,

MarshalledObject
attributes,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.setAttributes(ObjectName,
AttributeList)

. The

AttributeList

parameter is
wrapped in a

MarshalledObject

.

**Parameters:** name

- The object name of the MBean within which the
attributes are to be set.
**Parameters:** attributes

- A list of attributes: The identification of
the attributes to be set and the values they are to be set to,
encapsulated into a

MarshalledObject

.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** The list of attributes that were set, with their new
values.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- An exception occurred when
trying to invoke the getAttributes method of a Dynamic MBean.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or attributes in parameter is null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** getAttributes(javax.management.ObjectName, java.lang.String[], javax.security.auth.Subject)

- invoke

```java
Object
invoke​(
ObjectName
name,

String
operationName,

MarshalledObject
params,

String
[] signature,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

MBeanException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.invoke(ObjectName,
String, Object[], String[])

. The

Object[]

parameter is wrapped in a

MarshalledObject

.

**Parameters:** name

- The object name of the MBean on which the method is
to be invoked.
**Parameters:** operationName

- The name of the operation to be invoked.
**Parameters:** params

- An array containing the parameters to be set when
the operation is invoked, encapsulated into a

MarshalledObject

. The encapsulated array can be
null, equivalent to an empty array.
**Parameters:** signature

- An array containing the signature of the
operation. The class objects will be loaded using the same
class loader as the one used for loading the MBean on which the
operation was invoked. Can be null, equivalent to an empty
array.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** The object returned by the operation, which represents
the result of invoking the operation on the MBean specified.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** MBeanException

- Wraps an exception thrown by the
MBean's invoked method.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown while trying to invoke
the method.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

when

name

or

operationName

is null.

- getDefaultDomain

```java
String
getDefaultDomain​(
Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.getDefaultDomain()

.

**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** the default domain.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- getDomains

```java
String
[] getDomains​(
Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.getDomains()

.

**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** the list of domains.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

- getMBeanInfo

```java
MBeanInfo
getMBeanInfo​(
ObjectName
name,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

IntrospectionException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.getMBeanInfo(ObjectName)

.

**Parameters:** name

- The name of the MBean to analyze
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** An instance of

MBeanInfo

allowing the
retrieval of all attributes and operations of this MBean.
**Throws:** IntrospectionException

- An exception occurred during
introspection.
**Throws:** InstanceNotFoundException

- The MBean specified was
not found.
**Throws:** ReflectionException

- An exception occurred when
trying to invoke the getMBeanInfo of a Dynamic MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.

- isInstanceOf

```java
boolean isInstanceOf​(
ObjectName
name,

String
className,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.isInstanceOf(ObjectName,
String)

.

**Parameters:** name

- The

ObjectName

of the MBean.
**Parameters:** className

- The name of the class.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** true if the MBean specified is an instance of the
specified class according to the rules above, false otherwise.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.

- addNotificationListener

```java
void addNotificationListener​(
ObjectName
name,

ObjectName
listener,

MarshalledObject
filter,

MarshalledObject
handback,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.addNotificationListener(ObjectName,
ObjectName, NotificationFilter, Object)

. The

NotificationFilter

parameter is wrapped in a

MarshalledObject

. The

Object

(handback) parameter is also wrapped in a

MarshalledObject

.

**Parameters:** name

- The name of the MBean on which the listener should
be added.
**Parameters:** listener

- The object name of the listener which will
handle the notifications emitted by the registered MBean.
**Parameters:** filter

- The filter object, encapsulated into a

MarshalledObject

. If filter encapsulated in the

MarshalledObject

has a null value, no filtering
will be performed before handling notifications.
**Parameters:** handback

- The context to be sent to the listener when a
notification is emitted, encapsulated into a

MarshalledObject

.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- The MBean name of the
notification listener or of the notification broadcaster does
not match any of the registered MBeans.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

. The MBean named by

listener

exists but does not implement the

NotificationListener

interface,
or

name

or

listener

is null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** removeNotificationListener(ObjectName, ObjectName, Subject)

,

removeNotificationListener(ObjectName, ObjectName,
MarshalledObject, MarshalledObject, Subject)

- removeNotificationListener

```java
void removeNotificationListener​(
ObjectName
name,

ObjectName
listener,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ListenerNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.removeNotificationListener(ObjectName,
ObjectName)

.

**Parameters:** name

- The name of the MBean on which the listener should
be removed.
**Parameters:** listener

- The object name of the listener to be removed.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- The MBean name provided
does not match any of the registered MBeans.
**Throws:** ListenerNotFoundException

- The listener is not
registered in the MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

when

name

or

listener

is null.
**See Also:** addNotificationListener(javax.management.ObjectName, javax.management.ObjectName, java.rmi.MarshalledObject, java.rmi.MarshalledObject, javax.security.auth.Subject)

- removeNotificationListener

```java
void removeNotificationListener​(
ObjectName
name,

ObjectName
listener,

MarshalledObject
filter,

MarshalledObject
handback,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ListenerNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.removeNotificationListener(ObjectName,
ObjectName, NotificationFilter, Object)

. The

NotificationFilter

parameter is wrapped in a

MarshalledObject

. The

Object

parameter is also wrapped in a

MarshalledObject

.

**Parameters:** name

- The name of the MBean on which the listener should
be removed.
**Parameters:** listener

- A listener that was previously added to this
MBean.
**Parameters:** filter

- The filter that was specified when the listener
was added, encapsulated into a

MarshalledObject

.
**Parameters:** handback

- The handback that was specified when the
listener was added, encapsulated into a

MarshalledObject

.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- The MBean name provided
does not match any of the registered MBeans.
**Throws:** ListenerNotFoundException

- The listener is not
registered in the MBean, or it is not registered with the given
filter and handback.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

when

name

or

listener

is null.
**See Also:** addNotificationListener(javax.management.ObjectName, javax.management.ObjectName, java.rmi.MarshalledObject, java.rmi.MarshalledObject, javax.security.auth.Subject)

- addNotificationListeners

```java
Integer
[] addNotificationListeners​(
ObjectName
[] names,

MarshalledObject
[] filters,

Subject
[] delegationSubjects)
throws
InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

.

Register for notifications from the given MBeans that match
the given filters. The remote client can subsequently retrieve
the notifications using the

fetchNotifications

method.

For each listener, the original

NotificationListener

and

handback

are
kept on the client side; in order for the client to be able to
identify them, the server generates and returns a unique

listenerID

. This

listenerID

is
forwarded with the

Notifications

to the remote
client.

If any one of the given (name, filter) pairs cannot be
registered, then the operation fails with an exception, and no
names or filters are registered.

**Parameters:** names

- the

ObjectNames

identifying the
MBeans emitting the Notifications.
**Parameters:** filters

- an array of marshalled representations of the

NotificationFilters

. Elements of this array can
be null.
**Parameters:** delegationSubjects

- the

Subjects

on behalf
of which the listeners are being added. Elements of this array
can be null. Also, the

delegationSubjects

parameter itself can be null, which is equivalent to an array
of null values with the same size as the

names

and

filters

arrays.
**Returns:** an array of

listenerIDs

identifying the
local listeners. This array has the same number of elements as
the parameters.
**Throws:** IllegalArgumentException

- if

names

or

filters

is null, or if

names

contains
a null element, or if the three arrays do not all have the same
size.
**Throws:** ClassCastException

- if one of the elements of

filters

unmarshalls as a non-null object that is
not a

NotificationFilter

.
**Throws:** InstanceNotFoundException

- if one of the

names

does not correspond to any registered MBean.
**Throws:** SecurityException

- if, for one of the MBeans, the
client, or the delegated Subject if any, does not have
permission to add a listener.
**Throws:** IOException

- if a general communication exception occurred.

- removeNotificationListeners

```java
void removeNotificationListeners​(
ObjectName
name,

Integer
[] listenerIDs,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ListenerNotFoundException
,

IOException
```

Handles the

removeNotificationListener(ObjectName, NotificationListener)

and

removeNotificationListener(ObjectName, NotificationListener, NotificationFilter, Object)

methods.

This method removes one or more

NotificationListener

s from a given MBean in the
MBean server.

The

NotificationListeners

are identified by the
IDs which were returned by the

addNotificationListeners(ObjectName[], MarshalledObject[],
Subject[])

method.

**Parameters:** name

- the

ObjectName

identifying the MBean
emitting the Notifications.
**Parameters:** listenerIDs

- the list of the IDs corresponding to the
listeners to remove.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- if the given

name

does not correspond to any registered MBean.
**Throws:** ListenerNotFoundException

- if one of the listeners was
not found on the server side. This exception can happen if the
MBean discarded a listener for some reason other than a call to

MBeanServer.removeNotificationListener

.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to remove the listeners.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** IllegalArgumentException

- if

ObjectName

or

listenerIds

is null or if

listenerIds

contains a null element.

- fetchNotifications

```java
NotificationResult
fetchNotifications​(long clientSequenceNumber,
int maxNotifications,
long timeout)
throws
IOException
```

Retrieves notifications from the connector server. This
method can block until there is at least one notification or
until the specified timeout is reached. The method can also
return at any time with zero notifications.

A notification can be included in the result if its sequence
number is no less than

clientSequenceNumber

and
this client has registered at least one listener for the MBean
generating the notification, with a filter that accepts the
notification. Each listener that is interested in the
notification is identified by an Integer ID that was returned
by

addNotificationListeners(ObjectName[],
MarshalledObject[], Subject[])

.

**Parameters:** clientSequenceNumber

- the first sequence number that the
client is interested in. If negative, it is interpreted as
meaning the sequence number that the next notification will
have.
**Parameters:** maxNotifications

- the maximum number of different
notifications to return. The

TargetedNotification

array in the returned

NotificationResult

can have
more elements than this if the same notification appears more
than once. The behavior is unspecified if this parameter is
negative.
**Parameters:** timeout

- the maximum time in milliseconds to wait for a
notification to arrive. This can be 0 to indicate that the
method should not wait if there are no notifications, but
should return at once. It can be

Long.MAX_VALUE

to indicate that there is no timeout. The behavior is
unspecified if this parameter is negative.
**Returns:** A

NotificationResult

.
**Throws:** IOException

- if a general communication exception occurred.

---

#### Method Detail

getConnectionId

```java
String
getConnectionId()
throws
IOException
```

Returns the connection ID. This string is different for
every open connection to a given RMI connector server.

**Returns:** the connection ID
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** RMIConnector.connect

---

#### getConnectionId

String

getConnectionId()
throws

IOException

Returns the connection ID. This string is different for
every open connection to a given RMI connector server.

close

```java
void close()
throws
IOException
```

Closes this connection. On return from this method, the RMI
object implementing this interface is unexported, so further
remote calls to it will fail.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if the connection could not be closed,
or the Remote object could not be unexported, or there was a
communication failure when transmitting the remote close
request.

---

#### close

void close()
throws

IOException

Closes this connection. On return from this method, the RMI
object implementing this interface is unexported, so further
remote calls to it will fail.

createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name,

Subject
delegationSubject)
throws
ReflectionException
,

InstanceAlreadyExistsException
,

MBeanRegistrationException
,

MBeanException
,

NotCompliantMBeanException
,

IOException
```

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName)

.

**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
instantiated MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or a

java.lang.Exception

that occurred
when trying to invoke the MBean's constructor.
**Throws:** InstanceAlreadyExistsException

- The MBean is already
under the control of the MBean server.
**Throws:** MBeanRegistrationException

- The

preRegister

(

MBeanRegistration

interface) method of the MBean has thrown an exception. The
MBean will not be registered.
**Throws:** MBeanException

- The constructor of the MBean has
thrown an exception.
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null, the

ObjectName

passed
in parameter contains a pattern or no

ObjectName

is specified for the MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

---

#### createMBean

ObjectInstance

createMBean​(

String

className,

ObjectName

name,

Subject

delegationSubject)
throws

ReflectionException

,

InstanceAlreadyExistsException

,

MBeanRegistrationException

,

MBeanException

,

NotCompliantMBeanException

,

IOException

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName)

.

createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name,

ObjectName
loaderName,

Subject
delegationSubject)
throws
ReflectionException
,

InstanceAlreadyExistsException
,

MBeanRegistrationException
,

MBeanException
,

NotCompliantMBeanException
,

InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, ObjectName)

.

**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** loaderName

- The object name of the class loader to be used.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
instantiated MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or a

java.lang.Exception

that occurred when trying to
invoke the MBean's constructor.
**Throws:** InstanceAlreadyExistsException

- The MBean is already
under the control of the MBean server.
**Throws:** MBeanRegistrationException

- The

preRegister

(

MBeanRegistration

interface) method of the MBean has thrown an exception. The
MBean will not be registered.
**Throws:** MBeanException

- The constructor of the MBean has
thrown an exception.
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean.
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null, the

ObjectName

passed
in parameter contains a pattern or no

ObjectName

is specified for the MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

---

#### createMBean

ObjectInstance

createMBean​(

String

className,

ObjectName

name,

ObjectName

loaderName,

Subject

delegationSubject)
throws

ReflectionException

,

InstanceAlreadyExistsException

,

MBeanRegistrationException

,

MBeanException

,

NotCompliantMBeanException

,

InstanceNotFoundException

,

IOException

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, ObjectName)

.

createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name,

MarshalledObject
params,

String
[] signature,

Subject
delegationSubject)
throws
ReflectionException
,

InstanceAlreadyExistsException
,

MBeanRegistrationException
,

MBeanException
,

NotCompliantMBeanException
,

IOException
```

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, Object[], String[])

. The

Object[]

parameter is wrapped in a

MarshalledObject

.

**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked, encapsulated into a

MarshalledObject

. The encapsulated array can be
null, equivalent to an empty array.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked. Can be null, equivalent to an empty
array.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
instantiated MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or a

java.lang.Exception

that occurred when trying to
invoke the MBean's constructor.
**Throws:** InstanceAlreadyExistsException

- The MBean is already
under the control of the MBean server.
**Throws:** MBeanRegistrationException

- The

preRegister

(

MBeanRegistration

interface) method of the MBean has thrown an exception. The
MBean will not be registered.
**Throws:** MBeanException

- The constructor of the MBean has
thrown an exception.
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null, the

ObjectName

passed
in parameter contains a pattern, or no

ObjectName

is specified for the MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

---

#### createMBean

ObjectInstance

createMBean​(

String

className,

ObjectName

name,

MarshalledObject

params,

String

[] signature,

Subject

delegationSubject)
throws

ReflectionException

,

InstanceAlreadyExistsException

,

MBeanRegistrationException

,

MBeanException

,

NotCompliantMBeanException

,

IOException

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, Object[], String[])

. The

Object[]

parameter is wrapped in a

MarshalledObject

.

createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name,

ObjectName
loaderName,

MarshalledObject
params,

String
[] signature,

Subject
delegationSubject)
throws
ReflectionException
,

InstanceAlreadyExistsException
,

MBeanRegistrationException
,

MBeanException
,

NotCompliantMBeanException
,

InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, ObjectName, Object[], String[])

. The

Object[]

parameter is wrapped in a

MarshalledObject

.

**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** loaderName

- The object name of the class loader to be used.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked, encapsulated into a

MarshalledObject

. The encapsulated array can be
null, equivalent to an empty array.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked. Can be null, equivalent to an empty
array.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
instantiated MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or a

java.lang.Exception

that occurred when trying to
invoke the MBean's constructor.
**Throws:** InstanceAlreadyExistsException

- The MBean is already
under the control of the MBean server.
**Throws:** MBeanRegistrationException

- The

preRegister

(

MBeanRegistration

interface) method of the MBean has thrown an exception. The
MBean will not be registered.
**Throws:** MBeanException

- The constructor of the MBean has
thrown an exception.
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean.
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null, the

ObjectName

passed
in parameter contains a pattern, or no

ObjectName

is specified for the MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

---

#### createMBean

ObjectInstance

createMBean​(

String

className,

ObjectName

name,

ObjectName

loaderName,

MarshalledObject

params,

String

[] signature,

Subject

delegationSubject)
throws

ReflectionException

,

InstanceAlreadyExistsException

,

MBeanRegistrationException

,

MBeanException

,

NotCompliantMBeanException

,

InstanceNotFoundException

,

IOException

Handles the method

MBeanServerConnection.createMBean(String,
ObjectName, ObjectName, Object[], String[])

. The

Object[]

parameter is wrapped in a

MarshalledObject

.

unregisterMBean

```java
void unregisterMBean​(
ObjectName
name,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

MBeanRegistrationException
,

IOException
```

Handles the method

MBeanServerConnection.unregisterMBean(ObjectName)

.

**Parameters:** name

- The object name of the MBean to be unregistered.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** MBeanRegistrationException

- The preDeregister
((

MBeanRegistration

interface) method of the MBean
has thrown an exception.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the MBean you are when trying to
unregister is the

MBeanServerDelegate

MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

---

#### unregisterMBean

void unregisterMBean​(

ObjectName

name,

Subject

delegationSubject)
throws

InstanceNotFoundException

,

MBeanRegistrationException

,

IOException

Handles the method

MBeanServerConnection.unregisterMBean(ObjectName)

.

getObjectInstance

```java
ObjectInstance
getObjectInstance​(
ObjectName
name,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.getObjectInstance(ObjectName)

.

**Parameters:** name

- The object name of the MBean.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** The

ObjectInstance

associated with the MBean
specified by

name

. The contained

ObjectName

is

name

and the contained class name is

getMBeanInfo(name)

.getClassName()

.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

---

#### getObjectInstance

ObjectInstance

getObjectInstance​(

ObjectName

name,

Subject

delegationSubject)
throws

InstanceNotFoundException

,

IOException

Handles the method

MBeanServerConnection.getObjectInstance(ObjectName)

.

queryMBeans

```java
Set
<
ObjectInstance
> queryMBeans​(
ObjectName
name,

MarshalledObject
query,

Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.queryMBeans(ObjectName,
QueryExp)

. The

QueryExp

is wrapped in a

MarshalledObject

.

**Parameters:** name

- The object name pattern identifying the MBeans to
be retrieved. If null or no domain and key properties are
specified, all the MBeans registered will be retrieved.
**Parameters:** query

- The query expression to be applied for selecting
MBeans, encapsulated into a

MarshalledObject

. If
the

MarshalledObject

encapsulates a null value no
query expression will be applied for selecting MBeans.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** A set containing the

ObjectInstance

objects for the selected MBeans. If no MBean satisfies the
query an empty list is returned.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

---

#### queryMBeans

Set

<

ObjectInstance

> queryMBeans​(

ObjectName

name,

MarshalledObject

query,

Subject

delegationSubject)
throws

IOException

Handles the method

MBeanServerConnection.queryMBeans(ObjectName,
QueryExp)

. The

QueryExp

is wrapped in a

MarshalledObject

.

queryNames

```java
Set
<
ObjectName
> queryNames​(
ObjectName
name,

MarshalledObject
query,

Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.queryNames(ObjectName,
QueryExp)

. The

QueryExp

is wrapped in a

MarshalledObject

.

**Parameters:** name

- The object name pattern identifying the MBean names
to be retrieved. If null or no domain and key properties are
specified, the name of all registered MBeans will be retrieved.
**Parameters:** query

- The query expression to be applied for selecting
MBeans, encapsulated into a

MarshalledObject

. If
the

MarshalledObject

encapsulates a null value no
query expression will be applied for selecting MBeans.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** A set containing the ObjectNames for the MBeans
selected. If no MBean satisfies the query, an empty list is
returned.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

---

#### queryNames

Set

<

ObjectName

> queryNames​(

ObjectName

name,

MarshalledObject

query,

Subject

delegationSubject)
throws

IOException

Handles the method

MBeanServerConnection.queryNames(ObjectName,
QueryExp)

. The

QueryExp

is wrapped in a

MarshalledObject

.

isRegistered

```java
boolean isRegistered​(
ObjectName
name,

Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.isRegistered(ObjectName)

.

**Parameters:** name

- The object name of the MBean to be checked.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** True if the MBean is already registered in the MBean
server, false otherwise.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

---

#### isRegistered

boolean isRegistered​(

ObjectName

name,

Subject

delegationSubject)
throws

IOException

Handles the method

MBeanServerConnection.isRegistered(ObjectName)

.

getMBeanCount

```java
Integer
getMBeanCount​(
Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.getMBeanCount()

.

**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** the number of MBeans registered.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

---

#### getMBeanCount

Integer

getMBeanCount​(

Subject

delegationSubject)
throws

IOException

Handles the method

MBeanServerConnection.getMBeanCount()

.

getAttribute

```java
Object
getAttribute​(
ObjectName
name,

String
attribute,

Subject
delegationSubject)
throws
MBeanException
,

AttributeNotFoundException
,

InstanceNotFoundException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.getAttribute(ObjectName,
String)

.

**Parameters:** name

- The object name of the MBean from which the
attribute is to be retrieved.
**Parameters:** attribute

- A String specifying the name of the attribute
to be retrieved.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** The value of the retrieved attribute.
**Throws:** AttributeNotFoundException

- The attribute specified
is not accessible in the MBean.
**Throws:** MBeanException

- Wraps an exception thrown by the
MBean's getter.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown when trying to invoke
the getter.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the attribute in parameter is
null.
**Throws:** RuntimeMBeanException

- Wraps a runtime exception thrown
by the MBean's getter.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** setAttribute(javax.management.ObjectName, java.rmi.MarshalledObject, javax.security.auth.Subject)

---

#### getAttribute

Object

getAttribute​(

ObjectName

name,

String

attribute,

Subject

delegationSubject)
throws

MBeanException

,

AttributeNotFoundException

,

InstanceNotFoundException

,

ReflectionException

,

IOException

Handles the method

MBeanServerConnection.getAttribute(ObjectName,
String)

.

getAttributes

```java
AttributeList
getAttributes​(
ObjectName
name,

String
[] attributes,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.getAttributes(ObjectName,
String[])

.

**Parameters:** name

- The object name of the MBean from which the
attributes are retrieved.
**Parameters:** attributes

- A list of the attributes to be retrieved.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** The list of the retrieved attributes.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- An exception occurred when
trying to invoke the getAttributes method of a Dynamic MBean.
**Throws:** RuntimeOperationsException

- Wrap a

java.lang.IllegalArgumentException

: The object
name in parameter is null or attributes in parameter is null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** setAttributes(javax.management.ObjectName, java.rmi.MarshalledObject, javax.security.auth.Subject)

---

#### getAttributes

AttributeList

getAttributes​(

ObjectName

name,

String

[] attributes,

Subject

delegationSubject)
throws

InstanceNotFoundException

,

ReflectionException

,

IOException

Handles the method

MBeanServerConnection.getAttributes(ObjectName,
String[])

.

setAttribute

```java
void setAttribute​(
ObjectName
name,

MarshalledObject
attribute,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

AttributeNotFoundException
,

InvalidAttributeValueException
,

MBeanException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.setAttribute(ObjectName,
Attribute)

. The

Attribute

parameter is wrapped
in a

MarshalledObject

.

**Parameters:** name

- The name of the MBean within which the attribute is
to be set.
**Parameters:** attribute

- The identification of the attribute to be set
and the value it is to be set to, encapsulated into a

MarshalledObject

.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** AttributeNotFoundException

- The attribute specified
is not accessible in the MBean.
**Throws:** InvalidAttributeValueException

- The value specified
for the attribute is not valid.
**Throws:** MBeanException

- Wraps an exception thrown by the
MBean's setter.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown when trying to invoke
the setter.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the attribute in parameter is
null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** getAttribute(javax.management.ObjectName, java.lang.String, javax.security.auth.Subject)

---

#### setAttribute

void setAttribute​(

ObjectName

name,

MarshalledObject

attribute,

Subject

delegationSubject)
throws

InstanceNotFoundException

,

AttributeNotFoundException

,

InvalidAttributeValueException

,

MBeanException

,

ReflectionException

,

IOException

Handles the method

MBeanServerConnection.setAttribute(ObjectName,
Attribute)

. The

Attribute

parameter is wrapped
in a

MarshalledObject

.

setAttributes

```java
AttributeList
setAttributes​(
ObjectName
name,

MarshalledObject
attributes,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.setAttributes(ObjectName,
AttributeList)

. The

AttributeList

parameter is
wrapped in a

MarshalledObject

.

**Parameters:** name

- The object name of the MBean within which the
attributes are to be set.
**Parameters:** attributes

- A list of attributes: The identification of
the attributes to be set and the values they are to be set to,
encapsulated into a

MarshalledObject

.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** The list of attributes that were set, with their new
values.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- An exception occurred when
trying to invoke the getAttributes method of a Dynamic MBean.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or attributes in parameter is null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** getAttributes(javax.management.ObjectName, java.lang.String[], javax.security.auth.Subject)

---

#### setAttributes

AttributeList

setAttributes​(

ObjectName

name,

MarshalledObject

attributes,

Subject

delegationSubject)
throws

InstanceNotFoundException

,

ReflectionException

,

IOException

Handles the method

MBeanServerConnection.setAttributes(ObjectName,
AttributeList)

. The

AttributeList

parameter is
wrapped in a

MarshalledObject

.

invoke

```java
Object
invoke​(
ObjectName
name,

String
operationName,

MarshalledObject
params,

String
[] signature,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

MBeanException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.invoke(ObjectName,
String, Object[], String[])

. The

Object[]

parameter is wrapped in a

MarshalledObject

.

**Parameters:** name

- The object name of the MBean on which the method is
to be invoked.
**Parameters:** operationName

- The name of the operation to be invoked.
**Parameters:** params

- An array containing the parameters to be set when
the operation is invoked, encapsulated into a

MarshalledObject

. The encapsulated array can be
null, equivalent to an empty array.
**Parameters:** signature

- An array containing the signature of the
operation. The class objects will be loaded using the same
class loader as the one used for loading the MBean on which the
operation was invoked. Can be null, equivalent to an empty
array.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** The object returned by the operation, which represents
the result of invoking the operation on the MBean specified.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** MBeanException

- Wraps an exception thrown by the
MBean's invoked method.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown while trying to invoke
the method.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

when

name

or

operationName

is null.

---

#### invoke

Object

invoke​(

ObjectName

name,

String

operationName,

MarshalledObject

params,

String

[] signature,

Subject

delegationSubject)
throws

InstanceNotFoundException

,

MBeanException

,

ReflectionException

,

IOException

Handles the method

MBeanServerConnection.invoke(ObjectName,
String, Object[], String[])

. The

Object[]

parameter is wrapped in a

MarshalledObject

.

getDefaultDomain

```java
String
getDefaultDomain​(
Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.getDefaultDomain()

.

**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** the default domain.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

---

#### getDefaultDomain

String

getDefaultDomain​(

Subject

delegationSubject)
throws

IOException

Handles the method

MBeanServerConnection.getDefaultDomain()

.

getDomains

```java
String
[] getDomains​(
Subject
delegationSubject)
throws
IOException
```

Handles the method

MBeanServerConnection.getDomains()

.

**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** the list of domains.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.

---

#### getDomains

String

[] getDomains​(

Subject

delegationSubject)
throws

IOException

Handles the method

MBeanServerConnection.getDomains()

.

getMBeanInfo

```java
MBeanInfo
getMBeanInfo​(
ObjectName
name,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

IntrospectionException
,

ReflectionException
,

IOException
```

Handles the method

MBeanServerConnection.getMBeanInfo(ObjectName)

.

**Parameters:** name

- The name of the MBean to analyze
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** An instance of

MBeanInfo

allowing the
retrieval of all attributes and operations of this MBean.
**Throws:** IntrospectionException

- An exception occurred during
introspection.
**Throws:** InstanceNotFoundException

- The MBean specified was
not found.
**Throws:** ReflectionException

- An exception occurred when
trying to invoke the getMBeanInfo of a Dynamic MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.

---

#### getMBeanInfo

MBeanInfo

getMBeanInfo​(

ObjectName

name,

Subject

delegationSubject)
throws

InstanceNotFoundException

,

IntrospectionException

,

ReflectionException

,

IOException

Handles the method

MBeanServerConnection.getMBeanInfo(ObjectName)

.

isInstanceOf

```java
boolean isInstanceOf​(
ObjectName
name,

String
className,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.isInstanceOf(ObjectName,
String)

.

**Parameters:** name

- The

ObjectName

of the MBean.
**Parameters:** className

- The name of the class.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Returns:** true if the MBean specified is an instance of the
specified class according to the rules above, false otherwise.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.

---

#### isInstanceOf

boolean isInstanceOf​(

ObjectName

name,

String

className,

Subject

delegationSubject)
throws

InstanceNotFoundException

,

IOException

Handles the method

MBeanServerConnection.isInstanceOf(ObjectName,
String)

.

addNotificationListener

```java
void addNotificationListener​(
ObjectName
name,

ObjectName
listener,

MarshalledObject
filter,

MarshalledObject
handback,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.addNotificationListener(ObjectName,
ObjectName, NotificationFilter, Object)

. The

NotificationFilter

parameter is wrapped in a

MarshalledObject

. The

Object

(handback) parameter is also wrapped in a

MarshalledObject

.

**Parameters:** name

- The name of the MBean on which the listener should
be added.
**Parameters:** listener

- The object name of the listener which will
handle the notifications emitted by the registered MBean.
**Parameters:** filter

- The filter object, encapsulated into a

MarshalledObject

. If filter encapsulated in the

MarshalledObject

has a null value, no filtering
will be performed before handling notifications.
**Parameters:** handback

- The context to be sent to the listener when a
notification is emitted, encapsulated into a

MarshalledObject

.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- The MBean name of the
notification listener or of the notification broadcaster does
not match any of the registered MBeans.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

. The MBean named by

listener

exists but does not implement the

NotificationListener

interface,
or

name

or

listener

is null.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**See Also:** removeNotificationListener(ObjectName, ObjectName, Subject)

,

removeNotificationListener(ObjectName, ObjectName,
MarshalledObject, MarshalledObject, Subject)

---

#### addNotificationListener

void addNotificationListener​(

ObjectName

name,

ObjectName

listener,

MarshalledObject

filter,

MarshalledObject

handback,

Subject

delegationSubject)
throws

InstanceNotFoundException

,

IOException

Handles the method

MBeanServerConnection.addNotificationListener(ObjectName,
ObjectName, NotificationFilter, Object)

. The

NotificationFilter

parameter is wrapped in a

MarshalledObject

. The

Object

(handback) parameter is also wrapped in a

MarshalledObject

.

removeNotificationListener

```java
void removeNotificationListener​(
ObjectName
name,

ObjectName
listener,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ListenerNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.removeNotificationListener(ObjectName,
ObjectName)

.

**Parameters:** name

- The name of the MBean on which the listener should
be removed.
**Parameters:** listener

- The object name of the listener to be removed.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- The MBean name provided
does not match any of the registered MBeans.
**Throws:** ListenerNotFoundException

- The listener is not
registered in the MBean.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

when

name

or

listener

is null.
**See Also:** addNotificationListener(javax.management.ObjectName, javax.management.ObjectName, java.rmi.MarshalledObject, java.rmi.MarshalledObject, javax.security.auth.Subject)

---

#### removeNotificationListener

void removeNotificationListener​(

ObjectName

name,

ObjectName

listener,

Subject

delegationSubject)
throws

InstanceNotFoundException

,

ListenerNotFoundException

,

IOException

Handles the method

MBeanServerConnection.removeNotificationListener(ObjectName,
ObjectName)

.

removeNotificationListener

```java
void removeNotificationListener​(
ObjectName
name,

ObjectName
listener,

MarshalledObject
filter,

MarshalledObject
handback,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ListenerNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.removeNotificationListener(ObjectName,
ObjectName, NotificationFilter, Object)

. The

NotificationFilter

parameter is wrapped in a

MarshalledObject

. The

Object

parameter is also wrapped in a

MarshalledObject

.

**Parameters:** name

- The name of the MBean on which the listener should
be removed.
**Parameters:** listener

- A listener that was previously added to this
MBean.
**Parameters:** filter

- The filter that was specified when the listener
was added, encapsulated into a

MarshalledObject

.
**Parameters:** handback

- The handback that was specified when the
listener was added, encapsulated into a

MarshalledObject

.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- The MBean name provided
does not match any of the registered MBeans.
**Throws:** ListenerNotFoundException

- The listener is not
registered in the MBean, or it is not registered with the given
filter and handback.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to perform this operation.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

when

name

or

listener

is null.
**See Also:** addNotificationListener(javax.management.ObjectName, javax.management.ObjectName, java.rmi.MarshalledObject, java.rmi.MarshalledObject, javax.security.auth.Subject)

---

#### removeNotificationListener

void removeNotificationListener​(

ObjectName

name,

ObjectName

listener,

MarshalledObject

filter,

MarshalledObject

handback,

Subject

delegationSubject)
throws

InstanceNotFoundException

,

ListenerNotFoundException

,

IOException

Handles the method

MBeanServerConnection.removeNotificationListener(ObjectName,
ObjectName, NotificationFilter, Object)

. The

NotificationFilter

parameter is wrapped in a

MarshalledObject

. The

Object

parameter is also wrapped in a

MarshalledObject

.

addNotificationListeners

```java
Integer
[] addNotificationListeners​(
ObjectName
[] names,

MarshalledObject
[] filters,

Subject
[] delegationSubjects)
throws
InstanceNotFoundException
,

IOException
```

Handles the method

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

.

Register for notifications from the given MBeans that match
the given filters. The remote client can subsequently retrieve
the notifications using the

fetchNotifications

method.

For each listener, the original

NotificationListener

and

handback

are
kept on the client side; in order for the client to be able to
identify them, the server generates and returns a unique

listenerID

. This

listenerID

is
forwarded with the

Notifications

to the remote
client.

If any one of the given (name, filter) pairs cannot be
registered, then the operation fails with an exception, and no
names or filters are registered.

**Parameters:** names

- the

ObjectNames

identifying the
MBeans emitting the Notifications.
**Parameters:** filters

- an array of marshalled representations of the

NotificationFilters

. Elements of this array can
be null.
**Parameters:** delegationSubjects

- the

Subjects

on behalf
of which the listeners are being added. Elements of this array
can be null. Also, the

delegationSubjects

parameter itself can be null, which is equivalent to an array
of null values with the same size as the

names

and

filters

arrays.
**Returns:** an array of

listenerIDs

identifying the
local listeners. This array has the same number of elements as
the parameters.
**Throws:** IllegalArgumentException

- if

names

or

filters

is null, or if

names

contains
a null element, or if the three arrays do not all have the same
size.
**Throws:** ClassCastException

- if one of the elements of

filters

unmarshalls as a non-null object that is
not a

NotificationFilter

.
**Throws:** InstanceNotFoundException

- if one of the

names

does not correspond to any registered MBean.
**Throws:** SecurityException

- if, for one of the MBeans, the
client, or the delegated Subject if any, does not have
permission to add a listener.
**Throws:** IOException

- if a general communication exception occurred.

---

#### addNotificationListeners

Integer

[] addNotificationListeners​(

ObjectName

[] names,

MarshalledObject

[] filters,

Subject

[] delegationSubjects)
throws

InstanceNotFoundException

,

IOException

Handles the method

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

.

Register for notifications from the given MBeans that match
the given filters. The remote client can subsequently retrieve
the notifications using the

fetchNotifications

method.

For each listener, the original

NotificationListener

and

handback

are
kept on the client side; in order for the client to be able to
identify them, the server generates and returns a unique

listenerID

. This

listenerID

is
forwarded with the

Notifications

to the remote
client.

If any one of the given (name, filter) pairs cannot be
registered, then the operation fails with an exception, and no
names or filters are registered.

Handles the method

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

.

Register for notifications from the given MBeans that match
the given filters. The remote client can subsequently retrieve
the notifications using the

fetchNotifications

method.

For each listener, the original

NotificationListener

and

handback

are
kept on the client side; in order for the client to be able to
identify them, the server generates and returns a unique

listenerID

. This

listenerID

is
forwarded with the

Notifications

to the remote
client.

If any one of the given (name, filter) pairs cannot be
registered, then the operation fails with an exception, and no
names or filters are registered.

removeNotificationListeners

```java
void removeNotificationListeners​(
ObjectName
name,

Integer
[] listenerIDs,

Subject
delegationSubject)
throws
InstanceNotFoundException
,

ListenerNotFoundException
,

IOException
```

Handles the

removeNotificationListener(ObjectName, NotificationListener)

and

removeNotificationListener(ObjectName, NotificationListener, NotificationFilter, Object)

methods.

This method removes one or more

NotificationListener

s from a given MBean in the
MBean server.

The

NotificationListeners

are identified by the
IDs which were returned by the

addNotificationListeners(ObjectName[], MarshalledObject[],
Subject[])

method.

**Parameters:** name

- the

ObjectName

identifying the MBean
emitting the Notifications.
**Parameters:** listenerIDs

- the list of the IDs corresponding to the
listeners to remove.
**Parameters:** delegationSubject

- The

Subject

containing the
delegation principals or

null

if the authentication
principal is used instead.
**Throws:** InstanceNotFoundException

- if the given

name

does not correspond to any registered MBean.
**Throws:** ListenerNotFoundException

- if one of the listeners was
not found on the server side. This exception can happen if the
MBean discarded a listener for some reason other than a call to

MBeanServer.removeNotificationListener

.
**Throws:** SecurityException

- if the client, or the delegated Subject
if any, does not have permission to remove the listeners.
**Throws:** IOException

- if a general communication exception occurred.
**Throws:** IllegalArgumentException

- if

ObjectName

or

listenerIds

is null or if

listenerIds

contains a null element.

---

#### removeNotificationListeners

void removeNotificationListeners​(

ObjectName

name,

Integer

[] listenerIDs,

Subject

delegationSubject)
throws

InstanceNotFoundException

,

ListenerNotFoundException

,

IOException

Handles the

removeNotificationListener(ObjectName, NotificationListener)

and

removeNotificationListener(ObjectName, NotificationListener, NotificationFilter, Object)

methods.

This method removes one or more

NotificationListener

s from a given MBean in the
MBean server.

The

NotificationListeners

are identified by the
IDs which were returned by the

addNotificationListeners(ObjectName[], MarshalledObject[],
Subject[])

method.

Handles the

removeNotificationListener(ObjectName, NotificationListener)

and

removeNotificationListener(ObjectName, NotificationListener, NotificationFilter, Object)

methods.

This method removes one or more

NotificationListener

s from a given MBean in the
MBean server.

The

NotificationListeners

are identified by the
IDs which were returned by the

addNotificationListeners(ObjectName[], MarshalledObject[],
Subject[])

method.

fetchNotifications

```java
NotificationResult
fetchNotifications​(long clientSequenceNumber,
int maxNotifications,
long timeout)
throws
IOException
```

Retrieves notifications from the connector server. This
method can block until there is at least one notification or
until the specified timeout is reached. The method can also
return at any time with zero notifications.

A notification can be included in the result if its sequence
number is no less than

clientSequenceNumber

and
this client has registered at least one listener for the MBean
generating the notification, with a filter that accepts the
notification. Each listener that is interested in the
notification is identified by an Integer ID that was returned
by

addNotificationListeners(ObjectName[],
MarshalledObject[], Subject[])

.

**Parameters:** clientSequenceNumber

- the first sequence number that the
client is interested in. If negative, it is interpreted as
meaning the sequence number that the next notification will
have.
**Parameters:** maxNotifications

- the maximum number of different
notifications to return. The

TargetedNotification

array in the returned

NotificationResult

can have
more elements than this if the same notification appears more
than once. The behavior is unspecified if this parameter is
negative.
**Parameters:** timeout

- the maximum time in milliseconds to wait for a
notification to arrive. This can be 0 to indicate that the
method should not wait if there are no notifications, but
should return at once. It can be

Long.MAX_VALUE

to indicate that there is no timeout. The behavior is
unspecified if this parameter is negative.
**Returns:** A

NotificationResult

.
**Throws:** IOException

- if a general communication exception occurred.

---

#### fetchNotifications

NotificationResult

fetchNotifications​(long clientSequenceNumber,
int maxNotifications,
long timeout)
throws

IOException

Retrieves notifications from the connector server. This
method can block until there is at least one notification or
until the specified timeout is reached. The method can also
return at any time with zero notifications.

A notification can be included in the result if its sequence
number is no less than

clientSequenceNumber

and
this client has registered at least one listener for the MBean
generating the notification, with a filter that accepts the
notification. Each listener that is interested in the
notification is identified by an Integer ID that was returned
by

addNotificationListeners(ObjectName[],
MarshalledObject[], Subject[])

.

Retrieves notifications from the connector server. This
method can block until there is at least one notification or
until the specified timeout is reached. The method can also
return at any time with zero notifications.

A notification can be included in the result if its sequence
number is no less than

clientSequenceNumber

and
this client has registered at least one listener for the MBean
generating the notification, with a filter that accepts the
notification. Each listener that is interested in the
notification is identified by an Integer ID that was returned
by

addNotificationListeners(ObjectName[],
MarshalledObject[], Subject[])

.

---

