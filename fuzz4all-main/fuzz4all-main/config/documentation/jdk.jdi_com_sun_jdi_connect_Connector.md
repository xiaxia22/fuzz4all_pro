# Interface Connector

**Source:** `jdk.jdi\com\sun\jdi\connect\Connector.html`

### Class Description

```java
public interface
Connector
```

A method of connection between a debugger and a target VM.
A connector encapsulates exactly one

Transport

. used
to establish the connection. Each connector has a set of arguments
which controls its operation. The arguments are stored as a
map, keyed by a string. Each implementation defines the string
argument keys it accepts.

**All Known Subinterfaces:** AttachingConnector

,

LaunchingConnector

,

ListeningConnector

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
name()

Returns a short identifier for the connector. Connector implementors
should follow similar naming conventions as are used with packages
to avoid name collisions. For example, the Sun connector
implementations have names prefixed with "com.sun.jdi.".
Not intended for exposure to end-user.

**Returns:**
- the name of this connector.

---

#### String
description()

Returns a human-readable description of this connector
and its purpose.

**Returns:**
- the description of this connector

---

#### Transport
transport()

Returns the transport mechanism used by this connector to establish
connections with a target VM.

**Returns:**
- the

Transport

used by this connector.

---

#### Map
<
String
,​
Connector.Argument
> defaultArguments()

Returns the arguments accepted by this Connector and their
default values. The keys of the returned map are string argument
names. The values are

Connector.Argument

containing
information about the argument and its default value.

**Returns:**
- the map associating argument names with argument
information and default value.

---

### Additional Sections

#### Interface Connector

**All Known Subinterfaces:** AttachingConnector

,

LaunchingConnector

,

ListeningConnector

```java
public interface
Connector
```

A method of connection between a debugger and a target VM.
A connector encapsulates exactly one

Transport

. used
to establish the connection. Each connector has a set of arguments
which controls its operation. The arguments are stored as a
map, keyed by a string. Each implementation defines the string
argument keys it accepts.

**Since:** 1.3
**See Also:** LaunchingConnector

,

AttachingConnector

,

ListeningConnector

,

Connector.Argument

public interface

Connector

A method of connection between a debugger and a target VM.
A connector encapsulates exactly one

Transport

. used
to establish the connection. Each connector has a set of arguments
which controls its operation. The arguments are stored as a
map, keyed by a string. Each implementation defines the string
argument keys it accepts.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

Connector.Argument

Specification for and value of a Connector argument.

static interface

Connector.BooleanArgument

Specification for and value of a Connector argument,
whose value is Boolean.

static interface

Connector.IntegerArgument

Specification for and value of a Connector argument,
whose value is an integer.

static interface

Connector.SelectedArgument

Specification for and value of a Connector argument,
whose value is a String selected from a list of choices.

static interface

Connector.StringArgument

Specification for and value of a Connector argument,
whose value is a String.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Map

<

String

,​

Connector.Argument

>

defaultArguments

()

Returns the arguments accepted by this Connector and their
default values.

String

description

()

Returns a human-readable description of this connector
and its purpose.

String

name

()

Returns a short identifier for the connector.

Transport

transport

()

Returns the transport mechanism used by this connector to establish
connections with a target VM.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

Connector.Argument

Specification for and value of a Connector argument.

static interface

Connector.BooleanArgument

Specification for and value of a Connector argument,
whose value is Boolean.

static interface

Connector.IntegerArgument

Specification for and value of a Connector argument,
whose value is an integer.

static interface

Connector.SelectedArgument

Specification for and value of a Connector argument,
whose value is a String selected from a list of choices.

static interface

Connector.StringArgument

Specification for and value of a Connector argument,
whose value is a String.

---

#### Nested Class Summary

Specification for and value of a Connector argument.

Specification for and value of a Connector argument,
whose value is Boolean.

Specification for and value of a Connector argument,
whose value is an integer.

Specification for and value of a Connector argument,
whose value is a String selected from a list of choices.

Specification for and value of a Connector argument,
whose value is a String.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Map

<

String

,​

Connector.Argument

>

defaultArguments

()

Returns the arguments accepted by this Connector and their
default values.

String

description

()

Returns a human-readable description of this connector
and its purpose.

String

name

()

Returns a short identifier for the connector.

Transport

transport

()

Returns the transport mechanism used by this connector to establish
connections with a target VM.

---

#### Method Summary

Returns the arguments accepted by this Connector and their
default values.

Returns a human-readable description of this connector
and its purpose.

Returns a short identifier for the connector.

Returns the transport mechanism used by this connector to establish
connections with a target VM.

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

Returns a short identifier for the connector. Connector implementors
should follow similar naming conventions as are used with packages
to avoid name collisions. For example, the Sun connector
implementations have names prefixed with "com.sun.jdi.".
Not intended for exposure to end-user.

**Returns:** the name of this connector.

- description

```java
String
description()
```

Returns a human-readable description of this connector
and its purpose.

**Returns:** the description of this connector

- transport

```java
Transport
transport()
```

Returns the transport mechanism used by this connector to establish
connections with a target VM.

**Returns:** the

Transport

used by this connector.

- defaultArguments

```java
Map
<
String
,​
Connector.Argument
> defaultArguments()
```

Returns the arguments accepted by this Connector and their
default values. The keys of the returned map are string argument
names. The values are

Connector.Argument

containing
information about the argument and its default value.

**Returns:** the map associating argument names with argument
information and default value.

Method Detail

- name

```java
String
name()
```

Returns a short identifier for the connector. Connector implementors
should follow similar naming conventions as are used with packages
to avoid name collisions. For example, the Sun connector
implementations have names prefixed with "com.sun.jdi.".
Not intended for exposure to end-user.

**Returns:** the name of this connector.

- description

```java
String
description()
```

Returns a human-readable description of this connector
and its purpose.

**Returns:** the description of this connector

- transport

```java
Transport
transport()
```

Returns the transport mechanism used by this connector to establish
connections with a target VM.

**Returns:** the

Transport

used by this connector.

- defaultArguments

```java
Map
<
String
,​
Connector.Argument
> defaultArguments()
```

Returns the arguments accepted by this Connector and their
default values. The keys of the returned map are string argument
names. The values are

Connector.Argument

containing
information about the argument and its default value.

**Returns:** the map associating argument names with argument
information and default value.

---

#### Method Detail

name

```java
String
name()
```

Returns a short identifier for the connector. Connector implementors
should follow similar naming conventions as are used with packages
to avoid name collisions. For example, the Sun connector
implementations have names prefixed with "com.sun.jdi.".
Not intended for exposure to end-user.

**Returns:** the name of this connector.

---

#### name

String

name()

Returns a short identifier for the connector. Connector implementors
should follow similar naming conventions as are used with packages
to avoid name collisions. For example, the Sun connector
implementations have names prefixed with "com.sun.jdi.".
Not intended for exposure to end-user.

description

```java
String
description()
```

Returns a human-readable description of this connector
and its purpose.

**Returns:** the description of this connector

---

#### description

String

description()

Returns a human-readable description of this connector
and its purpose.

transport

```java
Transport
transport()
```

Returns the transport mechanism used by this connector to establish
connections with a target VM.

**Returns:** the

Transport

used by this connector.

---

#### transport

Transport

transport()

Returns the transport mechanism used by this connector to establish
connections with a target VM.

defaultArguments

```java
Map
<
String
,​
Connector.Argument
> defaultArguments()
```

Returns the arguments accepted by this Connector and their
default values. The keys of the returned map are string argument
names. The values are

Connector.Argument

containing
information about the argument and its default value.

**Returns:** the map associating argument names with argument
information and default value.

---

#### defaultArguments

Map

<

String

,​

Connector.Argument

> defaultArguments()

Returns the arguments accepted by this Connector and their
default values. The keys of the returned map are string argument
names. The values are

Connector.Argument

containing
information about the argument and its default value.

---

