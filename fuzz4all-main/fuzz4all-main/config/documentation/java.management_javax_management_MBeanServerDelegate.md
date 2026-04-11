# Class MBeanServerDelegate

**Source:** `java.management\javax\management\MBeanServerDelegate.html`

### Class Description

```java
public class
MBeanServerDelegate

extends
Object

implements
MBeanServerDelegateMBean
,
NotificationEmitter
```

Represents the MBean server from the management point of view.
The MBeanServerDelegate MBean emits the MBeanServerNotifications when
an MBean is registered/unregistered in the MBean server.

**All Implemented Interfaces:** MBeanServerDelegateMBean

,

NotificationBroadcaster

,

NotificationEmitter

---

### Field Details

#### public static final
ObjectName
DELEGATE_NAME

Defines the default ObjectName of the MBeanServerDelegate.

**Since:**
- 1.6

---

### Constructor Details

#### public MBeanServerDelegate()

Create a MBeanServerDelegate object.

---

### Method Details

#### public
String
getMBeanServerId()

Returns the MBean server agent identity.

**Specified by:**
- getMBeanServerId

in interface

MBeanServerDelegateMBean

**Returns:**
- the identity.

---

#### public
String
getSpecificationName()

Returns the full name of the JMX specification implemented
by this product.

**Specified by:**
- getSpecificationName

in interface

MBeanServerDelegateMBean

**Returns:**
- the specification name.

---

#### public
String
getSpecificationVersion()

Returns the version of the JMX specification implemented
by this product.

**Specified by:**
- getSpecificationVersion

in interface

MBeanServerDelegateMBean

**Returns:**
- the specification version.

---

#### public
String
getSpecificationVendor()

Returns the vendor of the JMX specification implemented
by this product.

**Specified by:**
- getSpecificationVendor

in interface

MBeanServerDelegateMBean

**Returns:**
- the specification vendor.

---

#### public
String
getImplementationName()

Returns the JMX implementation name (the name of this product).

**Specified by:**
- getImplementationName

in interface

MBeanServerDelegateMBean

**Returns:**
- the implementation name.

---

#### public
String
getImplementationVersion()

Returns the JMX implementation version (the version of this product).

**Specified by:**
- getImplementationVersion

in interface

MBeanServerDelegateMBean

**Returns:**
- the implementation version.

---

#### public
String
getImplementationVendor()

Returns the JMX implementation vendor (the vendor of this product).

**Specified by:**
- getImplementationVendor

in interface

MBeanServerDelegateMBean

**Returns:**
- the implementation vendor.

---

#### public void sendNotification​(
Notification
notification)

Enables the MBean server to send a notification.
If the passed

notification

has a sequence number lesser
or equal to 0, then replace it with the delegate's own sequence
number.

**Parameters:**
- notification

- The notification to send.

---

### Additional Sections

#### Class MBeanServerDelegate

java.lang.Object

- javax.management.MBeanServerDelegate

javax.management.MBeanServerDelegate

**All Implemented Interfaces:** MBeanServerDelegateMBean

,

NotificationBroadcaster

,

NotificationEmitter

```java
public class
MBeanServerDelegate

extends
Object

implements
MBeanServerDelegateMBean
,
NotificationEmitter
```

Represents the MBean server from the management point of view.
The MBeanServerDelegate MBean emits the MBeanServerNotifications when
an MBean is registered/unregistered in the MBean server.

**Since:** 1.5

public class

MBeanServerDelegate

extends

Object

implements

MBeanServerDelegateMBean

,

NotificationEmitter

Represents the MBean server from the management point of view.
The MBeanServerDelegate MBean emits the MBeanServerNotifications when
an MBean is registered/unregistered in the MBean server.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

ObjectName

DELEGATE_NAME

Defines the default ObjectName of the MBeanServerDelegate.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MBeanServerDelegate

()

Create a MBeanServerDelegate object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getImplementationName

()

Returns the JMX implementation name (the name of this product).

String

getImplementationVendor

()

Returns the JMX implementation vendor (the vendor of this product).

String

getImplementationVersion

()

Returns the JMX implementation version (the version of this product).

String

getMBeanServerId

()

Returns the MBean server agent identity.

String

getSpecificationName

()

Returns the full name of the JMX specification implemented
by this product.

String

getSpecificationVendor

()

Returns the vendor of the JMX specification implemented
by this product.

String

getSpecificationVersion

()

Returns the version of the JMX specification implemented
by this product.

void

sendNotification

​(

Notification

notification)

Enables the MBean server to send a notification.

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

- Methods declared in interface javax.management.

NotificationBroadcaster

addNotificationListener

,

getNotificationInfo

,

removeNotificationListener

- Methods declared in interface javax.management.

NotificationEmitter

removeNotificationListener

Field Summary

Fields

Modifier and Type

Field

Description

static

ObjectName

DELEGATE_NAME

Defines the default ObjectName of the MBeanServerDelegate.

---

#### Field Summary

Defines the default ObjectName of the MBeanServerDelegate.

Constructor Summary

Constructors

Constructor

Description

MBeanServerDelegate

()

Create a MBeanServerDelegate object.

---

#### Constructor Summary

Create a MBeanServerDelegate object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getImplementationName

()

Returns the JMX implementation name (the name of this product).

String

getImplementationVendor

()

Returns the JMX implementation vendor (the vendor of this product).

String

getImplementationVersion

()

Returns the JMX implementation version (the version of this product).

String

getMBeanServerId

()

Returns the MBean server agent identity.

String

getSpecificationName

()

Returns the full name of the JMX specification implemented
by this product.

String

getSpecificationVendor

()

Returns the vendor of the JMX specification implemented
by this product.

String

getSpecificationVersion

()

Returns the version of the JMX specification implemented
by this product.

void

sendNotification

​(

Notification

notification)

Enables the MBean server to send a notification.

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

- Methods declared in interface javax.management.

NotificationBroadcaster

addNotificationListener

,

getNotificationInfo

,

removeNotificationListener

- Methods declared in interface javax.management.

NotificationEmitter

removeNotificationListener

---

#### Method Summary

Returns the JMX implementation name (the name of this product).

Returns the JMX implementation vendor (the vendor of this product).

Returns the JMX implementation version (the version of this product).

Returns the MBean server agent identity.

Returns the full name of the JMX specification implemented
by this product.

Returns the vendor of the JMX specification implemented
by this product.

Returns the version of the JMX specification implemented
by this product.

Enables the MBean server to send a notification.

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

NotificationEmitter

removeNotificationListener

---

#### Methods declared in interface javax.management. NotificationEmitter

============ FIELD DETAIL ===========

- Field Detail

- DELEGATE_NAME

```java
public static final
ObjectName
DELEGATE_NAME
```

Defines the default ObjectName of the MBeanServerDelegate.

**Since:** 1.6

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MBeanServerDelegate

```java
public MBeanServerDelegate()
```

Create a MBeanServerDelegate object.

============ METHOD DETAIL ==========

- Method Detail

- getMBeanServerId

```java
public
String
getMBeanServerId()
```

Returns the MBean server agent identity.

**Specified by:** getMBeanServerId

in interface

MBeanServerDelegateMBean
**Returns:** the identity.

- getSpecificationName

```java
public
String
getSpecificationName()
```

Returns the full name of the JMX specification implemented
by this product.

**Specified by:** getSpecificationName

in interface

MBeanServerDelegateMBean
**Returns:** the specification name.

- getSpecificationVersion

```java
public
String
getSpecificationVersion()
```

Returns the version of the JMX specification implemented
by this product.

**Specified by:** getSpecificationVersion

in interface

MBeanServerDelegateMBean
**Returns:** the specification version.

- getSpecificationVendor

```java
public
String
getSpecificationVendor()
```

Returns the vendor of the JMX specification implemented
by this product.

**Specified by:** getSpecificationVendor

in interface

MBeanServerDelegateMBean
**Returns:** the specification vendor.

- getImplementationName

```java
public
String
getImplementationName()
```

Returns the JMX implementation name (the name of this product).

**Specified by:** getImplementationName

in interface

MBeanServerDelegateMBean
**Returns:** the implementation name.

- getImplementationVersion

```java
public
String
getImplementationVersion()
```

Returns the JMX implementation version (the version of this product).

**Specified by:** getImplementationVersion

in interface

MBeanServerDelegateMBean
**Returns:** the implementation version.

- getImplementationVendor

```java
public
String
getImplementationVendor()
```

Returns the JMX implementation vendor (the vendor of this product).

**Specified by:** getImplementationVendor

in interface

MBeanServerDelegateMBean
**Returns:** the implementation vendor.

- sendNotification

```java
public void sendNotification​(
Notification
notification)
```

Enables the MBean server to send a notification.
If the passed

notification

has a sequence number lesser
or equal to 0, then replace it with the delegate's own sequence
number.

**Parameters:** notification

- The notification to send.

Field Detail

- DELEGATE_NAME

```java
public static final
ObjectName
DELEGATE_NAME
```

Defines the default ObjectName of the MBeanServerDelegate.

**Since:** 1.6

---

#### Field Detail

DELEGATE_NAME

```java
public static final
ObjectName
DELEGATE_NAME
```

Defines the default ObjectName of the MBeanServerDelegate.

**Since:** 1.6

---

#### DELEGATE_NAME

public static final

ObjectName

DELEGATE_NAME

Defines the default ObjectName of the MBeanServerDelegate.

Constructor Detail

- MBeanServerDelegate

```java
public MBeanServerDelegate()
```

Create a MBeanServerDelegate object.

---

#### Constructor Detail

MBeanServerDelegate

```java
public MBeanServerDelegate()
```

Create a MBeanServerDelegate object.

---

#### MBeanServerDelegate

public MBeanServerDelegate()

Create a MBeanServerDelegate object.

Method Detail

- getMBeanServerId

```java
public
String
getMBeanServerId()
```

Returns the MBean server agent identity.

**Specified by:** getMBeanServerId

in interface

MBeanServerDelegateMBean
**Returns:** the identity.

- getSpecificationName

```java
public
String
getSpecificationName()
```

Returns the full name of the JMX specification implemented
by this product.

**Specified by:** getSpecificationName

in interface

MBeanServerDelegateMBean
**Returns:** the specification name.

- getSpecificationVersion

```java
public
String
getSpecificationVersion()
```

Returns the version of the JMX specification implemented
by this product.

**Specified by:** getSpecificationVersion

in interface

MBeanServerDelegateMBean
**Returns:** the specification version.

- getSpecificationVendor

```java
public
String
getSpecificationVendor()
```

Returns the vendor of the JMX specification implemented
by this product.

**Specified by:** getSpecificationVendor

in interface

MBeanServerDelegateMBean
**Returns:** the specification vendor.

- getImplementationName

```java
public
String
getImplementationName()
```

Returns the JMX implementation name (the name of this product).

**Specified by:** getImplementationName

in interface

MBeanServerDelegateMBean
**Returns:** the implementation name.

- getImplementationVersion

```java
public
String
getImplementationVersion()
```

Returns the JMX implementation version (the version of this product).

**Specified by:** getImplementationVersion

in interface

MBeanServerDelegateMBean
**Returns:** the implementation version.

- getImplementationVendor

```java
public
String
getImplementationVendor()
```

Returns the JMX implementation vendor (the vendor of this product).

**Specified by:** getImplementationVendor

in interface

MBeanServerDelegateMBean
**Returns:** the implementation vendor.

- sendNotification

```java
public void sendNotification​(
Notification
notification)
```

Enables the MBean server to send a notification.
If the passed

notification

has a sequence number lesser
or equal to 0, then replace it with the delegate's own sequence
number.

**Parameters:** notification

- The notification to send.

---

#### Method Detail

getMBeanServerId

```java
public
String
getMBeanServerId()
```

Returns the MBean server agent identity.

**Specified by:** getMBeanServerId

in interface

MBeanServerDelegateMBean
**Returns:** the identity.

---

#### getMBeanServerId

public

String

getMBeanServerId()

Returns the MBean server agent identity.

getSpecificationName

```java
public
String
getSpecificationName()
```

Returns the full name of the JMX specification implemented
by this product.

**Specified by:** getSpecificationName

in interface

MBeanServerDelegateMBean
**Returns:** the specification name.

---

#### getSpecificationName

public

String

getSpecificationName()

Returns the full name of the JMX specification implemented
by this product.

getSpecificationVersion

```java
public
String
getSpecificationVersion()
```

Returns the version of the JMX specification implemented
by this product.

**Specified by:** getSpecificationVersion

in interface

MBeanServerDelegateMBean
**Returns:** the specification version.

---

#### getSpecificationVersion

public

String

getSpecificationVersion()

Returns the version of the JMX specification implemented
by this product.

getSpecificationVendor

```java
public
String
getSpecificationVendor()
```

Returns the vendor of the JMX specification implemented
by this product.

**Specified by:** getSpecificationVendor

in interface

MBeanServerDelegateMBean
**Returns:** the specification vendor.

---

#### getSpecificationVendor

public

String

getSpecificationVendor()

Returns the vendor of the JMX specification implemented
by this product.

getImplementationName

```java
public
String
getImplementationName()
```

Returns the JMX implementation name (the name of this product).

**Specified by:** getImplementationName

in interface

MBeanServerDelegateMBean
**Returns:** the implementation name.

---

#### getImplementationName

public

String

getImplementationName()

Returns the JMX implementation name (the name of this product).

getImplementationVersion

```java
public
String
getImplementationVersion()
```

Returns the JMX implementation version (the version of this product).

**Specified by:** getImplementationVersion

in interface

MBeanServerDelegateMBean
**Returns:** the implementation version.

---

#### getImplementationVersion

public

String

getImplementationVersion()

Returns the JMX implementation version (the version of this product).

getImplementationVendor

```java
public
String
getImplementationVendor()
```

Returns the JMX implementation vendor (the vendor of this product).

**Specified by:** getImplementationVendor

in interface

MBeanServerDelegateMBean
**Returns:** the implementation vendor.

---

#### getImplementationVendor

public

String

getImplementationVendor()

Returns the JMX implementation vendor (the vendor of this product).

sendNotification

```java
public void sendNotification​(
Notification
notification)
```

Enables the MBean server to send a notification.
If the passed

notification

has a sequence number lesser
or equal to 0, then replace it with the delegate's own sequence
number.

**Parameters:** notification

- The notification to send.

---

#### sendNotification

public void sendNotification​(

Notification

notification)

Enables the MBean server to send a notification.
If the passed

notification

has a sequence number lesser
or equal to 0, then replace it with the delegate's own sequence
number.

---

