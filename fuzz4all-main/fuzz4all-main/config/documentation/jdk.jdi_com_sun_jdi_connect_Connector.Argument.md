# Interface Connector.Argument

**Source:** `jdk.jdi\com\sun\jdi\connect\Connector.Argument.html`

### Class Description

```java
public static interface
Connector.Argument

extends
Serializable
```

Specification for and value of a Connector argument.
Will always implement a subinterface of Argument:

Connector.StringArgument

,

Connector.BooleanArgument

,

Connector.IntegerArgument

,
or

Connector.SelectedArgument

.

**All Superinterfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
name()

Returns a short, unique identifier for the argument.
Not intended for exposure to end-user.

**Returns:**
- the name of this argument.

---

#### String
label()

Returns a short human-readable label for this argument.

**Returns:**
- a label for this argument

---

#### String
description()

Returns a human-readable description of this argument
and its purpose.

**Returns:**
- the description of this argument

---

#### String
value()

Returns the current value of the argument. Initially, the
default value is returned. If the value is currently unspecified,
null is returned.

**Returns:**
- the current value of the argument.

---

#### void setValue​(
String
value)

Sets the value of the argument.
The value should be checked with

isValid(String)

before setting it; invalid values will throw an exception
when the connection is established - for example,
on

LaunchingConnector.launch(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

---

#### boolean isValid​(
String
value)

Performs basic sanity check of argument.

**Returns:**
- true

if the value is valid to be
used in

setValue(String)

---

#### boolean mustSpecify()

Indicates whether the argument must be specified. If true,

setValue(java.lang.String)

must be used to set a non-null value before
using this argument in establishing a connection.

**Returns:**
- true

if the argument must be specified;

false

otherwise.

---

### Additional Sections

#### Interface Connector.Argument

**All Superinterfaces:** Serializable

**All Known Subinterfaces:** Connector.BooleanArgument

,

Connector.IntegerArgument

,

Connector.SelectedArgument

,

Connector.StringArgument

**Enclosing interface:** Connector

```java
public static interface
Connector.Argument

extends
Serializable
```

Specification for and value of a Connector argument.
Will always implement a subinterface of Argument:

Connector.StringArgument

,

Connector.BooleanArgument

,

Connector.IntegerArgument

,
or

Connector.SelectedArgument

.

public static interface

Connector.Argument

extends

Serializable

Specification for and value of a Connector argument.
Will always implement a subinterface of Argument:

Connector.StringArgument

,

Connector.BooleanArgument

,

Connector.IntegerArgument

,
or

Connector.SelectedArgument

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

description

()

Returns a human-readable description of this argument
and its purpose.

boolean

isValid

​(

String

value)

Performs basic sanity check of argument.

String

label

()

Returns a short human-readable label for this argument.

boolean

mustSpecify

()

Indicates whether the argument must be specified.

String

name

()

Returns a short, unique identifier for the argument.

void

setValue

​(

String

value)

Sets the value of the argument.

String

value

()

Returns the current value of the argument.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

description

()

Returns a human-readable description of this argument
and its purpose.

boolean

isValid

​(

String

value)

Performs basic sanity check of argument.

String

label

()

Returns a short human-readable label for this argument.

boolean

mustSpecify

()

Indicates whether the argument must be specified.

String

name

()

Returns a short, unique identifier for the argument.

void

setValue

​(

String

value)

Sets the value of the argument.

String

value

()

Returns the current value of the argument.

---

#### Method Summary

Returns a human-readable description of this argument
and its purpose.

Performs basic sanity check of argument.

Returns a short human-readable label for this argument.

Indicates whether the argument must be specified.

Returns a short, unique identifier for the argument.

Sets the value of the argument.

Returns the current value of the argument.

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

Returns a short, unique identifier for the argument.
Not intended for exposure to end-user.

**Returns:** the name of this argument.

- label

```java
String
label()
```

Returns a short human-readable label for this argument.

**Returns:** a label for this argument

- description

```java
String
description()
```

Returns a human-readable description of this argument
and its purpose.

**Returns:** the description of this argument

- value

```java
String
value()
```

Returns the current value of the argument. Initially, the
default value is returned. If the value is currently unspecified,
null is returned.

**Returns:** the current value of the argument.

- setValue

```java
void setValue​(
String
value)
```

Sets the value of the argument.
The value should be checked with

isValid(String)

before setting it; invalid values will throw an exception
when the connection is established - for example,
on

LaunchingConnector.launch(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

- isValid

```java
boolean isValid​(
String
value)
```

Performs basic sanity check of argument.

**Returns:** true

if the value is valid to be
used in

setValue(String)

- mustSpecify

```java
boolean mustSpecify()
```

Indicates whether the argument must be specified. If true,

setValue(java.lang.String)

must be used to set a non-null value before
using this argument in establishing a connection.

**Returns:** true

if the argument must be specified;

false

otherwise.

Method Detail

- name

```java
String
name()
```

Returns a short, unique identifier for the argument.
Not intended for exposure to end-user.

**Returns:** the name of this argument.

- label

```java
String
label()
```

Returns a short human-readable label for this argument.

**Returns:** a label for this argument

- description

```java
String
description()
```

Returns a human-readable description of this argument
and its purpose.

**Returns:** the description of this argument

- value

```java
String
value()
```

Returns the current value of the argument. Initially, the
default value is returned. If the value is currently unspecified,
null is returned.

**Returns:** the current value of the argument.

- setValue

```java
void setValue​(
String
value)
```

Sets the value of the argument.
The value should be checked with

isValid(String)

before setting it; invalid values will throw an exception
when the connection is established - for example,
on

LaunchingConnector.launch(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

- isValid

```java
boolean isValid​(
String
value)
```

Performs basic sanity check of argument.

**Returns:** true

if the value is valid to be
used in

setValue(String)

- mustSpecify

```java
boolean mustSpecify()
```

Indicates whether the argument must be specified. If true,

setValue(java.lang.String)

must be used to set a non-null value before
using this argument in establishing a connection.

**Returns:** true

if the argument must be specified;

false

otherwise.

---

#### Method Detail

name

```java
String
name()
```

Returns a short, unique identifier for the argument.
Not intended for exposure to end-user.

**Returns:** the name of this argument.

---

#### name

String

name()

Returns a short, unique identifier for the argument.
Not intended for exposure to end-user.

label

```java
String
label()
```

Returns a short human-readable label for this argument.

**Returns:** a label for this argument

---

#### label

String

label()

Returns a short human-readable label for this argument.

description

```java
String
description()
```

Returns a human-readable description of this argument
and its purpose.

**Returns:** the description of this argument

---

#### description

String

description()

Returns a human-readable description of this argument
and its purpose.

value

```java
String
value()
```

Returns the current value of the argument. Initially, the
default value is returned. If the value is currently unspecified,
null is returned.

**Returns:** the current value of the argument.

---

#### value

String

value()

Returns the current value of the argument. Initially, the
default value is returned. If the value is currently unspecified,
null is returned.

setValue

```java
void setValue​(
String
value)
```

Sets the value of the argument.
The value should be checked with

isValid(String)

before setting it; invalid values will throw an exception
when the connection is established - for example,
on

LaunchingConnector.launch(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

---

#### setValue

void setValue​(

String

value)

Sets the value of the argument.
The value should be checked with

isValid(String)

before setting it; invalid values will throw an exception
when the connection is established - for example,
on

LaunchingConnector.launch(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

isValid

```java
boolean isValid​(
String
value)
```

Performs basic sanity check of argument.

**Returns:** true

if the value is valid to be
used in

setValue(String)

---

#### isValid

boolean isValid​(

String

value)

Performs basic sanity check of argument.

mustSpecify

```java
boolean mustSpecify()
```

Indicates whether the argument must be specified. If true,

setValue(java.lang.String)

must be used to set a non-null value before
using this argument in establishing a connection.

**Returns:** true

if the argument must be specified;

false

otherwise.

---

#### mustSpecify

boolean mustSpecify()

Indicates whether the argument must be specified. If true,

setValue(java.lang.String)

must be used to set a non-null value before
using this argument in establishing a connection.

---

