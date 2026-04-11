# Interface HandshakeCompletedListener

**Source:** `java.base\javax\net\ssl\HandshakeCompletedListener.html`

### Class Description

```java
public interface
HandshakeCompletedListener

extends
EventListener
```

This interface is implemented by any class which wants to receive
notifications about the completion of an SSL protocol handshake
on a given SSL connection.

When an SSL handshake completes, new security parameters will
have been established. Those parameters always include the security
keys used to protect messages. They may also include parameters
associated with a new

session

such as authenticated
peer identity and a new SSL cipher suite.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void handshakeCompleted​(
HandshakeCompletedEvent
event)

This method is invoked on registered objects
when a SSL handshake is completed.

**Parameters:**
- event

- the event identifying when the SSL Handshake
completed on a given SSL connection

---

### Additional Sections

#### Interface HandshakeCompletedListener

**All Superinterfaces:** EventListener

```java
public interface
HandshakeCompletedListener

extends
EventListener
```

This interface is implemented by any class which wants to receive
notifications about the completion of an SSL protocol handshake
on a given SSL connection.

When an SSL handshake completes, new security parameters will
have been established. Those parameters always include the security
keys used to protect messages. They may also include parameters
associated with a new

session

such as authenticated
peer identity and a new SSL cipher suite.

**Since:** 1.4

public interface

HandshakeCompletedListener

extends

EventListener

This interface is implemented by any class which wants to receive
notifications about the completion of an SSL protocol handshake
on a given SSL connection.

When an SSL handshake completes, new security parameters will
have been established. Those parameters always include the security
keys used to protect messages. They may also include parameters
associated with a new

session

such as authenticated
peer identity and a new SSL cipher suite.

When an SSL handshake completes, new security parameters will
have been established. Those parameters always include the security
keys used to protect messages. They may also include parameters
associated with a new

session

such as authenticated
peer identity and a new SSL cipher suite.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

handshakeCompleted

​(

HandshakeCompletedEvent

event)

This method is invoked on registered objects
when a SSL handshake is completed.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

handshakeCompleted

​(

HandshakeCompletedEvent

event)

This method is invoked on registered objects
when a SSL handshake is completed.

---

#### Method Summary

This method is invoked on registered objects
when a SSL handshake is completed.

============ METHOD DETAIL ==========

- Method Detail

- handshakeCompleted

```java
void handshakeCompleted​(
HandshakeCompletedEvent
event)
```

This method is invoked on registered objects
when a SSL handshake is completed.

**Parameters:** event

- the event identifying when the SSL Handshake
completed on a given SSL connection

Method Detail

- handshakeCompleted

```java
void handshakeCompleted​(
HandshakeCompletedEvent
event)
```

This method is invoked on registered objects
when a SSL handshake is completed.

**Parameters:** event

- the event identifying when the SSL Handshake
completed on a given SSL connection

---

#### Method Detail

handshakeCompleted

```java
void handshakeCompleted​(
HandshakeCompletedEvent
event)
```

This method is invoked on registered objects
when a SSL handshake is completed.

**Parameters:** event

- the event identifying when the SSL Handshake
completed on a given SSL connection

---

#### handshakeCompleted

void handshakeCompleted​(

HandshakeCompletedEvent

event)

This method is invoked on registered objects
when a SSL handshake is completed.

---

