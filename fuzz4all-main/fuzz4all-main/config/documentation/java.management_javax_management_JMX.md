# Class JMX

**Source:** `java.management\javax\management\JMX.html`

### Class Description

```java
public class
JMX

extends
Object
```

Static methods from the JMX API. There are no instances of this class.

**Since:** 1.6

---

### Field Details

#### public static final
String
DEFAULT_VALUE_FIELD

The name of the

defaultValue

field.

**See Also:**
- Constant Field Values

---

#### public static final
String
IMMUTABLE_INFO_FIELD

The name of the

immutableInfo

field.

**See Also:**
- Constant Field Values

---

#### public static final
String
INTERFACE_CLASS_NAME_FIELD

The name of the

interfaceClassName

field.

**See Also:**
- Constant Field Values

---

#### public static final
String
LEGAL_VALUES_FIELD

The name of the

legalValues

field.

**See Also:**
- Constant Field Values

---

#### public static final
String
MAX_VALUE_FIELD

The name of the

maxValue

field.

**See Also:**
- Constant Field Values

---

#### public static final
String
MIN_VALUE_FIELD

The name of the

minValue

field.

**See Also:**
- Constant Field Values

---

#### public static final
String
MXBEAN_FIELD

The name of the

mxbean

field.

**See Also:**
- Constant Field Values

---

#### public static final
String
OPEN_TYPE_FIELD

The name of the

openType

field.

**See Also:**
- Constant Field Values

---

#### public static final
String
ORIGINAL_TYPE_FIELD

The name of the

originalType

field.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### public static <T> T newMBeanProxy​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass)

Make a proxy for a Standard MBean in a local or remote
MBean Server.

If you have an MBean Server

mbs

containing an MBean
with

ObjectName

name

, and if the MBean's
management interface is described by the Java interface

MyMBean

, you can construct a proxy for the MBean like
this:

```java
MyMBean proxy = JMX.newMBeanProxy(mbs, name, MyMBean.class);
```

Suppose, for example,

MyMBean

looks like this:

```java
public interface MyMBean {
public String getSomeAttribute();
public void setSomeAttribute(String value);
public void someOperation(String param1, int param2);
}
```

Then you can execute:

- proxy.getSomeAttribute()

which will result in a
call to

mbs.

getAttribute

(name, "SomeAttribute")

.

proxy.setSomeAttribute("whatever")

which will result
in a call to

mbs.

setAttribute

(name, new Attribute("SomeAttribute", "whatever"))

.

proxy.someOperation("param1", 2)

which will be
translated into a call to

mbs.

invoke

(name, "someOperation", <etc>)

.

The object returned by this method is a

Proxy

whose

InvocationHandler

is an

MBeanServerInvocationHandler

.

This method is equivalent to

newMBeanProxy(connection, objectName, interfaceClass,
false)

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

**Returns:**
- the new proxy instance.

**Throws:**
- IllegalArgumentException

- if

interfaceClass

is not
a

compliant MBean
interface

**Type Parameters:**
- T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMBean.class

, for
example, then the return type is

MyMBean

.

---

#### public static <T> T newMBeanProxy​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass,
boolean notificationEmitter)

Make a proxy for a Standard MBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

This method behaves the same as

newMBeanProxy(MBeanServerConnection, ObjectName, Class)

, but
additionally, if

notificationEmitter

is

true

, then the MBean is assumed to be a

NotificationBroadcaster

or

NotificationEmitter

and the
returned proxy will implement

NotificationEmitter

as
well as

interfaceClass

. A call to

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

on the proxy
will result in a call to

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

, and
likewise for the other methods of

NotificationBroadcaster

and

NotificationEmitter

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
- notificationEmitter

- make the returned proxy
implement

NotificationEmitter

by forwarding its methods
via

connection

.

**Returns:**
- the new proxy instance.

**Throws:**
- IllegalArgumentException

- if

interfaceClass

is not
a

compliant MBean
interface

**Type Parameters:**
- T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMBean.class

, for
example, then the return type is

MyMBean

.

---

#### public static <T> T newMXBeanProxy​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass)

Make a proxy for an MXBean in a local or remote MBean Server.

If you have an MBean Server

mbs

containing an
MXBean with

ObjectName

name

, and if the
MXBean's management interface is described by the Java
interface

MyMXBean

, you can construct a proxy for
the MXBean like this:

```java
MyMXBean proxy = JMX.newMXBeanProxy(mbs, name, MyMXBean.class);
```

Suppose, for example,

MyMXBean

looks like this:

```java
public interface MyMXBean {
public String getSimpleAttribute();
public void setSimpleAttribute(String value);
public
MemoryUsage
getMappedAttribute();
public void setMappedAttribute(MemoryUsage memoryUsage);
public MemoryUsage someOperation(String param1, MemoryUsage param2);
}
```

Then:

- proxy.getSimpleAttribute()

will result in a
call to

mbs.

getAttribute

(name, "SimpleAttribute")

.

proxy.setSimpleAttribute("whatever")

will result
in a call to

mbs.

setAttribute

(name,
new Attribute("SimpleAttribute", "whatever"))

.

Because

String

is a

simple type

, in the
sense of

SimpleType

, it
is not changed in the context of an MXBean. The MXBean
proxy behaves the same as a Standard MBean proxy (see

newMBeanProxy

) for the attribute

SimpleAttribute

.

proxy.getMappedAttribute()

will result in a call
to

mbs.getAttribute("MappedAttribute")

. The MXBean
mapping rules mean that the actual type of the attribute

MappedAttribute

will be

CompositeData

and
that is what the

mbs.getAttribute

call will return.
The proxy will then convert the

CompositeData

back into
the expected type

MemoryUsage

using the MXBean mapping
rules.

Similarly,

proxy.setMappedAttribute(memoryUsage)

will convert the

MemoryUsage

argument into a

CompositeData

before calling

mbs.setAttribute

.

proxy.someOperation("whatever", memoryUsage)

will convert the

MemoryUsage

argument into a

CompositeData

and call

mbs.invoke

. The value returned
by

mbs.invoke

will be also be a

CompositeData

,
and the proxy will convert this into the expected type

MemoryUsage

using the MXBean mapping rules.

The object returned by this method is a

Proxy

whose

InvocationHandler

is an

MBeanServerInvocationHandler

.

This method is equivalent to

newMXBeanProxy(connection, objectName, interfaceClass,
false)

.

**Parameters:**
- connection

- the MBean server to forward to.
- objectName

- the name of the MBean within

connection

to forward to.
- interfaceClass

- the MXBean interface,
which will also be implemented by the returned proxy.

**Returns:**
- the new proxy instance.

**Throws:**
- IllegalArgumentException

- if

interfaceClass

is not
a

compliant MXBean interface

**Type Parameters:**
- T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMXBean.class

, for
example, then the return type is

MyMXBean

.

---

#### public static <T> T newMXBeanProxy​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass,
boolean notificationEmitter)

Make a proxy for an MXBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

This method behaves the same as

newMXBeanProxy(MBeanServerConnection, ObjectName, Class)

, but
additionally, if

notificationEmitter

is

true

, then the MXBean is assumed to be a

NotificationBroadcaster

or

NotificationEmitter

and the
returned proxy will implement

NotificationEmitter

as
well as

interfaceClass

. A call to

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

on the proxy
will result in a call to

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

, and
likewise for the other methods of

NotificationBroadcaster

and

NotificationEmitter

.

**Parameters:**
- connection

- the MBean server to forward to.
- objectName

- the name of the MBean within

connection

to forward to.
- interfaceClass

- the MXBean interface,
which will also be implemented by the returned proxy.
- notificationEmitter

- make the returned proxy
implement

NotificationEmitter

by forwarding its methods
via

connection

.

**Returns:**
- the new proxy instance.

**Throws:**
- IllegalArgumentException

- if

interfaceClass

is not
a

compliant MXBean interface

**Type Parameters:**
- T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMXBean.class

, for
example, then the return type is

MyMXBean

.

---

#### public static boolean isMXBeanInterface​(
Class
<?> interfaceClass)

Test whether an interface is an MXBean interface.
An interface is an MXBean interface if it is public,
annotated

@MXBean

or

@MXBean(true)

or if it does not have an

@MXBean

annotation
and its name ends with "

MXBean

".

**Parameters:**
- interfaceClass

- The candidate interface.

**Returns:**
- true if

interfaceClass

is a

compliant MXBean interface

**Throws:**
- NullPointerException

- if

interfaceClass

is null.

---

### Additional Sections

#### Class JMX

java.lang.Object

- javax.management.JMX

javax.management.JMX

```java
public class
JMX

extends
Object
```

Static methods from the JMX API. There are no instances of this class.

**Since:** 1.6

public class

JMX

extends

Object

Static methods from the JMX API. There are no instances of this class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

DEFAULT_VALUE_FIELD

The name of the

defaultValue

field.

static

String

IMMUTABLE_INFO_FIELD

The name of the

immutableInfo

field.

static

String

INTERFACE_CLASS_NAME_FIELD

The name of the

interfaceClassName

field.

static

String

LEGAL_VALUES_FIELD

The name of the

legalValues

field.

static

String

MAX_VALUE_FIELD

The name of the

maxValue

field.

static

String

MIN_VALUE_FIELD

The name of the

minValue

field.

static

String

MXBEAN_FIELD

The name of the

mxbean

field.

static

String

OPEN_TYPE_FIELD

The name of the

openType

field.

static

String

ORIGINAL_TYPE_FIELD

The name of the

originalType

field.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static boolean

isMXBeanInterface

​(

Class

<?> interfaceClass)

Test whether an interface is an MXBean interface.

static <T> T

newMBeanProxy

​(

MBeanServerConnection

connection,

ObjectName

objectName,

Class

<T> interfaceClass)

Make a proxy for a Standard MBean in a local or remote
MBean Server.

static <T> T

newMBeanProxy

​(

MBeanServerConnection

connection,

ObjectName

objectName,

Class

<T> interfaceClass,
boolean notificationEmitter)

Make a proxy for a Standard MBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

static <T> T

newMXBeanProxy

​(

MBeanServerConnection

connection,

ObjectName

objectName,

Class

<T> interfaceClass)

Make a proxy for an MXBean in a local or remote MBean Server.

static <T> T

newMXBeanProxy

​(

MBeanServerConnection

connection,

ObjectName

objectName,

Class

<T> interfaceClass,
boolean notificationEmitter)

Make a proxy for an MXBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

String

DEFAULT_VALUE_FIELD

The name of the

defaultValue

field.

static

String

IMMUTABLE_INFO_FIELD

The name of the

immutableInfo

field.

static

String

INTERFACE_CLASS_NAME_FIELD

The name of the

interfaceClassName

field.

static

String

LEGAL_VALUES_FIELD

The name of the

legalValues

field.

static

String

MAX_VALUE_FIELD

The name of the

maxValue

field.

static

String

MIN_VALUE_FIELD

The name of the

minValue

field.

static

String

MXBEAN_FIELD

The name of the

mxbean

field.

static

String

OPEN_TYPE_FIELD

The name of the

openType

field.

static

String

ORIGINAL_TYPE_FIELD

The name of the

originalType

field.

---

#### Field Summary

The name of the

defaultValue

field.

The name of the

immutableInfo

field.

The name of the

interfaceClassName

field.

The name of the

legalValues

field.

The name of the

maxValue

field.

The name of the

minValue

field.

The name of the

mxbean

field.

The name of the

openType

field.

The name of the

originalType

field.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static boolean

isMXBeanInterface

​(

Class

<?> interfaceClass)

Test whether an interface is an MXBean interface.

static <T> T

newMBeanProxy

​(

MBeanServerConnection

connection,

ObjectName

objectName,

Class

<T> interfaceClass)

Make a proxy for a Standard MBean in a local or remote
MBean Server.

static <T> T

newMBeanProxy

​(

MBeanServerConnection

connection,

ObjectName

objectName,

Class

<T> interfaceClass,
boolean notificationEmitter)

Make a proxy for a Standard MBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

static <T> T

newMXBeanProxy

​(

MBeanServerConnection

connection,

ObjectName

objectName,

Class

<T> interfaceClass)

Make a proxy for an MXBean in a local or remote MBean Server.

static <T> T

newMXBeanProxy

​(

MBeanServerConnection

connection,

ObjectName

objectName,

Class

<T> interfaceClass,
boolean notificationEmitter)

Make a proxy for an MXBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

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

---

#### Method Summary

Test whether an interface is an MXBean interface.

Make a proxy for a Standard MBean in a local or remote
MBean Server.

Make a proxy for a Standard MBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

Make a proxy for an MXBean in a local or remote MBean Server.

Make a proxy for an MXBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

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

============ FIELD DETAIL ===========

- Field Detail

- DEFAULT_VALUE_FIELD

```java
public static final
String
DEFAULT_VALUE_FIELD
```

The name of the

defaultValue

field.

**See Also:** Constant Field Values

- IMMUTABLE_INFO_FIELD

```java
public static final
String
IMMUTABLE_INFO_FIELD
```

The name of the

immutableInfo

field.

**See Also:** Constant Field Values

- INTERFACE_CLASS_NAME_FIELD

```java
public static final
String
INTERFACE_CLASS_NAME_FIELD
```

The name of the

interfaceClassName

field.

**See Also:** Constant Field Values

- LEGAL_VALUES_FIELD

```java
public static final
String
LEGAL_VALUES_FIELD
```

The name of the

legalValues

field.

**See Also:** Constant Field Values

- MAX_VALUE_FIELD

```java
public static final
String
MAX_VALUE_FIELD
```

The name of the

maxValue

field.

**See Also:** Constant Field Values

- MIN_VALUE_FIELD

```java
public static final
String
MIN_VALUE_FIELD
```

The name of the

minValue

field.

**See Also:** Constant Field Values

- MXBEAN_FIELD

```java
public static final
String
MXBEAN_FIELD
```

The name of the

mxbean

field.

**See Also:** Constant Field Values

- OPEN_TYPE_FIELD

```java
public static final
String
OPEN_TYPE_FIELD
```

The name of the

openType

field.

**See Also:** Constant Field Values

- ORIGINAL_TYPE_FIELD

```java
public static final
String
ORIGINAL_TYPE_FIELD
```

The name of the

originalType

field.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- newMBeanProxy

```java
public static <T> T newMBeanProxy​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass)
```

Make a proxy for a Standard MBean in a local or remote
MBean Server.

If you have an MBean Server

mbs

containing an MBean
with

ObjectName

name

, and if the MBean's
management interface is described by the Java interface

MyMBean

, you can construct a proxy for the MBean like
this:

```java
MyMBean proxy = JMX.newMBeanProxy(mbs, name, MyMBean.class);
```

Suppose, for example,

MyMBean

looks like this:

```java
public interface MyMBean {
public String getSomeAttribute();
public void setSomeAttribute(String value);
public void someOperation(String param1, int param2);
}
```

Then you can execute:

- proxy.getSomeAttribute()

which will result in a
call to

mbs.

getAttribute

(name, "SomeAttribute")

.

proxy.setSomeAttribute("whatever")

which will result
in a call to

mbs.

setAttribute

(name, new Attribute("SomeAttribute", "whatever"))

.

proxy.someOperation("param1", 2)

which will be
translated into a call to

mbs.

invoke

(name, "someOperation", <etc>)

.

The object returned by this method is a

Proxy

whose

InvocationHandler

is an

MBeanServerInvocationHandler

.

This method is equivalent to

newMBeanProxy(connection, objectName, interfaceClass,
false)

.

**Type Parameters:** T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMBean.class

, for
example, then the return type is

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
**Returns:** the new proxy instance.
**Throws:** IllegalArgumentException

- if

interfaceClass

is not
a

compliant MBean
interface

- newMBeanProxy

```java
public static <T> T newMBeanProxy​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass,
boolean notificationEmitter)
```

Make a proxy for a Standard MBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

This method behaves the same as

newMBeanProxy(MBeanServerConnection, ObjectName, Class)

, but
additionally, if

notificationEmitter

is

true

, then the MBean is assumed to be a

NotificationBroadcaster

or

NotificationEmitter

and the
returned proxy will implement

NotificationEmitter

as
well as

interfaceClass

. A call to

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

on the proxy
will result in a call to

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

, and
likewise for the other methods of

NotificationBroadcaster

and

NotificationEmitter

.

**Type Parameters:** T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMBean.class

, for
example, then the return type is

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
**Parameters:** notificationEmitter

- make the returned proxy
implement

NotificationEmitter

by forwarding its methods
via

connection

.
**Returns:** the new proxy instance.
**Throws:** IllegalArgumentException

- if

interfaceClass

is not
a

compliant MBean
interface

- newMXBeanProxy

```java
public static <T> T newMXBeanProxy​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass)
```

Make a proxy for an MXBean in a local or remote MBean Server.

If you have an MBean Server

mbs

containing an
MXBean with

ObjectName

name

, and if the
MXBean's management interface is described by the Java
interface

MyMXBean

, you can construct a proxy for
the MXBean like this:

```java
MyMXBean proxy = JMX.newMXBeanProxy(mbs, name, MyMXBean.class);
```

Suppose, for example,

MyMXBean

looks like this:

```java
public interface MyMXBean {
public String getSimpleAttribute();
public void setSimpleAttribute(String value);
public
MemoryUsage
getMappedAttribute();
public void setMappedAttribute(MemoryUsage memoryUsage);
public MemoryUsage someOperation(String param1, MemoryUsage param2);
}
```

Then:

- proxy.getSimpleAttribute()

will result in a
call to

mbs.

getAttribute

(name, "SimpleAttribute")

.

proxy.setSimpleAttribute("whatever")

will result
in a call to

mbs.

setAttribute

(name,
new Attribute("SimpleAttribute", "whatever"))

.

Because

String

is a

simple type

, in the
sense of

SimpleType

, it
is not changed in the context of an MXBean. The MXBean
proxy behaves the same as a Standard MBean proxy (see

newMBeanProxy

) for the attribute

SimpleAttribute

.

proxy.getMappedAttribute()

will result in a call
to

mbs.getAttribute("MappedAttribute")

. The MXBean
mapping rules mean that the actual type of the attribute

MappedAttribute

will be

CompositeData

and
that is what the

mbs.getAttribute

call will return.
The proxy will then convert the

CompositeData

back into
the expected type

MemoryUsage

using the MXBean mapping
rules.

Similarly,

proxy.setMappedAttribute(memoryUsage)

will convert the

MemoryUsage

argument into a

CompositeData

before calling

mbs.setAttribute

.

proxy.someOperation("whatever", memoryUsage)

will convert the

MemoryUsage

argument into a

CompositeData

and call

mbs.invoke

. The value returned
by

mbs.invoke

will be also be a

CompositeData

,
and the proxy will convert this into the expected type

MemoryUsage

using the MXBean mapping rules.

The object returned by this method is a

Proxy

whose

InvocationHandler

is an

MBeanServerInvocationHandler

.

This method is equivalent to

newMXBeanProxy(connection, objectName, interfaceClass,
false)

.

**Type Parameters:** T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMXBean.class

, for
example, then the return type is

MyMXBean

.
**Parameters:** connection

- the MBean server to forward to.
**Parameters:** objectName

- the name of the MBean within

connection

to forward to.
**Parameters:** interfaceClass

- the MXBean interface,
which will also be implemented by the returned proxy.
**Returns:** the new proxy instance.
**Throws:** IllegalArgumentException

- if

interfaceClass

is not
a

compliant MXBean interface

- newMXBeanProxy

```java
public static <T> T newMXBeanProxy​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass,
boolean notificationEmitter)
```

Make a proxy for an MXBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

This method behaves the same as

newMXBeanProxy(MBeanServerConnection, ObjectName, Class)

, but
additionally, if

notificationEmitter

is

true

, then the MXBean is assumed to be a

NotificationBroadcaster

or

NotificationEmitter

and the
returned proxy will implement

NotificationEmitter

as
well as

interfaceClass

. A call to

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

on the proxy
will result in a call to

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

, and
likewise for the other methods of

NotificationBroadcaster

and

NotificationEmitter

.

**Type Parameters:** T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMXBean.class

, for
example, then the return type is

MyMXBean

.
**Parameters:** connection

- the MBean server to forward to.
**Parameters:** objectName

- the name of the MBean within

connection

to forward to.
**Parameters:** interfaceClass

- the MXBean interface,
which will also be implemented by the returned proxy.
**Parameters:** notificationEmitter

- make the returned proxy
implement

NotificationEmitter

by forwarding its methods
via

connection

.
**Returns:** the new proxy instance.
**Throws:** IllegalArgumentException

- if

interfaceClass

is not
a

compliant MXBean interface

- isMXBeanInterface

```java
public static boolean isMXBeanInterface​(
Class
<?> interfaceClass)
```

Test whether an interface is an MXBean interface.
An interface is an MXBean interface if it is public,
annotated

@MXBean

or

@MXBean(true)

or if it does not have an

@MXBean

annotation
and its name ends with "

MXBean

".

**Parameters:** interfaceClass

- The candidate interface.
**Returns:** true if

interfaceClass

is a

compliant MXBean interface
**Throws:** NullPointerException

- if

interfaceClass

is null.

Field Detail

- DEFAULT_VALUE_FIELD

```java
public static final
String
DEFAULT_VALUE_FIELD
```

The name of the

defaultValue

field.

**See Also:** Constant Field Values

- IMMUTABLE_INFO_FIELD

```java
public static final
String
IMMUTABLE_INFO_FIELD
```

The name of the

immutableInfo

field.

**See Also:** Constant Field Values

- INTERFACE_CLASS_NAME_FIELD

```java
public static final
String
INTERFACE_CLASS_NAME_FIELD
```

The name of the

interfaceClassName

field.

**See Also:** Constant Field Values

- LEGAL_VALUES_FIELD

```java
public static final
String
LEGAL_VALUES_FIELD
```

The name of the

legalValues

field.

**See Also:** Constant Field Values

- MAX_VALUE_FIELD

```java
public static final
String
MAX_VALUE_FIELD
```

The name of the

maxValue

field.

**See Also:** Constant Field Values

- MIN_VALUE_FIELD

```java
public static final
String
MIN_VALUE_FIELD
```

The name of the

minValue

field.

**See Also:** Constant Field Values

- MXBEAN_FIELD

```java
public static final
String
MXBEAN_FIELD
```

The name of the

mxbean

field.

**See Also:** Constant Field Values

- OPEN_TYPE_FIELD

```java
public static final
String
OPEN_TYPE_FIELD
```

The name of the

openType

field.

**See Also:** Constant Field Values

- ORIGINAL_TYPE_FIELD

```java
public static final
String
ORIGINAL_TYPE_FIELD
```

The name of the

originalType

field.

**See Also:** Constant Field Values

---

#### Field Detail

DEFAULT_VALUE_FIELD

```java
public static final
String
DEFAULT_VALUE_FIELD
```

The name of the

defaultValue

field.

**See Also:** Constant Field Values

---

#### DEFAULT_VALUE_FIELD

public static final

String

DEFAULT_VALUE_FIELD

The name of the

defaultValue

field.

IMMUTABLE_INFO_FIELD

```java
public static final
String
IMMUTABLE_INFO_FIELD
```

The name of the

immutableInfo

field.

**See Also:** Constant Field Values

---

#### IMMUTABLE_INFO_FIELD

public static final

String

IMMUTABLE_INFO_FIELD

The name of the

immutableInfo

field.

INTERFACE_CLASS_NAME_FIELD

```java
public static final
String
INTERFACE_CLASS_NAME_FIELD
```

The name of the

interfaceClassName

field.

**See Also:** Constant Field Values

---

#### INTERFACE_CLASS_NAME_FIELD

public static final

String

INTERFACE_CLASS_NAME_FIELD

The name of the

interfaceClassName

field.

LEGAL_VALUES_FIELD

```java
public static final
String
LEGAL_VALUES_FIELD
```

The name of the

legalValues

field.

**See Also:** Constant Field Values

---

#### LEGAL_VALUES_FIELD

public static final

String

LEGAL_VALUES_FIELD

The name of the

legalValues

field.

MAX_VALUE_FIELD

```java
public static final
String
MAX_VALUE_FIELD
```

The name of the

maxValue

field.

**See Also:** Constant Field Values

---

#### MAX_VALUE_FIELD

public static final

String

MAX_VALUE_FIELD

The name of the

maxValue

field.

MIN_VALUE_FIELD

```java
public static final
String
MIN_VALUE_FIELD
```

The name of the

minValue

field.

**See Also:** Constant Field Values

---

#### MIN_VALUE_FIELD

public static final

String

MIN_VALUE_FIELD

The name of the

minValue

field.

MXBEAN_FIELD

```java
public static final
String
MXBEAN_FIELD
```

The name of the

mxbean

field.

**See Also:** Constant Field Values

---

#### MXBEAN_FIELD

public static final

String

MXBEAN_FIELD

The name of the

mxbean

field.

OPEN_TYPE_FIELD

```java
public static final
String
OPEN_TYPE_FIELD
```

The name of the

openType

field.

**See Also:** Constant Field Values

---

#### OPEN_TYPE_FIELD

public static final

String

OPEN_TYPE_FIELD

The name of the

openType

field.

ORIGINAL_TYPE_FIELD

```java
public static final
String
ORIGINAL_TYPE_FIELD
```

The name of the

originalType

field.

**See Also:** Constant Field Values

---

#### ORIGINAL_TYPE_FIELD

public static final

String

ORIGINAL_TYPE_FIELD

The name of the

originalType

field.

Method Detail

- newMBeanProxy

```java
public static <T> T newMBeanProxy​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass)
```

Make a proxy for a Standard MBean in a local or remote
MBean Server.

If you have an MBean Server

mbs

containing an MBean
with

ObjectName

name

, and if the MBean's
management interface is described by the Java interface

MyMBean

, you can construct a proxy for the MBean like
this:

```java
MyMBean proxy = JMX.newMBeanProxy(mbs, name, MyMBean.class);
```

Suppose, for example,

MyMBean

looks like this:

```java
public interface MyMBean {
public String getSomeAttribute();
public void setSomeAttribute(String value);
public void someOperation(String param1, int param2);
}
```

Then you can execute:

- proxy.getSomeAttribute()

which will result in a
call to

mbs.

getAttribute

(name, "SomeAttribute")

.

proxy.setSomeAttribute("whatever")

which will result
in a call to

mbs.

setAttribute

(name, new Attribute("SomeAttribute", "whatever"))

.

proxy.someOperation("param1", 2)

which will be
translated into a call to

mbs.

invoke

(name, "someOperation", <etc>)

.

The object returned by this method is a

Proxy

whose

InvocationHandler

is an

MBeanServerInvocationHandler

.

This method is equivalent to

newMBeanProxy(connection, objectName, interfaceClass,
false)

.

**Type Parameters:** T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMBean.class

, for
example, then the return type is

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
**Returns:** the new proxy instance.
**Throws:** IllegalArgumentException

- if

interfaceClass

is not
a

compliant MBean
interface

- newMBeanProxy

```java
public static <T> T newMBeanProxy​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass,
boolean notificationEmitter)
```

Make a proxy for a Standard MBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

This method behaves the same as

newMBeanProxy(MBeanServerConnection, ObjectName, Class)

, but
additionally, if

notificationEmitter

is

true

, then the MBean is assumed to be a

NotificationBroadcaster

or

NotificationEmitter

and the
returned proxy will implement

NotificationEmitter

as
well as

interfaceClass

. A call to

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

on the proxy
will result in a call to

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

, and
likewise for the other methods of

NotificationBroadcaster

and

NotificationEmitter

.

**Type Parameters:** T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMBean.class

, for
example, then the return type is

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
**Parameters:** notificationEmitter

- make the returned proxy
implement

NotificationEmitter

by forwarding its methods
via

connection

.
**Returns:** the new proxy instance.
**Throws:** IllegalArgumentException

- if

interfaceClass

is not
a

compliant MBean
interface

- newMXBeanProxy

```java
public static <T> T newMXBeanProxy​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass)
```

Make a proxy for an MXBean in a local or remote MBean Server.

If you have an MBean Server

mbs

containing an
MXBean with

ObjectName

name

, and if the
MXBean's management interface is described by the Java
interface

MyMXBean

, you can construct a proxy for
the MXBean like this:

```java
MyMXBean proxy = JMX.newMXBeanProxy(mbs, name, MyMXBean.class);
```

Suppose, for example,

MyMXBean

looks like this:

```java
public interface MyMXBean {
public String getSimpleAttribute();
public void setSimpleAttribute(String value);
public
MemoryUsage
getMappedAttribute();
public void setMappedAttribute(MemoryUsage memoryUsage);
public MemoryUsage someOperation(String param1, MemoryUsage param2);
}
```

Then:

- proxy.getSimpleAttribute()

will result in a
call to

mbs.

getAttribute

(name, "SimpleAttribute")

.

proxy.setSimpleAttribute("whatever")

will result
in a call to

mbs.

setAttribute

(name,
new Attribute("SimpleAttribute", "whatever"))

.

Because

String

is a

simple type

, in the
sense of

SimpleType

, it
is not changed in the context of an MXBean. The MXBean
proxy behaves the same as a Standard MBean proxy (see

newMBeanProxy

) for the attribute

SimpleAttribute

.

proxy.getMappedAttribute()

will result in a call
to

mbs.getAttribute("MappedAttribute")

. The MXBean
mapping rules mean that the actual type of the attribute

MappedAttribute

will be

CompositeData

and
that is what the

mbs.getAttribute

call will return.
The proxy will then convert the

CompositeData

back into
the expected type

MemoryUsage

using the MXBean mapping
rules.

Similarly,

proxy.setMappedAttribute(memoryUsage)

will convert the

MemoryUsage

argument into a

CompositeData

before calling

mbs.setAttribute

.

proxy.someOperation("whatever", memoryUsage)

will convert the

MemoryUsage

argument into a

CompositeData

and call

mbs.invoke

. The value returned
by

mbs.invoke

will be also be a

CompositeData

,
and the proxy will convert this into the expected type

MemoryUsage

using the MXBean mapping rules.

The object returned by this method is a

Proxy

whose

InvocationHandler

is an

MBeanServerInvocationHandler

.

This method is equivalent to

newMXBeanProxy(connection, objectName, interfaceClass,
false)

.

**Type Parameters:** T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMXBean.class

, for
example, then the return type is

MyMXBean

.
**Parameters:** connection

- the MBean server to forward to.
**Parameters:** objectName

- the name of the MBean within

connection

to forward to.
**Parameters:** interfaceClass

- the MXBean interface,
which will also be implemented by the returned proxy.
**Returns:** the new proxy instance.
**Throws:** IllegalArgumentException

- if

interfaceClass

is not
a

compliant MXBean interface

- newMXBeanProxy

```java
public static <T> T newMXBeanProxy​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass,
boolean notificationEmitter)
```

Make a proxy for an MXBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

This method behaves the same as

newMXBeanProxy(MBeanServerConnection, ObjectName, Class)

, but
additionally, if

notificationEmitter

is

true

, then the MXBean is assumed to be a

NotificationBroadcaster

or

NotificationEmitter

and the
returned proxy will implement

NotificationEmitter

as
well as

interfaceClass

. A call to

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

on the proxy
will result in a call to

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

, and
likewise for the other methods of

NotificationBroadcaster

and

NotificationEmitter

.

**Type Parameters:** T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMXBean.class

, for
example, then the return type is

MyMXBean

.
**Parameters:** connection

- the MBean server to forward to.
**Parameters:** objectName

- the name of the MBean within

connection

to forward to.
**Parameters:** interfaceClass

- the MXBean interface,
which will also be implemented by the returned proxy.
**Parameters:** notificationEmitter

- make the returned proxy
implement

NotificationEmitter

by forwarding its methods
via

connection

.
**Returns:** the new proxy instance.
**Throws:** IllegalArgumentException

- if

interfaceClass

is not
a

compliant MXBean interface

- isMXBeanInterface

```java
public static boolean isMXBeanInterface​(
Class
<?> interfaceClass)
```

Test whether an interface is an MXBean interface.
An interface is an MXBean interface if it is public,
annotated

@MXBean

or

@MXBean(true)

or if it does not have an

@MXBean

annotation
and its name ends with "

MXBean

".

**Parameters:** interfaceClass

- The candidate interface.
**Returns:** true if

interfaceClass

is a

compliant MXBean interface
**Throws:** NullPointerException

- if

interfaceClass

is null.

---

#### Method Detail

newMBeanProxy

```java
public static <T> T newMBeanProxy​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass)
```

Make a proxy for a Standard MBean in a local or remote
MBean Server.

If you have an MBean Server

mbs

containing an MBean
with

ObjectName

name

, and if the MBean's
management interface is described by the Java interface

MyMBean

, you can construct a proxy for the MBean like
this:

```java
MyMBean proxy = JMX.newMBeanProxy(mbs, name, MyMBean.class);
```

Suppose, for example,

MyMBean

looks like this:

```java
public interface MyMBean {
public String getSomeAttribute();
public void setSomeAttribute(String value);
public void someOperation(String param1, int param2);
}
```

Then you can execute:

- proxy.getSomeAttribute()

which will result in a
call to

mbs.

getAttribute

(name, "SomeAttribute")

.

proxy.setSomeAttribute("whatever")

which will result
in a call to

mbs.

setAttribute

(name, new Attribute("SomeAttribute", "whatever"))

.

proxy.someOperation("param1", 2)

which will be
translated into a call to

mbs.

invoke

(name, "someOperation", <etc>)

.

The object returned by this method is a

Proxy

whose

InvocationHandler

is an

MBeanServerInvocationHandler

.

This method is equivalent to

newMBeanProxy(connection, objectName, interfaceClass,
false)

.

**Type Parameters:** T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMBean.class

, for
example, then the return type is

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
**Returns:** the new proxy instance.
**Throws:** IllegalArgumentException

- if

interfaceClass

is not
a

compliant MBean
interface

---

#### newMBeanProxy

public static <T> T newMBeanProxy​(

MBeanServerConnection

connection,

ObjectName

objectName,

Class

<T> interfaceClass)

Make a proxy for a Standard MBean in a local or remote
MBean Server.

If you have an MBean Server

mbs

containing an MBean
with

ObjectName

name

, and if the MBean's
management interface is described by the Java interface

MyMBean

, you can construct a proxy for the MBean like
this:

```java
MyMBean proxy = JMX.newMBeanProxy(mbs, name, MyMBean.class);
```

Suppose, for example,

MyMBean

looks like this:

```java
public interface MyMBean {
public String getSomeAttribute();
public void setSomeAttribute(String value);
public void someOperation(String param1, int param2);
}
```

Then you can execute:

- proxy.getSomeAttribute()

which will result in a
call to

mbs.

getAttribute

(name, "SomeAttribute")

.

proxy.setSomeAttribute("whatever")

which will result
in a call to

mbs.

setAttribute

(name, new Attribute("SomeAttribute", "whatever"))

.

proxy.someOperation("param1", 2)

which will be
translated into a call to

mbs.

invoke

(name, "someOperation", <etc>)

.

The object returned by this method is a

Proxy

whose

InvocationHandler

is an

MBeanServerInvocationHandler

.

This method is equivalent to

newMBeanProxy(connection, objectName, interfaceClass,
false)

.

Make a proxy for a Standard MBean in a local or remote
MBean Server.

If you have an MBean Server

mbs

containing an MBean
with

ObjectName

name

, and if the MBean's
management interface is described by the Java interface

MyMBean

, you can construct a proxy for the MBean like
this:

MyMBean proxy = JMX.newMBeanProxy(mbs, name, MyMBean.class);

Suppose, for example,

MyMBean

looks like this:

public interface MyMBean {
public String getSomeAttribute();
public void setSomeAttribute(String value);
public void someOperation(String param1, int param2);
}

Then you can execute:

proxy.getSomeAttribute()

which will result in a
call to

mbs.

getAttribute

(name, "SomeAttribute")

.

proxy.setSomeAttribute("whatever")

which will result
in a call to

mbs.

setAttribute

(name, new Attribute("SomeAttribute", "whatever"))

.

proxy.someOperation("param1", 2)

which will be
translated into a call to

mbs.

invoke

(name, "someOperation", <etc>)

.

The object returned by this method is a

Proxy

whose

InvocationHandler

is an

MBeanServerInvocationHandler

.

This method is equivalent to

newMBeanProxy(connection, objectName, interfaceClass,
false)

.

newMBeanProxy

```java
public static <T> T newMBeanProxy​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass,
boolean notificationEmitter)
```

Make a proxy for a Standard MBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

This method behaves the same as

newMBeanProxy(MBeanServerConnection, ObjectName, Class)

, but
additionally, if

notificationEmitter

is

true

, then the MBean is assumed to be a

NotificationBroadcaster

or

NotificationEmitter

and the
returned proxy will implement

NotificationEmitter

as
well as

interfaceClass

. A call to

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

on the proxy
will result in a call to

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

, and
likewise for the other methods of

NotificationBroadcaster

and

NotificationEmitter

.

**Type Parameters:** T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMBean.class

, for
example, then the return type is

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
**Parameters:** notificationEmitter

- make the returned proxy
implement

NotificationEmitter

by forwarding its methods
via

connection

.
**Returns:** the new proxy instance.
**Throws:** IllegalArgumentException

- if

interfaceClass

is not
a

compliant MBean
interface

---

#### newMBeanProxy

public static <T> T newMBeanProxy​(

MBeanServerConnection

connection,

ObjectName

objectName,

Class

<T> interfaceClass,
boolean notificationEmitter)

Make a proxy for a Standard MBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

This method behaves the same as

newMBeanProxy(MBeanServerConnection, ObjectName, Class)

, but
additionally, if

notificationEmitter

is

true

, then the MBean is assumed to be a

NotificationBroadcaster

or

NotificationEmitter

and the
returned proxy will implement

NotificationEmitter

as
well as

interfaceClass

. A call to

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

on the proxy
will result in a call to

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

, and
likewise for the other methods of

NotificationBroadcaster

and

NotificationEmitter

.

Make a proxy for a Standard MBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

This method behaves the same as

newMBeanProxy(MBeanServerConnection, ObjectName, Class)

, but
additionally, if

notificationEmitter

is

true

, then the MBean is assumed to be a

NotificationBroadcaster

or

NotificationEmitter

and the
returned proxy will implement

NotificationEmitter

as
well as

interfaceClass

. A call to

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

on the proxy
will result in a call to

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

, and
likewise for the other methods of

NotificationBroadcaster

and

NotificationEmitter

.

newMXBeanProxy

```java
public static <T> T newMXBeanProxy​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass)
```

Make a proxy for an MXBean in a local or remote MBean Server.

If you have an MBean Server

mbs

containing an
MXBean with

ObjectName

name

, and if the
MXBean's management interface is described by the Java
interface

MyMXBean

, you can construct a proxy for
the MXBean like this:

```java
MyMXBean proxy = JMX.newMXBeanProxy(mbs, name, MyMXBean.class);
```

Suppose, for example,

MyMXBean

looks like this:

```java
public interface MyMXBean {
public String getSimpleAttribute();
public void setSimpleAttribute(String value);
public
MemoryUsage
getMappedAttribute();
public void setMappedAttribute(MemoryUsage memoryUsage);
public MemoryUsage someOperation(String param1, MemoryUsage param2);
}
```

Then:

- proxy.getSimpleAttribute()

will result in a
call to

mbs.

getAttribute

(name, "SimpleAttribute")

.

proxy.setSimpleAttribute("whatever")

will result
in a call to

mbs.

setAttribute

(name,
new Attribute("SimpleAttribute", "whatever"))

.

Because

String

is a

simple type

, in the
sense of

SimpleType

, it
is not changed in the context of an MXBean. The MXBean
proxy behaves the same as a Standard MBean proxy (see

newMBeanProxy

) for the attribute

SimpleAttribute

.

proxy.getMappedAttribute()

will result in a call
to

mbs.getAttribute("MappedAttribute")

. The MXBean
mapping rules mean that the actual type of the attribute

MappedAttribute

will be

CompositeData

and
that is what the

mbs.getAttribute

call will return.
The proxy will then convert the

CompositeData

back into
the expected type

MemoryUsage

using the MXBean mapping
rules.

Similarly,

proxy.setMappedAttribute(memoryUsage)

will convert the

MemoryUsage

argument into a

CompositeData

before calling

mbs.setAttribute

.

proxy.someOperation("whatever", memoryUsage)

will convert the

MemoryUsage

argument into a

CompositeData

and call

mbs.invoke

. The value returned
by

mbs.invoke

will be also be a

CompositeData

,
and the proxy will convert this into the expected type

MemoryUsage

using the MXBean mapping rules.

The object returned by this method is a

Proxy

whose

InvocationHandler

is an

MBeanServerInvocationHandler

.

This method is equivalent to

newMXBeanProxy(connection, objectName, interfaceClass,
false)

.

**Type Parameters:** T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMXBean.class

, for
example, then the return type is

MyMXBean

.
**Parameters:** connection

- the MBean server to forward to.
**Parameters:** objectName

- the name of the MBean within

connection

to forward to.
**Parameters:** interfaceClass

- the MXBean interface,
which will also be implemented by the returned proxy.
**Returns:** the new proxy instance.
**Throws:** IllegalArgumentException

- if

interfaceClass

is not
a

compliant MXBean interface

---

#### newMXBeanProxy

public static <T> T newMXBeanProxy​(

MBeanServerConnection

connection,

ObjectName

objectName,

Class

<T> interfaceClass)

Make a proxy for an MXBean in a local or remote MBean Server.

If you have an MBean Server

mbs

containing an
MXBean with

ObjectName

name

, and if the
MXBean's management interface is described by the Java
interface

MyMXBean

, you can construct a proxy for
the MXBean like this:

```java
MyMXBean proxy = JMX.newMXBeanProxy(mbs, name, MyMXBean.class);
```

Suppose, for example,

MyMXBean

looks like this:

```java
public interface MyMXBean {
public String getSimpleAttribute();
public void setSimpleAttribute(String value);
public
MemoryUsage
getMappedAttribute();
public void setMappedAttribute(MemoryUsage memoryUsage);
public MemoryUsage someOperation(String param1, MemoryUsage param2);
}
```

Then:

- proxy.getSimpleAttribute()

will result in a
call to

mbs.

getAttribute

(name, "SimpleAttribute")

.

proxy.setSimpleAttribute("whatever")

will result
in a call to

mbs.

setAttribute

(name,
new Attribute("SimpleAttribute", "whatever"))

.

Because

String

is a

simple type

, in the
sense of

SimpleType

, it
is not changed in the context of an MXBean. The MXBean
proxy behaves the same as a Standard MBean proxy (see

newMBeanProxy

) for the attribute

SimpleAttribute

.

proxy.getMappedAttribute()

will result in a call
to

mbs.getAttribute("MappedAttribute")

. The MXBean
mapping rules mean that the actual type of the attribute

MappedAttribute

will be

CompositeData

and
that is what the

mbs.getAttribute

call will return.
The proxy will then convert the

CompositeData

back into
the expected type

MemoryUsage

using the MXBean mapping
rules.

Similarly,

proxy.setMappedAttribute(memoryUsage)

will convert the

MemoryUsage

argument into a

CompositeData

before calling

mbs.setAttribute

.

proxy.someOperation("whatever", memoryUsage)

will convert the

MemoryUsage

argument into a

CompositeData

and call

mbs.invoke

. The value returned
by

mbs.invoke

will be also be a

CompositeData

,
and the proxy will convert this into the expected type

MemoryUsage

using the MXBean mapping rules.

The object returned by this method is a

Proxy

whose

InvocationHandler

is an

MBeanServerInvocationHandler

.

This method is equivalent to

newMXBeanProxy(connection, objectName, interfaceClass,
false)

.

If you have an MBean Server

mbs

containing an
MXBean with

ObjectName

name

, and if the
MXBean's management interface is described by the Java
interface

MyMXBean

, you can construct a proxy for
the MXBean like this:

MyMXBean proxy = JMX.newMXBeanProxy(mbs, name, MyMXBean.class);

Suppose, for example,

MyMXBean

looks like this:

public interface MyMXBean {
public String getSimpleAttribute();
public void setSimpleAttribute(String value);
public

MemoryUsage

getMappedAttribute();
public void setMappedAttribute(MemoryUsage memoryUsage);
public MemoryUsage someOperation(String param1, MemoryUsage param2);
}

Then:

proxy.getSimpleAttribute()

will result in a
call to

mbs.

getAttribute

(name, "SimpleAttribute")

.

proxy.setSimpleAttribute("whatever")

will result
in a call to

mbs.

setAttribute

(name,
new Attribute("SimpleAttribute", "whatever"))

.

Because

String

is a

simple type

, in the
sense of

SimpleType

, it
is not changed in the context of an MXBean. The MXBean
proxy behaves the same as a Standard MBean proxy (see

newMBeanProxy

) for the attribute

SimpleAttribute

.

proxy.getMappedAttribute()

will result in a call
to

mbs.getAttribute("MappedAttribute")

. The MXBean
mapping rules mean that the actual type of the attribute

MappedAttribute

will be

CompositeData

and
that is what the

mbs.getAttribute

call will return.
The proxy will then convert the

CompositeData

back into
the expected type

MemoryUsage

using the MXBean mapping
rules.

Similarly,

proxy.setMappedAttribute(memoryUsage)

will convert the

MemoryUsage

argument into a

CompositeData

before calling

mbs.setAttribute

.

proxy.someOperation("whatever", memoryUsage)

will convert the

MemoryUsage

argument into a

CompositeData

and call

mbs.invoke

. The value returned
by

mbs.invoke

will be also be a

CompositeData

,
and the proxy will convert this into the expected type

MemoryUsage

using the MXBean mapping rules.

proxy.getSimpleAttribute()

will result in a
call to

mbs.

getAttribute

(name, "SimpleAttribute")

.

proxy.setSimpleAttribute("whatever")

will result
in a call to

mbs.

setAttribute

(name,
new Attribute("SimpleAttribute", "whatever"))

.

Because

String

is a

simple type

, in the
sense of

SimpleType

, it
is not changed in the context of an MXBean. The MXBean
proxy behaves the same as a Standard MBean proxy (see

newMBeanProxy

) for the attribute

SimpleAttribute

.

proxy.getMappedAttribute()

will result in a call
to

mbs.getAttribute("MappedAttribute")

. The MXBean
mapping rules mean that the actual type of the attribute

MappedAttribute

will be

CompositeData

and
that is what the

mbs.getAttribute

call will return.
The proxy will then convert the

CompositeData

back into
the expected type

MemoryUsage

using the MXBean mapping
rules.

Similarly,

proxy.setMappedAttribute(memoryUsage)

will convert the

MemoryUsage

argument into a

CompositeData

before calling

mbs.setAttribute

.

proxy.someOperation("whatever", memoryUsage)

will convert the

MemoryUsage

argument into a

CompositeData

and call

mbs.invoke

. The value returned
by

mbs.invoke

will be also be a

CompositeData

,
and the proxy will convert this into the expected type

MemoryUsage

using the MXBean mapping rules.

The object returned by this method is a

Proxy

whose

InvocationHandler

is an

MBeanServerInvocationHandler

.

This method is equivalent to

newMXBeanProxy(connection, objectName, interfaceClass,
false)

.

newMXBeanProxy

```java
public static <T> T newMXBeanProxy​(
MBeanServerConnection
connection,

ObjectName
objectName,

Class
<T> interfaceClass,
boolean notificationEmitter)
```

Make a proxy for an MXBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

This method behaves the same as

newMXBeanProxy(MBeanServerConnection, ObjectName, Class)

, but
additionally, if

notificationEmitter

is

true

, then the MXBean is assumed to be a

NotificationBroadcaster

or

NotificationEmitter

and the
returned proxy will implement

NotificationEmitter

as
well as

interfaceClass

. A call to

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

on the proxy
will result in a call to

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

, and
likewise for the other methods of

NotificationBroadcaster

and

NotificationEmitter

.

**Type Parameters:** T

- allows the compiler to know that if the

interfaceClass

parameter is

MyMXBean.class

, for
example, then the return type is

MyMXBean

.
**Parameters:** connection

- the MBean server to forward to.
**Parameters:** objectName

- the name of the MBean within

connection

to forward to.
**Parameters:** interfaceClass

- the MXBean interface,
which will also be implemented by the returned proxy.
**Parameters:** notificationEmitter

- make the returned proxy
implement

NotificationEmitter

by forwarding its methods
via

connection

.
**Returns:** the new proxy instance.
**Throws:** IllegalArgumentException

- if

interfaceClass

is not
a

compliant MXBean interface

---

#### newMXBeanProxy

public static <T> T newMXBeanProxy​(

MBeanServerConnection

connection,

ObjectName

objectName,

Class

<T> interfaceClass,
boolean notificationEmitter)

Make a proxy for an MXBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

This method behaves the same as

newMXBeanProxy(MBeanServerConnection, ObjectName, Class)

, but
additionally, if

notificationEmitter

is

true

, then the MXBean is assumed to be a

NotificationBroadcaster

or

NotificationEmitter

and the
returned proxy will implement

NotificationEmitter

as
well as

interfaceClass

. A call to

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

on the proxy
will result in a call to

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

, and
likewise for the other methods of

NotificationBroadcaster

and

NotificationEmitter

.

Make a proxy for an MXBean in a local or remote MBean
Server that may also support the methods of

NotificationEmitter

.

This method behaves the same as

newMXBeanProxy(MBeanServerConnection, ObjectName, Class)

, but
additionally, if

notificationEmitter

is

true

, then the MXBean is assumed to be a

NotificationBroadcaster

or

NotificationEmitter

and the
returned proxy will implement

NotificationEmitter

as
well as

interfaceClass

. A call to

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

on the proxy
will result in a call to

MBeanServerConnection.addNotificationListener(ObjectName,
NotificationListener, NotificationFilter, Object)

, and
likewise for the other methods of

NotificationBroadcaster

and

NotificationEmitter

.

isMXBeanInterface

```java
public static boolean isMXBeanInterface​(
Class
<?> interfaceClass)
```

Test whether an interface is an MXBean interface.
An interface is an MXBean interface if it is public,
annotated

@MXBean

or

@MXBean(true)

or if it does not have an

@MXBean

annotation
and its name ends with "

MXBean

".

**Parameters:** interfaceClass

- The candidate interface.
**Returns:** true if

interfaceClass

is a

compliant MXBean interface
**Throws:** NullPointerException

- if

interfaceClass

is null.

---

#### isMXBeanInterface

public static boolean isMXBeanInterface​(

Class

<?> interfaceClass)

Test whether an interface is an MXBean interface.
An interface is an MXBean interface if it is public,
annotated

@MXBean

or

@MXBean(true)

or if it does not have an

@MXBean

annotation
and its name ends with "

MXBean

".

---

