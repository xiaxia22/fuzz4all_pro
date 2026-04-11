# Interface UserSessionListener

**Source:** `java.desktop\java\awt\desktop\UserSessionListener.html`

### Class Description

```java
public interface
UserSessionListener

extends
SystemEventListener
```

Implementors receive notification when the user session changes.

This notification is useful for discontinuing a costly animation,
or indicating that the user is no longer present on a network service.

Some systems may provide a reason of the user session change.

**All Superinterfaces:** EventListener

,

SystemEventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void userSessionDeactivated​(
UserSessionEvent
e)

Called when the user session has been switched away.

**Parameters:**
- e

- the user session switch event

---

#### void userSessionActivated​(
UserSessionEvent
e)

Called when the user session has been switched to.

**Parameters:**
- e

- the user session switch event

---

### Additional Sections

#### Interface UserSessionListener

**All Superinterfaces:** EventListener

,

SystemEventListener

```java
public interface
UserSessionListener

extends
SystemEventListener
```

Implementors receive notification when the user session changes.

This notification is useful for discontinuing a costly animation,
or indicating that the user is no longer present on a network service.

Some systems may provide a reason of the user session change.

**Since:** 9
**See Also:** UserSessionEvent.Reason.UNSPECIFIED

,

UserSessionEvent.Reason.CONSOLE

,

UserSessionEvent.Reason.REMOTE

,

UserSessionEvent.Reason.LOCK

public interface

UserSessionListener

extends

SystemEventListener

Implementors receive notification when the user session changes.

This notification is useful for discontinuing a costly animation,
or indicating that the user is no longer present on a network service.

Some systems may provide a reason of the user session change.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

userSessionActivated

​(

UserSessionEvent

e)

Called when the user session has been switched to.

void

userSessionDeactivated

​(

UserSessionEvent

e)

Called when the user session has been switched away.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

userSessionActivated

​(

UserSessionEvent

e)

Called when the user session has been switched to.

void

userSessionDeactivated

​(

UserSessionEvent

e)

Called when the user session has been switched away.

---

#### Method Summary

Called when the user session has been switched to.

Called when the user session has been switched away.

============ METHOD DETAIL ==========

- Method Detail

- userSessionDeactivated

```java
void userSessionDeactivated​(
UserSessionEvent
e)
```

Called when the user session has been switched away.

**Parameters:** e

- the user session switch event

- userSessionActivated

```java
void userSessionActivated​(
UserSessionEvent
e)
```

Called when the user session has been switched to.

**Parameters:** e

- the user session switch event

Method Detail

- userSessionDeactivated

```java
void userSessionDeactivated​(
UserSessionEvent
e)
```

Called when the user session has been switched away.

**Parameters:** e

- the user session switch event

- userSessionActivated

```java
void userSessionActivated​(
UserSessionEvent
e)
```

Called when the user session has been switched to.

**Parameters:** e

- the user session switch event

---

#### Method Detail

userSessionDeactivated

```java
void userSessionDeactivated​(
UserSessionEvent
e)
```

Called when the user session has been switched away.

**Parameters:** e

- the user session switch event

---

#### userSessionDeactivated

void userSessionDeactivated​(

UserSessionEvent

e)

Called when the user session has been switched away.

userSessionActivated

```java
void userSessionActivated​(
UserSessionEvent
e)
```

Called when the user session has been switched to.

**Parameters:** e

- the user session switch event

---

#### userSessionActivated

void userSessionActivated​(

UserSessionEvent

e)

Called when the user session has been switched to.

---

