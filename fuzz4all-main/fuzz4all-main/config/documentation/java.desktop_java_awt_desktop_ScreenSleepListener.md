# Interface ScreenSleepListener

**Source:** `java.desktop\java\awt\desktop\ScreenSleepListener.html`

### Class Description

```java
public interface
ScreenSleepListener

extends
SystemEventListener
```

Implementors receive notification when the displays attached to the system have entered power save sleep.

This notification is useful for discontinuing a costly animation, or indicating that the user is no longer present on a network service.

**All Superinterfaces:** EventListener

,

SystemEventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void screenAboutToSleep​(
ScreenSleepEvent
e)

Called when the system displays have entered power save sleep.

**Parameters:**
- e

- the screen sleep event

---

#### void screenAwoke​(
ScreenSleepEvent
e)

Called when the system displays have awoken from power save sleep.

**Parameters:**
- e

- the screen sleep event

---

### Additional Sections

#### Interface ScreenSleepListener

**All Superinterfaces:** EventListener

,

SystemEventListener

```java
public interface
ScreenSleepListener

extends
SystemEventListener
```

Implementors receive notification when the displays attached to the system have entered power save sleep.

This notification is useful for discontinuing a costly animation, or indicating that the user is no longer present on a network service.

**Since:** 9

public interface

ScreenSleepListener

extends

SystemEventListener

Implementors receive notification when the displays attached to the system have entered power save sleep.

This notification is useful for discontinuing a costly animation, or indicating that the user is no longer present on a network service.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

screenAboutToSleep

​(

ScreenSleepEvent

e)

Called when the system displays have entered power save sleep.

void

screenAwoke

​(

ScreenSleepEvent

e)

Called when the system displays have awoken from power save sleep.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

screenAboutToSleep

​(

ScreenSleepEvent

e)

Called when the system displays have entered power save sleep.

void

screenAwoke

​(

ScreenSleepEvent

e)

Called when the system displays have awoken from power save sleep.

---

#### Method Summary

Called when the system displays have entered power save sleep.

Called when the system displays have awoken from power save sleep.

============ METHOD DETAIL ==========

- Method Detail

- screenAboutToSleep

```java
void screenAboutToSleep​(
ScreenSleepEvent
e)
```

Called when the system displays have entered power save sleep.

**Parameters:** e

- the screen sleep event

- screenAwoke

```java
void screenAwoke​(
ScreenSleepEvent
e)
```

Called when the system displays have awoken from power save sleep.

**Parameters:** e

- the screen sleep event

Method Detail

- screenAboutToSleep

```java
void screenAboutToSleep​(
ScreenSleepEvent
e)
```

Called when the system displays have entered power save sleep.

**Parameters:** e

- the screen sleep event

- screenAwoke

```java
void screenAwoke​(
ScreenSleepEvent
e)
```

Called when the system displays have awoken from power save sleep.

**Parameters:** e

- the screen sleep event

---

#### Method Detail

screenAboutToSleep

```java
void screenAboutToSleep​(
ScreenSleepEvent
e)
```

Called when the system displays have entered power save sleep.

**Parameters:** e

- the screen sleep event

---

#### screenAboutToSleep

void screenAboutToSleep​(

ScreenSleepEvent

e)

Called when the system displays have entered power save sleep.

screenAwoke

```java
void screenAwoke​(
ScreenSleepEvent
e)
```

Called when the system displays have awoken from power save sleep.

**Parameters:** e

- the screen sleep event

---

#### screenAwoke

void screenAwoke​(

ScreenSleepEvent

e)

Called when the system displays have awoken from power save sleep.

---

