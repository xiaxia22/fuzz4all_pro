# Interface QuitHandler

**Source:** `java.desktop\java\awt\desktop\QuitHandler.html`

### Class Description

```java
public interface
QuitHandler
```

An implementor determines if requests to quit this application should proceed or cancel.

**Since:** 9
**See Also:** Desktop.setQuitHandler(java.awt.desktop.QuitHandler)

,

Desktop.setQuitStrategy(java.awt.desktop.QuitStrategy)

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void handleQuitRequestWith​(
QuitEvent
e,

QuitResponse
response)

Invoked when the application is asked to quit.

Implementors must call either

QuitResponse.cancelQuit()

,

QuitResponse.performQuit()

, or ensure the application terminates.
The process (or log-out) requesting this app to quit will be blocked until the

QuitResponse

is handled.
Apps that require complex UI to shutdown may call the

QuitResponse

from any thread.
Your app may be asked to quit multiple times before you have responded to the initial request.
This handler is called each time a quit is requested, and the same

QuitResponse

object is passed until it is handled.
Once used, the

QuitResponse

cannot be used again to change the decision.

**Parameters:**
- e

- the request to quit this application.
- response

- the one-shot response object used to cancel or proceed with the quit action.

---

### Additional Sections

#### Interface QuitHandler

```java
public interface
QuitHandler
```

An implementor determines if requests to quit this application should proceed or cancel.

**Since:** 9
**See Also:** Desktop.setQuitHandler(java.awt.desktop.QuitHandler)

,

Desktop.setQuitStrategy(java.awt.desktop.QuitStrategy)

public interface

QuitHandler

An implementor determines if requests to quit this application should proceed or cancel.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

handleQuitRequestWith

​(

QuitEvent

e,

QuitResponse

response)

Invoked when the application is asked to quit.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

handleQuitRequestWith

​(

QuitEvent

e,

QuitResponse

response)

Invoked when the application is asked to quit.

---

#### Method Summary

Invoked when the application is asked to quit.

============ METHOD DETAIL ==========

- Method Detail

- handleQuitRequestWith

```java
void handleQuitRequestWith​(
QuitEvent
e,

QuitResponse
response)
```

Invoked when the application is asked to quit.

Implementors must call either

QuitResponse.cancelQuit()

,

QuitResponse.performQuit()

, or ensure the application terminates.
The process (or log-out) requesting this app to quit will be blocked until the

QuitResponse

is handled.
Apps that require complex UI to shutdown may call the

QuitResponse

from any thread.
Your app may be asked to quit multiple times before you have responded to the initial request.
This handler is called each time a quit is requested, and the same

QuitResponse

object is passed until it is handled.
Once used, the

QuitResponse

cannot be used again to change the decision.

**Parameters:** e

- the request to quit this application.
**Parameters:** response

- the one-shot response object used to cancel or proceed with the quit action.

Method Detail

- handleQuitRequestWith

```java
void handleQuitRequestWith​(
QuitEvent
e,

QuitResponse
response)
```

Invoked when the application is asked to quit.

Implementors must call either

QuitResponse.cancelQuit()

,

QuitResponse.performQuit()

, or ensure the application terminates.
The process (or log-out) requesting this app to quit will be blocked until the

QuitResponse

is handled.
Apps that require complex UI to shutdown may call the

QuitResponse

from any thread.
Your app may be asked to quit multiple times before you have responded to the initial request.
This handler is called each time a quit is requested, and the same

QuitResponse

object is passed until it is handled.
Once used, the

QuitResponse

cannot be used again to change the decision.

**Parameters:** e

- the request to quit this application.
**Parameters:** response

- the one-shot response object used to cancel or proceed with the quit action.

---

#### Method Detail

handleQuitRequestWith

```java
void handleQuitRequestWith​(
QuitEvent
e,

QuitResponse
response)
```

Invoked when the application is asked to quit.

Implementors must call either

QuitResponse.cancelQuit()

,

QuitResponse.performQuit()

, or ensure the application terminates.
The process (or log-out) requesting this app to quit will be blocked until the

QuitResponse

is handled.
Apps that require complex UI to shutdown may call the

QuitResponse

from any thread.
Your app may be asked to quit multiple times before you have responded to the initial request.
This handler is called each time a quit is requested, and the same

QuitResponse

object is passed until it is handled.
Once used, the

QuitResponse

cannot be used again to change the decision.

**Parameters:** e

- the request to quit this application.
**Parameters:** response

- the one-shot response object used to cancel or proceed with the quit action.

---

#### handleQuitRequestWith

void handleQuitRequestWith​(

QuitEvent

e,

QuitResponse

response)

Invoked when the application is asked to quit.

Implementors must call either

QuitResponse.cancelQuit()

,

QuitResponse.performQuit()

, or ensure the application terminates.
The process (or log-out) requesting this app to quit will be blocked until the

QuitResponse

is handled.
Apps that require complex UI to shutdown may call the

QuitResponse

from any thread.
Your app may be asked to quit multiple times before you have responded to the initial request.
This handler is called each time a quit is requested, and the same

QuitResponse

object is passed until it is handled.
Once used, the

QuitResponse

cannot be used again to change the decision.

---

