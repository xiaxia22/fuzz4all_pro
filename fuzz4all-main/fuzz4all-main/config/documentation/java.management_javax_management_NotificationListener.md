# Interface NotificationListener

**Source:** `java.management\javax\management\NotificationListener.html`

### Class Description

```java
public interface
NotificationListener

extends
EventListener
```

Should be implemented by an object that wants to receive notifications.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void handleNotification​(
Notification
notification,

Object
handback)

Invoked when a JMX notification occurs.
The implementation of this method should return as soon as possible, to avoid
blocking its notification broadcaster.

**Parameters:**
- notification

- The notification.
- handback

- An opaque object which helps the listener to associate
information regarding the MBean emitter. This object is passed to the
addNotificationListener call and resent, without modification, to the
listener.

---

### Additional Sections

#### Interface NotificationListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** RelationService

```java
public interface
NotificationListener

extends
EventListener
```

Should be implemented by an object that wants to receive notifications.

**Since:** 1.5

public interface

NotificationListener

extends

EventListener

Should be implemented by an object that wants to receive notifications.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

handleNotification

​(

Notification

notification,

Object

handback)

Invoked when a JMX notification occurs.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

handleNotification

​(

Notification

notification,

Object

handback)

Invoked when a JMX notification occurs.

---

#### Method Summary

Invoked when a JMX notification occurs.

============ METHOD DETAIL ==========

- Method Detail

- handleNotification

```java
void handleNotification​(
Notification
notification,

Object
handback)
```

Invoked when a JMX notification occurs.
The implementation of this method should return as soon as possible, to avoid
blocking its notification broadcaster.

**Parameters:** notification

- The notification.
**Parameters:** handback

- An opaque object which helps the listener to associate
information regarding the MBean emitter. This object is passed to the
addNotificationListener call and resent, without modification, to the
listener.

Method Detail

- handleNotification

```java
void handleNotification​(
Notification
notification,

Object
handback)
```

Invoked when a JMX notification occurs.
The implementation of this method should return as soon as possible, to avoid
blocking its notification broadcaster.

**Parameters:** notification

- The notification.
**Parameters:** handback

- An opaque object which helps the listener to associate
information regarding the MBean emitter. This object is passed to the
addNotificationListener call and resent, without modification, to the
listener.

---

#### Method Detail

handleNotification

```java
void handleNotification​(
Notification
notification,

Object
handback)
```

Invoked when a JMX notification occurs.
The implementation of this method should return as soon as possible, to avoid
blocking its notification broadcaster.

**Parameters:** notification

- The notification.
**Parameters:** handback

- An opaque object which helps the listener to associate
information regarding the MBean emitter. This object is passed to the
addNotificationListener call and resent, without modification, to the
listener.

---

#### handleNotification

void handleNotification​(

Notification

notification,

Object

handback)

Invoked when a JMX notification occurs.
The implementation of this method should return as soon as possible, to avoid
blocking its notification broadcaster.

---

