# Interface BeanContextServiceRevokedListener

**Source:** `java.desktop\java\beans\beancontext\BeanContextServiceRevokedListener.html`

### Class Description

```java
public interface
BeanContextServiceRevokedListener

extends
EventListener
```

The listener interface for receiving

BeanContextServiceRevokedEvent

objects. A class that is
interested in processing a

BeanContextServiceRevokedEvent

implements this interface.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void serviceRevoked​(
BeanContextServiceRevokedEvent
bcsre)

The service named has been revoked. getService requests for
this service will no longer be satisfied.

**Parameters:**
- bcsre

- the

BeanContextServiceRevokedEvent

received
by this listener.

---

### Additional Sections

#### Interface BeanContextServiceRevokedListener

**All Superinterfaces:** EventListener

**All Known Subinterfaces:** BeanContextServices

,

BeanContextServicesListener

**All Known Implementing Classes:** BeanContextChildSupport

,

BeanContextServicesSupport

,

BeanContextServicesSupport.BCSSProxyServiceProvider

,

BeanContextSupport

```java
public interface
BeanContextServiceRevokedListener

extends
EventListener
```

The listener interface for receiving

BeanContextServiceRevokedEvent

objects. A class that is
interested in processing a

BeanContextServiceRevokedEvent

implements this interface.

public interface

BeanContextServiceRevokedListener

extends

EventListener

The listener interface for receiving

BeanContextServiceRevokedEvent

objects. A class that is
interested in processing a

BeanContextServiceRevokedEvent

implements this interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

serviceRevoked

​(

BeanContextServiceRevokedEvent

bcsre)

The service named has been revoked. getService requests for
this service will no longer be satisfied.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

serviceRevoked

​(

BeanContextServiceRevokedEvent

bcsre)

The service named has been revoked. getService requests for
this service will no longer be satisfied.

---

#### Method Summary

The service named has been revoked. getService requests for
this service will no longer be satisfied.

============ METHOD DETAIL ==========

- Method Detail

- serviceRevoked

```java
void serviceRevoked​(
BeanContextServiceRevokedEvent
bcsre)
```

The service named has been revoked. getService requests for
this service will no longer be satisfied.

**Parameters:** bcsre

- the

BeanContextServiceRevokedEvent

received
by this listener.

Method Detail

- serviceRevoked

```java
void serviceRevoked​(
BeanContextServiceRevokedEvent
bcsre)
```

The service named has been revoked. getService requests for
this service will no longer be satisfied.

**Parameters:** bcsre

- the

BeanContextServiceRevokedEvent

received
by this listener.

---

#### Method Detail

serviceRevoked

```java
void serviceRevoked​(
BeanContextServiceRevokedEvent
bcsre)
```

The service named has been revoked. getService requests for
this service will no longer be satisfied.

**Parameters:** bcsre

- the

BeanContextServiceRevokedEvent

received
by this listener.

---

#### serviceRevoked

void serviceRevoked​(

BeanContextServiceRevokedEvent

bcsre)

The service named has been revoked. getService requests for
this service will no longer be satisfied.

---

