# Class UserSessionEvent

**Source:** `java.desktop\java\awt\desktop\UserSessionEvent.html`

### Class Description

```java
public final class
UserSessionEvent

extends
AppEvent
```

Event sent when the user session has been changed.

Some systems may provide a reason of a user session change.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UserSessionEvent​(
UserSessionEvent.Reason
reason)

Constructs a

UserSessionEvent

.

**Parameters:**
- reason

- the reason of the user session change

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
- UnsupportedOperationException

- if Desktop API is not supported on
the current platform

**See Also:**
- Desktop.isDesktopSupported()

,

GraphicsEnvironment.isHeadless()

---

### Method Details

#### public
UserSessionEvent.Reason
getReason()

Gets a reason of the user session change.

**Returns:**
- reason a reason

**See Also:**
- UserSessionEvent.Reason.UNSPECIFIED

,

UserSessionEvent.Reason.CONSOLE

,

UserSessionEvent.Reason.REMOTE

,

UserSessionEvent.Reason.LOCK

---

### Additional Sections

#### Class UserSessionEvent

java.lang.Object

- java.util.EventObject
- - java.awt.desktop.AppEvent
- - java.awt.desktop.UserSessionEvent

java.util.EventObject

- java.awt.desktop.AppEvent
- - java.awt.desktop.UserSessionEvent

java.awt.desktop.AppEvent

- java.awt.desktop.UserSessionEvent

java.awt.desktop.UserSessionEvent

**All Implemented Interfaces:** Serializable

```java
public final class
UserSessionEvent

extends
AppEvent
```

Event sent when the user session has been changed.

Some systems may provide a reason of a user session change.

**Since:** 9
**See Also:** UserSessionListener.userSessionActivated(UserSessionEvent)

,

UserSessionListener.userSessionDeactivated(UserSessionEvent)

,

Serialized Form

public final class

UserSessionEvent

extends

AppEvent

Event sent when the user session has been changed.

Some systems may provide a reason of a user session change.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

UserSessionEvent.Reason

Kinds of available reasons of user session change.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UserSessionEvent

​(

UserSessionEvent.Reason

reason)

Constructs a

UserSessionEvent

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

UserSessionEvent.Reason

getReason

()

Gets a reason of the user session change.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

wait

,

wait

,

wait

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

UserSessionEvent.Reason

Kinds of available reasons of user session change.

---

#### Nested Class Summary

Kinds of available reasons of user session change.

Field Summary

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

UserSessionEvent

​(

UserSessionEvent.Reason

reason)

Constructs a

UserSessionEvent

.

---

#### Constructor Summary

Constructs a

UserSessionEvent

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

UserSessionEvent.Reason

getReason

()

Gets a reason of the user session change.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Gets a reason of the user session change.

Methods declared in class java.util.

EventObject

getSource

,

toString

---

#### Methods declared in class java.util. EventObject

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- UserSessionEvent

```java
public UserSessionEvent​(
UserSessionEvent.Reason
reason)
```

Constructs a

UserSessionEvent

.

**Parameters:** reason

- the reason of the user session change
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** UnsupportedOperationException

- if Desktop API is not supported on
the current platform
**See Also:** Desktop.isDesktopSupported()

,

GraphicsEnvironment.isHeadless()

============ METHOD DETAIL ==========

- Method Detail

- getReason

```java
public
UserSessionEvent.Reason
getReason()
```

Gets a reason of the user session change.

**Returns:** reason a reason
**See Also:** UserSessionEvent.Reason.UNSPECIFIED

,

UserSessionEvent.Reason.CONSOLE

,

UserSessionEvent.Reason.REMOTE

,

UserSessionEvent.Reason.LOCK

Constructor Detail

- UserSessionEvent

```java
public UserSessionEvent​(
UserSessionEvent.Reason
reason)
```

Constructs a

UserSessionEvent

.

**Parameters:** reason

- the reason of the user session change
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** UnsupportedOperationException

- if Desktop API is not supported on
the current platform
**See Also:** Desktop.isDesktopSupported()

,

GraphicsEnvironment.isHeadless()

---

#### Constructor Detail

UserSessionEvent

```java
public UserSessionEvent​(
UserSessionEvent.Reason
reason)
```

Constructs a

UserSessionEvent

.

**Parameters:** reason

- the reason of the user session change
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** UnsupportedOperationException

- if Desktop API is not supported on
the current platform
**See Also:** Desktop.isDesktopSupported()

,

GraphicsEnvironment.isHeadless()

---

#### UserSessionEvent

public UserSessionEvent​(

UserSessionEvent.Reason

reason)

Constructs a

UserSessionEvent

.

Method Detail

- getReason

```java
public
UserSessionEvent.Reason
getReason()
```

Gets a reason of the user session change.

**Returns:** reason a reason
**See Also:** UserSessionEvent.Reason.UNSPECIFIED

,

UserSessionEvent.Reason.CONSOLE

,

UserSessionEvent.Reason.REMOTE

,

UserSessionEvent.Reason.LOCK

---

#### Method Detail

getReason

```java
public
UserSessionEvent.Reason
getReason()
```

Gets a reason of the user session change.

**Returns:** reason a reason
**See Also:** UserSessionEvent.Reason.UNSPECIFIED

,

UserSessionEvent.Reason.CONSOLE

,

UserSessionEvent.Reason.REMOTE

,

UserSessionEvent.Reason.LOCK

---

#### getReason

public

UserSessionEvent.Reason

getReason()

Gets a reason of the user session change.

---

