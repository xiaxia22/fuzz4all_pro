# Class AppForegroundEvent

**Source:** `java.desktop\java\awt\desktop\AppForegroundEvent.html`

### Class Description

```java
public final class
AppForegroundEvent

extends
AppEvent
```

Event sent when the application has become the foreground app, and when it is
no longer the foreground app.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AppForegroundEvent()

Constructs an

AppForegroundEvent

.

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

*No entries found.*

### Additional Sections

#### Class AppForegroundEvent

java.lang.Object

- java.util.EventObject
- - java.awt.desktop.AppEvent
- - java.awt.desktop.AppForegroundEvent

java.util.EventObject

- java.awt.desktop.AppEvent
- - java.awt.desktop.AppForegroundEvent

java.awt.desktop.AppEvent

- java.awt.desktop.AppForegroundEvent

java.awt.desktop.AppForegroundEvent

**All Implemented Interfaces:** Serializable

```java
public final class
AppForegroundEvent

extends
AppEvent
```

Event sent when the application has become the foreground app, and when it is
no longer the foreground app.

**Since:** 9
**See Also:** AppForegroundListener.appRaisedToForeground(AppForegroundEvent)

,

AppForegroundListener.appMovedToBackground(AppForegroundEvent)

,

Serialized Form

public final class

AppForegroundEvent

extends

AppEvent

Event sent when the application has become the foreground app, and when it is
no longer the foreground app.

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

AppForegroundEvent

()

Constructs an

AppForegroundEvent

.

========== METHOD SUMMARY ===========

- Method Summary

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

AppForegroundEvent

()

Constructs an

AppForegroundEvent

.

---

#### Constructor Summary

Constructs an

AppForegroundEvent

.

Method Summary

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

- AppForegroundEvent

```java
public AppForegroundEvent()
```

Constructs an

AppForegroundEvent

.

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

Constructor Detail

- AppForegroundEvent

```java
public AppForegroundEvent()
```

Constructs an

AppForegroundEvent

.

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

AppForegroundEvent

```java
public AppForegroundEvent()
```

Constructs an

AppForegroundEvent

.

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

#### AppForegroundEvent

public AppForegroundEvent()

Constructs an

AppForegroundEvent

.

---

