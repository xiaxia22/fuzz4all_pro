# Interface SSLSessionBindingListener

**Source:** `java.base\javax\net\ssl\SSLSessionBindingListener.html`

### Class Description

```java
public interface
SSLSessionBindingListener

extends
EventListener
```

This interface is implemented by objects which want to know when
they are being bound or unbound from a SSLSession. When either event
occurs via

SSLSession.putValue(String, Object)

or

SSLSession.removeValue(String)

, the event is communicated
through a SSLSessionBindingEvent identifying the session.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void valueBound​(
SSLSessionBindingEvent
event)

This is called to notify the listener that it is being bound into
an SSLSession.

**Parameters:**
- event

- the event identifying the SSLSession into
which the listener is being bound.

---

#### void valueUnbound​(
SSLSessionBindingEvent
event)

This is called to notify the listener that it is being unbound
from a SSLSession.

**Parameters:**
- event

- the event identifying the SSLSession from
which the listener is being unbound.

---

### Additional Sections

#### Interface SSLSessionBindingListener

**All Superinterfaces:** EventListener

```java
public interface
SSLSessionBindingListener

extends
EventListener
```

This interface is implemented by objects which want to know when
they are being bound or unbound from a SSLSession. When either event
occurs via

SSLSession.putValue(String, Object)

or

SSLSession.removeValue(String)

, the event is communicated
through a SSLSessionBindingEvent identifying the session.

**Since:** 1.4
**See Also:** SSLSession

,

SSLSessionBindingEvent

public interface

SSLSessionBindingListener

extends

EventListener

This interface is implemented by objects which want to know when
they are being bound or unbound from a SSLSession. When either event
occurs via

SSLSession.putValue(String, Object)

or

SSLSession.removeValue(String)

, the event is communicated
through a SSLSessionBindingEvent identifying the session.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

valueBound

​(

SSLSessionBindingEvent

event)

This is called to notify the listener that it is being bound into
an SSLSession.

void

valueUnbound

​(

SSLSessionBindingEvent

event)

This is called to notify the listener that it is being unbound
from a SSLSession.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

valueBound

​(

SSLSessionBindingEvent

event)

This is called to notify the listener that it is being bound into
an SSLSession.

void

valueUnbound

​(

SSLSessionBindingEvent

event)

This is called to notify the listener that it is being unbound
from a SSLSession.

---

#### Method Summary

This is called to notify the listener that it is being bound into
an SSLSession.

This is called to notify the listener that it is being unbound
from a SSLSession.

============ METHOD DETAIL ==========

- Method Detail

- valueBound

```java
void valueBound​(
SSLSessionBindingEvent
event)
```

This is called to notify the listener that it is being bound into
an SSLSession.

**Parameters:** event

- the event identifying the SSLSession into
which the listener is being bound.

- valueUnbound

```java
void valueUnbound​(
SSLSessionBindingEvent
event)
```

This is called to notify the listener that it is being unbound
from a SSLSession.

**Parameters:** event

- the event identifying the SSLSession from
which the listener is being unbound.

Method Detail

- valueBound

```java
void valueBound​(
SSLSessionBindingEvent
event)
```

This is called to notify the listener that it is being bound into
an SSLSession.

**Parameters:** event

- the event identifying the SSLSession into
which the listener is being bound.

- valueUnbound

```java
void valueUnbound​(
SSLSessionBindingEvent
event)
```

This is called to notify the listener that it is being unbound
from a SSLSession.

**Parameters:** event

- the event identifying the SSLSession from
which the listener is being unbound.

---

#### Method Detail

valueBound

```java
void valueBound​(
SSLSessionBindingEvent
event)
```

This is called to notify the listener that it is being bound into
an SSLSession.

**Parameters:** event

- the event identifying the SSLSession into
which the listener is being bound.

---

#### valueBound

void valueBound​(

SSLSessionBindingEvent

event)

This is called to notify the listener that it is being bound into
an SSLSession.

valueUnbound

```java
void valueUnbound​(
SSLSessionBindingEvent
event)
```

This is called to notify the listener that it is being unbound
from a SSLSession.

**Parameters:** event

- the event identifying the SSLSession from
which the listener is being unbound.

---

#### valueUnbound

void valueUnbound​(

SSLSessionBindingEvent

event)

This is called to notify the listener that it is being unbound
from a SSLSession.

---

