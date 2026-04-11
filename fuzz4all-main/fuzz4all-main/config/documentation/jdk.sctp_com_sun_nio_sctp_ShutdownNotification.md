# Class ShutdownNotification

**Source:** `jdk.sctp\com\sun\nio\sctp\ShutdownNotification.html`

### Class Description

```java
public abstract class
ShutdownNotification

extends
Object

implements
Notification
```

Notification emitted when a peers shutdowns an the association.

When a peer sends a

SHUTDOWN

, the SCTP stack delivers this
notification to inform the application that it should cease sending data.

**All Implemented Interfaces:** Notification

---

### Field Details

*No entries found.*

### Constructor Details

#### protected ShutdownNotification()

Initializes a new instance of this class.

---

### Method Details

#### public abstract
Association
association()

Returns the association that this notification is applicable to.

**Specified by:**
- association

in interface

Notification

**Returns:**
- The association that received the shutdown

---

### Additional Sections

#### Class ShutdownNotification

java.lang.Object

- com.sun.nio.sctp.ShutdownNotification

com.sun.nio.sctp.ShutdownNotification

**All Implemented Interfaces:** Notification

```java
public abstract class
ShutdownNotification

extends
Object

implements
Notification
```

Notification emitted when a peers shutdowns an the association.

When a peer sends a

SHUTDOWN

, the SCTP stack delivers this
notification to inform the application that it should cease sending data.

**Since:** 1.7

public abstract class

ShutdownNotification

extends

Object

implements

Notification

Notification emitted when a peers shutdowns an the association.

When a peer sends a

SHUTDOWN

, the SCTP stack delivers this
notification to inform the application that it should cease sending data.

When a peer sends a

SHUTDOWN

, the SCTP stack delivers this
notification to inform the application that it should cease sending data.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ShutdownNotification

()

Initializes a new instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Association

association

()

Returns the association that this notification is applicable to.

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ShutdownNotification

()

Initializes a new instance of this class.

---

#### Constructor Summary

Initializes a new instance of this class.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Association

association

()

Returns the association that this notification is applicable to.

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

Returns the association that this notification is applicable to.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ShutdownNotification

```java
protected ShutdownNotification()
```

Initializes a new instance of this class.

============ METHOD DETAIL ==========

- Method Detail

- association

```java
public abstract
Association
association()
```

Returns the association that this notification is applicable to.

**Specified by:** association

in interface

Notification
**Returns:** The association that received the shutdown

Constructor Detail

- ShutdownNotification

```java
protected ShutdownNotification()
```

Initializes a new instance of this class.

---

#### Constructor Detail

ShutdownNotification

```java
protected ShutdownNotification()
```

Initializes a new instance of this class.

---

#### ShutdownNotification

protected ShutdownNotification()

Initializes a new instance of this class.

Method Detail

- association

```java
public abstract
Association
association()
```

Returns the association that this notification is applicable to.

**Specified by:** association

in interface

Notification
**Returns:** The association that received the shutdown

---

#### Method Detail

association

```java
public abstract
Association
association()
```

Returns the association that this notification is applicable to.

**Specified by:** association

in interface

Notification
**Returns:** The association that received the shutdown

---

#### association

public abstract

Association

association()

Returns the association that this notification is applicable to.

---

