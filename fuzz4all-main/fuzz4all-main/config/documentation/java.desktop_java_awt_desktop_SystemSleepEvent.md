# Class SystemSleepEvent

**Source:** `java.desktop\java\awt\desktop\SystemSleepEvent.html`

### Class Description

```java
public final class
SystemSleepEvent

extends
AppEvent
```

Event sent when the system enters and exits power save sleep.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SystemSleepEvent()

Constructs a

SystemSleepEvent

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

#### Class SystemSleepEvent

java.lang.Object

- java.util.EventObject
- - java.awt.desktop.AppEvent
- - java.awt.desktop.SystemSleepEvent

java.util.EventObject

- java.awt.desktop.AppEvent
- - java.awt.desktop.SystemSleepEvent

java.awt.desktop.AppEvent

- java.awt.desktop.SystemSleepEvent

java.awt.desktop.SystemSleepEvent

**All Implemented Interfaces:** Serializable

```java
public final class
SystemSleepEvent

extends
AppEvent
```

Event sent when the system enters and exits power save sleep.

**Since:** 9
**See Also:** SystemSleepListener.systemAboutToSleep(SystemSleepEvent)

,

SystemSleepListener.systemAwoke(SystemSleepEvent)

,

Serialized Form

public final class

SystemSleepEvent

extends

AppEvent

Event sent when the system enters and exits power save sleep.

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

SystemSleepEvent

()

Constructs a

SystemSleepEvent

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

SystemSleepEvent

()

Constructs a

SystemSleepEvent

.

---

#### Constructor Summary

Constructs a

SystemSleepEvent

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

- SystemSleepEvent

```java
public SystemSleepEvent()
```

Constructs a

SystemSleepEvent

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

- SystemSleepEvent

```java
public SystemSleepEvent()
```

Constructs a

SystemSleepEvent

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

SystemSleepEvent

```java
public SystemSleepEvent()
```

Constructs a

SystemSleepEvent

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

#### SystemSleepEvent

public SystemSleepEvent()

Constructs a

SystemSleepEvent

.

---

