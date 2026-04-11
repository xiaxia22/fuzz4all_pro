# Interface Connector.SelectedArgument

**Source:** `jdk.jdi\com\sun\jdi\connect\Connector.SelectedArgument.html`

### Class Description

```java
public static interface
Connector.SelectedArgument

extends
Connector.Argument
```

Specification for and value of a Connector argument,
whose value is a String selected from a list of choices.

**All Superinterfaces:** Connector.Argument

,

Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<
String
> choices()

Return the possible values for the argument

**Returns:**
- List

of

String

---

#### boolean isValid​(
String
value)

Performs basic sanity check of argument.

**Specified by:**
- isValid

in interface

Connector.Argument

**Returns:**
- true

if value is one of

choices()

.

---

### Additional Sections

#### Interface Connector.SelectedArgument

**All Superinterfaces:** Connector.Argument

,

Serializable

**Enclosing interface:** Connector

```java
public static interface
Connector.SelectedArgument

extends
Connector.Argument
```

Specification for and value of a Connector argument,
whose value is a String selected from a list of choices.

public static interface

Connector.SelectedArgument

extends

Connector.Argument

Specification for and value of a Connector argument,
whose value is a String selected from a list of choices.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<

String

>

choices

()

Return the possible values for the argument

boolean

isValid

​(

String

value)

Performs basic sanity check of argument.

- Methods declared in interface com.sun.jdi.connect.

Connector.Argument

description

,

label

,

mustSpecify

,

name

,

setValue

,

value

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<

String

>

choices

()

Return the possible values for the argument

boolean

isValid

​(

String

value)

Performs basic sanity check of argument.

- Methods declared in interface com.sun.jdi.connect.

Connector.Argument

description

,

label

,

mustSpecify

,

name

,

setValue

,

value

---

#### Method Summary

Return the possible values for the argument

Performs basic sanity check of argument.

Methods declared in interface com.sun.jdi.connect.

Connector.Argument

description

,

label

,

mustSpecify

,

name

,

setValue

,

value

---

#### Methods declared in interface com.sun.jdi.connect. Connector.Argument

============ METHOD DETAIL ==========

- Method Detail

- choices

```java
List
<
String
> choices()
```

Return the possible values for the argument

**Returns:** List

of

String

- isValid

```java
boolean isValid​(
String
value)
```

Performs basic sanity check of argument.

**Specified by:** isValid

in interface

Connector.Argument
**Returns:** true

if value is one of

choices()

.

Method Detail

- choices

```java
List
<
String
> choices()
```

Return the possible values for the argument

**Returns:** List

of

String

- isValid

```java
boolean isValid​(
String
value)
```

Performs basic sanity check of argument.

**Specified by:** isValid

in interface

Connector.Argument
**Returns:** true

if value is one of

choices()

.

---

#### Method Detail

choices

```java
List
<
String
> choices()
```

Return the possible values for the argument

**Returns:** List

of

String

---

#### choices

List

<

String

> choices()

Return the possible values for the argument

isValid

```java
boolean isValid​(
String
value)
```

Performs basic sanity check of argument.

**Specified by:** isValid

in interface

Connector.Argument
**Returns:** true

if value is one of

choices()

.

---

#### isValid

boolean isValid​(

String

value)

Performs basic sanity check of argument.

---

