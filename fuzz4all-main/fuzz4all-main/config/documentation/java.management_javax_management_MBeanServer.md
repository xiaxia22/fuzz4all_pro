# Interface MBeanServer

**Source:** `java.management\javax\management\MBeanServer.html`

### Class Description

```java
public interface
MBeanServer

extends
MBeanServerConnection
```

This is the interface for MBean manipulation on the agent
side. It contains the methods necessary for the creation,
registration, and deletion of MBeans as well as the access methods
for registered MBeans. This is the core component of the JMX
infrastructure.

User code does not usually implement this interface. Instead,
an object that implements this interface is obtained with one of
the methods in the

MBeanServerFactory

class.

Every MBean which is added to the MBean server becomes
manageable: its attributes and operations become remotely
accessible through the connectors/adaptors connected to that MBean
server. A Java object cannot be registered in the MBean server
unless it is a JMX compliant MBean.

When an MBean is registered or unregistered in the
MBean server a

MBeanServerNotification

Notification is emitted. To register an
object as listener to MBeanServerNotifications you should call the
MBean server method

addNotificationListener

with

ObjectName

the

ObjectName

of the

MBeanServerDelegate

. This

ObjectName

is:

JMImplementation:type=MBeanServerDelegate

.

An object obtained from the

createMBeanServer

or

newMBeanServer

methods of the

MBeanServerFactory

class applies security
checks to its methods, as follows.

First, if there is no security manager (

System.getSecurityManager()

is null), then an implementation of
this interface is free not to make any checks.

Assuming that there is a security manager, or that the
implementation chooses to make checks anyway, the checks are made
as detailed below. In what follows, and unless otherwise specified,

className

is the
string returned by

MBeanInfo.getClassName()

for the target
MBean.

If a security check fails, the method throws

SecurityException

.

For methods that can throw

InstanceNotFoundException

,
this exception is thrown for a non-existent MBean, regardless of
permissions. This is because a non-existent MBean has no

className

.

- For the

invoke

method, the caller's
permissions must imply

MBeanPermission(className, operationName, name, "invoke")

.

For the

getAttribute

method, the
caller's permissions must imply

MBeanPermission(className, attribute, name, "getAttribute")

.

For the

getAttributes

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "getAttribute")

.
Additionally, for each attribute

a

in the

AttributeList

, if the caller's permissions do not imply

MBeanPermission(className,

a

, name, "getAttribute")

, the
MBean server will behave as if that attribute had not been in the
supplied list.

For the

setAttribute

method, the
caller's permissions must imply

MBeanPermission(className, attrName, name, "setAttribute")

, where

attrName

is

attribute.getName()

.

For the

setAttributes

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "setAttribute")

.
Additionally, for each attribute

a

in the

AttributeList

, if the caller's permissions do not imply

MBeanPermission(className,

a

, name, "setAttribute")

, the
MBean server will behave as if that attribute had not been in the
supplied list.

For the

addNotificationListener

methods,
the caller's permissions must imply

MBeanPermission(className, null, name,
"addNotificationListener")

.

For the

removeNotificationListener

methods,
the caller's permissions must imply

MBeanPermission(className, null, name,
"removeNotificationListener")

.

For the

getMBeanInfo

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "getMBeanInfo")

.

For the

getObjectInstance

method,
the caller's permissions must imply

MBeanPermission(className, null, name, "getObjectInstance")

.

For the

isInstanceOf

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "isInstanceOf")

.

For the

queryMBeans

method, the
caller's permissions must imply

MBeanPermission(null, null, null, "queryMBeans")

.
Additionally, for each MBean

n

that matches

name

,
if the caller's permissions do not imply

MBeanPermission(className, null,

n

, "queryMBeans")

, the
MBean server will behave as if that MBean did not exist.

Certain query elements perform operations on the MBean server.
If the caller does not have the required permissions for a given
MBean, that MBean will not be included in the result of the query.
The standard query elements that are affected are

Query.attr(String)

,

Query.attr(String,String)

, and

Query.classattr()

.

For the

queryNames

method, the checks
are the same as for

queryMBeans

except that

"queryNames"

is used instead of

"queryMBeans"

in the

MBeanPermission

objects. Note that a

"queryMBeans"

permission implies
the corresponding

"queryNames"

permission.

For the

getDomains

method, the caller's
permissions must imply

MBeanPermission(null, null, null, "getDomains")

. Additionally,
for each domain

d

in the returned array, if the caller's
permissions do not imply

MBeanPermission(null, null, new ObjectName("

d

:x=x"),
"getDomains")

, the domain is eliminated from the array. Here,

x=x

is any

key=value

pair, needed to
satisfy ObjectName's constructor but not otherwise relevant.

For the

getClassLoader

method, the
caller's permissions must imply

MBeanPermission(className, null, loaderName,
"getClassLoader")

.

For the

getClassLoaderFor

method,
the caller's permissions must imply

MBeanPermission(className, null, mbeanName,
"getClassLoaderFor")

.

For the

getClassLoaderRepository

method, the caller's permissions must
imply

MBeanPermission(null, null, null, "getClassLoaderRepository")

.

For the deprecated

deserialize

methods, the
required permissions are the same as for the methods that replace
them.

For the

instantiate

methods, the caller's
permissions must imply

MBeanPermission(className, null, null, "instantiate")

,
where

className

is the name of the class which is to
be instantiated.

For the

registerMBean

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "registerMBean")

.

If the

MBeanPermission

check succeeds, the MBean's
class is validated by checking that its

ProtectionDomain

implies

MBeanTrustPermission("register")

.

Finally, if the

name

argument is null, another

MBeanPermission

check is made using the

ObjectName

returned by

MBeanRegistration.preRegister

.

For the

createMBean

methods, the caller's
permissions must imply the permissions needed by the equivalent

instantiate

followed by

registerMBean

.

For the

unregisterMBean

method,
the caller's permissions must imply

MBeanPermission(className, null, name, "unregisterMBean")

.

**All Superinterfaces:** MBeanServerConnection

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ObjectInstance
createMBean​(
String
className,

ObjectName
name)
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

Instantiates and registers an MBean in the MBean server. The
MBean server will use its

Default Loader
Repository

to load the class of the MBean. An object name is
associated with the MBean. If the object name given is null, the
MBean must provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

This method is equivalent to

createMBean(className, name, (Object[]) null, (String[])
null)

.

If this method successfully creates an MBean, a notification
is sent as described

above

.

**Specified by:**
- createMBean

in interface

MBeanServerConnection

**Parameters:**
- className

- The class name of the MBean to be instantiated.
- name

- The object name of the MBean. May be null.

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
- RuntimeMBeanException

- If the MBean's constructor or its

preRegister

or

postRegister

method threw
a

RuntimeException

. If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

createMBean

method will
throw a

RuntimeMBeanException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
- RuntimeErrorException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

createMBean

method will
throw a

RuntimeErrorException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
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
thrown an exception
- NotCompliantMBeanException

- This class is not a JMX
compliant MBean

**See Also:**
- MBeanRegistration

---

#### ObjectInstance
createMBean​(
String
className,

ObjectName
name,

ObjectName
loaderName)
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

Instantiates and registers an MBean in the MBean server. The
class loader to be used is identified by its object name. An
object name is associated with the MBean. If the object name of
the loader is null, the ClassLoader that loaded the MBean
server will be used. If the MBean's object name given is null,
the MBean must provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

This method is equivalent to

createMBean(className, name, loaderName, (Object[]) null,
(String[]) null)

.

If this method successfully creates an MBean, a notification
is sent as described

above

.

**Specified by:**
- createMBean

in interface

MBeanServerConnection

**Parameters:**
- className

- The class name of the MBean to be instantiated.
- name

- The object name of the MBean. May be null.
- loaderName

- The object name of the class loader to be used.

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
- RuntimeMBeanException

- If the MBean's constructor or its

preRegister

or

postRegister

method threw
a

RuntimeException

. If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

createMBean

method will
throw a

RuntimeMBeanException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
- RuntimeErrorException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

createMBean

method will
throw a

RuntimeErrorException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
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
thrown an exception
- NotCompliantMBeanException

- This class is not a JMX
compliant MBean
- InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.

**See Also:**
- MBeanRegistration

---

#### ObjectInstance
createMBean​(
String
className,

ObjectName
name,

Object
[] params,

String
[] signature)
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

Instantiates and registers an MBean in the MBean server. The
MBean server will use its

Default Loader
Repository

to load the class of the MBean. An object name is
associated with the MBean. If the object name given is null, the
MBean must provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

If this method successfully creates an MBean, a notification
is sent as described

above

.

**Specified by:**
- createMBean

in interface

MBeanServerConnection

**Parameters:**
- className

- The class name of the MBean to be instantiated.
- name

- The object name of the MBean. May be null.
- params

- An array containing the parameters of the
constructor to be invoked.
- signature

- An array containing the signature of the
constructor to be invoked.

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
- RuntimeMBeanException

- If the MBean's constructor or its

preRegister

or

postRegister

method threw
a

RuntimeException

. If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

createMBean

method will
throw a

RuntimeMBeanException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
- RuntimeErrorException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

createMBean

method will
throw a

RuntimeErrorException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
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
thrown an exception
- NotCompliantMBeanException

- This class is not a JMX
compliant MBean

**See Also:**
- MBeanRegistration

---

#### ObjectInstance
createMBean​(
String
className,

ObjectName
name,

ObjectName
loaderName,

Object
[] params,

String
[] signature)
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

Instantiates and registers an MBean in the MBean server. The
class loader to be used is identified by its object name. An
object name is associated with the MBean. If the object name of
the loader is not specified, the ClassLoader that loaded the
MBean server will be used. If the MBean object name given is
null, the MBean must provide its own name by implementing the

MBeanRegistration

interface and returning the name from the

preRegister

method.

If this method successfully creates an MBean, a notification
is sent as described

above

.

**Specified by:**
- createMBean

in interface

MBeanServerConnection

**Parameters:**
- className

- The class name of the MBean to be instantiated.
- name

- The object name of the MBean. May be null.
- loaderName

- The object name of the class loader to be used.
- params

- An array containing the parameters of the
constructor to be invoked.
- signature

- An array containing the signature of the
constructor to be invoked.

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
- RuntimeMBeanException

- The MBean's constructor or its

preRegister

or

postRegister

method threw
a

RuntimeException

. If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

createMBean

method will
throw a

RuntimeMBeanException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
- RuntimeErrorException

- If the

postRegister

method
(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

createMBean

method will
throw a

RuntimeErrorException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
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
thrown an exception
- NotCompliantMBeanException

- This class is not a JMX
compliant MBean
- InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.

**See Also:**
- MBeanRegistration

---

#### ObjectInstance
registerMBean​(
Object
object,

ObjectName
name)
throws
InstanceAlreadyExistsException
,

MBeanRegistrationException
,

NotCompliantMBeanException

Registers a pre-existing object as an MBean with the MBean
server. If the object name given is null, the MBean must
provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

If this method successfully registers an MBean, a notification
is sent as described

above

.

**Parameters:**
- object

- The MBean to be registered as an MBean.
- name

- The object name of the MBean. May be null.

**Returns:**
- An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
registered MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.

**Throws:**
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
- RuntimeMBeanException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

registerMBean

method will
throw a

RuntimeMBeanException

, although the MBean
registration succeeded. In such a case, the MBean will be actually
registered even though the

registerMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
- RuntimeErrorException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

registerMBean

method will
throw a

RuntimeErrorException

, although the MBean
registration succeeded. In such a case, the MBean will be actually
registered even though the

registerMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
- NotCompliantMBeanException

- This object is not a JMX
compliant MBean
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
passed in parameter is null or no object name is specified.

**See Also:**
- MBeanRegistration

---

#### void unregisterMBean​(
ObjectName
name)
throws
InstanceNotFoundException
,

MBeanRegistrationException

Unregisters an MBean from the MBean server. The MBean is
identified by its object name. Once the method has been
invoked, the MBean may no longer be accessed by its object
name.

If this method successfully unregisters an MBean, a notification
is sent as described

above

.

**Specified by:**
- unregisterMBean

in interface

MBeanServerConnection

**Parameters:**
- name

- The object name of the MBean to be unregistered.

**Throws:**
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the MBean you are when trying to
unregister is the

MBeanServerDelegate

MBean.
- RuntimeMBeanException

- If the

postDeregister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

unregisterMBean

method
will throw a

RuntimeMBeanException

, although the MBean
unregistration succeeded. In such a case, the MBean will be actually
unregistered even though the

unregisterMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preDeregister

, in which case the MBean
will remain registered.
- RuntimeErrorException

- If the

postDeregister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

unregisterMBean

method will
throw a

RuntimeErrorException

, although the MBean
unregistration succeeded. In such a case, the MBean will be actually
unregistered even though the

unregisterMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preDeregister

, in which case the MBean
will remain registered.
- InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
- MBeanRegistrationException

- The preDeregister
((

MBeanRegistration

interface) method of the MBean
has thrown an exception.

**See Also:**
- MBeanRegistration

---

#### Set
<
ObjectInstance
> queryMBeans​(
ObjectName
name,

QueryExp
query)

Gets MBeans controlled by the MBean server. This method allows
any of the following to be obtained: All MBeans, a set of
MBeans specified by pattern matching on the

ObjectName

and/or a Query expression, a specific
MBean. When the object name is null or no domain and key
properties are specified, all objects are to be selected (and
filtered if a query is specified). It returns the set of

ObjectInstance

objects (containing the

ObjectName

and the Java Class name) for the
selected MBeans.

**Specified by:**
- queryMBeans

in interface

MBeanServerConnection

**Parameters:**
- name

- The object name pattern identifying the MBeans to
be retrieved. If null or no domain and key properties are
specified, all the MBeans registered will be retrieved.
- query

- The query expression to be applied for selecting
MBeans. If null no query expression will be applied for
selecting MBeans.

**Returns:**
- A set containing the

ObjectInstance

objects for the selected MBeans. If no MBean satisfies the
query an empty list is returned.

**Throws:**
- RuntimeOperationsException

---

#### Set
<
ObjectName
> queryNames​(
ObjectName
name,

QueryExp
query)

Gets the names of MBeans controlled by the MBean server. This
method enables any of the following to be obtained: The names
of all MBeans, the names of a set of MBeans specified by
pattern matching on the

ObjectName

and/or a Query
expression, a specific MBean name (equivalent to testing
whether an MBean is registered). When the object name is null
or no domain and key properties are specified, all objects are
selected (and filtered if a query is specified). It returns the
set of ObjectNames for the MBeans selected.

**Specified by:**
- queryNames

in interface

MBeanServerConnection

**Parameters:**
- name

- The object name pattern identifying the MBean names
to be retrieved. If null or no domain and key properties are
specified, the name of all registered MBeans will be retrieved.
- query

- The query expression to be applied for selecting
MBeans. If null no query expression will be applied for
selecting MBeans.

**Returns:**
- A set containing the ObjectNames for the MBeans
selected. If no MBean satisfies the query, an empty list is
returned.

**Throws:**
- RuntimeOperationsException

---

#### boolean isRegistered​(
ObjectName
name)

Description copied from interface:

MBeanServerConnection

**Specified by:**
- isRegistered

in interface

MBeanServerConnection

**Parameters:**
- name

- The object name of the MBean to be checked.

**Returns:**
- True if the MBean is already registered in the MBean
server, false otherwise.

**Throws:**
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.

---

#### Integer
getMBeanCount()

Returns the number of MBeans registered in the MBean server.

**Specified by:**
- getMBeanCount

in interface

MBeanServerConnection

**Returns:**
- the number of registered MBeans, wrapped in an Integer.
If the caller's permissions are restricted, this number may
be greater than the number of MBeans the caller can access.

---

#### Object
getAttribute​(
ObjectName
name,

String
attribute)
throws
MBeanException
,

AttributeNotFoundException
,

InstanceNotFoundException
,

ReflectionException

Description copied from interface:

MBeanServerConnection

**Specified by:**
- getAttribute

in interface

MBeanServerConnection

**Parameters:**
- name

- The object name of the MBean from which the
attribute is to be retrieved.
- attribute

- A String specifying the name of the attribute
to be retrieved.

**Returns:**
- The value of the retrieved attribute.

**Throws:**
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the attribute in parameter is
null.
- MBeanException

- Wraps an exception thrown by the
MBean's getter.
- AttributeNotFoundException

- The attribute specified
is not accessible in the MBean.
- InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
- ReflectionException

- Wraps a

java.lang.Exception

thrown when trying to invoke
the setter.

**See Also:**
- MBeanServerConnection.setAttribute(javax.management.ObjectName, javax.management.Attribute)

---

#### AttributeList
getAttributes​(
ObjectName
name,

String
[] attributes)
throws
InstanceNotFoundException
,

ReflectionException

Description copied from interface:

MBeanServerConnection

**Specified by:**
- getAttributes

in interface

MBeanServerConnection

**Parameters:**
- name

- The object name of the MBean from which the
attributes are retrieved.
- attributes

- A list of the attributes to be retrieved.

**Returns:**
- The list of the retrieved attributes.

**Throws:**
- RuntimeOperationsException

- Wrap a

java.lang.IllegalArgumentException

: The object
name in parameter is null or attributes in parameter is null.
- InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
- ReflectionException

- An exception occurred when
trying to invoke the getAttributes method of a Dynamic MBean.

**See Also:**
- MBeanServerConnection.setAttributes(javax.management.ObjectName, javax.management.AttributeList)

---

#### void setAttribute​(
ObjectName
name,

Attribute
attribute)
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

Description copied from interface:

MBeanServerConnection

**Specified by:**
- setAttribute

in interface

MBeanServerConnection

**Parameters:**
- name

- The name of the MBean within which the attribute is
to be set.
- attribute

- The identification of the attribute to be set
and the value it is to be set to.

**Throws:**
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the attribute in parameter is
null.
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

**See Also:**
- MBeanServerConnection.getAttribute(javax.management.ObjectName, java.lang.String)

---

#### AttributeList
setAttributes​(
ObjectName
name,

AttributeList
attributes)
throws
InstanceNotFoundException
,

ReflectionException

Description copied from interface:

MBeanServerConnection

**Specified by:**
- setAttributes

in interface

MBeanServerConnection

**Parameters:**
- name

- The object name of the MBean within which the
attributes are to be set.
- attributes

- A list of attributes: The identification of
the attributes to be set and the values they are to be set to.

**Returns:**
- The list of attributes that were set, with their new
values.

**Throws:**
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or attributes in parameter is null.
- InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
- ReflectionException

- An exception occurred when
trying to invoke the getAttributes method of a Dynamic MBean.

**See Also:**
- MBeanServerConnection.getAttributes(javax.management.ObjectName, java.lang.String[])

---

#### void addNotificationListener​(
ObjectName
name,

NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
throws
InstanceNotFoundException

Adds a listener to a registered MBean.
Notifications emitted by the MBean will be forwarded to the listener.

If the source of the notification
is a reference to an MBean object, the MBean server will replace it
by that MBean's ObjectName. Otherwise the source is unchanged.

**Specified by:**
- addNotificationListener

in interface

MBeanServerConnection

**Parameters:**
- name

- The name of the MBean on which the listener should
be added.
- listener

- The listener object which will handle the
notifications emitted by the registered MBean.
- filter

- The filter object. If filter is null, no
filtering will be performed before handling notifications.
- handback

- The context to be sent to the listener when a
notification is emitted.

**Throws:**
- InstanceNotFoundException

- The MBean name provided
does not match any of the registered MBeans.

**See Also:**
- MBeanServerConnection.removeNotificationListener(ObjectName, NotificationListener)

,

MBeanServerConnection.removeNotificationListener(ObjectName, NotificationListener,
NotificationFilter, Object)

---

#### void addNotificationListener​(
ObjectName
name,

ObjectName
listener,

NotificationFilter
filter,

Object
handback)
throws
InstanceNotFoundException

Adds a listener to a registered MBean.

A notification emitted by an MBean will be forwarded by the
MBeanServer to the listener. If the source of the notification
is a reference to an MBean object, the MBean server will
replace it by that MBean's ObjectName. Otherwise the source is
unchanged.

The listener object that receives notifications is the one
that is registered with the given name at the time this method
is called. Even if it is subsequently unregistered, it will
continue to receive notifications.

**Specified by:**
- addNotificationListener

in interface

MBeanServerConnection

**Parameters:**
- name

- The name of the MBean on which the listener should
be added.
- listener

- The object name of the listener which will
handle the notifications emitted by the registered MBean.
- filter

- The filter object. If filter is null, no
filtering will be performed before handling notifications.
- handback

- The context to be sent to the listener when a
notification is emitted.

**Throws:**
- RuntimeOperationsException

- Wraps an

IllegalArgumentException

. The MBean named by

listener

exists but does not implement the

NotificationListener

interface.
- InstanceNotFoundException

- The MBean name of the
notification listener or of the notification broadcaster does
not match any of the registered MBeans.

**See Also:**
- MBeanServerConnection.removeNotificationListener(ObjectName, ObjectName)

,

MBeanServerConnection.removeNotificationListener(ObjectName, ObjectName,
NotificationFilter, Object)

---

#### Object
instantiate​(
String
className)
throws
ReflectionException
,

MBeanException

Instantiates an object using the list of all class loaders
registered in the MBean server's

Class Loader
Repository

. The object's class should have a public
constructor. This method returns a reference to the newly
created object. The newly created object is not registered in
the MBean server.

This method is equivalent to

instantiate(className, (Object[]) null, (String[]) null)

.

**Parameters:**
- className

- The class name of the object to be instantiated.

**Returns:**
- The newly instantiated object.

**Throws:**
- ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or the

java.lang.Exception

that occurred when trying to
invoke the object's constructor.
- MBeanException

- The constructor of the object has
thrown an exception
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null.

---

#### Object
instantiate​(
String
className,

ObjectName
loaderName)
throws
ReflectionException
,

MBeanException
,

InstanceNotFoundException

Instantiates an object using the class Loader specified by its

ObjectName

. If the loader name is null, the
ClassLoader that loaded the MBean Server will be used. The
object's class should have a public constructor. This method
returns a reference to the newly created object. The newly
created object is not registered in the MBean server.

This method is equivalent to

instantiate(className, loaderName, (Object[]) null, (String[])
null)

.

**Parameters:**
- className

- The class name of the MBean to be instantiated.
- loaderName

- The object name of the class loader to be used.

**Returns:**
- The newly instantiated object.

**Throws:**
- ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or the

java.lang.Exception

that occurred when trying to
invoke the object's constructor.
- MBeanException

- The constructor of the object has
thrown an exception.
- InstanceNotFoundException

- The specified class loader
is not registered in the MBeanServer.
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null.

---

#### Object
instantiate​(
String
className,

Object
[] params,

String
[] signature)
throws
ReflectionException
,

MBeanException

Instantiates an object using the list of all class loaders
registered in the MBean server

Class Loader
Repository

. The object's class should have a public
constructor. The call returns a reference to the newly created
object. The newly created object is not registered in the
MBean server.

**Parameters:**
- className

- The class name of the object to be instantiated.
- params

- An array containing the parameters of the
constructor to be invoked.
- signature

- An array containing the signature of the
constructor to be invoked.

**Returns:**
- The newly instantiated object.

**Throws:**
- ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or the

java.lang.Exception

that occurred when trying to
invoke the object's constructor.
- MBeanException

- The constructor of the object has
thrown an exception
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null.

---

#### Object
instantiate​(
String
className,

ObjectName
loaderName,

Object
[] params,

String
[] signature)
throws
ReflectionException
,

MBeanException
,

InstanceNotFoundException

Instantiates an object. The class loader to be used is
identified by its object name. If the object name of the loader
is null, the ClassLoader that loaded the MBean server will be
used. The object's class should have a public constructor.
The call returns a reference to the newly created object. The
newly created object is not registered in the MBean server.

**Parameters:**
- className

- The class name of the object to be instantiated.
- params

- An array containing the parameters of the
constructor to be invoked.
- signature

- An array containing the signature of the
constructor to be invoked.
- loaderName

- The object name of the class loader to be used.

**Returns:**
- The newly instantiated object.

**Throws:**
- ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or the

java.lang.Exception

that
occurred when trying to invoke the object's constructor.
- MBeanException

- The constructor of the object has
thrown an exception
- InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
- RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null.

---

#### @Deprecated
(
since
="1.5")
default
ObjectInputStream
deserialize​(
ObjectName
name,
byte[] data)
throws
InstanceNotFoundException
,

OperationsException

De-serializes a byte array in the context of the class loader
of an MBean.

**Parameters:**
- name

- The name of the MBean whose class loader should be
used for the de-serialization.
- data

- The byte array to be de-sererialized.

**Returns:**
- The de-serialized object stream.

**Throws:**
- InstanceNotFoundException

- The MBean specified is not
found.
- OperationsException

- Any of the usual Input/Output
related exceptions.

**Implementation Requirements:**
- This method throws

UnsupportedOperationException

by default.

---

#### @Deprecated
(
since
="1.5")
default
ObjectInputStream
deserialize​(
String
className,
byte[] data)
throws
OperationsException
,

ReflectionException

De-serializes a byte array in the context of a given MBean
class loader. The class loader is found by loading the class

className

through the

Class Loader
Repository

. The resultant class's class loader is the one to
use.

**Parameters:**
- className

- The name of the class whose class loader should be
used for the de-serialization.
- data

- The byte array to be de-sererialized.

**Returns:**
- The de-serialized object stream.

**Throws:**
- OperationsException

- Any of the usual Input/Output
related exceptions.
- ReflectionException

- The specified class could not be
loaded by the class loader repository

**Implementation Requirements:**
- This method throws

UnsupportedOperationException

by default.

---

#### @Deprecated
(
since
="1.5")
default
ObjectInputStream
deserialize​(
String
className,

ObjectName
loaderName,
byte[] data)
throws
InstanceNotFoundException
,

OperationsException
,

ReflectionException

De-serializes a byte array in the context of a given MBean
class loader. The class loader is the one that loaded the
class with name "className". The name of the class loader to
be used for loading the specified class is specified. If null,
the MBean Server's class loader will be used.

**Parameters:**
- className

- The name of the class whose class loader should be
used for the de-serialization.
- data

- The byte array to be de-sererialized.
- loaderName

- The name of the class loader to be used for
loading the specified class. If null, the MBean Server's class
loader will be used.

**Returns:**
- The de-serialized object stream.

**Throws:**
- InstanceNotFoundException

- The specified class loader
MBean is not found.
- OperationsException

- Any of the usual Input/Output
related exceptions.
- ReflectionException

- The specified class could not be
loaded by the specified class loader.

**Implementation Requirements:**
- This method throws

UnsupportedOperationException

by default.

---

#### ClassLoader
getClassLoaderFor​(
ObjectName
mbeanName)
throws
InstanceNotFoundException

Return the

ClassLoader

that was used for
loading the class of the named MBean.

**Parameters:**
- mbeanName

- The ObjectName of the MBean.

**Returns:**
- The ClassLoader used for that MBean. If

l

is the MBean's actual ClassLoader, and

r

is the
returned value, then either:

- r

is identical to

l

; or

the result of

r

.loadClass(

s

)

is the
same as

l

.loadClass(

s

)

for any string

s

.

What this means is that the ClassLoader may be wrapped in
another ClassLoader for security or other reasons.

**Throws:**
- InstanceNotFoundException

- if the named MBean is not found.

---

#### ClassLoader
getClassLoader​(
ObjectName
loaderName)
throws
InstanceNotFoundException

Return the named

ClassLoader

.

**Parameters:**
- loaderName

- The ObjectName of the ClassLoader. May be
null, in which case the MBean server's own ClassLoader is
returned.

**Returns:**
- The named ClassLoader. If

l

is the actual
ClassLoader with that name, and

r

is the returned
value, then either:

- r

is identical to

l

; or

the result of

r

.loadClass(

s

)

is the
same as

l

.loadClass(

s

)

for any string

s

.

What this means is that the ClassLoader may be wrapped in
another ClassLoader for security or other reasons.

**Throws:**
- InstanceNotFoundException

- if the named ClassLoader is
not found.

---

#### ClassLoaderRepository
getClassLoaderRepository()

Return the ClassLoaderRepository for this MBeanServer.

**Returns:**
- The ClassLoaderRepository for this MBeanServer.

---

### Additional Sections

#### Interface MBeanServer

**All Superinterfaces:** MBeanServerConnection

**All Known Subinterfaces:** MBeanServerForwarder

```java
public interface
MBeanServer

extends
MBeanServerConnection
```

This is the interface for MBean manipulation on the agent
side. It contains the methods necessary for the creation,
registration, and deletion of MBeans as well as the access methods
for registered MBeans. This is the core component of the JMX
infrastructure.

User code does not usually implement this interface. Instead,
an object that implements this interface is obtained with one of
the methods in the

MBeanServerFactory

class.

Every MBean which is added to the MBean server becomes
manageable: its attributes and operations become remotely
accessible through the connectors/adaptors connected to that MBean
server. A Java object cannot be registered in the MBean server
unless it is a JMX compliant MBean.

When an MBean is registered or unregistered in the
MBean server a

MBeanServerNotification

Notification is emitted. To register an
object as listener to MBeanServerNotifications you should call the
MBean server method

addNotificationListener

with

ObjectName

the

ObjectName

of the

MBeanServerDelegate

. This

ObjectName

is:

JMImplementation:type=MBeanServerDelegate

.

An object obtained from the

createMBeanServer

or

newMBeanServer

methods of the

MBeanServerFactory

class applies security
checks to its methods, as follows.

First, if there is no security manager (

System.getSecurityManager()

is null), then an implementation of
this interface is free not to make any checks.

Assuming that there is a security manager, or that the
implementation chooses to make checks anyway, the checks are made
as detailed below. In what follows, and unless otherwise specified,

className

is the
string returned by

MBeanInfo.getClassName()

for the target
MBean.

If a security check fails, the method throws

SecurityException

.

For methods that can throw

InstanceNotFoundException

,
this exception is thrown for a non-existent MBean, regardless of
permissions. This is because a non-existent MBean has no

className

.

- For the

invoke

method, the caller's
permissions must imply

MBeanPermission(className, operationName, name, "invoke")

.

For the

getAttribute

method, the
caller's permissions must imply

MBeanPermission(className, attribute, name, "getAttribute")

.

For the

getAttributes

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "getAttribute")

.
Additionally, for each attribute

a

in the

AttributeList

, if the caller's permissions do not imply

MBeanPermission(className,

a

, name, "getAttribute")

, the
MBean server will behave as if that attribute had not been in the
supplied list.

For the

setAttribute

method, the
caller's permissions must imply

MBeanPermission(className, attrName, name, "setAttribute")

, where

attrName

is

attribute.getName()

.

For the

setAttributes

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "setAttribute")

.
Additionally, for each attribute

a

in the

AttributeList

, if the caller's permissions do not imply

MBeanPermission(className,

a

, name, "setAttribute")

, the
MBean server will behave as if that attribute had not been in the
supplied list.

For the

addNotificationListener

methods,
the caller's permissions must imply

MBeanPermission(className, null, name,
"addNotificationListener")

.

For the

removeNotificationListener

methods,
the caller's permissions must imply

MBeanPermission(className, null, name,
"removeNotificationListener")

.

For the

getMBeanInfo

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "getMBeanInfo")

.

For the

getObjectInstance

method,
the caller's permissions must imply

MBeanPermission(className, null, name, "getObjectInstance")

.

For the

isInstanceOf

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "isInstanceOf")

.

For the

queryMBeans

method, the
caller's permissions must imply

MBeanPermission(null, null, null, "queryMBeans")

.
Additionally, for each MBean

n

that matches

name

,
if the caller's permissions do not imply

MBeanPermission(className, null,

n

, "queryMBeans")

, the
MBean server will behave as if that MBean did not exist.

Certain query elements perform operations on the MBean server.
If the caller does not have the required permissions for a given
MBean, that MBean will not be included in the result of the query.
The standard query elements that are affected are

Query.attr(String)

,

Query.attr(String,String)

, and

Query.classattr()

.

For the

queryNames

method, the checks
are the same as for

queryMBeans

except that

"queryNames"

is used instead of

"queryMBeans"

in the

MBeanPermission

objects. Note that a

"queryMBeans"

permission implies
the corresponding

"queryNames"

permission.

For the

getDomains

method, the caller's
permissions must imply

MBeanPermission(null, null, null, "getDomains")

. Additionally,
for each domain

d

in the returned array, if the caller's
permissions do not imply

MBeanPermission(null, null, new ObjectName("

d

:x=x"),
"getDomains")

, the domain is eliminated from the array. Here,

x=x

is any

key=value

pair, needed to
satisfy ObjectName's constructor but not otherwise relevant.

For the

getClassLoader

method, the
caller's permissions must imply

MBeanPermission(className, null, loaderName,
"getClassLoader")

.

For the

getClassLoaderFor

method,
the caller's permissions must imply

MBeanPermission(className, null, mbeanName,
"getClassLoaderFor")

.

For the

getClassLoaderRepository

method, the caller's permissions must
imply

MBeanPermission(null, null, null, "getClassLoaderRepository")

.

For the deprecated

deserialize

methods, the
required permissions are the same as for the methods that replace
them.

For the

instantiate

methods, the caller's
permissions must imply

MBeanPermission(className, null, null, "instantiate")

,
where

className

is the name of the class which is to
be instantiated.

For the

registerMBean

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "registerMBean")

.

If the

MBeanPermission

check succeeds, the MBean's
class is validated by checking that its

ProtectionDomain

implies

MBeanTrustPermission("register")

.

Finally, if the

name

argument is null, another

MBeanPermission

check is made using the

ObjectName

returned by

MBeanRegistration.preRegister

.

For the

createMBean

methods, the caller's
permissions must imply the permissions needed by the equivalent

instantiate

followed by

registerMBean

.

For the

unregisterMBean

method,
the caller's permissions must imply

MBeanPermission(className, null, name, "unregisterMBean")

.

**Since:** 1.5

public interface

MBeanServer

extends

MBeanServerConnection

This is the interface for MBean manipulation on the agent
side. It contains the methods necessary for the creation,
registration, and deletion of MBeans as well as the access methods
for registered MBeans. This is the core component of the JMX
infrastructure.

User code does not usually implement this interface. Instead,
an object that implements this interface is obtained with one of
the methods in the

MBeanServerFactory

class.

Every MBean which is added to the MBean server becomes
manageable: its attributes and operations become remotely
accessible through the connectors/adaptors connected to that MBean
server. A Java object cannot be registered in the MBean server
unless it is a JMX compliant MBean.

When an MBean is registered or unregistered in the
MBean server a

MBeanServerNotification

Notification is emitted. To register an
object as listener to MBeanServerNotifications you should call the
MBean server method

addNotificationListener

with

ObjectName

the

ObjectName

of the

MBeanServerDelegate

. This

ObjectName

is:

JMImplementation:type=MBeanServerDelegate

.

An object obtained from the

createMBeanServer

or

newMBeanServer

methods of the

MBeanServerFactory

class applies security
checks to its methods, as follows.

First, if there is no security manager (

System.getSecurityManager()

is null), then an implementation of
this interface is free not to make any checks.

Assuming that there is a security manager, or that the
implementation chooses to make checks anyway, the checks are made
as detailed below. In what follows, and unless otherwise specified,

className

is the
string returned by

MBeanInfo.getClassName()

for the target
MBean.

If a security check fails, the method throws

SecurityException

.

For methods that can throw

InstanceNotFoundException

,
this exception is thrown for a non-existent MBean, regardless of
permissions. This is because a non-existent MBean has no

className

.

- For the

invoke

method, the caller's
permissions must imply

MBeanPermission(className, operationName, name, "invoke")

.

For the

getAttribute

method, the
caller's permissions must imply

MBeanPermission(className, attribute, name, "getAttribute")

.

For the

getAttributes

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "getAttribute")

.
Additionally, for each attribute

a

in the

AttributeList

, if the caller's permissions do not imply

MBeanPermission(className,

a

, name, "getAttribute")

, the
MBean server will behave as if that attribute had not been in the
supplied list.

For the

setAttribute

method, the
caller's permissions must imply

MBeanPermission(className, attrName, name, "setAttribute")

, where

attrName

is

attribute.getName()

.

For the

setAttributes

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "setAttribute")

.
Additionally, for each attribute

a

in the

AttributeList

, if the caller's permissions do not imply

MBeanPermission(className,

a

, name, "setAttribute")

, the
MBean server will behave as if that attribute had not been in the
supplied list.

For the

addNotificationListener

methods,
the caller's permissions must imply

MBeanPermission(className, null, name,
"addNotificationListener")

.

For the

removeNotificationListener

methods,
the caller's permissions must imply

MBeanPermission(className, null, name,
"removeNotificationListener")

.

For the

getMBeanInfo

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "getMBeanInfo")

.

For the

getObjectInstance

method,
the caller's permissions must imply

MBeanPermission(className, null, name, "getObjectInstance")

.

For the

isInstanceOf

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "isInstanceOf")

.

For the

queryMBeans

method, the
caller's permissions must imply

MBeanPermission(null, null, null, "queryMBeans")

.
Additionally, for each MBean

n

that matches

name

,
if the caller's permissions do not imply

MBeanPermission(className, null,

n

, "queryMBeans")

, the
MBean server will behave as if that MBean did not exist.

Certain query elements perform operations on the MBean server.
If the caller does not have the required permissions for a given
MBean, that MBean will not be included in the result of the query.
The standard query elements that are affected are

Query.attr(String)

,

Query.attr(String,String)

, and

Query.classattr()

.

For the

queryNames

method, the checks
are the same as for

queryMBeans

except that

"queryNames"

is used instead of

"queryMBeans"

in the

MBeanPermission

objects. Note that a

"queryMBeans"

permission implies
the corresponding

"queryNames"

permission.

For the

getDomains

method, the caller's
permissions must imply

MBeanPermission(null, null, null, "getDomains")

. Additionally,
for each domain

d

in the returned array, if the caller's
permissions do not imply

MBeanPermission(null, null, new ObjectName("

d

:x=x"),
"getDomains")

, the domain is eliminated from the array. Here,

x=x

is any

key=value

pair, needed to
satisfy ObjectName's constructor but not otherwise relevant.

For the

getClassLoader

method, the
caller's permissions must imply

MBeanPermission(className, null, loaderName,
"getClassLoader")

.

For the

getClassLoaderFor

method,
the caller's permissions must imply

MBeanPermission(className, null, mbeanName,
"getClassLoaderFor")

.

For the

getClassLoaderRepository

method, the caller's permissions must
imply

MBeanPermission(null, null, null, "getClassLoaderRepository")

.

For the deprecated

deserialize

methods, the
required permissions are the same as for the methods that replace
them.

For the

instantiate

methods, the caller's
permissions must imply

MBeanPermission(className, null, null, "instantiate")

,
where

className

is the name of the class which is to
be instantiated.

For the

registerMBean

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "registerMBean")

.

If the

MBeanPermission

check succeeds, the MBean's
class is validated by checking that its

ProtectionDomain

implies

MBeanTrustPermission("register")

.

Finally, if the

name

argument is null, another

MBeanPermission

check is made using the

ObjectName

returned by

MBeanRegistration.preRegister

.

For the

createMBean

methods, the caller's
permissions must imply the permissions needed by the equivalent

instantiate

followed by

registerMBean

.

For the

unregisterMBean

method,
the caller's permissions must imply

MBeanPermission(className, null, name, "unregisterMBean")

.

This is the interface for MBean manipulation on the agent
side. It contains the methods necessary for the creation,
registration, and deletion of MBeans as well as the access methods
for registered MBeans. This is the core component of the JMX
infrastructure.

User code does not usually implement this interface. Instead,
an object that implements this interface is obtained with one of
the methods in the

MBeanServerFactory

class.

Every MBean which is added to the MBean server becomes
manageable: its attributes and operations become remotely
accessible through the connectors/adaptors connected to that MBean
server. A Java object cannot be registered in the MBean server
unless it is a JMX compliant MBean.

When an MBean is registered or unregistered in the
MBean server a

MBeanServerNotification

Notification is emitted. To register an
object as listener to MBeanServerNotifications you should call the
MBean server method

addNotificationListener

with

ObjectName

the

ObjectName

of the

MBeanServerDelegate

. This

ObjectName

is:

JMImplementation:type=MBeanServerDelegate

.

An object obtained from the

createMBeanServer

or

newMBeanServer

methods of the

MBeanServerFactory

class applies security
checks to its methods, as follows.

First, if there is no security manager (

System.getSecurityManager()

is null), then an implementation of
this interface is free not to make any checks.

Assuming that there is a security manager, or that the
implementation chooses to make checks anyway, the checks are made
as detailed below. In what follows, and unless otherwise specified,

className

is the
string returned by

MBeanInfo.getClassName()

for the target
MBean.

If a security check fails, the method throws

SecurityException

.

For methods that can throw

InstanceNotFoundException

,
this exception is thrown for a non-existent MBean, regardless of
permissions. This is because a non-existent MBean has no

className

.

For the

invoke

method, the caller's
permissions must imply

MBeanPermission(className, operationName, name, "invoke")

.

For the

getAttribute

method, the
caller's permissions must imply

MBeanPermission(className, attribute, name, "getAttribute")

.

For the

getAttributes

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "getAttribute")

.
Additionally, for each attribute

a

in the

AttributeList

, if the caller's permissions do not imply

MBeanPermission(className,

a

, name, "getAttribute")

, the
MBean server will behave as if that attribute had not been in the
supplied list.

For the

setAttribute

method, the
caller's permissions must imply

MBeanPermission(className, attrName, name, "setAttribute")

, where

attrName

is

attribute.getName()

.

For the

setAttributes

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "setAttribute")

.
Additionally, for each attribute

a

in the

AttributeList

, if the caller's permissions do not imply

MBeanPermission(className,

a

, name, "setAttribute")

, the
MBean server will behave as if that attribute had not been in the
supplied list.

For the

addNotificationListener

methods,
the caller's permissions must imply

MBeanPermission(className, null, name,
"addNotificationListener")

.

For the

removeNotificationListener

methods,
the caller's permissions must imply

MBeanPermission(className, null, name,
"removeNotificationListener")

.

For the

getMBeanInfo

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "getMBeanInfo")

.

For the

getObjectInstance

method,
the caller's permissions must imply

MBeanPermission(className, null, name, "getObjectInstance")

.

For the

isInstanceOf

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "isInstanceOf")

.

For the

queryMBeans

method, the
caller's permissions must imply

MBeanPermission(null, null, null, "queryMBeans")

.
Additionally, for each MBean

n

that matches

name

,
if the caller's permissions do not imply

MBeanPermission(className, null,

n

, "queryMBeans")

, the
MBean server will behave as if that MBean did not exist.

Certain query elements perform operations on the MBean server.
If the caller does not have the required permissions for a given
MBean, that MBean will not be included in the result of the query.
The standard query elements that are affected are

Query.attr(String)

,

Query.attr(String,String)

, and

Query.classattr()

.

For the

queryNames

method, the checks
are the same as for

queryMBeans

except that

"queryNames"

is used instead of

"queryMBeans"

in the

MBeanPermission

objects. Note that a

"queryMBeans"

permission implies
the corresponding

"queryNames"

permission.

For the

getDomains

method, the caller's
permissions must imply

MBeanPermission(null, null, null, "getDomains")

. Additionally,
for each domain

d

in the returned array, if the caller's
permissions do not imply

MBeanPermission(null, null, new ObjectName("

d

:x=x"),
"getDomains")

, the domain is eliminated from the array. Here,

x=x

is any

key=value

pair, needed to
satisfy ObjectName's constructor but not otherwise relevant.

For the

getClassLoader

method, the
caller's permissions must imply

MBeanPermission(className, null, loaderName,
"getClassLoader")

.

For the

getClassLoaderFor

method,
the caller's permissions must imply

MBeanPermission(className, null, mbeanName,
"getClassLoaderFor")

.

For the

getClassLoaderRepository

method, the caller's permissions must
imply

MBeanPermission(null, null, null, "getClassLoaderRepository")

.

For the deprecated

deserialize

methods, the
required permissions are the same as for the methods that replace
them.

For the

instantiate

methods, the caller's
permissions must imply

MBeanPermission(className, null, null, "instantiate")

,
where

className

is the name of the class which is to
be instantiated.

For the

registerMBean

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "registerMBean")

.

If the

MBeanPermission

check succeeds, the MBean's
class is validated by checking that its

ProtectionDomain

implies

MBeanTrustPermission("register")

.

Finally, if the

name

argument is null, another

MBeanPermission

check is made using the

ObjectName

returned by

MBeanRegistration.preRegister

.

For the

createMBean

methods, the caller's
permissions must imply the permissions needed by the equivalent

instantiate

followed by

registerMBean

.

For the

unregisterMBean

method,
the caller's permissions must imply

MBeanPermission(className, null, name, "unregisterMBean")

.

For the

invoke

method, the caller's
permissions must imply

MBeanPermission(className, operationName, name, "invoke")

.

For the

getAttribute

method, the
caller's permissions must imply

MBeanPermission(className, attribute, name, "getAttribute")

.

For the

getAttributes

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "getAttribute")

.
Additionally, for each attribute

a

in the

AttributeList

, if the caller's permissions do not imply

MBeanPermission(className,

a

, name, "getAttribute")

, the
MBean server will behave as if that attribute had not been in the
supplied list.

For the

setAttribute

method, the
caller's permissions must imply

MBeanPermission(className, attrName, name, "setAttribute")

, where

attrName

is

attribute.getName()

.

For the

setAttributes

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "setAttribute")

.
Additionally, for each attribute

a

in the

AttributeList

, if the caller's permissions do not imply

MBeanPermission(className,

a

, name, "setAttribute")

, the
MBean server will behave as if that attribute had not been in the
supplied list.

For the

addNotificationListener

methods,
the caller's permissions must imply

MBeanPermission(className, null, name,
"addNotificationListener")

.

For the

removeNotificationListener

methods,
the caller's permissions must imply

MBeanPermission(className, null, name,
"removeNotificationListener")

.

For the

getMBeanInfo

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "getMBeanInfo")

.

For the

getObjectInstance

method,
the caller's permissions must imply

MBeanPermission(className, null, name, "getObjectInstance")

.

For the

isInstanceOf

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "isInstanceOf")

.

For the

queryMBeans

method, the
caller's permissions must imply

MBeanPermission(null, null, null, "queryMBeans")

.
Additionally, for each MBean

n

that matches

name

,
if the caller's permissions do not imply

MBeanPermission(className, null,

n

, "queryMBeans")

, the
MBean server will behave as if that MBean did not exist.

Certain query elements perform operations on the MBean server.
If the caller does not have the required permissions for a given
MBean, that MBean will not be included in the result of the query.
The standard query elements that are affected are

Query.attr(String)

,

Query.attr(String,String)

, and

Query.classattr()

.

For the

queryNames

method, the checks
are the same as for

queryMBeans

except that

"queryNames"

is used instead of

"queryMBeans"

in the

MBeanPermission

objects. Note that a

"queryMBeans"

permission implies
the corresponding

"queryNames"

permission.

For the

getDomains

method, the caller's
permissions must imply

MBeanPermission(null, null, null, "getDomains")

. Additionally,
for each domain

d

in the returned array, if the caller's
permissions do not imply

MBeanPermission(null, null, new ObjectName("

d

:x=x"),
"getDomains")

, the domain is eliminated from the array. Here,

x=x

is any

key=value

pair, needed to
satisfy ObjectName's constructor but not otherwise relevant.

For the

getClassLoader

method, the
caller's permissions must imply

MBeanPermission(className, null, loaderName,
"getClassLoader")

.

For the

getClassLoaderFor

method,
the caller's permissions must imply

MBeanPermission(className, null, mbeanName,
"getClassLoaderFor")

.

For the

getClassLoaderRepository

method, the caller's permissions must
imply

MBeanPermission(null, null, null, "getClassLoaderRepository")

.

For the deprecated

deserialize

methods, the
required permissions are the same as for the methods that replace
them.

For the

instantiate

methods, the caller's
permissions must imply

MBeanPermission(className, null, null, "instantiate")

,
where

className

is the name of the class which is to
be instantiated.

For the

registerMBean

method, the
caller's permissions must imply

MBeanPermission(className, null, name, "registerMBean")

.

If the

MBeanPermission

check succeeds, the MBean's
class is validated by checking that its

ProtectionDomain

implies

MBeanTrustPermission("register")

.

Finally, if the

name

argument is null, another

MBeanPermission

check is made using the

ObjectName

returned by

MBeanRegistration.preRegister

.

For the

createMBean

methods, the caller's
permissions must imply the permissions needed by the equivalent

instantiate

followed by

registerMBean

.

For the

unregisterMBean

method,
the caller's permissions must imply

MBeanPermission(className, null, name, "unregisterMBean")

.

If the

MBeanPermission

check succeeds, the MBean's
class is validated by checking that its

ProtectionDomain

implies

MBeanTrustPermission("register")

.

Finally, if the

name

argument is null, another

MBeanPermission

check is made using the

ObjectName

returned by

MBeanRegistration.preRegister

.

For the

createMBean

methods, the caller's
permissions must imply the permissions needed by the equivalent

instantiate

followed by

registerMBean

.

For the

unregisterMBean

method,
the caller's permissions must imply

MBeanPermission(className, null, name, "unregisterMBean")

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addNotificationListener

​(

ObjectName

name,

NotificationListener

listener,

NotificationFilter

filter,

Object

handback)

Adds a listener to a registered MBean.

void

addNotificationListener

​(

ObjectName

name,

ObjectName

listener,

NotificationFilter

filter,

Object

handback)

Adds a listener to a registered MBean.

ObjectInstance

createMBean

​(

String

className,

ObjectName

name)

Instantiates and registers an MBean in the MBean server.

ObjectInstance

createMBean

​(

String

className,

ObjectName

name,

Object

[] params,

String

[] signature)

Instantiates and registers an MBean in the MBean server.

ObjectInstance

createMBean

​(

String

className,

ObjectName

name,

ObjectName

loaderName)

Instantiates and registers an MBean in the MBean server.

ObjectInstance

createMBean

​(

String

className,

ObjectName

name,

ObjectName

loaderName,

Object

[] params,

String

[] signature)

Instantiates and registers an MBean in the MBean server.

default

ObjectInputStream

deserialize

​(

String

className,
byte[] data)

Deprecated.

Use

getClassLoaderRepository()

to obtain the
class loader repository and use it to deserialize.

default

ObjectInputStream

deserialize

​(

String

className,

ObjectName

loaderName,
byte[] data)

Deprecated.

Use

getClassLoader

to obtain
the class loader for deserialization.

default

ObjectInputStream

deserialize

​(

ObjectName

name,
byte[] data)

Deprecated.

Use

getClassLoaderFor

to
obtain the appropriate class loader for deserialization.

Object

getAttribute

​(

ObjectName

name,

String

attribute)

Gets the value of a specific attribute of a named MBean.

AttributeList

getAttributes

​(

ObjectName

name,

String

[] attributes)

Retrieves the values of several attributes of a named MBean.

ClassLoader

getClassLoader

​(

ObjectName

loaderName)

Return the named

ClassLoader

.

ClassLoader

getClassLoaderFor

​(

ObjectName

mbeanName)

Return the

ClassLoader

that was used for
loading the class of the named MBean.

ClassLoaderRepository

getClassLoaderRepository

()

Return the ClassLoaderRepository for this MBeanServer.

Integer

getMBeanCount

()

Returns the number of MBeans registered in the MBean server.

Object

instantiate

​(

String

className)

Instantiates an object using the list of all class loaders
registered in the MBean server's

Class Loader
Repository

.

Object

instantiate

​(

String

className,

Object

[] params,

String

[] signature)

Instantiates an object using the list of all class loaders
registered in the MBean server

Class Loader
Repository

.

Object

instantiate

​(

String

className,

ObjectName

loaderName)

Instantiates an object using the class Loader specified by its

ObjectName

.

Object

instantiate

​(

String

className,

ObjectName

loaderName,

Object

[] params,

String

[] signature)

Instantiates an object.

boolean

isRegistered

​(

ObjectName

name)

Checks whether an MBean, identified by its object name, is
already registered with the MBean server.

Set

<

ObjectInstance

>

queryMBeans

​(

ObjectName

name,

QueryExp

query)

Gets MBeans controlled by the MBean server.

Set

<

ObjectName

>

queryNames

​(

ObjectName

name,

QueryExp

query)

Gets the names of MBeans controlled by the MBean server.

ObjectInstance

registerMBean

​(

Object

object,

ObjectName

name)

Registers a pre-existing object as an MBean with the MBean
server.

void

setAttribute

​(

ObjectName

name,

Attribute

attribute)

Sets the value of a specific attribute of a named MBean.

AttributeList

setAttributes

​(

ObjectName

name,

AttributeList

attributes)

Sets the values of several attributes of a named MBean.

void

unregisterMBean

​(

ObjectName

name)

Unregisters an MBean from the MBean server.

- Methods declared in interface javax.management.

MBeanServerConnection

getDefaultDomain

,

getDomains

,

getMBeanInfo

,

getObjectInstance

,

invoke

,

isInstanceOf

,

removeNotificationListener

,

removeNotificationListener

,

removeNotificationListener

,

removeNotificationListener

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addNotificationListener

​(

ObjectName

name,

NotificationListener

listener,

NotificationFilter

filter,

Object

handback)

Adds a listener to a registered MBean.

void

addNotificationListener

​(

ObjectName

name,

ObjectName

listener,

NotificationFilter

filter,

Object

handback)

Adds a listener to a registered MBean.

ObjectInstance

createMBean

​(

String

className,

ObjectName

name)

Instantiates and registers an MBean in the MBean server.

ObjectInstance

createMBean

​(

String

className,

ObjectName

name,

Object

[] params,

String

[] signature)

Instantiates and registers an MBean in the MBean server.

ObjectInstance

createMBean

​(

String

className,

ObjectName

name,

ObjectName

loaderName)

Instantiates and registers an MBean in the MBean server.

ObjectInstance

createMBean

​(

String

className,

ObjectName

name,

ObjectName

loaderName,

Object

[] params,

String

[] signature)

Instantiates and registers an MBean in the MBean server.

default

ObjectInputStream

deserialize

​(

String

className,
byte[] data)

Deprecated.

Use

getClassLoaderRepository()

to obtain the
class loader repository and use it to deserialize.

default

ObjectInputStream

deserialize

​(

String

className,

ObjectName

loaderName,
byte[] data)

Deprecated.

Use

getClassLoader

to obtain
the class loader for deserialization.

default

ObjectInputStream

deserialize

​(

ObjectName

name,
byte[] data)

Deprecated.

Use

getClassLoaderFor

to
obtain the appropriate class loader for deserialization.

Object

getAttribute

​(

ObjectName

name,

String

attribute)

Gets the value of a specific attribute of a named MBean.

AttributeList

getAttributes

​(

ObjectName

name,

String

[] attributes)

Retrieves the values of several attributes of a named MBean.

ClassLoader

getClassLoader

​(

ObjectName

loaderName)

Return the named

ClassLoader

.

ClassLoader

getClassLoaderFor

​(

ObjectName

mbeanName)

Return the

ClassLoader

that was used for
loading the class of the named MBean.

ClassLoaderRepository

getClassLoaderRepository

()

Return the ClassLoaderRepository for this MBeanServer.

Integer

getMBeanCount

()

Returns the number of MBeans registered in the MBean server.

Object

instantiate

​(

String

className)

Instantiates an object using the list of all class loaders
registered in the MBean server's

Class Loader
Repository

.

Object

instantiate

​(

String

className,

Object

[] params,

String

[] signature)

Instantiates an object using the list of all class loaders
registered in the MBean server

Class Loader
Repository

.

Object

instantiate

​(

String

className,

ObjectName

loaderName)

Instantiates an object using the class Loader specified by its

ObjectName

.

Object

instantiate

​(

String

className,

ObjectName

loaderName,

Object

[] params,

String

[] signature)

Instantiates an object.

boolean

isRegistered

​(

ObjectName

name)

Checks whether an MBean, identified by its object name, is
already registered with the MBean server.

Set

<

ObjectInstance

>

queryMBeans

​(

ObjectName

name,

QueryExp

query)

Gets MBeans controlled by the MBean server.

Set

<

ObjectName

>

queryNames

​(

ObjectName

name,

QueryExp

query)

Gets the names of MBeans controlled by the MBean server.

ObjectInstance

registerMBean

​(

Object

object,

ObjectName

name)

Registers a pre-existing object as an MBean with the MBean
server.

void

setAttribute

​(

ObjectName

name,

Attribute

attribute)

Sets the value of a specific attribute of a named MBean.

AttributeList

setAttributes

​(

ObjectName

name,

AttributeList

attributes)

Sets the values of several attributes of a named MBean.

void

unregisterMBean

​(

ObjectName

name)

Unregisters an MBean from the MBean server.

- Methods declared in interface javax.management.

MBeanServerConnection

getDefaultDomain

,

getDomains

,

getMBeanInfo

,

getObjectInstance

,

invoke

,

isInstanceOf

,

removeNotificationListener

,

removeNotificationListener

,

removeNotificationListener

,

removeNotificationListener

---

#### Method Summary

Adds a listener to a registered MBean.

Instantiates and registers an MBean in the MBean server.

Deprecated.

Use

getClassLoaderRepository()

to obtain the
class loader repository and use it to deserialize.

Deprecated.

Use

getClassLoader

to obtain
the class loader for deserialization.

Deprecated.

Use

getClassLoaderFor

to
obtain the appropriate class loader for deserialization.

Gets the value of a specific attribute of a named MBean.

Retrieves the values of several attributes of a named MBean.

Return the named

ClassLoader

.

Return the

ClassLoader

that was used for
loading the class of the named MBean.

Return the ClassLoaderRepository for this MBeanServer.

Returns the number of MBeans registered in the MBean server.

Instantiates an object using the list of all class loaders
registered in the MBean server's

Class Loader
Repository

.

Instantiates an object using the list of all class loaders
registered in the MBean server

Class Loader
Repository

.

Instantiates an object using the class Loader specified by its

ObjectName

.

Instantiates an object.

Checks whether an MBean, identified by its object name, is
already registered with the MBean server.

Gets MBeans controlled by the MBean server.

Gets the names of MBeans controlled by the MBean server.

Registers a pre-existing object as an MBean with the MBean
server.

Sets the value of a specific attribute of a named MBean.

Sets the values of several attributes of a named MBean.

Unregisters an MBean from the MBean server.

Methods declared in interface javax.management.

MBeanServerConnection

getDefaultDomain

,

getDomains

,

getMBeanInfo

,

getObjectInstance

,

invoke

,

isInstanceOf

,

removeNotificationListener

,

removeNotificationListener

,

removeNotificationListener

,

removeNotificationListener

---

#### Methods declared in interface javax.management. MBeanServerConnection

============ METHOD DETAIL ==========

- Method Detail

- createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name)
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
```

Instantiates and registers an MBean in the MBean server. The
MBean server will use its

Default Loader
Repository

to load the class of the MBean. An object name is
associated with the MBean. If the object name given is null, the
MBean must provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

This method is equivalent to

createMBean(className, name, (Object[]) null, (String[])
null)

.

If this method successfully creates an MBean, a notification
is sent as described

above

.

**Specified by:** createMBean

in interface

MBeanServerConnection
**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
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
**Throws:** RuntimeMBeanException

- If the MBean's constructor or its

preRegister

or

postRegister

method threw
a

RuntimeException

. If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

createMBean

method will
throw a

RuntimeMBeanException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** RuntimeErrorException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

createMBean

method will
throw a

RuntimeErrorException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
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
thrown an exception
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean
**See Also:** MBeanRegistration

- createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name,

ObjectName
loaderName)
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
```

Instantiates and registers an MBean in the MBean server. The
class loader to be used is identified by its object name. An
object name is associated with the MBean. If the object name of
the loader is null, the ClassLoader that loaded the MBean
server will be used. If the MBean's object name given is null,
the MBean must provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

This method is equivalent to

createMBean(className, name, loaderName, (Object[]) null,
(String[]) null)

.

If this method successfully creates an MBean, a notification
is sent as described

above

.

**Specified by:** createMBean

in interface

MBeanServerConnection
**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** loaderName

- The object name of the class loader to be used.
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
**Throws:** RuntimeMBeanException

- If the MBean's constructor or its

preRegister

or

postRegister

method threw
a

RuntimeException

. If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

createMBean

method will
throw a

RuntimeMBeanException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** RuntimeErrorException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

createMBean

method will
throw a

RuntimeErrorException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
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
thrown an exception
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
**See Also:** MBeanRegistration

- createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name,

Object
[] params,

String
[] signature)
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
```

Instantiates and registers an MBean in the MBean server. The
MBean server will use its

Default Loader
Repository

to load the class of the MBean. An object name is
associated with the MBean. If the object name given is null, the
MBean must provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

If this method successfully creates an MBean, a notification
is sent as described

above

.

**Specified by:** createMBean

in interface

MBeanServerConnection
**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked.
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
**Throws:** RuntimeMBeanException

- If the MBean's constructor or its

preRegister

or

postRegister

method threw
a

RuntimeException

. If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

createMBean

method will
throw a

RuntimeMBeanException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** RuntimeErrorException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

createMBean

method will
throw a

RuntimeErrorException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
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
thrown an exception
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean
**See Also:** MBeanRegistration

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

Object
[] params,

String
[] signature)
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
```

Instantiates and registers an MBean in the MBean server. The
class loader to be used is identified by its object name. An
object name is associated with the MBean. If the object name of
the loader is not specified, the ClassLoader that loaded the
MBean server will be used. If the MBean object name given is
null, the MBean must provide its own name by implementing the

MBeanRegistration

interface and returning the name from the

preRegister

method.

If this method successfully creates an MBean, a notification
is sent as described

above

.

**Specified by:** createMBean

in interface

MBeanServerConnection
**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** loaderName

- The object name of the class loader to be used.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked.
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
**Throws:** RuntimeMBeanException

- The MBean's constructor or its

preRegister

or

postRegister

method threw
a

RuntimeException

. If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

createMBean

method will
throw a

RuntimeMBeanException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** RuntimeErrorException

- If the

postRegister

method
(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

createMBean

method will
throw a

RuntimeErrorException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
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
thrown an exception
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
**See Also:** MBeanRegistration

- registerMBean

```java
ObjectInstance
registerMBean​(
Object
object,

ObjectName
name)
throws
InstanceAlreadyExistsException
,

MBeanRegistrationException
,

NotCompliantMBeanException
```

Registers a pre-existing object as an MBean with the MBean
server. If the object name given is null, the MBean must
provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

If this method successfully registers an MBean, a notification
is sent as described

above

.

**Parameters:** object

- The MBean to be registered as an MBean.
**Parameters:** name

- The object name of the MBean. May be null.
**Returns:** An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
registered MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.
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
**Throws:** RuntimeMBeanException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

registerMBean

method will
throw a

RuntimeMBeanException

, although the MBean
registration succeeded. In such a case, the MBean will be actually
registered even though the

registerMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** RuntimeErrorException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

registerMBean

method will
throw a

RuntimeErrorException

, although the MBean
registration succeeded. In such a case, the MBean will be actually
registered even though the

registerMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** NotCompliantMBeanException

- This object is not a JMX
compliant MBean
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
passed in parameter is null or no object name is specified.
**See Also:** MBeanRegistration

- unregisterMBean

```java
void unregisterMBean​(
ObjectName
name)
throws
InstanceNotFoundException
,

MBeanRegistrationException
```

Unregisters an MBean from the MBean server. The MBean is
identified by its object name. Once the method has been
invoked, the MBean may no longer be accessed by its object
name.

If this method successfully unregisters an MBean, a notification
is sent as described

above

.

**Specified by:** unregisterMBean

in interface

MBeanServerConnection
**Parameters:** name

- The object name of the MBean to be unregistered.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the MBean you are when trying to
unregister is the

MBeanServerDelegate

MBean.
**Throws:** RuntimeMBeanException

- If the

postDeregister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

unregisterMBean

method
will throw a

RuntimeMBeanException

, although the MBean
unregistration succeeded. In such a case, the MBean will be actually
unregistered even though the

unregisterMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preDeregister

, in which case the MBean
will remain registered.
**Throws:** RuntimeErrorException

- If the

postDeregister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

unregisterMBean

method will
throw a

RuntimeErrorException

, although the MBean
unregistration succeeded. In such a case, the MBean will be actually
unregistered even though the

unregisterMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preDeregister

, in which case the MBean
will remain registered.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** MBeanRegistrationException

- The preDeregister
((

MBeanRegistration

interface) method of the MBean
has thrown an exception.
**See Also:** MBeanRegistration

- queryMBeans

```java
Set
<
ObjectInstance
> queryMBeans​(
ObjectName
name,

QueryExp
query)
```

Gets MBeans controlled by the MBean server. This method allows
any of the following to be obtained: All MBeans, a set of
MBeans specified by pattern matching on the

ObjectName

and/or a Query expression, a specific
MBean. When the object name is null or no domain and key
properties are specified, all objects are to be selected (and
filtered if a query is specified). It returns the set of

ObjectInstance

objects (containing the

ObjectName

and the Java Class name) for the
selected MBeans.

**Specified by:** queryMBeans

in interface

MBeanServerConnection
**Parameters:** name

- The object name pattern identifying the MBeans to
be retrieved. If null or no domain and key properties are
specified, all the MBeans registered will be retrieved.
**Parameters:** query

- The query expression to be applied for selecting
MBeans. If null no query expression will be applied for
selecting MBeans.
**Returns:** A set containing the

ObjectInstance

objects for the selected MBeans. If no MBean satisfies the
query an empty list is returned.
**Throws:** RuntimeOperationsException

- queryNames

```java
Set
<
ObjectName
> queryNames​(
ObjectName
name,

QueryExp
query)
```

Gets the names of MBeans controlled by the MBean server. This
method enables any of the following to be obtained: The names
of all MBeans, the names of a set of MBeans specified by
pattern matching on the

ObjectName

and/or a Query
expression, a specific MBean name (equivalent to testing
whether an MBean is registered). When the object name is null
or no domain and key properties are specified, all objects are
selected (and filtered if a query is specified). It returns the
set of ObjectNames for the MBeans selected.

**Specified by:** queryNames

in interface

MBeanServerConnection
**Parameters:** name

- The object name pattern identifying the MBean names
to be retrieved. If null or no domain and key properties are
specified, the name of all registered MBeans will be retrieved.
**Parameters:** query

- The query expression to be applied for selecting
MBeans. If null no query expression will be applied for
selecting MBeans.
**Returns:** A set containing the ObjectNames for the MBeans
selected. If no MBean satisfies the query, an empty list is
returned.
**Throws:** RuntimeOperationsException

- isRegistered

```java
boolean isRegistered​(
ObjectName
name)
```

Description copied from interface:

MBeanServerConnection

Checks whether an MBean, identified by its object name, is
already registered with the MBean server.

**Specified by:** isRegistered

in interface

MBeanServerConnection
**Parameters:** name

- The object name of the MBean to be checked.
**Returns:** True if the MBean is already registered in the MBean
server, false otherwise.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.

- getMBeanCount

```java
Integer
getMBeanCount()
```

Returns the number of MBeans registered in the MBean server.

**Specified by:** getMBeanCount

in interface

MBeanServerConnection
**Returns:** the number of registered MBeans, wrapped in an Integer.
If the caller's permissions are restricted, this number may
be greater than the number of MBeans the caller can access.

- getAttribute

```java
Object
getAttribute​(
ObjectName
name,

String
attribute)
throws
MBeanException
,

AttributeNotFoundException
,

InstanceNotFoundException
,

ReflectionException
```

Description copied from interface:

MBeanServerConnection

Gets the value of a specific attribute of a named MBean. The MBean
is identified by its object name.

**Specified by:** getAttribute

in interface

MBeanServerConnection
**Parameters:** name

- The object name of the MBean from which the
attribute is to be retrieved.
**Parameters:** attribute

- A String specifying the name of the attribute
to be retrieved.
**Returns:** The value of the retrieved attribute.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the attribute in parameter is
null.
**Throws:** MBeanException

- Wraps an exception thrown by the
MBean's getter.
**Throws:** AttributeNotFoundException

- The attribute specified
is not accessible in the MBean.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown when trying to invoke
the setter.
**See Also:** MBeanServerConnection.setAttribute(javax.management.ObjectName, javax.management.Attribute)

- getAttributes

```java
AttributeList
getAttributes​(
ObjectName
name,

String
[] attributes)
throws
InstanceNotFoundException
,

ReflectionException
```

Description copied from interface:

MBeanServerConnection

Retrieves the values of several attributes of a named MBean. The MBean
is identified by its object name.

If one or more attributes cannot be retrieved for some reason, they
will be omitted from the returned

AttributeList

. The caller
should check that the list is the same size as the

attributes

array. To discover what problem prevented a given attribute from being
retrieved, call

getAttribute

for that attribute.

Here is an example of calling this method and checking that it
succeeded in retrieving all the requested attributes:

```java
String[] attrNames = ...;
AttributeList list = mbeanServerConnection.getAttributes(objectName, attrNames);
if (list.size() == attrNames.length)
System.out.println("All attributes were retrieved successfully");
else {

List<String>
missing = new
ArrayList<String>
(
Arrays.asList
(attrNames));
for (Attribute a : list.asList())
missing.remove(a.getName());
System.out.println("Did not retrieve: " + missing);
}
```

**Specified by:** getAttributes

in interface

MBeanServerConnection
**Parameters:** name

- The object name of the MBean from which the
attributes are retrieved.
**Parameters:** attributes

- A list of the attributes to be retrieved.
**Returns:** The list of the retrieved attributes.
**Throws:** RuntimeOperationsException

- Wrap a

java.lang.IllegalArgumentException

: The object
name in parameter is null or attributes in parameter is null.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- An exception occurred when
trying to invoke the getAttributes method of a Dynamic MBean.
**See Also:** MBeanServerConnection.setAttributes(javax.management.ObjectName, javax.management.AttributeList)

- setAttribute

```java
void setAttribute​(
ObjectName
name,

Attribute
attribute)
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
```

Description copied from interface:

MBeanServerConnection

Sets the value of a specific attribute of a named MBean. The MBean
is identified by its object name.

**Specified by:** setAttribute

in interface

MBeanServerConnection
**Parameters:** name

- The name of the MBean within which the attribute is
to be set.
**Parameters:** attribute

- The identification of the attribute to be set
and the value it is to be set to.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the attribute in parameter is
null.
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
**See Also:** MBeanServerConnection.getAttribute(javax.management.ObjectName, java.lang.String)

- setAttributes

```java
AttributeList
setAttributes​(
ObjectName
name,

AttributeList
attributes)
throws
InstanceNotFoundException
,

ReflectionException
```

Description copied from interface:

MBeanServerConnection

Sets the values of several attributes of a named MBean. The MBean is
identified by its object name.

If one or more attributes cannot be set for some reason, they will be
omitted from the returned

AttributeList

. The caller should check
that the input

AttributeList

is the same size as the output one.
To discover what problem prevented a given attribute from being retrieved,
it will usually be possible to call

setAttribute

for that attribute, although this is not guaranteed to work. (For
example, the values of two attributes may have been rejected because
they were inconsistent with each other. Setting one of them alone might
be allowed.)

Here is an example of calling this method and checking that it
succeeded in setting all the requested attributes:

```java
AttributeList inputAttrs = ...;
AttributeList outputAttrs = mbeanServerConnection.setAttributes(
objectName, inputAttrs);
if (inputAttrs.size() == outputAttrs.size())
System.out.println("All attributes were set successfully");
else {

List<String>
missing = new
ArrayList<String>
();
for (Attribute a : inputAttrs.asList())
missing.add(a.getName());
for (Attribute a : outputAttrs.asList())
missing.remove(a.getName());
System.out.println("Did not set: " + missing);
}
```

**Specified by:** setAttributes

in interface

MBeanServerConnection
**Parameters:** name

- The object name of the MBean within which the
attributes are to be set.
**Parameters:** attributes

- A list of attributes: The identification of
the attributes to be set and the values they are to be set to.
**Returns:** The list of attributes that were set, with their new
values.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or attributes in parameter is null.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- An exception occurred when
trying to invoke the getAttributes method of a Dynamic MBean.
**See Also:** MBeanServerConnection.getAttributes(javax.management.ObjectName, java.lang.String[])

- addNotificationListener

```java
void addNotificationListener​(
ObjectName
name,

NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
throws
InstanceNotFoundException
```

Adds a listener to a registered MBean.
Notifications emitted by the MBean will be forwarded to the listener.

If the source of the notification
is a reference to an MBean object, the MBean server will replace it
by that MBean's ObjectName. Otherwise the source is unchanged.

**Specified by:** addNotificationListener

in interface

MBeanServerConnection
**Parameters:** name

- The name of the MBean on which the listener should
be added.
**Parameters:** listener

- The listener object which will handle the
notifications emitted by the registered MBean.
**Parameters:** filter

- The filter object. If filter is null, no
filtering will be performed before handling notifications.
**Parameters:** handback

- The context to be sent to the listener when a
notification is emitted.
**Throws:** InstanceNotFoundException

- The MBean name provided
does not match any of the registered MBeans.
**See Also:** MBeanServerConnection.removeNotificationListener(ObjectName, NotificationListener)

,

MBeanServerConnection.removeNotificationListener(ObjectName, NotificationListener,
NotificationFilter, Object)

- addNotificationListener

```java
void addNotificationListener​(
ObjectName
name,

ObjectName
listener,

NotificationFilter
filter,

Object
handback)
throws
InstanceNotFoundException
```

Adds a listener to a registered MBean.

A notification emitted by an MBean will be forwarded by the
MBeanServer to the listener. If the source of the notification
is a reference to an MBean object, the MBean server will
replace it by that MBean's ObjectName. Otherwise the source is
unchanged.

The listener object that receives notifications is the one
that is registered with the given name at the time this method
is called. Even if it is subsequently unregistered, it will
continue to receive notifications.

**Specified by:** addNotificationListener

in interface

MBeanServerConnection
**Parameters:** name

- The name of the MBean on which the listener should
be added.
**Parameters:** listener

- The object name of the listener which will
handle the notifications emitted by the registered MBean.
**Parameters:** filter

- The filter object. If filter is null, no
filtering will be performed before handling notifications.
**Parameters:** handback

- The context to be sent to the listener when a
notification is emitted.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

. The MBean named by

listener

exists but does not implement the

NotificationListener

interface.
**Throws:** InstanceNotFoundException

- The MBean name of the
notification listener or of the notification broadcaster does
not match any of the registered MBeans.
**See Also:** MBeanServerConnection.removeNotificationListener(ObjectName, ObjectName)

,

MBeanServerConnection.removeNotificationListener(ObjectName, ObjectName,
NotificationFilter, Object)

- instantiate

```java
Object
instantiate​(
String
className)
throws
ReflectionException
,

MBeanException
```

Instantiates an object using the list of all class loaders
registered in the MBean server's

Class Loader
Repository

. The object's class should have a public
constructor. This method returns a reference to the newly
created object. The newly created object is not registered in
the MBean server.

This method is equivalent to

instantiate(className, (Object[]) null, (String[]) null)

.

**Parameters:** className

- The class name of the object to be instantiated.
**Returns:** The newly instantiated object.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or the

java.lang.Exception

that occurred when trying to
invoke the object's constructor.
**Throws:** MBeanException

- The constructor of the object has
thrown an exception
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null.

- instantiate

```java
Object
instantiate​(
String
className,

ObjectName
loaderName)
throws
ReflectionException
,

MBeanException
,

InstanceNotFoundException
```

Instantiates an object using the class Loader specified by its

ObjectName

. If the loader name is null, the
ClassLoader that loaded the MBean Server will be used. The
object's class should have a public constructor. This method
returns a reference to the newly created object. The newly
created object is not registered in the MBean server.

This method is equivalent to

instantiate(className, loaderName, (Object[]) null, (String[])
null)

.

**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** loaderName

- The object name of the class loader to be used.
**Returns:** The newly instantiated object.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or the

java.lang.Exception

that occurred when trying to
invoke the object's constructor.
**Throws:** MBeanException

- The constructor of the object has
thrown an exception.
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBeanServer.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null.

- instantiate

```java
Object
instantiate​(
String
className,

Object
[] params,

String
[] signature)
throws
ReflectionException
,

MBeanException
```

Instantiates an object using the list of all class loaders
registered in the MBean server

Class Loader
Repository

. The object's class should have a public
constructor. The call returns a reference to the newly created
object. The newly created object is not registered in the
MBean server.

**Parameters:** className

- The class name of the object to be instantiated.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked.
**Returns:** The newly instantiated object.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or the

java.lang.Exception

that occurred when trying to
invoke the object's constructor.
**Throws:** MBeanException

- The constructor of the object has
thrown an exception
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null.

- instantiate

```java
Object
instantiate​(
String
className,

ObjectName
loaderName,

Object
[] params,

String
[] signature)
throws
ReflectionException
,

MBeanException
,

InstanceNotFoundException
```

Instantiates an object. The class loader to be used is
identified by its object name. If the object name of the loader
is null, the ClassLoader that loaded the MBean server will be
used. The object's class should have a public constructor.
The call returns a reference to the newly created object. The
newly created object is not registered in the MBean server.

**Parameters:** className

- The class name of the object to be instantiated.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked.
**Parameters:** loaderName

- The object name of the class loader to be used.
**Returns:** The newly instantiated object.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or the

java.lang.Exception

that
occurred when trying to invoke the object's constructor.
**Throws:** MBeanException

- The constructor of the object has
thrown an exception
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null.

- deserialize

```java
@Deprecated
(
since
="1.5")
default
ObjectInputStream
deserialize​(
ObjectName
name,
byte[] data)
throws
InstanceNotFoundException
,

OperationsException
```

Deprecated.

Use

getClassLoaderFor

to
obtain the appropriate class loader for deserialization.

De-serializes a byte array in the context of the class loader
of an MBean.

**Implementation Requirements:** This method throws

UnsupportedOperationException

by default.
**Parameters:** name

- The name of the MBean whose class loader should be
used for the de-serialization.
**Parameters:** data

- The byte array to be de-sererialized.
**Returns:** The de-serialized object stream.
**Throws:** InstanceNotFoundException

- The MBean specified is not
found.
**Throws:** OperationsException

- Any of the usual Input/Output
related exceptions.

- deserialize

```java
@Deprecated
(
since
="1.5")
default
ObjectInputStream
deserialize​(
String
className,
byte[] data)
throws
OperationsException
,

ReflectionException
```

Deprecated.

Use

getClassLoaderRepository()

to obtain the
class loader repository and use it to deserialize.

De-serializes a byte array in the context of a given MBean
class loader. The class loader is found by loading the class

className

through the

Class Loader
Repository

. The resultant class's class loader is the one to
use.

**Implementation Requirements:** This method throws

UnsupportedOperationException

by default.
**Parameters:** className

- The name of the class whose class loader should be
used for the de-serialization.
**Parameters:** data

- The byte array to be de-sererialized.
**Returns:** The de-serialized object stream.
**Throws:** OperationsException

- Any of the usual Input/Output
related exceptions.
**Throws:** ReflectionException

- The specified class could not be
loaded by the class loader repository

- deserialize

```java
@Deprecated
(
since
="1.5")
default
ObjectInputStream
deserialize​(
String
className,

ObjectName
loaderName,
byte[] data)
throws
InstanceNotFoundException
,

OperationsException
,

ReflectionException
```

Deprecated.

Use

getClassLoader

to obtain
the class loader for deserialization.

De-serializes a byte array in the context of a given MBean
class loader. The class loader is the one that loaded the
class with name "className". The name of the class loader to
be used for loading the specified class is specified. If null,
the MBean Server's class loader will be used.

**Implementation Requirements:** This method throws

UnsupportedOperationException

by default.
**Parameters:** className

- The name of the class whose class loader should be
used for the de-serialization.
**Parameters:** data

- The byte array to be de-sererialized.
**Parameters:** loaderName

- The name of the class loader to be used for
loading the specified class. If null, the MBean Server's class
loader will be used.
**Returns:** The de-serialized object stream.
**Throws:** InstanceNotFoundException

- The specified class loader
MBean is not found.
**Throws:** OperationsException

- Any of the usual Input/Output
related exceptions.
**Throws:** ReflectionException

- The specified class could not be
loaded by the specified class loader.

- getClassLoaderFor

```java
ClassLoader
getClassLoaderFor​(
ObjectName
mbeanName)
throws
InstanceNotFoundException
```

Return the

ClassLoader

that was used for
loading the class of the named MBean.

**Parameters:** mbeanName

- The ObjectName of the MBean.
**Returns:** The ClassLoader used for that MBean. If

l

is the MBean's actual ClassLoader, and

r

is the
returned value, then either:

- r

is identical to

l

; or

the result of

r

.loadClass(

s

)

is the
same as

l

.loadClass(

s

)

for any string

s

.

What this means is that the ClassLoader may be wrapped in
another ClassLoader for security or other reasons.
**Throws:** InstanceNotFoundException

- if the named MBean is not found.

- getClassLoader

```java
ClassLoader
getClassLoader​(
ObjectName
loaderName)
throws
InstanceNotFoundException
```

Return the named

ClassLoader

.

**Parameters:** loaderName

- The ObjectName of the ClassLoader. May be
null, in which case the MBean server's own ClassLoader is
returned.
**Returns:** The named ClassLoader. If

l

is the actual
ClassLoader with that name, and

r

is the returned
value, then either:

- r

is identical to

l

; or

the result of

r

.loadClass(

s

)

is the
same as

l

.loadClass(

s

)

for any string

s

.

What this means is that the ClassLoader may be wrapped in
another ClassLoader for security or other reasons.
**Throws:** InstanceNotFoundException

- if the named ClassLoader is
not found.

- getClassLoaderRepository

```java
ClassLoaderRepository
getClassLoaderRepository()
```

Return the ClassLoaderRepository for this MBeanServer.

**Returns:** The ClassLoaderRepository for this MBeanServer.

Method Detail

- createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name)
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
```

Instantiates and registers an MBean in the MBean server. The
MBean server will use its

Default Loader
Repository

to load the class of the MBean. An object name is
associated with the MBean. If the object name given is null, the
MBean must provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

This method is equivalent to

createMBean(className, name, (Object[]) null, (String[])
null)

.

If this method successfully creates an MBean, a notification
is sent as described

above

.

**Specified by:** createMBean

in interface

MBeanServerConnection
**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
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
**Throws:** RuntimeMBeanException

- If the MBean's constructor or its

preRegister

or

postRegister

method threw
a

RuntimeException

. If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

createMBean

method will
throw a

RuntimeMBeanException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** RuntimeErrorException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

createMBean

method will
throw a

RuntimeErrorException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
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
thrown an exception
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean
**See Also:** MBeanRegistration

- createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name,

ObjectName
loaderName)
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
```

Instantiates and registers an MBean in the MBean server. The
class loader to be used is identified by its object name. An
object name is associated with the MBean. If the object name of
the loader is null, the ClassLoader that loaded the MBean
server will be used. If the MBean's object name given is null,
the MBean must provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

This method is equivalent to

createMBean(className, name, loaderName, (Object[]) null,
(String[]) null)

.

If this method successfully creates an MBean, a notification
is sent as described

above

.

**Specified by:** createMBean

in interface

MBeanServerConnection
**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** loaderName

- The object name of the class loader to be used.
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
**Throws:** RuntimeMBeanException

- If the MBean's constructor or its

preRegister

or

postRegister

method threw
a

RuntimeException

. If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

createMBean

method will
throw a

RuntimeMBeanException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** RuntimeErrorException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

createMBean

method will
throw a

RuntimeErrorException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
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
thrown an exception
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
**See Also:** MBeanRegistration

- createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name,

Object
[] params,

String
[] signature)
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
```

Instantiates and registers an MBean in the MBean server. The
MBean server will use its

Default Loader
Repository

to load the class of the MBean. An object name is
associated with the MBean. If the object name given is null, the
MBean must provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

If this method successfully creates an MBean, a notification
is sent as described

above

.

**Specified by:** createMBean

in interface

MBeanServerConnection
**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked.
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
**Throws:** RuntimeMBeanException

- If the MBean's constructor or its

preRegister

or

postRegister

method threw
a

RuntimeException

. If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

createMBean

method will
throw a

RuntimeMBeanException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** RuntimeErrorException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

createMBean

method will
throw a

RuntimeErrorException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
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
thrown an exception
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean
**See Also:** MBeanRegistration

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

Object
[] params,

String
[] signature)
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
```

Instantiates and registers an MBean in the MBean server. The
class loader to be used is identified by its object name. An
object name is associated with the MBean. If the object name of
the loader is not specified, the ClassLoader that loaded the
MBean server will be used. If the MBean object name given is
null, the MBean must provide its own name by implementing the

MBeanRegistration

interface and returning the name from the

preRegister

method.

If this method successfully creates an MBean, a notification
is sent as described

above

.

**Specified by:** createMBean

in interface

MBeanServerConnection
**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** loaderName

- The object name of the class loader to be used.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked.
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
**Throws:** RuntimeMBeanException

- The MBean's constructor or its

preRegister

or

postRegister

method threw
a

RuntimeException

. If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

createMBean

method will
throw a

RuntimeMBeanException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** RuntimeErrorException

- If the

postRegister

method
(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

createMBean

method will
throw a

RuntimeErrorException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
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
thrown an exception
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
**See Also:** MBeanRegistration

- registerMBean

```java
ObjectInstance
registerMBean​(
Object
object,

ObjectName
name)
throws
InstanceAlreadyExistsException
,

MBeanRegistrationException
,

NotCompliantMBeanException
```

Registers a pre-existing object as an MBean with the MBean
server. If the object name given is null, the MBean must
provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

If this method successfully registers an MBean, a notification
is sent as described

above

.

**Parameters:** object

- The MBean to be registered as an MBean.
**Parameters:** name

- The object name of the MBean. May be null.
**Returns:** An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
registered MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.
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
**Throws:** RuntimeMBeanException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

registerMBean

method will
throw a

RuntimeMBeanException

, although the MBean
registration succeeded. In such a case, the MBean will be actually
registered even though the

registerMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** RuntimeErrorException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

registerMBean

method will
throw a

RuntimeErrorException

, although the MBean
registration succeeded. In such a case, the MBean will be actually
registered even though the

registerMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** NotCompliantMBeanException

- This object is not a JMX
compliant MBean
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
passed in parameter is null or no object name is specified.
**See Also:** MBeanRegistration

- unregisterMBean

```java
void unregisterMBean​(
ObjectName
name)
throws
InstanceNotFoundException
,

MBeanRegistrationException
```

Unregisters an MBean from the MBean server. The MBean is
identified by its object name. Once the method has been
invoked, the MBean may no longer be accessed by its object
name.

If this method successfully unregisters an MBean, a notification
is sent as described

above

.

**Specified by:** unregisterMBean

in interface

MBeanServerConnection
**Parameters:** name

- The object name of the MBean to be unregistered.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the MBean you are when trying to
unregister is the

MBeanServerDelegate

MBean.
**Throws:** RuntimeMBeanException

- If the

postDeregister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

unregisterMBean

method
will throw a

RuntimeMBeanException

, although the MBean
unregistration succeeded. In such a case, the MBean will be actually
unregistered even though the

unregisterMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preDeregister

, in which case the MBean
will remain registered.
**Throws:** RuntimeErrorException

- If the

postDeregister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

unregisterMBean

method will
throw a

RuntimeErrorException

, although the MBean
unregistration succeeded. In such a case, the MBean will be actually
unregistered even though the

unregisterMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preDeregister

, in which case the MBean
will remain registered.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** MBeanRegistrationException

- The preDeregister
((

MBeanRegistration

interface) method of the MBean
has thrown an exception.
**See Also:** MBeanRegistration

- queryMBeans

```java
Set
<
ObjectInstance
> queryMBeans​(
ObjectName
name,

QueryExp
query)
```

Gets MBeans controlled by the MBean server. This method allows
any of the following to be obtained: All MBeans, a set of
MBeans specified by pattern matching on the

ObjectName

and/or a Query expression, a specific
MBean. When the object name is null or no domain and key
properties are specified, all objects are to be selected (and
filtered if a query is specified). It returns the set of

ObjectInstance

objects (containing the

ObjectName

and the Java Class name) for the
selected MBeans.

**Specified by:** queryMBeans

in interface

MBeanServerConnection
**Parameters:** name

- The object name pattern identifying the MBeans to
be retrieved. If null or no domain and key properties are
specified, all the MBeans registered will be retrieved.
**Parameters:** query

- The query expression to be applied for selecting
MBeans. If null no query expression will be applied for
selecting MBeans.
**Returns:** A set containing the

ObjectInstance

objects for the selected MBeans. If no MBean satisfies the
query an empty list is returned.
**Throws:** RuntimeOperationsException

- queryNames

```java
Set
<
ObjectName
> queryNames​(
ObjectName
name,

QueryExp
query)
```

Gets the names of MBeans controlled by the MBean server. This
method enables any of the following to be obtained: The names
of all MBeans, the names of a set of MBeans specified by
pattern matching on the

ObjectName

and/or a Query
expression, a specific MBean name (equivalent to testing
whether an MBean is registered). When the object name is null
or no domain and key properties are specified, all objects are
selected (and filtered if a query is specified). It returns the
set of ObjectNames for the MBeans selected.

**Specified by:** queryNames

in interface

MBeanServerConnection
**Parameters:** name

- The object name pattern identifying the MBean names
to be retrieved. If null or no domain and key properties are
specified, the name of all registered MBeans will be retrieved.
**Parameters:** query

- The query expression to be applied for selecting
MBeans. If null no query expression will be applied for
selecting MBeans.
**Returns:** A set containing the ObjectNames for the MBeans
selected. If no MBean satisfies the query, an empty list is
returned.
**Throws:** RuntimeOperationsException

- isRegistered

```java
boolean isRegistered​(
ObjectName
name)
```

Description copied from interface:

MBeanServerConnection

Checks whether an MBean, identified by its object name, is
already registered with the MBean server.

**Specified by:** isRegistered

in interface

MBeanServerConnection
**Parameters:** name

- The object name of the MBean to be checked.
**Returns:** True if the MBean is already registered in the MBean
server, false otherwise.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.

- getMBeanCount

```java
Integer
getMBeanCount()
```

Returns the number of MBeans registered in the MBean server.

**Specified by:** getMBeanCount

in interface

MBeanServerConnection
**Returns:** the number of registered MBeans, wrapped in an Integer.
If the caller's permissions are restricted, this number may
be greater than the number of MBeans the caller can access.

- getAttribute

```java
Object
getAttribute​(
ObjectName
name,

String
attribute)
throws
MBeanException
,

AttributeNotFoundException
,

InstanceNotFoundException
,

ReflectionException
```

Description copied from interface:

MBeanServerConnection

Gets the value of a specific attribute of a named MBean. The MBean
is identified by its object name.

**Specified by:** getAttribute

in interface

MBeanServerConnection
**Parameters:** name

- The object name of the MBean from which the
attribute is to be retrieved.
**Parameters:** attribute

- A String specifying the name of the attribute
to be retrieved.
**Returns:** The value of the retrieved attribute.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the attribute in parameter is
null.
**Throws:** MBeanException

- Wraps an exception thrown by the
MBean's getter.
**Throws:** AttributeNotFoundException

- The attribute specified
is not accessible in the MBean.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown when trying to invoke
the setter.
**See Also:** MBeanServerConnection.setAttribute(javax.management.ObjectName, javax.management.Attribute)

- getAttributes

```java
AttributeList
getAttributes​(
ObjectName
name,

String
[] attributes)
throws
InstanceNotFoundException
,

ReflectionException
```

Description copied from interface:

MBeanServerConnection

Retrieves the values of several attributes of a named MBean. The MBean
is identified by its object name.

If one or more attributes cannot be retrieved for some reason, they
will be omitted from the returned

AttributeList

. The caller
should check that the list is the same size as the

attributes

array. To discover what problem prevented a given attribute from being
retrieved, call

getAttribute

for that attribute.

Here is an example of calling this method and checking that it
succeeded in retrieving all the requested attributes:

```java
String[] attrNames = ...;
AttributeList list = mbeanServerConnection.getAttributes(objectName, attrNames);
if (list.size() == attrNames.length)
System.out.println("All attributes were retrieved successfully");
else {

List<String>
missing = new
ArrayList<String>
(
Arrays.asList
(attrNames));
for (Attribute a : list.asList())
missing.remove(a.getName());
System.out.println("Did not retrieve: " + missing);
}
```

**Specified by:** getAttributes

in interface

MBeanServerConnection
**Parameters:** name

- The object name of the MBean from which the
attributes are retrieved.
**Parameters:** attributes

- A list of the attributes to be retrieved.
**Returns:** The list of the retrieved attributes.
**Throws:** RuntimeOperationsException

- Wrap a

java.lang.IllegalArgumentException

: The object
name in parameter is null or attributes in parameter is null.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- An exception occurred when
trying to invoke the getAttributes method of a Dynamic MBean.
**See Also:** MBeanServerConnection.setAttributes(javax.management.ObjectName, javax.management.AttributeList)

- setAttribute

```java
void setAttribute​(
ObjectName
name,

Attribute
attribute)
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
```

Description copied from interface:

MBeanServerConnection

Sets the value of a specific attribute of a named MBean. The MBean
is identified by its object name.

**Specified by:** setAttribute

in interface

MBeanServerConnection
**Parameters:** name

- The name of the MBean within which the attribute is
to be set.
**Parameters:** attribute

- The identification of the attribute to be set
and the value it is to be set to.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the attribute in parameter is
null.
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
**See Also:** MBeanServerConnection.getAttribute(javax.management.ObjectName, java.lang.String)

- setAttributes

```java
AttributeList
setAttributes​(
ObjectName
name,

AttributeList
attributes)
throws
InstanceNotFoundException
,

ReflectionException
```

Description copied from interface:

MBeanServerConnection

Sets the values of several attributes of a named MBean. The MBean is
identified by its object name.

If one or more attributes cannot be set for some reason, they will be
omitted from the returned

AttributeList

. The caller should check
that the input

AttributeList

is the same size as the output one.
To discover what problem prevented a given attribute from being retrieved,
it will usually be possible to call

setAttribute

for that attribute, although this is not guaranteed to work. (For
example, the values of two attributes may have been rejected because
they were inconsistent with each other. Setting one of them alone might
be allowed.)

Here is an example of calling this method and checking that it
succeeded in setting all the requested attributes:

```java
AttributeList inputAttrs = ...;
AttributeList outputAttrs = mbeanServerConnection.setAttributes(
objectName, inputAttrs);
if (inputAttrs.size() == outputAttrs.size())
System.out.println("All attributes were set successfully");
else {

List<String>
missing = new
ArrayList<String>
();
for (Attribute a : inputAttrs.asList())
missing.add(a.getName());
for (Attribute a : outputAttrs.asList())
missing.remove(a.getName());
System.out.println("Did not set: " + missing);
}
```

**Specified by:** setAttributes

in interface

MBeanServerConnection
**Parameters:** name

- The object name of the MBean within which the
attributes are to be set.
**Parameters:** attributes

- A list of attributes: The identification of
the attributes to be set and the values they are to be set to.
**Returns:** The list of attributes that were set, with their new
values.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or attributes in parameter is null.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- An exception occurred when
trying to invoke the getAttributes method of a Dynamic MBean.
**See Also:** MBeanServerConnection.getAttributes(javax.management.ObjectName, java.lang.String[])

- addNotificationListener

```java
void addNotificationListener​(
ObjectName
name,

NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
throws
InstanceNotFoundException
```

Adds a listener to a registered MBean.
Notifications emitted by the MBean will be forwarded to the listener.

If the source of the notification
is a reference to an MBean object, the MBean server will replace it
by that MBean's ObjectName. Otherwise the source is unchanged.

**Specified by:** addNotificationListener

in interface

MBeanServerConnection
**Parameters:** name

- The name of the MBean on which the listener should
be added.
**Parameters:** listener

- The listener object which will handle the
notifications emitted by the registered MBean.
**Parameters:** filter

- The filter object. If filter is null, no
filtering will be performed before handling notifications.
**Parameters:** handback

- The context to be sent to the listener when a
notification is emitted.
**Throws:** InstanceNotFoundException

- The MBean name provided
does not match any of the registered MBeans.
**See Also:** MBeanServerConnection.removeNotificationListener(ObjectName, NotificationListener)

,

MBeanServerConnection.removeNotificationListener(ObjectName, NotificationListener,
NotificationFilter, Object)

- addNotificationListener

```java
void addNotificationListener​(
ObjectName
name,

ObjectName
listener,

NotificationFilter
filter,

Object
handback)
throws
InstanceNotFoundException
```

Adds a listener to a registered MBean.

A notification emitted by an MBean will be forwarded by the
MBeanServer to the listener. If the source of the notification
is a reference to an MBean object, the MBean server will
replace it by that MBean's ObjectName. Otherwise the source is
unchanged.

The listener object that receives notifications is the one
that is registered with the given name at the time this method
is called. Even if it is subsequently unregistered, it will
continue to receive notifications.

**Specified by:** addNotificationListener

in interface

MBeanServerConnection
**Parameters:** name

- The name of the MBean on which the listener should
be added.
**Parameters:** listener

- The object name of the listener which will
handle the notifications emitted by the registered MBean.
**Parameters:** filter

- The filter object. If filter is null, no
filtering will be performed before handling notifications.
**Parameters:** handback

- The context to be sent to the listener when a
notification is emitted.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

. The MBean named by

listener

exists but does not implement the

NotificationListener

interface.
**Throws:** InstanceNotFoundException

- The MBean name of the
notification listener or of the notification broadcaster does
not match any of the registered MBeans.
**See Also:** MBeanServerConnection.removeNotificationListener(ObjectName, ObjectName)

,

MBeanServerConnection.removeNotificationListener(ObjectName, ObjectName,
NotificationFilter, Object)

- instantiate

```java
Object
instantiate​(
String
className)
throws
ReflectionException
,

MBeanException
```

Instantiates an object using the list of all class loaders
registered in the MBean server's

Class Loader
Repository

. The object's class should have a public
constructor. This method returns a reference to the newly
created object. The newly created object is not registered in
the MBean server.

This method is equivalent to

instantiate(className, (Object[]) null, (String[]) null)

.

**Parameters:** className

- The class name of the object to be instantiated.
**Returns:** The newly instantiated object.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or the

java.lang.Exception

that occurred when trying to
invoke the object's constructor.
**Throws:** MBeanException

- The constructor of the object has
thrown an exception
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null.

- instantiate

```java
Object
instantiate​(
String
className,

ObjectName
loaderName)
throws
ReflectionException
,

MBeanException
,

InstanceNotFoundException
```

Instantiates an object using the class Loader specified by its

ObjectName

. If the loader name is null, the
ClassLoader that loaded the MBean Server will be used. The
object's class should have a public constructor. This method
returns a reference to the newly created object. The newly
created object is not registered in the MBean server.

This method is equivalent to

instantiate(className, loaderName, (Object[]) null, (String[])
null)

.

**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** loaderName

- The object name of the class loader to be used.
**Returns:** The newly instantiated object.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or the

java.lang.Exception

that occurred when trying to
invoke the object's constructor.
**Throws:** MBeanException

- The constructor of the object has
thrown an exception.
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBeanServer.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null.

- instantiate

```java
Object
instantiate​(
String
className,

Object
[] params,

String
[] signature)
throws
ReflectionException
,

MBeanException
```

Instantiates an object using the list of all class loaders
registered in the MBean server

Class Loader
Repository

. The object's class should have a public
constructor. The call returns a reference to the newly created
object. The newly created object is not registered in the
MBean server.

**Parameters:** className

- The class name of the object to be instantiated.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked.
**Returns:** The newly instantiated object.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or the

java.lang.Exception

that occurred when trying to
invoke the object's constructor.
**Throws:** MBeanException

- The constructor of the object has
thrown an exception
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null.

- instantiate

```java
Object
instantiate​(
String
className,

ObjectName
loaderName,

Object
[] params,

String
[] signature)
throws
ReflectionException
,

MBeanException
,

InstanceNotFoundException
```

Instantiates an object. The class loader to be used is
identified by its object name. If the object name of the loader
is null, the ClassLoader that loaded the MBean server will be
used. The object's class should have a public constructor.
The call returns a reference to the newly created object. The
newly created object is not registered in the MBean server.

**Parameters:** className

- The class name of the object to be instantiated.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked.
**Parameters:** loaderName

- The object name of the class loader to be used.
**Returns:** The newly instantiated object.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or the

java.lang.Exception

that
occurred when trying to invoke the object's constructor.
**Throws:** MBeanException

- The constructor of the object has
thrown an exception
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null.

- deserialize

```java
@Deprecated
(
since
="1.5")
default
ObjectInputStream
deserialize​(
ObjectName
name,
byte[] data)
throws
InstanceNotFoundException
,

OperationsException
```

Deprecated.

Use

getClassLoaderFor

to
obtain the appropriate class loader for deserialization.

De-serializes a byte array in the context of the class loader
of an MBean.

**Implementation Requirements:** This method throws

UnsupportedOperationException

by default.
**Parameters:** name

- The name of the MBean whose class loader should be
used for the de-serialization.
**Parameters:** data

- The byte array to be de-sererialized.
**Returns:** The de-serialized object stream.
**Throws:** InstanceNotFoundException

- The MBean specified is not
found.
**Throws:** OperationsException

- Any of the usual Input/Output
related exceptions.

- deserialize

```java
@Deprecated
(
since
="1.5")
default
ObjectInputStream
deserialize​(
String
className,
byte[] data)
throws
OperationsException
,

ReflectionException
```

Deprecated.

Use

getClassLoaderRepository()

to obtain the
class loader repository and use it to deserialize.

De-serializes a byte array in the context of a given MBean
class loader. The class loader is found by loading the class

className

through the

Class Loader
Repository

. The resultant class's class loader is the one to
use.

**Implementation Requirements:** This method throws

UnsupportedOperationException

by default.
**Parameters:** className

- The name of the class whose class loader should be
used for the de-serialization.
**Parameters:** data

- The byte array to be de-sererialized.
**Returns:** The de-serialized object stream.
**Throws:** OperationsException

- Any of the usual Input/Output
related exceptions.
**Throws:** ReflectionException

- The specified class could not be
loaded by the class loader repository

- deserialize

```java
@Deprecated
(
since
="1.5")
default
ObjectInputStream
deserialize​(
String
className,

ObjectName
loaderName,
byte[] data)
throws
InstanceNotFoundException
,

OperationsException
,

ReflectionException
```

Deprecated.

Use

getClassLoader

to obtain
the class loader for deserialization.

De-serializes a byte array in the context of a given MBean
class loader. The class loader is the one that loaded the
class with name "className". The name of the class loader to
be used for loading the specified class is specified. If null,
the MBean Server's class loader will be used.

**Implementation Requirements:** This method throws

UnsupportedOperationException

by default.
**Parameters:** className

- The name of the class whose class loader should be
used for the de-serialization.
**Parameters:** data

- The byte array to be de-sererialized.
**Parameters:** loaderName

- The name of the class loader to be used for
loading the specified class. If null, the MBean Server's class
loader will be used.
**Returns:** The de-serialized object stream.
**Throws:** InstanceNotFoundException

- The specified class loader
MBean is not found.
**Throws:** OperationsException

- Any of the usual Input/Output
related exceptions.
**Throws:** ReflectionException

- The specified class could not be
loaded by the specified class loader.

- getClassLoaderFor

```java
ClassLoader
getClassLoaderFor​(
ObjectName
mbeanName)
throws
InstanceNotFoundException
```

Return the

ClassLoader

that was used for
loading the class of the named MBean.

**Parameters:** mbeanName

- The ObjectName of the MBean.
**Returns:** The ClassLoader used for that MBean. If

l

is the MBean's actual ClassLoader, and

r

is the
returned value, then either:

- r

is identical to

l

; or

the result of

r

.loadClass(

s

)

is the
same as

l

.loadClass(

s

)

for any string

s

.

What this means is that the ClassLoader may be wrapped in
another ClassLoader for security or other reasons.
**Throws:** InstanceNotFoundException

- if the named MBean is not found.

- getClassLoader

```java
ClassLoader
getClassLoader​(
ObjectName
loaderName)
throws
InstanceNotFoundException
```

Return the named

ClassLoader

.

**Parameters:** loaderName

- The ObjectName of the ClassLoader. May be
null, in which case the MBean server's own ClassLoader is
returned.
**Returns:** The named ClassLoader. If

l

is the actual
ClassLoader with that name, and

r

is the returned
value, then either:

- r

is identical to

l

; or

the result of

r

.loadClass(

s

)

is the
same as

l

.loadClass(

s

)

for any string

s

.

What this means is that the ClassLoader may be wrapped in
another ClassLoader for security or other reasons.
**Throws:** InstanceNotFoundException

- if the named ClassLoader is
not found.

- getClassLoaderRepository

```java
ClassLoaderRepository
getClassLoaderRepository()
```

Return the ClassLoaderRepository for this MBeanServer.

**Returns:** The ClassLoaderRepository for this MBeanServer.

---

#### Method Detail

createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name)
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
```

Instantiates and registers an MBean in the MBean server. The
MBean server will use its

Default Loader
Repository

to load the class of the MBean. An object name is
associated with the MBean. If the object name given is null, the
MBean must provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

This method is equivalent to

createMBean(className, name, (Object[]) null, (String[])
null)

.

If this method successfully creates an MBean, a notification
is sent as described

above

.

**Specified by:** createMBean

in interface

MBeanServerConnection
**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
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
**Throws:** RuntimeMBeanException

- If the MBean's constructor or its

preRegister

or

postRegister

method threw
a

RuntimeException

. If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

createMBean

method will
throw a

RuntimeMBeanException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** RuntimeErrorException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

createMBean

method will
throw a

RuntimeErrorException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
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
thrown an exception
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean
**See Also:** MBeanRegistration

---

#### createMBean

ObjectInstance

createMBean​(

String

className,

ObjectName

name)
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

Instantiates and registers an MBean in the MBean server. The
MBean server will use its

Default Loader
Repository

to load the class of the MBean. An object name is
associated with the MBean. If the object name given is null, the
MBean must provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

This method is equivalent to

createMBean(className, name, (Object[]) null, (String[])
null)

.

If this method successfully creates an MBean, a notification
is sent as described

above

.

Instantiates and registers an MBean in the MBean server. The
MBean server will use its

Default Loader
Repository

to load the class of the MBean. An object name is
associated with the MBean. If the object name given is null, the
MBean must provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

This method is equivalent to

createMBean(className, name, (Object[]) null, (String[])
null)

.

If this method successfully creates an MBean, a notification
is sent as described

above

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
loaderName)
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
```

Instantiates and registers an MBean in the MBean server. The
class loader to be used is identified by its object name. An
object name is associated with the MBean. If the object name of
the loader is null, the ClassLoader that loaded the MBean
server will be used. If the MBean's object name given is null,
the MBean must provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

This method is equivalent to

createMBean(className, name, loaderName, (Object[]) null,
(String[]) null)

.

If this method successfully creates an MBean, a notification
is sent as described

above

.

**Specified by:** createMBean

in interface

MBeanServerConnection
**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** loaderName

- The object name of the class loader to be used.
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
**Throws:** RuntimeMBeanException

- If the MBean's constructor or its

preRegister

or

postRegister

method threw
a

RuntimeException

. If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

createMBean

method will
throw a

RuntimeMBeanException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** RuntimeErrorException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

createMBean

method will
throw a

RuntimeErrorException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
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
thrown an exception
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
**See Also:** MBeanRegistration

---

#### createMBean

ObjectInstance

createMBean​(

String

className,

ObjectName

name,

ObjectName

loaderName)
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

Instantiates and registers an MBean in the MBean server. The
class loader to be used is identified by its object name. An
object name is associated with the MBean. If the object name of
the loader is null, the ClassLoader that loaded the MBean
server will be used. If the MBean's object name given is null,
the MBean must provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

This method is equivalent to

createMBean(className, name, loaderName, (Object[]) null,
(String[]) null)

.

If this method successfully creates an MBean, a notification
is sent as described

above

.

Instantiates and registers an MBean in the MBean server. The
class loader to be used is identified by its object name. An
object name is associated with the MBean. If the object name of
the loader is null, the ClassLoader that loaded the MBean
server will be used. If the MBean's object name given is null,
the MBean must provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

This method is equivalent to

createMBean(className, name, loaderName, (Object[]) null,
(String[]) null)

.

If this method successfully creates an MBean, a notification
is sent as described

above

.

createMBean

```java
ObjectInstance
createMBean​(
String
className,

ObjectName
name,

Object
[] params,

String
[] signature)
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
```

Instantiates and registers an MBean in the MBean server. The
MBean server will use its

Default Loader
Repository

to load the class of the MBean. An object name is
associated with the MBean. If the object name given is null, the
MBean must provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

If this method successfully creates an MBean, a notification
is sent as described

above

.

**Specified by:** createMBean

in interface

MBeanServerConnection
**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked.
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
**Throws:** RuntimeMBeanException

- If the MBean's constructor or its

preRegister

or

postRegister

method threw
a

RuntimeException

. If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

createMBean

method will
throw a

RuntimeMBeanException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** RuntimeErrorException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

createMBean

method will
throw a

RuntimeErrorException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
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
thrown an exception
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean
**See Also:** MBeanRegistration

---

#### createMBean

ObjectInstance

createMBean​(

String

className,

ObjectName

name,

Object

[] params,

String

[] signature)
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

Instantiates and registers an MBean in the MBean server. The
MBean server will use its

Default Loader
Repository

to load the class of the MBean. An object name is
associated with the MBean. If the object name given is null, the
MBean must provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

If this method successfully creates an MBean, a notification
is sent as described

above

.

If this method successfully creates an MBean, a notification
is sent as described

above

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

Object
[] params,

String
[] signature)
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
```

Instantiates and registers an MBean in the MBean server. The
class loader to be used is identified by its object name. An
object name is associated with the MBean. If the object name of
the loader is not specified, the ClassLoader that loaded the
MBean server will be used. If the MBean object name given is
null, the MBean must provide its own name by implementing the

MBeanRegistration

interface and returning the name from the

preRegister

method.

If this method successfully creates an MBean, a notification
is sent as described

above

.

**Specified by:** createMBean

in interface

MBeanServerConnection
**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** name

- The object name of the MBean. May be null.
**Parameters:** loaderName

- The object name of the class loader to be used.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked.
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
**Throws:** RuntimeMBeanException

- The MBean's constructor or its

preRegister

or

postRegister

method threw
a

RuntimeException

. If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

createMBean

method will
throw a

RuntimeMBeanException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** RuntimeErrorException

- If the

postRegister

method
(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

createMBean

method will
throw a

RuntimeErrorException

, although the MBean creation
and registration succeeded. In such a case, the MBean will be actually
registered even though the

createMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
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
thrown an exception
**Throws:** NotCompliantMBeanException

- This class is not a JMX
compliant MBean
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
**See Also:** MBeanRegistration

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

Object

[] params,

String

[] signature)
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

Instantiates and registers an MBean in the MBean server. The
class loader to be used is identified by its object name. An
object name is associated with the MBean. If the object name of
the loader is not specified, the ClassLoader that loaded the
MBean server will be used. If the MBean object name given is
null, the MBean must provide its own name by implementing the

MBeanRegistration

interface and returning the name from the

preRegister

method.

If this method successfully creates an MBean, a notification
is sent as described

above

.

If this method successfully creates an MBean, a notification
is sent as described

above

.

registerMBean

```java
ObjectInstance
registerMBean​(
Object
object,

ObjectName
name)
throws
InstanceAlreadyExistsException
,

MBeanRegistrationException
,

NotCompliantMBeanException
```

Registers a pre-existing object as an MBean with the MBean
server. If the object name given is null, the MBean must
provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

If this method successfully registers an MBean, a notification
is sent as described

above

.

**Parameters:** object

- The MBean to be registered as an MBean.
**Parameters:** name

- The object name of the MBean. May be null.
**Returns:** An

ObjectInstance

, containing the

ObjectName

and the Java class name of the newly
registered MBean. If the contained

ObjectName

is

n

, the contained Java class name is

getMBeanInfo(n)

.getClassName()

.
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
**Throws:** RuntimeMBeanException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

registerMBean

method will
throw a

RuntimeMBeanException

, although the MBean
registration succeeded. In such a case, the MBean will be actually
registered even though the

registerMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** RuntimeErrorException

- If the

postRegister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

registerMBean

method will
throw a

RuntimeErrorException

, although the MBean
registration succeeded. In such a case, the MBean will be actually
registered even though the

registerMBean

method
threw an exception. Note that

RuntimeErrorException

can
also be thrown by

preRegister

, in which case the MBean
will not be registered.
**Throws:** NotCompliantMBeanException

- This object is not a JMX
compliant MBean
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
passed in parameter is null or no object name is specified.
**See Also:** MBeanRegistration

---

#### registerMBean

ObjectInstance

registerMBean​(

Object

object,

ObjectName

name)
throws

InstanceAlreadyExistsException

,

MBeanRegistrationException

,

NotCompliantMBeanException

Registers a pre-existing object as an MBean with the MBean
server. If the object name given is null, the MBean must
provide its own name by implementing the

MBeanRegistration

interface
and returning the name from the

preRegister

method.

If this method successfully registers an MBean, a notification
is sent as described

above

.

If this method successfully registers an MBean, a notification
is sent as described

above

.

unregisterMBean

```java
void unregisterMBean​(
ObjectName
name)
throws
InstanceNotFoundException
,

MBeanRegistrationException
```

Unregisters an MBean from the MBean server. The MBean is
identified by its object name. Once the method has been
invoked, the MBean may no longer be accessed by its object
name.

If this method successfully unregisters an MBean, a notification
is sent as described

above

.

**Specified by:** unregisterMBean

in interface

MBeanServerConnection
**Parameters:** name

- The object name of the MBean to be unregistered.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the MBean you are when trying to
unregister is the

MBeanServerDelegate

MBean.
**Throws:** RuntimeMBeanException

- If the

postDeregister

(

MBeanRegistration

interface) method of the MBean throws a

RuntimeException

, the

unregisterMBean

method
will throw a

RuntimeMBeanException

, although the MBean
unregistration succeeded. In such a case, the MBean will be actually
unregistered even though the

unregisterMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preDeregister

, in which case the MBean
will remain registered.
**Throws:** RuntimeErrorException

- If the

postDeregister

(

MBeanRegistration

interface) method of the MBean throws an

Error

, the

unregisterMBean

method will
throw a

RuntimeErrorException

, although the MBean
unregistration succeeded. In such a case, the MBean will be actually
unregistered even though the

unregisterMBean

method
threw an exception. Note that

RuntimeMBeanException

can
also be thrown by

preDeregister

, in which case the MBean
will remain registered.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** MBeanRegistrationException

- The preDeregister
((

MBeanRegistration

interface) method of the MBean
has thrown an exception.
**See Also:** MBeanRegistration

---

#### unregisterMBean

void unregisterMBean​(

ObjectName

name)
throws

InstanceNotFoundException

,

MBeanRegistrationException

Unregisters an MBean from the MBean server. The MBean is
identified by its object name. Once the method has been
invoked, the MBean may no longer be accessed by its object
name.

If this method successfully unregisters an MBean, a notification
is sent as described

above

.

If this method successfully unregisters an MBean, a notification
is sent as described

above

.

queryMBeans

```java
Set
<
ObjectInstance
> queryMBeans​(
ObjectName
name,

QueryExp
query)
```

Gets MBeans controlled by the MBean server. This method allows
any of the following to be obtained: All MBeans, a set of
MBeans specified by pattern matching on the

ObjectName

and/or a Query expression, a specific
MBean. When the object name is null or no domain and key
properties are specified, all objects are to be selected (and
filtered if a query is specified). It returns the set of

ObjectInstance

objects (containing the

ObjectName

and the Java Class name) for the
selected MBeans.

**Specified by:** queryMBeans

in interface

MBeanServerConnection
**Parameters:** name

- The object name pattern identifying the MBeans to
be retrieved. If null or no domain and key properties are
specified, all the MBeans registered will be retrieved.
**Parameters:** query

- The query expression to be applied for selecting
MBeans. If null no query expression will be applied for
selecting MBeans.
**Returns:** A set containing the

ObjectInstance

objects for the selected MBeans. If no MBean satisfies the
query an empty list is returned.
**Throws:** RuntimeOperationsException

---

#### queryMBeans

Set

<

ObjectInstance

> queryMBeans​(

ObjectName

name,

QueryExp

query)

Gets MBeans controlled by the MBean server. This method allows
any of the following to be obtained: All MBeans, a set of
MBeans specified by pattern matching on the

ObjectName

and/or a Query expression, a specific
MBean. When the object name is null or no domain and key
properties are specified, all objects are to be selected (and
filtered if a query is specified). It returns the set of

ObjectInstance

objects (containing the

ObjectName

and the Java Class name) for the
selected MBeans.

queryNames

```java
Set
<
ObjectName
> queryNames​(
ObjectName
name,

QueryExp
query)
```

Gets the names of MBeans controlled by the MBean server. This
method enables any of the following to be obtained: The names
of all MBeans, the names of a set of MBeans specified by
pattern matching on the

ObjectName

and/or a Query
expression, a specific MBean name (equivalent to testing
whether an MBean is registered). When the object name is null
or no domain and key properties are specified, all objects are
selected (and filtered if a query is specified). It returns the
set of ObjectNames for the MBeans selected.

**Specified by:** queryNames

in interface

MBeanServerConnection
**Parameters:** name

- The object name pattern identifying the MBean names
to be retrieved. If null or no domain and key properties are
specified, the name of all registered MBeans will be retrieved.
**Parameters:** query

- The query expression to be applied for selecting
MBeans. If null no query expression will be applied for
selecting MBeans.
**Returns:** A set containing the ObjectNames for the MBeans
selected. If no MBean satisfies the query, an empty list is
returned.
**Throws:** RuntimeOperationsException

---

#### queryNames

Set

<

ObjectName

> queryNames​(

ObjectName

name,

QueryExp

query)

Gets the names of MBeans controlled by the MBean server. This
method enables any of the following to be obtained: The names
of all MBeans, the names of a set of MBeans specified by
pattern matching on the

ObjectName

and/or a Query
expression, a specific MBean name (equivalent to testing
whether an MBean is registered). When the object name is null
or no domain and key properties are specified, all objects are
selected (and filtered if a query is specified). It returns the
set of ObjectNames for the MBeans selected.

isRegistered

```java
boolean isRegistered​(
ObjectName
name)
```

Description copied from interface:

MBeanServerConnection

Checks whether an MBean, identified by its object name, is
already registered with the MBean server.

**Specified by:** isRegistered

in interface

MBeanServerConnection
**Parameters:** name

- The object name of the MBean to be checked.
**Returns:** True if the MBean is already registered in the MBean
server, false otherwise.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null.

---

#### isRegistered

boolean isRegistered​(

ObjectName

name)

Description copied from interface:

MBeanServerConnection

Checks whether an MBean, identified by its object name, is
already registered with the MBean server.

getMBeanCount

```java
Integer
getMBeanCount()
```

Returns the number of MBeans registered in the MBean server.

**Specified by:** getMBeanCount

in interface

MBeanServerConnection
**Returns:** the number of registered MBeans, wrapped in an Integer.
If the caller's permissions are restricted, this number may
be greater than the number of MBeans the caller can access.

---

#### getMBeanCount

Integer

getMBeanCount()

Returns the number of MBeans registered in the MBean server.

getAttribute

```java
Object
getAttribute​(
ObjectName
name,

String
attribute)
throws
MBeanException
,

AttributeNotFoundException
,

InstanceNotFoundException
,

ReflectionException
```

Description copied from interface:

MBeanServerConnection

Gets the value of a specific attribute of a named MBean. The MBean
is identified by its object name.

**Specified by:** getAttribute

in interface

MBeanServerConnection
**Parameters:** name

- The object name of the MBean from which the
attribute is to be retrieved.
**Parameters:** attribute

- A String specifying the name of the attribute
to be retrieved.
**Returns:** The value of the retrieved attribute.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the attribute in parameter is
null.
**Throws:** MBeanException

- Wraps an exception thrown by the
MBean's getter.
**Throws:** AttributeNotFoundException

- The attribute specified
is not accessible in the MBean.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown when trying to invoke
the setter.
**See Also:** MBeanServerConnection.setAttribute(javax.management.ObjectName, javax.management.Attribute)

---

#### getAttribute

Object

getAttribute​(

ObjectName

name,

String

attribute)
throws

MBeanException

,

AttributeNotFoundException

,

InstanceNotFoundException

,

ReflectionException

Description copied from interface:

MBeanServerConnection

Gets the value of a specific attribute of a named MBean. The MBean
is identified by its object name.

getAttributes

```java
AttributeList
getAttributes​(
ObjectName
name,

String
[] attributes)
throws
InstanceNotFoundException
,

ReflectionException
```

Description copied from interface:

MBeanServerConnection

Retrieves the values of several attributes of a named MBean. The MBean
is identified by its object name.

If one or more attributes cannot be retrieved for some reason, they
will be omitted from the returned

AttributeList

. The caller
should check that the list is the same size as the

attributes

array. To discover what problem prevented a given attribute from being
retrieved, call

getAttribute

for that attribute.

Here is an example of calling this method and checking that it
succeeded in retrieving all the requested attributes:

```java
String[] attrNames = ...;
AttributeList list = mbeanServerConnection.getAttributes(objectName, attrNames);
if (list.size() == attrNames.length)
System.out.println("All attributes were retrieved successfully");
else {

List<String>
missing = new
ArrayList<String>
(
Arrays.asList
(attrNames));
for (Attribute a : list.asList())
missing.remove(a.getName());
System.out.println("Did not retrieve: " + missing);
}
```

**Specified by:** getAttributes

in interface

MBeanServerConnection
**Parameters:** name

- The object name of the MBean from which the
attributes are retrieved.
**Parameters:** attributes

- A list of the attributes to be retrieved.
**Returns:** The list of the retrieved attributes.
**Throws:** RuntimeOperationsException

- Wrap a

java.lang.IllegalArgumentException

: The object
name in parameter is null or attributes in parameter is null.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- An exception occurred when
trying to invoke the getAttributes method of a Dynamic MBean.
**See Also:** MBeanServerConnection.setAttributes(javax.management.ObjectName, javax.management.AttributeList)

---

#### getAttributes

AttributeList

getAttributes​(

ObjectName

name,

String

[] attributes)
throws

InstanceNotFoundException

,

ReflectionException

Description copied from interface:

MBeanServerConnection

Retrieves the values of several attributes of a named MBean. The MBean
is identified by its object name.

If one or more attributes cannot be retrieved for some reason, they
will be omitted from the returned

AttributeList

. The caller
should check that the list is the same size as the

attributes

array. To discover what problem prevented a given attribute from being
retrieved, call

getAttribute

for that attribute.

Here is an example of calling this method and checking that it
succeeded in retrieving all the requested attributes:

```java
String[] attrNames = ...;
AttributeList list = mbeanServerConnection.getAttributes(objectName, attrNames);
if (list.size() == attrNames.length)
System.out.println("All attributes were retrieved successfully");
else {

List<String>
missing = new
ArrayList<String>
(
Arrays.asList
(attrNames));
for (Attribute a : list.asList())
missing.remove(a.getName());
System.out.println("Did not retrieve: " + missing);
}
```

Retrieves the values of several attributes of a named MBean. The MBean
is identified by its object name.

If one or more attributes cannot be retrieved for some reason, they
will be omitted from the returned

AttributeList

. The caller
should check that the list is the same size as the

attributes

array. To discover what problem prevented a given attribute from being
retrieved, call

getAttribute

for that attribute.

Here is an example of calling this method and checking that it
succeeded in retrieving all the requested attributes:

String[] attrNames = ...;
AttributeList list = mbeanServerConnection.getAttributes(objectName, attrNames);
if (list.size() == attrNames.length)
System.out.println("All attributes were retrieved successfully");
else {

List<String>

missing = new

ArrayList<String>

(

Arrays.asList

(attrNames));
for (Attribute a : list.asList())
missing.remove(a.getName());
System.out.println("Did not retrieve: " + missing);
}

setAttribute

```java
void setAttribute​(
ObjectName
name,

Attribute
attribute)
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
```

Description copied from interface:

MBeanServerConnection

Sets the value of a specific attribute of a named MBean. The MBean
is identified by its object name.

**Specified by:** setAttribute

in interface

MBeanServerConnection
**Parameters:** name

- The name of the MBean within which the attribute is
to be set.
**Parameters:** attribute

- The identification of the attribute to be set
and the value it is to be set to.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or the attribute in parameter is
null.
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
**See Also:** MBeanServerConnection.getAttribute(javax.management.ObjectName, java.lang.String)

---

#### setAttribute

void setAttribute​(

ObjectName

name,

Attribute

attribute)
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

Description copied from interface:

MBeanServerConnection

Sets the value of a specific attribute of a named MBean. The MBean
is identified by its object name.

setAttributes

```java
AttributeList
setAttributes​(
ObjectName
name,

AttributeList
attributes)
throws
InstanceNotFoundException
,

ReflectionException
```

Description copied from interface:

MBeanServerConnection

Sets the values of several attributes of a named MBean. The MBean is
identified by its object name.

If one or more attributes cannot be set for some reason, they will be
omitted from the returned

AttributeList

. The caller should check
that the input

AttributeList

is the same size as the output one.
To discover what problem prevented a given attribute from being retrieved,
it will usually be possible to call

setAttribute

for that attribute, although this is not guaranteed to work. (For
example, the values of two attributes may have been rejected because
they were inconsistent with each other. Setting one of them alone might
be allowed.)

Here is an example of calling this method and checking that it
succeeded in setting all the requested attributes:

```java
AttributeList inputAttrs = ...;
AttributeList outputAttrs = mbeanServerConnection.setAttributes(
objectName, inputAttrs);
if (inputAttrs.size() == outputAttrs.size())
System.out.println("All attributes were set successfully");
else {

List<String>
missing = new
ArrayList<String>
();
for (Attribute a : inputAttrs.asList())
missing.add(a.getName());
for (Attribute a : outputAttrs.asList())
missing.remove(a.getName());
System.out.println("Did not set: " + missing);
}
```

**Specified by:** setAttributes

in interface

MBeanServerConnection
**Parameters:** name

- The object name of the MBean within which the
attributes are to be set.
**Parameters:** attributes

- A list of attributes: The identification of
the attributes to be set and the values they are to be set to.
**Returns:** The list of attributes that were set, with their new
values.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The object
name in parameter is null or attributes in parameter is null.
**Throws:** InstanceNotFoundException

- The MBean specified is not
registered in the MBean server.
**Throws:** ReflectionException

- An exception occurred when
trying to invoke the getAttributes method of a Dynamic MBean.
**See Also:** MBeanServerConnection.getAttributes(javax.management.ObjectName, java.lang.String[])

---

#### setAttributes

AttributeList

setAttributes​(

ObjectName

name,

AttributeList

attributes)
throws

InstanceNotFoundException

,

ReflectionException

Description copied from interface:

MBeanServerConnection

Sets the values of several attributes of a named MBean. The MBean is
identified by its object name.

If one or more attributes cannot be set for some reason, they will be
omitted from the returned

AttributeList

. The caller should check
that the input

AttributeList

is the same size as the output one.
To discover what problem prevented a given attribute from being retrieved,
it will usually be possible to call

setAttribute

for that attribute, although this is not guaranteed to work. (For
example, the values of two attributes may have been rejected because
they were inconsistent with each other. Setting one of them alone might
be allowed.)

Here is an example of calling this method and checking that it
succeeded in setting all the requested attributes:

```java
AttributeList inputAttrs = ...;
AttributeList outputAttrs = mbeanServerConnection.setAttributes(
objectName, inputAttrs);
if (inputAttrs.size() == outputAttrs.size())
System.out.println("All attributes were set successfully");
else {

List<String>
missing = new
ArrayList<String>
();
for (Attribute a : inputAttrs.asList())
missing.add(a.getName());
for (Attribute a : outputAttrs.asList())
missing.remove(a.getName());
System.out.println("Did not set: " + missing);
}
```

Sets the values of several attributes of a named MBean. The MBean is
identified by its object name.

If one or more attributes cannot be set for some reason, they will be
omitted from the returned

AttributeList

. The caller should check
that the input

AttributeList

is the same size as the output one.
To discover what problem prevented a given attribute from being retrieved,
it will usually be possible to call

setAttribute

for that attribute, although this is not guaranteed to work. (For
example, the values of two attributes may have been rejected because
they were inconsistent with each other. Setting one of them alone might
be allowed.)

Here is an example of calling this method and checking that it
succeeded in setting all the requested attributes:

```java
AttributeList inputAttrs = ...;
AttributeList outputAttrs = mbeanServerConnection.setAttributes(
objectName, inputAttrs);
if (inputAttrs.size() == outputAttrs.size())
System.out.println("All attributes were set successfully");
else {

List<String>
missing = new
ArrayList<String>
();
for (Attribute a : inputAttrs.asList())
missing.add(a.getName());
for (Attribute a : outputAttrs.asList())
missing.remove(a.getName());
System.out.println("Did not set: " + missing);
}
```

Here is an example of calling this method and checking that it
succeeded in setting all the requested attributes:

AttributeList inputAttrs = ...;
AttributeList outputAttrs = mbeanServerConnection.setAttributes(

objectName, inputAttrs);
if (inputAttrs.size() == outputAttrs.size())
System.out.println("All attributes were set successfully");
else {

List<String>

missing = new

ArrayList<String>

();
for (Attribute a : inputAttrs.asList())
missing.add(a.getName());
for (Attribute a : outputAttrs.asList())
missing.remove(a.getName());
System.out.println("Did not set: " + missing);
}

addNotificationListener

```java
void addNotificationListener​(
ObjectName
name,

NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
throws
InstanceNotFoundException
```

Adds a listener to a registered MBean.
Notifications emitted by the MBean will be forwarded to the listener.

If the source of the notification
is a reference to an MBean object, the MBean server will replace it
by that MBean's ObjectName. Otherwise the source is unchanged.

**Specified by:** addNotificationListener

in interface

MBeanServerConnection
**Parameters:** name

- The name of the MBean on which the listener should
be added.
**Parameters:** listener

- The listener object which will handle the
notifications emitted by the registered MBean.
**Parameters:** filter

- The filter object. If filter is null, no
filtering will be performed before handling notifications.
**Parameters:** handback

- The context to be sent to the listener when a
notification is emitted.
**Throws:** InstanceNotFoundException

- The MBean name provided
does not match any of the registered MBeans.
**See Also:** MBeanServerConnection.removeNotificationListener(ObjectName, NotificationListener)

,

MBeanServerConnection.removeNotificationListener(ObjectName, NotificationListener,
NotificationFilter, Object)

---

#### addNotificationListener

void addNotificationListener​(

ObjectName

name,

NotificationListener

listener,

NotificationFilter

filter,

Object

handback)
throws

InstanceNotFoundException

Adds a listener to a registered MBean.
Notifications emitted by the MBean will be forwarded to the listener.

If the source of the notification
is a reference to an MBean object, the MBean server will replace it
by that MBean's ObjectName. Otherwise the source is unchanged.

Adds a listener to a registered MBean.
Notifications emitted by the MBean will be forwarded to the listener.

addNotificationListener

```java
void addNotificationListener​(
ObjectName
name,

ObjectName
listener,

NotificationFilter
filter,

Object
handback)
throws
InstanceNotFoundException
```

Adds a listener to a registered MBean.

A notification emitted by an MBean will be forwarded by the
MBeanServer to the listener. If the source of the notification
is a reference to an MBean object, the MBean server will
replace it by that MBean's ObjectName. Otherwise the source is
unchanged.

The listener object that receives notifications is the one
that is registered with the given name at the time this method
is called. Even if it is subsequently unregistered, it will
continue to receive notifications.

**Specified by:** addNotificationListener

in interface

MBeanServerConnection
**Parameters:** name

- The name of the MBean on which the listener should
be added.
**Parameters:** listener

- The object name of the listener which will
handle the notifications emitted by the registered MBean.
**Parameters:** filter

- The filter object. If filter is null, no
filtering will be performed before handling notifications.
**Parameters:** handback

- The context to be sent to the listener when a
notification is emitted.
**Throws:** RuntimeOperationsException

- Wraps an

IllegalArgumentException

. The MBean named by

listener

exists but does not implement the

NotificationListener

interface.
**Throws:** InstanceNotFoundException

- The MBean name of the
notification listener or of the notification broadcaster does
not match any of the registered MBeans.
**See Also:** MBeanServerConnection.removeNotificationListener(ObjectName, ObjectName)

,

MBeanServerConnection.removeNotificationListener(ObjectName, ObjectName,
NotificationFilter, Object)

---

#### addNotificationListener

void addNotificationListener​(

ObjectName

name,

ObjectName

listener,

NotificationFilter

filter,

Object

handback)
throws

InstanceNotFoundException

Adds a listener to a registered MBean.

A notification emitted by an MBean will be forwarded by the
MBeanServer to the listener. If the source of the notification
is a reference to an MBean object, the MBean server will
replace it by that MBean's ObjectName. Otherwise the source is
unchanged.

The listener object that receives notifications is the one
that is registered with the given name at the time this method
is called. Even if it is subsequently unregistered, it will
continue to receive notifications.

Adds a listener to a registered MBean.

A notification emitted by an MBean will be forwarded by the
MBeanServer to the listener. If the source of the notification
is a reference to an MBean object, the MBean server will
replace it by that MBean's ObjectName. Otherwise the source is
unchanged.

The listener object that receives notifications is the one
that is registered with the given name at the time this method
is called. Even if it is subsequently unregistered, it will
continue to receive notifications.

instantiate

```java
Object
instantiate​(
String
className)
throws
ReflectionException
,

MBeanException
```

Instantiates an object using the list of all class loaders
registered in the MBean server's

Class Loader
Repository

. The object's class should have a public
constructor. This method returns a reference to the newly
created object. The newly created object is not registered in
the MBean server.

This method is equivalent to

instantiate(className, (Object[]) null, (String[]) null)

.

**Parameters:** className

- The class name of the object to be instantiated.
**Returns:** The newly instantiated object.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or the

java.lang.Exception

that occurred when trying to
invoke the object's constructor.
**Throws:** MBeanException

- The constructor of the object has
thrown an exception
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null.

---

#### instantiate

Object

instantiate​(

String

className)
throws

ReflectionException

,

MBeanException

Instantiates an object using the list of all class loaders
registered in the MBean server's

Class Loader
Repository

. The object's class should have a public
constructor. This method returns a reference to the newly
created object. The newly created object is not registered in
the MBean server.

This method is equivalent to

instantiate(className, (Object[]) null, (String[]) null)

.

Instantiates an object using the list of all class loaders
registered in the MBean server's

Class Loader
Repository

. The object's class should have a public
constructor. This method returns a reference to the newly
created object. The newly created object is not registered in
the MBean server.

This method is equivalent to

instantiate(className, (Object[]) null, (String[]) null)

.

instantiate

```java
Object
instantiate​(
String
className,

ObjectName
loaderName)
throws
ReflectionException
,

MBeanException
,

InstanceNotFoundException
```

Instantiates an object using the class Loader specified by its

ObjectName

. If the loader name is null, the
ClassLoader that loaded the MBean Server will be used. The
object's class should have a public constructor. This method
returns a reference to the newly created object. The newly
created object is not registered in the MBean server.

This method is equivalent to

instantiate(className, loaderName, (Object[]) null, (String[])
null)

.

**Parameters:** className

- The class name of the MBean to be instantiated.
**Parameters:** loaderName

- The object name of the class loader to be used.
**Returns:** The newly instantiated object.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or the

java.lang.Exception

that occurred when trying to
invoke the object's constructor.
**Throws:** MBeanException

- The constructor of the object has
thrown an exception.
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBeanServer.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null.

---

#### instantiate

Object

instantiate​(

String

className,

ObjectName

loaderName)
throws

ReflectionException

,

MBeanException

,

InstanceNotFoundException

Instantiates an object using the class Loader specified by its

ObjectName

. If the loader name is null, the
ClassLoader that loaded the MBean Server will be used. The
object's class should have a public constructor. This method
returns a reference to the newly created object. The newly
created object is not registered in the MBean server.

This method is equivalent to

instantiate(className, loaderName, (Object[]) null, (String[])
null)

.

Instantiates an object using the class Loader specified by its

ObjectName

. If the loader name is null, the
ClassLoader that loaded the MBean Server will be used. The
object's class should have a public constructor. This method
returns a reference to the newly created object. The newly
created object is not registered in the MBean server.

This method is equivalent to

instantiate(className, loaderName, (Object[]) null, (String[])
null)

.

instantiate

```java
Object
instantiate​(
String
className,

Object
[] params,

String
[] signature)
throws
ReflectionException
,

MBeanException
```

Instantiates an object using the list of all class loaders
registered in the MBean server

Class Loader
Repository

. The object's class should have a public
constructor. The call returns a reference to the newly created
object. The newly created object is not registered in the
MBean server.

**Parameters:** className

- The class name of the object to be instantiated.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked.
**Returns:** The newly instantiated object.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or the

java.lang.Exception

that occurred when trying to
invoke the object's constructor.
**Throws:** MBeanException

- The constructor of the object has
thrown an exception
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null.

---

#### instantiate

Object

instantiate​(

String

className,

Object

[] params,

String

[] signature)
throws

ReflectionException

,

MBeanException

Instantiates an object using the list of all class loaders
registered in the MBean server

Class Loader
Repository

. The object's class should have a public
constructor. The call returns a reference to the newly created
object. The newly created object is not registered in the
MBean server.

instantiate

```java
Object
instantiate​(
String
className,

ObjectName
loaderName,

Object
[] params,

String
[] signature)
throws
ReflectionException
,

MBeanException
,

InstanceNotFoundException
```

Instantiates an object. The class loader to be used is
identified by its object name. If the object name of the loader
is null, the ClassLoader that loaded the MBean server will be
used. The object's class should have a public constructor.
The call returns a reference to the newly created object. The
newly created object is not registered in the MBean server.

**Parameters:** className

- The class name of the object to be instantiated.
**Parameters:** params

- An array containing the parameters of the
constructor to be invoked.
**Parameters:** signature

- An array containing the signature of the
constructor to be invoked.
**Parameters:** loaderName

- The object name of the class loader to be used.
**Returns:** The newly instantiated object.
**Throws:** ReflectionException

- Wraps a

java.lang.ClassNotFoundException

or the

java.lang.Exception

that
occurred when trying to invoke the object's constructor.
**Throws:** MBeanException

- The constructor of the object has
thrown an exception
**Throws:** InstanceNotFoundException

- The specified class loader
is not registered in the MBean server.
**Throws:** RuntimeOperationsException

- Wraps a

java.lang.IllegalArgumentException

: The className
passed in parameter is null.

---

#### instantiate

Object

instantiate​(

String

className,

ObjectName

loaderName,

Object

[] params,

String

[] signature)
throws

ReflectionException

,

MBeanException

,

InstanceNotFoundException

Instantiates an object. The class loader to be used is
identified by its object name. If the object name of the loader
is null, the ClassLoader that loaded the MBean server will be
used. The object's class should have a public constructor.
The call returns a reference to the newly created object. The
newly created object is not registered in the MBean server.

deserialize

```java
@Deprecated
(
since
="1.5")
default
ObjectInputStream
deserialize​(
ObjectName
name,
byte[] data)
throws
InstanceNotFoundException
,

OperationsException
```

Deprecated.

Use

getClassLoaderFor

to
obtain the appropriate class loader for deserialization.

De-serializes a byte array in the context of the class loader
of an MBean.

**Implementation Requirements:** This method throws

UnsupportedOperationException

by default.
**Parameters:** name

- The name of the MBean whose class loader should be
used for the de-serialization.
**Parameters:** data

- The byte array to be de-sererialized.
**Returns:** The de-serialized object stream.
**Throws:** InstanceNotFoundException

- The MBean specified is not
found.
**Throws:** OperationsException

- Any of the usual Input/Output
related exceptions.

---

#### deserialize

@Deprecated

(

since

="1.5")
default

ObjectInputStream

deserialize​(

ObjectName

name,
byte[] data)
throws

InstanceNotFoundException

,

OperationsException

De-serializes a byte array in the context of the class loader
of an MBean.

deserialize

```java
@Deprecated
(
since
="1.5")
default
ObjectInputStream
deserialize​(
String
className,
byte[] data)
throws
OperationsException
,

ReflectionException
```

Deprecated.

Use

getClassLoaderRepository()

to obtain the
class loader repository and use it to deserialize.

De-serializes a byte array in the context of a given MBean
class loader. The class loader is found by loading the class

className

through the

Class Loader
Repository

. The resultant class's class loader is the one to
use.

**Implementation Requirements:** This method throws

UnsupportedOperationException

by default.
**Parameters:** className

- The name of the class whose class loader should be
used for the de-serialization.
**Parameters:** data

- The byte array to be de-sererialized.
**Returns:** The de-serialized object stream.
**Throws:** OperationsException

- Any of the usual Input/Output
related exceptions.
**Throws:** ReflectionException

- The specified class could not be
loaded by the class loader repository

---

#### deserialize

@Deprecated

(

since

="1.5")
default

ObjectInputStream

deserialize​(

String

className,
byte[] data)
throws

OperationsException

,

ReflectionException

De-serializes a byte array in the context of a given MBean
class loader. The class loader is found by loading the class

className

through the

Class Loader
Repository

. The resultant class's class loader is the one to
use.

deserialize

```java
@Deprecated
(
since
="1.5")
default
ObjectInputStream
deserialize​(
String
className,

ObjectName
loaderName,
byte[] data)
throws
InstanceNotFoundException
,

OperationsException
,

ReflectionException
```

Deprecated.

Use

getClassLoader

to obtain
the class loader for deserialization.

De-serializes a byte array in the context of a given MBean
class loader. The class loader is the one that loaded the
class with name "className". The name of the class loader to
be used for loading the specified class is specified. If null,
the MBean Server's class loader will be used.

**Implementation Requirements:** This method throws

UnsupportedOperationException

by default.
**Parameters:** className

- The name of the class whose class loader should be
used for the de-serialization.
**Parameters:** data

- The byte array to be de-sererialized.
**Parameters:** loaderName

- The name of the class loader to be used for
loading the specified class. If null, the MBean Server's class
loader will be used.
**Returns:** The de-serialized object stream.
**Throws:** InstanceNotFoundException

- The specified class loader
MBean is not found.
**Throws:** OperationsException

- Any of the usual Input/Output
related exceptions.
**Throws:** ReflectionException

- The specified class could not be
loaded by the specified class loader.

---

#### deserialize

@Deprecated

(

since

="1.5")
default

ObjectInputStream

deserialize​(

String

className,

ObjectName

loaderName,
byte[] data)
throws

InstanceNotFoundException

,

OperationsException

,

ReflectionException

De-serializes a byte array in the context of a given MBean
class loader. The class loader is the one that loaded the
class with name "className". The name of the class loader to
be used for loading the specified class is specified. If null,
the MBean Server's class loader will be used.

getClassLoaderFor

```java
ClassLoader
getClassLoaderFor​(
ObjectName
mbeanName)
throws
InstanceNotFoundException
```

Return the

ClassLoader

that was used for
loading the class of the named MBean.

**Parameters:** mbeanName

- The ObjectName of the MBean.
**Returns:** The ClassLoader used for that MBean. If

l

is the MBean's actual ClassLoader, and

r

is the
returned value, then either:

- r

is identical to

l

; or

the result of

r

.loadClass(

s

)

is the
same as

l

.loadClass(

s

)

for any string

s

.

What this means is that the ClassLoader may be wrapped in
another ClassLoader for security or other reasons.
**Throws:** InstanceNotFoundException

- if the named MBean is not found.

---

#### getClassLoaderFor

ClassLoader

getClassLoaderFor​(

ObjectName

mbeanName)
throws

InstanceNotFoundException

Return the

ClassLoader

that was used for
loading the class of the named MBean.

r

is identical to

l

; or

the result of

r

.loadClass(

s

)

is the
same as

l

.loadClass(

s

)

for any string

s

.

getClassLoader

```java
ClassLoader
getClassLoader​(
ObjectName
loaderName)
throws
InstanceNotFoundException
```

Return the named

ClassLoader

.

**Parameters:** loaderName

- The ObjectName of the ClassLoader. May be
null, in which case the MBean server's own ClassLoader is
returned.
**Returns:** The named ClassLoader. If

l

is the actual
ClassLoader with that name, and

r

is the returned
value, then either:

- r

is identical to

l

; or

the result of

r

.loadClass(

s

)

is the
same as

l

.loadClass(

s

)

for any string

s

.

What this means is that the ClassLoader may be wrapped in
another ClassLoader for security or other reasons.
**Throws:** InstanceNotFoundException

- if the named ClassLoader is
not found.

---

#### getClassLoader

ClassLoader

getClassLoader​(

ObjectName

loaderName)
throws

InstanceNotFoundException

Return the named

ClassLoader

.

r

is identical to

l

; or

the result of

r

.loadClass(

s

)

is the
same as

l

.loadClass(

s

)

for any string

s

.

getClassLoaderRepository

```java
ClassLoaderRepository
getClassLoaderRepository()
```

Return the ClassLoaderRepository for this MBeanServer.

**Returns:** The ClassLoaderRepository for this MBeanServer.

---

#### getClassLoaderRepository

ClassLoaderRepository

getClassLoaderRepository()

Return the ClassLoaderRepository for this MBeanServer.

---

