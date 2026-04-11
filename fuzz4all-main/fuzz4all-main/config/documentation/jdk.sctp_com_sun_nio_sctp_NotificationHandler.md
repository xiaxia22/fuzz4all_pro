# Interface NotificationHandler<T>

**Source:** `jdk.sctp\com\sun\nio\sctp\NotificationHandler.html`

### Class Description

```java
public interface
NotificationHandler<T>
```

A handler for consuming notifications from the SCTP stack.

The SCTP channels defined in this package allow a notification handler to
be specified to consume notifications from the SCTP stack. When a
notification is received the

handleNotification

method of the handler is invoked to handle that
notification.

Additionally, an attachment object can be attached to the

receive

operation to provide context when consuming the notification. The
attachment is important for cases where a

state-less

NotificationHandler

is used to consume the result of many

receive

operations.

Handler implementations are encouraged to extend the

AbstractNotificationHandler

class which implements this interface and
provide notification specific methods. However, an API should generally use
this handler interface as the type for parameters, return type, etc. rather
than the abstract class.

**All Known Implementing Classes:** AbstractNotificationHandler

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### HandlerResult
handleNotification​(
Notification
notification,

T
attachment)

Invoked when a notification is received from the SCTP stack.

**Parameters:**
- notification

- The notification
- attachment

- The object attached to the receive operation when it was initiated.

**Returns:**
- The handler result

---

### Additional Sections

#### Interface NotificationHandler<T>

**All Known Implementing Classes:** AbstractNotificationHandler

```java
public interface
NotificationHandler<T>
```

A handler for consuming notifications from the SCTP stack.

The SCTP channels defined in this package allow a notification handler to
be specified to consume notifications from the SCTP stack. When a
notification is received the

handleNotification

method of the handler is invoked to handle that
notification.

Additionally, an attachment object can be attached to the

receive

operation to provide context when consuming the notification. The
attachment is important for cases where a

state-less

NotificationHandler

is used to consume the result of many

receive

operations.

Handler implementations are encouraged to extend the

AbstractNotificationHandler

class which implements this interface and
provide notification specific methods. However, an API should generally use
this handler interface as the type for parameters, return type, etc. rather
than the abstract class.

**Since:** 1.7

public interface

NotificationHandler<T>

A handler for consuming notifications from the SCTP stack.

The SCTP channels defined in this package allow a notification handler to
be specified to consume notifications from the SCTP stack. When a
notification is received the

handleNotification

method of the handler is invoked to handle that
notification.

Additionally, an attachment object can be attached to the

receive

operation to provide context when consuming the notification. The
attachment is important for cases where a

state-less

NotificationHandler

is used to consume the result of many

receive

operations.

Handler implementations are encouraged to extend the

AbstractNotificationHandler

class which implements this interface and
provide notification specific methods. However, an API should generally use
this handler interface as the type for parameters, return type, etc. rather
than the abstract class.

The SCTP channels defined in this package allow a notification handler to
be specified to consume notifications from the SCTP stack. When a
notification is received the

handleNotification

method of the handler is invoked to handle that
notification.

Additionally, an attachment object can be attached to the

receive

operation to provide context when consuming the notification. The
attachment is important for cases where a

state-less

NotificationHandler

is used to consume the result of many

receive

operations.

Handler implementations are encouraged to extend the

AbstractNotificationHandler

class which implements this interface and
provide notification specific methods. However, an API should generally use
this handler interface as the type for parameters, return type, etc. rather
than the abstract class.

Additionally, an attachment object can be attached to the

receive

operation to provide context when consuming the notification. The
attachment is important for cases where a

state-less

NotificationHandler

is used to consume the result of many

receive

operations.

Handler implementations are encouraged to extend the

AbstractNotificationHandler

class which implements this interface and
provide notification specific methods. However, an API should generally use
this handler interface as the type for parameters, return type, etc. rather
than the abstract class.

Handler implementations are encouraged to extend the

AbstractNotificationHandler

class which implements this interface and
provide notification specific methods. However, an API should generally use
this handler interface as the type for parameters, return type, etc. rather
than the abstract class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

HandlerResult

handleNotification

​(

Notification

notification,

T

attachment)

Invoked when a notification is received from the SCTP stack.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

HandlerResult

handleNotification

​(

Notification

notification,

T

attachment)

Invoked when a notification is received from the SCTP stack.

---

#### Method Summary

Invoked when a notification is received from the SCTP stack.

============ METHOD DETAIL ==========

- Method Detail

- handleNotification

```java
HandlerResult
handleNotification​(
Notification
notification,

T
attachment)
```

Invoked when a notification is received from the SCTP stack.

**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the receive operation when it was initiated.
**Returns:** The handler result

Method Detail

- handleNotification

```java
HandlerResult
handleNotification​(
Notification
notification,

T
attachment)
```

Invoked when a notification is received from the SCTP stack.

**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the receive operation when it was initiated.
**Returns:** The handler result

---

#### Method Detail

handleNotification

```java
HandlerResult
handleNotification​(
Notification
notification,

T
attachment)
```

Invoked when a notification is received from the SCTP stack.

**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the receive operation when it was initiated.
**Returns:** The handler result

---

#### handleNotification

HandlerResult

handleNotification​(

Notification

notification,

T

attachment)

Invoked when a notification is received from the SCTP stack.

---

