# Interface JConsoleContext

**Source:** `jdk.jconsole\com\sun\tools\jconsole\JConsoleContext.html`

### Class Description

```java
public interface
JConsoleContext
```

JConsoleContext

represents a JConsole connection to a target
application.

JConsoleContext

notifies any

PropertyChangeListeners

about the

ConnectionState

property change to

CONNECTED

and

DISCONNECTED

.
The

JConsoleContext

instance will be the source for
any generated events.

**Since:** 1.6

---

### Field Details

#### static final
String
CONNECTION_STATE_PROPERTY

The

ConnectionState

bound property name.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### MBeanServerConnection
getMBeanServerConnection()

Returns the

MBeanServerConnection

for the
connection to an application. The returned

MBeanServerConnection

object becomes invalid when
the connection state is changed to the

DISCONNECTED

state.

**Returns:**
- the

MBeanServerConnection

for the
connection to an application.

---

#### JConsoleContext.ConnectionState
getConnectionState()

Returns the current connection state.

**Returns:**
- the current connection state.

---

#### void addPropertyChangeListener​(
PropertyChangeListener
listener)

Add a

PropertyChangeListener

to the listener list.
The listener is registered for all properties.
The same listener object may be added more than once, and will be called
as many times as it is added.
If

listener

is

null

, no exception is thrown and
no action is taken.

**Parameters:**
- listener

- The

PropertyChangeListener

to be added

---

#### void removePropertyChangeListener​(
PropertyChangeListener
listener)

Removes a

PropertyChangeListener

from the listener list. This
removes a

PropertyChangeListener

that was registered for all
properties. If

listener

was added more than once to the same
event source, it will be notified one less time after being removed. If

listener

is

null

, or was never added, no exception is
thrown and no action is taken.

**Parameters:**
- listener

- the

PropertyChangeListener

to be removed

---

### Additional Sections

#### Interface JConsoleContext

```java
public interface
JConsoleContext
```

JConsoleContext

represents a JConsole connection to a target
application.

JConsoleContext

notifies any

PropertyChangeListeners

about the

ConnectionState

property change to

CONNECTED

and

DISCONNECTED

.
The

JConsoleContext

instance will be the source for
any generated events.

**Since:** 1.6

public interface

JConsoleContext

JConsoleContext

represents a JConsole connection to a target
application.

JConsoleContext

notifies any

PropertyChangeListeners

about the

ConnectionState

property change to

CONNECTED

and

DISCONNECTED

.
The

JConsoleContext

instance will be the source for
any generated events.

JConsoleContext

notifies any

PropertyChangeListeners

about the

ConnectionState

property change to

CONNECTED

and

DISCONNECTED

.
The

JConsoleContext

instance will be the source for
any generated events.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

JConsoleContext.ConnectionState

Values for the

ConnectionState

bound property.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

CONNECTION_STATE_PROPERTY

The

ConnectionState

bound property name.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Add a

PropertyChangeListener

to the listener list.

JConsoleContext.ConnectionState

getConnectionState

()

Returns the current connection state.

MBeanServerConnection

getMBeanServerConnection

()

Returns the

MBeanServerConnection

for the
connection to an application.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

JConsoleContext.ConnectionState

Values for the

ConnectionState

bound property.

---

#### Nested Class Summary

Values for the

ConnectionState

bound property.

Field Summary

Fields

Modifier and Type

Field

Description

static

String

CONNECTION_STATE_PROPERTY

The

ConnectionState

bound property name.

---

#### Field Summary

The

ConnectionState

bound property name.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Add a

PropertyChangeListener

to the listener list.

JConsoleContext.ConnectionState

getConnectionState

()

Returns the current connection state.

MBeanServerConnection

getMBeanServerConnection

()

Returns the

MBeanServerConnection

for the
connection to an application.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list.

---

#### Method Summary

Add a

PropertyChangeListener

to the listener list.

Returns the current connection state.

Returns the

MBeanServerConnection

for the
connection to an application.

Removes a

PropertyChangeListener

from the listener list.

============ FIELD DETAIL ===========

- Field Detail

- CONNECTION_STATE_PROPERTY

```java
static final
String
CONNECTION_STATE_PROPERTY
```

The

ConnectionState

bound property name.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getMBeanServerConnection

```java
MBeanServerConnection
getMBeanServerConnection()
```

Returns the

MBeanServerConnection

for the
connection to an application. The returned

MBeanServerConnection

object becomes invalid when
the connection state is changed to the

DISCONNECTED

state.

**Returns:** the

MBeanServerConnection

for the
connection to an application.

- getConnectionState

```java
JConsoleContext.ConnectionState
getConnectionState()
```

Returns the current connection state.

**Returns:** the current connection state.

- addPropertyChangeListener

```java
void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Add a

PropertyChangeListener

to the listener list.
The listener is registered for all properties.
The same listener object may be added more than once, and will be called
as many times as it is added.
If

listener

is

null

, no exception is thrown and
no action is taken.

**Parameters:** listener

- The

PropertyChangeListener

to be added

- removePropertyChangeListener

```java
void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list. This
removes a

PropertyChangeListener

that was registered for all
properties. If

listener

was added more than once to the same
event source, it will be notified one less time after being removed. If

listener

is

null

, or was never added, no exception is
thrown and no action is taken.

**Parameters:** listener

- the

PropertyChangeListener

to be removed

Field Detail

- CONNECTION_STATE_PROPERTY

```java
static final
String
CONNECTION_STATE_PROPERTY
```

The

ConnectionState

bound property name.

**See Also:** Constant Field Values

---

#### Field Detail

CONNECTION_STATE_PROPERTY

```java
static final
String
CONNECTION_STATE_PROPERTY
```

The

ConnectionState

bound property name.

**See Also:** Constant Field Values

---

#### CONNECTION_STATE_PROPERTY

static final

String

CONNECTION_STATE_PROPERTY

The

ConnectionState

bound property name.

Method Detail

- getMBeanServerConnection

```java
MBeanServerConnection
getMBeanServerConnection()
```

Returns the

MBeanServerConnection

for the
connection to an application. The returned

MBeanServerConnection

object becomes invalid when
the connection state is changed to the

DISCONNECTED

state.

**Returns:** the

MBeanServerConnection

for the
connection to an application.

- getConnectionState

```java
JConsoleContext.ConnectionState
getConnectionState()
```

Returns the current connection state.

**Returns:** the current connection state.

- addPropertyChangeListener

```java
void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Add a

PropertyChangeListener

to the listener list.
The listener is registered for all properties.
The same listener object may be added more than once, and will be called
as many times as it is added.
If

listener

is

null

, no exception is thrown and
no action is taken.

**Parameters:** listener

- The

PropertyChangeListener

to be added

- removePropertyChangeListener

```java
void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list. This
removes a

PropertyChangeListener

that was registered for all
properties. If

listener

was added more than once to the same
event source, it will be notified one less time after being removed. If

listener

is

null

, or was never added, no exception is
thrown and no action is taken.

**Parameters:** listener

- the

PropertyChangeListener

to be removed

---

#### Method Detail

getMBeanServerConnection

```java
MBeanServerConnection
getMBeanServerConnection()
```

Returns the

MBeanServerConnection

for the
connection to an application. The returned

MBeanServerConnection

object becomes invalid when
the connection state is changed to the

DISCONNECTED

state.

**Returns:** the

MBeanServerConnection

for the
connection to an application.

---

#### getMBeanServerConnection

MBeanServerConnection

getMBeanServerConnection()

Returns the

MBeanServerConnection

for the
connection to an application. The returned

MBeanServerConnection

object becomes invalid when
the connection state is changed to the

DISCONNECTED

state.

getConnectionState

```java
JConsoleContext.ConnectionState
getConnectionState()
```

Returns the current connection state.

**Returns:** the current connection state.

---

#### getConnectionState

JConsoleContext.ConnectionState

getConnectionState()

Returns the current connection state.

addPropertyChangeListener

```java
void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Add a

PropertyChangeListener

to the listener list.
The listener is registered for all properties.
The same listener object may be added more than once, and will be called
as many times as it is added.
If

listener

is

null

, no exception is thrown and
no action is taken.

**Parameters:** listener

- The

PropertyChangeListener

to be added

---

#### addPropertyChangeListener

void addPropertyChangeListener​(

PropertyChangeListener

listener)

Add a

PropertyChangeListener

to the listener list.
The listener is registered for all properties.
The same listener object may be added more than once, and will be called
as many times as it is added.
If

listener

is

null

, no exception is thrown and
no action is taken.

removePropertyChangeListener

```java
void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list. This
removes a

PropertyChangeListener

that was registered for all
properties. If

listener

was added more than once to the same
event source, it will be notified one less time after being removed. If

listener

is

null

, or was never added, no exception is
thrown and no action is taken.

**Parameters:** listener

- the

PropertyChangeListener

to be removed

---

#### removePropertyChangeListener

void removePropertyChangeListener​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list. This
removes a

PropertyChangeListener

that was registered for all
properties. If

listener

was added more than once to the same
event source, it will be notified one less time after being removed. If

listener

is

null

, or was never added, no exception is
thrown and no action is taken.

---

