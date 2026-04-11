# Interface QuitResponse

**Source:** `java.desktop\java\awt\desktop\QuitResponse.html`

### Class Description

```java
public interface
QuitResponse
```

Used to respond to a request to quit the application.

**Since:** 9
**See Also:** Desktop.setQuitHandler(java.awt.desktop.QuitHandler)

,

QuitHandler

,

Desktop.setQuitStrategy(java.awt.desktop.QuitStrategy)

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void performQuit()

Notifies the external quit requester that the quit will proceed, and performs the default

QuitStrategy

.

---

#### void cancelQuit()

Notifies the external quit requester that the user has explicitly canceled the pending quit, and leaves the application running.

Note: this will cancel a pending log-out, restart, or shutdown.

---

### Additional Sections

#### Interface QuitResponse

```java
public interface
QuitResponse
```

Used to respond to a request to quit the application.

**Since:** 9
**See Also:** Desktop.setQuitHandler(java.awt.desktop.QuitHandler)

,

QuitHandler

,

Desktop.setQuitStrategy(java.awt.desktop.QuitStrategy)

public interface

QuitResponse

Used to respond to a request to quit the application.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

cancelQuit

()

Notifies the external quit requester that the user has explicitly canceled the pending quit, and leaves the application running.

void

performQuit

()

Notifies the external quit requester that the quit will proceed, and performs the default

QuitStrategy

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

cancelQuit

()

Notifies the external quit requester that the user has explicitly canceled the pending quit, and leaves the application running.

void

performQuit

()

Notifies the external quit requester that the quit will proceed, and performs the default

QuitStrategy

.

---

#### Method Summary

Notifies the external quit requester that the user has explicitly canceled the pending quit, and leaves the application running.

Notifies the external quit requester that the quit will proceed, and performs the default

QuitStrategy

.

============ METHOD DETAIL ==========

- Method Detail

- performQuit

```java
void performQuit()
```

Notifies the external quit requester that the quit will proceed, and performs the default

QuitStrategy

.

- cancelQuit

```java
void cancelQuit()
```

Notifies the external quit requester that the user has explicitly canceled the pending quit, and leaves the application running.

Note: this will cancel a pending log-out, restart, or shutdown.

Method Detail

- performQuit

```java
void performQuit()
```

Notifies the external quit requester that the quit will proceed, and performs the default

QuitStrategy

.

- cancelQuit

```java
void cancelQuit()
```

Notifies the external quit requester that the user has explicitly canceled the pending quit, and leaves the application running.

Note: this will cancel a pending log-out, restart, or shutdown.

---

#### Method Detail

performQuit

```java
void performQuit()
```

Notifies the external quit requester that the quit will proceed, and performs the default

QuitStrategy

.

---

#### performQuit

void performQuit()

Notifies the external quit requester that the quit will proceed, and performs the default

QuitStrategy

.

cancelQuit

```java
void cancelQuit()
```

Notifies the external quit requester that the user has explicitly canceled the pending quit, and leaves the application running.

Note: this will cancel a pending log-out, restart, or shutdown.

---

#### cancelQuit

void cancelQuit()

Notifies the external quit requester that the user has explicitly canceled the pending quit, and leaves the application running.

Note: this will cancel a pending log-out, restart, or shutdown.

---

