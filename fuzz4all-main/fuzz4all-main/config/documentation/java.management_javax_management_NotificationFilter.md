# Interface NotificationFilter

**Source:** `java.management\javax\management\NotificationFilter.html`

### Class Description

```java
public interface
NotificationFilter

extends
Serializable
```

To be implemented by a any class acting as a notification filter.
It allows a registered notification listener to filter the notifications of interest.

**All Superinterfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isNotificationEnabled​(
Notification
notification)

Invoked before sending the specified notification to the listener.

**Parameters:**
- notification

- The notification to be sent.

**Returns:**
- true

if the notification has to be sent to the listener,

false

otherwise.

---

### Additional Sections

#### Interface NotificationFilter

**All Superinterfaces:** Serializable

**All Known Implementing Classes:** AttributeChangeNotificationFilter

,

MBeanServerNotificationFilter

,

NotificationFilterSupport

```java
public interface
NotificationFilter

extends
Serializable
```

To be implemented by a any class acting as a notification filter.
It allows a registered notification listener to filter the notifications of interest.

**Since:** 1.5

public interface

NotificationFilter

extends

Serializable

To be implemented by a any class acting as a notification filter.
It allows a registered notification listener to filter the notifications of interest.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

isNotificationEnabled

​(

Notification

notification)

Invoked before sending the specified notification to the listener.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

isNotificationEnabled

​(

Notification

notification)

Invoked before sending the specified notification to the listener.

---

#### Method Summary

Invoked before sending the specified notification to the listener.

============ METHOD DETAIL ==========

- Method Detail

- isNotificationEnabled

```java
boolean isNotificationEnabled​(
Notification
notification)
```

Invoked before sending the specified notification to the listener.

**Parameters:** notification

- The notification to be sent.
**Returns:** true

if the notification has to be sent to the listener,

false

otherwise.

Method Detail

- isNotificationEnabled

```java
boolean isNotificationEnabled​(
Notification
notification)
```

Invoked before sending the specified notification to the listener.

**Parameters:** notification

- The notification to be sent.
**Returns:** true

if the notification has to be sent to the listener,

false

otherwise.

---

#### Method Detail

isNotificationEnabled

```java
boolean isNotificationEnabled​(
Notification
notification)
```

Invoked before sending the specified notification to the listener.

**Parameters:** notification

- The notification to be sent.
**Returns:** true

if the notification has to be sent to the listener,

false

otherwise.

---

#### isNotificationEnabled

boolean isNotificationEnabled​(

Notification

notification)

Invoked before sending the specified notification to the listener.

---

