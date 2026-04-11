# Interface SystemSleepListener

**Source:** `java.desktop\java\awt\desktop\SystemSleepListener.html`

### Class Description

```java
public interface
SystemSleepListener

extends
SystemEventListener
```

Implementors receive notification as the system is entering sleep, and after
the system wakes.

This notification is useful for disconnecting from network services prior to
sleep, or re-establishing a connection if the network configuration has
changed during sleep.

**All Superinterfaces:** EventListener

,

SystemEventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void systemAboutToSleep​(
SystemSleepEvent
e)

Called when the system is about to sleep. Note: This message may not be
delivered prior to the actual system sleep, and may be processed after
the corresponding wake has occurred.

**Parameters:**
- e

- the system sleep event

---

#### void systemAwoke​(
SystemSleepEvent
e)

Called after the system has awoken from sleeping.

**Parameters:**
- e

- the system sleep event

---

### Additional Sections

#### Interface SystemSleepListener

**All Superinterfaces:** EventListener

,

SystemEventListener

```java
public interface
SystemSleepListener

extends
SystemEventListener
```

Implementors receive notification as the system is entering sleep, and after
the system wakes.

This notification is useful for disconnecting from network services prior to
sleep, or re-establishing a connection if the network configuration has
changed during sleep.

**Since:** 9

public interface

SystemSleepListener

extends

SystemEventListener

Implementors receive notification as the system is entering sleep, and after
the system wakes.

This notification is useful for disconnecting from network services prior to
sleep, or re-establishing a connection if the network configuration has
changed during sleep.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

systemAboutToSleep

​(

SystemSleepEvent

e)

Called when the system is about to sleep.

void

systemAwoke

​(

SystemSleepEvent

e)

Called after the system has awoken from sleeping.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

systemAboutToSleep

​(

SystemSleepEvent

e)

Called when the system is about to sleep.

void

systemAwoke

​(

SystemSleepEvent

e)

Called after the system has awoken from sleeping.

---

#### Method Summary

Called when the system is about to sleep.

Called after the system has awoken from sleeping.

============ METHOD DETAIL ==========

- Method Detail

- systemAboutToSleep

```java
void systemAboutToSleep​(
SystemSleepEvent
e)
```

Called when the system is about to sleep. Note: This message may not be
delivered prior to the actual system sleep, and may be processed after
the corresponding wake has occurred.

**Parameters:** e

- the system sleep event

- systemAwoke

```java
void systemAwoke​(
SystemSleepEvent
e)
```

Called after the system has awoken from sleeping.

**Parameters:** e

- the system sleep event

Method Detail

- systemAboutToSleep

```java
void systemAboutToSleep​(
SystemSleepEvent
e)
```

Called when the system is about to sleep. Note: This message may not be
delivered prior to the actual system sleep, and may be processed after
the corresponding wake has occurred.

**Parameters:** e

- the system sleep event

- systemAwoke

```java
void systemAwoke​(
SystemSleepEvent
e)
```

Called after the system has awoken from sleeping.

**Parameters:** e

- the system sleep event

---

#### Method Detail

systemAboutToSleep

```java
void systemAboutToSleep​(
SystemSleepEvent
e)
```

Called when the system is about to sleep. Note: This message may not be
delivered prior to the actual system sleep, and may be processed after
the corresponding wake has occurred.

**Parameters:** e

- the system sleep event

---

#### systemAboutToSleep

void systemAboutToSleep​(

SystemSleepEvent

e)

Called when the system is about to sleep. Note: This message may not be
delivered prior to the actual system sleep, and may be processed after
the corresponding wake has occurred.

systemAwoke

```java
void systemAwoke​(
SystemSleepEvent
e)
```

Called after the system has awoken from sleeping.

**Parameters:** e

- the system sleep event

---

#### systemAwoke

void systemAwoke​(

SystemSleepEvent

e)

Called after the system has awoken from sleeping.

---

