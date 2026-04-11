# Interface AppForegroundListener

**Source:** `java.desktop\java\awt\desktop\AppForegroundListener.html`

### Class Description

```java
public interface
AppForegroundListener

extends
SystemEventListener
```

Implementors are notified when the app becomes the foreground app and when it
is no longer the foreground app. This notification is useful for hiding and
showing transient UI like palette windows which should be hidden when the app
is in the background.

**All Superinterfaces:** EventListener

,

SystemEventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void appRaisedToForeground​(
AppForegroundEvent
e)

Called when the app becomes the foreground app.

**Parameters:**
- e

- event

---

#### void appMovedToBackground​(
AppForegroundEvent
e)

Called when the app becomes the background app and another app becomes
the foreground app.

**Parameters:**
- e

- event

---

### Additional Sections

#### Interface AppForegroundListener

**All Superinterfaces:** EventListener

,

SystemEventListener

```java
public interface
AppForegroundListener

extends
SystemEventListener
```

Implementors are notified when the app becomes the foreground app and when it
is no longer the foreground app. This notification is useful for hiding and
showing transient UI like palette windows which should be hidden when the app
is in the background.

**Since:** 9

public interface

AppForegroundListener

extends

SystemEventListener

Implementors are notified when the app becomes the foreground app and when it
is no longer the foreground app. This notification is useful for hiding and
showing transient UI like palette windows which should be hidden when the app
is in the background.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

appMovedToBackground

​(

AppForegroundEvent

e)

Called when the app becomes the background app and another app becomes
the foreground app.

void

appRaisedToForeground

​(

AppForegroundEvent

e)

Called when the app becomes the foreground app.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

appMovedToBackground

​(

AppForegroundEvent

e)

Called when the app becomes the background app and another app becomes
the foreground app.

void

appRaisedToForeground

​(

AppForegroundEvent

e)

Called when the app becomes the foreground app.

---

#### Method Summary

Called when the app becomes the background app and another app becomes
the foreground app.

Called when the app becomes the foreground app.

============ METHOD DETAIL ==========

- Method Detail

- appRaisedToForeground

```java
void appRaisedToForeground​(
AppForegroundEvent
e)
```

Called when the app becomes the foreground app.

**Parameters:** e

- event

- appMovedToBackground

```java
void appMovedToBackground​(
AppForegroundEvent
e)
```

Called when the app becomes the background app and another app becomes
the foreground app.

**Parameters:** e

- event

Method Detail

- appRaisedToForeground

```java
void appRaisedToForeground​(
AppForegroundEvent
e)
```

Called when the app becomes the foreground app.

**Parameters:** e

- event

- appMovedToBackground

```java
void appMovedToBackground​(
AppForegroundEvent
e)
```

Called when the app becomes the background app and another app becomes
the foreground app.

**Parameters:** e

- event

---

#### Method Detail

appRaisedToForeground

```java
void appRaisedToForeground​(
AppForegroundEvent
e)
```

Called when the app becomes the foreground app.

**Parameters:** e

- event

---

#### appRaisedToForeground

void appRaisedToForeground​(

AppForegroundEvent

e)

Called when the app becomes the foreground app.

appMovedToBackground

```java
void appMovedToBackground​(
AppForegroundEvent
e)
```

Called when the app becomes the background app and another app becomes
the foreground app.

**Parameters:** e

- event

---

#### appMovedToBackground

void appMovedToBackground​(

AppForegroundEvent

e)

Called when the app becomes the background app and another app becomes
the foreground app.

---

