# Interface UnsolicitedNotificationListener

**Source:** `java.naming\javax\naming\ldap\UnsolicitedNotificationListener.html`

### Class Description

```java
public interface
UnsolicitedNotificationListener

extends
NamingListener
```

This interface is for handling

UnsolicitedNotificationEvent

.
"Unsolicited notification" is defined in

RFC 2251

.
It allows the server to send unsolicited notifications to the client.
An

UnsolicitedNotificationListener

must:

- Implement this interface and its method

Implement

NamingListener.namingExceptionThrown()

so
that it will be notified of exceptions thrown while attempting to
collect unsolicited notification events.

Register with the context using one of the

addNamingListener()

methods from

EventContext

or

EventDirContext

.
Only the

NamingListener

argument of these methods are applicable;
the rest are ignored for an

UnsolicitedNotificationListener

.
(These arguments might be applicable to the listener if it implements
other listener interfaces).

**All Superinterfaces:** EventListener

,

NamingListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void notificationReceived​(
UnsolicitedNotificationEvent
evt)

Called when an unsolicited notification has been received.

**Parameters:**
- evt

- The non-null UnsolicitedNotificationEvent

---

### Additional Sections

#### Interface UnsolicitedNotificationListener

**All Superinterfaces:** EventListener

,

NamingListener

```java
public interface
UnsolicitedNotificationListener

extends
NamingListener
```

This interface is for handling

UnsolicitedNotificationEvent

.
"Unsolicited notification" is defined in

RFC 2251

.
It allows the server to send unsolicited notifications to the client.
An

UnsolicitedNotificationListener

must:

- Implement this interface and its method

Implement

NamingListener.namingExceptionThrown()

so
that it will be notified of exceptions thrown while attempting to
collect unsolicited notification events.

Register with the context using one of the

addNamingListener()

methods from

EventContext

or

EventDirContext

.
Only the

NamingListener

argument of these methods are applicable;
the rest are ignored for an

UnsolicitedNotificationListener

.
(These arguments might be applicable to the listener if it implements
other listener interfaces).

**Since:** 1.3
**See Also:** UnsolicitedNotificationEvent

,

UnsolicitedNotification

,

EventContext.addNamingListener(javax.naming.Name, int, javax.naming.event.NamingListener)

,

EventDirContext.addNamingListener(javax.naming.Name, java.lang.String, javax.naming.directory.SearchControls, javax.naming.event.NamingListener)

,

EventContext.removeNamingListener(javax.naming.event.NamingListener)

public interface

UnsolicitedNotificationListener

extends

NamingListener

This interface is for handling

UnsolicitedNotificationEvent

.
"Unsolicited notification" is defined in

RFC 2251

.
It allows the server to send unsolicited notifications to the client.
An

UnsolicitedNotificationListener

must:

- Implement this interface and its method

Implement

NamingListener.namingExceptionThrown()

so
that it will be notified of exceptions thrown while attempting to
collect unsolicited notification events.

Register with the context using one of the

addNamingListener()

methods from

EventContext

or

EventDirContext

.
Only the

NamingListener

argument of these methods are applicable;
the rest are ignored for an

UnsolicitedNotificationListener

.
(These arguments might be applicable to the listener if it implements
other listener interfaces).

Implement this interface and its method

Implement

NamingListener.namingExceptionThrown()

so
that it will be notified of exceptions thrown while attempting to
collect unsolicited notification events.

Register with the context using one of the

addNamingListener()

methods from

EventContext

or

EventDirContext

.
Only the

NamingListener

argument of these methods are applicable;
the rest are ignored for an

UnsolicitedNotificationListener

.
(These arguments might be applicable to the listener if it implements
other listener interfaces).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

notificationReceived

​(

UnsolicitedNotificationEvent

evt)

Called when an unsolicited notification has been received.

- Methods declared in interface javax.naming.event.

NamingListener

namingExceptionThrown

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

notificationReceived

​(

UnsolicitedNotificationEvent

evt)

Called when an unsolicited notification has been received.

- Methods declared in interface javax.naming.event.

NamingListener

namingExceptionThrown

---

#### Method Summary

Called when an unsolicited notification has been received.

Methods declared in interface javax.naming.event.

NamingListener

namingExceptionThrown

---

#### Methods declared in interface javax.naming.event. NamingListener

============ METHOD DETAIL ==========

- Method Detail

- notificationReceived

```java
void notificationReceived​(
UnsolicitedNotificationEvent
evt)
```

Called when an unsolicited notification has been received.

**Parameters:** evt

- The non-null UnsolicitedNotificationEvent

Method Detail

- notificationReceived

```java
void notificationReceived​(
UnsolicitedNotificationEvent
evt)
```

Called when an unsolicited notification has been received.

**Parameters:** evt

- The non-null UnsolicitedNotificationEvent

---

#### Method Detail

notificationReceived

```java
void notificationReceived​(
UnsolicitedNotificationEvent
evt)
```

Called when an unsolicited notification has been received.

**Parameters:** evt

- The non-null UnsolicitedNotificationEvent

---

#### notificationReceived

void notificationReceived​(

UnsolicitedNotificationEvent

evt)

Called when an unsolicited notification has been received.

---

