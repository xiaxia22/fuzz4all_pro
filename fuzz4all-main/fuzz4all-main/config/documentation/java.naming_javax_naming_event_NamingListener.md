# Interface NamingListener

**Source:** `java.naming\javax\naming\event\NamingListener.html`

### Class Description

```java
public interface
NamingListener

extends
EventListener
```

This interface is the root of listener interfaces that
handle

NamingEvent

s.
It does not make sense for a listener to implement just this interface.
A listener typically implements a subinterface of

NamingListener

,
such as

ObjectChangeListener

or

NamespaceChangeListener

.

This interface contains a single method,

namingExceptionThrown()

,
that must be implemented so that the listener can be notified of
exceptions that are thrown (by the service provider) while gathering
information about the events that they're interested in.
When this method is invoked, the listener has been automatically deregistered
from the

EventContext

with which it has registered.

For example, suppose a listener implements

ObjectChangeListener

and
registers with an

EventContext

.
Then, if the connection to the server is subsequently broken,
the listener will receive a

NamingExceptionEvent

and may
take some corrective action, such as notifying the user of the application.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void namingExceptionThrown​(
NamingExceptionEvent
evt)

Called when a naming exception is thrown while attempting
to fire a

NamingEvent

.

**Parameters:**
- evt

- The nonnull event.

---

### Additional Sections

#### Interface NamingListener

**All Superinterfaces:** EventListener

**All Known Subinterfaces:** NamespaceChangeListener

,

ObjectChangeListener

,

UnsolicitedNotificationListener

```java
public interface
NamingListener

extends
EventListener
```

This interface is the root of listener interfaces that
handle

NamingEvent

s.
It does not make sense for a listener to implement just this interface.
A listener typically implements a subinterface of

NamingListener

,
such as

ObjectChangeListener

or

NamespaceChangeListener

.

This interface contains a single method,

namingExceptionThrown()

,
that must be implemented so that the listener can be notified of
exceptions that are thrown (by the service provider) while gathering
information about the events that they're interested in.
When this method is invoked, the listener has been automatically deregistered
from the

EventContext

with which it has registered.

For example, suppose a listener implements

ObjectChangeListener

and
registers with an

EventContext

.
Then, if the connection to the server is subsequently broken,
the listener will receive a

NamingExceptionEvent

and may
take some corrective action, such as notifying the user of the application.

**Since:** 1.3
**See Also:** NamingEvent

,

NamingExceptionEvent

,

EventContext

,

EventDirContext

public interface

NamingListener

extends

EventListener

This interface is the root of listener interfaces that
handle

NamingEvent

s.
It does not make sense for a listener to implement just this interface.
A listener typically implements a subinterface of

NamingListener

,
such as

ObjectChangeListener

or

NamespaceChangeListener

.

This interface contains a single method,

namingExceptionThrown()

,
that must be implemented so that the listener can be notified of
exceptions that are thrown (by the service provider) while gathering
information about the events that they're interested in.
When this method is invoked, the listener has been automatically deregistered
from the

EventContext

with which it has registered.

For example, suppose a listener implements

ObjectChangeListener

and
registers with an

EventContext

.
Then, if the connection to the server is subsequently broken,
the listener will receive a

NamingExceptionEvent

and may
take some corrective action, such as notifying the user of the application.

This interface contains a single method,

namingExceptionThrown()

,
that must be implemented so that the listener can be notified of
exceptions that are thrown (by the service provider) while gathering
information about the events that they're interested in.
When this method is invoked, the listener has been automatically deregistered
from the

EventContext

with which it has registered.

For example, suppose a listener implements

ObjectChangeListener

and
registers with an

EventContext

.
Then, if the connection to the server is subsequently broken,
the listener will receive a

NamingExceptionEvent

and may
take some corrective action, such as notifying the user of the application.

For example, suppose a listener implements

ObjectChangeListener

and
registers with an

EventContext

.
Then, if the connection to the server is subsequently broken,
the listener will receive a

NamingExceptionEvent

and may
take some corrective action, such as notifying the user of the application.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

namingExceptionThrown

​(

NamingExceptionEvent

evt)

Called when a naming exception is thrown while attempting
to fire a

NamingEvent

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

namingExceptionThrown

​(

NamingExceptionEvent

evt)

Called when a naming exception is thrown while attempting
to fire a

NamingEvent

.

---

#### Method Summary

Called when a naming exception is thrown while attempting
to fire a

NamingEvent

.

============ METHOD DETAIL ==========

- Method Detail

- namingExceptionThrown

```java
void namingExceptionThrown​(
NamingExceptionEvent
evt)
```

Called when a naming exception is thrown while attempting
to fire a

NamingEvent

.

**Parameters:** evt

- The nonnull event.

Method Detail

- namingExceptionThrown

```java
void namingExceptionThrown​(
NamingExceptionEvent
evt)
```

Called when a naming exception is thrown while attempting
to fire a

NamingEvent

.

**Parameters:** evt

- The nonnull event.

---

#### Method Detail

namingExceptionThrown

```java
void namingExceptionThrown​(
NamingExceptionEvent
evt)
```

Called when a naming exception is thrown while attempting
to fire a

NamingEvent

.

**Parameters:** evt

- The nonnull event.

---

#### namingExceptionThrown

void namingExceptionThrown​(

NamingExceptionEvent

evt)

Called when a naming exception is thrown while attempting
to fire a

NamingEvent

.

---

