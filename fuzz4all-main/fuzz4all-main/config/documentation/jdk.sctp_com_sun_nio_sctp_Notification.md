# Interface Notification

**Source:** `jdk.sctp\com\sun\nio\sctp\Notification.html`

### Class Description

```java
public interface
Notification
```

A notification from the SCTP stack.

Objects of this type are passed to the

NotificationHandler

when
a notification is received.

An SCTP channel supports the following notifications:

AssociationChangeNotification

,

PeerAddressChangeNotification

,

SendFailedNotification

,

ShutdownNotification

, and may support
additional implementation specific notifications.

**All Known Implementing Classes:** AssociationChangeNotification

,

PeerAddressChangeNotification

,

SendFailedNotification

,

ShutdownNotification

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Association
association()

Returns the association that this notification is applicable to.

**Returns:**
- The association

---

### Additional Sections

#### Interface Notification

**All Known Implementing Classes:** AssociationChangeNotification

,

PeerAddressChangeNotification

,

SendFailedNotification

,

ShutdownNotification

```java
public interface
Notification
```

A notification from the SCTP stack.

Objects of this type are passed to the

NotificationHandler

when
a notification is received.

An SCTP channel supports the following notifications:

AssociationChangeNotification

,

PeerAddressChangeNotification

,

SendFailedNotification

,

ShutdownNotification

, and may support
additional implementation specific notifications.

**Since:** 1.7

public interface

Notification

A notification from the SCTP stack.

Objects of this type are passed to the

NotificationHandler

when
a notification is received.

An SCTP channel supports the following notifications:

AssociationChangeNotification

,

PeerAddressChangeNotification

,

SendFailedNotification

,

ShutdownNotification

, and may support
additional implementation specific notifications.

Objects of this type are passed to the

NotificationHandler

when
a notification is received.

An SCTP channel supports the following notifications:

AssociationChangeNotification

,

PeerAddressChangeNotification

,

SendFailedNotification

,

ShutdownNotification

, and may support
additional implementation specific notifications.

An SCTP channel supports the following notifications:

AssociationChangeNotification

,

PeerAddressChangeNotification

,

SendFailedNotification

,

ShutdownNotification

, and may support
additional implementation specific notifications.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Association

association

()

Returns the association that this notification is applicable to.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Association

association

()

Returns the association that this notification is applicable to.

---

#### Method Summary

Returns the association that this notification is applicable to.

============ METHOD DETAIL ==========

- Method Detail

- association

```java
Association
association()
```

Returns the association that this notification is applicable to.

**Returns:** The association

Method Detail

- association

```java
Association
association()
```

Returns the association that this notification is applicable to.

**Returns:** The association

---

#### Method Detail

association

```java
Association
association()
```

Returns the association that this notification is applicable to.

**Returns:** The association

---

#### association

Association

association()

Returns the association that this notification is applicable to.

---

