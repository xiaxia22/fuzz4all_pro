# Interface BeanContextServicesListener

**Source:** `java.desktop\java\beans\beancontext\BeanContextServicesListener.html`

### Class Description

```java
public interface
BeanContextServicesListener

extends
BeanContextServiceRevokedListener
```

The listener interface for receiving

BeanContextServiceAvailableEvent

objects.
A class that is interested in processing a

BeanContextServiceAvailableEvent

implements this interface.

**All Superinterfaces:** BeanContextServiceRevokedListener

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void serviceAvailable​(
BeanContextServiceAvailableEvent
bcsae)

The service named has been registered. getService requests for
this service may now be made.

**Parameters:**
- bcsae

- the

BeanContextServiceAvailableEvent

---

### Additional Sections

#### Interface BeanContextServicesListener

**All Superinterfaces:** BeanContextServiceRevokedListener

,

EventListener

**All Known Subinterfaces:** BeanContextServices

**All Known Implementing Classes:** BeanContextChildSupport

,

BeanContextServicesSupport

,

BeanContextSupport

```java
public interface
BeanContextServicesListener

extends
BeanContextServiceRevokedListener
```

The listener interface for receiving

BeanContextServiceAvailableEvent

objects.
A class that is interested in processing a

BeanContextServiceAvailableEvent

implements this interface.

public interface

BeanContextServicesListener

extends

BeanContextServiceRevokedListener

The listener interface for receiving

BeanContextServiceAvailableEvent

objects.
A class that is interested in processing a

BeanContextServiceAvailableEvent

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

serviceAvailable

​(

BeanContextServiceAvailableEvent

bcsae)

The service named has been registered. getService requests for
this service may now be made.

- Methods declared in interface java.beans.beancontext.

BeanContextServiceRevokedListener

serviceRevoked

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

serviceAvailable

​(

BeanContextServiceAvailableEvent

bcsae)

The service named has been registered. getService requests for
this service may now be made.

- Methods declared in interface java.beans.beancontext.

BeanContextServiceRevokedListener

serviceRevoked

---

#### Method Summary

The service named has been registered. getService requests for
this service may now be made.

Methods declared in interface java.beans.beancontext.

BeanContextServiceRevokedListener

serviceRevoked

---

#### Methods declared in interface java.beans.beancontext. BeanContextServiceRevokedListener

============ METHOD DETAIL ==========

- Method Detail

- serviceAvailable

```java
void serviceAvailable​(
BeanContextServiceAvailableEvent
bcsae)
```

The service named has been registered. getService requests for
this service may now be made.

**Parameters:** bcsae

- the

BeanContextServiceAvailableEvent

Method Detail

- serviceAvailable

```java
void serviceAvailable​(
BeanContextServiceAvailableEvent
bcsae)
```

The service named has been registered. getService requests for
this service may now be made.

**Parameters:** bcsae

- the

BeanContextServiceAvailableEvent

---

#### Method Detail

serviceAvailable

```java
void serviceAvailable​(
BeanContextServiceAvailableEvent
bcsae)
```

The service named has been registered. getService requests for
this service may now be made.

**Parameters:** bcsae

- the

BeanContextServiceAvailableEvent

---

#### serviceAvailable

void serviceAvailable​(

BeanContextServiceAvailableEvent

bcsae)

The service named has been registered. getService requests for
this service may now be made.

---

