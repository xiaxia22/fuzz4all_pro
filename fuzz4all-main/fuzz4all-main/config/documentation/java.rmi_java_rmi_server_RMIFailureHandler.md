# Interface RMIFailureHandler

**Source:** `java.rmi\java\rmi\server\RMIFailureHandler.html`

### Class Description

```java
public interface
RMIFailureHandler
```

An

RMIFailureHandler

can be registered via the

RMISocketFactory.setFailureHandler

call. The

failure

method of the handler is invoked when the RMI
runtime is unable to create a

ServerSocket

to listen
for incoming calls. The

failure

method returns a boolean
indicating whether the runtime should attempt to re-create the

ServerSocket

.

**Since:** 1.1

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean failure​(
Exception
ex)

The

failure

callback is invoked when the RMI
runtime is unable to create a

ServerSocket

via the

RMISocketFactory

. An

RMIFailureHandler

is registered via a call to

RMISocketFacotry.setFailureHandler

. If no failure
handler is installed, the default behavior is to attempt to
re-create the ServerSocket.

**Parameters:**
- ex

- the exception that occurred during

ServerSocket

creation

**Returns:**
- if true, the RMI runtime attempts to retry

ServerSocket

creation

**See Also:**
- RMISocketFactory.setFailureHandler(RMIFailureHandler)

**Since:**
- 1.1

---

### Additional Sections

#### Interface RMIFailureHandler

```java
public interface
RMIFailureHandler
```

An

RMIFailureHandler

can be registered via the

RMISocketFactory.setFailureHandler

call. The

failure

method of the handler is invoked when the RMI
runtime is unable to create a

ServerSocket

to listen
for incoming calls. The

failure

method returns a boolean
indicating whether the runtime should attempt to re-create the

ServerSocket

.

**Since:** 1.1

public interface

RMIFailureHandler

An

RMIFailureHandler

can be registered via the

RMISocketFactory.setFailureHandler

call. The

failure

method of the handler is invoked when the RMI
runtime is unable to create a

ServerSocket

to listen
for incoming calls. The

failure

method returns a boolean
indicating whether the runtime should attempt to re-create the

ServerSocket

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

failure

​(

Exception

ex)

The

failure

callback is invoked when the RMI
runtime is unable to create a

ServerSocket

via the

RMISocketFactory

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

failure

​(

Exception

ex)

The

failure

callback is invoked when the RMI
runtime is unable to create a

ServerSocket

via the

RMISocketFactory

.

---

#### Method Summary

The

failure

callback is invoked when the RMI
runtime is unable to create a

ServerSocket

via the

RMISocketFactory

.

============ METHOD DETAIL ==========

- Method Detail

- failure

```java
boolean failure​(
Exception
ex)
```

The

failure

callback is invoked when the RMI
runtime is unable to create a

ServerSocket

via the

RMISocketFactory

. An

RMIFailureHandler

is registered via a call to

RMISocketFacotry.setFailureHandler

. If no failure
handler is installed, the default behavior is to attempt to
re-create the ServerSocket.

**Parameters:** ex

- the exception that occurred during

ServerSocket

creation
**Returns:** if true, the RMI runtime attempts to retry

ServerSocket

creation
**Since:** 1.1
**See Also:** RMISocketFactory.setFailureHandler(RMIFailureHandler)

Method Detail

- failure

```java
boolean failure​(
Exception
ex)
```

The

failure

callback is invoked when the RMI
runtime is unable to create a

ServerSocket

via the

RMISocketFactory

. An

RMIFailureHandler

is registered via a call to

RMISocketFacotry.setFailureHandler

. If no failure
handler is installed, the default behavior is to attempt to
re-create the ServerSocket.

**Parameters:** ex

- the exception that occurred during

ServerSocket

creation
**Returns:** if true, the RMI runtime attempts to retry

ServerSocket

creation
**Since:** 1.1
**See Also:** RMISocketFactory.setFailureHandler(RMIFailureHandler)

---

#### Method Detail

failure

```java
boolean failure​(
Exception
ex)
```

The

failure

callback is invoked when the RMI
runtime is unable to create a

ServerSocket

via the

RMISocketFactory

. An

RMIFailureHandler

is registered via a call to

RMISocketFacotry.setFailureHandler

. If no failure
handler is installed, the default behavior is to attempt to
re-create the ServerSocket.

**Parameters:** ex

- the exception that occurred during

ServerSocket

creation
**Returns:** if true, the RMI runtime attempts to retry

ServerSocket

creation
**Since:** 1.1
**See Also:** RMISocketFactory.setFailureHandler(RMIFailureHandler)

---

#### failure

boolean failure​(

Exception

ex)

The

failure

callback is invoked when the RMI
runtime is unable to create a

ServerSocket

via the

RMISocketFactory

. An

RMIFailureHandler

is registered via a call to

RMISocketFacotry.setFailureHandler

. If no failure
handler is installed, the default behavior is to attempt to
re-create the ServerSocket.

---

