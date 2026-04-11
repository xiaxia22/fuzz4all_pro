# Interface MBeanServerForwarder

**Source:** `java.management\javax\management\remote\MBeanServerForwarder.html`

### Class Description

```java
public interface
MBeanServerForwarder

extends
MBeanServer
```

An object of this class implements the MBeanServer interface and
wraps another object that also implements that interface.
Typically, an implementation of this interface performs some action
in some or all methods of the

MBeanServer

interface
before and/or after forwarding the method to the wrapped object.
Examples include security checking and logging.

**All Superinterfaces:** MBeanServer

,

MBeanServerConnection

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### MBeanServer
getMBeanServer()

Returns the MBeanServer object to which requests will be forwarded.

**Returns:**
- the MBeanServer object to which requests will be forwarded,
or null if there is none.

**See Also:**
- setMBeanServer(javax.management.MBeanServer)

---

#### void setMBeanServer​(
MBeanServer
mbs)

Sets the MBeanServer object to which requests will be forwarded
after treatment by this object.

**Parameters:**
- mbs

- the MBeanServer object to which requests will be forwarded.

**Throws:**
- IllegalArgumentException

- if this object is already
forwarding to an MBeanServer object or if

mbs

is
null or if

mbs

is identical to this object.

**See Also:**
- getMBeanServer()

---

### Additional Sections

#### Interface MBeanServerForwarder

**All Superinterfaces:** MBeanServer

,

MBeanServerConnection

```java
public interface
MBeanServerForwarder

extends
MBeanServer
```

An object of this class implements the MBeanServer interface and
wraps another object that also implements that interface.
Typically, an implementation of this interface performs some action
in some or all methods of the

MBeanServer

interface
before and/or after forwarding the method to the wrapped object.
Examples include security checking and logging.

**Since:** 1.5

public interface

MBeanServerForwarder

extends

MBeanServer

An object of this class implements the MBeanServer interface and
wraps another object that also implements that interface.
Typically, an implementation of this interface performs some action
in some or all methods of the

MBeanServer

interface
before and/or after forwarding the method to the wrapped object.
Examples include security checking and logging.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

MBeanServer

getMBeanServer

()

Returns the MBeanServer object to which requests will be forwarded.

void

setMBeanServer

​(

MBeanServer

mbs)

Sets the MBeanServer object to which requests will be forwarded
after treatment by this object.

- Methods declared in interface javax.management.

MBeanServer

addNotificationListener

,

addNotificationListener

,

createMBean

,

createMBean

,

createMBean

,

createMBean

,

deserialize

,

deserialize

,

deserialize

,

getAttribute

,

getAttributes

,

getClassLoader

,

getClassLoaderFor

,

getClassLoaderRepository

,

getMBeanCount

,

instantiate

,

instantiate

,

instantiate

,

instantiate

,

isRegistered

,

queryMBeans

,

queryNames

,

registerMBean

,

setAttribute

,

setAttributes

,

unregisterMBean

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

Modifier and Type

Method

Description

MBeanServer

getMBeanServer

()

Returns the MBeanServer object to which requests will be forwarded.

void

setMBeanServer

​(

MBeanServer

mbs)

Sets the MBeanServer object to which requests will be forwarded
after treatment by this object.

- Methods declared in interface javax.management.

MBeanServer

addNotificationListener

,

addNotificationListener

,

createMBean

,

createMBean

,

createMBean

,

createMBean

,

deserialize

,

deserialize

,

deserialize

,

getAttribute

,

getAttributes

,

getClassLoader

,

getClassLoaderFor

,

getClassLoaderRepository

,

getMBeanCount

,

instantiate

,

instantiate

,

instantiate

,

instantiate

,

isRegistered

,

queryMBeans

,

queryNames

,

registerMBean

,

setAttribute

,

setAttributes

,

unregisterMBean

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

Returns the MBeanServer object to which requests will be forwarded.

Sets the MBeanServer object to which requests will be forwarded
after treatment by this object.

Methods declared in interface javax.management.

MBeanServer

addNotificationListener

,

addNotificationListener

,

createMBean

,

createMBean

,

createMBean

,

createMBean

,

deserialize

,

deserialize

,

deserialize

,

getAttribute

,

getAttributes

,

getClassLoader

,

getClassLoaderFor

,

getClassLoaderRepository

,

getMBeanCount

,

instantiate

,

instantiate

,

instantiate

,

instantiate

,

isRegistered

,

queryMBeans

,

queryNames

,

registerMBean

,

setAttribute

,

setAttributes

,

unregisterMBean

---

#### Methods declared in interface javax.management. MBeanServer

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

- getMBeanServer

```java
MBeanServer
getMBeanServer()
```

Returns the MBeanServer object to which requests will be forwarded.

**Returns:** the MBeanServer object to which requests will be forwarded,
or null if there is none.
**See Also:** setMBeanServer(javax.management.MBeanServer)

- setMBeanServer

```java
void setMBeanServer​(
MBeanServer
mbs)
```

Sets the MBeanServer object to which requests will be forwarded
after treatment by this object.

**Parameters:** mbs

- the MBeanServer object to which requests will be forwarded.
**Throws:** IllegalArgumentException

- if this object is already
forwarding to an MBeanServer object or if

mbs

is
null or if

mbs

is identical to this object.
**See Also:** getMBeanServer()

Method Detail

- getMBeanServer

```java
MBeanServer
getMBeanServer()
```

Returns the MBeanServer object to which requests will be forwarded.

**Returns:** the MBeanServer object to which requests will be forwarded,
or null if there is none.
**See Also:** setMBeanServer(javax.management.MBeanServer)

- setMBeanServer

```java
void setMBeanServer​(
MBeanServer
mbs)
```

Sets the MBeanServer object to which requests will be forwarded
after treatment by this object.

**Parameters:** mbs

- the MBeanServer object to which requests will be forwarded.
**Throws:** IllegalArgumentException

- if this object is already
forwarding to an MBeanServer object or if

mbs

is
null or if

mbs

is identical to this object.
**See Also:** getMBeanServer()

---

#### Method Detail

getMBeanServer

```java
MBeanServer
getMBeanServer()
```

Returns the MBeanServer object to which requests will be forwarded.

**Returns:** the MBeanServer object to which requests will be forwarded,
or null if there is none.
**See Also:** setMBeanServer(javax.management.MBeanServer)

---

#### getMBeanServer

MBeanServer

getMBeanServer()

Returns the MBeanServer object to which requests will be forwarded.

setMBeanServer

```java
void setMBeanServer​(
MBeanServer
mbs)
```

Sets the MBeanServer object to which requests will be forwarded
after treatment by this object.

**Parameters:** mbs

- the MBeanServer object to which requests will be forwarded.
**Throws:** IllegalArgumentException

- if this object is already
forwarding to an MBeanServer object or if

mbs

is
null or if

mbs

is identical to this object.
**See Also:** getMBeanServer()

---

#### setMBeanServer

void setMBeanServer​(

MBeanServer

mbs)

Sets the MBeanServer object to which requests will be forwarded
after treatment by this object.

---

