# Class ScreenSleepEvent

**Source:** `java.desktop\java\awt\desktop\ScreenSleepEvent.html`

### Class Description

```java
public final class
ScreenSleepEvent

extends
AppEvent
```

Event sent when the displays attached to the system enter and exit power save
sleep.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ScreenSleepEvent()

Constructs a

ScreenSleepEvent

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

#### Class ScreenSleepEvent

java.lang.Object

- java.util.EventObject
- - java.awt.desktop.AppEvent
- - java.awt.desktop.ScreenSleepEvent

java.util.EventObject

- java.awt.desktop.AppEvent
- - java.awt.desktop.ScreenSleepEvent

java.awt.desktop.AppEvent

- java.awt.desktop.ScreenSleepEvent

java.awt.desktop.ScreenSleepEvent

**All Implemented Interfaces:** Serializable

```java
public final class
ScreenSleepEvent

extends
AppEvent
```

Event sent when the displays attached to the system enter and exit power save
sleep.

**Since:** 9
**See Also:** ScreenSleepListener.screenAboutToSleep(ScreenSleepEvent)

,

ScreenSleepListener.screenAwoke(ScreenSleepEvent)

,

Serialized Form

public final class

ScreenSleepEvent

extends

AppEvent

Event sent when the displays attached to the system enter and exit power save
sleep.

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

ScreenSleepEvent

()

Constructs a

ScreenSleepEvent

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

ScreenSleepEvent

()

Constructs a

ScreenSleepEvent

.

---

#### Constructor Summary

Constructs a

ScreenSleepEvent

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

- ScreenSleepEvent

```java
public ScreenSleepEvent()
```

Constructs a

ScreenSleepEvent

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

- ScreenSleepEvent

```java
public ScreenSleepEvent()
```

Constructs a

ScreenSleepEvent

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

ScreenSleepEvent

```java
public ScreenSleepEvent()
```

Constructs a

ScreenSleepEvent

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

#### ScreenSleepEvent

public ScreenSleepEvent()

Constructs a

ScreenSleepEvent

.

---

