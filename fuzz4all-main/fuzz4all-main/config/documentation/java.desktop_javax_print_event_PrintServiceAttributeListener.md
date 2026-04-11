# Interface PrintServiceAttributeListener

**Source:** `java.desktop\javax\print\event\PrintServiceAttributeListener.html`

### Class Description

```java
public interface
PrintServiceAttributeListener
```

Implementations of this listener interface are attached to a

PrintService

to monitor the status of the
print service.

To monitor a particular job see

PrintJobListener

and

PrintJobAttributeListener

.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void attributeUpdate​(
PrintServiceAttributeEvent
psae)

Called to notify a listener of an event in the print service. The service
will call this method on an event notification thread. The client should
not perform lengthy processing in this callback or subsequent event
notifications may be blocked.

**Parameters:**
- psae

- the event being notified

---

### Additional Sections

#### Interface PrintServiceAttributeListener

```java
public interface
PrintServiceAttributeListener
```

Implementations of this listener interface are attached to a

PrintService

to monitor the status of the
print service.

To monitor a particular job see

PrintJobListener

and

PrintJobAttributeListener

.

public interface

PrintServiceAttributeListener

Implementations of this listener interface are attached to a

PrintService

to monitor the status of the
print service.

To monitor a particular job see

PrintJobListener

and

PrintJobAttributeListener

.

To monitor a particular job see

PrintJobListener

and

PrintJobAttributeListener

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

attributeUpdate

​(

PrintServiceAttributeEvent

psae)

Called to notify a listener of an event in the print service.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

attributeUpdate

​(

PrintServiceAttributeEvent

psae)

Called to notify a listener of an event in the print service.

---

#### Method Summary

Called to notify a listener of an event in the print service.

============ METHOD DETAIL ==========

- Method Detail

- attributeUpdate

```java
void attributeUpdate​(
PrintServiceAttributeEvent
psae)
```

Called to notify a listener of an event in the print service. The service
will call this method on an event notification thread. The client should
not perform lengthy processing in this callback or subsequent event
notifications may be blocked.

**Parameters:** psae

- the event being notified

Method Detail

- attributeUpdate

```java
void attributeUpdate​(
PrintServiceAttributeEvent
psae)
```

Called to notify a listener of an event in the print service. The service
will call this method on an event notification thread. The client should
not perform lengthy processing in this callback or subsequent event
notifications may be blocked.

**Parameters:** psae

- the event being notified

---

#### Method Detail

attributeUpdate

```java
void attributeUpdate​(
PrintServiceAttributeEvent
psae)
```

Called to notify a listener of an event in the print service. The service
will call this method on an event notification thread. The client should
not perform lengthy processing in this callback or subsequent event
notifications may be blocked.

**Parameters:** psae

- the event being notified

---

#### attributeUpdate

void attributeUpdate​(

PrintServiceAttributeEvent

psae)

Called to notify a listener of an event in the print service. The service
will call this method on an event notification thread. The client should
not perform lengthy processing in this callback or subsequent event
notifications may be blocked.

---

