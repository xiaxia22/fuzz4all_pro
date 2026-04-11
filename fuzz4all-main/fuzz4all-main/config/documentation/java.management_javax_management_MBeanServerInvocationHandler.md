# Class MBeanServerInvocationHandler

**Source:** `java.management\javax\management\MBeanServerInvocationHandler.html`

### Class Description

```java
public class
MBeanServerInvocationHandler

extends
Object

implements
InvocationHandler
```

InvocationHandler

that forwards methods in an MBean's
management interface through the MBean server to the MBean.

Given an

MBeanServerConnection

, the

ObjectName

of an MBean within that MBean server, and a Java interface

Intf

that describes the management interface of the
MBean using the patterns for a Standard MBean or an MXBean, this
class can be used to construct a proxy for the MBean. The proxy
implements the interface

Intf

such that all of its
methods are forwarded through the MBean server to the MBean.

If the

InvocationHandler

is for an MXBean, then the parameters of
a method are converted from the type declared in the MXBean
interface into the corresponding mapped type, and the return value
is converted from the mapped type into the declared type. For
example, with the method

public List<String> reverse(List<String> list);

and given that the mapped type for

List<String>

is

String[]

, a call to

proxy.reverse(someList)

will convert

someList

from a

List<String>

to a

String[]

,
call the MBean operation

reverse

, then convert the returned

String[]

into a

List<String>

.

The method Object.toString(), Object.hashCode(), or
Object.equals(Object), when invoked on a proxy using this
invocation handler, is forwarded to the MBean server as a method on
the proxied MBean only if it appears in one of the proxy's
interfaces. For a proxy created with

JMX.newMBeanProxy

or

JMX.newMXBeanProxy

, this means that the method must appear in the
Standard MBean or MXBean interface. Otherwise these methods have
the following behavior:

- toString() returns a string representation of the proxy

hashCode() returns a hash code for the proxy such
that two equal proxies have the same hash code

equals(Object)
returns true if and only if the Object argument is of the same
proxy class as this proxy, with an MBeanServerInvocationHandler
that has the same MBeanServerConnection and ObjectName; if one
of the

MBeanServerInvocationHandler

s was constructed with
a

Class

argument then the other must have been constructed
with the same

Class

for

equals

to return true.

**All Implemented Interfaces:** InvocationHandler

---

### Field Details

*No entries found.*

### Constructor Details

#### public MBeanServerInvocationHandler​(
MBeanServerConnection
connection,

ObjectName
objectName)

Invocation handler that forwards methods through an MBean
server to a Standard MBean. This constructor may be called
instead of relying on

JMX.newMBeanProxy

, for instance if you need to supply a
different

ClassLoader

to

Proxy.newProxyInstance

.

This constructor is not appropriate for an MXBean. Use

MBeanServerInvocationHandler(MBeanServerConnection,
ObjectName, boolean)

for that. This constructor is equivalent
to

new MBeanServerInvocationHandler(connection,
objectName, false)

.

**Parameters:**
- connection

- the MBean server connection through which all
methods of a proxy using this handler will be forwarded.
- objectName

- the name of the MBean within the MBean server
to which methods will be forwarded.

---

#### public MBeanServerInvocationHandler​(
MBeanServerConnection
connection,

ObjectName
objectName,
boolean isMXBean)

Invocation handler that can forward methods through an MBean
server to a Standard MBean or MXBean. This constructor may be called
instead of relying on

JMX.newMXBeanProxy

, for instance if you need to supply a
different

ClassLoader

to

Proxy.newProxyInstance

.

**Parameters:**
- connection

- the MBean server connection through which all
methods of a proxy using this handler will be forwarded.
- objectName

- the name of the MBean within the MBean server
to which methods will be forwarded.
- isMXBean

- if true, the proxy is for an

MXBean

, and
appropriate mappings will be applied to method parameters and return
values.

**Since:**
- 1.6

---

### Method Details

#### public
MBeanServerConnection
getMBeanServerConnection()

The MBean server connection through which the methods of
a proxy using this handler are forwarded.

**Returns:**
- the MBean server connection.

**Since:**
- 1.6

---

#### public
ObjectName
getObjectName()

The name of the MBean within the MBean server to which methods
are forwarded.

**Returns:**
- the object name.

**Since:**
- 1.6

---

#### public boolean isMXBean()

If true, the proxy is for an MXBean, and appropriate mappings
are applied to method parameters and return values.

**Returns:**
- whether the proxy is for an MXBean.

**Since:**
- 1.6

---

#### public static <T> T newProxyInstance​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass,
boolean notificationBroadcaster)

Return a proxy that implements the given interface by
forwarding its methods through the given MBean server to the
named MBean. As of 1.6, the methods

JMX.newMBeanProxy(MBeanServerConnection, ObjectName, Class)

and

JMX.newMBeanProxy(MBeanServerConnection, ObjectName, Class,
boolean)

are preferred to this method.

This method is equivalent to

Proxy.newProxyInstance

(interfaceClass.getClassLoader(),
interfaces, handler)

. Here

handler

is the
result of

new
MBeanServerInvocationHandler(connection, objectName)

, and

interfaces

is an array that has one element if

notificationBroadcaster

is false and two if it is
true. The first element of

interfaces

is

interfaceClass

and the second, if present, is

NotificationEmitter.class

.

**Parameters:**
- connection

- the MBean server to forward to.
- objectName

- the name of the MBean within

connection

to forward to.
- interfaceClass

- the management interface that the MBean
exports, which will also be implemented by the returned proxy.
- notificationBroadcaster

- make the returned proxy
implement

NotificationEmitter

by forwarding its methods
via

connection

. A call to

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

on the proxy will
result in a call to

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

, and likewise
for the other methods of

NotificationBroadcaster

and

NotificationEmitter

.

**Returns:**
- the new proxy instance.

**See Also:**
- JMX.newMBeanProxy(MBeanServerConnection, ObjectName, Class, boolean)

**Type Parameters:**
- T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMBean.class

, for example,
then the return type is

MyMBean

.

---

### Additional Sections

#### Class MBeanServerInvocationHandler

java.lang.Object

- javax.management.MBeanServerInvocationHandler

javax.management.MBeanServerInvocationHandler

**All Implemented Interfaces:** InvocationHandler

```java
public class
MBeanServerInvocationHandler

extends
Object

implements
InvocationHandler
```

InvocationHandler

that forwards methods in an MBean's
management interface through the MBean server to the MBean.

Given an

MBeanServerConnection

, the

ObjectName

of an MBean within that MBean server, and a Java interface

Intf

that describes the management interface of the
MBean using the patterns for a Standard MBean or an MXBean, this
class can be used to construct a proxy for the MBean. The proxy
implements the interface

Intf

such that all of its
methods are forwarded through the MBean server to the MBean.

If the

InvocationHandler

is for an MXBean, then the parameters of
a method are converted from the type declared in the MXBean
interface into the corresponding mapped type, and the return value
is converted from the mapped type into the declared type. For
example, with the method

public List<String> reverse(List<String> list);

and given that the mapped type for

List<String>

is

String[]

, a call to

proxy.reverse(someList)

will convert

someList

from a

List<String>

to a

String[]

,
call the MBean operation

reverse

, then convert the returned

String[]

into a

List<String>

.

The method Object.toString(), Object.hashCode(), or
Object.equals(Object), when invoked on a proxy using this
invocation handler, is forwarded to the MBean server as a method on
the proxied MBean only if it appears in one of the proxy's
interfaces. For a proxy created with

JMX.newMBeanProxy

or

JMX.newMXBeanProxy

, this means that the method must appear in the
Standard MBean or MXBean interface. Otherwise these methods have
the following behavior:

- toString() returns a string representation of the proxy

hashCode() returns a hash code for the proxy such
that two equal proxies have the same hash code

equals(Object)
returns true if and only if the Object argument is of the same
proxy class as this proxy, with an MBeanServerInvocationHandler
that has the same MBeanServerConnection and ObjectName; if one
of the

MBeanServerInvocationHandler

s was constructed with
a

Class

argument then the other must have been constructed
with the same

Class

for

equals

to return true.

**Since:** 1.5

public class

MBeanServerInvocationHandler

extends

Object

implements

InvocationHandler

InvocationHandler

that forwards methods in an MBean's
management interface through the MBean server to the MBean.

Given an

MBeanServerConnection

, the

ObjectName

of an MBean within that MBean server, and a Java interface

Intf

that describes the management interface of the
MBean using the patterns for a Standard MBean or an MXBean, this
class can be used to construct a proxy for the MBean. The proxy
implements the interface

Intf

such that all of its
methods are forwarded through the MBean server to the MBean.

If the

InvocationHandler

is for an MXBean, then the parameters of
a method are converted from the type declared in the MXBean
interface into the corresponding mapped type, and the return value
is converted from the mapped type into the declared type. For
example, with the method

public List<String> reverse(List<String> list);

and given that the mapped type for

List<String>

is

String[]

, a call to

proxy.reverse(someList)

will convert

someList

from a

List<String>

to a

String[]

,
call the MBean operation

reverse

, then convert the returned

String[]

into a

List<String>

.

The method Object.toString(), Object.hashCode(), or
Object.equals(Object), when invoked on a proxy using this
invocation handler, is forwarded to the MBean server as a method on
the proxied MBean only if it appears in one of the proxy's
interfaces. For a proxy created with

JMX.newMBeanProxy

or

JMX.newMXBeanProxy

, this means that the method must appear in the
Standard MBean or MXBean interface. Otherwise these methods have
the following behavior:

- toString() returns a string representation of the proxy

hashCode() returns a hash code for the proxy such
that two equal proxies have the same hash code

equals(Object)
returns true if and only if the Object argument is of the same
proxy class as this proxy, with an MBeanServerInvocationHandler
that has the same MBeanServerConnection and ObjectName; if one
of the

MBeanServerInvocationHandler

s was constructed with
a

Class

argument then the other must have been constructed
with the same

Class

for

equals

to return true.

InvocationHandler

that forwards methods in an MBean's
management interface through the MBean server to the MBean.

Given an

MBeanServerConnection

, the

ObjectName

of an MBean within that MBean server, and a Java interface

Intf

that describes the management interface of the
MBean using the patterns for a Standard MBean or an MXBean, this
class can be used to construct a proxy for the MBean. The proxy
implements the interface

Intf

such that all of its
methods are forwarded through the MBean server to the MBean.

If the

InvocationHandler

is for an MXBean, then the parameters of
a method are converted from the type declared in the MXBean
interface into the corresponding mapped type, and the return value
is converted from the mapped type into the declared type. For
example, with the method

public List<String> reverse(List<String> list);

and given that the mapped type for

List<String>

is

String[]

, a call to

proxy.reverse(someList)

will convert

someList

from a

List<String>

to a

String[]

,
call the MBean operation

reverse

, then convert the returned

String[]

into a

List<String>

.

The method Object.toString(), Object.hashCode(), or
Object.equals(Object), when invoked on a proxy using this
invocation handler, is forwarded to the MBean server as a method on
the proxied MBean only if it appears in one of the proxy's
interfaces. For a proxy created with

JMX.newMBeanProxy

or

JMX.newMXBeanProxy

, this means that the method must appear in the
Standard MBean or MXBean interface. Otherwise these methods have
the following behavior:

- toString() returns a string representation of the proxy

hashCode() returns a hash code for the proxy such
that two equal proxies have the same hash code

equals(Object)
returns true if and only if the Object argument is of the same
proxy class as this proxy, with an MBeanServerInvocationHandler
that has the same MBeanServerConnection and ObjectName; if one
of the

MBeanServerInvocationHandler

s was constructed with
a

Class

argument then the other must have been constructed
with the same

Class

for

equals

to return true.

toString() returns a string representation of the proxy

hashCode() returns a hash code for the proxy such
that two equal proxies have the same hash code

equals(Object)
returns true if and only if the Object argument is of the same
proxy class as this proxy, with an MBeanServerInvocationHandler
that has the same MBeanServerConnection and ObjectName; if one
of the

MBeanServerInvocationHandler

s was constructed with
a

Class

argument then the other must have been constructed
with the same

Class

for

equals

to return true.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MBeanServerInvocationHandler

​(

MBeanServerConnection

connection,

ObjectName

objectName)

Invocation handler that forwards methods through an MBean
server to a Standard MBean.

MBeanServerInvocationHandler

​(

MBeanServerConnection

connection,

ObjectName

objectName,
boolean isMXBean)

Invocation handler that can forward methods through an MBean
server to a Standard MBean or MXBean.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MBeanServerConnection

getMBeanServerConnection

()

The MBean server connection through which the methods of
a proxy using this handler are forwarded.

ObjectName

getObjectName

()

The name of the MBean within the MBean server to which methods
are forwarded.

boolean

isMXBean

()

If true, the proxy is for an MXBean, and appropriate mappings
are applied to method parameters and return values.

static <T> T

newProxyInstance

​(

MBeanServerConnection

connection,

ObjectName

objectName,

Class

<T> interfaceClass,
boolean notificationBroadcaster)

Return a proxy that implements the given interface by
forwarding its methods through the given MBean server to the
named MBean.

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

- Methods declared in interface java.lang.reflect.

InvocationHandler

invoke

Constructor Summary

Constructors

Constructor

Description

MBeanServerInvocationHandler

​(

MBeanServerConnection

connection,

ObjectName

objectName)

Invocation handler that forwards methods through an MBean
server to a Standard MBean.

MBeanServerInvocationHandler

​(

MBeanServerConnection

connection,

ObjectName

objectName,
boolean isMXBean)

Invocation handler that can forward methods through an MBean
server to a Standard MBean or MXBean.

---

#### Constructor Summary

Invocation handler that forwards methods through an MBean
server to a Standard MBean.

Invocation handler that can forward methods through an MBean
server to a Standard MBean or MXBean.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MBeanServerConnection

getMBeanServerConnection

()

The MBean server connection through which the methods of
a proxy using this handler are forwarded.

ObjectName

getObjectName

()

The name of the MBean within the MBean server to which methods
are forwarded.

boolean

isMXBean

()

If true, the proxy is for an MXBean, and appropriate mappings
are applied to method parameters and return values.

static <T> T

newProxyInstance

​(

MBeanServerConnection

connection,

ObjectName

objectName,

Class

<T> interfaceClass,
boolean notificationBroadcaster)

Return a proxy that implements the given interface by
forwarding its methods through the given MBean server to the
named MBean.

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

- Methods declared in interface java.lang.reflect.

InvocationHandler

invoke

---

#### Method Summary

The MBean server connection through which the methods of
a proxy using this handler are forwarded.

The name of the MBean within the MBean server to which methods
are forwarded.

If true, the proxy is for an MXBean, and appropriate mappings
are applied to method parameters and return values.

Return a proxy that implements the given interface by
forwarding its methods through the given MBean server to the
named MBean.

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

Methods declared in interface java.lang.reflect.

InvocationHandler

invoke

---

#### Methods declared in interface java.lang.reflect. InvocationHandler

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MBeanServerInvocationHandler

```java
public MBeanServerInvocationHandler​(
MBeanServerConnection
connection,

ObjectName
objectName)
```

Invocation handler that forwards methods through an MBean
server to a Standard MBean. This constructor may be called
instead of relying on

JMX.newMBeanProxy

, for instance if you need to supply a
different

ClassLoader

to

Proxy.newProxyInstance

.

This constructor is not appropriate for an MXBean. Use

MBeanServerInvocationHandler(MBeanServerConnection,
ObjectName, boolean)

for that. This constructor is equivalent
to

new MBeanServerInvocationHandler(connection,
objectName, false)

.

**Parameters:** connection

- the MBean server connection through which all
methods of a proxy using this handler will be forwarded.
**Parameters:** objectName

- the name of the MBean within the MBean server
to which methods will be forwarded.

- MBeanServerInvocationHandler

```java
public MBeanServerInvocationHandler​(
MBeanServerConnection
connection,

ObjectName
objectName,
boolean isMXBean)
```

Invocation handler that can forward methods through an MBean
server to a Standard MBean or MXBean. This constructor may be called
instead of relying on

JMX.newMXBeanProxy

, for instance if you need to supply a
different

ClassLoader

to

Proxy.newProxyInstance

.

**Parameters:** connection

- the MBean server connection through which all
methods of a proxy using this handler will be forwarded.
**Parameters:** objectName

- the name of the MBean within the MBean server
to which methods will be forwarded.
**Parameters:** isMXBean

- if true, the proxy is for an

MXBean

, and
appropriate mappings will be applied to method parameters and return
values.
**Since:** 1.6

============ METHOD DETAIL ==========

- Method Detail

- getMBeanServerConnection

```java
public
MBeanServerConnection
getMBeanServerConnection()
```

The MBean server connection through which the methods of
a proxy using this handler are forwarded.

**Returns:** the MBean server connection.
**Since:** 1.6

- getObjectName

```java
public
ObjectName
getObjectName()
```

The name of the MBean within the MBean server to which methods
are forwarded.

**Returns:** the object name.
**Since:** 1.6

- isMXBean

```java
public boolean isMXBean()
```

If true, the proxy is for an MXBean, and appropriate mappings
are applied to method parameters and return values.

**Returns:** whether the proxy is for an MXBean.
**Since:** 1.6

- newProxyInstance

```java
public static <T> T newProxyInstance​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass,
boolean notificationBroadcaster)
```

Return a proxy that implements the given interface by
forwarding its methods through the given MBean server to the
named MBean. As of 1.6, the methods

JMX.newMBeanProxy(MBeanServerConnection, ObjectName, Class)

and

JMX.newMBeanProxy(MBeanServerConnection, ObjectName, Class,
boolean)

are preferred to this method.

This method is equivalent to

Proxy.newProxyInstance

(interfaceClass.getClassLoader(),
interfaces, handler)

. Here

handler

is the
result of

new
MBeanServerInvocationHandler(connection, objectName)

, and

interfaces

is an array that has one element if

notificationBroadcaster

is false and two if it is
true. The first element of

interfaces

is

interfaceClass

and the second, if present, is

NotificationEmitter.class

.

**Type Parameters:** T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMBean.class

, for example,
then the return type is

MyMBean

.
**Parameters:** connection

- the MBean server to forward to.
**Parameters:** objectName

- the name of the MBean within

connection

to forward to.
**Parameters:** interfaceClass

- the management interface that the MBean
exports, which will also be implemented by the returned proxy.
**Parameters:** notificationBroadcaster

- make the returned proxy
implement

NotificationEmitter

by forwarding its methods
via

connection

. A call to

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

on the proxy will
result in a call to

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

, and likewise
for the other methods of

NotificationBroadcaster

and

NotificationEmitter

.
**Returns:** the new proxy instance.
**See Also:** JMX.newMBeanProxy(MBeanServerConnection, ObjectName, Class, boolean)

Constructor Detail

- MBeanServerInvocationHandler

```java
public MBeanServerInvocationHandler​(
MBeanServerConnection
connection,

ObjectName
objectName)
```

Invocation handler that forwards methods through an MBean
server to a Standard MBean. This constructor may be called
instead of relying on

JMX.newMBeanProxy

, for instance if you need to supply a
different

ClassLoader

to

Proxy.newProxyInstance

.

This constructor is not appropriate for an MXBean. Use

MBeanServerInvocationHandler(MBeanServerConnection,
ObjectName, boolean)

for that. This constructor is equivalent
to

new MBeanServerInvocationHandler(connection,
objectName, false)

.

**Parameters:** connection

- the MBean server connection through which all
methods of a proxy using this handler will be forwarded.
**Parameters:** objectName

- the name of the MBean within the MBean server
to which methods will be forwarded.

- MBeanServerInvocationHandler

```java
public MBeanServerInvocationHandler​(
MBeanServerConnection
connection,

ObjectName
objectName,
boolean isMXBean)
```

Invocation handler that can forward methods through an MBean
server to a Standard MBean or MXBean. This constructor may be called
instead of relying on

JMX.newMXBeanProxy

, for instance if you need to supply a
different

ClassLoader

to

Proxy.newProxyInstance

.

**Parameters:** connection

- the MBean server connection through which all
methods of a proxy using this handler will be forwarded.
**Parameters:** objectName

- the name of the MBean within the MBean server
to which methods will be forwarded.
**Parameters:** isMXBean

- if true, the proxy is for an

MXBean

, and
appropriate mappings will be applied to method parameters and return
values.
**Since:** 1.6

---

#### Constructor Detail

MBeanServerInvocationHandler

```java
public MBeanServerInvocationHandler​(
MBeanServerConnection
connection,

ObjectName
objectName)
```

Invocation handler that forwards methods through an MBean
server to a Standard MBean. This constructor may be called
instead of relying on

JMX.newMBeanProxy

, for instance if you need to supply a
different

ClassLoader

to

Proxy.newProxyInstance

.

This constructor is not appropriate for an MXBean. Use

MBeanServerInvocationHandler(MBeanServerConnection,
ObjectName, boolean)

for that. This constructor is equivalent
to

new MBeanServerInvocationHandler(connection,
objectName, false)

.

**Parameters:** connection

- the MBean server connection through which all
methods of a proxy using this handler will be forwarded.
**Parameters:** objectName

- the name of the MBean within the MBean server
to which methods will be forwarded.

---

#### MBeanServerInvocationHandler

public MBeanServerInvocationHandler​(

MBeanServerConnection

connection,

ObjectName

objectName)

Invocation handler that forwards methods through an MBean
server to a Standard MBean. This constructor may be called
instead of relying on

JMX.newMBeanProxy

, for instance if you need to supply a
different

ClassLoader

to

Proxy.newProxyInstance

.

This constructor is not appropriate for an MXBean. Use

MBeanServerInvocationHandler(MBeanServerConnection,
ObjectName, boolean)

for that. This constructor is equivalent
to

new MBeanServerInvocationHandler(connection,
objectName, false)

.

Invocation handler that forwards methods through an MBean
server to a Standard MBean. This constructor may be called
instead of relying on

JMX.newMBeanProxy

, for instance if you need to supply a
different

ClassLoader

to

Proxy.newProxyInstance

.

This constructor is not appropriate for an MXBean. Use

MBeanServerInvocationHandler(MBeanServerConnection,
ObjectName, boolean)

for that. This constructor is equivalent
to

new MBeanServerInvocationHandler(connection,
objectName, false)

.

MBeanServerInvocationHandler

```java
public MBeanServerInvocationHandler​(
MBeanServerConnection
connection,

ObjectName
objectName,
boolean isMXBean)
```

Invocation handler that can forward methods through an MBean
server to a Standard MBean or MXBean. This constructor may be called
instead of relying on

JMX.newMXBeanProxy

, for instance if you need to supply a
different

ClassLoader

to

Proxy.newProxyInstance

.

**Parameters:** connection

- the MBean server connection through which all
methods of a proxy using this handler will be forwarded.
**Parameters:** objectName

- the name of the MBean within the MBean server
to which methods will be forwarded.
**Parameters:** isMXBean

- if true, the proxy is for an

MXBean

, and
appropriate mappings will be applied to method parameters and return
values.
**Since:** 1.6

---

#### MBeanServerInvocationHandler

public MBeanServerInvocationHandler​(

MBeanServerConnection

connection,

ObjectName

objectName,
boolean isMXBean)

Invocation handler that can forward methods through an MBean
server to a Standard MBean or MXBean. This constructor may be called
instead of relying on

JMX.newMXBeanProxy

, for instance if you need to supply a
different

ClassLoader

to

Proxy.newProxyInstance

.

Method Detail

- getMBeanServerConnection

```java
public
MBeanServerConnection
getMBeanServerConnection()
```

The MBean server connection through which the methods of
a proxy using this handler are forwarded.

**Returns:** the MBean server connection.
**Since:** 1.6

- getObjectName

```java
public
ObjectName
getObjectName()
```

The name of the MBean within the MBean server to which methods
are forwarded.

**Returns:** the object name.
**Since:** 1.6

- isMXBean

```java
public boolean isMXBean()
```

If true, the proxy is for an MXBean, and appropriate mappings
are applied to method parameters and return values.

**Returns:** whether the proxy is for an MXBean.
**Since:** 1.6

- newProxyInstance

```java
public static <T> T newProxyInstance​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass,
boolean notificationBroadcaster)
```

Return a proxy that implements the given interface by
forwarding its methods through the given MBean server to the
named MBean. As of 1.6, the methods

JMX.newMBeanProxy(MBeanServerConnection, ObjectName, Class)

and

JMX.newMBeanProxy(MBeanServerConnection, ObjectName, Class,
boolean)

are preferred to this method.

This method is equivalent to

Proxy.newProxyInstance

(interfaceClass.getClassLoader(),
interfaces, handler)

. Here

handler

is the
result of

new
MBeanServerInvocationHandler(connection, objectName)

, and

interfaces

is an array that has one element if

notificationBroadcaster

is false and two if it is
true. The first element of

interfaces

is

interfaceClass

and the second, if present, is

NotificationEmitter.class

.

**Type Parameters:** T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMBean.class

, for example,
then the return type is

MyMBean

.
**Parameters:** connection

- the MBean server to forward to.
**Parameters:** objectName

- the name of the MBean within

connection

to forward to.
**Parameters:** interfaceClass

- the management interface that the MBean
exports, which will also be implemented by the returned proxy.
**Parameters:** notificationBroadcaster

- make the returned proxy
implement

NotificationEmitter

by forwarding its methods
via

connection

. A call to

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

on the proxy will
result in a call to

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

, and likewise
for the other methods of

NotificationBroadcaster

and

NotificationEmitter

.
**Returns:** the new proxy instance.
**See Also:** JMX.newMBeanProxy(MBeanServerConnection, ObjectName, Class, boolean)

---

#### Method Detail

getMBeanServerConnection

```java
public
MBeanServerConnection
getMBeanServerConnection()
```

The MBean server connection through which the methods of
a proxy using this handler are forwarded.

**Returns:** the MBean server connection.
**Since:** 1.6

---

#### getMBeanServerConnection

public

MBeanServerConnection

getMBeanServerConnection()

The MBean server connection through which the methods of
a proxy using this handler are forwarded.

getObjectName

```java
public
ObjectName
getObjectName()
```

The name of the MBean within the MBean server to which methods
are forwarded.

**Returns:** the object name.
**Since:** 1.6

---

#### getObjectName

public

ObjectName

getObjectName()

The name of the MBean within the MBean server to which methods
are forwarded.

isMXBean

```java
public boolean isMXBean()
```

If true, the proxy is for an MXBean, and appropriate mappings
are applied to method parameters and return values.

**Returns:** whether the proxy is for an MXBean.
**Since:** 1.6

---

#### isMXBean

public boolean isMXBean()

If true, the proxy is for an MXBean, and appropriate mappings
are applied to method parameters and return values.

newProxyInstance

```java
public static <T> T newProxyInstance​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass,
boolean notificationBroadcaster)
```

Return a proxy that implements the given interface by
forwarding its methods through the given MBean server to the
named MBean. As of 1.6, the methods

JMX.newMBeanProxy(MBeanServerConnection, ObjectName, Class)

and

JMX.newMBeanProxy(MBeanServerConnection, ObjectName, Class,
boolean)

are preferred to this method.

This method is equivalent to

Proxy.newProxyInstance

(interfaceClass.getClassLoader(),
interfaces, handler)

. Here

handler

is the
result of

new
MBeanServerInvocationHandler(connection, objectName)

, and

interfaces

is an array that has one element if

notificationBroadcaster

is false and two if it is
true. The first element of

interfaces

is

interfaceClass

and the second, if present, is

NotificationEmitter.class

.

**Type Parameters:** T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMBean.class

, for example,
then the return type is

MyMBean

.
**Parameters:** connection

- the MBean server to forward to.
**Parameters:** objectName

- the name of the MBean within

connection

to forward to.
**Parameters:** interfaceClass

- the management interface that the MBean
exports, which will also be implemented by the returned proxy.
**Parameters:** notificationBroadcaster

- make the returned proxy
implement

NotificationEmitter

by forwarding its methods
via

connection

. A call to

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

on the proxy will
result in a call to

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

, and likewise
for the other methods of

NotificationBroadcaster

and

NotificationEmitter

.
**Returns:** the new proxy instance.
**See Also:** JMX.newMBeanProxy(MBeanServerConnection, ObjectName, Class, boolean)

---

#### newProxyInstance

public static <T> T newProxyInstance​(

MBeanServerConnection

connection,

ObjectName

objectName,

Class

<T> interfaceClass,
boolean notificationBroadcaster)

Return a proxy that implements the given interface by
forwarding its methods through the given MBean server to the
named MBean. As of 1.6, the methods

JMX.newMBeanProxy(MBeanServerConnection, ObjectName, Class)

and

JMX.newMBeanProxy(MBeanServerConnection, ObjectName, Class,
boolean)

are preferred to this method.

This method is equivalent to

Proxy.newProxyInstance

(interfaceClass.getClassLoader(),
interfaces, handler)

. Here

handler

is the
result of

new
MBeanServerInvocationHandler(connection, objectName)

, and

interfaces

is an array that has one element if

notificationBroadcaster

is false and two if it is
true. The first element of

interfaces

is

interfaceClass

and the second, if present, is

NotificationEmitter.class

.

Return a proxy that implements the given interface by
forwarding its methods through the given MBean server to the
named MBean. As of 1.6, the methods

JMX.newMBeanProxy(MBeanServerConnection, ObjectName, Class)

and

JMX.newMBeanProxy(MBeanServerConnection, ObjectName, Class,
boolean)

are preferred to this method.

This method is equivalent to

Proxy.newProxyInstance

(interfaceClass.getClassLoader(),
interfaces, handler)

. Here

handler

is the
result of

new
MBeanServerInvocationHandler(connection, objectName)

, and

interfaces

is an array that has one element if

notificationBroadcaster

is false and two if it is
true. The first element of

interfaces

is

interfaceClass

and the second, if present, is

NotificationEmitter.class

.

---

