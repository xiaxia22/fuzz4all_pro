# Interface BeanContextMembershipListener

**Source:** `java.desktop\java\beans\beancontext\BeanContextMembershipListener.html`

### Class Description

```java
public interface
BeanContextMembershipListener

extends
EventListener
```

Compliant BeanContexts fire events on this interface when the state of
the membership of the BeanContext changes.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void childrenAdded​(
BeanContextMembershipEvent
bcme)

Called when a child or list of children is added to a

BeanContext

that this listener is registered with.

**Parameters:**
- bcme

- The

BeanContextMembershipEvent

describing the change that occurred.

---

#### void childrenRemoved​(
BeanContextMembershipEvent
bcme)

Called when a child or list of children is removed
from a

BeanContext

that this listener
is registered with.

**Parameters:**
- bcme

- The

BeanContextMembershipEvent

describing the change that occurred.

---

### Additional Sections

#### Interface BeanContextMembershipListener

**All Superinterfaces:** EventListener

```java
public interface
BeanContextMembershipListener

extends
EventListener
```

Compliant BeanContexts fire events on this interface when the state of
the membership of the BeanContext changes.

**Since:** 1.2
**See Also:** BeanContext

public interface

BeanContextMembershipListener

extends

EventListener

Compliant BeanContexts fire events on this interface when the state of
the membership of the BeanContext changes.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

childrenAdded

​(

BeanContextMembershipEvent

bcme)

Called when a child or list of children is added to a

BeanContext

that this listener is registered with.

void

childrenRemoved

​(

BeanContextMembershipEvent

bcme)

Called when a child or list of children is removed
from a

BeanContext

that this listener
is registered with.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

childrenAdded

​(

BeanContextMembershipEvent

bcme)

Called when a child or list of children is added to a

BeanContext

that this listener is registered with.

void

childrenRemoved

​(

BeanContextMembershipEvent

bcme)

Called when a child or list of children is removed
from a

BeanContext

that this listener
is registered with.

---

#### Method Summary

Called when a child or list of children is added to a

BeanContext

that this listener is registered with.

Called when a child or list of children is removed
from a

BeanContext

that this listener
is registered with.

============ METHOD DETAIL ==========

- Method Detail

- childrenAdded

```java
void childrenAdded​(
BeanContextMembershipEvent
bcme)
```

Called when a child or list of children is added to a

BeanContext

that this listener is registered with.

**Parameters:** bcme

- The

BeanContextMembershipEvent

describing the change that occurred.

- childrenRemoved

```java
void childrenRemoved​(
BeanContextMembershipEvent
bcme)
```

Called when a child or list of children is removed
from a

BeanContext

that this listener
is registered with.

**Parameters:** bcme

- The

BeanContextMembershipEvent

describing the change that occurred.

Method Detail

- childrenAdded

```java
void childrenAdded​(
BeanContextMembershipEvent
bcme)
```

Called when a child or list of children is added to a

BeanContext

that this listener is registered with.

**Parameters:** bcme

- The

BeanContextMembershipEvent

describing the change that occurred.

- childrenRemoved

```java
void childrenRemoved​(
BeanContextMembershipEvent
bcme)
```

Called when a child or list of children is removed
from a

BeanContext

that this listener
is registered with.

**Parameters:** bcme

- The

BeanContextMembershipEvent

describing the change that occurred.

---

#### Method Detail

childrenAdded

```java
void childrenAdded​(
BeanContextMembershipEvent
bcme)
```

Called when a child or list of children is added to a

BeanContext

that this listener is registered with.

**Parameters:** bcme

- The

BeanContextMembershipEvent

describing the change that occurred.

---

#### childrenAdded

void childrenAdded​(

BeanContextMembershipEvent

bcme)

Called when a child or list of children is added to a

BeanContext

that this listener is registered with.

childrenRemoved

```java
void childrenRemoved​(
BeanContextMembershipEvent
bcme)
```

Called when a child or list of children is removed
from a

BeanContext

that this listener
is registered with.

**Parameters:** bcme

- The

BeanContextMembershipEvent

describing the change that occurred.

---

#### childrenRemoved

void childrenRemoved​(

BeanContextMembershipEvent

bcme)

Called when a child or list of children is removed
from a

BeanContext

that this listener
is registered with.

---

